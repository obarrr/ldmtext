#!/usr/bin/env python3
"""
Line-wrap fidelity backstop for a completed page text file.

Rules 5/6 require every body-text line break to be read directly from the
1920 page image, never approximated or reflowed to a target width. Unlike
the length/hyphen checks in check_lines.py, nothing previously caught a
page whose line breaks were reflowed to an even width instead of copied
from the image, as long as it happened to stay under 72 chars (confirmed
failure mode: page 475, 2026-07-19 — every line was rewritten to a ~72-
char target with zero relationship to the image's actual line endings).

This script is an ADVISORY cross-check, not a source of truth: it OCRs
the page image with Tesseract purely to get an approximate independent
line count and length profile, and flags a page whose body text looks
suspiciously different from what real 1920 justified type produces. A
warning here means "go re-verify against the image," not "this is wrong"
— and a clean report does not by itself prove every line break is
correct. It is not a substitute for reading the image line-by-line
per rules 5/6; check_lines.py's overlength/hyphen checks still apply
on top of this.

Usage: py check_line_wrap.py <book_page> <page_txt_path>
"""
import re
import statistics
import sys
from pathlib import Path

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

BASE_DIR = Path(__file__).parent
PAGES_DIR = BASE_DIR / "pages_1920"
PDF_OFFSET = 22  # book_page + 22 = file_page, for the 1920 edition

_HEADER_RE = re.compile(
    r'^.{0,15}(?:LIBRO\s+DE\s+\S+|CAP[IÍ]T[UV]LO|CAP\.\s+[IVX]+).{0,70}$',
    re.I,
)
_WATERMARK = re.compile(r'Digitized\s+by\s+Google', re.I)


def ocr_body_lines(book_page: int) -> list:
    """OCR the body region (top 87%) of the page image; return non-blank lines."""
    file_page = book_page + PDF_OFFSET
    img_path = PAGES_DIR / f"page_{file_page:04d}.png"
    if not img_path.exists():
        print(f"WARNING: image not found ({img_path}) — skipping OCR cross-check.")
        return None
    img = Image.open(img_path)
    w, h = img.size
    body = img.crop((0, 0, w, int(h * 0.87)))
    raw = pytesseract.image_to_string(body, lang="spa", config="--psm 6 --oem 3")
    lines = []
    for ln in raw.replace('\x0c', '').splitlines():
        s = ln.strip()
        if not s or _HEADER_RE.match(s) or _WATERMARK.search(s):
            continue
        lines.append(s)
    return lines


def txt_body_lines(path: str) -> list:
    """Return the body-text lines of page_NNN.txt: after 'Página N', up to
    the first blank line (i.e. before Block 1 / footnotes)."""
    with open(path, encoding="utf-8") as f:
        lines = [l.rstrip("\n") for l in f]
    start = 1 if lines and lines[0].startswith("Página") else 0
    body = []
    for l in lines[start:]:
        if l.strip() == "":
            break
        body.append(l)
    return body


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    book_page = int(sys.argv[1])
    txt_path = sys.argv[2]

    txt_lines = txt_body_lines(txt_path)
    txt_count = len(txt_lines)
    lengths = [len(l) for l in txt_lines]

    print(f"page_{book_page} body lines in {txt_path}: {txt_count}")
    if lengths:
        print(f"  length range: {min(lengths)}-{max(lengths)} chars, "
              f"mean {statistics.mean(lengths):.1f}, "
              f"stdev {statistics.pstdev(lengths):.1f}")
        short = sum(1 for n in lengths if n < 50)
        print(f"  lines under 50 chars: {short} "
              f"(real justified type usually has several per page — verse "
              f"ends, short exclamations, etc.; near-zero short lines with "
              f"a narrow length range is a reflow red flag)")

    ocr_lines = ocr_body_lines(book_page)
    if ocr_lines is not None:
        ocr_count = len(ocr_lines)
        diff = txt_count - ocr_count
        print(f"\nTesseract OCR body line count (rough, advisory only): {ocr_count}")
        print(f"Difference (txt - ocr): {diff:+d}")
        if abs(diff) > 1:
            print(
                "  <-- FLAG: line count differs from the OCR estimate by "
                "more than 1. This is only a rough cross-check (OCR can "
                "mis-split or merge lines on its own), but a gap this size "
                "warrants re-reading the top/mid/bot image crops line by "
                "line and confirming each output line ends where the image "
                "ends it (rules 5/6), not just that it's under 72 chars."
            )
        else:
            print("  OCR count is close to the file's line count — no red flag, "
                  "but this does not substitute for the per-line image check.")

    print(
        "\nReminder: this script cannot tell you a line break is in the "
        "WRONG place if the resulting line count and lengths happen to look "
        "plausible. It only catches gross reflow. The actual rule 5/6 "
        "requirement is to read every line ending from the image crop."
    )


if __name__ == "__main__":
    main()
