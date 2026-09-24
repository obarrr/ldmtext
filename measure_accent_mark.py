"""
Measure candidate accent/stray-mark blobs at pixel resolution, for resolving
"is this a real printed accent or scan debris?" calls objectively instead of
by eye. See feedback_stray_mark_google_ocr_order memory for the calibration
this was built from (2 Nefi 10:3 "sú" and 2 Nefi 10:21 "qué", both specks).

Usage:
    measure_accent_mark.py <page_png> <top> <bottom> <left> <right> [threshold]

Crops the given pixel box out of the page image, binarizes it (default
threshold 128 -- dark pixel = ink), runs connected-component labeling, and
prints every component's bounding box and pixel-area, sorted left to right.
Run it once over a candidate mark + its letter, and once over a nearby
known-good accented letter on the same line/page for reference, then compare:

  - Real accents (calibrated on genuine "á" in this edition's type):
    ~50-70 dark pixels, ONE connected component merged with (touching) the
    letter below it (0px gap between accent bbox bottom and letter bbox top).
  - Scan-debris specks (calibrated on 2 Nefi 10:3 and 10:21, both confirmed
    by direct editor inspection): ~8-10 dark pixels, often split into two or
    more tiny fragments, sitting 2-7px above the letter with a visible gap.

**These thresholds are only valid at the source resolution they were
calibrated on: `pages_1920/*.png`, confirmed embedded at 400dpi (PIL
`im.info['dpi']` reads exactly 399.9992 on every page checked so far).
This script always measures the RAW page PNG directly -- it does no
resizing itself, and prints the file's own embedded DPI every run so
each measurement is self-documenting.** Do not run this against a
zoomed/resized copy (e.g. a saved 3x-6x PIL .resize() crop made for
visual inspection, or a `measure_word_gap.py`-style 1200dpi
re-rasterization) and compare its pixel counts to the 400dpi
calibration table above without rescaling -- area scales with the
SQUARE of the DPI ratio (a 1200dpi crop reads ~9x the dark-pixel area
of the same mark at 400dpi). If the printed DPI does not match the
figures you're comparing against, rescale or re-derive the thresholds
before drawing a conclusion.

Coordinates are relative to the full-resolution page PNG, y first (row/
top-to-bottom) then x (column/left-to-right) per PIL/numpy array
convention. Find the rough box first with a visual zoom crop (PIL crop +
resize, viewed separately -- never fed into this script), then narrow to
exact pixel bounds here.
"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage


def main():
    if len(sys.argv) not in (6, 7):
        print(__doc__)
        sys.exit(1)
    page_png, top, bottom, left, right = sys.argv[1:6]
    top, bottom, left, right = int(top), int(bottom), int(left), int(right)
    threshold = int(sys.argv[6]) if len(sys.argv) == 7 else 128

    im_raw = Image.open(page_png)
    dpi = im_raw.info.get("dpi")
    if dpi is None:
        print(f"WARNING: {page_png} has no embedded DPI metadata -- cannot "
              f"confirm this matches the 400dpi calibration in the docstring. "
              f"Do not compare the pixel-area numbers below to that table "
              f"without independently confirming resolution.")
    elif abs(dpi[0] - 400) > 1 or abs(dpi[1] - 400) > 1:
        print(f"WARNING: {page_png} is embedded at {dpi} dpi, not ~400dpi. "
              f"The 400dpi calibration table in this script's docstring does "
              f"NOT apply directly -- rescale by (dpi/400)**2 before "
              f"comparing area, or re-derive thresholds at this resolution.")
    else:
        print(f"{page_png} confirmed at {dpi} dpi -- matches 400dpi calibration.")

    im = im_raw.convert("L")
    arr = np.array(im)
    region = arr[top:bottom, left:right]
    binary = region < threshold
    labeled, n = ndimage.label(binary)
    objs = ndimage.find_objects(labeled)

    comps = []
    for sl in objs:
        if sl is None:
            continue
        y0, y1 = sl[0].start, sl[0].stop
        x0, x1 = sl[1].start, sl[1].stop
        area = int(binary[y0:y1, x0:x1].sum())
        comps.append((x0, x1, y0, y1, x1 - x0, y1 - y0, area))
    comps.sort()

    print(f"{page_png}  region top={top} bottom={bottom} left={left} right={right} threshold={threshold}")
    print(f"{'x-range':>14} {'y-range':>12} {'w':>4} {'h':>4} {'area(px)':>9}")
    for x0, x1, y0, y1, w, h, area in comps:
        print(f"x[{x0:>4}:{x1:<4}] y[{y0:>4}:{y1:<4}] {w:>4} {h:>4} {area:>9}")


if __name__ == "__main__":
    main()
