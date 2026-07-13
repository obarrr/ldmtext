#!/usr/bin/env python3
"""
Libro de Mormon 1920 - Page Processing Helper
Usage: python process_page.py <input.pdf> <page_label> [first_footnote_number]

Produces image crops in the system temp folder:
  page_NNN_full.png       full page at 400dpi
  page_NNN_top.png        top 40%
  page_NNN_mid.png        middle 30-70%
  page_NNN_bot.png        bottom 65-90%
  page_NNN_fn.png         footnote area 87-100%
  page_NNN_fn_zoom.png    footnote area 3x zoom for superscript reading
"""

import sys
import subprocess
import os
import tempfile
from PIL import Image

# Windows: winget installs poppler here; falls back to PATH on other systems
PDFTOPPM_PATH = (
    r"C:\Users\Robert O'Barr\AppData\Local\Microsoft\WinGet\Packages"
    r"\oschwartz10612.Poppler_Microsoft.Winget.Source_8wekyb3d8bbwe"
    r"\poppler-25.07.0\Library\bin\pdftoppm.exe"
)
PDFTOPPM = PDFTOPPM_PATH if os.path.exists(PDFTOPPM_PATH) else "pdftoppm"

OUTDIR = tempfile.gettempdir()

def rasterize(pdf_path, page_label):
    out_prefix = os.path.join(OUTDIR, f"page_{page_label}")
    subprocess.run([PDFTOPPM, "-r", "400", "-png", pdf_path, out_prefix],
                   check=True)
    # pdftoppm appends -1.png for single-page PDFs
    full_path = f"{out_prefix}-1.png"
    return full_path

def crop_sections(full_path, page_label):
    img = Image.open(full_path)
    w, h = img.size
    print(f"Full image size: {w}x{h} pixels at 400dpi")

    sections = {
        "top": (0, 0,            w, int(h * 0.40)),
        "mid": (0, int(h * 0.30), w, int(h * 0.70)),
        "bot": (0, int(h * 0.65), w, int(h * 0.90)),
        "fn":  (0, int(h * 0.87), w, h),
    }
    paths = {}
    for name, box in sections.items():
        crop = img.crop(box)
        path = os.path.join(OUTDIR, f"page_{page_label}_{name}.png")
        crop.save(path)
        paths[name] = path
        print(f"Saved {name}: {path}")

    # 3x zoom on footnote area for superscript reading
    fn_img = img.crop(sections["fn"])
    fn_zoom = fn_img.resize(
        (fn_img.width * 3, fn_img.height * 3), Image.LANCZOS
    )
    zoom_path = os.path.join(OUTDIR, f"page_{page_label}_fn_zoom.png")
    fn_zoom.save(zoom_path)
    paths["fn_zoom"] = zoom_path
    print(f"Saved fn_zoom: {zoom_path}")

    return paths

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python process_page.py <input.pdf> <page_label> "
              "[first_fn_number]")
        sys.exit(1)

    pdf_path = sys.argv[1]
    page_label = sys.argv[2]
    first_fn = int(sys.argv[3]) if len(sys.argv) > 3 else None

    print(f"Processing page {page_label} from {pdf_path}")
    if first_fn:
        print(f"First footnote number: {first_fn}")

    if pdf_path.lower().endswith('.png'):
        full_path = pdf_path
    else:
        full_path = rasterize(pdf_path, page_label)
    paths = crop_sections(full_path, page_label)

    print("\nAll section images saved to:", OUTDIR)
    print("Key files to read:")
    print(f"  fn_zoom : {paths['fn_zoom']}")
    print(f"  top     : {paths['top']}")
    print(f"  mid     : {paths['mid']}")
    print(f"  bot     : {paths['bot']}")
