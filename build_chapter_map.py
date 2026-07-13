#!/usr/bin/env python3
"""
build_chapter_map.py -- Populate chapter_map.csv using chapter heading detection.

Prerequisites
-------------
Before running, manually fill in the page_1920, page_1879, and page_1886
columns for chapter 1 of every book in chapter_map.csv.  These 45 values
(15 books x 3 editions) define the scan boundaries.  All page numbers are
PDF page numbers (not book page numbers).

How it works
------------
For each edition and each book:
  1. Read the chapter 1 PDF page from the CSV as the scan start.
  2. Use the next book's chapter 1 page as the scan end.
  3. Scan every page in that range, OCR-ing the full page.
  4. Look for lines matching "CAPÍTULO [ROMAN]." (1920/1886) or
     "CHAPTER [ROMAN]." (1879) that are isolated by blank lines above
     or below -- the signature of a large centered chapter heading.
  5. Record the PDF page of the first occurrence of each chapter number.
  6. Skip any cell already filled in the CSV.

Requirements
------------
    pip install pytesseract pillow
    Tesseract 5.x with Spanish (spa) language pack
"""

import csv
import re
import shutil
import tempfile
import threading
import time
from pathlib import Path
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = \
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"

BASE_DIR    = Path(__file__).parent
MAP_FILE    = BASE_DIR / "chapter_map.csv"
LOCAL_BACKUP = Path(tempfile.gettempdir()) / "chapter_map_backup.csv"

# --- SMB keepalive -------------------------------------------------------
_ka_stop = threading.Event()

def _keepalive(path):
    """Stat the network directory every 30 s to prevent SMB session timeout."""
    while not _ka_stop.wait(30):
        try:
            path.stat()
        except Exception:
            pass
# -------------------------------------------------------------------------

LANG = {"1920": "spa", "1879": "eng", "1886": "spa"}

BOOK_SEQUENCE = [
    "1 Nephi", "2 Nephi", "Jacob", "Enos", "Jarom", "Omni",
    "Words of Mormon", "Mosiah", "Alma", "Helaman",
    "3 Nephi", "4 Nephi", "Mormon", "Ether", "Moroni",
]

# Chapter heading patterns -- match a COMPLETE line that is only the heading.
# CHAP_LINE: heading with a readable number  ("CAPÍTULO 2."  or  "CHAPTER II.")
# CHAP_ANY:  heading word present but number missing or unreadable
#            ("CAPÍTULO ."  or  "CAPÍTULO"  or  "CHAPTER")
#            In this case the chapter number comes from the sequential counter.
CHAP_LINE = {
    # [^a-zA-Z]* allows leading OCR artifacts (e.g. ". CAPÍTULO")
    # CHA/CAP anchor; flex chars cover P->F and U->V misreads
    # [A-Z]+|\d+ captures any letter sequence -- to_int() handles unreadable
    # Roman numerals (e.g. "W" for "XII") by returning None -> counter fallback
    "spa": re.compile(r'^[^a-zA-Z]*CAP[IÍ]T[UVN]LO\s+([A-Z]+|\d+)', re.I),
    "eng": re.compile(r'^[^a-zA-Z]*CHA[A-Z]{1,5}\s+([A-Z]+|\d+)',    re.I),
}
CHAP_ANY = {
    # Allow any non-alphanumeric after the word -- catches corrupted numbers like ">"
    "spa": re.compile(r'^[^a-zA-Z]*CAP[IÍ]T[UVN]LO\s*[^a-zA-Z0-9]*$', re.I),
    "eng": re.compile(r'^[^a-zA-Z]*CHA[A-Z]{1,5}\s*[^a-zA-Z0-9]*$',    re.I),
}
ROMAN_LINE = re.compile(r'^\s*([IVXLCDM]+|\d+)[.\s,;]*$', re.I)

ROMAN = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

def to_int(s):
    s = s.strip().upper()
    if s.isdigit():
        return int(s)
    total, prev = 0, 0
    for ch in reversed(s):
        v = ROMAN.get(ch, 0)
        total += v if v >= prev else -v
        prev = v
    return total if total > 0 else None



def find_chapters_in_range(edition, book, start_pdf, end_pdf):
    """
    Scan PDF pages start_pdf..end_pdf-1 for chapter headings.

    Uses a sequential counter so that chapters whose numbers are physically
    damaged or unreadable in the original can still be assigned correctly.
    When a readable number is found it is cross-checked against the counter;
    a mismatch is flagged but the explicit number takes precedence.

    Returns {chapter_num: first_pdf_page}.
    """
    lang_key  = "eng" if edition == "1879" else "spa"
    lang      = LANG[edition]
    pages_dir = BASE_DIR / f"pages_{edition}"
    results   = {}
    expected  = 2   # chapter 1 already filled from manual entry

    for pdf_pg in range(start_pdf, end_pdf):
        img_path = pages_dir / f"page_{pdf_pg:04d}.png"
        if not img_path.exists():
            continue

        try:
            text = pytesseract.image_to_string(Image.open(img_path), lang=lang)
        except Exception as e:
            print(f"    [{edition}] pdf p.{pdf_pg:04d}: SKIP (image read error: {e})")
            continue
        lines = text.splitlines()

        for i, line in enumerate(lines):
            ch_num    = None
            estimated = False

            # Case 1: heading with readable number -- "CAPÍTULO 2." / "CHAPTER II."
            m = CHAP_LINE[lang_key].match(line)
            if m:
                ch_num = to_int(m.group(1))
                if ch_num is None:
                    # Unreadable OCR (e.g. "W" for "XII") -- use counter
                    ch_num    = expected
                    estimated = True
                elif abs(ch_num - expected) > 15:
                    print(f"    [{edition}] pdf p.{pdf_pg:04d}: "
                          f"SKIP implausible ch.{ch_num} (expected ~{expected})"
                          f" -- OCR corruption, using counter")
                    ch_num    = expected
                    estimated = True
                elif ch_num != expected:
                    print(f"    [{edition}] pdf p.{pdf_pg:04d}: "
                          f"WARNING expected ch.{expected}, found ch.{ch_num}")

            # Case 2: heading word present but number missing or unreadable
            #         ("CAPÍTULO ."  or  bare "CAPÍTULO")
            elif CHAP_ANY[lang_key].match(line):
                # Try the very next non-empty line for a standalone numeral
                for j in range(i + 1, min(len(lines), i + 3)):
                    nxt = lines[j].strip()
                    if not nxt:
                        continue
                    m2 = ROMAN_LINE.match(nxt)
                    if m2:
                        ch_num = to_int(m2.group(1))
                    break
                # Still nothing -- fall back to counter
                if ch_num is None:
                    ch_num    = expected
                    estimated = True

            if ch_num is None:
                continue

            # Blank line on at least one immediately adjacent side
            before_blank = i > 0 and not lines[i - 1].strip()
            after_blank  = (i + 1 < len(lines)) and not lines[i + 1].strip()
            if not (before_blank or after_blank):
                continue

            # If this chapter was already recorded but we're past it,
            # the number is an OCR misread -- use the sequential counter
            if ch_num in results and ch_num < expected and expected not in results:
                ch_num    = expected
                estimated = True

            if ch_num not in results:
                results[ch_num] = pdf_pg
                expected = ch_num + 1
                tag = " (counter)" if estimated else ""
                print(f"    [{edition}] pdf p.{pdf_pg:04d}: "
                      f"{book} ch.{ch_num}{tag}")

    return results


def load_map():
    rows = []
    src = MAP_FILE if MAP_FILE.exists() else LOCAL_BACKUP
    if src == LOCAL_BACKUP:
        print(f"  NOTE: Network CSV unavailable -- loading from local backup: {LOCAL_BACKUP}")
    with open(src, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append(dict(row))
    return rows


def save_map(rows):
    fieldnames = ["book", "chapter", "page_1920", "page_1879", "page_1886"]
    # Always write local backup first (survives network outages)
    with open(LOCAL_BACKUP, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    # Copy to network with up to 5 retries (15 s apart)
    for attempt in range(5):
        try:
            shutil.copy2(LOCAL_BACKUP, MAP_FILE)
            return
        except OSError as e:
            if attempt < 4:
                print(f"  Network save attempt {attempt + 1} failed ({e}), "
                      f"retrying in 15 s...")
                time.sleep(15)
            else:
                print(f"  WARNING: All network save attempts failed.")
                print(f"           Data is safe in local backup: {LOCAL_BACKUP}")


def build_index(rows):
    return {(r["book"], int(r["chapter"])): r for r in rows}


def scan_edition(edition, rows, book_filter=None):
    col   = f"page_{edition}"
    index = build_index(rows)
    filled = 0

    # Gather chapter 1 PDF pages for each book -- these are the range boundaries
    book_starts = {}
    for row in rows:
        if int(row["chapter"]) == 1 and row[col].strip():
            book_starts[row["book"]] = int(row[col])

    if not book_starts:
        print(f"  [{edition}] No chapter 1 pages found in CSV.")
        print(f"           Fill in page_{edition} for ch.1 of every book first.")
        return 0

    missing = [b for b in BOOK_SEQUENCE if b not in book_starts]
    if missing:
        print(f"  [{edition}] Missing ch.1 for: {', '.join(missing)}")
        print(f"           Those books will be skipped.")

    # Order by PDF page so scan ranges are correct
    ordered = sorted(
        [(book, book_starts[book]) for book in BOOK_SEQUENCE if book in book_starts],
        key=lambda x: x[1]
    )

    # Find the actual last PDF page number from the pages folder
    pages_dir = BASE_DIR / f"pages_{edition}"
    all_pages = sorted(pages_dir.glob("page_*.png"))
    last_pdf  = int(all_pages[-1].stem.split("_")[-1]) + 1 if all_pages else 9999

    # Build scan range for every book (needed for end_pdf even when filtering)
    scan_ranges = []
    for idx, (book, start_pdf) in enumerate(ordered):
        end_pdf = ordered[idx + 1][1] if idx + 1 < len(ordered) else last_pdf
        scan_ranges.append((book, start_pdf, end_pdf))

    # Apply book filter
    to_scan = [(b, s, e) for b, s, e in scan_ranges
               if book_filter is None or b == book_filter]

    if book_filter and not to_scan:
        print(f"  [{edition}] Book '{book_filter}' not found in CSV. "
              f"Check spelling against BOOK_SEQUENCE.")
        return 0

    print(f"  [{edition}] Scan ranges:")
    for book, start_pdf, end_pdf in to_scan:
        print(f"    {book:20s}: pdf p.{start_pdf:4d} – {end_pdf - 1:4d}")
    print()

    for book, start_pdf, end_pdf in to_scan:
        print(f"  [{edition}] {book} ...")
        chapter_pages = find_chapters_in_range(edition, book, start_pdf, end_pdf)

        for ch_num, pdf_pg in sorted(chapter_pages.items()):
            key = (book, ch_num)
            if key in index and not index[key][col].strip():
                index[key][col] = str(pdf_pg)
                filled += 1
        print()

    print(f"  [{edition}] {filled} cells filled.")
    return filled


def main():
    import sys
    args = sys.argv[1:]

    # Optional filters: --book "2 Nephi"  --edition 1920
    book_filter    = None
    edition_filter = None
    i = 0
    while i < len(args):
        if args[i] == "--book" and i + 1 < len(args):
            book_filter = args[i + 1]
            i += 2
        elif args[i] == "--edition" and i + 1 < len(args):
            edition_filter = args[i + 1]
            i += 2
        else:
            i += 1

    editions = [edition_filter] if edition_filter else ["1920", "1879", "1886"]

    print("build_chapter_map.py")
    print(f"  Map:     {MAP_FILE}")
    if book_filter:
        print(f"  Book:    {book_filter}")
    if edition_filter:
        print(f"  Edition: {edition_filter}")
    print()

    # Keep SMB session alive during long scans
    _ka_stop.clear()
    ka = threading.Thread(target=_keepalive, args=(BASE_DIR,), daemon=True)
    ka.start()
    print(f"  (keepalive thread started for {BASE_DIR})")
    print()

    rows  = load_map()
    total = 0
    for edition in editions:
        filled = scan_edition(edition, rows, book_filter=book_filter)
        total += filled
        if filled:
            save_map(rows)
            print(f"  (saved after {edition})")
        print()

    _ka_stop.set()
    print(f"Done. {total} cells updated total.")
    print("Run check_chapter_map.py to audit results.")


if __name__ == "__main__":
    main()
