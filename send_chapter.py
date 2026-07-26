#!/usr/bin/env python3
"""
Session F helper — extract one chapter from librodm.txt (body text +
its Block 2 footnote entries) into chapters_emailed/<Book>_<N>.txt, and
optionally email it via Outlook COM automation.

Usage:
  py send_chapter.py --next                        # report next chapter, no extraction
  py send_chapter.py <Book> <N> [--no-send]         # extract (+ send unless --no-send)
  py send_chapter.py --next --send                  # extract+send whatever is next
  py send_chapter.py <Book> <N> --to=a@x.com,b@y.com --no-log
                                                     # one-off resend to a custom
                                                     # recipient list without touching
                                                     # the sent-chapters log

<Book> matches the first column of chapter_map.csv, e.g.:
  "1 Nephi" "2 Nephi" Jacob Enos Jarom Omni "Words of Mormon" Mosiah
  Alma Helaman "3 Nephi" "4 Nephi" Mormon Ether Moroni
"""
import csv
import os
import re
import sys
import unicodedata
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
LIBRODM = os.path.join(ROOT, "librodm.txt")
CHAPTER_MAP = os.path.join(ROOT, "chapter_map.csv")
OUT_DIR = os.path.join(ROOT, "chapters_emailed")
LOG_PATH = os.path.join(OUT_DIR, "_log.txt")

RECIPIENTS = ["claudia@theobarrs.com", "obarrr@yahoo.com"]

SMTP_HOST = "mail.theobarrs.com"
SMTP_PORT = 465
SMTP_USERNAME = "robert@theobarrs.com"
CREDENTIAL_SERVICE = "libro_de_mormon_smtp"

# (chapter_map key, display name for subject/body, body-header regex)
BOOK_ORDER = [
    ("1 Nephi", "I Nefi", r"^(PRIMER LIBRO DE NEFI|LIBRO DE I NEFI)\.?,?$"),
    ("2 Nephi", "II Nefi", r"^(SEGUNDO LIBRO DE NEFI|LIBRO DE II NEFI)\.?,?$"),
    ("Jacob", "Jacob", r"^LIBRO DE JACOB\.?$"),
    ("Enos", "Enós", r"^LIBRO DE ENOS\.?$"),
    ("Jarom", "Jarom", r"^LIBRO DE JAROM\.?$"),
    ("Omni", "Omni", r"^LIBRO DE OMNI\.?$"),
    ("Words of Mormon", "Palabras de Mormón", r"^PALABRAS DE MORM[OÓ]N\.?$"),
    ("Mosiah", "Mosíah", r"^LIBRO DE MOS[IÍ]AH\.?$"),
    ("Alma", "Alma", r"^LIBRO DE ALMA\.?$"),
    ("Helaman", "Helamán", r"^LIBRO DE HELAM[AÁ]N\.?$"),
    ("3 Nephi", "III Nefi", r"^(III NEFI|LIBRO DE III NEFI)\.?$"),
    ("4 Nephi", "IV Nefi", r"^(IV NEFI|LIBRO DE IV NEFI)\.?$"),
    ("Mormon", "Mormón", r"^LIBRO DE MORM[OÓ]N\.?$"),
    ("Ether", "Éther", r"^LIBRO DE .THER\.?$"),
    ("Moroni", "Moroni", r"^LIBRO DE MORONI\.?$"),
]
BOOK_KEYS = [b[0] for b in BOOK_ORDER]
BOOK_DISPLAY = {b[0]: b[1] for b in BOOK_ORDER}
BOOK_HEADER_RE = {b[0]: re.compile(b[2]) for b in BOOK_ORDER}


def max_chapter(book_key):
    best = 0
    with open(CHAPTER_MAP, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["book"] == book_key:
                best = max(best, int(row["chapter"]))
    return best


def slugify(display_name):
    norm = unicodedata.normalize("NFKD", display_name)
    ascii_only = norm.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"\s+", "_", ascii_only.strip())


def read_lines():
    with open(LIBRODM, encoding="utf-8") as f:
        return f.readlines()


def find_notas_start(lines):
    for i, line in enumerate(lines):
        if line.rstrip("\n") == "Notas":
            return i
    raise RuntimeError("Could not find 'Notas' marker in librodm.txt")


def find_body_book_positions(lines, notas_start):
    """Return list of (line_index, book_key) for every body-section book
    header found before the Notas section, in file order."""
    positions = []
    for i in range(notas_start):
        stripped = lines[i].rstrip("\n")
        for key, rx in BOOK_HEADER_RE.items():
            if rx.match(stripped):
                positions.append((i, key))
                break
    return positions


def extract_chapter(book_key, chapter_num):
    lines = read_lines()
    notas_start = find_notas_start(lines)
    positions = find_body_book_positions(lines, notas_start)

    book_starts = [p for p in positions if p[1] == book_key]
    if not book_starts:
        raise RuntimeError(
            f"Book '{book_key}' not found in the body of librodm.txt "
            "(not transcribed/integrated yet?)"
        )
    book_start = book_starts[0][0]

    later = [p[0] for p in positions if p[0] > book_start]
    book_end = min(later) if later else notas_start

    chap_re = re.compile(r"^CAP[IÍ]TULO\s+" + str(chapter_num) + r"\.$")
    next_chap_re = re.compile(r"^CAP[IÍ]TULO\s+" + str(chapter_num + 1) + r"\.$")

    chap_start = None
    for i in range(book_start, book_end):
        if chap_re.match(lines[i].rstrip("\n")):
            chap_start = i
            break
    if chap_start is None:
        raise RuntimeError(
            f"'{book_key}' chapter {chapter_num} heading not found "
            "(not transcribed/integrated yet?)"
        )

    chap_end = book_end
    for i in range(chap_start + 1, book_end):
        if next_chap_re.match(lines[i].rstrip("\n")):
            chap_end = i
            break

    chapter_lines = lines[chap_start:chap_end]
    # trim leading/trailing blank lines
    while chapter_lines and chapter_lines[0].strip() == "":
        chapter_lines.pop(0)
    while chapter_lines and chapter_lines[-1].strip() == "":
        chapter_lines.pop()
    chapter_text = "".join(chapter_lines)

    footnote_nums = []
    seen = set()
    for m in re.finditer(r"\[(\d+)\]", chapter_text):
        n = int(m.group(1))
        if n not in seen:
            seen.add(n)
            footnote_nums.append(n)

    entries = parse_notas_entries(lines, notas_start)
    missing = [n for n in footnote_nums if n not in entries]
    if missing:
        raise RuntimeError(f"Footnote number(s) not found in Notas section: {missing}")

    footnote_block = "\n".join(f"{n}: {entries[n].strip()}" for n in sorted(footnote_nums))

    return chapter_text, footnote_block


def parse_notas_entries(lines, notas_start):
    entries = {}
    current_num = None
    header_re = re.compile(r"^[A-ZÁÉÍÓÚÑ0-9 .,'\-]+$")
    entry_re = re.compile(r"^(\d+):\s?(.*)$")
    for line in lines[notas_start + 1:]:
        stripped = line.rstrip("\n")
        m = entry_re.match(stripped)
        if m:
            current_num = int(m.group(1))
            entries[current_num] = m.group(2)
            continue
        if stripped.strip() == "":
            current_num = None
            continue
        if header_re.match(stripped):
            current_num = None
            continue
        if current_num is not None:
            entries[current_num] += " " + stripped.strip()
    return entries


def read_log():
    if not os.path.exists(LOG_PATH):
        return []
    entries = []
    with open(LOG_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("|")
            if len(parts) >= 2:
                entries.append((parts[0], int(parts[1])))
    return entries


def next_chapter():
    log = read_log()
    if not log:
        raise RuntimeError("Log is empty and has no seed entry — specify book+chapter explicitly.")
    last_book, last_chapter = log[-1]
    if last_book not in BOOK_KEYS:
        raise RuntimeError(f"Log's last book '{last_book}' not recognized.")
    idx = BOOK_KEYS.index(last_book)
    last_max = max_chapter(last_book)
    if last_chapter < last_max:
        return last_book, last_chapter + 1
    if idx + 1 >= len(BOOK_KEYS):
        raise RuntimeError("Already at the last book/chapter of the Book of Mormon.")
    return BOOK_KEYS[idx + 1], 1


def append_log(book_key, chapter_num, note=""):
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"{book_key}|{chapter_num}|{date.today().isoformat()}|{note}\n")


def send_email(subject, body, recipients=None):
    import smtplib
    import ssl
    from email.message import EmailMessage

    import keyring

    recipients = recipients or RECIPIENTS

    password = keyring.get_password(CREDENTIAL_SERVICE, SMTP_USERNAME)
    if not password:
        raise RuntimeError(
            f"No stored SMTP credential for {SMTP_USERNAME}. "
            "Run: py setup_email_credentials.py"
        )

    msg = EmailMessage()
    msg["From"] = SMTP_USERNAME
    msg["To"] = ", ".join(recipients)
    msg["Subject"] = subject
    msg.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context) as server:
        server.login(SMTP_USERNAME, password)
        server.send_message(msg)


def main():
    raw_args = sys.argv[1:]
    do_send = "--no-send" not in raw_args
    no_log = "--no-log" in raw_args
    recipients_override = None
    for a in raw_args:
        if a.startswith("--to="):
            recipients_override = [e.strip() for e in a[len("--to="):].split(",") if e.strip()]
    args = [a for a in raw_args if a not in ("--no-send", "--send", "--no-log")
            and not a.startswith("--to=")]

    if args and args[0] == "--next":
        book_key, chapter_num = next_chapter()
        print(f"Next chapter: {BOOK_DISPLAY[book_key]} Capítulo {chapter_num} "
              f"(chapter_map key: '{book_key}')")
        if len(raw_args) == 1:  # truly bare --next, nothing else: report only
            return
    elif len(args) >= 2:
        book_key, chapter_num = args[0], int(args[1])
        if book_key not in BOOK_KEYS:
            print(f"Unknown book '{book_key}'. Valid keys: {BOOK_KEYS}")
            sys.exit(1)
    else:
        print(__doc__)
        sys.exit(1)

    display = BOOK_DISPLAY[book_key]
    chapter_text, footnote_block = extract_chapter(book_key, chapter_num)
    full_text = chapter_text.rstrip("\n") + "\n\n" + footnote_block + "\n"

    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, f"{slugify(display)}_{chapter_num}.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_text)
    print(f"Wrote {out_path}")

    subject = f"{display} Capítulo {chapter_num}"
    send_to = recipients_override or RECIPIENTS
    if do_send:
        send_email(subject, full_text, recipients=send_to)
        print(f"Sent: {subject}  ->  {', '.join(send_to)}")
        if not no_log:
            append_log(book_key, chapter_num)
        else:
            print("--no-log: log not updated")
    else:
        print(f"--no-send: skipped sending '{subject}'")


if __name__ == "__main__":
    main()
