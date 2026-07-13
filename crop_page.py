#!/usr/bin/env python3
"""
Crop a specific region of a page image for closer inspection.
Usage: python3 crop_page.py <image.png> <top_pct> <bot_pct> [zoom] [out.png]

Example - zoom in on lines around 60-75% of the page at 2x:
  python3 crop_page.py /tmp/page_438_full.png 60 75 2 /tmp/detail.png
"""
import sys
from PIL import Image

img_path = sys.argv[1]
top_pct  = float(sys.argv[2]) / 100
bot_pct  = float(sys.argv[3]) / 100
zoom     = int(sys.argv[4]) if len(sys.argv) > 4 else 1
out_path = sys.argv[5] if len(sys.argv) > 5 else '/tmp/crop_out.png'

img = Image.open(img_path)
w, h = img.size
crop = img.crop((0, int(h*top_pct), w, int(h*bot_pct)))
if zoom > 1:
    crop = crop.resize((crop.width*zoom, crop.height*zoom), Image.LANCZOS)
crop.save(out_path)
print(f"Saved {out_path}  size={crop.size}")
