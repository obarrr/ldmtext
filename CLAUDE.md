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
├── viewer/                    manual-check viewer app (see Script Reference:
│                               build_viewer_data.py) — open viewer/index.html
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

**Exception — explicit multi-session request.** If the user explicitly asks
for a range of sessions in one go ("apply Sessions A through E to page NNN",
"do A–E for page NNN", "run all five sessions for page NNN"), that means:
run every session in that range, in order, in this one session, WITHOUT
stopping to ask for permission or confirmation between steps. Do not pause
after Session A to ask whether to continue — the user already answered that
by naming the range. Report results as you go, but keep going through
Session E (and update Current Progress / sessions-log.md at the end as
normal). Only stop early if a step hits a genuine blocker that needs the
user's judgment.

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

- **2026-10-16/17**: Final verification checks before freezing
  `librodm.txt` as `librodm_transcribed.txt` -- ALL SIX DONE. Full
  record, tools and every editor ruling: `workspace/proofread-1920.md`
  ("Current Progress" at the top, items 2-6 at the end).
  (1) three-way OCR (done 2026-10-11). (2) footnote accent sweep:
  FAMILIA entries Mosíah/Véase/Versículos/Éxodo recounted image by
  image. (3) every accent/punctuation log entry re-checked on contact
  sheets (335 entries): 4 overturned (Mormón 3:14, III Nefi 6:12,
  Mosíah 2:9, 2 Nefi 32:3). (4) accent-variant and single-occurrence
  word scans: 3 transcription fixes, ~25 misprints newly logged, new
  FAMILIA entries "grafía de época" and "zelo". (5) footnotes: all
  2,194 Block 2 cross-references verified, plus a comparison with the
  1879 Pratt notes (OCR, then image checks): 4 transcription fixes
  (III Nefi 14b, Mormón 4k, Jacob 4i/4j swap), 6 footnote errors
  logged. (6) blind random sample, 200 lines / 11,386 characters:
  0 letter/accent/punctuation errors, 1 spacing slip (fixed) -- 95%
  upper bound ~0.03% for the Project Gutenberg submission.
  Lesson saved to memory: italic footnote i/j are told apart by tail
  direction (i right, j left).

- **Next step**: freeze `librodm.txt` as `librodm_transcribed.txt`
  (after the editor commits), then start `librodm_cleaned.txt`. The
  plan, the editor's philosophy and the list of every place decisions
  are recorded: `workspace/error_table_20260909.md` (section "Where to
  look when building `_cleaned`"). Working file: `errores_1920_revision.xlsx`
  (one row per logged error in book order; the editor is filling in the
  1946 edition's readings and the Gutenberg/modern decisions -- do not
  regenerate it without `--merge <current file>`, which carries the
  editor's input over). Deferred to that phase: the pptext
  re-run without `permitted words.txt` (cross-check every flag against
  `errors in 1920.txt`) and the open "empieze" pptext question. Later,
  possibly: `librodm_modern.txt` built on `_cleaned`. Chapter emailing
  (Session F) continues independently.
- **1946 review -- where we are (updated 2026-10-23)**: the editor is
  checking every logged error against their printed 1946 Libro de
  Mormón (no 1946 scan in the repo; the editor reads it and reports).
  Plan: (1) Familias tab first -- for each FAMILIA, Claude gives ~5
  sample verses with the exact 1920 word, page and context (column D
  holds the suggested verses), the editor reports what 1946 prints, and
  Claude records it: result in column E (corrige todos / mantiene
  todos / mixto / no informa / corrige / reescribe), details in F, and
  the matching Errores rows in P/Q. (2) Then the single-error rows on
  the Errores tab, in book order. (3) Only after that, the Gutenberg
  and modern decisions (columns R/S; Familias G/H).
  **Done = Familias column E filled; Errores column P filled.**
  Status: 29 of 34 families done. NEXT: "j por g" (sample 1 Nefi 17:19
  aflijido/aflijirme, 2 Nefi 1:5 escojida, Alma 19:27 aflijirles, Alma
  61:2 aflijido, Moroni 2:1 escojido), then "todas los", adverbios en
  -mente, grafía de época, circum-. Then 1,144 single-error rows (20
  front-matter rows already done). Findings so far: 1946 drops the
  accent on the preposition "a" everywhere (1911 rule), so accent
  questions on "a" are "no informa"; 1946 keeps "cuando" + future; it
  sometimes rewords a verse instead of correcting a word. Before each
  write: back up the workbook to `workspace/`, check for a LibreOffice
  lock file, change only the cells involved.
- **Completed pages**: All of it -- book pages 1-631 plus front matter,
  transcribed, manually proofread (2026-10-10) and fully verified
  (2026-10-17).

## Script Reference
- `build_viewer_data.py NNN [NNN ...]` / `build_viewer_data.py --all` —
  added 2026-09-13. Data layer for `viewer/index.html`, a standalone
  static-HTML tool (open the file directly, no server) for a human,
  side-by-side manual check of the transcription against the source
  image: page image on top, transcription below, both very wide/short
  panes, scroll-synced. `--all` regenerates `viewer/all_pages.js` and
  `viewer/chapter_map.js` from the current `librodm.txt` /
  `librodm_foot.txt` / `chapter_map.csv` — re-run it after any of those
  change so the viewer doesn't go stale. Footnote markers are remapped
  from librodm's sequential numbers back to the chapter-local letter
  (a, b, c, ..., then 2a, 2b, ... past z -- keys like "51-2a"; fixed 2026-09-24, previously showed the raw number for those) parsed off each `librodm_foot.txt` entry's key, since
  that's what's actually printed as a superscript in the image. Per-page
  scroll-sync calibration (where the body/footnote divider and the
  page's first line fall in the image) is saved in the browser's
  localStorage as you adjust it, NOT in this repo — it's viewer-only
  convenience state, browser-local and not currently backed by a file,
  so a fresh browser/profile starts from the script's rough automatic
  guess again. Three independent markers are calibrated per page: where
  the first transcribed line starts, where body ends/footnotes begin,
  and where footnote text actually ends (added 2026-09-13 -- footnote
  text rarely runs to the image's literal bottom edge, so this is
  separate from the body/footnote divider rather than forcing it to do
  double duty). Front matter (title page, testimonies, table of
  contents -- "Pagina i" through "Pagina xiv" in librodm.txt) is
  included too (added 2026-09-13); it uses a DIFFERENT file-page offset
  than the main text (+8, not +22 -- confirmed against the actual scan
  images, not assumed) and is addressed by its roman-numeral label
  rather than a plain page number. Two front-matter pages (ii, vi) are
  blank in the original and have no "Pagina" marker at all, so they
  have no viewer entry; navigation just skips over them. This whole
  tool is fully static (open viewer/index.html directly -- no server,
  and it never reads librodm.txt/librodm_foot.txt/chapter_map.csv live;
  those are only read at --all build time), so after any edit to those
  master files the viewer will look stale until --all is rerun. To hand
  the viewer to someone else, package viewer/ (index.html, all_pages.js,
  chapter_map.js) together with pages_1920/ (~170MB of PNGs) -- nothing
  else is read at runtime. This is a live, still-evolving tool (not yet
  fully self-sufficient for headers/new-book pages) — see chat history
  for full design rationale if extending it.
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
- `measure_accent_mark.py <page_png> <top> <bottom> <left> <right> [threshold]`
  — added 2026-09-15 during the manual-proofread pass, after two specks
  (2 Nefi 10:3 "sú", 2 Nefi 10:21 "qué") were each initially misjudged as
  genuine accents by zoom + Google OCR and only caught by the editor's own
  direct look. Crops the given pixel box straight out of the already-
  rasterized 400dpi page PNG (no re-rasterization, unlike
  `measure_word_gap.py`), binarizes it, and runs connected-component
  labeling (`scipy.ndimage.label`), printing every blob's bounding box and
  dark-pixel area. Run once over the candidate mark+letter and once over a
  known-good accented letter on the same line/page, then compare: real
  accents in this font run ~50-70 dark pixels as ONE component merged
  (0px gap) with the letter below; both confirmed specks measured only
  ~9-10 dark pixels, fragmented into 1-2 tiny disconnected blobs sitting
  2-7px above the letter with a visible gap. See
  [[feedback_stray_mark_google_ocr_order]] for the full calibration data
  and how this fits into the check order (Google OCR, then zoom, then this
  pixel measurement, then still surface it to the editor before logging —
  this tool sharpens the call, it doesn't replace the escalation step).
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
