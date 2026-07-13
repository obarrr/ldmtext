#!/usr/bin/env python3
"""
ocr_diag.py -- Show raw Tesseract output for a single page image.
Usage: python ocr_diag.py <edition> <pdf_page_number>
Example: python ocr_diag.py 1920 80
"""
import sys
from pathlib import Path
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = \
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"

BASE_DIR = Path(__file__).parent
LANG = {"1920": "spa", "1879": "eng", "1886": "spa"}

edition  = sys.argv[1]
pdf_pg   = int(sys.argv[2])
lang     = LANG[edition]
img_path = BASE_DIR / f"pages_{edition}" / f"page_{pdf_pg:04d}.png"

print(f"Edition : {edition}")
print(f"Page    : {pdf_pg:04d}")
print(f"Image   : {img_path}")
print(f"Lang    : {lang}")
print(f"Exists  : {img_path.exists()}")
print()
print("=" * 60)
print("RAW OCR OUTPUT (line numbers added):")
print("=" * 60)

text  = pytesseract.image_to_string(Image.open(img_path), lang=lang)
lines = text.splitlines()

import re
CHAP_LINE = {
    "spa": re.compile(r'^\s*CAP[IÍ]T[UVN]LO\s+([IVXLCDM]+|\d+)', re.I),
    "eng": re.compile(r'^\s*CHA[A-Z]{1,5}\s+([IVXLCDM]+|\d+)',    re.I),
}
lang_key = "eng" if edition == "1879" else "spa"

for i, line in enumerate(lines):
    blank_marker = " <-- BLANK" if not line.strip() else ""
    m = CHAP_LINE[lang_key].match(line)
    regex_marker = f" <-- REGEX MATCH ch={m.group(1)}" if m else ""
    print(f"{i:3d}: {repr(line)}{blank_marker}{regex_marker}")
    if m:
        print(f"       CODEPOINTS: {[hex(ord(c)) for c in line.strip()]}")
        before_blank = i > 0 and not lines[i - 1].strip()
        after_blank  = (i + 1 < len(lines)) and not lines[i + 1].strip()
        print(f"       before_blank={before_blank}  after_blank={after_blank}  would_record={before_blank or after_blank}")
