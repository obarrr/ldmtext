#!/usr/bin/env python3
"""
Cross-check a transcribed page's body text against the 1920 PDF's own
embedded (Google-OCR) text layer, as a second opinion on letter-level
misreads -- not a source of truth, and never a reason to second-guess
hyphenation/word-boundary calls (see below).

Usage: py check_google_crosscheck.py <book_page> [page_txt_path]

Requires google_text_1920/page_NNNN.txt to already exist for this page
(run extract_google_text.py first).

How it compares (see project discussion, 2026-07-24/25):
- Both sides are reduced to a single character stream per page, with ALL
  whitespace and ALL hyphens removed before comparing. This is deliberate,
  not just convenient: Google's raw extraction frequently drops spaces
  between words entirely, and diffing at word-token granularity would
  flag every one of those as a mismatch. Stripping whitespace first means
  word-fusion on Google's side is structurally invisible to the diff --
  it can never surface as a candidate, so it can never tempt a change to
  a word-boundary call that the narrow-space-vs-merge rule
  (feedback_narrow_space_vs_merge) already settled via 1886/grammar. This
  tool has no opinion on hyphenation or word boundaries and must never be
  used to argue for one.
- Footnote superscript letters are a known weak spot for Google's OCR
  (dropped, glued onto the next word, or rendered as a stray quote
  character) -- not worth zooming or re-reading for. Any short (<=2 char)
  surplus on Google's side that lands at a position where this page's own
  [NNNN] footnote marker was stripped out of the transcription is
  auto-dismissed without being reported.
- Google's footnote-block text (dense, citation-heavy, even less
  reliable) is never excluded from the extraction, but is naturally
  ignored here: only content past the end of the transcribed body text
  is discarded, so the footnote block just falls into that trailing
  region.
- Everything else that differs -- letters, accents, punctuation -- is
  reported as a candidate worth investigating: re-zoom the mapped line,
  re-read independently, and either confirm the existing transcription
  (note it and move on), fix a genuine misread, or -- if still
  ambiguous -- keep the transcription as-is and flag it explicitly,
  same as any other unresolved rule-32 case.
"""
import io
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

BASE_DIR = Path(__file__).parent
GOOGLE_DIR = BASE_DIR / "google_text_1920"
PDF_OFFSET = 22

MARKER_RE = re.compile(r"\[\d+\]")
STRIP_CHARS = set(" \t\n\r-")  # whitespace + hyphens (single and "--" both)


def body_lines(path: Path):
    """Body-text lines of page_NNN.txt: after 'Página N', up to the first
    blank line -- same convention as check_line_wrap.py."""
    lines = path.read_text(encoding="utf-8").splitlines()
    start = 1 if lines and lines[0].startswith("Página") else 0
    out = []
    for l in lines[start:]:
        if l.strip() == "":
            break
        out.append(l)
    return out


def build_stream(lines):
    """Strip [NNNN] markers, whitespace, and hyphens; return the stripped
    character stream, the list of stripped-stream positions where a marker
    used to be, and a parallel list mapping each stripped-stream index back
    to its 1-based line number within `lines` (for reporting)."""
    raw = "\n".join(lines)
    out_chars = []
    out_line_of = []
    marker_positions = []
    line_no = 1
    i = 0
    n = len(raw)
    while i < n:
        ch = raw[i]
        if ch == "\n":
            line_no += 1
            i += 1
            continue
        m = MARKER_RE.match(raw, i)
        if m:
            marker_positions.append(len(out_chars))
            i = m.end()
            continue
        if ch in STRIP_CHARS:
            i += 1
            continue
        out_chars.append(ch)
        out_line_of.append(line_no)
        i += 1
    return "".join(out_chars), marker_positions, out_line_of


def build_google_stream(text):
    out_chars = []
    for ch in text:
        if ch in STRIP_CHARS:
            continue
        out_chars.append(ch)
    return "".join(out_chars)


def near_marker(pos, marker_positions, slack=2):
    return any(abs(pos - m) <= slack for m in marker_positions)


def context(s, i, j, width=25):
    a = max(0, i - width)
    b = min(len(s), j + width)
    return s[a:i] + "‹" + s[i:j] + "›" + s[j:b]


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    book_page = int(sys.argv[1])
    file_page = book_page + PDF_OFFSET
    page_txt = Path(sys.argv[2]) if len(sys.argv) > 2 else BASE_DIR / "pages" / f"page_{book_page}.txt"
    google_txt = GOOGLE_DIR / f"page_{file_page:04d}.txt"

    if not page_txt.exists():
        print(f"ERROR: {page_txt} not found")
        sys.exit(1)
    if not google_txt.exists():
        print(f"ERROR: {google_txt} not found -- run "
              f"'py extract_google_text.py {book_page}' first")
        sys.exit(1)

    lines = body_lines(page_txt)
    mine, marker_positions, line_of = build_stream(lines)
    google_text = google_txt.read_text(encoding="utf-8")
    google = build_google_stream(google_text)

    sm = SequenceMatcher(None, mine, google, autojunk=False)
    opcodes = sm.get_opcodes()

    candidates = []
    dismissed_marker = 0
    dismissed_trailing = 0

    for tag, i1, i2, j1, j2 in opcodes:
        if tag == "equal":
            continue
        # trailing content past the end of my transcribed stream (almost
        # always the footnote block) -- not investigated
        if i1 == i2 == len(mine):
            dismissed_trailing += 1
            continue
        # short Google-side surplus at a known footnote-marker position --
        # a swallowed/glued superscript letter, not investigated
        surplus = (j2 - j1) - (i2 - i1)
        if surplus >= 1 and (j2 - j1) <= 2 and near_marker(i1, marker_positions):
            dismissed_marker += 1
            continue
        candidates.append((tag, i1, i2, j1, j2))

    print(f"book_page={book_page}  file_page={file_page}")
    print(f"mine: {len(mine)} chars (stripped)  google: {len(google)} chars (stripped)")
    print(f"dismissed (footnote-marker glue): {dismissed_marker}")
    print(f"dismissed (trailing/footnote-block content): {dismissed_trailing}")
    print(f"candidates worth investigating: {len(candidates)}")
    print()

    for tag, i1, i2, j1, j2 in candidates:
        approx_line = line_of[i1] if i1 < len(line_of) else line_of[-1] if line_of else "?"
        print(f"[{tag}] near line {approx_line} (page {book_page})")
        print(f"  mine:   {context(mine, i1, i2)!r}")
        print(f"  google: {context(google, j1, j2)!r}")
        print()


if __name__ == "__main__":
    main()
