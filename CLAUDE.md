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
- **Last completed**: pages 453–460 fully done, Sessions A–E all complete.
  `librodm_foot.txt` ends at footnote 3305; `librodm.txt`'s Notas section
  goes through 3305 too. Chapters Helamán 1–6 have been emailed (see
  `chapters_emailed/_log.txt`); Helamán 7 (spanning pages 453-460 plus
  more) is transcribed but not yet sent.
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
- **2026-07-15**: Session E run for pages 453-460 (a full-document sweep
  requested by the user, not just the new-page default). Pages 453-458
  needed no changes — already fully resolved in an earlier session.
  Found and resolved 6 new genuine 1920 errors in Helamán 9 (verses 4,
  6, 11, 14 — see `errors in 1920.txt`), all confirmed against 1886.
  Also closed a `permitted words.txt` mirroring gap: `aguasse` and
  `Isafas` had `errors in 1920.txt` entries but were never added to the
  good-words list (same gap pattern as `seperado`, which turned out to
  already be fixed — mirrored on 2026-07-14 or earlier, no longer an
  open gap as of this date). Dash check, footnote-number consistency,
  and curly-quote scan all came back clean for pages 453-460.
- **2026-07-17**: Sessions B–E run for pages 469-470 (Helamán 12:21-26,
  Helamán 13:1-14). Session B: footnotes verified against 1920 images;
  mandatory 1879 check for page 469's "i" letter (g/h/i/j cluster)
  confirmed against 1879 page 472 — matches the same-page glyph
  resolution already on file. Session C/D: body text, Block 1, and
  Block 2 all integrated cleanly via the scripts, footnote numbers
  3332-3341. Session E: found and confirmed 4 new genuine 1920 errors
  against 1886 (Helamán 12:22 "Poi lo tanto", 12:25 "dsesaría", 13:7
  "aninciado", 13:14 "conservada" — all in `errors in 1920.txt`); none
  needed `permitted words.txt` entries. Also discovered and documented
  a pptext quirk in the `orthography-check` skill: brand-new
  single-occurrence misprints can go unflagged in the full-document
  spellcheck report for reasons unrelated to the good-words list
  (confirmed via a minimal reproduction and direct aspell testing) —
  a clean pptext report is no longer sufficient on its own to clear a
  word 1886/RAE comparison already flags as wrong.
- **2026-07-18**: Sessions A–E run for pages 471-472 (Helamán 13:15-33).
  Session A: mandatory 1879 checks for page 471's i/j pair (footnote
  block g,h,i,j — the "i" glyph before "malditos" v.19 was initially
  mistaken for a curly opening quote, and the true "j" at v.24
  "desecháis" was initially misassigned as "i" by shape alone before
  the 1879 check and alphabetical-sequence reasoning settled it) and
  page 472's "l" (v.31 "resbaladizas") — both confirmed against BOM
  1879 Pratt (chapter_map Helamán 13, files 474/475). Session C/D:
  body text, Block 1, and Block 2 integrated cleanly, footnote numbers
  3342-3348. Session E: full pptext regeneration (`report_wsl_
  20260718.html`) found and confirmed 6 new genuine 1920 errors against
  1886 (Helamán 13:21 "también." for "también,", 13:21 "aunuciado" for
  "anunciado", 13:22 "requezas" for "riquezas", 13:22 "envidia." for
  "envidia,", 13:28 "cs" for "os", 13:28 "alat anza" — a damaged-type
  misprint — for "alabanza"), all added to `errors in 1920.txt`; one
  suspected error (v.24 missing "¡" before "ay") checked out as NOT an
  error — 1886 also lacks it there. Also closed a `permitted words.txt`
  mirroring gap carried over from the 2026-07-17 session: "Poi",
  "dsesaría", and "aninciado" (Helamán 12:22, 12:25, 13:7) were
  confirmed errors but never mirrored into `permitted words.txt`
  because pptext wasn't flagging them at the time (the known
  brand-new-misprint quirk); the fresh regeneration now flags all
  three, so they were added, along with legitimate-but-rare
  conjugations "predicóles" and "maldecirá" flagged in the same pass.
  Footnote-number check, dash check, curly-quote scan, and Jeebies all
  came back clean for the new range.
- **2026-07-18b**: Sessions A–E run for page 473 (Helamán 13:33-39,
  chapter boundary mid-page into Helamán 14:1-3). Session A: mandatory
  1879/same-page checks for the "n, Véase l." cross-reference target
  (one of the mandatory i/l/1 letters even as a target, not just a
  page's own lettering) — confirmed via both a same-page glyph
  comparison (continuous stroke, no dot) and independent 1879 (BOM
  1879 Pratt page 468, file page 476), which prints "n, see l."
  exactly, resolving to the already-established footnote 3347. Chapter
  13 closes and 14 opens mid-page (rule 13: letters restart at "a",
  sequential numbering continues, 3349-3354); no blank line needed in
  Block 1 since it's the same book (rule 20). Session E: fresh pptext
  regeneration found and confirmed 2 new genuine 1920 errors against
  1886 (Helamán 13:38 "aqué!" for "aquél" — apparent damaged type,
  the "l"+accent replaced by a stray "!" — and 13:39 "esuchad" for
  "escuchad"), both added to `errors in 1920.txt` and mirrored into
  `permitted words.txt` since pptext actually flagged both this run.
  Footnote-number check, dash check, curly-quote scan, hyphenation,
  and Jeebies all came back clean for the new range.
- **2026-07-18c**: Sessions A–E run for page 474 (Helamán 14:3-15).
  Session A: mandatory 1879 check for superscript "i" (v.12, before
  "Padre") confirmed via same-page glyph (short stroke + separated
  dot) and independent 1879 (BOM 1879 Pratt page 469, file page 477),
  which prints "the Father of heaven and of earth" at the identical
  position — content-fit strong (target citations all describe Christ
  as Father of heaven/earth). Session E: fresh pptext regeneration
  caught a genuine 1920 error that Session A's investigative pass had
  missed and transcribed without flagging — Helamán 14:5 "aparacerá"
  (should be "aparecerá"). This one is also present in 1886 (a shared
  error, same pattern as "seperado"/"extragos"), so the 1886
  comparison alone would NOT have settled it; independent research
  did: RAE has no entry for "aparacer" (only "aparecer"), the
  reference corpora have zero hits for "aparacer" vs. 9 for
  "aparecer" in Reina-Valera, and the modern Spanish LDS edition uses
  "aparecerá" — confirmed genuine error, added to `errors in
  1920.txt` with a note on the shared-error pattern, and added to
  `permitted words.txt` (actually flagged this run). Also added
  "esesto" (v.6, a genuine missing-interword-space defect like
  page 474's own "esesto" — unlike the comma-adjacent cases on pages
  471-472, this one has no delimiter between the two merged words, so
  it actually gets flagged and needed a `permitted words.txt` entry
  too). Footnote-number check, dash check, curly-quote scan,
  hyphenation, and Jeebies all came back clean.
- **2026-07-18d, user correction**: user reviewed the 1920 page images
  themselves for three previously-logged "errors" and determined they
  are scan/print artifacts of this particular copy (uneven ink
  coverage / possible dust), not genuine 1920 typesetting errors:
  Helamán 13:28 "cs" (→ "os") and "alat anza" (→ "alabanza"), and
  Helamán 13:38 "aqué!" (→ "aquél", accented — 1920 does use the
  accent on "aquél" elsewhere, confirm that convention if it recurs).
  All three `errors in 1920.txt` entries were REMOVED (not just
  edited) and the body text was corrected in `pages/page_472.txt`,
  `pages/page_473.txt`, and `librodm.txt` to read the intended words;
  each page's Corrections log now explains the scan-artifact call
  instead of calling it a misprint. The corresponding `permitted
  words.txt` entries (cs, alat, anza, aqué) were also removed since
  those garbled forms no longer appear anywhere in the text. **Lesson
  for future Session E/general review**: a word that looks broken in
  the 1920 scan is not automatically a genuine 1920 print error —
  when the "damage" looks physical (uneven ink, a stray gap, a
  broken-looking stroke) rather than a clean substitution of one
  full, valid word-shape for another, it's worth a second look before
  logging it as an error, and the editor may override on inspection
  even after a 1886-comparison-backed entry already exists.
- **2026-07-18e**: Session A completed for page 475 (Helamán
  14:15(continues)–23, footnotes 3363-3376, letters j-w). Footnote
  letter/target resolution had already been fully worked out in a
  prior session (heavily swash 1879 cross-checks) and was used as-is.
  One suspected-error cluster in v.21 ("masa com?pleta. se
  despedazal?án") was resolved by the user on inspection as an
  ink-coverage/print-uniformity artifact of this scan copy — same
  pattern as the 2026-07-18d cases on pages 472-473 — not a genuine
  1920 error: corrected in the transcription to read "una masa
  completa, se despedazarán;", no `errors in 1920.txt` entry, Corrections
  log in `pages/page_475.txt` explains the scan-artifact call. Two
  hyphenated line-break rejoins applied ("condenación" v.19,
  "conmoverá" v.21); "primera muerte--aquella" (v.16) and "señal,--la"
  (v.20) are intentional em-dashes, left as printed. `check_lines.py`
  clean (0 over 72, 0 trailing hyphens).
  - **IN PROGRESS — page 475 needs Sessions B–E next**, then run the
    full A–E cycle for page 476 (file page 498), first footnote
    following wherever 475 ends (3377).
- **2026-07-19**: User audit of `pages/page_475.txt` found that its body
  text line breaks did not match the 1920 image at all — every line had
  been reflowed to a roughly even ~72-character width instead of copied
  from the actual print, even though `check_lines.py` came back clean
  (that script only checks length/trailing hyphens, not whether a break
  is in the right place). Root cause: rule 9 (the character cap) is
  self-checkable while generating flowing text, so it's easy to satisfy
  by construction; rules 5/6 (read every line ending from the image)
  require actively cross-referencing the image line-by-line, which
  silently drops out unless transcription is done as a literal
  line-by-line copy from the start rather than composed as prose and
  wrapped afterward. Spot-checks of pages 470 and 474 against their
  images found no such problem, so this looks like an isolated lapse,
  not a document-wide pattern — but it means a clean `check_lines.py`
  report alone is not proof a page's line breaks are image-derived.
  Fixed: `pages/page_475.txt` was fully re-transcribed line-by-line from
  `pages_1920/page_0497.png` (top/mid/bot crops); the two genuine
  hyphenated line-break splits (v.19 "con-/denación", v.21
  "con-/moverá") were re-applied per rules 7/8 against the correct line
  boundaries; content, footnote numbers (3363-3376), and the earlier
  scan-artifact call on v.21 ("masa completa, se despedazarán") were all
  unaffected and carried over unchanged. Also added `check_line_wrap.py`
  (see Script Reference) as a partial, advisory mechanical backstop, and
  updated `libro_de_mormon_rules.md` (rule 6) and the `transcribe-page`
  skill (new step 4/5) to require an explicit line-by-line raw transcript,
  counted against the image before any rule 7/8 adjustment, rather than
  relying on rule 9 compliance as an implicit proxy for rules 5/6.
  Session B (verify footnotes) for page 475 has not been done yet.
- **2026-07-19b**: A from-scratch re-transcription experiment on page 465
  (independent Session A redo, ignoring prior versions, to fidelity-test
  the rule 6 line-by-line requirement) surfaced a real spacing gap in the
  rules: it correctly normalized one justification-widened gap (v.20)
  citing page 464's precedent, but left three other identical-pattern
  double-spaces (v.11, v.16, v.17, v.21) un-normalized — confirmed via
  zoom to be genuine wider print gaps, not a typing slip. Rule 6 was
  extended with an unconditional single-space-normalization clause (no
  precedent-citation needed, no `errors in 1920.txt` entry) so this
  can't silently depend on the transcriber remembering to cite an
  earlier page. Separately, the user's own review of the 465/471/473/
  474/475 line-break work concluded only page 475 had actually failed;
  465 was restored to its git-committed base version (`page_465_orig.txt`)
  rather than kept as the fresh rewrite. That restore surfaced one
  genuine, previously-uncaught 1920 misprint the fresh rewrite had found
  but the old version missed: Helamán 11:17 "tierre" for "tierra"
  (confirmed via zoom — same line prints "tierra" correctly a few words
  later — and 1886 page 462/file 480 confirms "tierra", so this is
  1920-only). Fixed in `pages/page_465.txt`, `librodm.txt`, `errors in
  1920.txt`, and `permitted words.txt`; `page_465_orig.txt` and
  `page_465_shortcut.txt` deleted as redundant. Page 475 then went
  through Sessions B–E: Session B's mandatory i/l/1 checks (marker "l"
  and target "i" in 14r) confirmed via 1879 (BOM Pratt file pages
  477-478); one footnote-citation discrepancy found (14v/3375 "I Nefi
  9:11" vs. 1879's "I. Nep. 19:11" — 1879's chapter fits the verse
  content, 1920's doesn't, so likely a dropped "1"; preserved as printed
  per rule 32, logged in `errors in 1920.txt`). Session C/D integrated
  cleanly, except `generate_block2.py` failed to resolve one multi-letter
  cross-reference ("Véase b, y, c, II Nefi 2.", footnote 3365) — its
  comma-split parser assumes the letters portion has no comma before the
  book name, which breaks on this "letter, y, letter," print style (a
  pre-existing bug: three earlier instances of the same style resolved
  correctly in `librodm.txt` only because they'd been fixed by hand
  previously, not because the script handles it — worth fixing in
  `generate_block2.py` next time it's touched). Resolved by hand
  ("Véase 261, y, 262."). Session E: fresh pptext regeneration
  (`report_wsl_20260719.html`) came back fully clean for the new range
  — no spellcheck suspects, no footnote gaps/duplicates, dash/hyphenation/
  paragraph-level checks all clean.
- **Next page**: 476 (file page 498), full A–E cycle, first footnote
  3377.
- **Completed pages**: 437–475, Sessions A–E all done through page 475.

## Script Reference
- `process_page.py <png> <label> [first_fn]` — crops page into top/mid/bot/fn/fn_zoom
- `check_lines.py <file>` — flags lines ≥ 73 chars
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
