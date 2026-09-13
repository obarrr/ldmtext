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

- **2026-09-12**: OCR-diff pilot (`workspace/_pilot_ocr_diff.py`, diffs
  `librodm.txt` against the 1920 PDF's own embedded Google-OCR text) run
  to completion across the ENTIRE book, pages 1–631, in 23 batches over
  one extended session. Originally scoped to 1–436 (the range that never
  got this project's image-reverification pipeline nor the
  Google-OCR-crosscheck tool); after the 1–436 sweep finished clean, the
  editor asked to extend it through 437–631 too, since a real bug found
  late in the 1–436 pass (see below) proved the diff catches
  integration-stage errors even in the already-tracked Session A–E
  range. Full batch-by-batch methodology, resource costs, and the
  complete false-positive taxonomy live in `workspace/diff1920ocr-trans.md`
  (batches 1–23) — read that file, not this summary, for any question
  about why a specific page/verse was or wasn't flagged.
  **1–436 results:** 10 silent transcription-slip fixes + 1 newly logged
  archaism (2 Nefi 8:12 "Quíen") from the systematic diff, overwhelmingly
  concentrated on book pages 1–2 (pages 3–436 were otherwise very clean
  after noise-filtering). One real bug: a "Página 411" marker was
  misspelled "Pagina 411" (missing the accent), silently breaking
  page-boundary detection for any script keying off that literal string
  — found and fixed (batch 16). 3 period/comma print-defect ambiguities
  flagged for the editor's own inspection, deliberately NOT resolved
  unilaterally (see `diff1920ocr-trans.md`'s running flagged list).
  Separately, at the editor's request, a manual full-image spot-audit of
  book page 337 (Alma 32:37) — done outside the regular diff-batch flow,
  word-for-word against the image plus 1886, independent of the Google
  diff — found 2 MORE real errors ("empieze" for "empiece", and "he
  aqui"/"he aquí" missing its accent twice) that the diff-based method
  structurally cannot see: it only catches OCR *disagreement* between
  the transcription and Google, so a clean, unambiguous misprint that
  both sides read identically produces zero diff signal. This is the
  pilot's known blind spot, confirmed directly in batch 13 when Google's
  own raw OCR text for that same page was checked and found to read the
  identical (wrong) unaccented spelling.
  **437–631 results (batches 18–23, run after extending scope):** pages
  in this range have `pages/page_NNN.txt` working files from the
  original Session A–E work, so before finalizing any comma/period/
  stray-mark candidate here the protocol was to check that page's
  Corrections section first (several apparent defects turned out to
  already be documented "scan/print artifact of this particular copy"
  calls — pages 472, 475 — determined NOT to be real 1920 errors on
  closer inspection). Found: 1 more silent accent-slip fix (Helamán
  4:9 "Moronihah"→"Moroníhah", didn't match the image); 3 new
  `errors in 1920.txt` entries covering 5 instances — Helamán 4:6
  "Moronihah" unaccented (shared with 1886), Helamán 8:23 "he aqui, El
  es Dios" missing both accents (1920-exclusive), and Helamán 8:27's
  cluster of FOUR "punto por coma" defects in one verse (all
  1920-exclusive, confirmed against 1886) — the last two both on the
  SAME page (458), whose dense 19-candidate cluster in the raw diff is
  what triggered the closer look; and 1 integration-stage regression
  caught and reversed: book page 510's chapter heading, already
  carefully verified during Session E as a genuine 1920 misprint
  ("CAPTULO 12.", missing the Í) and correctly preserved in
  `pages/page_510.txt`, had drifted back to its corrected spelling
  ("CAPÍTULO 12.") in `librodm.txt` at some point after Session C
  integration — restored to match the verified misprint. Every other
  non-routine-looking candidate across 437–631 (batches 20–23 in
  particular) turned out to already be thoroughly documented and
  resolved in that page's own notes, confirming that range's existing
  Session A–E work is generally solid — the pilot's value there was
  specifically in catching integration/drift-stage slips the per-page
  pipeline structurally can't see, not in finding fresh transcription
  errors.
  **Editor's plan going forward** (set 2026-09-12): treat this
  diff-based pilot as a cheap, now-complete first pass across the whole
  book. Next: a separate, more expensive manual page-by-page
  proofreading pass (full image read, word-for-word comparison, 1886
  cross-check — same method as the page-337 spot-audit) — not yet
  started, batch size/starting point to be decided with the editor. Also
  still open from before: diagnosing why a whole-document pptext run
  with `permitted words.txt` suppressed apparently flagged "empieze" as
  a suspect word without an `errors in 1920.txt` entry resulting from
  it — relevant to item (3) below.

- **Next page**: NONE — page-by-page transcription (pages 437–631,
  Sessions A–E) has been complete since 2026-09-03; see that work's full
  history in `sessions-log.md` (search `\b631\b` or earlier page
  numbers). Current focus is document-wide quality passes, not new
  pages. Remaining project-level work: (1) DONE — full-document pptext
  review (§1–6) and the `permitted words.txt` reverse-consistency audit
  (Category A/B, batches B1–B7) both completed 2026-09-08–10; full
  detail in `sessions-log.md`. (2) DONE 2026-09-12 — the OCR-diff pilot
  now covers the entire book, pages 1–631 (see above); full detail in
  `workspace/diff1920ocr-trans.md`. (3) STILL TO DO — the
  blanket-suppression pptext re-run with `permitted words.txt` set
  aside, cross-referencing every fresh flag against
  `errors in 1920.txt` (see the `orthography-check` skill); this is
  also where the open "empieze"/pptext discrepancy noted above should
  get resolved. (4) IN PROGRESS (started 2026-09-12) — the manual,
  image-based, chapter-by-chapter proofreading pass that the OCR-diff
  pilot's findings motivated; see "Editor's plan" above and the new
  `manual-proofread` skill. Front matter through 1 Nefi 4 done so far;
  a recurring pattern worth noting is the transcription occasionally
  having silently "corrected" a genuine 1920 misprint toward the
  standard spelling (1 Nefi 1:16, footnote 4a) — worth watching for
  elsewhere. Full running log, per-chapter findings, and the
  current-progress line (next unit to do) all live in
  `workspace/proofread-1920.md` — read that file for status, not this
  paragraph. Chapter emailing (Session F) continues independently.
- **Completed pages**: All of it. `librodm.txt` contains the entire Book
  of Mormon, book pages 1–631 (1 Nefi 1:1 through Moroni 10:34). Pages
  437–631 went through the full tracked Session A–E per-page pipeline;
  pages 1–436 went through an earlier editorial pass (458 pre-existing
  `errors in 1920.txt` entries) plus the now-complete OCR-diff pilot
  (item 2 above) — see that pilot's summary for what is and isn't
  covered by "checked" for this range (it catches OCR-disagreement-shaped
  errors, not every possible error type; see the page-337 spot-audit
  note above).

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
