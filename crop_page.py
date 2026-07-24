#!/usr/bin/env python3
"""
Crop a specific region of a page image for closer inspection.
Usage: python3 crop_page.py <image.png> <top_pct> <bot_pct> [zoom] [out.png] [left_pct] [right_pct]

left_pct/right_pct default to 0/100 (full width) when omitted, so all
existing full-width-only call sites keep working unchanged.

Example - zoom in on lines around 60-75% of the page at 2x, full width:
  python3 crop_page.py /tmp/page_438_full.png 60 75 2 /tmp/detail.png

Example - isolate a single glyph horizontally too, e.g. the 20-30% width
band of a line at 87-89% down the page, at 14x zoom (added 2026-07-23 —
a full-width crop at high zoom still gets downsampled on display/model
input once it's wide enough, so distinguishing a single small glyph like
"r" vs "v" needs the horizontal crop to narrow the saved image down):
  python3 crop_page.py /tmp/page_501_full.png 87 89 14 /tmp/glyph.png 20 30
"""
import sys
from PIL import Image

img_path = sys.argv[1]
top_pct   = float(sys.argv[2]) / 100
bot_pct   = float(sys.argv[3]) / 100
zoom      = int(sys.argv[4]) if len(sys.argv) > 4 else 1
out_path  = sys.argv[5] if len(sys.argv) > 5 else '/tmp/crop_out.png'
left_pct  = float(sys.argv[6]) / 100 if len(sys.argv) > 6 else 0.0
right_pct = float(sys.argv[7]) / 100 if len(sys.argv) > 7 else 1.0

img = Image.open(img_path)
w, h = img.size
crop = img.crop((int(w*left_pct), int(h*top_pct), int(w*right_pct), int(h*bot_pct)))
if zoom > 1:
    crop = crop.resize((crop.width*zoom, crop.height*zoom), Image.LANCZOS)
crop.save(out_path)
print(f"Saved {out_path}  size={crop.size}")
