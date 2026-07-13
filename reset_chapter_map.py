#!/usr/bin/env python3
"""
reset_chapter_map.py -- Clear all auto-detected values from chapter_map.csv,
keeping only the three manually confirmed anchor values for 1 Nephi chapter 1.

Run this before re-running build_chapter_map.py after a failed or partial scan.
"""

from pathlib import Path
import csv

BASE_DIR = Path(__file__).parent
MAP_FILE = BASE_DIR / "chapter_map.csv"

def main():
    rows = []
    with open(MAP_FILE, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append(dict(row))

    cleared = 0
    for row in rows:
        if int(row["chapter"]) == 1:
            continue   # preserve all chapter 1 (book start) pages
        for ed in ("1920", "1879", "1886"):
            col = f"page_{ed}"
            if row[col].strip():
                row[col] = ""
                cleared += 1

    fieldnames = ["book", "chapter", "page_1920", "page_1879", "page_1886"]
    with open(MAP_FILE, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    print(f"Reset complete. {cleared} values cleared.")
    print("All chapter 1 (book start) pages preserved.")
    print("Now run: python build_chapter_map.py")

if __name__ == "__main__":
    main()
