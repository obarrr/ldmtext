#!/usr/bin/env python3
"""
Measure a suspected narrow-space-vs-merge word gap at high native DPI.

Why this exists: the standard 400dpi transcription crop
(process_page.py / crop_page.py, via pdftoppm) is fine for reading
letter shapes, but resizing/zooming that crop with PIL only
interpolates existing pixels -- it cannot recover a hairline gap that
the 400dpi rasterization already blurred away. A real case on page 517
measured a genuine printed gap as only 1px (indistinguishable from
intra-word letter kerning) at 400dpi, but the same gap measured 20px
(clearly wider than kerning) once rendered at 1200dpi straight from the
source PDF. See the `feedback_narrow_space_vs_merge` memory.

This script re-rasterizes ONE page directly from the source PDF at a
much higher DPI (default 1200) using pdfplumber, then does a
column-darkness gap analysis across a row band you specify, printing
every gap's pixel position and width plus an annotated image -- so you
can visually confirm which gap is the disputed word-boundary and
compare its width against the intra-word kerning gaps inside the very
same word(s), which is the correct baseline (NOT other word-gaps on
the line -- justification stretches those unevenly; the same "vino á"
pair on page 517 measured 58px in one line and 20px two lines later).

Usage:
  python measure_word_gap.py <pdf_page_number> <approx_top_pct> <approx_bot_pct> [line_index] [dpi] [pdf_path]

  pdf_page_number: 1-indexed page number matching pages_1920/page_NNNN.png
                   naming (i.e. the "file page" from chapter_map.csv).
  approx_top_pct/approx_bot_pct: rough vertical band (0-100) containing
                   the line in question -- same convention as
                   crop_page.py. Get this from process_page.py's mid/
                   top/bot crops first, then narrow in. This can span
                   several lines -- the script finds each individual
                   text line inside the slice (by locating near-blank
                   row gaps between lines, not just any nonzero row) and
                   lists them.
  line_index: 0-based index into the lines found within that slice. If
              omitted, the script only lists the detected lines (with a
              tiny preview image each) and does NOT run gap analysis --
              run it again with the right index once you know which one
              you want.
  dpi: default 1200. Bump higher (e.g. 2400) if 1200 still doesn't
       resolve the gap.

Output (all in the system temp folder):
  gap_page_<N>_line<I>_preview.png    tiny preview of each detected line
                                      (when line_index is omitted)
  gap_page_<N>_line<I>_band.png       plain crop of the chosen line
  gap_page_<N>_line<I>_annotated.png  same crop with every detected gap
                                      boundary drawn and labeled with its
                                      start-pixel x coordinate and width

Read both images, then read off the gap widths printed to stdout and
compare the disputed junction's width to the narrowest/widest intra-word
gaps in the same word(s) -- a real space should be at least ~2x any
intra-word kerning gap; anything closer than that is genuinely
ambiguous even at high DPI and should go to the editor's own look
rather than being resolved unilaterally.
"""
import sys
import os
import tempfile
import numpy as np
import pdfplumber
from PIL import Image, ImageDraw

DEFAULT_PDF = "Libro_de_Mormon 1920.pdf"
OUTDIR = tempfile.gettempdir()
DARK_THRESH = 150


def render_page(pdf_path, page_number, dpi):
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_number - 1]
        im = page.to_image(resolution=dpi)
        pil_img = im.original if hasattr(im, "original") else im
        return pil_img.convert("L")


def find_gaps(dark, y0, y1, x0, x1, min_width=1):
    strip = dark[y0:y1, x0:x1]
    col_sums = strip.sum(axis=0)
    w = col_sums.shape[0]
    gaps = []
    in_gap = False
    gstart = 0
    for x in range(w):
        if col_sums[x] == 0 and not in_gap:
            gstart = x
            in_gap = True
        elif col_sums[x] != 0 and in_gap:
            gaps.append((x0 + gstart, x0 + x, x - gstart))
            in_gap = False
    if in_gap:
        gaps.append((x0 + gstart, x0 + w, w - gstart))
    return [g for g in gaps if g[2] >= min_width]


def find_line_bands(dark, y0, y1, blank_thresh=None, min_line_height=15):
    """Split a (possibly multi-line) row slice into individual text lines
    by finding runs of near-blank rows between them. Requiring several
    consecutive near-blank rows (not just one) avoids false splits from
    a single row that happens to fall between a descender and the next
    line's ascender.

    blank_thresh defaults to a fraction of the slice's own peak row
    density rather than a fixed pixel count -- at high DPI the
    inter-line "gap" rows are NOT truly zero (accent marks, scan
    texture, and antialiasing put a noise floor of several percent of
    peak density even between lines), so a small fixed threshold like
    3 fails to find any gap at all. A relative threshold self-scales
    with DPI/rendering settings instead of needing manual retuning."""
    row_sums = dark[y0:y1, :].sum(axis=1)
    n = len(row_sums)
    if blank_thresh is None:
        peak = row_sums.max() if len(row_sums) else 0
        blank_thresh = max(3, 0.1 * peak)
    is_blank = row_sums <= blank_thresh
    lines = []
    in_line = False
    start = 0
    blank_run = 0
    for i in range(n):
        if not is_blank[i]:
            if not in_line:
                start = i
                in_line = True
            blank_run = 0
        else:
            if in_line:
                blank_run += 1
                if blank_run >= 4:
                    end = i - blank_run + 1
                    if end - start >= min_line_height:
                        lines.append((y0 + start, y0 + end))
                    in_line = False
                    blank_run = 0
    if in_line:
        end = n - blank_run
        if end - start >= min_line_height:
            lines.append((y0 + start, y0 + end))
    return lines


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)

    page_number = int(sys.argv[1])
    top_pct = float(sys.argv[2]) / 100
    bot_pct = float(sys.argv[3]) / 100
    line_index = int(sys.argv[4]) if len(sys.argv) > 4 and sys.argv[4] != "-" else None
    dpi = int(sys.argv[5]) if len(sys.argv) > 5 else 1200
    pdf_path = sys.argv[6] if len(sys.argv) > 6 else DEFAULT_PDF

    print(f"Rendering page {page_number} at {dpi}dpi from {pdf_path} ...")
    img = render_page(pdf_path, page_number, dpi)
    w, h = img.size
    print(f"Full page size at {dpi}dpi: {w}x{h}")

    y0, y1 = int(h * top_pct), int(h * bot_pct)
    arr = np.array(img)
    dark = arr < DARK_THRESH

    lines = find_line_bands(dark, y0, y1)
    if not lines:
        print("No text lines found in that vertical band -- widen top/bot pct.")
        sys.exit(1)

    if line_index is None:
        print(f"\n{len(lines)} line(s) found in that slice:")
        for i, (ly0, ly1) in enumerate(lines):
            preview = img.crop((0, ly0, w, ly1)).convert("RGB")
            path = os.path.join(OUTDIR, f"gap_page_{page_number}_line{i}_preview.png")
            preview.save(path)
            print(f"  [{i}] rows {ly0}-{ly1}  ({ly1-ly0}px tall)  -> {path}")
        print("\nRe-run with a line_index argument to analyze one of these.")
        return

    ty0, ty1 = lines[line_index]
    print(f"Using line {line_index}: rows {ty0}-{ty1}")

    gaps = find_gaps(dark, ty0, ty1, 0, w)
    print(f"\n{len(gaps)} gaps found (start, end, width_px):")
    for g in gaps:
        print(f"  {g[0]:6d} - {g[1]:6d}   {g[2]:4d}px")

    band = img.crop((0, ty0, w, ty1)).convert("RGB")
    band_path = os.path.join(OUTDIR, f"gap_page_{page_number}_line{line_index}_band.png")
    band.save(band_path)

    ann = band.copy()
    draw = ImageDraw.Draw(ann)
    for gs, ge, gw in gaps:
        draw.line([(gs, 0), (gs, ann.height)], fill=(255, 0, 0), width=1)
        draw.line([(ge, 0), (ge, ann.height)], fill=(0, 0, 255), width=1)
        draw.text((gs, 2), f"{gw}", fill=(0, 150, 0))
    ann_path = os.path.join(OUTDIR, f"gap_page_{page_number}_line{line_index}_annotated.png")
    ann.save(ann_path)

    print(f"\nSaved band:      {band_path}")
    print(f"Saved annotated: {ann_path}")
    print("\nRead the annotated image, find the disputed word junction's")
    print("gap width, and compare it to the narrowest/widest intra-word")
    print("kerning gaps inside the same word(s) elsewhere in this band --")
    print("NOT to other word-gaps on the line (justification stretches")
    print("those unevenly). A real space should be at least ~2x any")
    print("intra-word kerning gap; closer than that is genuinely")
    print("ambiguous even at high DPI and should go to the editor.")


if __name__ == "__main__":
    main()
