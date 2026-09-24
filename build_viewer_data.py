#!/usr/bin/env python3
"""
Data-extraction layer for the manual-check viewer (viewer/index.html).

Given a book page (an arabic number for the main text, or a lowercase
roman numeral for front matter -- title page, testimonies, table of
contents), produces a JSON-able dict with:
  - book_page, file_page, image path (pages_1920/page_{file_page:04d}.png)
  - body_lines: the page's body text, exactly as it appears between its
    "Pagina N" marker and the next one, from librodm.txt
  - footnotes: the footnote entries actually cited on this page (by [N]
    marker in the body text), pulled from librodm_foot.txt, each with its
    resolved citation text and its chapter-local letter (a, b, c, ...) --
    the same letter printed as the superscript in the source image, since
    footnote numbers run globally but letters restart each chapter.

Front matter ("Pagina i", "Pagina iii", ...) uses a different file-page
offset than the main text (+8, not +22) -- discovered by checking the
actual scanned images, not assumed. Two front-matter pages (ii, vi) are
blank in the original and were never given a "Pagina" marker, so they
have no entry here; page navigation simply skips over them.

Run directly to dump a page's extracted data to stdout for spot-checking:

    py build_viewer_data.py 1
    py build_viewer_data.py 458
    py build_viewer_data.py iii

Run with --all to regenerate viewer/all_pages.js and viewer/chapter_map.js
from the current librodm.txt / librodm_foot.txt / chapter_map.csv -- do
this any time those files change (new pages integrated, corrections made)
so the viewer stays in sync with the master files.

    py build_viewer_data.py --all
"""
import csv
import io
import json
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

MASTER = "librodm.txt"
FOOT_MASTER = "librodm_foot.txt"
FILE_PAGE_OFFSET = 22       # arabic book_page -> file_page
ROMAN_FILE_PAGE_OFFSET = 8  # roman-numeral book_page -> file_page

PAGE_MARKER = re.compile(r'^P[aá]gina ([ivxlcdm]+|\d+)$')
FOOTNOTE_MARKER = re.compile(r'\[(\d+)\]')
FN_LINE = re.compile(r'^(\S+),\s+(\d+):\s*(.*)$')
VERSE_LINE = re.compile(r'^\d+\.\s')

ROMAN_VALUES = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}


def roman_to_int(s):
    s = s.lower()
    total = 0
    prev = 0
    for ch in reversed(s):
        val = ROMAN_VALUES[ch]
        total += -val if val < prev else val
        prev = max(prev, val)
    return total


def _is_caps_title(s):
    s = s.strip()
    if not s or s.startswith("CAPÍTULO") or PAGE_MARKER.match(s):
        return False
    letters = [c for c in s if c.isalpha()]
    return bool(letters) and all(c.isupper() for c in letters)


def _trim_blank_edges(lines):
    while lines and lines[0].strip() == "":
        lines.pop(0)
    while lines and lines[-1].strip() == "":
        lines.pop()
    return lines


def _scan_pages():
    """Single pass over librodm.txt, splitting pages into an arabic dict
    ({int: [lines]}) and a front-matter dict ({roman_label: [lines]}),
    keyed by exactly what follows "Pagina " on each marker line.
    """
    with open(MASTER, encoding="utf-8") as f:
        lines = [l.rstrip("\n") for l in f]

    arabic = {}
    roman = {}
    current_key = None
    is_roman = False
    current_lines = []

    def flush():
        if current_key is None:
            return
        trimmed = _trim_blank_edges(current_lines)
        (roman if is_roman else arabic)[current_key] = trimmed

    for line in lines:
        m = PAGE_MARKER.match(line.strip())
        if m:
            flush()
            label = m.group(1)
            is_roman = not label.isdigit()
            current_key = label if is_roman else int(label)
            current_lines = []
        elif current_key is not None:
            if line.strip() == "Notas":
                flush()
                current_key = None
                current_lines = []
            else:
                current_lines.append(line)
    flush()
    return arabic, roman


def load_body_pages():
    """Return {book_page: [body_lines]} for every arabic page in librodm.txt."""
    arabic, _ = _scan_pages()
    return arabic


def load_front_matter_pages():
    """Return {roman_label: [body_lines]} for every front-matter page."""
    _, roman = _scan_pages()
    return roman


LETTER_SUFFIX = re.compile(r'^\d+([a-zA-Z]+)$')


def load_footnote_entries():
    """Return {sequential_num: {"text": ..., "letter": ...}} from
    librodm_foot.txt. "letter" is the chapter-local letter (a, b, c, ...)
    parsed off the entry's "<chapter><letter>, <num>:" key.
    """
    with open(FOOT_MASTER, encoding="utf-8") as f:
        lines = [l.rstrip("\n") for l in f]

    entries = {}
    current_num = None
    current_letter = None
    current_text = []

    def flush():
        if current_num is not None:
            entries[current_num] = {
                "text": " ".join(current_text).strip(),
                "letter": current_letter,
            }

    for line in lines:
        m = FN_LINE.match(line.strip())
        if m:
            flush()
            key = m.group(1)
            lm = LETTER_SUFFIX.match(key)
            current_letter = lm.group(1) if lm else None
            current_num = int(m.group(2))
            current_text = [m.group(3)]
        elif line.strip() == "" or _is_caps_title(line):
            flush()
            current_num = None
            current_letter = None
            current_text = []
        elif current_num is not None:
            current_text.append(line.strip())
    flush()
    return entries


def build_entry(book_page, file_page, body_lines, foot_entries):
    nums = sorted({int(n) for l in body_lines for n in FOOTNOTE_MARKER.findall(l)})

    first_verse_line_idx = next(
        (i for i, l in enumerate(body_lines) if VERSE_LINE.match(l)), None
    )

    footnotes = []
    missing = []
    for n in nums:
        entry = foot_entries.get(n)
        if entry is None:
            missing.append(n)
            continue
        footnotes.append({
            "num": n,
            "letter": entry["letter"],
            "text": entry["text"],
            "chars": len(entry["text"]),
        })

    return {
        "book_page": book_page,
        "file_page": file_page,
        "image": f"pages_1920/page_{file_page:04d}.png",
        "body_lines": body_lines,
        "first_verse_line_idx": first_verse_line_idx,
        "footnotes": footnotes,
        "missing_footnotes": missing,
    }


def get_page_data(book_page, body_pages=None, foot_entries=None):
    body_pages = body_pages if body_pages is not None else load_body_pages()
    foot_entries = foot_entries if foot_entries is not None else load_footnote_entries()
    body_lines = body_pages.get(book_page, [])
    return build_entry(book_page, book_page + FILE_PAGE_OFFSET, body_lines, foot_entries)


def get_front_matter_data(label, front_pages=None, foot_entries=None):
    front_pages = front_pages if front_pages is not None else load_front_matter_pages()
    foot_entries = foot_entries if foot_entries is not None else load_footnote_entries()
    body_lines = front_pages.get(label, [])
    file_page = roman_to_int(label) + ROMAN_FILE_PAGE_OFFSET
    return build_entry(label, file_page, body_lines, foot_entries)


# Calibration values already hand-tuned in the viewer for specific pages --
# preserved here so a fresh --all dump doesn't lose that work. Everything
# else gets the naive default guess below, to be tuned live in the viewer.
# NOTE: the viewer itself persists per-page calibration in the browser's
# localStorage once you adjust a page's markers there, which takes
# precedence over these guesses -- this dict only matters for a page that
# has never been calibrated in any browser yet.
TUNED_CALIBRATION = {
    1: {"divider_guess": 0.89, "verse1_guess": 0.635},
    458: {"divider_guess": 0.865, "verse1_guess": 0.105},
}
DEFAULT_DIVIDER_GUESS = 0.88


def add_calibration_guess(data):
    tuned = TUNED_CALIBRATION.get(data["book_page"])
    if tuned:
        data.update(tuned)
        data.setdefault("foot_end_guess", 1.0)
        return data

    data["divider_guess"] = DEFAULT_DIVIDER_GUESS
    # Default assumes footnote text runs to the image's physical bottom
    # edge -- usually wrong (there's typically blank margin below the last
    # footnote line), but the viewer's "Footnote end" marker lets it be
    # corrected per page without disturbing the body/footnote divider.
    data["foot_end_guess"] = 1.0
    idx = data["first_verse_line_idx"]
    total = len(data["body_lines"])
    if not idx or total == 0:
        data["verse1_guess"] = 0.0
    else:
        # Naive starting point: assumes uniform line height, which is
        # exactly wrong for heading/synopsis text -- just gives the viewer
        # something closer than 0 to start dragging from.
        data["verse1_guess"] = round((idx / total) * DEFAULT_DIVIDER_GUESS, 3)
    return data


def _ordered_labels(front_pages, body_pages):
    """Full document order: front matter (i, iii, iv, ...) then arabic
    (1, 2, 3, ...). Used to assign a purely-numeric "order" field so the
    viewer's prev/next buttons don't need to know about roman numerals.
    """
    return sorted(front_pages, key=roman_to_int) + sorted(body_pages)


def dump_all_pages(out_path):
    body_pages = load_body_pages()
    front_pages = load_front_matter_pages()
    foot_entries = load_footnote_entries()

    pages = []
    for label in sorted(front_pages, key=roman_to_int):
        data = get_front_matter_data(label, front_pages, foot_entries)
        add_calibration_guess(data)
        pages.append(data)
    for bp in sorted(body_pages):
        data = get_page_data(bp, body_pages, foot_entries)
        add_calibration_guess(data)
        pages.append(data)

    for i, p in enumerate(pages):
        p["order"] = i

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("const ALL_PAGES = ")
        json.dump(pages, f, ensure_ascii=False)
        f.write(";\n")
    print(f"Wrote {len(pages)} pages to {out_path} "
          f"({len(front_pages)} front matter + {len(body_pages)} body)")


def dump_chapter_map(csv_path, out_path):
    body_pages = load_body_pages()
    front_pages = load_front_matter_pages()
    order_by_label = {
        str(label): i for i, label in enumerate(_ordered_labels(front_pages, body_pages))
    }

    chapters = []
    for label in sorted(front_pages, key=roman_to_int):
        chapters.append({
            "book": "Front Matter",
            "chapter": label,
            "book_page": label,
            "order": order_by_label[label],
            "label_text": f"Page {label}",
        })

    with open(csv_path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        book_page = int(r["page_1920"]) - FILE_PAGE_OFFSET
        chapters.append({
            "book": r["book"],
            "chapter": int(r["chapter"]),
            "book_page": book_page,
            "order": order_by_label[str(book_page)],
        })

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("const CHAPTER_MAP = ")
        json.dump(chapters, f, ensure_ascii=False)
        f.write(";\n")
    print(f"Wrote {len(chapters)} chapters to {out_path} "
          f"(incl. {len(front_pages)} front matter)")


def main():
    if len(sys.argv) < 2:
        print("Usage: py build_viewer_data.py NNN [NNN ...] | i | iii | ...")
        print("       py build_viewer_data.py --all")
        sys.exit(1)

    if sys.argv[1] == "--all":
        dump_all_pages("viewer/all_pages.js")
        dump_chapter_map("chapter_map.csv", "viewer/chapter_map.js")
        return

    body_pages = load_body_pages()
    front_pages = load_front_matter_pages()
    foot_entries = load_footnote_entries()

    for arg in sys.argv[1:]:
        if arg.isdigit():
            data = get_page_data(int(arg), body_pages, foot_entries)
        else:
            data = get_front_matter_data(arg.lower(), front_pages, foot_entries)
        print(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
