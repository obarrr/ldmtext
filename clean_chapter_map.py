#!/usr/bin/env python3
"""
clean_chapter_map.py -- Remove non-monotonic page values from chapter_map.csv.

A non-monotonic value is one where chapter N's page number is not strictly
greater than chapter N-1's page number for the same book and edition.
These arise from Roman-numeral OCR errors locking in a wrong page number
before the correct page is scanned.

After running this script, re-run build_chapter_map.py to fill the gaps.

Run from the libro_de_mormon_1920 folder:
    python clean_chapter_map.py
"""

import csv
from pathlib import Path

BASE_DIR = Path(__file__).parent
MAP_FILE = BASE_DIR / "chapter_map.csv"

BOOK_SEQUENCE = [
    "1 Nephi", "2 Nephi", "Jacob", "Enos", "Jarom", "Omni",
    "Words of Mormon", "Mosiah", "Alma", "Helaman",
    "3 Nephi", "4 Nephi", "Mormon", "Ether", "Moroni",
]

EDITIONS = ["1920", "1879", "1886"]


def clean_column(rows, col):
    """
    For each book, walk chapters in order.  Keep a page value only if it
    is strictly greater than the last kept value for that book.
    Returns (cleaned_rows, n_cleared).
    """
    last_page = {}   # book -> last accepted page number
    cleared   = 0

    for row in rows:
        book = row["book"]
        val  = row[col].strip()
        if not val:
            continue
        pg = int(val)
        prev = last_page.get(book, 0)
        if pg > prev:
            last_page[book] = pg   # accept
        else:
            row[col] = ""          # reject: not monotonically forward
            cleared += 1

    return rows, cleared


def load_map():
    rows = []
    with open(MAP_FILE, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append(dict(row))
    return rows


def save_map(rows):
    fieldnames = ["book", "chapter", "page_1920", "page_1879", "page_1886"]
    with open(MAP_FILE, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def main():
    rows = load_map()
    total_cleared = 0

    for edition in EDITIONS:
        col = f"page_{edition}"
        rows, n = clean_column(rows, col)
        print(f"  [{edition}] {n} non-monotonic values cleared.")
        total_cleared += n

    save_map(rows)
    print(f"\nSaved. {total_cleared} values cleared total.")
    print("Now re-run build_chapter_map.py to fill the gaps.")


if __name__ == "__main__":
    main()
