"""
audit_spot_check.py -- Random spot-check of chapter_map.csv.

For N randomly-chosen chapters, OCRs the recorded start page in each edition
and checks whether the chapter heading found matches the expected chapter number.
Also shows the running header (line 0) for independent confirmation.

Usage:
    py audit_spot_check.py               # 10 random samples, whole book
    py audit_spot_check.py 20            # 20 random samples
    py audit_spot_check.py 10 42         # 10 samples, random seed 42
    py audit_spot_check.py 15 0 --end    # last-third of each book only
"""

import csv
import random
import re
import sys
from pathlib import Path

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

BASE_DIR = Path(__file__).parent
CSV_PATH = BASE_DIR / "chapter_map.csv"

EDITIONS = {
    "1920": {"lang": "spa", "col": "page_1920"},
    "1879": {"lang": "eng", "col": "page_1879"},
    "1886": {"lang": "spa", "col": "page_1886"},
}

# Same regexes as ocr_diag / build_chapter_map
CHAP_RE = {
    "spa": re.compile(r'^\s*CAP[IÍ]T[UVN]LO\s+([IVXLCDM]+|\d+)', re.I),
    "eng": re.compile(r'^\s*CHA[A-Z]{1,5}\s+([IVXLCDM]+|\d+)',    re.I),
}

ROMAN = {
    "I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"VII":7,"VIII":8,"IX":9,"X":10,
    "XI":11,"XII":12,"XIII":13,"XIV":14,"XV":15,"XVI":16,"XVII":17,"XVIII":18,
    "XIX":19,"XX":20,"XXI":21,"XXII":22,"XXIII":23,"XXIV":24,"XXV":25,
    "XXVI":26,"XXVII":27,"XXVIII":28,"XXIX":29,"XXX":30,"XXXI":31,"XXXII":32,
    "XXXIII":33,"XXXIV":34,"XXXV":35,"XXXVI":36,"XXXVII":37,"XXXVIII":38,
    "XXXIX":39,"XL":40,"XLI":41,"XLII":42,"XLIII":43,"XLIV":44,"XLV":45,
    "XLVI":46,"XLVII":47,"XLVIII":48,"XLIX":49,"L":50,"LI":51,"LII":52,
    "LIII":53,"LIV":54,"LV":55,"LVI":56,"LVII":57,"LVIII":58,"LIX":59,
    "LX":60,"LXI":61,"LXII":62,"LXIII":63,
}

def roman_to_int(s):
    return ROMAN.get(s.upper())

def parse_chapter(token):
    """Return integer chapter from Arabic or Roman numeral token."""
    token = token.strip().rstrip(".")
    if token.isdigit():
        return int(token)
    return roman_to_int(token)

def ocr_page(img_path, lang_key):
    """Return (running_header, found_chapter_int_or_None)."""
    text  = pytesseract.image_to_string(Image.open(img_path), lang=lang_key)
    lines = [l for l in text.splitlines()]
    header = lines[0].strip() if lines else ""
    pat = CHAP_RE["eng" if lang_key == "eng" else "spa"]
    for line in lines:
        m = pat.match(line)
        if m:
            ch = parse_chapter(m.group(1))
            if ch:
                return header, ch
    return header, None

def main():
    args      = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags     = [a for a in sys.argv[1:] if     a.startswith("--")]
    n_samples = int(args[0]) if len(args) > 0 else 10
    seed      = int(args[1]) if len(args) > 1 else None
    end_only  = "--end" in flags   # restrict to last third of each book

    all_rows = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["page_1920"] and r["page_1879"] and r["page_1886"]:
                all_rows.append(r)

    if end_only:
        # group by book, keep only the last third of chapters in each book
        from collections import defaultdict
        by_book = defaultdict(list)
        for r in all_rows:
            by_book[r["book"]].append(r)
        rows = []
        for book_rows in by_book.values():
            cutoff = max(1, len(book_rows) * 2 // 3)   # start of last third
            rows.extend(book_rows[cutoff:])
        label = "last-third of each book"
    else:
        rows  = all_rows
        label = "all chapters"

    rng = random.Random(seed)
    samples = rng.sample(rows, min(n_samples, len(rows)))
    print(f"Sampling {len(samples)} chapters from: {label}\n")
    samples.sort(key=lambda r: (r["book"], int(r["chapter"])))

    pass_count = fail_count = 0

    for row in samples:
        book    = row["book"]
        ch_exp  = int(row["chapter"])
        print(f"\n{'='*60}")
        print(f"  {book} ch.{ch_exp}")
        print(f"{'='*60}")

        for ed, info in EDITIONS.items():
            pg   = int(row[info["col"]])
            lang = info["lang"]
            img  = BASE_DIR / f"pages_{ed}" / f"page_{pg:04d}.png"

            header, ch_found = ocr_page(img, lang)

            if ch_found == ch_exp:
                status = "PASS"
                pass_count += 1
            else:
                status = "FAIL"
                fail_count += 1

            found_str = str(ch_found) if ch_found else "not found"
            print(f"  [{ed}] p.{pg:04d}  header: {header[:50]:<50}  "
                  f"body ch: {found_str:<10}  {status}")

    total = pass_count + fail_count
    print(f"\n{'='*60}")
    print(f"  Result: {pass_count}/{total} passed  ({fail_count} failed)")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
