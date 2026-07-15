#!/usr/bin/env python3
"""
Quick line length checker for a completed page text file.
Usage: python3 check_lines.py page_NNN.txt [max_len]
"""
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

path = sys.argv[1]
max_len = int(sys.argv[2]) if len(sys.argv) > 2 else 72

with open(path, encoding="utf-8") as f:
    lines = f.readlines()

over = 0
hyphen_hits = []  # (line_no, this_line, next_line)
for i, line in enumerate(lines, 1):
    l = line.rstrip()
    ll = len(l)
    flags = []
    if ll > max_len:
        flags.append(f"OVER {max_len}")
        over += 1
    # Trailing single hyphen: an un-rejoined line-break word split (rule 7
    # says this must NEVER survive into the output). Em-dashes ("--") are
    # a separate, legitimate convention (see dash check notes in the
    # orthography-check skill) and are deliberately not flagged here.
    if l.endswith("-") and not l.endswith("--"):
        flags.append("TRAILING HYPHEN - see detail below")
        next_line = lines[i].rstrip() if i < len(lines) else ""
        hyphen_hits.append((i, l, next_line))
    flag = f"  <-- {'; '.join(flags)}" if flags else ""
    print(f"{i:3d} {ll:3d}  {l}{flag}")

print(f"\nTotal lines: {len(lines)}  |  Over {max_len}: {over}  |  "
      f"Trailing hyphens: {len(hyphen_hits)}")

if hyphen_hits:
    print(f"\n{'-'*72}")
    print("TRAILING HYPHEN DETAIL — resolve each one before finishing the page.")
    print("Most are unrejoined line-break splits (rule 7): strip the hyphen,")
    print("reattach the next line's first word, recheck length (rule 8 if it")
    print("no longer fits). A few are legitimate: Spanish compound ordinals")
    print("(e.g. \"sexagesimo-segundo\") carry the hyphen as part of the word")
    print("itself and are correct as printed — only a genuine printer's")
    print("line-break split should be rejoined.")
    print(f"{'-'*72}")
    for i, this_line, next_line in hyphen_hits:
        stem = this_line.rsplit(None, 1)[-1].rstrip("-")
        first_word = next_line.split(None, 1)[0] if next_line else ""
        candidate = f"{stem}{first_word}"
        print(f"\nLine {i}: {this_line}")
        print(f"Line {i+1}: {next_line}")
        print(f"  candidate rejoin: \"{candidate}\" — real split, or a "
              f"legitimate compound word?")
