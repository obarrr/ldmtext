#!/usr/bin/env python3
"""
verify_fn.py — Cross-check 1920 Spanish footnotes against 1879 English edition.

For each footnote on the specified 1920 page, finds the matching entry in the
1879 English pages for the same chapter and extracts the readable cross-reference
letter, helping resolve garbled superscripts in the 1920 OCR.

Usage:
    py verify_fn.py <book_page> <first_fn> "<book>" <chapter>

    book_page : 1920 book page number (running header), e.g. 442
    first_fn  : first sequential footnote number on this page, e.g. 3201
    book      : book name as in chapter_map.csv, e.g. "Alma" or "Helaman"
    chapter   : chapter number (integer), e.g. 60

Output:
    Printed summary to stdout.
    Full report written to:  extracted pages/page_NNN_fn_check.txt
"""

import csv
import re
import sys
from pathlib import Path

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

BASE_DIR   = Path(__file__).parent
PAGES_1920 = BASE_DIR / "pages_1920"
PAGES_1879 = BASE_DIR / "pages_1879"
OUT_DIR    = BASE_DIR / "extracted pages"
MAP_PATH   = BASE_DIR / "chapter_map.csv"

# chapter_map.csv stores FILE PAGE numbers for all three editions.
# Use chapter_map values directly as file page numbers (no offset needed).
# PDF_OFFSET_1920 is only used to convert the user-supplied BOOK page
# (running header number) to the 1920 file page for the OCR crop.
PDF_OFFSET_1920 = 22   # 1920 file_page = book_page + 22  (verified: book p.441 → page_0463.png)


# ── Chapter map ───────────────────────────────────────────────────────────────

def load_chapter_map():
    rows = []
    with open(MAP_PATH, encoding='utf-8') as f:
        for row in csv.DictReader(f):
            row['chapter']   = int(row['chapter'])
            row['page_1920'] = int(row['page_1920'])
            row['page_1879'] = int(row['page_1879'])
            row['page_1886'] = int(row['page_1886'])
            rows.append(row)
    return rows


def find_chapter(rows, book, chapter):
    for i, row in enumerate(rows):
        if row['book'] == book and row['chapter'] == chapter:
            return i, row
    raise ValueError(f"Not found in chapter_map.csv: {book!r} chapter {chapter}")


def chapter_end_page(rows, idx, edition_key):
    """Return the start page of the NEXT chapter (exclusive upper bound)."""
    if idx + 1 < len(rows):
        return rows[idx + 1][edition_key]
    return rows[idx][edition_key] + 20   # generous tail for the last chapter


# ── Image / OCR helpers ───────────────────────────────────────────────────────

def fn_zoom_crop(img_path, scale=3):
    """Return the footnote strip (bottom 13% of page) at 3× zoom."""
    img = Image.open(img_path)
    w, h = img.size
    fn = img.crop((0, int(h * 0.87), w, h))
    return fn.resize((fn.width * scale, fn.height * scale), Image.LANCZOS)


def tess_ocr(img, lang='spa'):
    return pytesseract.image_to_string(img, lang=lang, config='--psm 6 --oem 3')


# ── Footnote parsing ──────────────────────────────────────────────────────────

_WATERMARK = re.compile(r'Digitized\s+by\s+Google', re.I)


def parse_entries(raw_ocr):
    """Split raw fn_zoom OCR text into individual footnote entry strings."""
    flat = ' '.join(raw_ocr.split())
    flat = _WATERMARK.sub('', flat).strip()
    return [c.strip() for c in re.split(r'\.\s+', flat) if len(c.strip()) > 3]


# ── Reference extraction ──────────────────────────────────────────────────────

_BOOK_NORM = {
    # Spanish (1920) forms
    '1nefi':   '1nephi',  '2nefi':   '2nephi',
    '3nefi':   '3nephi',  '4nefi':   '4nephi',
    'mosíah':  'mosiah',  'helamán': 'helaman',
    'éter':    'ether',
    # English (1879) forms
    '1nephi':  '1nephi',  '2nephi':  '2nephi',
    '3nephi':  '3nephi',  '4nephi':  '4nephi',
    'mosiah':  'mosiah',  'helaman': 'helaman',
    'ether':   'ether',
    # Shared
    'alma':    'alma',    'omni':    'omni',
    'enos':    'enos',    'jarom':   'jarom',
    'jacob':   'jacob',   'moroni':  'moroni',
    'mormon':  'mormon',
    'wordsofmormon': 'wordsofmormon',
}
_KNOWN_BOOKS = set(_BOOK_NORM.values())

# Pattern to strip noise characters before a book name
_NOISE = re.compile(r'^[\W\d_]+')


def _norm_book(raw):
    key = re.sub(r'[\s\W]', '', raw.lower())
    return _BOOK_NORM.get(key, key)


def _fix_chapter(s):
    """Normalise a chapter string: replace trailing/isolated 'l' (OCR for '1')."""
    return re.sub(r'\bl\b', '1', s.replace('l', '1') if re.fullmatch(r'[l]+', s) else s)


def extract_ref(entry):
    """
    Return (norm_book, chapter_str, verse_or_None) from a footnote entry.
    Case-insensitive for 'see'/'Véase'; handles 'l'→'1' OCR confusion in
    chapter numbers (e.g. 'Omni l' → chapter '1').
    Returns None if no recognisable reference found.
    """
    LETTERS = r'[A-ZÁÉÍÓÚÑa-záéíóúñ]'
    BOOK_PAT = fr'({LETTERS}+(?:\s+{LETTERS}+)*)'

    # Direct verse reference: BookName ch:vs  (colon sometimes OCR'd as space+digit)
    m = re.search(fr'{BOOK_PAT}\s+(\d+)\s*[: ]\s*(\d+)', entry)
    if m:
        b = _norm_book(m.group(1))
        if b in _KNOWN_BOOKS:
            return b, m.group(2), m.group(3)

    # Cross-reference: see/Véase [letter(s)], BookName ch
    # Allow fused 'seeh' and lowercase 'see'
    m = re.search(
        fr'(?:see|v[eé]ase)\s*\S*[,\s]+{BOOK_PAT}\s+(\d+|[lI]+)',
        entry, re.I,
    )
    if m:
        b   = _norm_book(m.group(1))
        ch  = _fix_chapter(m.group(2))
        if b in _KNOWN_BOOKS:
            return b, ch, None

    # Plain BookName ch  (catch-all; 'l' may mean '1')
    m = re.search(fr'{BOOK_PAT}\s+(\d+|[lI]+)', entry)
    if m:
        b  = _norm_book(m.group(1))
        ch = _fix_chapter(m.group(2))
        if b in _KNOWN_BOOKS:
            return b, ch, None

    # Fused BookName+chapter like "Omnil" (OCR merges book name and '1')
    m = re.search(fr'{BOOK_PAT}([lI\d]+)\b', entry)
    if m:
        b      = _norm_book(m.group(1))
        ch_raw = m.group(2)
        ch     = ch_raw.replace('l', '1').replace('I', '1')
        if b in _KNOWN_BOOKS and ch.isdigit():
            return b, ch, None

    return None


def extract_fn_letter(entry):
    """
    Extract the footnote's own letter from the start of an entry.
    Handles garbled starts like 'a@,' or 'é,', single ('b,') and
    two-letter codes ('2a,').
    """
    m = re.match(r'^\s*[\W\d_]*([A-Za-z][A-Za-z0-9]?)\s*[,.]', entry.strip())
    return m.group(1) if m else None


def extract_crossref_letter(entry):
    """
    Extract the cross-reference letter after 'See'/'Véase'.
    Case-insensitive; handles fused 'seeh,' (no space after 'see').
    """
    # Fused: "seeh," → cross-ref letter is "h"
    m = re.search(r'(?:see|v[eé]ase)([A-Za-z0-9]{1,3})\s*[,\s]', entry, re.I)
    if m:
        return m.group(1)
    # Space-separated: "see h," or "Véase 2k,"
    m = re.search(r'(?:see|v[eé]ase)\s+([A-Za-z0-9]{1,3})\s*[,\s]', entry, re.I)
    if m:
        return m.group(1)
    return None


def presplit_merged(entries):
    """
    Attempt to split merged 1879 entries such as
    "c, see c, Alma 48, d, Alma 22 3 32"  →  ["c, see c, Alma 48", "d, Alma 22:32"]

    Split pattern: ', [1-2 chars], ' followed by 'see' or a capital letter
    (indicating a new footnote entry starts).
    """
    result = []
    for e in entries:
        # Try splitting at ", [short code], see " or ", [short code], [Capital]"
        parts = re.split(r',\s+(?=[a-z2][a-z]?\s*,\s*(?:see\s|[A-Z]))', e, flags=re.I)
        result.extend(p.strip() for p in parts if len(p.strip()) > 3)
    return result


# ── Reference-based matching ──────────────────────────────────────────────────

def match_by_ref(entries_1920, entries_1879):
    """
    For each 1920 entry, find the best unused 1879 entry with matching
    target book + chapter.  Multiple entries for the same chapter (e.g.
    two for Alma 48) are consumed in order.

    Returns list of (entry_1920, matched_1879_or_None, quality_tag).
    quality_tag: 'ok' | 'no-match' | 'no-ref'
    """
    pool = [(extract_ref(e), e) for e in entries_1879]

    results = []
    for e20 in entries_1920:
        ref20 = extract_ref(e20)
        if ref20 is None:
            results.append((e20, None, 'no-ref'))
            continue
        key20 = (ref20[0], ref20[1])

        found = None
        for j, (ref79, _) in enumerate(pool):
            if ref79 and (ref79[0], ref79[1]) == key20:
                found = j
                break
        if found is not None:
            _, e79 = pool.pop(found)
            results.append((e20, e79, 'ok'))
        else:
            results.append((e20, None, 'no-match'))

    return results


# ── Output formatting ─────────────────────────────────────────────────────────

def format_report(book, chapter, book_page, first_fn,
                  p1879_file_start, p1879_file_end,
                  matches, raw_1920, entries_1879_raw, entries_1879_split):
    out = []
    out.append(f"Footnote verification — {book} {chapter}, 1920 page {book_page}")
    out.append(f"1879 chapter range  : file pages {p1879_file_start}-{p1879_file_end - 1}")
    out.append("=" * 72)
    out.append("")

    for i, (e20, e79, quality) in enumerate(matches):
        letter = chr(ord('a') + i) if i < 26 else f"2{chr(ord('a') + i - 26)}"
        fn_num = first_fn + i

        out.append(f"-- Entry {letter}  [fn {fn_num}] " + "-" * 48)
        out.append(f"  1920 raw : {e20}")

        if quality == 'ok' and e79:
            fn_ltr = extract_fn_letter(e79)
            cr_ltr = extract_crossref_letter(e79)
            out.append(f"  1879 raw : {e79}")
            parts = []
            if fn_ltr:
                parts.append(f"fn letter = [{fn_ltr}]")
            if cr_ltr:
                parts.append(f"cross-ref letter = [{cr_ltr}]")
            out.append("  => " + (", ".join(parts) if parts else "(letters not auto-parsed)"))
        elif quality == 'no-match':
            ref20 = extract_ref(e20)
            ref_str = f"{ref20[0]} {ref20[1]}" if ref20 else "?"
            out.append(f"  1879     : (no match for {ref_str} — see raw list below)")
        else:
            out.append(f"  1879     : (1920 reference not parseable from OCR)")
        out.append("")

    out.append("=" * 72)
    out.append("RAW 1920 fn_zoom OCR:")
    out.append(raw_1920.strip())
    out.append("")
    out.append(f"ALL 1879 chapter entries ({len(entries_1879_raw)} raw parsed, "
               f"{len(entries_1879_split)} after pre-split):")
    for e in entries_1879_split:
        cr = extract_crossref_letter(e) or "?"
        fn = extract_fn_letter(e) or "?"
        out.append(f"  fn=[{fn}]  cr=[{cr}]  raw: {e}")

    return '\n'.join(out)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 5:
        print(__doc__)
        sys.exit(1)

    book_page = int(sys.argv[1])
    first_fn  = int(sys.argv[2])
    book      = sys.argv[3]
    chapter   = int(sys.argv[4])

    our_file_page = book_page + PDF_OFFSET_1920
    print(f"verify_fn.py")
    print(f"  1920 page : {book_page}  (page_{our_file_page:04d}.png)")
    print(f"  book      : {book} chapter {chapter}")
    print(f"  first fn  : {first_fn}")
    print()

    rows = load_chapter_map()
    idx, ch_row = find_chapter(rows, book, chapter)
    p1879_file_start = ch_row['page_1879']
    p1879_file_end   = chapter_end_page(rows, idx, 'page_1879')
    print(f"Chapter map: {book} {chapter}")
    print(f"  1920 chapter starts : file page {ch_row['page_1920']} "
          f"(book page {ch_row['page_1920'] - PDF_OFFSET_1920})")
    print(f"  1879 range          : file pages {p1879_file_start}-{p1879_file_end - 1}")
    print()

    # ── 1920 fn_zoom: only the specified page ─────────────────────────────────
    path_1920 = PAGES_1920 / f"page_{our_file_page:04d}.png"
    if not path_1920.exists():
        print(f"ERROR: {path_1920} not found"); sys.exit(1)
    print(f"[1/3] OCR 1920 fn_zoom: page_{our_file_page:04d}.png")
    raw_1920     = tess_ocr(fn_zoom_crop(path_1920), lang='spa')
    entries_1920 = parse_entries(raw_1920)
    print(f"       {len(entries_1920)} entries parsed")

    # ── 1879 fn_zoom: all chapter pages ───────────────────────────────────────
    print(f"[2/3] OCR 1879 fn_zoom: file pages {p1879_file_start}-{p1879_file_end - 1}")
    entries_1879_raw = []
    for fp in range(p1879_file_start, p1879_file_end):
        path79 = PAGES_1879 / f"page_{fp:04d}.png"
        if not path79.exists():
            continue
        raw79 = tess_ocr(fn_zoom_crop(path79), lang='eng')
        e79   = parse_entries(raw79)
        entries_1879_raw.extend(e79)
        print(f"       page_{fp:04d}.png : {len(e79)} entries")
    entries_1879_split = presplit_merged(entries_1879_raw)
    print(f"       {len(entries_1879_raw)} raw -> {len(entries_1879_split)} after pre-split")

    # ── Reference-based matching ───────────────────────────────────────────────
    print(f"[3/3] Matching by reference...")
    matches = match_by_ref(entries_1920, entries_1879_split)
    n_ok    = sum(1 for *_, q in matches if q == 'ok')
    print(f"       {n_ok}/{len(matches)} matched")
    print()

    report   = format_report(book, chapter, book_page, first_fn,
                             p1879_file_start, p1879_file_end,
                             matches, raw_1920, entries_1879_raw, entries_1879_split)
    out_path = OUT_DIR / f"page_{book_page}_fn_check.txt"
    out_path.write_text(report, encoding='utf-8')

    lines   = report.splitlines()
    raw_sec = next((i for i, l in enumerate(lines) if l.startswith('=====') and i > 5), len(lines))
    for line in lines[:raw_sec + 1]:
        print(line)

    print(f"\nFull report: {out_path.name}")


if __name__ == "__main__":
    main()
