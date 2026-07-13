#!/usr/bin/env python3
"""
draft_page.py — Generate a draft page_NNN_draft.txt for editor review.

Combines Google OCR (pdftotext) and Tesseract OCR on the pre-rasterized
1920 page image, votes word-by-word, applies correction rules, and parses
Block 1 footnote entries from the fn_zoom crop.

Usage:
    py draft_page.py <book_page> <first_fn> <chapter>

    book_page  : page number shown in running header (e.g. 442)
    first_fn   : first sequential footnote number on this page (e.g. 3201)
    chapter    : chapter number for Block 1 prefix (e.g. 4)

Output:
    extracted pages/page_NNN_draft.txt

The draft contains:
  - Body text (Tesseract OCR, image line-breaks preserved, corrections applied)
  - Block 1 footnote entries parsed from fn_zoom (verify letters against image)
  - Auto-generated Corrections log entries
  - REVIEW section: Google vs Tesseract conflict list with context, long lines

After review:
  - Work through conflict list; fix body text words from image where needed
  - Insert [N] footnote markers in body text using fn_zoom image
  - Verify line endings against image crops
  - Rename to page_NNN.txt and run check_lines.py
"""

import os
import re
import sys
import difflib
from pathlib import Path
from PIL import Image
import pytesseract
import pdfplumber

# ── Paths ──────────────────────────────────────────────────────────────────────
pytesseract.pytesseract.tesseract_cmd = \
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"

BASE_DIR  = Path(__file__).parent
PAGES_DIR = BASE_DIR / "pages_1920"
OUT_DIR   = BASE_DIR / "extracted pages"
PDF_1920  = BASE_DIR / "Libro_de_Mormon 1920.pdf"

# PDF file page number = book page number + this offset.
# Verified: book p.442 = pages_1920/page_0464.png  (464 - 442 = 22).
PDF_OFFSET = 22


# ── Crop generation ────────────────────────────────────────────────────────────
def make_crops(book_page: int) -> dict:
    """Load pre-rasterized image and return dict of PIL Image crops."""
    pdf_page = book_page + PDF_OFFSET
    img_path = PAGES_DIR / f"page_{pdf_page:04d}.png"
    if not img_path.exists():
        raise FileNotFoundError(f"Pre-rasterized image not found: {img_path}")
    img = Image.open(img_path)
    w, h = img.size
    fn_img = img.crop((0, int(h * 0.87), w, h))
    return {
        "body":    img.crop((0, 0, w, int(h * 0.87))),
        "fn":      fn_img,
        "fn_zoom": fn_img.resize(
            (fn_img.width * 3, fn_img.height * 3), Image.LANCZOS
        ),
    }


# ── OCR sources ────────────────────────────────────────────────────────────────
def google_ocr(book_page: int) -> str:
    """
    Extract the Google OCR text layer for the body region of one book page.

    Uses pdfplumber's within_bbox() to crop to the top 87% of the page —
    the same region used for the Tesseract body crop — so that footnotes
    are excluded without relying on text-pattern heuristics.
    """
    pdf_page = book_page + PDF_OFFSET
    try:
        with pdfplumber.open(str(PDF_1920)) as pdf:
            page = pdf.pages[pdf_page - 1]          # 0-based index
            w = float(page.width)
            h = float(page.height)
            body = page.within_bbox((0, 0, w, h * 0.87))
            return body.extract_text(x_tolerance=2, y_tolerance=3) or ""
    except Exception as e:
        print(f"  [pdfplumber] {e}", file=sys.stderr)
        return ""


def tess_ocr(img: Image.Image, psm: int = 6) -> str:
    """Run Tesseract (Spanish) on a PIL Image and return raw text."""
    try:
        return pytesseract.image_to_string(
            img, lang="spa", config=f"--psm {psm} --oem 3"
        )
    except Exception as e:
        print(f"  [tesseract] {e}", file=sys.stderr)
        return ""


# ── Text cleaning ──────────────────────────────────────────────────────────────
_HEADER_RE = re.compile(
    r'^.{0,15}(?:LIBRO\s+DE\s+\S+|CAP[IÍ]T[UV]LO|CAP\.\s+[IVX]+).{0,70}$',
    re.I | re.M
)
_WATERMARK   = re.compile(r'Digitized\s+by\s+Google', re.I)
_MULTI_BLANK = re.compile(r'\n{3,}')


def clean(text: str) -> str:
    """Strip headers, watermark, form feeds; normalise blank lines."""
    text = text.replace('\x0c', '')
    text = _HEADER_RE.sub('', text)
    text = _WATERMARK.sub('', text)
    text = _MULTI_BLANK.sub('\n\n', text)
    return text.strip()


def strip_footnotes(text: str) -> str:
    """
    Return only the body text — everything before the footnote section.

    Primary heuristic: find the last numbered verse line (e.g. "12. Y vino…"),
    then take through the end of that paragraph.  This works for both Google
    OCR (where footnote letters are garbled) and Tesseract.
    Fallback: look for a line starting with a letter/code and comma ("a, ").
    """
    lines = text.splitlines()

    # Primary: scan backwards for the last line that starts a numbered verse
    last_verse_start = None
    for i in range(len(lines) - 1, -1, -1):
        if re.match(r'^\s*\d+\.\s', lines[i]):
            last_verse_start = i
            break

    if last_verse_start is not None:
        # Extend to the end of that verse's paragraph (stop at blank line or
        # at the start of a line that looks like a footnote entry)
        cut = len(lines)
        for j in range(last_verse_start + 1, len(lines)):
            s = lines[j].strip()
            if not s:
                cut = j
                break
            if re.match(r'^([a-z]|\d[a-z]{1,2}),\s', s, re.I):
                cut = j
                break
        return '\n'.join(lines[:cut]).strip()

    # Fallback: letter-comma heuristic
    for i, line in enumerate(lines):
        if re.match(r'^\s*([a-z]|\d[a-z]{1,2}),\s', line, re.I):
            return '\n'.join(lines[:i]).strip()

    return text.strip()


# ── Word-level conflict detection ─────────────────────────────────────────────
def _norm(word: str) -> str:
    """Lowercase and strip punctuation for comparison."""
    return re.sub(r'[^\wÀ-ɏ]', '', word.lower())


def find_conflicts(google_body: str, tess_body: str) -> list:
    """
    Align two OCR texts word-by-word via difflib SequenceMatcher.

    Returns a list of dicts, one per disagreeing segment:
      {
        'google':  the Google word(s)  (or '[missing]')
        'tess':    the Tesseract word(s) (or '[missing]')
        'context': up to 4 Tesseract words of surrounding context
      }

    The body text is NOT modified here — Tesseract's text is used as-is so
    its image-derived line breaks are preserved.  The conflict list is
    appended to the REVIEW section at the bottom of the draft.
    """
    g_words = google_body.split()
    t_words = tess_body.split()

    sm = difflib.SequenceMatcher(
        None,
        [_norm(w) for w in g_words],
        [_norm(w) for w in t_words],
        autojunk=False,
    )

    conflicts = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            continue
        gw = ' '.join(g_words[i1:i2]) if i1 < i2 else '[missing]'
        tw = ' '.join(t_words[j1:j2]) if j1 < j2 else '[missing]'
        # 2 words of context on either side from Tesseract
        ctx_l = ' '.join(t_words[max(0, j1 - 2):j1])
        ctx_r = ' '.join(t_words[j2:min(len(t_words), j2 + 2)])
        ctx   = ('…' + ctx_l + ' ' if ctx_l else '') + \
                f'[HERE]' + \
                (' ' + ctx_r + '…' if ctx_r else '')
        conflicts.append({'google': gw, 'tess': tw, 'context': ctx})

    return conflicts


# ── Correction rules ──────────────────────────────────────────────────────────
_HYPHEN_SPLIT = re.compile(r'(\w)-\n(\w)')
_PUNCT_SPACE  = re.compile(r' +([;:,])')
_VERSE_COLON  = re.compile(r'(\d)\s+:\s+(\d)')   # "22 : 32" → "22:32"
_MULTI_SPACE  = re.compile(r'  +')

_NAME_FIXES = [
    (re.compile(r'\bNefl\b'), 'Nefi'),
    (re.compile(r'\bNef\b'),  'Nefi'),
]


def apply_corrections(text: str) -> tuple:
    """Apply known mechanical correction rules. Returns (text, log_list)."""
    log = []

    # Rejoin hyphenated line-break splits
    def rejoin(m):
        log.append(
            f'hyphen rejoined: "{m.group(1)}-" + "{m.group(2)}"'
        )
        return m.group(1) + m.group(2)
    text = _HYPHEN_SPLIT.sub(rejoin, text)

    # Remove spaces before punctuation
    n_before = len(re.findall(_PUNCT_SPACE, text))
    text = _PUNCT_SPACE.sub(r'\1', text)
    if n_before:
        log.append(f'spaces before punctuation removed (×{n_before})')

    # Fix spaces around colons in verse references
    n_colon = len(re.findall(_VERSE_COLON, text))
    text = _VERSE_COLON.sub(r'\1:\2', text)
    if n_colon:
        log.append(f'spaces around ":" in verse refs removed (×{n_colon})')

    # Collapse multiple spaces
    text = _MULTI_SPACE.sub(' ', text)

    # Known name OCR errors
    for pattern, correct in _NAME_FIXES:
        n = len(pattern.findall(text))
        if n:
            text = pattern.sub(correct, text)
            log.append(f'name fix: → "{correct}" (×{n})')

    return text, log


# ── Block 1 footnote parsing ──────────────────────────────────────────────────
def parse_block1(fn_zoom_img: Image.Image, chapter: int,
                 first_fn: int) -> tuple:
    """
    Run Tesseract on the fn_zoom image and parse footnote entries into
    Block 1 draft lines.  Returns (block1_lines, letter_list, raw_ocr).

    Strategy: split the raw OCR on '. ' (period + space) to isolate entry
    chunks — this works even when OCR garbles the footnote letter codes.
    Each chunk becomes one VERIFY line with the fn number pre-filled.
    The human reads the fn_zoom image to correct the letter codes and
    cross-reference letters.

    Two-letter footnote codes (2a, 2b …) are detected when the chapter
    reaches more than 26 footnotes; the caller adjusts via first_fn offset.
    """
    raw  = tess_ocr(fn_zoom_img, psm=6)
    flat = ' '.join(raw.split())
    flat = _WATERMARK.sub('', flat).strip()

    # Split on every '. ' boundary — each chunk is one footnote entry.
    # Filter out very short fragments (likely OCR noise from the rule line).
    chunks = [c.strip() for c in re.split(r'\.\s+', flat) if len(c.strip()) > 3]

    block1  = []
    letters = []
    fn_num  = first_fn

    for i, chunk in enumerate(chunks):
        # Assign sequential letter: a, b, c … z, then 2a, 2b …
        if i < 26:
            letter = chr(ord('a') + i)
            prefix = f'{chapter}{letter}'
        else:
            letter = f'2{chr(ord("a") + i - 26)}'
            prefix = f'{chapter}-{letter}'

        # Clean up the reference text
        ref = chunk.rstrip('.')
        ref = _VERSE_COLON.sub(r'\1:\2', ref)        # "22 : 32" → "22:32"
        ref = re.sub(r'(\d),\s+(\d)', r'\1,\2', ref) # "9, 11" → "9,11"
        ref = re.sub(r'\s+', ' ', ref).strip()

        # Output as a VERIFY line — human corrects letter codes from image
        line = f'{prefix}, {fn_num}:  [VERIFY: {ref}.]'

        # Wrap at 79 chars if needed
        if len(line) > 79:
            cut = line.rfind(' ', 0, 79)
            block1.append(line[:cut] if cut > 0 else line[:79])
            block1.append(line[cut + 1:] if cut > 0 else line[79:])
        else:
            block1.append(line)

        letters.append(letter)
        fn_num += 1

    return block1, letters, flat   # raw OCR returned for reference


# ── Line-length check ─────────────────────────────────────────────────────────
def long_lines(text: str, limit: int = 79) -> list:
    """Return list of (line_num, length, text) for lines over limit chars."""
    return [
        (i, len(ln), ln)
        for i, ln in enumerate(text.splitlines(), 1)
        if len(ln) > limit
    ]


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)

    book_page = int(sys.argv[1])
    first_fn  = int(sys.argv[2])
    chapter   = int(sys.argv[3])
    pdf_page  = book_page + PDF_OFFSET

    print(f"draft_page.py")
    print(f"  book page  : {book_page}")
    print(f"  first fn   : {first_fn}")
    print(f"  chapter    : {chapter}")
    print(f"  PDF page   : {pdf_page}  (offset={PDF_OFFSET})")
    print()

    # 1. Crops
    print("[1/5] Loading pre-rasterized image and generating crops...")
    crops = make_crops(book_page)

    # 2. Google OCR — already scoped to top 87% of PDF page via within_bbox()
    print("[2/5] Extracting Google OCR (body region, 0–87% of page)...")
    g_raw  = google_ocr(book_page)
    g_body = clean(g_raw) if g_raw else ""
    if not g_body:
        print("  WARNING: no Google OCR text — draft will use Tesseract only.")

    # 3. Tesseract on body crop (same 0–87% region, from pre-rasterized PNG)
    print("[3/5] Running Tesseract on body crop (0–87% of page)...")
    t_raw  = tess_ocr(crops["body"], psm=6)
    t_body = strip_footnotes(clean(t_raw))   # Tess still needs heuristic strip

    # 4. Corrections on Tesseract body; compare with Google for conflict list
    print("[4/5] Applying corrections and finding Google/Tesseract conflicts...")
    body, corr_log = apply_corrections(t_body)
    conflicts = find_conflicts(g_body, t_body) if g_body else []

    # 5. Block 1 from fn_zoom
    print("[5/5] Parsing Block 1 from fn_zoom...")
    block1, fn_letters, fn_raw = parse_block1(crops["fn_zoom"], chapter, first_fn)

    # ── Assemble draft file ────────────────────────────────────────────────────
    out = []

    out.append(f"Página {book_page}")
    out.append(body)
    out.append("")

    if block1:
        out.extend(block1)
        out.append("")
        out.append("fn_zoom raw OCR (for correcting VERIFY lines above):")
        out.append(fn_raw)
    else:
        out.append("(Block 1: no entries parsed — check fn_zoom image manually)")
        if fn_raw:
            out.append("")
            out.append("fn_zoom raw OCR:")
            out.append(fn_raw)

    out.append("")
    out.append("Corrections")
    if corr_log:
        for entry in corr_log:
            out.append(f"[auto] {entry}")
    else:
        out.append("[auto] (none)")

    # REVIEW section
    out.append("")
    out.append("=" * 60)
    out.append("REVIEW REQUIRED — complete before renaming to page_NNN.txt")
    out.append("=" * 60)

    if fn_letters:
        count    = len(fn_letters)
        last_fn  = first_fn + count - 1
        out.append(
            f"\nFootnotes: {count} on this page  "
            f"numbers [{first_fn}]–[{last_fn}]  "
            f"letters: {', '.join(fn_letters)}"
        )
        out.append(
            "→ Read fn_zoom image to verify each letter; read body crops to"
        )
        out.append(
            "  find superscript position; insert [N] immediately before the word."
        )
        out.append(
            "  Note: cross-reference letters in Block 1 ALWAYS need image verification."
        )

    over = long_lines(body)
    if over:
        out.append(f"\nLines over 79 chars in body draft ({len(over)}):")
        for ln, length, txt in over:
            out.append(f"  line {ln:3d} ({length} chars): {txt[:65]}...")

    if conflicts:
        out.append(
            f"\n{len(conflicts)} word conflict(s) — resolve each from the image:"
        )
        out.append(
            "  (Google OCR = text layer; Tess = Tesseract on image; "
            "body draft uses Tess)"
        )
        for i, c in enumerate(conflicts[:40], 1):
            g  = c['google'];  t = c['tess'];  ctx = c['context']
            out.append(f"  {i:2d}.  Google: {g!r:30s}  Tess: {t!r}")
            out.append(f"       context: {ctx}")
        if len(conflicts) > 40:
            out.append(f"  ... and {len(conflicts) - 40} more conflicts")
    else:
        out.append(
            "\nNo word conflicts — Google OCR and Tesseract agreed on all words."
        )

    out.append("")
    out.append(
        "When complete: rename to page_NNN.txt then run:"
    )
    out.append(
        f'  py check_lines.py "extracted pages\\page_{book_page}.txt"'
    )

    content  = '\n'.join(out)
    out_path = OUT_DIR / f"page_{book_page}_draft.txt"
    out_path.write_text(content, encoding='utf-8')

    n_corr = sum(
        int(re.search(r'×(\d+)', c).group(1)) if re.search(r'×(\d+)', c) else 1
        for c in corr_log
    )
    print(f"\nDraft written : {out_path.name}")
    print(f"  Word conflicts    : {len(conflicts)}")
    print(f"  Block 1 entries   : {len(block1)}")
    print(f"  Auto-corrections  : {n_corr}")
    print(f"  Long lines (body) : {len(long_lines(body))}")


if __name__ == "__main__":
    main()
