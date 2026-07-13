#!/usr/bin/env python3
"""
check_chapter_map.py -- Audit chapter_map.csv for likely errors and fill gaps.

Checks performed:
  1. Missing values  (blank cells)
  2. Non-monotonic  (chapter N page >= chapter N+1 page within same book)
  3. Short span     (< 2 pages between consecutive chapters in same book)
  4. Long span      (> 20 pages -- may be legitimate but worth a look)
  5. Edition ratio  (1920 span vs 1886 span ratio outside 0.4 - 2.5)

Options:
  --fill-gaps    Interpolate blank cells from surrounding filled values and
                 save back to chapter_map.csv.  Estimated values are written
                 as plain numbers; a report lists every estimate so you can
                 verify or correct them manually.
  --crops        Save a header-strip PNG for every flagged page to crops_check\

Usage:
    python check_chapter_map.py
    python check_chapter_map.py --fill-gaps
    python check_chapter_map.py --fill-gaps --crops
"""

import csv
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent
MAP_FILE = BASE_DIR / "chapter_map.csv"

EDITIONS  = ["1920", "1879", "1886"]
MIN_SPAN  = 2
MAX_SPAN  = 20


# ---------------------------------------------------------------------------
# Load / save
# ---------------------------------------------------------------------------

def load_map():
    rows = []
    with open(MAP_FILE, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append(dict(row))
    return rows


def save_map(rows):
    fieldnames = ["book", "chapter", "page_1920", "page_1879", "page_1886"]
    with open(MAP_FILE, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def page(row, edition):
    val = row[f"page_{edition}"].strip()
    return int(val) if val else None


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def check_missing(rows):
    missing = []
    for row in rows:
        for ed in EDITIONS:
            if not row[f"page_{ed}"].strip():
                missing.append((row["book"], int(row["chapter"]), ed))
    return missing


def check_nonmonotonic(rows):
    issues = []
    prev = {ed: {} for ed in EDITIONS}
    for row in rows:
        book = row["book"]
        ch   = int(row["chapter"])
        for ed in EDITIONS:
            pg = page(row, ed)
            if pg is None:
                continue
            if book in prev[ed]:
                last_ch, last_pg = prev[ed][book]
                if pg <= last_pg:
                    issues.append((book, last_ch, ch, ed, last_pg, pg))
            prev[ed][book] = (ch, pg)
    return issues


def check_spans(rows):
    short_spans, long_spans = [], []
    prev = {ed: {} for ed in EDITIONS}
    for row in rows:
        book = row["book"]
        ch   = int(row["chapter"])
        for ed in EDITIONS:
            pg = page(row, ed)
            if pg is None:
                continue
            if book in prev[ed]:
                last_ch, last_pg = prev[ed][book]
                span = pg - last_pg
                if span < MIN_SPAN:
                    short_spans.append((book, last_ch, ch, ed, last_pg, pg, span))
                elif span > MAX_SPAN:
                    long_spans.append((book, last_ch, ch, ed, last_pg, pg, span))
            prev[ed][book] = (ch, pg)
    return short_spans, long_spans


def check_edition_ratio(rows):
    issues = []
    prev_1920, prev_1886 = {}, {}
    for row in rows:
        book = row["book"]
        ch   = int(row["chapter"])
        pg20 = page(row, "1920")
        pg86 = page(row, "1886")

        if book in prev_1920 and book in prev_1886:
            last_ch20, last_pg20 = prev_1920[book]
            last_ch86, last_pg86 = prev_1886[book]
            if last_ch20 == last_ch86 and pg20 is not None and pg86 is not None:
                span20 = pg20 - last_pg20
                span86 = pg86 - last_pg86
                if span86 > 0 and span20 > 0:
                    ratio = span20 / span86
                    if ratio < 0.4 or ratio > 2.5:
                        issues.append((book, last_ch20, ch, span20, span86, ratio))

        if pg20 is not None:
            prev_1920[book] = (ch, pg20)
        if pg86 is not None:
            prev_1886[book] = (ch, pg86)

    return issues


# ---------------------------------------------------------------------------
# Gap filling via linear interpolation
# ---------------------------------------------------------------------------

def fill_gaps(rows, edition):
    """
    For every blank cell in this edition column, interpolate from the
    nearest filled values before and after it in the overall row sequence.
    Cross-book neighbours are used freely since all editions have
    continuous page numbering across the whole PDF.

    Returns a list of (book, chapter, estimated_page, left_anchor, right_anchor)
    for every cell that was filled.  The rows list is updated in place.
    """
    col = f"page_{edition}"

    # Snapshot current page values (None = blank)
    pages = [int(r[col]) if r[col].strip() else None for r in rows]
    n     = len(pages)

    estimates = []

    for i in range(n):
        if pages[i] is not None:
            continue

        # Nearest filled to the left
        left_i = left_pg = None
        for j in range(i - 1, -1, -1):
            if pages[j] is not None:
                left_i, left_pg = j, pages[j]
                break

        # Nearest filled to the right
        right_i = right_pg = None
        for j in range(i + 1, n):
            if pages[j] is not None:
                right_i, right_pg = j, pages[j]
                break

        if left_i is None and right_i is None:
            continue   # no anchors at all -- cannot estimate

        if left_i is None:
            # Only a right anchor: step back one page per row
            est = max(1, right_pg - (right_i - i))
        elif right_i is None:
            # Only a left anchor: step forward one page per row
            est = left_pg + (i - left_i)
        else:
            # Linear interpolation between left and right anchors
            frac = (i - left_i) / (right_i - left_i)
            est  = round(left_pg + frac * (right_pg - left_pg))
            est  = max(left_pg + 1, est)   # never go backwards

        book = rows[i]["book"]
        ch   = int(rows[i]["chapter"])

        if left_i is not None:
            left_label = (f"{rows[left_i]['book']} ch.{rows[left_i]['chapter']}"
                          f"=p.{left_pg}")
        else:
            left_label = "none"

        if right_i is not None:
            right_label = (f"{rows[right_i]['book']} ch.{rows[right_i]['chapter']}"
                           f"=p.{right_pg}")
        else:
            right_label = "none"

        estimates.append((book, ch, est, left_label, right_label))

        # Write estimate and update snapshot so subsequent gaps in the
        # same pass can use this value as an anchor.
        rows[i][col] = str(est)
        pages[i]     = est

    return estimates


# ---------------------------------------------------------------------------
# Optional header-strip crops
# ---------------------------------------------------------------------------

def save_crops(flagged_pages):
    try:
        from PIL import Image
    except ImportError:
        print("  [crops] Pillow not installed -- skipping.")
        return

    out_dir = BASE_DIR / "crops_check"
    out_dir.mkdir(exist_ok=True)
    saved = 0

    for edition, pg_num, label in sorted(set(flagged_pages)):
        img_path = BASE_DIR / f"pages_{edition}" / f"page_{pg_num:04d}.png"
        if not img_path.exists():
            print(f"  [crops] Not found: {img_path.name}")
            continue
        img = Image.open(img_path)
        w, h = img.size
        strip = img.crop((0, 0, w, int(h * 0.12)))
        safe  = label.replace(" ", "_").replace(",", "")
        strip.save(out_dir / f"{edition}_p{pg_num:04d}_{safe}.png")
        saved += 1

    print(f"  [crops] {saved} header strips saved to crops_check\\")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    do_fill  = "--fill-gaps" in sys.argv
    do_crops = "--crops"     in sys.argv

    rows        = load_map()
    total_cells = len(rows) * len(EDITIONS)

    missing      = check_missing(rows)
    nonmono      = check_nonmonotonic(rows)
    short, long_ = check_spans(rows)
    ratio_issues = check_edition_ratio(rows)

    flagged_pages = []

    print("=== chapter_map.csv audit ===")
    print(f"    Rows: {len(rows)}   Editions: {len(EDITIONS)}"
          f"   Total cells: {total_cells}\n")

    # ---- Missing ----
    print(f"--- 1. Missing values: {len(missing)} ---")
    if missing:
        cur_book = None
        for book, ch, ed in missing:
            if book != cur_book:
                print(f"  {book}")
                cur_book = book
            print(f"      ch.{ch:3d}  [{ed}]")
    else:
        print("  None -- all cells filled.")
    print()

    # ---- Non-monotonic ----
    print(f"--- 2. Non-monotonic page numbers: {len(nonmono)} ---")
    for book, ch_a, ch_b, ed, pg_a, pg_b in nonmono:
        print(f"  [{ed}] {book} ch.{ch_a} (p.{pg_a}) >= ch.{ch_b} (p.{pg_b})")
        flagged_pages += [(ed, pg_a, f"{book}_ch{ch_a}"),
                          (ed, pg_b, f"{book}_ch{ch_b}")]
    if not nonmono:
        print("  None.")
    print()

    # ---- Short spans ----
    print(f"--- 3. Short spans (< {MIN_SPAN} pages): {len(short)} ---")
    for book, ch_a, ch_b, ed, pg_a, pg_b, span in short:
        print(f"  [{ed}] {book} ch.{ch_a}-ch.{ch_b}: "
              f"p.{pg_a}->p.{pg_b} = {span} page(s)")
        flagged_pages.append((ed, pg_b, f"{book}_ch{ch_b}_short"))
    if not short:
        print("  None.")
    print()

    # ---- Long spans ----
    print(f"--- 4. Long spans (> {MAX_SPAN} pages): {len(long_)} ---")
    for book, ch_a, ch_b, ed, pg_a, pg_b, span in long_:
        print(f"  [{ed}] {book} ch.{ch_a}-ch.{ch_b}: "
              f"p.{pg_a}->p.{pg_b} = {span} pages")
        flagged_pages.append((ed, pg_b, f"{book}_ch{ch_b}_long"))
    if not long_:
        print("  None.")
    print()

    # ---- Edition ratio ----
    print(f"--- 5. Edition ratio (1920/1886 span outside 0.4-2.5): "
          f"{len(ratio_issues)} ---")
    for book, ch_a, ch_b, span20, span86, ratio in ratio_issues:
        print(f"  {book} ch.{ch_a}-ch.{ch_b}: "
              f"1920={span20}pp  1886={span86}pp  ratio={ratio:.2f}")
    if not ratio_issues:
        print("  None.")
    print()

    # ---- Gap filling ----
    if do_fill:
        print("--- Gap filling (--fill-gaps) ---")
        total_filled = 0
        for edition in EDITIONS:
            estimates = fill_gaps(rows, edition)
            if estimates:
                print(f"\n  [{edition}] {len(estimates)} estimates:")
                for book, ch, est, left, right in estimates:
                    print(f"    {book} ch.{ch}: ~p.{est}"
                          f"  (between {left}  and  {right})")
            else:
                print(f"  [{edition}] No gaps to fill.")
            total_filled += len(estimates)

        if total_filled:
            save_map(rows)
            print(f"\n  Saved. {total_filled} estimated values written.")
            print("  Review the estimates above and correct any that look wrong.")
        print()

    # ---- Summary ----
    filled   = sum(1 for r in rows
                   for ed in EDITIONS if r[f"page_{ed}"].strip())
    pct      = 100 * filled / total_cells
    problems = len(nonmono) + len(short) + len(ratio_issues)
    print("=== Summary ===")
    print(f"  Filled:         {filled}/{total_cells} ({pct:.1f}%)")
    print(f"  Missing:        {len(missing)}")
    print(f"  Problems:       {problems}"
          f"  (non-monotonic + short spans + ratio issues)")
    print(f"  Long spans:     {len(long_)}  (review but may be correct)")

    if do_crops and flagged_pages:
        print()
        save_crops(flagged_pages)


if __name__ == "__main__":
    main()
