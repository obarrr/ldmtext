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

- **2026-09-03**: Sessions A–E run in one session for page 631 (Moroni
  10:32-34), first footnote 4659, Moroni 10 letters y-2c (5 footnotes,
  4659-4663). **THIS IS THE FINAL PAGE OF THE BOOK OF MORMON.** Page
  CONTINUES and FINISHES Moroni 10 (last chapter). Page 630 ended
  mid-verse 10:32 ("...y si por la gracia de Dios os hiciereis"), so
  page 631 OPENS mid-verse with the continuation ("perfectos en Jesu
  Cristo, de ningún modo negaréis entonces el poder de Dios.") —
  "Página 631" on its own line, body on the next line, NO blank line
  after the marker, NO heading (rule 1). Body = 12 print lines, ends
  "...vivos y muertos. Amén." (Moroni 10:34). Nothing printed after it
  — no "FIN", no colophon (mid/bot crops blank; 1886 file p.644 also
  ends with only a decorative flourish after "Amen."). Running header
  "CAP. X.) LIBRO DE MORONI. 631" discarded (rule 2). No page-boundary
  word split (rule 10 N/A), no hyphen rejoins (rule 7 N/A). Rule 8
  cascade: the 5 markers pushed raw lines 9-11 past 72 chars, cascading
  three word-moves ("reunan"+[4662], "encontraros", "Eterno de" each ->
  next line start); output stays 12 body lines. Rule 6: 2 sentence
  double-spaces collapsed (v.34 "de todos.  Pronto", "muertos.  Amén.").
  Rule 31 N/A (no body semicolons this page). Rule 36: faint speck
  between "34." and "Ahora" (v.34) — Google OCR (page_0653.txt) AND
  1886 file p.644 both print clean "34. Ahora"; stray debris,
  transcribed without it, NOT logged. 5 markers: 10y=[4659] "ningún"
  (v.32); 10z=[4660] "derrame" (v.33); 10-2a=[4661] "paraíso" (v.34);
  10-2b=[4662] "reunan" (v.34); 10-2c=[4663] "agradable" (v.34). Block
  1: 10y "Véase e, III Nefi 29."; 10z "Véase f, II Nefi 2."; 10-2a
  "Véase l, II Nefi 9."; 10-2b "Véase d, II Nefi 2."; 10-2c "Jacob
  6:13." Same book, same chapter -> Block 1 gets NO blank line / NO
  book header (rule 20). MANDATORY i/l/1 check — 10-2a's cross-ref
  target letter: the 1920 fn-block superscripts on this page are ALL
  heavily over-inked blobs (entry letters AND every "Véase" target
  letter unreadable from the 1920 glyph alone), so all 5 entries were
  resolved entirely from 1879 file p.631 (Moroni 10 fn continuation,
  letters r-2c, clean italic type): "y, see e, III. Nep. 29. z, see f,
  II. Nep. 2. 2a, see l, II. Nep. 9. 2b, see d, II. Nep. 2. 2c, Jacob
  6:13." The 2a target letter is an unmistakable "l" — plain tall
  ascender, no dot/descender/crossbar — contrasting the dotted,
  below-baseline "j" of "x, see j," directly above it. NOT "i".
  Content-fit: 10-2c "Jacob 6:13" on "el agradable tribunal del gran
  Jehová" — Jacob 6:13 = "la agradable barra de Dios" ("the pleasing
  bar of God"), exact match; 10-2a "II Nefi 9" (Jacob's resurrection/
  paradise discourse) on "el paraíso de Dios" — strong fit for "l".
  Session B: fresh independent 1920 fn-block crop (8x) + fresh
  body-marker crops (5x) + fresh 1879 file p.631 crop — all 5 Block 1
  entries and all 5 markers UNCHANGED; 10-2a "l" re-confirmed. Session
  C: insert_body_text.py 631 — librodm.txt 33070->33084 (+14);
  librodm_foot.txt 4993->4998 (+5, NO blank line / NO book header, rule
  20). Página sequence 620..631 contiguous; "Página 631" appears once.
  Session D: generate_block2.py 631 appended 4659-4663 (librodm.txt
  33084->33089) — no unresolved warnings, no wrapped/compound-entry
  bugs (none of the 5 entries wrap). 4659->4016 (III Nefi 29e, text
  cites "...Moroni 7:35-38; 10:19-29." — reciprocal); 4660->265 (II
  Nefi 2f); 4661->369 (II Nefi 9l, text = "Alma 40:12,14; IV Nefi
  1:14; Moroni 10:34." — cites this exact verse, reciprocal);
  4662->263 (II Nefi 2d); 4663 direct "Jacob 6:13." Anchor<->Block-2:
  max anchor 4663 = max def 4663, contiguous 1..4663, no gaps/dupes,
  only the documented Jacob 2:15/812 def-without-anchor. Session E:
  fresh full pptext report report_wsl_20260903e2.html walked end to
  end. SPELLCHECK: ZERO new page-631 suspects ("perfeccionáis",
  "negaréis", "vengáis", "seréis", "reunan" all unflagged) — NO
  permitted words.txt additions. Every other page-631 pptext hit is a
  known structural false positive (short-lines flood over 12 body lines
  + 5 Block 2 entries; the page 630/631 mid-verse boundary
  "...os hiciereis" in the "unexpected paragraph end" list — the book
  now ends on a complete sentence so page 631's own last line is NOT
  flagged). NO page-631 findings in edit-distance / repeated-word /
  duplicate-line / adjacent-space / trailing-space / character /
  scanno / curly-quote / spaced-punctuation / special-situations /
  book-level / "full stop followed by unexpected sequence". Jeebies
  clean. Footnote check: union of both buckets = 4643-4663 contiguous,
  no dupes, no out-of-range. Dash check: the 5 new Block 2 entries have
  NO hyphens; letter-hyphen-letter blind-spot scan of the page-631
  segment = 0 tokens. Whole-document mechanical sweeps all clean
  (check_spaced_punctuation librodm.txt 33089; check_footnote_punctuation
  librodm_foot.txt 4998; check_verse_indent librodm.txt; curly-quote
  scan of librodm.txt / librodm_foot.txt / page_631.txt all zero;
  anchor<->Block-2 only [812]). 1886 comparison — Moroni 10:32-34 ALL
  on 1886 file p.644 (book p.626); the ENTIRE text of page 631 compared
  word-for-word. NO genuine 1920 deviations; NO errors-in-1920 entry.
  Differences all previously-established house style: (a) 1920 supplies
  acute accents 1886 omits — "perfeccionáis"/"negáis"/"vengáis"/
  "ningún" for 1886 "perfeccionais"/"negais"/"vengais"/"ningun"; (b)
  1920 modernizes 1886 archaic forms — "entonces"<-"entónces" (x2),
  "remisión"<-"remision", "aire"<-"áire", "paraíso"<-"paraiso"; (c)
  "Jesu Cristo" unhyphenated vs 1886 "Jesu-Cristo" — documented
  legitimate archaic form (feedback_jesu_cristo_hyphen); (d) "Amén" vs
  1886 "Amen" — acute-accent modernization, document-wide; (e) v.34
  sentence double-spaces present in 1886 too — collapsed per rule 6.
  1886 also ends the Book of Mormon here. feedback_narrow_space_vs_merge:
  nothing noticed. NO text changes to page_631.txt or librodm.txt in
  Session E.

- **Next page**: NONE — page 631 was the final page. The Book of
  Mormon body transcription (pages 437-631, Sessions A–E) is COMPLETE.
  Remaining project-level cleanup: (1) DONE 2026-09-03 —
  `generate_block2.py --fix-unresolved` run on the finished document;
  re-resolved 0 (all resolvable cross-refs were already resolved
  page-by-page in each Session D). One compound entry (4341, Moroni 4d)
  fixed by hand -> `Véase 102; ...`; one dead reference (4013, III Nefi
  29b `Véase 2j, III Nefi 15` — no such letter, likely a 1920 misprint)
  left in letter form and flagged for the editor. See sessions-log.md.
  (2) IN PROGRESS — full-document pptext review (all categories except
  short lines), findings in `workspace/fulltext_pptext_review_20260903.md`.
  Editor working through it. 2026-09-05: rechecked the review file's
  period-for-comma list — its "not yet logged" sub-list was wrong, ALL
  of those are already in errors in 1920.txt (grep-detection artifact).
  Editor then worked the whole category — 9 reversals, each with the
  errors-log entry deleted and the text corrected as a PRINT DEFECT
  (not a textual error): Helamán 13:22 "envidia.", IV Nefi 1:14
  "pasado ya.", Helamán 9:6 "al pueblo.", III Nefi 24:15
  "orgullosos.", IV Nefi 1:2 "disputas." (defective/weak commas →
  comma); III Nefi 1:13 "por. boca", III Nefi 9:22 "quienquiera. que",
  III Nefi 28:15 "poder. contemplar", Mormón 4:11 "corazón.se" (stray
  specks → mark removed). Helamán 9:4's entry enriched with a fresh
  1886 check; the rest confirmed genuine and staying logged. A 10th
  print-defect reversal followed: Helamán 8:21 "ha-sido" -> "ha sido"
  (the "hyphen" is a stray speck; 1920 writes "ha sido" correctly one
  clause earlier), errors-log entry deleted.
  **Editor rule established:** `errors in 1920.txt` is for TEXTUAL
  errors only (wrong/misspelled/missing words, a punctuation mark
  genuinely set wrong) — print defects (stray specks, weak/broken/
  half-inked type) are fixed silently, not logged. See
  `feedback_errors_log_textual_not_print`.
  §5A/§5B done (2026-09-05): compound-ordinal / "sumo-sacerdote"
  line-splits rejoined onto one line (Helamán 6:1/6:14/6:33, III Nefi
  6:22; page files synced); Mosíah 11:11 "sumosacerdotes" hyphen
  restored; Helamán 11:3 "septusgésimo-tercio" errors-log entry
  enriched (already logged).
  §5C done (2026-09-07): (a) `II Crónicas 36, 14-20` footnote (I Nefi
  3d / fn 15) — faithful 1920 misprint (comma for colon), preserved as
  printed, NEW errors-log entry "Footnote 1 Nefi 3d, 15". (b) Footnote
  "Verículo/Verículos" (missing "s") family — faithful 1920 misprints,
  preserved as printed, ALL logged: Mosíah 1b/3m/4d/4h/5e/6d/8n/8p. (c)
  Footnote "Versiculo/Versiculos" (missing í-tilde) family — faithful
  1920, preserved as printed, ALL logged under a master entry at
  "Footnote 2 Nefi 9i, 366" (+ Omni 1i, Mosíah 18b/18c/18d, Alma
  14h/17w/21q/30-2e/34k/60r, Éther 14e; Alma 60r's Block-1 text also
  corrected back to unaccented to match). (d) `Alma:1:27,30`→`Alma
  1:27,30` (fn 1125) — transcription slip, fixed silently, not logged.
  (e) `I Nefi 1:4, 2:4`→`I Nefi 1:4; 2:4` (fn 1144) — house-style
  normalization, fixed silently. (f) `Véase; 2c` stray semicolon
  (Mormón 2e / fn 4084) — 1920 misprint already logged; the `;` was
  normalized out (it blocked `generate_block2.py`'s "Véase " resolver),
  then `--fix-unresolved` re-resolved fn 4084 → `Véase 4057.`;
  page_556.txt notes synced. (g) `;,` double punctuation (I Nefi 22o /
  fn 242) — transcription artifact, comma removed, not logged. (h)
  BONUS, surfaced during §5C: Mormón 2:6 has a genuine SPURIOUS footnote
  superscript (before "fuímos", no matching a–g entry; 1879 + Google
  OCR both show nothing there) — reclassified from the page-556
  Session-A "stray speck" call and NEWLY logged; not transcribed as a
  `[N]` marker. (i) `4d, 1117` also carried `Alma ...; 22:13,42: 26`
  — the `,` had to be a chapter-separating `;` (Alma 22 has only 35
  verses, so `22:42` is impossible; `42:26` fits the ascending order),
  plus a stray space; normalized to `22:13; 42:26`, fixed silently.
  §5C fully DONE — all 8 review rows closed.
  Footnote spaced-colon sweep (2026-09-07, prompted by the `4d` find):
  swept `librodm_foot.txt` + `librodm.txt` Block 2 for `<digit>: <digit>`
  in citation text. Fixed silently — 20 lines: 16 stray-space
  closures (`I Nefi 22: 8-12` → `22:8-12`, etc.) + 2 cases where `: `
  stood in for a chapter separator (`Moroni 7:...,48: 8:3` → `48; 8:3`;
  `Alma 21:9: 34:9` → `21:9; 34:9`), each done in both files. The
  `seqnum:`-prefix spaces (`4267: 1000 años…` etc.) were protected, not
  touched. Noticed in passing, NOT fixed (need image checks): footnote
  spelling typos `Doctrinas y Conveniós` (foot 671) and `Doctrinos y
  Convenios` (foot 387 / Block 2 28455).
  Still open in the review
  file: §5D, §5E, §6 (`LIBRO DF MORMON` header typo),
  Bienamado/Bien-amado, permitted-words housekeeping.
  (3) STILL TO DO — the blanket-suppression pptext re-run with
  `permitted words.txt` set aside, cross-referencing every fresh flag
  against `errors in 1920.txt` (see the orthography-check skill).
  Chapter emailing (Session F) continues independently.
- **Completed pages**: 437–631, Sessions A–E fully done through page
  631 — the entire Book of Mormon.

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
