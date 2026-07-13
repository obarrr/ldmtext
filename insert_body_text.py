#!/usr/bin/env python3
"""
Session C: integrate one or more verified page_NNN.txt files into the
master files.

For each page, in the order given:
  1. Insert its body text into librodm.txt immediately before the
     "Notas" line (located by scanning backwards from the end of the
     file), preceded by a blank-line separator, matching the existing
     Pagina-N block convention.
  2. Append its Block 1 footnote entries to the end of librodm_foot.txt.
     Entries are normalized to one space after the colon (the
     established librodm_foot.txt convention). No blank line is
     inserted between entries, including across a same-book chapter
     boundary (rule 20) -- EXCEPT when a footnote's chapter number is
     lower than the previous footnote's, which means a new book of the
     Book of Mormon has started. In that case a blank line, the book
     name (in caps, no trailing punctuation), and another blank line
     are inserted before the new entry. The book name is extracted from
     that page's own body text: the first all-caps title line found
     immediately above the page's "CAPÍTULO 1." heading (walking back
     through any synopsis paragraph and skipping subtitle lines such as
     "HIJO DE ALMA.").

Usage: python insert_body_text.py 441 442 443 444 445 446
       python insert_body_text.py 441 442 --footnotes-only  (body text
           already inserted in an earlier run; only append Block 1)
       python insert_body_text.py 441 442 --body-only  (only insert body
           text; append Block 1 later, e.g. once footnotes still need
           verification but body text is ready to go in)

Note: the book-boundary logic has not yet been exercised against real
data (no page processed so far has crossed a book boundary) -- verify
its output by hand the first time it actually fires.
"""
import io
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PAGES_DIR = "pages"
MASTER = "librodm.txt"
FOOT_MASTER = "librodm_foot.txt"

FN_LINE = re.compile(r'^(\S+,\s+\d+:)(\s*)(.*)$')
VERSE_LINE = re.compile(r'^\d+\.\s')


def load_page_lines(page_num):
    path = f"{PAGES_DIR}/page_{page_num}.txt"
    with open(path, encoding="utf-8") as f:
        return [l.rstrip("\n") for l in f]


def split_page(lines):
    """Return (body_lines, block1_lines) for a page's raw lines."""
    fn_idx = next(i for i, l in enumerate(lines) if FN_LINE.match(l))
    body = lines[:fn_idx]
    while body and body[-1] == "":
        body.pop()

    block1_end = next(
        i for i, l in enumerate(lines[fn_idx:], fn_idx) if l.strip() == ""
    )
    block1 = lines[fn_idx:block1_end]
    return body, block1


def normalize_entry(line):
    m = FN_LINE.match(line)
    if not m:
        return line
    return f"{m.group(1)} {m.group(3)}"


def chapter_of(entry_line):
    ident = entry_line.split(",", 1)[0]
    m = re.match(r'^(\d+)', ident)
    if not m:
        raise ValueError(f"Cannot parse chapter number from entry: {entry_line!r}")
    return int(m.group(1))


def is_caps_title(s):
    s = s.strip()
    if s.startswith("CAPÍTULO") or s.startswith("Página") or s.startswith("Pagina"):
        return False
    letters = [c for c in s if c.isalpha()]
    return bool(letters) and all(c.isupper() for c in letters)


def extract_book_header(body):
    cap1_idx = next(
        (i for i, l in enumerate(body) if l.strip() == "CAPÍTULO 1."), None
    )
    if cap1_idx is None:
        return None

    i = cap1_idx - 1
    while i >= 0 and body[i].strip() == "":
        i -= 1
    if i < 0:
        return None

    if not is_caps_title(body[i]):
        while i >= 0 and body[i].strip() != "" and not is_caps_title(body[i]):
            i -= 1
        while i >= 0 and body[i].strip() == "":
            i -= 1

    last_title = None
    while i >= 0 and is_caps_title(body[i]):
        last_title = body[i].strip()
        i -= 1
        j = i
        while j >= 0 and body[j].strip() == "":
            j -= 1
        if j >= 0 and is_caps_title(body[j]):
            i = j
        else:
            break

    if last_title is None:
        return None
    return last_title.rstrip(".,").strip()


def find_notas_index(lines):
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].strip() == "Notas":
            return i
    raise ValueError("Notas line not found in librodm.txt")


def insert_body_text(page_nums, bodies):
    with open(MASTER, encoding="utf-8") as f:
        lines = [l.rstrip("\n") for l in f]

    notas_idx = find_notas_index(lines)
    prefix = lines[:notas_idx]
    suffix = lines[notas_idx:]

    if prefix and prefix[-1] != "":
        prefix.append("")

    middle = []
    for i, num in enumerate(page_nums):
        if i > 0:
            middle.append("")
        middle.extend(bodies[num])
    middle.append("")

    new_lines = prefix + middle + suffix
    with open(MASTER, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(new_lines) + "\n")


def find_last_chapter(foot_lines):
    for l in reversed(foot_lines):
        if FN_LINE.match(l):
            return chapter_of(l)
    raise ValueError("No existing Block 1 entry found in librodm_foot.txt")


def append_block1(page_nums, bodies, block1s):
    with open(FOOT_MASTER, encoding="utf-8") as f:
        foot_lines = [l.rstrip("\n") for l in f]

    last_chapter = find_last_chapter(foot_lines)
    appended = []

    for num in page_nums:
        for raw in block1s[num]:
            entry = normalize_entry(raw)
            chapter = chapter_of(entry)
            if chapter < last_chapter:
                header = extract_book_header(bodies[num])
                if header is None:
                    raise ValueError(
                        f"Book boundary detected at page {num} entry "
                        f"{entry!r} (chapter {chapter} < {last_chapter}) "
                        f"but no book header found in that page's body text. "
                        f"Resolve manually."
                    )
                appended.append("")
                appended.append(header)
                appended.append("")
            appended.append(entry)
            last_chapter = chapter

    new_lines = foot_lines + appended
    with open(FOOT_MASTER, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(new_lines) + "\n")

    return appended


def main():
    args = sys.argv[1:]
    footnotes_only = "--footnotes-only" in args
    body_only = "--body-only" in args
    page_nums = [a for a in args if not a.startswith("--")]
    if not page_nums or (footnotes_only and body_only):
        print("Usage: python insert_body_text.py NNN [NNN ...] "
              "[--footnotes-only | --body-only]")
        sys.exit(1)

    bodies = {}
    block1s = {}
    for num in page_nums:
        lines = load_page_lines(num)
        body, block1 = split_page(lines)
        bodies[num] = body
        block1s[num] = block1

    if not footnotes_only:
        insert_body_text(page_nums, bodies)
        print(f"Inserted body text for pages: {', '.join(page_nums)}")

    if not body_only:
        appended = append_block1(page_nums, bodies, block1s)
        print(f"Appended {sum(1 for l in appended if l and not l.isupper())} "
              f"Block 1 entries to {FOOT_MASTER}.")
        headers = [l for l in appended if l and l.isupper()]
        if headers:
            print(f"Book boundary header(s) inserted: {', '.join(headers)}")


if __name__ == "__main__":
    main()
