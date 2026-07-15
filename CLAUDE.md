# Libro de Mormón 1920 — Project Guide for Claude Code

## Paths
- **On Desktop-6p05aa1 (remote)**: `D:\Users\Robert O'Barr\Documents\My Documents\family\robert\bofm\libro_de_mormon_1920\`
- **From local machine via mapped drive**: `Z:\Users\Robert O'Barr\Documents\My Documents\family\robert\bofm\libro_de_mormon_1920\`
- **UNC (fallback)**: `\\Desktop-6p05aa1\d\Users\Robert O'Barr\Documents\My Documents\family\robert\bofm\libro_de_mormon_1920\`
- Start Claude Code sessions from whichever path applies to the machine you are on.

## Project
Transcribing the 1920 Spanish Libro de Mormón for Project Gutenberg.
Three source PDFs: 1920 (primary), 1879 Pratt English (footnote disambiguation),
1886 Spanish (error checking). All pre-rasterized at 400dpi into subfolders.

## Folder Layout
```
libro_de_mormon_1920/
├── CLAUDE.md                  this file
├── libro_de_mormon_rules.md   authoritative transcription rules — READ FIRST
├── chapter_map.csv            book/chapter to file-page lookup (all 3 editions)
├── librodm.txt                primary output: body text + Block 2 footnotes
├── librodm_foot.txt           Block 1 (chapter+letter) footnotes output
├── permitted words.txt        pptext good-words list
├── errors in 1920.txt         documented 1920 original errors
├── pages/                     completed page transcriptions (page_437.txt …)
├── workspace/                 temporary drafts, fn_check files, test files
├── pages_1920/                pre-rasterized 1920 PNGs: page_0001.png …
├── pages_1879/                pre-rasterized 1879 PNGs
├── pages_1886/                pre-rasterized 1886 PNGs
└── [scripts]                  all .py scripts live here at project root
```

## Key Constants
- **1920 offset**: file_page = book_page + 22 (chapter_map stores FILE pages)
- **1879 offset**: file_page = book_page + 8
- **1886 offset**: file_page = book_page + offset (TBD per section)
- Footnote numbers run sequentially across the entire document, never restart.
- Footnote letters restart at `a` at the beginning of each chapter.

## Review Pass — One Step Per Session
**Do each step in a separate Claude Code session.** This keeps context small,
avoids timeouts, and lets the user review results before proceeding. Full
instructions for each step live in its own skill, loaded automatically the
moment its trigger phrase is used — so only the step you're actually
running is ever in context, not all five at once.

- **Session A** — Transcribe the page. Trigger: "Transcribe page NNN[,
  first footnote NNNN]." (first footnote is auto-derived from the previous
  page file when possible — see the `transcribe-page` skill.)
- **Session B** — Verify footnote superscripts. Trigger: "Verify footnotes
  for page NNN."
- **Session C** — Insert body text and append Block 1 footnotes. Trigger:
  "Integrate pages NNN-NNN into librodm.txt and librodm_foot.txt."
- **Session D** — Generate Block 2 and append to librodm.txt. Trigger:
  "Generate Block 2 for page NNN."
- **Session E** — Orthography check. Trigger: "Orthography check for
  page NNN."

## Current Progress
- **Last completed**: pages 451–452 fully done, Sessions A–E all complete.
  `librodm_foot.txt` ends at footnote 3269; `librodm.txt`'s Notas section
  goes through 3269 too. Chapters Helamán 1–3 have been emailed (see
  `chapters_emailed/_log.txt`); Helamán 4 is transcribed but not yet sent.
  On 2026-07-13, Session E for pages 451-452 also swept the Corrections
  logs of every earlier page (437-450) per the mandatory check added to
  the `orthography-check` skill on 2026-07-12 — this was the first time
  that sweep ran at scale. It found and resolved 6 previously-undetected
  genuine 1920 errors (Helamán 4:5, 4:14, 5:10, 6:21 ×2, 6:22, 6:38 — see
  `errors in 1920.txt`) plus one incident where a Session A transcriber
  had silently "corrected" a suspected misprint (Helamán 4:5 "en al año"
  → typed as "en el año") instead of preserving it — now fixed in both
  `page_442.txt` and `librodm.txt`. Going forward this sweep only needs
  to run against newly-transcribed pages, not re-run from page 437 (see
  `orthography-check` skill's progress tracker for the exact cutoff).
  One known gap remains: `errors in 1920.txt`'s "Helamán 5:35 seperado"
  entry (logged 2026-07-11 or earlier) was never mirrored into
  `permitted words.txt`, unlike every other preserved-as-printed error —
  not yet fixed as of 2026-07-13.
- **2026-07-14**: user spotted that `errors in 1920.txt` had Alma-book
  entries scattered into the middle of the Helamán section, out of
  book/chapter/verse order. Root cause: two commits' worth of
  whole-document Session E sweeps (2026-07-12 and 2026-07-14) found
  confirmed errors spanning several already-transcribed books/chapters
  in a single pass, but all new findings were appended to the literal
  end of the file — which only produces correct order when every
  finding belongs to the page currently being transcribed. Fixed by
  reordering the file (verified as a pure line reordering — same
  535-line multiset before/after, nothing added/changed/lost) and by
  adding an explicit insert-in-order instruction to the
  `orthography-check` skill so future multi-book sweeps place each
  finding at its correct position instead of appending.
- **Next page**: 453 (Helamán 6 continues; next footnote 3270)
- **Completed pages**: 437–452 (in pages/ folder)

## Script Reference
- `process_page.py <png> <label> [first_fn]` — crops page into top/mid/bot/fn/fn_zoom
- `check_lines.py <file>` — flags lines ≥ 73 chars
- `crop_page.py` — zooms into a specific vertical band
- `insert_body_text.py <NNN> [NNN ...] [--footnotes-only | --body-only]` — Session C:
  inserts one or more pages' body text into `librodm.txt` before `Notas`,
  and appends their Block 1 entries to `librodm_foot.txt` (handling
  book-boundary headers automatically; see rule 20 note in the rules doc)
- `generate_block2.py <NNN> [NNN ...]` / `generate_block2.py --fix-unresolved`
  — Session D: resolves Block 1 cross-references to sequential numbers
  (book-aware) and appends Block 2 entries to `librodm.txt`; the
  `--fix-unresolved` mode rescans the whole document for previously-stuck
  cross-references now resolvable — run once the full text is done
- `draft_page.py` — OCR-based draft (experimental, not primary workflow)
- `verify_fn.py` — cross-checks 1920 footnotes against 1879 English
- `build_chapter_map.py` — OCR-scans pages to fill chapter_map.csv
