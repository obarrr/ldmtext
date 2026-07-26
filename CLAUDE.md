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
- **2026-07-19c**: Sessions B–E run for page 476 (Helamán 14:24-31,
  Helamán 15:1-2, footnotes 3377-3385, letters x-z/2a-2e then chapter
  15 restarts at a). Session B: independent re-verification of all
  Block 1 entries and body markers against the 1920 image, plus an
  extra-discretion 1879 cross-check (file pages 478-479, chapter_map
  Helamán 14/15) for the x/z pair, which looked visually similar
  (both flat-topped, no crossing strokes or descender) at this print
  size — 1879 confirmed the full x/y/z/2a-2e/15a sequence letter-for-
  letter. Session C/D integrated cleanly, but generating Block 2
  surfaced a genuine Session A transcription error found nowhere else
  in the pipeline: footnote 3381 (14-2b) had been transcribed as
  "Véase n." when it should read "Véase s." — the original content-fit
  reasoning (matching v.26's near-verbatim repeat of v.21's text) and
  the 1879 cross-check ("2b, see s") both actually pointed to letter s
  the whole time, but got mislabeled as "n" in the write-up; corrected
  in `pages/page_476.txt`, `librodm_foot.txt`, and `librodm.txt`'s
  Block 2 entry (3381: Véase 3372, not 3367). Session E: fresh pptext
  regeneration (`report_wsl_20260719b.html`) came back fully clean for
  the new range — no spellcheck suspects, no footnote gaps/duplicates,
  no new dash/hyphenation findings, and an independent curly-quote
  scan and full-stop-then-lowercase scan of the new lines both came
  back clean too.
- **2026-07-19d**: Sessions B–E run for page 477 (Helamán 15:3-11,
  footnotes 3386-3390, letters b-f). Session B: independently
  re-verified all five body markers and Block 1 entries against
  pages_1920/page_0499.png (top/mid/bot/fn_zoom); none of this page's
  own letters or its cross-reference targets (n, o) are i/l/1, so no
  new mandatory 1879 check applied — the discretionary 1879 checks
  Session A already ran for the 15b/15d blob glyph and the 15c "e" vs
  "o" ambiguity were reviewed and confirmed sufficient. No errors
  found. Session C/D integrated cleanly via the scripts. Session E:
  fresh pptext regeneration (`report_wsl_20260719c.html`) came back
  fully clean for the new range — spellcheck, edit distance, dash/
  hyphenation, footnote-number consistency (merged-bucket diff: zero
  duplicates, zero out-of-range, only the pre-existing 812/Jacob 2:15
  gap), scanno, curly quotes, special situations, book level, and
  Jeebies all clean; a mandatory sweep of the page's own Corrections
  log found only transcription-mechanics and already-1879-settled
  footnote-letter notes, nothing needing a fresh 1886/RAE check. No
  `errors in 1920.txt` or `permitted words.txt` entries needed.
- **2026-07-19e**: Sessions B–E run for page 478 (Helamán 15:11-17,
  Helamán 16:1-2, footnotes 3391-3399, letters g-m then chapter 16
  restarts at a-b). Session B: independently re-verified all 9 Block 1
  entries and body markers against pages_1920/page_0500.png; mandatory
  1879 check re-run independently for this page's own letters i and l
  (BOM 1879 Pratt file page 480 — chapter_map's listed 479 only carries
  Helamán 14's tail, matching the "one page later" pattern already seen
  for this chapter) confirmed both letter-for-letter, plus bonus
  reconfirmation of g/h/j/k including Session A's swash-glyph "2e"
  resolution. Session C integrated cleanly. Session D: `generate_block2.py`
  left 3 entries unresolved (3391, 3393, 3396) — a new variant of the
  known cross-reference-parsing limitation (a "Véase X; también véase Y"
  clause with two separate targets gets treated as one unparseable
  letters-list) — resolved by hand via book-aware lookup (Enos 1c=975,
  II Nefi 27c=682), matching an exact existing precedent already in
  librodm.txt. Session E: fresh pptext regeneration
  (`report_wsl_20260719d.html`) came back fully clean for the new range —
  no spellcheck suspects, no hyphenation findings (page has no hyphens),
  footnote-number consistency confirmed (max 3399, zero duplicates, only
  the pre-existing 812 gap), curly-quote scan clean, book/paragraph-level
  and Jeebies all clean. Corrections-log sweep found only transcription-
  mechanics notes, nothing needing `errors in 1920.txt` or `permitted
  words.txt`. `generate_block2.py`'s two known cross-reference-parsing
  gaps (comma-split from page 475, two-target "también" clause from this
  page) are both still worth fixing next time the script is touched.
- **2026-07-20**: Sessions B–E run for page 479 (Helamán 16:1-13,
  footnotes 3400-3401, letters c-d). Session B: independently
  re-verified both Block 1 entries and body markers against
  pages_1920/page_0501.png; neither this page's own letters (c, d) nor
  either cross-reference target (a verse number and a chapter:verse
  citation, no letters) is i/l/1, so no mandatory 1879 check applied.
  Session C/D integrated cleanly. Session E: fresh pptext regeneration
  (`report_wsl_20260720.html`) flagged 5 spellcheck suspects, all from
  this page; checked each against 1886 (file pages 493-494) plus
  independent RAE/corpus/modern-edition research. Confirmed 4 new
  genuine 1920 errors, all added to `errors in 1920.txt`: Helamán 16:5
  "aunuciadas" (→ anunciadas) and "buatizase" (→ bautizase), both
  1920-only per 1886; Helamán 16:10 "circumspectamente" and 16:5
  "arrepentiéndose" — both also present in 1886 (shared-error pattern
  like "aparacerá"/"seperado") but confirmed wrong via RAE (no entry
  for the "circumspect-" spelling, only "circunspect-") and the modern
  LDS Spanish edition (uses "circunspección" and the irregular gerund
  "arrepintiéndose" at these verses). "apoderáos" confirmed legitimate
  (established accented-imperative convention) and added to `permitted
  words.txt` along with `circumspectamente` and `arrepentiéndose`.
  Separately, a user review of v.7 found the Session A/B "quese"
  reading was wrong: the print has a real, reduced-width space between
  "que" and "se," not a true zero-space merge like page 474's "esesto"
  — corrected to "que se" in `pages/page_479.txt` and `librodm.txt`
  (no `errors in 1920.txt` entry; not a misprint). Added a new note to
  rule 6 in `libro_de_mormon_rules.md` distinguishing a genuine merged-
  word defect from a narrow-but-real gap, so future sessions verify gap
  width at zoom before treating a tight word-pair as a true merge.
  Footnote-anchor check, curly-quote scan, dash check, and Jeebies all
  came back clean.
- **2026-07-20b**: User's own reading of an already-completed page
  (`page_467.txt`, Helamán 11) caught a previously-uncaught genuine 1920
  error: v.36 "en año" (missing "el"), confirmed against 1886 (file 482,
  book page 464) reading "en el año." Added to `errors in 1920.txt` and
  `page_467.txt`'s Corrections log.
- **2026-07-20c**: Discovered pages 480 and 481 were both already fully
  transcribed through Session E on disk (Sessions A–E complete, per
  their own Corrections logs and `errors in 1920.txt`/`permitted
  words.txt` entries — e.g. Helamán 16:20 "podermos", 16:21
  "sugetarán", 16:23 "piodigios"/"ápesar" for page 480), but this
  progress log was never updated after page 480 finished, so it still
  read "Next page: 480." Both pages remain uncommitted (`git status`
  shows `pages/page_480.txt` and `pages/page_481.txt` untracked, plus
  modified `errors in 1920.txt`/`librodm.txt`/`librodm_foot.txt`/
  `permitted words.txt`). Sessions D–E then run for page 481
  (Helamán 16:24-25 chapter close; III Nefi opens — book/chapter
  boundary, footnotes 3405-3411): Session D's `generate_block2.py`
  resolved all 7 Block 2 entries cleanly, including inserting the
  "III NEFI" Notas section header correctly on the first real exercise
  of the book-boundary logic flagged as untested back on 2026-07-19e/
  page 476 (bottom-to-top selection correctly picked "III NEFI," not
  "LIBRO DE NEFI," matching the disambiguation the user had explicitly
  called for in a prior page-481 Session C note — no `librodm.txt`
  hand-fix needed this time). Session E: fresh pptext regeneration
  (`report_wsl_20260720b.html`) found 2 genuine 1920 errors, both
  confirmed against 1886 (file page 496) and neither currently
  pptext-flagged (the known brand-new-single-occurrence quirk, so
  no `permitted words.txt` entries): III Nefi 1:5 "aunuciadas" for
  "anunciadas" (third confirmed instance of this exact missing-letter
  pattern, after Helamán 13:21 and 16:5), and III Nefi 1:3 "análes"
  (accented) — 1886 actually accents "análes" all three times on this
  page while 1920 only does so once, and RAE/corpus/modern-edition
  research all confirm unaccented "anales" is the only correct form
  (same shared-error pattern as "seperado"). Footnote-anchor check
  (3405-3411, only the pre-existing 812 gap), curly-quote scan (zero
  curly quotes in either master file), dash check, and `check_lines.py`
  all clean.
- **2026-07-20d**: Sessions A–E run for page 482 (III Nefi 1:6(continues)-16,
  footnotes 3412-3423, letters h-s). Session A: mandatory 1879 check for
  this page's own "i" and "l" letters (BOM 1879 Pratt file pages 484-485,
  chapter_map 3 Nephi ch.1) confirmed all twelve letters h-s and their
  reference text exactly, including a same-page glyph comparison first
  (v.9's "i": dot + short hook, vs. v.13's "l": continuous unbroken
  stroke, no dot). Three suspected misprints caught and preserved as
  printed per rule 32: v.11 "c amó" (gap where "clamó"'s "l" apparently
  failed to ink) and "Dos" (missing "i" from "Dios"), and v.13 "por.
  boca" (a spurious period with no grammatical basis). Session D:
  `generate_block2.py` resolved all three Mosíah cross-references (m,
  n, o) cleanly; spot-checked the book-aware resolution against
  `librodm_foot.txt`'s "LIBRO DE MOSIAH" section to confirm none
  collided with a different book's same chapter+letter. Session E:
  fresh pptext regeneration (`report_wsl_20260721.html`) flagged 2
  spellcheck suspects — "apesadumbrarse" (v.7, confirmed legitimate,
  matches 1886 exactly, added to `permitted words.txt` only) and
  "frustado" (v.16, confirmed genuine error despite matching 1886 —
  same shared-error pattern as "seperado" — RAE has no entry for it,
  zero corpus hits, and the modern LDS Spanish edition uses "frustrado"
  at this exact verse; added to both `errors in 1920.txt` and
  `permitted words.txt`). The other two Session A suspects ("c amó" →
  "clamó", "Dos" → "Dios") were confirmed against 1886 (file page 497)
  and added to `errors in 1920.txt`; neither is currently pptext-
  flagged (known brand-new-single-occurrence quirk), so no `permitted
  words.txt` entries for those two. Footnote-anchor check (3412-3423,
  only the pre-existing 812 gap), curly-quote scan, and dash/hyphen-
  compound scan all clean.
- **2026-07-21b**: Sessions A–E run for page 483 (III Nefi 1:16(continues)-
  26, footnotes 3424-3430, letters t-z). Session A: none of this page's
  letters (t-z) fall in the mandatory i/l/1 set; assignment made by
  strict sequential position plus independent glyph-shape zoom
  comparison against the footnote block's own reference letters and
  strong content-fit for every entry (Norte/Sur América at v.17's
  "Norte"/"Sud"; Helamán 14:3-4's no-darkness sign at v.19's "no hubo
  obscuridad"; Helamán 14:5's star prophecy at v.21's "nueva estrella";
  II Nefi 9 (baptism scriptures) at v.23's "bautismo"; II Nefi 25 (law
  of Moses) at v.25's "ley"). One rule-8 marker-overflow cascade (moving
  "Norte" then "admiración," each to the next line). Session D's
  `generate_block2.py` confirmed both cross-references resolved to the
  correct II Nefi book section (378: baptism scriptures; 653: II Nefi
  25's law-of-Moses passages), matching their v.23/v.25 context exactly.
  Session E: fresh pptext regeneration (`report_wsl_20260721b.html`)
  found zero new spellcheck suspects (only pre-existing hit in the whole
  document remains "buatizase," Helamán 16:5). Two of this page's three
  suspected-misprint Corrections-log items confirmed as genuine 1920-only
  errors against 1886 (file page 498) and added to `errors in 1920.txt`:
  III Nefi 1:18 "lo profetas" (missing "s") and 1:19 "se curso natural"
  ("se" for "su") — neither needed a `permitted words.txt` entry since
  both are real dictionary words pptext wouldn't flag regardless. The
  third (v.22's free-floating dot between "que" and "desde") was left
  for the editor's own visual judgment rather than added unilaterally;
  the editor reviewed the 1920 image directly and confirmed the mark is
  a scan artifact (visibly smaller and fainter than this edition's
  genuine typeset periods), not real type — corrected in the
  transcription to read "que desde entonces" in both `page_483.txt` and
  `librodm.txt`, no `errors in 1920.txt` entry. Footnote-anchor check
  (3424-3430, only the pre-existing 812 gap), curly-quote scan, and
  dash/hyphen-compound scan all clean.
- **2026-07-21c**: Sessions A–E run for page 484 (III Nefi 1:26(continues)-30,
  chapter boundary into III Nefi 2:1-4, footnotes 3431-3432, letters "2a"
  — chapter 1's lettering continuing past z — then chapter 2 restarts at
  "a"). Session A: neither footnote letter is i/l/1, so no mandatory 1879
  check; both resolved by glyph zoom plus strong content fit ("2a" sits at
  "Gadianton" in the chapter that introduces the robber band by name; "a"
  sits at "esas señales" in ch.2 v.1, matching the Helamán 14 signs cited).
  Last word on the page, "nona-", is a genuine page-boundary hyphen split
  (start of "nonagésimo-séptimo", confirmed against 1886) left unresolved
  per rule 10 pending page 485. Session D's `generate_block2.py` needed no
  cross-reference resolution — both entries were direct scripture
  citations, not "Véase" pointers. Session E: fresh pptext regeneration
  (`report_wsl_20260721c.html`) flagged one spellcheck suspect,
  "admiráronse" (ch.2 v.1) — confirmed legitimate archaic enclitic-pronoun
  form, matches 1886 exactly and independently attested in Don Quijote (4
  hits for "Admiráronse" in the local reference corpus); added to
  `permitted words.txt` only. This page's own suspected-misprint
  Corrections-log item was confirmed as a genuine 1920-only error against
  1886 (file page 499, chapter_map 3 Nephi ch.1/2 boundary): v.29
  "Lamanitas; porque; he aquí" — 1886 has no punctuation at all between
  "porque" and "hé aquí," (only a comma after "aquí"), so 1920's semicolon
  after "porque" is spurious; added to `errors in 1920.txt` (no
  `permitted words.txt` entry needed — not a spellcheck matter). 1886's
  accented "hé" vs. 1920's unaccented "he" at the same spot is an ordinary
  minor accent variation, not logged separately. Footnote-anchor check
  (union of both pptext footnote-check buckets covers 1-3432 with zero
  duplicates/out-of-range, only the pre-existing 812 gap) and curly-quote
  scan (zero curly quotes in either master file) both clean.
- **2026-07-21d**: Sessions A–E run for page 485 (III Nefi 2:4(continues)-16,
  footnotes 3433-3441, letters b-j; chapter 2 closes at v.16). Session A
  also resolved page 484's pending page-boundary word: "nona-" +
  "gésimo-séptimo," rejoin to "nonagésimo-séptimo," and fit on page 484's
  last line (69 chars), so `pages/page_484.txt` and its already-integrated
  copy in `librodm.txt` were both corrected. Session A/B: mandatory 1879
  check for letter i (v.15) confirmed via same-page i/j glyph comparison
  plus independent 1879 (BOM Pratt file page 480, one page past the
  chapter_map-listed 479 — same "one page later" drift as prior pages in
  this chapter); all nine letters b-j cross-checked against 1879
  letter-for-letter as a bonus, and Session B re-ran the check
  independently with a fresh crop rather than reusing Session A's. Session
  C/D integrated cleanly (`insert_body_text.py 485`, `generate_block2.py
  485`), all 9 Block 2 cross-references resolved with no unresolved
  targets; four spot-checked against `librodm_foot.txt` and confirmed
  correct book-aware matches. Session E: fresh pptext regeneration
  initially flagged "YNefi" (v.9) as a suspected zero-space merge — this
  was **wrong**: the user, looking at the same PDF page, caught that there
  is a real, healthy space there. A pixel-level column-projection
  measurement (numpy) confirmed the user's read: the Y-N gap measures 6px,
  double the 2-3px intra-word kerning gaps within "Nefi" itself and
  comparable to another ordinary word-gap on the same line (8px) —
  corrected to "Y Nefi" in `page_485.txt` and `librodm.txt`, no
  `errors in 1920.txt`/`permitted words.txt` entry. See the updated
  `feedback_narrow_space_vs_merge` memory: eyeballing a zoomed crop has
  now produced the wrong merge-vs-space verdict twice, so this judgment
  call now requires a pixel-width measurement, not just a visual read.
  Separately, this run also re-flagged the pre-existing "buatizase"
  (Helamán 16:5, already in `errors in 1920.txt` since 2026-07-20) —
  mirrored into `permitted words.txt` now to close that gap. Independent
  full-document footnote-anchor check (regex scan): max 3441, zero
  duplicates, only the pre-existing 812 gap. Curly-quote scan and
  letter-hyphen-letter compound scan both clean; Jeebies clean.
- **2026-07-21e**: Sessions B–E run for page 486 (III Nefi 2:17-19 chapter
  close, Helamán 2:11-13 cross-ref; chapter 3 opens 3:1-5; footnotes
  3442-3444, letters k then a-b). Session B: independently re-verified
  all three Block 1 entries and body markers against
  pages_1920/page_0508.png; none of k/a/b nor their cross-reference
  targets is i/l/1, so no mandatory 1879 check applied. Session C/D
  integrated cleanly (`insert_body_text.py 486`, `generate_block2.py
  486`); footnote 3444 ("Véase m, Mosíah 29") correctly resolved to the
  same target (1608) as page 485's "h", confirming the recurring
  liberty-themed cross-reference. Session E: fresh pptext regeneration
  (`report_wsl_20260721f.html`, spellcheck suspects section fully
  empty) found no new spellcheck flags, but confirmed both of Session
  A's preserved-as-printed suspected misprints as genuine 1920-only
  errors via 1886 (file page 501, book page 483): III Nefi 2:18
  "volveron" (→ volviéron) and 2:19 "etando" (→ estando), both added to
  `errors in 1920.txt`; neither is pptext-flagged, so no `permitted
  words.txt` entries. Note: 1886 pages in this stretch (file ~499-501+)
  misprint their own running header as "II NEFI" instead of "III NEFI"
  for several consecutive pages — a printing quirk of the 1886 edition
  itself, not logged anywhere since it's not a 1920 error, but worth
  knowing if a future session navigates this same 1886 page range and
  the header looks wrong. Footnote-anchor check (full-document, max
  3444): zero duplicates, zero out-of-range, only the pre-existing 812
  gap. Curly-quote scan (zero curly quotes in either master file) and
  hyphen-compound scan both clean.
- **2026-07-21f**: Sessions A–E run for page 487 (III Nefi 3:6-14,
  footnotes 3445-3448, letters c-f). Session A required two corrections
  from the editor after initial transcription: v.11 "vino á" was
  misread as a zero-gap merge ("vinoá") despite a zoomed crop and a
  pixel-projection scan both appearing to confirm it — this is now a
  third recurrence of the narrow-space-vs-merge failure mode (see
  `feedback_narrow_space_vs_merge`), and the editor's direct read of
  the actual page was what settled it, not further zooming/measuring.
  Separately, footnote f ("Véase [letter], Alma 48") was misread as
  target letter "e" from an isolated 12x zoom; the editor identified it
  as "c" directly from the page, matching 1879's parallel entry ("f,
  see c, Alma 48.") exactly and confirmed by content-fit (Alma 48c
  resolves to Alma 49-53, Moroni's fortified-cities chapters — a much
  stronger match for "fortificaciones" than 48e's title-of-liberty
  content); Block 2 generation independently confirmed the fix by
  resolving 3448 to 2823 (48c), not 2825 (48e). Both corrections are
  now also reflected in `feedback_ambiguous_superscript_letters`
  (lesson: run the content-fit check before reaching for rule 26 as an
  explanation when 1879 and 1920 disagree on a target letter). Session
  A's mandatory 1879 check for footnote letters c/d (both cross-
  reference target letter "i" in II Nefi 10, even though c/d themselves
  aren't i/l/1) was confirmed via BOM 1879 Pratt file page 489
  (chapter_map III Nephi ch.3, "one page later" content drift);
  Session B re-ran this independently from a fresh crop and reconfirmed
  it. Session C/D integrated cleanly (`insert_body_text.py 487`,
  `generate_block2.py 487`), all 4 Block 2 entries resolved with no
  unresolved targets. Session E: fresh pptext regeneration
  (`report_wsl_20260721e.html`) flagged one spellcheck suspect,
  "entregáos" (v.7) — confirmed legitimate archaic accented imperative,
  matches 1886 (file page 484, allowing for 1886's extra "nos" enclitic
  that 1920 drops) even though modern RAE convention no longer accents
  this ending; added to `permitted words.txt` only. Footnote-anchor
  check (max 3448, zero duplicates/out-of-range, only the pre-existing
  812 gap) and curly-quote scan both clean; no other findings in this
  page's line range across the rest of the report.
- **2026-07-21g**: Sessions A–E run for page 488 (III Nefi 3:14(continues)-
  24, footnotes 3449-3457, letters g-o). This page had an unusually high
  concentration of genuine 1920 print defects — 9 confirmed misprints in
  one page, all verified against 1886 (file page 503, book 485, which
  maps this page's entire content onto a single 1886 page): III Nefi
  3:15 "dicíendoles" (accent on wrong vowel) and "arrepintie.eis"
  (missing "r", damaged type — no "r" printed at all, just an isolated
  mark); 3:16 "giandes" (damaged "r" printed as a bare dotless stroke),
  "Lachoneus. que" (period for comma), and "requiería" (extra "i" —
  imperfect indicative of "requerir" doesn't diphthongize, and this one
  was Session E's own catch via pptext, not spotted during Session A/B);
  3:17 "dirigieran. cuando" (period for comma); 3:19 "de de perversidad"
  (genuine dittography); 3:21 "Gidgiddoniles respondió les respondió"
  (merged word plus duplicated verb — two stacked defects in one spot)
  and "el Señor. nos" (spurious period, no punctuation at all in 1886).
  All 9 added to `errors in 1920.txt`. Session A also resolved two
  narrow-space-vs-merge judgment calls via pixel column-projection
  measurement rather than eyeballing (`país de` and `el Señor`, both
  7px — same class as page 485's 6px "Y Nefi" precedent), and one
  scan-artifact call (a floating dot between "para" and "defenderse",
  resolved the same way as the page 483 v.22 precedent, confirmed
  clean against 1886). Session A/B's mandatory 1879 check (letters i
  and l, this chapter's own lettering, plus k's cross-reference target
  letter l) confirmed via BOM 1879 Pratt file pages 490-491 (chapter_map
  3 Nephi ch.3, "one page later" drift); Session B re-ran it
  independently from fresh crops. Session D's `generate_block2.py`
  resolved all 9 Block 2 entries cleanly, including two targeting
  Alma 22's two-letter codes ("Véase 2k"/"Véase 2l" — confirmed via
  existing precedent in `librodm_foot.txt` that a cross-reference
  target's own 2-letter code is written without a hyphen, unlike this
  chapter's own entries). Session E: fresh pptext regeneration
  (`report_wsl_20260721g.html`) flagged three spellcheck suspects
  ("arrepintie", "eis", "requiería" — all added to `permitted
  words.txt` since this run actually flagged them); "giandes",
  "dicíendoles", and "Gidgiddoniles" were not flagged (known brand-new-
  single-occurrence quirk), so no `permitted words.txt` entries for
  those three. Footnote check needed the two-bucket union technique
  (3439/3441/3446 all landed in the start-of-line "footnotes" bucket
  only, since each opens a wrapped line) to confirm a clean 1..3457
  range with only the pre-existing 812 gap. Curly-quote scan and a
  letter-hyphen-letter compound scan of the new lines both clean.
- **2026-07-22**: Sessions A–E run for page 489 (III Nefi 3:24(continues)-26
  chapter close, III Nefi 4:1-4, footnotes 3458-3470, letters p-t then a-h).
  Session A: rejoined two hyphenated line-break splits ("forti-/ficaron" →
  "fortificaron", "pro-/visiones" → "provisiones"), each triggering rule 8
  rebalancing cascades since the rejoined lines exceeded 72 chars. Confirmed
  three narrow-but-real spaces via pixel column-projection scan rather than
  eyeballing (10px, 10px, 5px gaps — all clearly nonzero, distinct from
  0-2px intra-letter kerning). Caught and corrected a punctuation misread
  mid-transcription: an initial low-zoom crop made "pecados;" look like a
  colon (the crop cut off the comma tail below it); a taller re-zoom
  confirmed it's a semicolon like the rest of the page. Flagged one
  suspected misprint preserved as printed: "nunguna" for "ninguna" (v.2).
  None of this page's own letters (p-t, a-h) or cross-reference targets
  (c, h, p, m, d) are i/l/1, so no mandatory 1879 check applied. Sessions
  B/C/D integrated cleanly via the scripts with no unresolved Block 2
  cross-references. Session E: fresh pptext regeneration confirmed
  "nunguna" against 1886 (file page 504, book 486) — genuine 1920-only
  error, added to `errors in 1920.txt`; not pptext-flagged this run (known
  brand-new-single-occurrence quirk), so no `permitted words.txt` entry.
  Footnote check clean (max 3470, only the pre-existing 812 gap, zero
  duplicates). Curly-quote scan and dash check both clean.
- **2026-07-22b, user correction — chapter/book subtitles must never be
  omitted**: the user caught that page 469's Corrections log had
  incorrectly justified DROPPING Helamán 13's own italic subtitle
  ("Profecía de Samuel, el Lamanita, á los Nefitas.") from the body text,
  citing rule 19 as precedent — but rule 19 has never governed body text
  at all; it only picks which single line becomes the short `LIBRO DE
  X`-style header in `librodm_foot.txt`'s Block 1 listing, a completely
  different file. The omission also rested on a false premise ("no
  chapter-heading subtitle has been transcribed on any completed page so
  far") that was already contradicted by Helamán 7's subtitle (page 453),
  transcribed correctly. Fixed: `libro_de_mormon_rules.md` Section 1 got a
  new rule requiring every subtitle — whole-book, single-book,
  multi-chapter, single-chapter, or even partial-chapter — to always be
  transcribed exactly as printed, in 1920's own order (which can differ
  from 1879/1886, e.g. 1920 sometimes prints `CAPÍTULO N.` before the
  subtitle where 1879/1886 print it after — a genuine repeatable 1920
  house-style difference, not an error); rule 19 itself got a scope note
  making clear it only applies to the Block 1 header. Restored the
  omitted subtitle in both `pages/page_469.txt` and `librodm.txt`
  ("Profecia de Samuel, el Lamanita, a los Nefitas." — transcribed
  without accents, exactly as 1920 prints it, unlike 1886's accented
  form). Audited every other chapter opening in the pages/ folder
  (437-489: chapters 8-12, 14-16, III Nefi 2-4) directly against the 1920
  images — confirmed no other omissions; those chapters genuinely have no
  subtitle in the print. Per the user's explicit instruction, both the
  order reversal and the missing accents were logged in `errors in
  1920.txt` (new "Helamán 13 (encabezado)" entry, matching the format and
  "pending editorial decision" framing of the pre-existing Helamán 7
  heading entry). Note: the Helamán 7 errors.txt entry says the ordering
  question is still "pendiente de decisión editorial," but `page_453.txt`'s
  own Corrections note already asserts the 1920 order was followed and
  settled — these two records disagree about whether this is still open
  and should be reconciled next time either page is touched. This audit
  did not extend to Helamán 1-6 or earlier books (Mosiah, Alma, etc.),
  which predate the `pages/` folder convention and have no generated
  notes to check, per the user's explicit scope.
- **2026-07-22c**: Sessions A–E run for page 490 (III Nefi 4:4(continues)-14,
  footnotes 3471-3472, letters i-j). Session A: mandatory 1879 check for
  letter i (i is in the i/l/1 set) confirmed via BOM 1879 Pratt file page
  493 (chapter_map 3 Nephi ch.4) — matched letter-for-letter and by body
  position ("ithreatenings" at v.12, "jGidgiddoni" at v.13), also
  independently confirmed by glyph shape (i: short stroke + separated dot
  on the baseline; j: matching stroke with a curved descender below the
  baseline). Two narrow-but-real word-pairs ("caer sobre," "Por cuyo,"
  v.6) were measured via pixel column-projection (5px and 6px, versus
  12-17px genuine word-spaces and 1-2px intra-letter gaps) rather than
  eyeballed, per `feedback_narrow_space_vs_merge`, and confirmed as
  narrow spacing, not merges, via 1886 (file page 504). A third tight
  pair, v.12 "que fueron," measured a true 0px gap (no space at all) via
  pixel scan and was initially logged as a genuine merge ("quefueron")
  in both `librodm.txt` and `errors in 1920.txt`/`permitted words.txt` —
  but the editor reviewed the actual page directly and determined there
  is enough space to read as two words; corrected to "que fueron" and
  all three entries (transcription, errors log, permitted-words) were
  reverted. This is the fourth recurrence of the editor's direct-image
  judgment overriding a Claude-side merge/gap-width call (see
  `feedback_narrow_space_vs_merge`), including once now after a properly
  isolated, well-compared pixel scan, not just eyeballing — so a pixel
  scan alone is no longer being treated as sufficient to close this
  question unilaterally; flag to the editor before finalizing. Also
  flagged v.7's unaccented "vino a suceder" (vs. this
  same page's "vino á suceder" at v.8/v.9, and 1886's accented v.7) as a
  suspected misprint, but a full-document check found the same
  unaccented construction already appears 4+ other times throughout
  `librodm.txt`, never previously logged as an error — concluded this is
  an established, recurring 1920 accentuation inconsistency, not a
  page-490-specific defect, so no `errors in 1920.txt` entry. Session D's
  `generate_block2.py` correctly resolved footnote j's "Véase h, III Nefi
  3" to chapter 3's own letter h (3450, Gidgiddoni's appointment as chief
  captain), not chapter 4's own h — confirming the book-aware,
  chapter-scoped cross-reference matching works correctly across a
  same-book chapter boundary. Session E: fresh pptext regeneration
  (`report_wsl_20260722c.html`) found only the "quefueron" spellcheck
  suspect (plus the pre-existing, unrelated "Profecia" from page 469);
  footnote-anchor check (max 3472, zero duplicates/out-of-range, only the
  pre-existing 812 gap), curly-quote scan, dash check, and paragraph-level
  checks all clean for the new range; Jeebies clean.
- **2026-07-22d**: Sessions A–E run for page 491 (III Nefi 4:14(continues)-
  26, footnotes 3473-3474, letters k-l). Session A: letter l is in the
  mandatory i/l/1 set — confirmed via BOM 1879 Pratt file page 494
  (chapter_map 3 Nephi ch.4, "one page later" content drift), which reads
  "furthermost parts of the land ˡnorthward" (v.23) with footnote block
  "l, North America." — letter-for-letter and target-for-target match;
  letter k (not mandatory) was also cross-checked as a discretionary bonus
  via 1879 file page 493 ("because of ᵏtheir much provision... k, ver.
  4."), matching v.18's "á causa de las muchas provisiones" exactly.
  Session B independently re-ran the mandatory l check from a fresh crop
  and reconfirmed it, plus noted 1879 spells the name "Zemnarihah" at the
  same v.23 spot (bonus corroborating evidence for a v.23-only 1920
  spelling defect, see below). Session C/D integrated cleanly, both Block
  2 entries resolved with no unresolved cross-references. Session E: fresh
  pptext regeneration (`report_wsl_20260722d.html`) flagged 2 spellcheck/
  edit-distance suspects, both confirmed as genuine 1920-only errors
  against 1886 (file page 506) and added to `errors in 1920.txt` and
  `permitted words.txt`: III Nefi 4:16 "lleagaron" (→ llegaron, extra "a")
  and III Nefi 4:23 "Zemnaríhan" (→ Zemnaríhah — every other instance on
  this same page, v.17 and v.22, correctly reads "Zemnaríhah"; 1886
  confirms "Zemnaríhah" at v.23 too, so 1920 alone misprints the final
  letter as "n"). Per the current rule 6 default (2026-07-22 editor
  guidance), v.15's tight "de los" (before "Nefitas," near-zero visible
  gap in the 1920 print) was transcribed as two words with no pixel
  analysis, noted in the page's Corrections log, and surfaced in Session
  E's summary rather than treated as a stopping point. Footnote-anchor
  check (max 3474, zero duplicates/out-of-range, only the pre-existing 812
  gap) and curly-quote scan both clean; no hyphens anywhere in this page's
  body text, so no dash-check findings.
- **2026-07-22e**: Sessions A–E run for page 492 (III Nefi 4:26-33 chapter
  close, III Nefi 5:1-3 chapter open, footnote 3475, letter m). Session A:
  only one footnote on this page, letter m (chapter 4's continuing
  lettering); its cross-reference target letter "i" (in "Véase i, II Nefi
  10") is in the mandatory i/l/1 set, confirmed via BOM 1879 Pratt file
  page 494 (chapter_map 3 Nephi ch.4, "one page later" content drift) —
  "m, see i, II. Nep. 10." matches letter-for-letter, and the target
  content (II Nefi 10's own footnote i, a passage specifically about
  secret combinations) is a strong content-fit match for v.29's "de las
  secretas combinaciones." Two stray scan-artifact ink dots (v.1, and at
  the v.1/v.2 boundary) were identified and not transcribed, matching the
  established pattern from pages 483/490. Session B independently
  reconfirmed the single Block 1 entry and the 1879 check from fresh
  crops, including a same-block glyph comparison (i: short stroke +
  dot; l: continuous unbroken stroke) against neighboring "l, North
  America." Session C/D integrated cleanly; Block 2 resolved 3475 to 398
  (II Nefi 10's own letter i), matching the content-fit reasoning
  exactly. Session E: fresh pptext regeneration
  (`report_wsl_20260722e.html`) flagged one spellcheck suspect, "arbol"
  (v.28) — confirmed genuine 1920-only error against 1886 (file page
  507): 1886 accents it "árbol" both times, and 1920's own very next
  line ("cortaron el árbol de raíz") accents it correctly too, so this
  is an isolated same-verse inconsistency, not a period convention; RAE
  confirms "arbol" (no tilde) isn't a recognized word. Added to `errors
  in 1920.txt` and `permitted words.txt`. Three more suspected
  misprints flagged in Session A's Corrections log were checked against
  1886 and confirmed genuine (none flagged by pptext this run — the
  known brand-new-single-occurrence quirk, so no `permitted words.txt`
  entries for these three): v.27 "prisoneros" (1886: "prisioneros"),
  v.28 "nurió" (1886: "murió"), and chapter 5 v.2 "sucedieran toda las
  cosas" (1886: "todas las cosas" — a concordance/grammar slip, not a
  single misspelled word). All four added to `errors in 1920.txt`.
  Verified "Hosana" (v.32, single "n") is NOT a page-specific error —
  already appears unflagged elsewhere in librodm.txt (line 1524),
  confirming it's an established 1920 spelling convention. Footnote-
  anchor check (full-document, max 3475): zero duplicates, zero
  out-of-range, only the pre-existing 812 gap. Curly-quote scan (zero
  curly quotes in either master file) clean; page 492's body text has
  no hyphens at all post-rejoin, so no dash-check findings.
- **2026-07-22f**: Sessions A–E run for page 493 (III Nefi 5:4-14,
  footnotes 3476-3485, letters a-j). Session A: mandatory 1879 check
  for letter i (v.12, "Alma") confirmed via BOM 1879 Pratt file page
  496 (chapter_map lists 495, content lands one page later — same
  "one page later" drift pattern seen throughout this book); all ten
  letters a-j cross-checked letter-for-letter and content-for-content
  against 1879 as a bonus, including h/i/j's content on the following
  1879 page. Session B independently re-ran the mandatory check from
  fresh crops and reconfirmed it, plus a same-page h/i glyph
  comparison. Session C/D integrated cleanly, both cross-references
  (footnote a's "Véase i, II Nefi 10" and footnote f's "Véase f, I
  Nefi 1") resolved correctly and book-aware. Session E: fresh pptext
  regeneration (`report_wsl_20260722f.html`) flagged 6 spellcheck
  suspects, all confirmed as genuine 1920-only errors against 1886
  (file pages 507-508), RAE, the reference corpora, and the modern
  Spanish edition (3 Nefi 5): III Nefi 5:4 "prisoneros" (a second
  instance of the same missing-"i" pattern as III Nefi 4:27), 5:5
  "amenzaas" (transposed letters, → amenazas), and 5:7-8 "vientidós",
  "vientitrés", "vienticuatro", "vienticinco" (×2) — all print
  "vient-" where this document's 8 other "veinti-" instances (and
  1886's spelled-out "veinte y dos" style, and the modern edition)
  agree the contraction should be "veinti-". Also confirmed footnote
  j's "Dicípulos" (missing "s", no 1886 comparison available since
  1886 carries no footnotes, but settled via internal consistency —
  "discípulo" is spelled correctly 9 other times in the document —
  and RAE) and a footnote g citation defect ("5:9,12,1;7:8-10" for
  "5:9,12,13;7:8-10", a dropped "3", confirmed against 1879's parallel
  entry). All 6 pptext-flagged words added to `permitted words.txt`;
  all 6 confirmed errors plus the footnote g citation defect added to
  `errors in 1920.txt` (the footnote entries as a new "Footnote III
  Nefi 5g/5j" style, following existing precedent for footnote-text
  errors). Footnote-anchor check (max 3485, zero duplicates/out-of-
  range, only the pre-existing 812 gap), curly-quote scan, and a
  hyphen-compound scan (page has no hyphens post-rejoin) all clean.
- **2026-07-22g**: Sessions A–E run for page 494 (III Nefi 5:15-26
  chapter close, III Nefi 6:1 chapter open, footnotes 3486-3491,
  letters k-o then 6a). Session A/B: mandatory 1879 check for letter l
  (this page's own letter, direct citation "Mormón 1:7," no Véase)
  confirmed via BOM 1879 Pratt file page 496 (chapter_map lists 495,
  content lands one page later — same drift pattern seen throughout
  this book): "k, see g. l, Mor. 1-7. m, see h, II. Nep. 1. n, see g,
  II. Nep. 3. o, see e, I. Nep. 15."; chapter 6's own letter a
  confirmed via 1879 file page 497 ("a, see m, I. Nep. 18."). Also
  discovered and corrected a page-493 indentation anomaly did NOT
  reflect the actual corpus convention: verse-start lines are flush
  left with no leading spaces almost everywhere (spot-checked 437, 440,
  460, 470, 479-481, 483, 486-488) — page 493's 4-space indent on its
  own opening line is an isolated inconsistency, not the standard;
  page 494 was transcribed flush-left. Four suspected floating-dot
  scan artifacts (v.15 "el.día", v.16 after "vida;", v.18 "hay.
  muchas", v.20 "soy·Mormón") and one narrow-space-vs-merge default
  (v.15 "delas" -> "de las") were all confirmed against 1886 (file
  pages 507-509, chapter_map III Nefi ch.5/6) in Session E: 1886 shows
  plain unmarked text at every scan-artifact spot and prints "de las"
  as two words. Session E also confirmed 3 new genuine 1920-only
  errors, all added to `errors in 1920.txt`: III Nefi 5:18 (the "18"
  missing its period, 1886 has "18."), III Nefi 5:18 "podermos" for
  "podemos" (1886 confirms — a different correction than the existing
  Helamán 16:20 "podermos" entry, which resolves to "podremos" at that
  page's own 1886 reading; this occurrence wasn't in this run's
  Spellcheck Suspect Words section because it's already blanket-
  suppressed by that earlier entry, not the "brand-new word" quirk),
  and III Nefi 5:22 "benedecidos" for "bendecidos" (1886 confirms,
  matches this page's own correct "bendecido" at v.21; added to
  `permitted words.txt` too since this run did flag it). Footnote-
  anchor check (full-document, max 3491): zero duplicates, zero
  out-of-range, only the pre-existing 812 gap. Curly-quote scan (zero
  curly quotes in either master file) clean; page 494's body text has
  no hyphens at all, so no dash-check findings. Jeebies clean.
- **2026-07-22h**: Sessions A–E run for page 495 (III Nefi 6:2-13,
  footnotes 3492-3499, letters b-i). Session A: mandatory 1879 check
  for letter i (this page's own letter, direct citation "Versículos
  21,22,27; Alma 10:14,15,17,27,32;14:5,18,23,27.", no Véase) confirmed
  via BOM 1879 Pratt file page 498 (chapter_map lists 3 Nephi ch.6 at
  497, content lands one page later — same drift pattern seen
  throughout this book); letters b-h cross-checked as a discretionary
  bonus. One hyphen rejoin ("pro-/visiones" → "provisiones") and one
  unconditional double-space normalization (v.2 "plata y  todas").
  Session B independently reconfirmed the mandatory i check from a
  fresh crop; no errors found. Session C/D integrated cleanly, all 8
  Block 2 entries resolved with no unresolved cross-references —
  notably "Véase h, III Nefi 3" (footnote e, 3495) correctly resolved
  to chapter 3's own letter h (3450), not chapter 6's, confirming
  book/chapter-scoped resolution across a same-book chapter gap.
  Session E: fresh pptext regeneration (report_wsl_20260722h.html)
  flagged 5 spellcheck suspects; confirmed 4 as new genuine 1920-only
  errors against 1886 (file pages 509-510) and added to `errors in
  1920.txt`/`permitted words.txt`: v.2 "specie" (→ especie), v.4
  "posperar" (→ prosperar, this page's own v.5 spells it correctly),
  v.9 "ásí" (→ así), v.9 "vientiocho" (→ veintiocho, same "vient-" for
  "veinti-" contraction-error pattern as III Nefi 5:7-8, even though
  1886 spells this instance out as "veinte y ocho" in three words).
  The 5th suspect, "retaliar" (v.13), was confirmed legitimate — 1886
  prints the identical word at the identical spot, and RAE DLE has
  related entries ("retaliación," "retaliador," regional Mexico/
  Venezuela usage from Latin "retaliare") confirming the root is real
  Spanish — added to `permitted words.txt` only. Two more Corrections-
  log suspects not flagged by pptext this run (known brand-new-single-
  occurrence quirk) were independently confirmed against 1886 and
  added to `errors in 1920.txt`: v.10 "vientinueve" (→ veintinueve,
  same pattern) and v.12 "oportuñidades" (→ oportunidades, stray tilde
  over "n"). Also confirmed and logged: v.9's "9" missing its period
  (1886 has "9.", every other verse number on the page has one) and
  v.12 "cause" for "causa" (1886: "á causa de sus riquezas" — "cause"
  is technically a valid Spanish word, the subjunctive of "causar," but
  doesn't fit grammatically here). The v.4 "completa en. el país"
  floating-dot scan-artifact call was confirmed against 1886 (plain
  text, no mark). Full-document footnote-anchor check (max 3499): zero
  duplicates, zero out-of-range, only the pre-existing 812 gap.
  Curly-quote scan clean; page has no hyphens post-rejoin, so no
  dash-check findings. Flagged for editor review per
  `feedback_narrow_space_vs_merge` (not a blocking question): v.2
  "consigo el," transcribed as two words per the current default.
- **2026-07-23**: Sessions A–E run for page 496 (III Nefi 6:14-22,
  footnotes 3500-3505, letters j-o). Session A: the first footnote's own
  letter was genuinely ambiguous between "i" and "j" by 1920 glyph shape
  alone (same curled-descender-plus-dot shape as the page's own "i"
  reference glyphs) — resolved via mandatory BOM 1879 Pratt check (file
  page 498: "j, III. Nep. 2:8." at the identical v.17 position before
  "thirtieth"/"treinta"), also consistent with strict sequential lettering
  (page 495 already used letter i as chapter 6's last letter). Letter l
  (v.21, mandatory i/l/1) confirmed via same-page glyph comparison plus
  BOM 1879 Pratt file page 499 ("l, see g, Mos. 26."); an initial misread
  of the target letter as "o" was caught and corrected to "g" via a
  tighter re-crop before finalizing. A floating ink blob in the margin
  after v.15 "inflándoles" was identified as a scan artifact, not a
  footnote marker — confirmed by letter-count accounting (6 letters in
  the block, 6 other confirmed body markers) and glyph-shape comparison.
  Two rule 7/8 line-length adjustments applied (hyphen rejoin
  "mantenién-/dose"→"manteniéndose"; "testificando in-/trepidamente"
  rejoined then re-split by rule 8 after marker insertion pushed it over
  72 chars) plus one marker-caused rule 8 overflow (v.21, "abogados"
  moved to the next line). v.22's "sumo-/sacerdote" line-break hyphen was
  identified as the compound word's own genuine hyphen (matching this
  page's own mid-line "sumo-sacerdotes" at v.21), not a rule 7 line-wrap
  split — left as printed. Session B independently re-verified all 6
  Block 1 entries and both mandatory 1879 checks from fresh crops,
  including re-confirming the l-target glyph is "g" not "o"; no errors
  found. Session C/D integrated cleanly, all 6 Block 2 cross-references
  resolved (l/o → 1520, Mosíah 26g; m/n → 3499, this chapter's own
  "abogados" footnote from page 495) with no unresolved targets. Session
  E: fresh pptext regeneration (`report_wsl_20260722i.html`) came back
  clean in the Spellcheck Suspect Words section for this page; the v.19
  suspected misprint "hallánbanse" (flagged in Session A's Corrections
  log) was confirmed as a genuine 1920-only error via 1886 (reads
  "hallábanse") plus independent RAE/modern-edition/corpus research —
  added to `errors in 1920.txt`; not pptext-flagged this run (known
  brand-new-single-occurrence quirk), so no `permitted words.txt` entry.
  Both "sumo-sacerdote(s)" hyphenation flags (v.21, v.22) were checked
  individually against 1886 and confirmed correct as printed. Footnote-
  anchor check (max 3505, zero duplicates/out-of-range, only the
  pre-existing 812 gap), curly-quote scan, and dash/hyphen scan all
  clean.
- **2026-07-23b, user correction**: user reviewing `chapters_emailed/
  Helaman_14.txt` caught that Helamán 14:6 "esesto" (page 474) is not a
  genuine merged-word print defect — the page image actually shows a
  real space between "es" and "esto". This was the founding precedent
  cited by two later narrow-space-vs-merge judgment calls (pages 479 and
  485's Corrections logs both reference "page 474's esesto" as their
  example of a confirmed true zero-space merge); those two pages' own
  corrections stand independently and were left as historical record,
  not rewritten. Corrected to "es esto" in `pages/page_474.txt`,
  `librodm.txt`, and `chapters_emailed/Helaman_14.txt`; removed the
  `permitted words.txt` entry for "esesto" (it was never added to
  `errors in 1920.txt`, so nothing to remove there). `page_474.txt`'s
  Corrections log entry for v.6 was updated to record the reversal
  rather than deleted.
- **2026-07-23c**: Sessions A–E run for page 497 (III Nefi 6:22-30
  chapter close, III Nefi 7:1-2 chapter open, footnotes 3506-3512,
  letters p-v). Session A: a thin, under-inked "l" in v.23 "las" and a
  stray ink blob above "e" in v.29 "eran" were both read as physical
  scan/ink artifacts rather than genuine letter substitutions (per the
  2026-07-18d precedent) and transcribed as the plain, grammatically-
  required words; a separate stray ink blob after "Ahora" (v.23, no
  letter shape) was identified as extraneous and not transcribed —
  this page's footnote block has exactly 7 letters (p-v), all fully
  accounted for by 7 confirmed body markers. v.23 "que fueron" (a true
  zero-width gap in the print) was transcribed as two words per the
  2026-07-22 default (grammar requires two words; no pixel analysis).
  v.27 "sumo-sacerdotes" retains its own compound hyphen (matching the
  page 496 precedent), not rule-7 rejoined. Mandatory 1879 check for
  footnote t's target letter "i" (t itself isn't i/l/1, but its
  citation "Véase i" is) confirmed via BOM 1879 Pratt file page 499 —
  all seven letters p-v matched letter-for-letter and target-for-
  target, including body-text marker placement ("the [t]lawyers and
  the [u]high priests," v.27). Session B independently re-verified
  from fresh crops, including re-confirming file page 499 (not 500,
  which turned out to already be chapter 7's own footnote block) is
  the correct 1879 page for this content. Session C/D integrated
  cleanly, all 7 Block 2 cross-references resolved with strong content
  fit (r → Omni 1h, "Es supuesto que la tierra de Zarahemla estaba al
  norte..."; v → Mosíah 29m, the recurring Alma-46 liberty citation).
  Session E: fresh pptext regeneration (`report_wsl_20260723.html`)
  came back clean in Spellcheck Suspects/Edit Distance for this page.
  All four of Session A's scan-artifact/narrow-space judgment calls
  were independently confirmed against 1886 (file pages 511-512, book
  493-494) and held up unchanged. One new genuine 1920-only error was
  found and confirmed: III Nefi 6:27 "juntamente, y, se unieron" has a
  spurious extra comma after "y" that 1886 doesn't have (1886: single
  comma, after "juntamente" only) — added to `errors in 1920.txt`; no
  `permitted words.txt` entry needed (punctuation, not spelling). The
  "sumo-sacerdotes"/"Sumo Sacerdotes" hyphenation category's new v.27
  instance was individually checked (not waved through) and confirmed
  to match 1886's own hyphenation at that spot. Footnote-anchor check
  (union of both pptext buckets, range 1-3512): zero duplicates, zero
  out-of-range, only the pre-existing 812 gap. Curly-quote scan and
  dash check (only the expected pending "sepa-" page-boundary hyphen)
  both clean.
- **2026-07-23d**: Sessions A–E run for page 498 (III Nefi 7:2(continues)-12,
  footnotes 3513-3515, letters a-c). Session A resolved page 497's pending
  page-boundary hyphen split first (rule 10): "sepa-" + this page's first
  word "raron" rejoin to "separaron"; appending the completed word to page
  497's last line keeps it at 67 characters, under the cap, so it was
  placed there and page 498's body text begins with the next word, "unos,"
  instead — `pages/page_497.txt` and its already-integrated copy in
  `librodm.txt` were both revised accordingly. Mandatory 1879 check for
  footnotes a and c's shared cross-reference target letter "i" ("Véase i,
  II Nefi 10" — the target letter is in the mandatory set even though a/c
  themselves are not) confirmed via BOM 1879 Pratt file page 500
  (chapter_map lists 3 Nephi ch.7 at 1879 file 500; this time content
  lands on the exact listed page, no drift): "a, see i, II. Nep. 10. b,
  III. Nep. 5:7. c, see i, II. Nep. 10." matches letter-for-letter and
  target-for-target — the same recurring "secretas combinaciones" II Nefi
  10 citation already established on pages 492/493/495. Session B
  independently reconfirmed both the footnote block and the 1879 check
  from fresh crops; no errors found. Session C/D integrated cleanly, both
  cross-references resolving to the same existing sequential number (398,
  II Nefi 10's own letter-i footnote). Session E: fresh pptext
  regeneration (`report_wsl_20260723b.html`) came back clean across every
  section for this page's new range — no spellcheck suspects, no edit-
  distance hits, no new hyphenation/dash findings (page 498 has no
  hyphens at all), footnote-anchor check (max 3515, zero duplicates,
  zero out-of-range, only the pre-existing 812 gap) clean, curly-quote
  and scanno checks clean, special-situations and paragraph-level checks
  (including "full stop followed by unexpected sequence") showed nothing
  new, Jeebies clean. One Corrections-log item promoted to `errors in
  1920.txt` after the mandatory 1886/independent-research check: v.12
  "vivían alagados de que habría" — 1886 shares the identical spelling
  (a shared-error case, same pattern as "aparacerá"/"seperado"/
  "frustado"), but "alagado" is a real, unrelated Spanish word (an
  Argentina/Bolivia regionalism for flooded/inundated terrain, confirmed
  via RAE), while the modern Spanish LDS edition uses "halagó" at this
  exact verse ("porque los halagó, diciéndoles que habría muchos
  disidentes"), matching 1879's English "for he flattered them" —
  confirmed genuine missing-"h" error; no `permitted words.txt` entry
  needed since pptext doesn't flag "alagados" (it's a real dictionary
  word). Two stray scan-artifact ink marks (v.2 after "país.", v.3 after
  "gobernador") were confirmed against 1886 as plain unmarked text,
  consistent with the established floating-mark precedent. One
  unconditional rule-6 space normalization applied (v.12's last line,
  wider gap after "pueblo." before "Y así lo hicieron").
- **2026-07-23b**: Sessions A–E run for page 499 (III Nefi 7:13-21,
  footnotes 3516-3519, letters d-g). Session A: none of this page's own
  letters (d-g) or footnote reference targets (plain verse/chapter
  citations, no "Véase") are in the mandatory i/l/1 set, so no mandatory
  1879 check applied; all four letters assigned by strict sequential
  position, confirmed by same-page glyph comparison (this page's own "d"
  vs. the fn_zoom block's final glyph, a closed bowl + descender loop
  matching a lowercase italic "g"). One rule-7 hyphen rejoin ("in-" +
  "mundos" → "inmundos"), which then triggered a rule-8 rebalancing
  cascade since the rejoined line exceeded 72 characters. Three
  unconditional rule-6 space normalizations (justification-widened gaps
  after sentence-ending periods, v.13/14/17). Two suspected misprints
  flagged and preserved as printed per rule 32: v.15 "abdominaciones"
  (spurious extra "d") and v.16 "coracones" (missing "z"/"c" for "z"
  substitution) — the same word, "corazones," is spelled correctly two
  verses earlier at v.14, isolating v.16 as a one-off. Session B
  independently re-verified all four Block 1 entries and body markers
  from a fresh crop; no errors found. Session C/D integrated cleanly via
  the scripts, no unresolved Block 2 cross-references (all four entries
  were direct verse/chapter citations, not "Véase" pointers). Session E:
  both suspected misprints confirmed as genuine 1920-only errors against
  1886 (file page 514, chapter_map 3 Nephi ch.7) — 1886 reads
  "abominaciones" and "corazones" at the respective spots — plus RAE
  (no entry for either 1920 form) and zero hits in all three reference
  corpora for either misspelling (vs. 60 corpus hits for "abominaciones"
  and dozens for "corazones"); both added to `errors in 1920.txt`.
  "abdominaciones" is pptext-flagged this run (Spellcheck Suspects +
  Edit Distance), so it was also added to `permitted words.txt`;
  "coracones" is not flagged (known brand-new-single-occurrence quirk),
  so no `permitted words.txt` entry for it. Fresh pptext regeneration
  (`report_wsl_20260723d.html`) came back clean everywhere else for the
  new range: footnote-anchor check (3512-3519 fully covered across both
  buckets, zero duplicates/out-of-range, only the pre-existing 812 gap),
  curly-quote scan (zero curly quotes in either master file), dash/hyphen
  check (page has no hyphens post-rejoin), and paragraph-level/Jeebies
  checks all clean (the only paragraph-level hits were the long-
  established false-positive verse/page-boundary pattern).
- **2026-07-23e**: Sessions A–E run for page 500 (III Nefi 7:22-26 chapter
  close, III Nefi 8:1-5 chapter open, footnotes 3520-3527, letters h-j
  then chapter 8 restarts at a-e). Session A: mandatory 1879 check for
  letter i (v.24) confirmed via BOM 1879 Pratt file page 502
  (chapter_map lists 3 Nephi ch.8 1879 page as 502, matching exactly):
  "h, ver. 19.  i, see u, II. Nep. 9.  j, see u, II. Nep. 9." — an
  unusual but confirmed-genuine case where two consecutive footnotes (i
  and j) cite the identical target; chapter 8's own letters a-e were
  independently confirmed as a bonus via the same 1879 page 502 (a-d)
  and page 503 (e — 1879's denser typesetting packs much more of
  chapter 8 per page, so letter e prints on a later 1879 page than a-d
  despite being the same 1920 page). One rule-8 marker-caused overflow
  (chapter 8 v.3, inserting footnote 3526 before "tinieblas" pushed the
  line to 73 chars, so "extensión" moved to the next line) and one
  hyphen rejoin (v.23 "arrepenti-"/"miento", landing at exactly 72
  chars). A small raised apostrophe-like mark between "días" and "en"
  (chapter 8 v.3) was identified as a scan artifact, matching the
  established floating-mark precedent (pages 483, 490, 492, 494, 497);
  confirmed clean against 1886 (file page 515) in Session E. Session B
  independently re-verified all eight Block 1 entries and body markers
  from fresh crops, plus re-ran the mandatory i/j check from a fresh
  1879 crop. Session C/D integrated cleanly; both cross-references
  (footnotes i and j) resolved to the same existing sequential number
  (378, II Nefi 9's letter u — the recurring baptism-scripture
  citation, a strong content fit for this page's baptism verses).
  Session E: fresh pptext regeneration (`report_wsl_20260723.html`)
  flagged one spellcheck suspect, "dolencías" (v.22) — this turned out
  to be a genuine Session A transcription error, not a 1920 print
  question: a fresh zoom showed the 1920 print has no accent at all
  ("dolencias"), confirmed against 1886 (file page 514, also
  unaccented). Corrected in `pages/page_500.txt` and `librodm.txt`; no
  `permitted words.txt`/`errors in 1920.txt` entry needed (rule 12 —
  transcription error, not a genuine-word or 1920-print question).
  Footnote-anchor check (full-document, max 3527): zero duplicates,
  zero out-of-range, only the pre-existing 812 gap. Curly-quote scan
  (zero curly quotes in either master file) clean; page has no hyphens
  post-rejoin, so no dash-check findings; short-lines/paragraph-level
  hits were all the long-established false-positive verse/Block-2-entry
  pattern.
- **2026-07-23e**: Sessions A–E run for page 501 (III Nefi 8:5(continues)-19,
  footnotes 3528-3554, letters f-z then two-letter codes 2a-2f — by far
  the densest footnote page transcribed so far, averaging nearly one
  marker per line). Session A/B: mandatory 1879 check for letters i
  (v.8, "ciudad de Zarahemla") and l (v.11, "Sud") confirmed via BOM
  1879 Pratt file page 503 (chapter_map III Nefi ch.8, "one page later"
  drift). Three separate footnote-target-letter misreads surfaced and
  were corrected across Sessions A/B/D, each requiring more than one
  round of re-zooming: (1) footnote i's own target read "k" then
  corrected to "h" (Session A, confirmed via 1879 and glyph shape);
  (2) footnote r's target went through THREE readings — "o" (Session
  A), then wrongly "corrected" to "y" (Session B, based on a misread of
  both the 1920 glyph and the 1879 comparison), before `generate_
  block2.py`'s unresolved-cross-reference report exposed the problem
  (III Nefi 6, already fully transcribed on pages 494-497, has no
  letter "y" — its own lettering runs only a-v, and a fresh check
  confirmed 1879's OWN chapter 6 also stops at v) — re-examined a third
  time and settled as "g", confirmed by a decisive content-fit: III
  Nefi 6g (footnote 3497) cites "Helamán 14:24; III Nefi 8:13," and
  Helamán 14:24 itself reads "se romperán muchas calzadas" — a direct,
  mutual mirror-image cross-reference to this page's own v.13 "se
  rompieron las calzadas"; (3) footnote 2f's target was disputed
  between Claude's own uncertain reads ("v" vs "r") — the editor did
  their own direct comparison of the page's reference glyphs and
  settled it as "v" (matching 1879 and the same kind of decisive
  content-fit: Helamán 14v/3375 already cites "III Nefi 8:6,12,19,"
  this exact verse). All three corrections are reflected in
  `pages/page_501.txt`, `librodm_foot.txt`, and `librodm.txt`'s Block 2
  (3540 now resolves to 3497). Added optional `left_pct`/`right_pct`
  arguments to `crop_page.py` this session — a full-width crop, even at
  high zoom, was not high-resolution enough to distinguish some of
  these small superscript glyphs; narrowing the crop horizontally
  fixed this. Session C/D integrated cleanly otherwise (26 of 27 Block
  2 cross-references resolved automatically; the 27th, footnote r, was
  hand-resolved after the letter correction above). Session E: fresh
  pptext regeneration (`report_wsl_20260723c.html`) came back clean
  across every section for the new range — no spellcheck suspects, no
  edit-distance hits, footnote-anchor check (union of both buckets)
  confirmed 3520-3554 fully covered with zero duplicates/out-of-range,
  the one dash-check hit in range is the expected verse-range hyphen
  (rule 23), "spaced punctuation" hits are all the document-wide
  established space-before-semicolon convention (not page-specific),
  book/paragraph-level checks and Jeebies clean. This page's own
  Corrections log had no suspected-misprint/spelling notes, so no
  `errors in 1920.txt`/`permitted words.txt` entries were needed at
  all for this page — a rare fully-clean orthography pass. **Lesson
  for future pages**: this page's unusually high rate of footnote-
  target misreads (3 of 27) suggests worn/small type in this specific
  footnote block warrants extra care — cross-check every resolved
  target against `generate_block2.py`'s unresolved-reference report
  and, when in doubt, prefer the target chapter's own already-
  transcribed lettering plus content-fit over a single zoomed glyph
  read.
- **2026-07-23f**: Sessions A–E run for page 502 (III Nefi 8:19(continues)-25
  chapter close, III Nefi 9:1-2 chapter open, footnotes 3555-3561, letters
  8-2g through 8-2l then chapter 9 restarts at a). Session A/B: mandatory
  1879 checks for footnote 8-2j's cross-reference target letter "i"
  ("Véase i, I Nefi 19") and footnote 8-2l's own marker letter "l" — both
  in the mandatory i/l/1 set. Same-page glyph comparison confirmed both
  (short stroke + separated dot for "i"; continuous unbroken curve for
  "l"). No live 1879 parallel existed for 8-2l specifically (1879's own
  chapter 8 footnote lettering ends at plain "j" on file page 502 — this
  chapter is far denser in 1920's footnoting than 1879's, roughly 38
  1920 letters vs.1879's 10), so an independent same-chapter back-
  reference check was used instead (8-2l's "Véase k" resolves to chapter
  8's own earlier footnote k = 3533, "Versículo 25...", a strong
  content-fit for this exact v.24-25 passage). For 8-2j's target, a live
  1879 read of I Nefi chapter 19's own footnote block (file page 57)
  confirmed letter i's content ("Hela. 14:20,27. III. Nep. 8:19-23.
  10:9.") matches this page's own 8-2i almost exactly. Two genuine
  zero-width print merges (v.23 "loscuales", "vistaninguna") were
  normalized to two words per the current rule-6 default (grammar
  requires two words; no zoom/pixel debate), later spot-confirmed
  against 1886 (file page 517) as two words there too. Session C/D
  integrated cleanly; both cross-references resolved correctly (8-2j
  to 177, I Nefi 19's own letter i; 8-2l to 3533, chapter 8's own
  earlier k). Session E: fresh pptext regeneration
  (`report_wsl_20260723e.html`) came back fully clean for the new
  range — no new spellcheck suspects, no new edit-distance hits,
  footnote-anchor check (1-3561, zero duplicates/out-of-range, only
  the pre-existing 812 gap) clean, curly-quote scan clean, the two
  dash-check hits in range are expected verse-range hyphens (rule 23),
  "spaced punctuation" hits match the established recent-pages
  convention, book/paragraph-level checks and Jeebies both clean. No
  `errors in 1920.txt` or `permitted words.txt` entries needed — a
  fully clean orthography pass.
- **2026-07-24, user correction**: user spotted that page 502 had many
  instances of a space preceding ";" and "!" that should have been
  removed. Root cause: a series of Session E notes on pages 496-502
  wrongly declared "space before ; and !" an "established recent-pages
  convention" to be preserved as printed — this was never actually
  licensed by rule 31, which already named "semicolon" explicitly
  alongside comma/colon; the "convention" note directly contradicted the
  existing rule. Separately, this is also why it kept slipping past
  pptext review: pptext's report has a dedicated "spaced punctuation"
  section (distinct from the unrelated, always-empty "spacing pattern
  check" near the top of the report) that was flagging every one of
  these all along, but that section was never on the `orthography-check`
  skill's pptext-walkthrough progress tracker, so Session E never
  actually reviewed it. Fixed: rule 31 in `libro_de_mormon_rules.md` now
  explicitly names exclamation and question marks and documents this
  correction so the "convention" isn't reinvented; the `orthography-check`
  skill now has a dedicated "Spaced punctuation check" subsection and the
  section was added to the progress tracker; `pages/page_502.txt` and
  `librodm.txt` were both fixed (12 instances: v.19 x2, v.20, v.21 x2,
  v.23, v.24, v.25 x3, ch.9 v.1 x2). **Not yet done**: pages 471-495
  contain earlier, sporadic instances of the same pattern (confirmed via
  the pptext report's spaced-punctuation section, which shows hits
  starting around Helamán 13) and have not been swept — scoped out of
  this fix per the user's page-502-specific request; worth a dedicated
  full-range sweep in a future session.
- **2026-07-24b**: Completed the full retroactive sweep flagged at the end
  of the prior entry. User noticed the space-before-";"/"!" pattern
  going back further than page 502 (as far back as page 470) and asked
  for a full pptext "spaced punctuation" pass across all of `librodm.txt`.
  Regenerated pptext (`report_wsl_20260724.html`), pulled every hit in
  the "spaced punctuation" section (86 instances total, none before page
  470 — pages up through ~469 are unaffected), and fixed all of them:
  `librodm.txt` (86 instances), `pages/page_470.txt` (1), `page_476.txt`
  (13), `page_495.txt` (11), `page_496.txt` (11), `page_497.txt` (6),
  `page_498.txt` (13), `page_499.txt` (13), `page_500.txt` (8),
  `page_501.txt` (10) — all body text only, historical Corrections-log
  quotes of the old (wrong) reading were left as documentation, with a
  new note added to each page explaining the reversal (and correcting
  two pages, 496 and 501, whose own Session E notes had explicitly
  mis-described the pattern as an "established convention" — see rule 31
  in `libro_de_mormon_rules.md`). Also fixed the same content in the
  three already-emailed chapter files affected: `chapters_emailed/
  Helaman_13.txt` (1), `Helaman_14.txt` (9), `Helaman_15.txt` (4);
  `Helaman_12.txt` had no instances. Used a bulk Python script for the
  actual text substitution rather than one-by-one edits, given the
  volume — this surfaced a real hazard worth remembering: the script's
  first pass wrote plain LF line endings, silently flattening the three
  `chapters_emailed` files (which are CRLF, unlike `librodm.txt`/
  `pages/*.txt`, which are already LF) and inflating their diffs from a
  handful of real changes to hundreds of spurious ones; caught via `git
  diff --stat` before anything was committed and fixed by restoring CRLF
  on just those three files. **Lesson for future bulk text edits**: check
  original line-ending format per file before a script-based rewrite
  (`file <path>` or inspect for `\r\n`), since this project's `.txt`
  files are not uniform (CRLF in `chapters_emailed/`, LF elsewhere) and a
  naive Python text-mode read/write can silently convert one to the
  other. Also, mid-investigation, `git stash` was run to inspect a
  pre-fix file version and briefly reverted all uncommitted work in the
  working tree — recovered immediately with `git stash pop`, no work
  lost, but a reminder to prefer `git show HEAD:<path>` over `git stash`
  for read-only historical comparisons when there are uncommitted changes
  in flight. Verified clean via a fresh pptext regeneration
  (`report_wsl_20260724b.html`): the "spaced punctuation" section no
  longer appears in the report at all (pptext omits sections with zero
  findings), confirming zero remaining instances anywhere in
  `librodm.txt`. Separately noted but NOT fixed (out of scope, different
  rule/vintage): `librodm_foot.txt` has 4 old citation-formatting
  instances of space-before-";"/":" (e.g. "I Nefi 4:9 ; II Nefi 5:15",
  "Isaías 65 : 17 ; 66 : 22") that look like an unrelated, older
  inconsistency violating rule 22 (no spaces around colons in
  references), not rule 31 — worth a separate cleanup pass sometime.
- **2026-07-24c**: Fixed the 5 space-before-punctuation instances found in
  `librodm_foot.txt` at the end of the prior entry (all older citation-
  formatting slips, unrelated in age to the pages 470-502 issue): "I
  Nefi 4:9 ; II Nefi 5:15" → no space before ";" (fn 140), "Enos 1:12-18 ;
  Alma 37:1-20" → same (fn 280), "Isaías 65 : 17 ; 66 : 22." → no spaces
  around colon or semicolon (fn 350), "Jeremías 50:16 ; 51:9." → no space
  before ";" (fn 608), "II Nefi 2 : 16" → no space around colon (fn
  1935). Per the user's request, added two permanent scripts (rather than
  relying on a rule alone) so this class of defect gets caught
  mechanically going forward: `check_spaced_punctuation.py` (rule 31,
  wired into `transcribe-page` step 9 to run before `check_lines.py`, and
  into `orthography-check`'s new "Spaced punctuation check" section to
  run against the whole document every Session E) and
  `check_footnote_punctuation.py` (rules 22/23, defaults to
  `librodm_foot.txt`, same wiring). Both scripts print line-number hits
  with a summary count; verified against the full corpus post-fix:
  `librodm.txt` and `librodm_foot.txt` both come back clean, and a sweep
  of every `pages/*.txt` file turned up 145 additional hits that were all
  confirmed to be historical Corrections-log quotes of already-fixed
  readings (documentation, not live defects) — spot-checked page 441's
  18 hits individually to confirm the pattern before accepting this
  conclusion for the rest.
- **2026-07-24d**: Sessions A–E run for page 503 (III Nefi 9:2(continues)-11,
  footnotes 3562-3574, letters 9b-9n). Session A: mandatory 1879 check for
  footnotes m and n's shared cross-reference target letter "i" (i is in
  the mandatory i/l/1 set) — same-page glyph comparison (short stroke +
  separated dot, distinct from this page's own "l," a continuous unbroken
  stroke) confirmed via BOM 1879 Pratt file page 505 for m ("m, see i.");
  1879's own chapter 9 lettering stops at m with no "n" printed at all
  (same denser-1920-footnoting pattern as page 502's 8-2l), so n's target
  was independently corroborated via content-fit (chapter 9's own i cites
  "Versículo 10," the burning-of-cities verse both m and n continue).
  Session B independently reconfirmed all 13 Block 1 entries and both
  1879 checks from fresh crops; no errors found. Session C's
  `insert_body_text.py` crashed on first run because this page's Block 1
  entries omitted the required chapter-number prefix (rule 16 — "9b" not
  just "b"); body text had already landed cleanly by that point, so the
  page file's entry labels were fixed and the script re-run with
  `--footnotes-only`. Session D's `generate_block2.py` resolved all 13
  entries cleanly, confirming m and n both resolve to the same target
  (3569), matching the Session A/B reasoning. Session E: fresh pptext
  regeneration (`report_wsl_20260724c.html`) flagged 8 spellcheck
  suspects — 7 legitimate Book-of-Mormon place names unique to this
  passage (Gad, Gilgal, Gimgimno, Jacobúgath, Josh, Mocum, Oníhah, all
  confirmed against 1886 file pages 517-518, added to `permitted
  words.txt` only) and "presenca" (v.9), confirmed as a genuine
  1920-only error (1886 reads "presencia" at this spot, this same page
  spells "presencia" correctly twice elsewhere, zero corpus hits, no RAE
  entry) — added to both `errors in 1920.txt` and `permitted words.txt`.
  Two more Session A/B suspected-misprint Corrections items were
  confirmed against 1886 and added to `errors in 1920.txt` (punctuation,
  no `permitted words.txt` entries needed): v.9 "país.;" (1886 reads
  "pais:" with a colon — 1920's period-immediately-followed-by-semicolon
  is a composition error) and v.11's verse number missing its period
  (1886 prints "11.", 1920 omits it here while using it on all eight
  other verse numbers on the page). Footnote-anchor check (max 3574,
  zero duplicates/out-of-range, only the pre-existing 812 gap), curly-
  quote scan, dash check (only legitimate verse-range hyphens in the new
  Block 2 entries), hyphenation/character checks, special situations,
  and paragraph-level checks all clean; Jeebies clean.
  `check_spaced_punctuation.py`/`check_footnote_punctuation.py` both
  confirm the full document is clean.
- **2026-07-24e**: Sessions A–E run for page 504 (III Nefi 9:11(continues)-21,
  footnotes 3575-3587, letters o-z then two-letter code 2a). Session A:
  mandatory 1879 check for footnote 9o's cross-reference target letter "i"
  ("Véase i, Helamán 14" — target letter is in the mandatory set even
  though o itself isn't) confirmed via BOM 1879 Pratt file page 476/477
  (chapter_map Helamán 14, "one page later" content-drift pattern already
  established for this book): Helamán 14's own footnote i reads "Mos.
  3:8. 15:4. Alma 11:39. III. Nep. 9:15. Ether 4:7.", sharing "Mos. 3:8"
  with 1920's own 9o citation and matching v.15's Christ's-eternal-nature
  content. Two rule-6 defaults applied without pixel analysis: v.14
  "quemi brazo" (zero-width print merge) transcribed as "que mi brazo"
  since grammar requires two words; v.17 "por·mí" (a floating scan-artifact
  dot) transcribed as a plain space, matching the established floating-
  mark precedent. One suspected misprint preserved as printed per rule 32:
  v.18 "la luz la vida del mundo" (missing "y"). Footnote 9y's citation
  is unusually long (a "no more shedding of blood" cross-reference chain
  spanning nearly every book) and was initially misread as a double-colon
  print anomaly, "I Nefi 10:17,19,22:13:37" (Session A/B zoom crops both
  appeared to show two evenly-stacked-dot colons) — a reasonable-effort
  1879 search during Session E found no parallel entry, since 1879's own
  chapter 9 lettering is far sparser than 1920's. The editor then reviewed
  both the 1920 print and 1879 directly, including the source PDF's own
  embedded text layer, and confirmed the first mark (after "22") is
  actually a semicolon: the correct reading is "I Nefi 10:17,19,22;
  13:37" (verses 17/19/22 of ch.10, then a new citation, ch.13 v.37,
  same book) — fixed in `pages/page_504.txt`, `librodm_foot.txt`, and
  `librodm.txt`'s Block 2 entry (3585) after Session E. All 39 body
  lines came in under the 72-char cap with zero rule-8 rebalancing needed.
  Session B independently re-verified all 13 Block 1 entries against a
  fresh full-block crop (including the 9y anomaly, at the time still
  unresolved, and the repeated "III Nefi 15:2-8" citation shared by
  9v/9x) and re-ran the mandatory 1879 check from a fresh crop — both
  reconfirmed exactly. Session C/D
  integrated cleanly (`insert_body_text.py 504`, `generate_block2.py
  504`), all 13 cross-references resolved with no unresolved targets
  (spot-checked 9o→Helamán 14i=3362, 9u→Mosíah 5d=1130, 9w→Mosíah 16m=1323,
  9-2a→same-chapter 9u=3581, all book-aware matches confirmed correct);
  one stray space the script's line-rewrap introduced mid-reference
  ("14, 20-22" for "14,20-22") was caught and fixed directly in
  `librodm.txt`. Session E: fresh pptext regeneration
  (`report_wsl_20260724c.html`) flagged one spellcheck suspect, "Alpha"
  (v.18) — confirmed legitimate via 1886 (file page 519, chapter_map III
  Nefi ch.9), which also prints "Alpha" (not "Alfa"), confirming this is
  the established period spelling for the translation, not an error;
  added to `permitted words.txt` only. The same 1886 comparison confirmed
  v.18's "la luz la vida del mundo" as a genuine 1920-only error (1886:
  "la luz y la vida del mundo") — added to `errors in 1920.txt`.
  Full-document footnote-anchor check (max 3587): zero duplicates, zero
  out-of-range, only the pre-existing 812 gap. Curly-quote scan and
  `check_spaced_punctuation.py`/`check_footnote_punctuation.py` (both run
  document-wide per the 2026-07-24 standing instruction) all clean. One
  item was flagged for the editor rather than resolved unilaterally —
  v.14's "que mi brazo" narrow-space-vs-merge default (per
  `feedback_narrow_space_vs_merge`, worth a look at the actual page) —
  still open as of this writing. The other flagged item, the 9y
  footnote's double-mark citation, was resolved the same day: the
  editor's direct review of the 1920 print, 1879, and the source PDF's
  embedded text layer confirmed the mark is a semicolon, not a second
  colon (see above).
- **2026-07-25**: Built and validated a new cross-check tool
  (`extract_google_text.py` + `check_google_crosscheck.py`) that diffs a
  transcribed page's body text against the 1920 PDF's own embedded/
  Google-OCR text layer, as a second opinion on letter-level misreads —
  wired into `transcribe-page` as Session A step 10. Design settled
  through discussion: character-level diff with whitespace AND hyphens
  stripped from both sides (so Google's frequent word-fusion never
  surfaces as a diff and can never be used to argue against a narrow-
  space-vs-merge call — see `feedback_narrow_space_vs_merge`), plus an
  auto-dismiss rule for short glued-superscript noise at known footnote-
  marker positions (not worth zooming for). Two real implementation
  snags, both resolved: raw `pdftotext` defaults to Latin-1 output and
  silently mangles every accented character (fixed with `-enc UTF-8` —
  ended up using `pdfplumber` instead, tuned to `x_tolerance=1.5`, which
  turned out to fix a separate word-fusion problem too); and no PDF
  vector geometry exists for the footnote-block divider (it's part of
  the scanned image, not a drawn line), so rather than chase a pixel-
  perfect crop, the extraction just pulls the whole page and the diff
  stage naturally ignores anything past the end of the already-
  transcribed body stream. Validated against pages 503-504 (both fully
  vetted already): page 503 correctly re-surfaced the already-known
  "país.;" double-punctuation case; page 504 caught one genuine,
  previously-undetected transcription error — v.13 "habéis" (typed)
  vs. the actually-printed "habeís" (misplaced accent, confirmed via
  high-zoom re-read) — which had passed every existing check because
  "habéis" is itself a valid word, so pptext/aspell had nothing to flag.
  Fixed in `pages/page_504.txt` and `librodm.txt`; added to `errors in
  1920.txt` (III Nefi 9:13) after confirming a matching pattern: 150+
  correct "habéis" instances elsewhere in `librodm.txt`, one other
  pre-existing uncaught instance of the identical error at II Nefi 1:25
  (already in `permitted words.txt`, never logged in `errors in
  1920.txt` until now), and RAE's unambiguous stress on é. User noted
  the 1920 editor/typesetter was a native English speaker with strong
  but non-native Spanish — exactly the profile likely to mis-stress an
  archaic/biblical conjugated verb form rather than misspell ordinary
  vocabulary, which fits this error category and is worth keeping in
  mind for future Session E accent-placement questions on unusual verb
  forms. Re-ran the cross-check after the fix: 0 remaining candidates
  for page 504.
- **2026-07-25a**: Sessions A–E run for page 505 (III Nefi 9:22 chapter
  close, III Nefi 10:1-9, footnotes 3588-3594, letters 9-2b then 10a-f).
  Session A: mandatory 1879 check for footnote 10e's cross-reference
  target letter "i" (I Nefi 19) confirmed via BOM 1879 Pratt file page
  57 ("i, Hela. 14:20,27. III. Nep. 8:19-23. 10:9."), a strong content
  fit with this page's own footnote 10f (III Nefi 8:19-23). One floating
  scan-artifact ink mark identified and not transcribed (footnote 10f,
  matching the established pattern). This page has a chapter heading
  (`CAPÍTULO 10.`) just 5 lines in, which exposed a real blind spot in
  `check_line_wrap.py` and `check_google_crosscheck.py`: both tools stop
  reading a page's "body lines" at the first blank line, so neither
  tool's automated pass reached anything past v.22 — a manual read of
  the full `google_text_1920/page_0527.txt` OCR text against the rest of
  the page caught a genuine transcription slip the automated check
  couldn't reach (v.7 "vuéstros," typed with an accent by mistake; the
  print reads unaccented "vuestros" — confirmed at high zoom and via
  1886). Session B independently reconfirmed all 7 Block 1 entries, the
  body markers, and the mandatory 1879 check from fresh crops; no errors
  found. Session C/D integrated cleanly, both Block 2 cross-references
  (10d/10e) resolved correctly and book-aware (128: I Nefi 15's own
  letter e; 177: I Nefi 19's own letter i, matching the 1879
  confirmation exactly). Session E: fresh pptext regeneration
  (`report_wsl_20260724d.html`) flagged 3 spellcheck/edit-distance
  suspects. Confirmed 2 new genuine 1920-only errors against 1886 (file
  pages 517/519/520): III Nefi 9:22 "quienquiera. que" (1886 has no
  punctuation at all between the two words — a genuine baseline period,
  not the floating-ink-artifact pattern) and III Nefi 10:7 "epoca" (1886
  and 33 other instances elsewhere in `librodm.txt` all accent "época,"
  an esdrújula word RAE requires to be accented). Also added a
  footnote-text entry for 10f's "Háciendo" — no 1886 comparison possible
  (1886 carries no footnotes), but RAE/WebSearch confirms a regular
  gerund like "haciendo" never takes an accent, matching the internal
  corpus evidence (34 correctly-spelled instances elsewhere). All three
  pptext-flagged words added to `permitted words.txt`. A fourth flagged
  word, "salváos" (v.22), confirmed legitimate — 1886 prints the
  identical accented form at the identical spot, matching the
  established archaic accented-imperative-plus-enclitic-pronoun pattern
  (apoderáos/entregáos, pages 479/487); added to `permitted words.txt`
  only. Footnote-anchor check (max 3594, zero duplicates/out-of-range,
  only the pre-existing 812 gap), `check_spaced_punctuation.py`/
  `check_footnote_punctuation.py` (whole document), independent
  curly-quote character scan, dash check, special situations, book-
  level, paragraph-level, and Jeebies checks all clean.
- **2026-07-25b**: Sessions A–E run for page 506 (III Nefi 9:9(continues)-18
  chapter close, footnotes 3595-3612, letters g-x — an unusually dense
  footnote page, 18 letters in one page). Session A: mandatory 1879
  check for this page's own letters i and l, plus g's and p's shared
  cross-reference target letter "i" (target letters are mandatory too),
  confirmed via same-page glyph comparison (i = short stroke + separated
  dot; l = continuous stroke, no dot) and BOM 1879 Pratt file page 508
  (chapter_map III Nefi ch.10, "one page later" drift — chapter 10's
  own a-f footnotes landed on 1879 file 507, g-x on 508); 1879's own
  h/i/j/k/l/m/o/r/t/u/w matched letter-for-letter and content-for-
  content, confirming the base sequence, while several "Véase"-style
  cross-reference target letters (g, n, p, q, v) diverged from 1879's
  own choices — expected rule-26 translation-word-order drift in how
  each edition letters the TARGET chapter, not an error. Footnotes n
  and q's target (visually resembling this page's own "n" glyph) was
  resolved as the two-letter code "2i" (III Nefi 8's own extended
  lettering) via both 1879's independent "see 2i" reading and a strong
  content-fit: III Nefi 8-2i (3557) itself cites "III Nefi 10:9" — this
  very page. One rule-8 marker cascade spanning four lines (two markers
  landing on one line pushed the overflow all the way to the start of
  v.15's own line, "profetas. 15. He aquí..." — verse boundaries are not
  a stopping point for the cascade). Session C/D integrated cleanly
  except one Block 2 cross-reference (footnote 10x, "Véase s, I Nefi
  3") that `generate_block2.py` couldn't resolve — I Nefi chapter 3's
  own lettering only runs a-h, so "s" can't be a valid target there; a
  high-zoom crop of the 1920 glyph showed an illegible, over-inked
  blob, and both BOM 1879 Pratt ("see a") and content-fit (I Nefi 3a
  cites the brass-plates retrieval, matching this page's own v.17
  "planchas de bronce") converged on target letter "a" instead;
  corrected and resolved by hand (Véase 12). The Google-text cross-check
  (Session A step 10) caught one genuine transcription error the
  initial read had missed — v.18 "reciberon," typed as the expected
  "recibieron" until a fresh zoom confirmed the print actually reads
  "reciberon" (missing "i") — and correctly cleared one false alarm (a
  garbled OCR artifact at a footnote-marker position, confirmed via
  zoom that the real "y" is genuinely printed there). Session E: fresh
  pptext regeneration (`report_wsl_20260724e.html`, re-confirmed clean
  via `report_wsl_20260724f.html`) flagged 2 words: "hendirse" (v.9,
  confirmed legitimate — matches 1886 exactly) added to `permitted
  words.txt` only; "reciberon" confirmed as a genuine 1920-only error
  (1886: "recibiéron"; zero RAE/corpus hits) added to both `errors in
  1920.txt` and `permitted words.txt`. Also added a footnote-text entry
  for 10t's "III Néfi 9" — a full-document grep found this is the only
  accented "Néfi" anywhere in either master file (vs. 2482 unaccented
  instances combined), an isolated print anomaly with no 1886 footnote
  text to compare against. Footnote-anchor check (max 3612, zero
  duplicates/out-of-range, only the pre-existing 812 gap), curly-quote
  scan, and `check_spaced_punctuation.py`/`check_footnote_punctuation.py`
  (whole document) all clean. One narrow-space item flagged for the
  editor per `feedback_narrow_space_vs_merge`, not resolved unilaterally:
  v.12 "más justa" (a real but narrow gap, transcribed as two words per
  the current default).
- **2026-07-25c**: Discovered page 507 was already fully transcribed
  through Session E on disk (Sessions A–E complete, per its own
  Corrections log, and already integrated into `librodm.txt`/
  `librodm_foot.txt` through footnote 3621 — Block 1 and Block 2 both
  present), but this progress log was never updated after it finished,
  so it still read "Next page: 507." Same stale-log pattern as
  2026-07-20c (pages 480/481).
- **2026-07-25d**: Sessions A–E run for page 508 (III Nefi 11:8(continues)-21,
  footnotes 3622-3637, letters h-w). Session A: mandatory 1879 check for
  letters i and l confirmed via BOM 1879 Pratt file page 510 (chapter_map
  lists III Nefi ch.11 at 1879 file 509, but that page's content actually
  matches 1920 page 507 — content lands one page later, at 510, with no
  further drift) — all 16 letters h-w matched 1879 letter-for-letter and
  citation-for-citation, including confirming two surprising-looking
  details as genuine: footnote l's citation has a comma (not a period)
  after the target letter ("Véase b, I Nefi 12."), and footnotes n and r
  both genuinely cite the identical target ("Véase 2b, Mosíah 7."). One
  hyphenated line-break rejoin (v.15 "convencién-/dose" → "convenciéndose"),
  two rule-8 marker-overflow cascades (v.11 "en lo que"; the v.15/16
  boundary, "venir." cascading onto v.16's own line and dropping that
  line's usual 4-space verse-initial indent, matching the page 506
  precedent). Two floating scan-artifact marks (not transcribed) and a
  Google-text cross-check (3 candidates, all dismissed as OCR noise/
  confirmed-correct accent) rounded out Session A. Session B independently
  reconfirmed everything from fresh crops. Session C/D integrated cleanly
  via the scripts, all 16 Block 2 cross-references resolved correctly to
  their book sections (Mosíah for h/n/o/r/u, I Nefi for l), confirmed via
  a section-header lookup rather than just trusting the script output.
  Session E: fresh pptext regeneration (`report_wsl_20260725b.html`) came
  back clean for spellcheck/edit-distance/footnote-anchor/dash/curly-quote/
  spaced-punctuation/hyphen-compound checks — only the pre-existing
  "Profecia" item and pre-existing 812 footnote gap remain, both unrelated
  to this page. One new genuine 1920-only error found via the "full stop
  followed by unexpected sequence" check: III Nefi 11:8 "en medio. de
  ellos." — confirmed against 1886 (file page 522, book page 504), which
  reads the clause continuously with no punctuation between "medio" and
  "de"; added to `errors in 1920.txt` (no `permitted words.txt` entry,
  punctuation not spelling).
- **2026-07-25e, user correction**: mid-Session-A on page 509, the user
  spotted that page 508 had 4-space-indented verse-number lines (e.g.
  "    9. Y aconteció...") that didn't match the flush-left convention
  of every other recent page. Investigation found this was a recurrence,
  not a new defect: the identical thing happened once before on page 493
  (noted informally back on 2026-07-22g), but that "fix" only changed how
  later pages were transcribed going forward — page 493 itself, and its
  already-integrated copy in `librodm.txt`, were left unfixed, and the
  lesson was never converted into an actual rule or a mechanical check,
  so nothing stopped it from recurring. A full scan turned up the defect
  on 8 pages total, not just 493/508: 453, 454, 489, 490, 491, 492, 493,
  508 (66 body-text instances). All 8 page files, `librodm.txt` (77
  lines), and the two already-emailed chapter files affected
  (`chapters_emailed/Helaman_6.txt`, `Helaman_7.txt` — Helamán 6-7 had
  already been sent to family; emails were not resent, but the archive
  copy was corrected for consistency, matching the 2026-07-24b precedent)
  were all fixed via a script that preserved each file's existing line
  ending (LF for pages/librodm.txt, CRLF for the chapters_emailed files —
  see the 2026-07-24b lesson on this) and deliberately stopped at each
  page file's `Corrections` header, since a wrapped Corrections-log
  prose paragraph can incidentally start a line with a quoted "NN. ..."
  excerpt that must NOT be touched (found one such false positive on
  page 508 itself, left alone). Added a permanent rule to
  `libro_de_mormon_rules.md` Section 1 (under rule 4) and a new
  mechanical backstop, `check_verse_indent.py`, wired into
  `transcribe-page` step 9 and `orthography-check`'s document-wide
  sweep, matching how `check_spaced_punctuation.py`/
  `check_footnote_punctuation.py` are wired in — the same pattern used
  to close the 2026-07-24 space-before-punctuation gap. **Lesson**: an
  informal progress-log note describing a one-off fix is not durable;
  a defect only reliably stops recurring once it's both (a) fixed at
  every existing occurrence, not just going forward, and (b) written
  into `libro_de_mormon_rules.md` and/or backed by a mechanical script,
  not left as institutional memory in CLAUDE.md alone.
- **2026-07-25f**: Sessions A–E run for page 509 (III Nefi 11:22-34
  chapter close, footnotes 3638-3651, letters x-z then two-letter codes
  2a-2k). Session A: the footnote block's first three letters, read
  individually off the 1920 image, appeared to be "z, v, t" in that
  order — a direct violation of rule 13's strict alphabetical ordering,
  and the same swash-font ambiguity documented on page 451 for
  s/t/v/x/y/z (this chapter's footnote-reference font is heavily
  stylized cursive). Cross-checked against BOM 1879 Pratt file page 511
  (chapter_map lists III Nefi ch.11 1879 file as 509, but content lands
  two pages later — one more page of drift than page 508's already-
  established "one page later" pattern, since this is denser 1920
  content spread across more running text): 1879's own u/v/w (already
  confirmed on page 508) are immediately followed by x/y/z, and the y/z
  entries matched this page's second/third entries almost word-for-word
  — reassigned the three glyphs from z/v/t to x/y/z accordingly; both
  1920 markers that had first looked like plain "z" (before "poder" and
  before "pararéis") are in fact two different letters (x and z) that
  only look alike in this font. Session B independently re-ran the
  check from a fresh crop and reconfirmed it exactly, plus re-verified
  all 14 Block 1 entries and body markers. Two hyphenated line-break
  rejoins (v.23 "des-/cenderéis," and the same verse's "bau-/tizaréis"
  once absorbed into "pararéis en ella... bautizaréis.") and one more
  (v.26 "cora-/zones" → "corazones"). Session C/D integrated cleanly,
  all 14 Block 2 cross-references resolved with no unresolved targets
  (spot-checked 11-2d → III Nefi 9's own letter p = 3576, confirmed
  book-aware). Session E: fresh pptext regeneration
  (`report_wsl_20260725c.html`) flagged 4 spellcheck/edit-distance
  suspects. Confirmed 2 new genuine 1920-only errors against 1886 (file
  pages 523-524, book pages 505-506): v.31 "decalraré" (→ declararé,
  letter-transposition typo) and v.32 "triago" (→ traigo, same
  pattern) — both added to `errors in 1920.txt` and `permitted
  words.txt`; RAE has no entry for either 1920 form and the reference
  corpora have zero hits for either. Confirmed 2 legitimate archaic
  forms matching 1886 exactly, added to `permitted words.txt` only:
  v.25 "Habiéndoseme" and v.28 "ántes" (accented — a genuine period
  spelling variant despite being the only accented instance in the
  whole document; 73 unrelated unaccented "antes" instances elsewhere
  don't contradict this). Full-document footnote-anchor check (max
  3651, zero duplicates/out-of-range, only the pre-existing 812 gap),
  curly-quote scan, and all three mechanical checker scripts
  (`check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py`, whole document) all clean.
- **2026-07-25f**: Sessions A–E run for page 510 (III Nefi 11:35-41
  chapter close, III Nefi 12:1 chapter open, footnotes 3652-3666,
  letters 2l-2u then chapter 12 restarts at a-e). Session A: mandatory
  1879 check (BOM 1879 Pratt file page 512, chapter_map III Nefi ch.12
  — content landed on the exact listed page, no drift) resolved several
  footnote target letters that were ambiguous or misread at first
  glance in this page's heavily swash reference font: 11-2p's target
  (candidate "2i", i is mandatory) turned out to have a hooked
  descender on closer zoom and is actually "2j", confirmed by 1879's
  "see 2j"; 11-2s's target was misread as plain "b" at low zoom but is
  actually the two-letter code "2b", confirmed by 1879 exactly; 11-2o
  and 12e (both citing "III Nefi 9") looked like plain "v" at every
  zoom tried with no visible descender, but 1879 reads both as "y" —
  settled decisively via content-fit, since 1920's own chapter 9
  footnote y (3585) already cites "III Nefi 11:35,36" and "12:1,2", the
  exact verses these two footnotes annotate; 12a's target was an
  illegible over-inked blob, resolved via 1879 ("see s") as the one
  target on the page where 1879's own letter position (a) also matches
  1920's, the strongest-confirmed call on the page. Also found and
  transcribed-as-printed a genuine 1920-only chapter-heading defect:
  1920 prints "CAPTULO 12." instead of "CAPÍTULO 12." (the "Í" is
  entirely missing, confirmed at 8x-16x zoom), unlike every other
  chapter heading in the document. Four hyphenated line-break rejoins
  (rule 7): "peque-/ñito", "pala-/bras", "es-/cogido", "bendi-/tos".
  Session B independently re-verified all 15 Block 1 entries and
  re-ran all four ambiguous-letter resolutions from fresh crops,
  reconfirming each exactly. Session C/D integrated cleanly
  (`insert_body_text.py 510`, `generate_block2.py 510`); all 16 Block 2
  cross-references resolved with no unresolved targets, and two of the
  resolutions independently corroborated Session A/B's trickiest calls
  (12a→s resolved to 3633, the exact 1879-confirmed III Nefi 1 target;
  11-2s→2b resolved to "III Nefi 11:37,38" — the literal "become as a
  little child" passage this page's own v.37-38 paraphrases). Session
  E: fresh pptext regeneration (`report_wsl_20260725e.html`) flagged
  only one new spellcheck suspect, "CAPTULO" itself (added to
  `permitted words.txt`); confirmed two more genuine 1920-only errors
  against 1886 (file pages 524-525, chapter_map III Nefi ch.11/12) from
  this page's own Corrections log: v.38 "no en podréis heredar" (1886
  has no "en" at all, and this page's own v.37 uses the correct
  parallel construction), and the "CAPTULO 12." heading itself; both
  added to `errors in 1920.txt`. A third suspected item, chapter 12
  v.1's "palabras. de estos doce" (a small mark initially transcribed
  as a spurious period), was reversed the same day after the editor
  reviewed the actual 1920 page directly and determined the mark is a
  tiny scan speck, not printed type — corrected to "palabras de estos
  doce" in `page_510.txt` and `librodm.txt`, and the corresponding
  `errors in 1920.txt` entry was removed. This matches the established
  scan-artifact pattern from pages 472-473/475/483/488/500 (see the
  2026-07-18d entry): physical-looking damage isn't automatically a
  genuine 1920 error, and the editor's direct look overrides an
  image-crop reading. Full-document footnote-anchor check (max 3666): zero
  duplicates, zero out-of-range, only the pre-existing 812 gap.
  `check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py` (whole document) and curly-quote scan all
  clean; page has no hyphens post-rejoin, so no dash-check findings.
  Two narrow-space-vs-merge notes (v.35 "testimonio desde", chapter 12
  v.1 "que os bauticen") left open for the editor's own look, per
  `feedback_narrow_space_vs_merge`.
- **2026-07-25g**: Sessions A–E run for page 511 (III Nefi 12:2-18,
  footnotes 3667-3674, letters f-m). Session A: mandatory 1879 check
  for this page's own letters i and l confirmed via BOM 1879 Pratt
  file page 513 (note: the PNG filename does not match the book's own
  printed page number in this range — file page_0513.png prints page
  "505," not page_0505.png, which turned out to hold unrelated III
  Nefi 6-8 content; the printed page number in the image itself, not
  the filename, is authoritative) — 1879's own h-l sequence ("h, Math.
  5:3. i, Math. 5:6. j, Math. 5:10. k, Math. 5:12. l, Math. 5:13.")
  matched letter-for-letter and citation-for-citation. Footnote 12g's
  target letter was initially read as "v" from the 1920 zoom (a clean
  two-stroke shape with no visible descender at this print size), but
  both 1879 ("g, see y, III. Nep. 9.") and content-fit overrode this:
  III Nefi 9's own letter y (3585) sits at "le bautizaré con fuego y
  el Espíritu Santo" (9:20), an exact thematic match for this page's
  v.2, whereas the "v" reading (3582, "en mí se ha cumplido la ley de
  Moisés") had no such fit; page 510 already cites this same "y, III
  Nefi 9" target twice (11-2o, 12e), further confirming y over v.
  Resolved as Véase y, III Nefi 9 (target 3585) — independently
  reconfirmed in Session B from a fresh 1879 crop. One rule 7 hyphen
  rejoin (v.9 "llama-/dos" → "llamados"). Verse-initial lines
  transcribed flush left per the 2026-07-25e standing convention.
  Session C/D integrated cleanly, all 8 Block 2 cross-references
  resolved automatically with no unresolved targets (12f→378, II Nefi
  9's own u; 12g→3585, confirming the Session A/B letter-y resolution).
  Session E: fresh pptext regeneration (`report_wsl_20260725.html`)
  came back clean for the new range — zero new spellcheck suspects
  (the only hit anywhere is the pre-existing, unrelated "Profecia"),
  zero edit-distance hits, footnote-anchor check (max 3674, zero
  duplicates/out-of-range, only the pre-existing 812 gap) clean,
  scanno/curly-quote checks clean, dash check clean (no hyphens in
  this page's body post-rejoin), book-level/Jeebies clean, and
  `check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py` all clean document-wide. One genuine 1920-
  only error confirmed and added to `errors in 1920.txt`: III Nefi
  12:3 "podres" for "pobres" ("poor in spirit," matching footnote
  12h's Mateo 5:3 citation) — 1886 reads "pobres" at this exact spot,
  RAE has no adjectival plural "podres" (only the unrelated singular
  noun "podre," pus/putrefaction), zero corpus hits for "podres" vs.
  98 for "pobres," and the modern Spanish edition (3 Nefi 12:3) also
  reads "pobres"; not pptext-flagged this run (known brand-new-single-
  occurrence quirk), so no `permitted words.txt` entry needed.
- **Next page**: 512 (file page 534), full A–E cycle, first footnote 3675.
- **Completed pages**: 437–511, Sessions A–E fully done through page 511.

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
