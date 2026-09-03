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

- **2026-09-04**: Sessions A–E run in one session for page 627 (Moroni
  9:10-22), first footnote 4629, Moroni 9 letters e-f (2 footnotes,
  4629-4630). Page CONTINUES the Book of Moroni and Moroni chapter 9 (no
  book header, no chapter heading, rule 1). Page 626 actually ended with
  Moroni 9:9 COMPLETE ("...que era la castidad y la virtud;" — 1920
  renders the modern em dash after "virtue" as a semicolon), NOT
  mid-verse as page 626's "Next page" note anticipated — page 627 OPENS
  with a fresh verse number "10." (rule 1 treatment identical either
  way). Running header "CAP. IX.) LIBRO DE MORONI. 627" discarded (rule
  2). Page ENDS with v.22 COMPLETE ("...ó de su entera destrucción."); no
  page-boundary word split (rule 10 N/A). Body = 44 output lines (= 44
  print lines). Rule 7: 3 hyphen rejoins — "conside-/rándolo" →
  "considerándolo" (70, kept); "los La-/manitas" → "Lamanitas" (68,
  kept); "sufri-/mientos" → "sufrimientos" (69, kept). Rule 8: no
  rebalance (longest = 71, v.22 line with [4630]). Rule 31: ×11 de-spaces
  before ";"/":"/"!" (1920 spaces these throughout the page). Rule 6: ×3
  sentence double-spaces collapsed. No zero-width merges, no
  narrow-space-vs-merge flags. Rule 22: Block 1 9e "Mormón 2 : 9." →
  "Mormón 2:9.", 9f "Mormón 8 : 3." → "Mormón 8:3." 2 markers: 9e=[4629]
  "Aarón" (9:17, "huido al ejército de Aarón"; 1879 "fled to the army of
  (e)Aaron"); 9f=[4630] "conserve" (9:22, "que te conserve la vida"; 1879
  "that he would (f)spare thy life", rule 26). Block 1: 9e "Mormón 2:9.",
  9f "Mormón 8:3." — both direct citations. MANDATORY i/l/1 check NOT
  triggered (entry letters e, f; no cross-ref target letters).
  Discretionary 1879 cross-check run on 9e (over-inked blob on the 1920
  scan): Moroni 9 vv.17-22 fall on 1879 file p.628 (NOT p.627 — 1879
  pagination doesn't track 1920). 1879 file p.628 fn-block, clean italic
  type: "e, Mor. 2 : 9.   f, Mor. 8 : 3.   g, Ether 13—[wrap] 4 : 11, 12.
  i, I. Nep. 13 : 31.   Alma 45 : 14." — 9e unambiguous italic "e", 9f
  unambiguous "f"; g/h/i annotate Moroni 9:23-25 (1920 page 628). 1879
  body markers: (e) before "Aaron" v.17, (f) before "spare" v.22. Google
  cross-check page 0649: 3 candidates — (1) v.13 "abominaciones--" vs
  Google "abominaciones" (Google drops trailing dashes); (2) v.17
  "Lamanitas" vs Google "Lȧmanitas" (stray OCR dot); (3) v.18 "He aquí;"
  vs Google "He aquí," (comma) — Session A/E zoom wrongly read a
  semicolon; the editor's direct look at the scan (2026-09-04) confirmed
  Google was right, the mark is a plain comma + stray speck (rule 36), so
  v.18 CORRECTED to "He aquí," in page_627.txt + librodm.txt. Google
  INDEPENDENTLY reads v.17 "ejírcitos" the same (í, not é). Session B: fresh independent fn-block
  crop (16×), body-marker crops (18×), 1879 file p.628 cross-check — all
  entries and markers UNCHANGED; over-inked "e" blob resolved off 1879's
  clear type. Session C: insert_body_text.py 627 — librodm.txt
  32865→32911 (+46); librodm_foot.txt 4963→4965 (2 Block 1 entries, NO
  blank line / NO book header — Moroni ch.9 continues, rule 20). Página
  sequence 620..627 contiguous. Session D: generate_block2.py 627
  appended 4629-4630 (librodm.txt 32911→32913) — both direct citations,
  no unresolved warnings, no wrapped-Block-1-entry bug. Anchor↔Block-2:
  max anchor 4630 = max def 4630, contiguous 1..4630, no gaps/dupes; only
  the documented Jacob 2:15/812 def-without-anchor remains. Session E:
  fresh full pptext report report_wsl_20260902e.html regenerated and
  walked end to end. SPELLCHECK: 1 new suspect — "Zenefi" (9:16), a
  Book-of-Mormon proper noun; 1886 file p.640 ALSO "Zenefi" (1879 /
  modern BoM "Zenephi"). ADDED to permitted words.txt (rule 10), NO
  errors-log entry (proper noun, shared with 1886). permitted words.txt:
  1288→1289. 1886 comparison — Moroni 9:10-18 on 1886 file p.640,
  9:18-22 on file p.641 — ALL of Moroni 9:10-22 compared word-for-word.
  ONE genuine 1920 deviation LOGGED in errors in 1920.txt (913→914,
  book-order append, Moroni 9 = true end): **Moroni 9:17 "ejírcitos"
  (ejércitos)** — 1920 prints "ejírcitos" (í for é) where the SAME verse
  prints "ejército" correctly twice; 1886 file p.640 "ejércitos" CORRECT
  (1920-ONLY error); zero corpus hits, aspell flags it standalone
  (→"ejércitos"); modern BoM "los ejércitos de los lamanitas"; 1879 "the
  armies of the Lamanites"; NOT in the full pptext Spellcheck section
  (same whole-document suppression as "Poi"/"dsesaría" pp.469-470,
  "bautizeis" Moroni 8:9), so NO permitted-words entry (no-op); preserved
  as printed. **Withdrawn intra-session:** a Moroni 9:18 "He aquí; que"
  (He aquí, que) entry was drafted and appended (913→915), then REMOVED
  after the editor's direct look at the scan showed the mark is a plain
  comma with a stray speck, not a semicolon — v.18 CORRECTED to "He aquí,"
  in page_627.txt + librodm.txt (a correct comma, no error; rule 12/36).
  errors in 1920.txt back to 914 lines. (My mistake: I had dismissed
  Google's comma reading as "normalization" instead of treating it as
  evidence — the exact failure rule 36 warns against.) NOT logged: (a)
  v.11 "civilización--", v.13 "abominaciones--" —
  1886 file p.640 ALSO prints an em dash at both (em-dash-representation
  convention, see below); (b) 1886 typos/accent drops "anmentado",
  "extension del pais", "órden", "hijo mio" — 1920 correct; (c) v.15 1886
  "Hé aquí que clama" no comma vs 1920 "He aquí, que clama" — 1920
  house-style comma addition. DASH CHECK: pptext's em-dash bucket flagged
  librodm.txt lines 27886/27890 — this page's Session A transcription
  used the real U+2014 em-dash char for "civilización—"/"abominaciones—".
  Per the documented dash convention (em-dash → "--"), BOTH converted to
  "--" in pages/page_627.txt AND librodm.txt. (Body-text changes this
  session: the ×2 em-dash → "--", plus v.18 "He aquí;" → "He aquí,"
  stray-speck correction. The ejírcitos error preserved as printed.)
  WHOLE-DOCUMENT em-dash cleanup (same session): the scan found 6 more
  U+2014 chars in librodm.txt from earlier pages — 20739+20742 (Helamán
  10:3), 23224 (III Nefi 16:4), 24206 (III Nefi 27:8, a ";—" pair),
  26053 (Éther 3:26), 26958 (Éther 12:28). Each verified against its own
  page's Session A note as a genuine em dash, none masking a
  transcription error ("mí—fuente" = "unto me—the fountain"; the earlier
  "má" worry was my misread). All 6 → "--" in librodm.txt and their page
  files (462/519/542/584/605, body only), plus the two already-emailed
  archive copies (chapters_emailed/Helaman_10.txt ×2, III_Nefi_16.txt ×1
  — NOT resent, archive-consistency per the 2026-07-24b/07-25
  precedent). librodm.txt / librodm_foot.txt / all chapters_emailed/*.txt
  now hold ZERO U+2014 (only _log.txt keeps 2, in its own prose
  comments). Whole-document mechanical sweeps
  clean (check_spaced_punctuation librodm.txt 32913;
  check_footnote_punctuation librodm_foot.txt 4965; check_verse_indent
  librodm.txt; anchor↔Block-2 only [812]; curly-quote scan zero). Jeebies
  clean. No page-627 edit-distance / repeated-word / duplicate-line /
  ellipsis / adjacent-dashes / scanno / special-situations / book-level /
  "full stop followed by unexpected sequence" findings. Short-lines +
  "unexpected paragraph end" page-627 hits are the usual structural
  verse-boundary false positives.
- **Next page**: 628, full A–E cycle, first footnote 4631. Page 627
  ended with Moroni 9:22 COMPLETE ("...ó de su entera destrucción.") —
  page 628 OPENS mid-chapter with Moroni 9:23 (no blank line, no chapter
  heading; rule 1). Moroni 9 continues (letters keep climbing from 9f;
  global number from 4630). Per the 1879 file p.628 fn-block seen this
  session, page 628's markers are g (Ether 13—...), h (Mormón 4:11-12),
  i (I Nefi 13:31) and likely j (Alma 45:14) — annotating Moroni 9:23-25.
  1879 Moroni 9 tail = file p.628; 1886 Moroni 9 tail = file p.641 (which
  also begins Moroni 10). Moroni 10 (the last chapter of the Book of
  Mormon) = 1920 file p.650, 1879 file p.627, 1886 file p.641
  (chapter_map has all Moroni rows). KNOWN generate_block2.py bugs to
  watch in Session D: (a) the wrapped-Block-1-entry spurious-trailer bug
  — if any Block 1 entry wraps to a second line, after Session D check
  the Notas tail for a stray "PRIMER LIBRO DE NEFI" / duplicate "NNNN:"
  block after the last real entry and delete it; (b) a COMPOUND Block 1
  entry ("Véase X, y Y" / "Véase X; También Y") may be left in letter
  form or mis-resolved — resolve by hand. (The whole-document U+2014
  em-dash cleanup that was flagged here is DONE — see the 2026-09-04
  entry above; librodm.txt and all chapter archives now hold zero
  U+2014.)
- **Completed pages**: 437–627, Sessions A–E fully done through page 627.

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
