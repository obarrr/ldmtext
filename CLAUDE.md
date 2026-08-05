# Libro de Mormón 1920 — Project Guide for Claude Code

## Paths
- **On Desktop-6p05aa1 (remote)**: `D:\Users\Robert O'Barr\Documents\My Documents\family\robert\bofm\libro_de_mormon_1920\`
- **From local machine via mapped drive**: `Z:\Users\Robert O'Barr\Documents\My Documents\family\robert\bofm\libro_de_mormon_1920\`
- **UNC (fallback)**: `\\Desktop-6p05aa1\d\Users\Robert O'Barr\Documents\My Documents\family\robert\bofm\libro_de_mormon_1920\`
- **Local copy on C:\ drive**: `C:\Users\rober\Documents\libro_de_mormon\`
- Start Claude Code sessions from whichever path applies to the machine you are on.
  All scripts use paths relative to the project folder (confirmed via
  grep: no `.py` file hardcodes `Z:\`, `D:\Users`, or the
  `Desktop-6p05aa1` machine name), so any of the paths above works
  identically — this list is just documentation for picking the right
  one to `cd` into, not something the scripts or Claude parse.

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
This section holds only the most recent session entry as a snapshot of
current state. The full history of every session lives in
`sessions-log.md`. **When a new session finishes**: append its entry
to the end of `sessions-log.md` (same dated-bullet format), then
replace the single entry below (and the `Next page`/`Completed pages`
lines) with the new one — do not accumulate multiple entries here.

**`sessions-log.md` should be ignored by default** — it's large
(~184k chars) and not needed for routine transcription work. Only open
it when there's a genuine ambiguity about what was done on a specific
page (e.g. why a word/footnote/letter was resolved a certain way, or
whether a suspected error was ever investigated) and getting that
right matters for the current task. To search it: `grep -n "\bNNN\b"
sessions-log.md` (NNN = the page number), then scan the hits — entries
are chronological, not indexed by page, so a page number can also show
up as noise inside another page's entry (a 1879/1886 cross-reference
"file page NNN"/"book page NNN" citation). Prefer hits on a `- **`
bullet's own opening line (that entry's actual subject), but also
check body-text hits, since a later user-correction entry about page
NNN often doesn't repeat "page NNN" in its own header. If a page has
more than one matching entry, the latest date is the current, correct
state — earlier entries may have been reversed.

- **2026-08-04**: Sessions A–E run for page 581 (Éther 2:16-25,
  continuing chapter 2, ending mid-verse-25), footnotes 4302-4306,
  letters n-r (continuing chapter 2's alphabet from page 580's j-m).
  None of this page's five superscripts (n, o, p, q, r) are i/l/1, so
  the mandatory Section 8 1879 check did not apply to any of them;
  confirmed via direct zoom of each. Three hyphenated line-break splits
  rejoined per rule 7 (v.18 "dici-/endo" and "con-/struido", v.22
  "¿con-/sentirás"), none needing a rule 8 cascade. Footnote q (v.20
  marker "fondo") is an unusually long entry — a multi-sentence
  explanatory footnote (not just a bare citation) describing how the
  barges' two air-holes worked, ending in an "Éther 6:6,7,10." cross-
  reference; confirmed against 1879 (pages_1879/page_0583.png, same q
  footnote, English "Both of these air-holes...") to have the same
  structure and content. Two genuine 1920-only errors found within
  that footnote q text, both confirmed via 1879 since this edition of
  1886 carries no footnotes at all: "volteados." printed with a period
  where the sense continues as one clause (1879's "turned bottom
  upwards" is a single continuous clause, matching the pattern already
  logged for page 580 v.10 "posea."; also independently caught by
  pptext's "full stop followed by unexpected sequence" check) and
  "superficia" printed for "superficie" (1879's "surface" confirms;
  also independently flagged by pptext's spellcheck/edit-distance
  check, 1 occurrence vs. 69 elsewhere in the document). Both logged in
  `errors in 1920.txt` as "Éther 2:24 (nota q) volteados. (volteados,)"
  and "Éther 2:24 (nota q) superficia (superficie)"; `superficia` added
  to `permitted words.txt` per rule 10. V.24's "Puesque" (one word) was
  also flagged for review but turned out to need no action — already
  used 12+ times earlier in the document and already present in
  `permitted words.txt`, and 1886 (book page 577/file 595) prints the
  identical form, confirming it's a legitimate archaic spelling shared
  with 1886. Session B independently re-verified all 5 Block 1 entries
  and all 5 `[N]` body markers against fresh crops (not reused from
  Session A) — no discrepancies. `check_google_crosscheck.py` flagged
  two spots, both resolved as OCR noise after zooming (a dropped colon
  after "diciendo," and a stray inserted apostrophe at a line-wrap
  boundary, neither present in the actual print). Whole-document
  footnote-anchor/Block-2-definition cross-check re-run clean: zero
  duplicate definitions, zero anchored-but-undefined numbers beyond the
  already-documented Jacob 2:15/812 print-original gap; footnote-number
  range check (1-4306) also clean, zero duplicates, zero missing beyond
  812. Whole-document `check_spaced_punctuation.py`,
  `check_footnote_punctuation.py`, and `check_verse_indent.py` all
  clean on both master files.
- **Next page**: 582, full A–E cycle, first footnote 4307.
- **Completed pages**: 437–581, Sessions A–E fully done through page 581.

## Script Reference
- `process_page.py <png> <label> [first_fn]` — crops page into top/mid/bot/fn/fn_zoom
- `check_spaced_punctuation.py <file> [file2 ...]` — flags any line with a
  space immediately before a comma, semicolon, colon, "!", or "?" (rule
  31). Run on a page file before `check_lines.py` in Session A, and
  against `librodm.txt` (whole document) every Session E — added
  2026-07-24 after 91 such defects accumulated undetected across pages
  470-502 and `librodm_foot.txt`.
- `check_footnote_punctuation.py [file ...]` — defaults to
  `librodm_foot.txt`; flags a space before a comma/semicolon/colon or a
  spaced verse-range hyphen in footnote citation text (rules 22/23). Also
  useful against a page's own file (Block 1 entries share the same
  format). Added 2026-07-24 alongside `check_spaced_punctuation.py`.
- `check_lines.py <file>` — flags lines ≥ 73 chars
- `measure_word_gap.py <file_page> <top_pct> <bot_pct> [line_index] [dpi]`
  — added 2026-07-26. Use when a word pair looks suspiciously tight
  (candidate zero-width merge). Re-rasterizes that one page directly
  from the source PDF at high DPI (default 1200, well above the
  standard 400dpi transcription crop) via pdfplumber, splits the
  requested slice into individual text lines, and prints every
  column-darkness gap's pixel position/width plus an annotated image.
  Run once without `line_index` to see which detected line is which,
  then again with the index for the actual measurements. Compare the
  disputed junction's width to the *intra-word letter-kerning gaps in
  the same word*, not to other word-gaps on the line (justification
  stretches those unevenly). A ratio of at least ~2x means it's a real
  space; closer than that is genuinely ambiguous even at high DPI and
  belongs with the editor. See `feedback_narrow_space_vs_merge` — the
  standard 400dpi crop pipeline has been shown to understate real gaps
  by roughly an order of magnitude (page 517's "vino á"/"cuando Jesús",
  both confirmed real ~20px gaps that measured only 1px at 400dpi).
- `check_line_wrap.py <book_page> <file>` — advisory OCR-based cross-check
  added 2026-07-19 after page 475's line breaks were found to be entirely
  reflowed rather than image-derived (see rule 6 note in the rules doc);
  flags a body line count or length profile that looks wrapped-to-width
  rather than copied from the image. Not authoritative — a clean result
  doesn't prove the line breaks are right, only that they aren't grossly
  reflowed.
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
- `extract_google_text.py <book_page> [book_page2 ...]` — added 2026-07-25.
  Extracts the 1920 PDF's own embedded/Google-OCR text layer for a page
  (whole page, body + footnote block together — see script docstring for
  why cropping at the footnote divider isn't needed) into
  `google_text_1920/page_NNNN.txt`, UTF-8. Must specify `-enc UTF-8` (not
  this script's concern, it's pdfplumber-based — but a hard-won lesson if
  ever reaching for raw `pdftotext`: it defaults to Latin-1 output and
  silently mangles every accented character otherwise). Run once per page
  before `check_google_crosscheck.py`.
- `check_google_crosscheck.py <book_page> [page_txt_path]` — added
  2026-07-25, Session A step 10 (see `transcribe-page` skill). Diffs the
  transcribed body text against `google_text_1920/`'s text as a second
  opinion on letter-level misreads. Both sides are reduced to a single
  character stream with ALL whitespace and hyphens stripped before
  comparing — deliberately, so Google's frequent word-fusion (dropped
  spaces) can never surface as a diff at all, and can never be used to
  second-guess a narrow-space-vs-merge call
  (`feedback_narrow_space_vs_merge`) that rule already settled via
  1886/grammar. Short (<=2 char) surplus text on Google's side landing at
  a known footnote-marker position is auto-dismissed too (glued/dropped
  superscript letters are a known OCR weak spot, not worth zooming for).
  Everything else that survives is reported as a candidate: re-zoom,
  re-read, and resolve or flag per the usual rule-32 logic. First live
  run (page 504) caught one genuine, previously-undetected transcription
  error this way — see the 2026-07-25 entry below.
