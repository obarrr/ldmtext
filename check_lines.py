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
for i, line in enumerate(lines, 1):
    l = line.rstrip()
    ll = len(l)
    flag = f"  <-- OVER {max_len}" if ll > max_len else ""
    print(f"{i:3d} {ll:3d}  {l}{flag}")
    if ll > max_len:
        over += 1

print(f"\nTotal lines: {len(lines)}  |  Over {max_len}: {over}")
