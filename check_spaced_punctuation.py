#!/usr/bin/env python3
"""
Space-before-punctuation checker (rule 31).
Flags any line where a space immediately precedes a comma, semicolon,
colon, exclamation mark, or question mark - whether from the original
1920 print or introduced during transcription/justification. Run this
BEFORE check_lines.py during Session A, and against librodm.txt (or a
range of pages/*.txt) during Session E.

Usage: python3 check_spaced_punctuation.py <file> [file2 ...]
Exit status: 1 if anything was flagged, 0 if clean.
"""
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PATTERN = re.compile(r' [,;:!?]')

if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(2)

total_hits = 0
for path in sys.argv[1:]:
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    hits = [(i, line.rstrip("\n")) for i, line in enumerate(lines, 1)
            if PATTERN.search(line)]
    total_hits += len(hits)
    if hits:
        print(f"\n{path}: {len(hits)} line(s) with a space before punctuation")
        for i, l in hits:
            print(f"  {i:5d}: {l}")
    else:
        print(f"{path}: clean ({len(lines)} lines)")

if len(sys.argv) > 2:
    print(f"\nTotal across {len(sys.argv) - 1} file(s): {total_hits} flagged line(s)")

print(
    "\nNote: a hit inside a page file's Corrections log may be a "
    "historical quote of an already-fixed reading (documentation, not a "
    "live defect) - check context before editing. Every hit in actual "
    "body text or footnote text should be fixed by removing the space."
    if total_hits else ""
)

sys.exit(1 if total_hits else 0)
