"""
check_spans.py — compare chapter page-spans across the three editions.

For each chapter, the span is: next_chapter_start - this_chapter_start.
For the last chapter of each book, the span uses the first page of the next
book (still meaningful — it's where the book ends).  The very last row
(Moroni ch.10) is skipped because there is no following row.

A chapter is flagged when the maximum span minus the minimum span across
the three editions exceeds THRESHOLD (default 1).
"""

import csv
from pathlib import Path

BASE_DIR = Path(r"\\Desktop-6p05aa1\d\Users\Robert O'Barr\Documents\My Documents\family\robert\bofm\libro_de_mormon_1920")
CSV_PATH = BASE_DIR / "chapter_map.csv"

THRESHOLD = 1   # flag when max_span - min_span > this


def main():
    rows = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append({
                "book":    r["book"],
                "chapter": int(r["chapter"]),
                "p1920":   int(r["page_1920"]) if r["page_1920"] else None,
                "p1879":   int(r["page_1879"]) if r["page_1879"] else None,
                "p1886":   int(r["page_1886"]) if r["page_1886"] else None,
            })

    issues = []

    for i, row in enumerate(rows[:-1]):          # skip last row (no successor)
        nxt = rows[i + 1]

        spans = {}
        for ed in ("p1920", "p1879", "p1886"):
            if row[ed] is not None and nxt[ed] is not None:
                spans[ed] = nxt[ed] - row[ed]

        vals = list(spans.values())
        if len(vals) < 2:
            continue

        rng = max(vals) - min(vals)
        if rng > THRESHOLD:
            issues.append({
                "book":      row["book"],
                "ch":        row["chapter"],
                "next_book": nxt["book"],
                "next_ch":   nxt["chapter"],
                "s1920":     spans.get("p1920"),
                "s1879":     spans.get("p1879"),
                "s1886":     spans.get("p1886"),
                "range":     rng,
                # raw pages for context
                "p1920": row["p1920"], "p1879": row["p1879"], "p1886": row["p1886"],
            })

    if not issues:
        print("No issues found — all chapter spans agree within the threshold.")
        return

    # ── header ──────────────────────────────────────────────────────────────
    hdr = (f"{'Book':<22} {'Ch':>3}  "
           f"{'pg_1920':>7} {'pg_1879':>7} {'pg_1886':>7}  "
           f"{'d1920':>6} {'d1879':>6} {'d1886':>6}  {'Rng':>4}")
    print(hdr)
    print("-" * len(hdr))

    for iss in issues:
        # note when the span crosses a book boundary
        if iss["next_book"] != iss["book"]:
            tag = f"  (last ch, next={iss['next_book']})"
        else:
            tag = ""

        def fmt(v):
            return f"{v:+d}" if v is not None else "  --"

        print(
            f"{iss['book']:<22} {iss['ch']:>3}  "
            f"{iss['p1920']:>7} {iss['p1879']:>7} {iss['p1886']:>7}  "
            f"{fmt(iss['s1920']):>6} {fmt(iss['s1879']):>6} {fmt(iss['s1886']):>6}  "
            f"{iss['range']:>4}{tag}"
        )

    print(f"\n{len(issues)} chapter(s) flagged (span range > {THRESHOLD} page).")


if __name__ == "__main__":
    main()
