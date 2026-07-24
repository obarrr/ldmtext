#!/usr/bin/env python3
"""
Footnote citation punctuation checker (rules 21-23, 31).
Flags, in librodm_foot.txt (Block 1) and/or librodm.txt's Notas section
(Block 2) footnote-definition lines:
  - a space before a comma, semicolon, or colon (e.g. "65 : 17",
    "51:9 ; 52:1" instead of "65:17", "51:9; 52:1")
  - a space on either side of a verse-range hyphen (rule 23 - number
    ranges use a single hyphen, no spaces, e.g. "13:5-6" not "13:5 - 6")

Usage: python3 check_footnote_punctuation.py [file ...]
       (defaults to librodm_foot.txt if no file given)
Exit status: 1 if anything was flagged, 0 if clean.
"""
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

SPACE_BEFORE = re.compile(r' [,;:]')
SPACED_DASH = re.compile(r'\d\s+-|-\s+\d')

paths = sys.argv[1:] or ["librodm_foot.txt"]

total_hits = 0
for path in paths:
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    hits = []
    for i, line in enumerate(lines, 1):
        l = line.rstrip("\n")
        if SPACE_BEFORE.search(l) or SPACED_DASH.search(l):
            hits.append((i, l))
    total_hits += len(hits)
    if hits:
        print(f"\n{path}: {len(hits)} line(s) flagged")
        for i, l in hits:
            print(f"  {i:5d}: {l}")
    else:
        print(f"{path}: clean ({len(lines)} lines)")

sys.exit(1 if total_hits else 0)
