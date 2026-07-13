#!/usr/bin/env python3
"""
ocr_page.py -- Print the full OCR output of a single page, line by line.
Used to diagnose what Tesseract actually produces so detection patterns
can be tuned to match.

Usage:
    python ocr_page.py 1920 25
    python ocr_page.py 1879 14
    python ocr_page.py 1886 22
"""

import sys
from pathlib import Path
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = \
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"

LANG = {"1920": "spa", "1879": "eng", "1886": "spa"}

BASE_DIR = Path(__file__).parent

def main():
    if len(sys.argv) != 3:
        print("Usage: python ocr_page.py <edition> <pdf_page_number>")
        print("  e.g. python ocr_page.py 1920 25")
        sys.exit(1)

    edition = sys.argv[1]
    pdf_pg  = int(sys.argv[2])
    lang    = LANG.get(edition, "spa")

    img_path = BASE_DIR / f"pages_{edition}" / f"page_{pdf_pg:04d}.png"
    if not img_path.exists():
        print(f"Not found: {img_path}")
        sys.exit(1)

    print(f"OCR of [{edition}] page {pdf_pg:04d}  (lang={lang})")
    print(f"File: {img_path}")
    print("-" * 60)

    text  = pytesseract.image_to_string(Image.open(img_path), lang=lang)
    lines = text.splitlines()

    for i, line in enumerate(lines):
        marker = " <--" if line.strip() else ""
        print(f"{i:3d}: {repr(line)}{marker}")

    print("-" * 60)
    print(f"{len(lines)} lines total")

if __name__ == "__main__":
    main()
