#!/usr/bin/env python3
"""
mini_test.py -- End-to-end simulation of build_chapter_map.py
for a small page range.  Does NOT write to chapter_map.csv.
"""
import csv, re
from pathlib import Path
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = \
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"

BASE_DIR  = Path(__file__).parent
MAP_FILE  = BASE_DIR / "chapter_map.csv"
EDITION   = "1920"
BOOK      = "2 Nephi"
START_PDF = 80
END_PDF   = 96   # exclusive -- pages 80-95
LANG      = "spa"
LANG_KEY  = "spa"
COL       = f"page_{EDITION}"

CHAP_LINE = {
    "spa": re.compile(r'^\s*CAP[IÍ]TULO\s+([IVXLCDM]+|\d+)[.\s,;]*$', re.I),
    "eng": re.compile(r'^\s*CHAPTER\s+([IVXLCDM]+|\d+)[.\s,;]*$',      re.I),
}
CHAP_ANY = {
    "spa": re.compile(r'^\s*CAP[IÍ]TULO\s*[.\s,;]*$', re.I),
    "eng": re.compile(r'^\s*CHAPTER\s*[.\s,;]*$',      re.I),
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

# Load CSV and build index
rows = []
with open(MAP_FILE, newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        rows.append(dict(row))
index = {(r["book"], int(r["chapter"])): r for r in rows}

print(f"Scanning {BOOK} pages {START_PDF}–{END_PDF-1} ({EDITION})")
print()

pages_dir = BASE_DIR / f"pages_{EDITION}"
results   = {}
expected  = 2

for pdf_pg in range(START_PDF, END_PDF):
    img_path = pages_dir / f"page_{pdf_pg:04d}.png"
    if not img_path.exists():
        print(f"  p.{pdf_pg:04d}: FILE NOT FOUND")
        continue

    text  = pytesseract.image_to_string(Image.open(img_path), lang=LANG)
    lines = text.splitlines()

    for i, line in enumerate(lines):
        ch_num = None

        m = CHAP_LINE[LANG_KEY].match(line)
        if m:
            ch_num = to_int(m.group(1))
        elif CHAP_ANY[LANG_KEY].match(line):
            for j in range(i + 1, min(len(lines), i + 3)):
                nxt = lines[j].strip()
                if not nxt:
                    continue
                m2 = ROMAN_LINE.match(nxt)
                if m2:
                    ch_num = to_int(m2.group(1))
                break
            if ch_num is None:
                ch_num = expected

        if ch_num is None:
            continue

        before_blank = i > 0 and not lines[i - 1].strip()
        after_blank  = (i + 1 < len(lines)) and not lines[i + 1].strip()
        if not (before_blank or after_blank):
            print(f"  p.{pdf_pg:04d}: found ch.{ch_num} BUT no adjacent blank line -- SKIPPED")
            continue

        if ch_num not in results:
            results[ch_num] = pdf_pg
            expected = ch_num + 1
            print(f"  p.{pdf_pg:04d}: found ch.{ch_num}  (before_blank={before_blank}  after_blank={after_blank})")

print()
print("Chapters found:", sorted(results.keys()))
print()
print("Write simulation:")
would_write = 0
for ch_num, pdf_pg in sorted(results.items()):
    key = (BOOK, ch_num)
    if key in index:
        current = index[key][COL].strip()
        if not current:
            print(f"  WOULD WRITE: {BOOK} ch.{ch_num} -> p.{pdf_pg}")
            would_write += 1
        else:
            print(f"  SKIP (already filled={current}): {BOOK} ch.{ch_num} -> p.{pdf_pg}")
    else:
        print(f"  KEY NOT IN INDEX: {key}")
print()
print(f"Total would-write: {would_write}")
