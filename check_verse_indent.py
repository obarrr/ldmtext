#!/usr/bin/env python3
"""
Verse-number indentation checker.
Flags any line where a verse number starting the line is preceded by
leading whitespace - verse numbers always begin at column 1, with zero
indentation, like every other body-text line in this project. Run this
alongside check_spaced_punctuation.py/check_footnote_punctuation.py:
during Session A on the new page file, and against librodm.txt during
Session E.

Confirmed failure mode (page 493, silently recurred on page 508 with no
mechanical guard in place until this script was added 2026-07-25): a
verse-start line gets typed with a few leading spaces, mimicking
paragraph-indent convention from ordinary prose, which this project's
plain-text transcription format never uses.

Usage: python3 check_verse_indent.py <file> [file2 ...]
Exit status: 1 if anything was flagged, 0 if clean.
"""
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PATTERN = re.compile(r'^[ \t]+\d+\.\s')

if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(2)

total_hits = 0
for path in sys.argv[1:]:
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    hits = [(i, line.rstrip("\n")) for i, line in enumerate(lines, 1)
            if PATTERN.match(line)]
    total_hits += len(hits)
    if hits:
        print(f"\n{path}: {len(hits)} line(s) with an indented verse number")
        for i, l in hits:
            print(f"  {i:5d}: {l}")
    else:
        print(f"{path}: clean ({len(lines)} lines)")

if len(sys.argv) > 2:
    print(f"\nTotal across {len(sys.argv) - 1} file(s): {total_hits} flagged line(s)")

print(
    "\nNote: a hit inside a page file's Corrections log may be a "
    "historical quote wrapped mid-prose (documentation, not a live "
    "defect) - check context before editing. Every hit in actual body "
    "text should be fixed by removing the leading whitespace."
    if total_hits else ""
)

sys.exit(1 if total_hits else 0)
