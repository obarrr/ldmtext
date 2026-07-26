#!/usr/bin/env python3
"""
Extract the 1920 PDF's own embedded (Google-OCR) text layer for one or more
book pages. Extracts the WHOLE page (body + footnote block together) rather
than trying to crop at the footnote divider -- that divider is part of the
scanned image, not a PDF vector object, so there's no reliable geometry to
crop against, and it isn't needed: check_google_crosscheck.py only ever
diffs against the length of the already-transcribed body text, so whatever
of Google's text falls past that point (the footnote block) is naturally
ignored as trailing content, never investigated.

Usage: py extract_google_text.py <book_page> [book_page2 ...]

Writes one file per page to google_text_1920/page_NNNN.txt (NNNN = file_page,
same numbering as pages_1920/), UTF-8 encoded. This is a reference corpus for
check_google_crosscheck.py -- not part of the transcription itself.
"""
import re
import sys
from pathlib import Path

import pdfplumber

BASE_DIR = Path(__file__).parent
PDF_PATH = BASE_DIR / "Libro_de_Mormon 1920.pdf"
OUT_DIR = BASE_DIR / "google_text_1920"
PDF_OFFSET = 22  # book_page + 22 = file_page, for the 1920 edition

# Same running-header pattern as check_line_wrap.py's OCR cross-check, reused
# here to strip the page-number/book-name/chapter-marker header line that
# the body-region crop still catches at the very top of the page.
_HEADER_RE = re.compile(
    r'^.{0,15}(?:LIBRO\s+DE\s+\S+|CAP[IÍ]T[UV]LO|CAP\.\s+[IVX]+).{0,70}$',
    re.I,
)
_WATERMARK = re.compile(r'Digitized\s+by\s+Google', re.I)


def extract_page_text(pdf, file_page: int) -> str:
    page = pdf.pages[file_page - 1]  # pdfplumber is 0-indexed
    text = page.extract_text(x_tolerance=1.5, y_tolerance=3) or ""
    lines = []
    for ln in text.splitlines():
        s = ln.strip()
        if not s or _HEADER_RE.match(s) or _WATERMARK.search(s):
            continue
        lines.append(s)
    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    book_pages = [int(a) for a in sys.argv[1:]]
    OUT_DIR.mkdir(exist_ok=True)

    with pdfplumber.open(PDF_PATH) as pdf:
        for book_page in book_pages:
            file_page = book_page + PDF_OFFSET
            text = extract_page_text(pdf, file_page)
            out_path = OUT_DIR / f"page_{file_page:04d}.txt"
            out_path.write_text(text, encoding="utf-8")
            print(f"book {book_page} (file {file_page}): "
                  f"{len(text)} chars -> {out_path}")


if __name__ == "__main__":
    main()
