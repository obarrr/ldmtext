#!/usr/bin/env python3
"""
split_pdfs.py -- Rasterize all three Book of Mormon PDFs into per-page images.

Run once from the libro_de_mormon_1920 folder:
    python split_pdfs.py

Output:
    pages_1920\page_0001.png ... page_NNNN.png
    pages_1879\page_0001.png ... page_NNNN.png
    pages_1886\page_0001.png ... page_NNNN.png

Page filenames reflect PDF page numbers (not book page numbers).
The chapter_map.csv lookup table connects PDF pages to book content.
"""

import os
import subprocess
from pathlib import Path

PDFTOPPM_PATH = (
    r"C:\Users\Robert O'Barr\AppData\Local\Microsoft\WinGet\Packages"
    r"\oschwartz10612.Poppler_Microsoft.Winget.Source_8wekyb3d8bbwe"
    r"\poppler-25.07.0\Library\bin\pdftoppm.exe"
)
PDFTOPPM = PDFTOPPM_PATH if os.path.exists(PDFTOPPM_PATH) else "pdftoppm"

BASE_DIR = Path(__file__).parent

PDFS = {
    "1920": BASE_DIR / "Libro_de_Mormon 1920.pdf",
    "1879": BASE_DIR / "BOM 1879 Pratt.pdf",
    "1886": BASE_DIR / "Libro_de_Mormon 1886.pdf",
}


def split_pdf(edition, pdf_path):
    out_dir = BASE_DIR / f"pages_{edition}"
    out_dir.mkdir(exist_ok=True)

    existing = sorted(out_dir.glob("page_*.png"))
    if existing:
        print(f"  [{edition}] {len(existing)} pages already present -- skipping.")
        print(f"           Delete {out_dir} to force a re-run.")
        return len(existing)

    print(f"  [{edition}] Rasterizing {pdf_path.name} at 400dpi ...")
    prefix = out_dir / "page"
    result = subprocess.run(
        [PDFTOPPM, "-r", "400", "-png", str(pdf_path), str(prefix)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"  [{edition}] ERROR: pdftoppm failed.")
        print(result.stderr)
        return 0

    # pdftoppm outputs page-1.png, page-2.png ... (padding varies by page count)
    # Rename to consistent 4-digit zero-padded names: page_0001.png etc.
    raw = sorted(out_dir.glob("page-*.png"))
    for f in raw:
        num = int(f.stem.split("-")[-1])
        f.rename(out_dir / f"page_{num:04d}.png")

    count = len(list(out_dir.glob("page_*.png")))
    print(f"  [{edition}] Done. {count} pages saved to {out_dir.name}\\")
    return count


def main():
    print("split_pdfs.py")
    print(f"  Poppler : {PDFTOPPM}")
    print(f"  Base dir: {BASE_DIR}")
    print()

    if not os.path.exists(PDFTOPPM):
        print("ERROR: pdftoppm not found at the expected path.")
        print("Check that Poppler is installed via winget.")
        return

    total = 0
    for edition, pdf_path in PDFS.items():
        if not pdf_path.exists():
            print(f"  [{edition}] PDF not found: {pdf_path.name} -- skipping.")
            continue
        total += split_pdf(edition, pdf_path)

    print()
    print(f"Complete. {total} total page images across all editions.")
    print()
    print("Next step: build chapter_map.csv to connect PDF pages to")
    print("book chapters for each of the three editions.")


if __name__ == "__main__":
    main()
