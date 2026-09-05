# Libro de Mormón 1920 — Session Log

Full, append-only history of every transcription session (Sessions A–E,
user corrections, tooling changes, etc.), one dated entry per session.
This file was split out of `CLAUDE.md`'s old `## Current Progress`
section on 2026-07-28 because it had grown to ~183k characters (95% of
the file) and pushed CLAUDE.md over the 150k-character limit.

**CLAUDE.md now only carries the single most recent entry** (a
snapshot of the current state), plus the `Next page` / `Completed
pages` pointers. Every session's full write-up belongs here.

**Going forward**: when a session finishes and CLAUDE.md's `##
Current Progress` section would normally get a new dated entry,
instead:
1. Append the new entry to the end of this file (after the last
   existing entry), in the same dated-bullet format as below.
2. In `CLAUDE.md`, replace the single existing entry in `##
   Current Progress` with this new entry (plus updated `Next page`
   and `Completed pages` lines) — CLAUDE.md never accumulates more
   than one session entry at a time.

---

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
- **2026-07-25g**: Sessions A–E run for page 513 (III Nefi 12:33-48
  chapter close, III Nefi 13:1-2 chapter open, footnotes 3684-3687,
  letters w-y then chapter 13 restarts at a). Discovered the CLAUDE.md
  "Next page: 512" note was stale in the other direction from the
  2026-07-20c/2026-07-25c pattern: page 512 itself was already fully
  transcribed through Session E (footnotes 3675-3683 already used, per
  its own Corrections log), so page 513's true starting footnote was
  3684, not the "first footnote 3675" the note implied — corrected
  before Session A began. Session A: none of this page's own
  chapter-12-tail letters (w, x, y) or chapter 13's first letter (a)
  are i/l/1, but the reference font is the same heavily stylized
  cursive seen on pages 509/510, and two of the three tail letters (x,
  y) looked like plain "z"/"v" at every zoom tried with no clearly
  visible distinguishing stroke — resolved via alphabetical-sequence
  inference (must continue from page 512's last letter, v, with no
  gaps) plus strong content-fit for each, then independently confirmed
  letter-for-letter and citation-for-citation via BOM 1879 Pratt file
  515 ("w, see o. x, III. Nep. 15:2,3. y, Math. 5:48. III. Nep.
  19:25-29. 27:27.") and file 516 ("a, see u, Alma 16."). Four rule-7
  hyphenated line-break rejoins (cumplirás, quienquiera, prójimo,
  sinagogas), all fitting under the 72-char cap with no rule-8
  rebalancing. Two suspected-misprint spots resolved as physical
  print/scan artifacts rather than genuine 1920 errors, both confirmed
  against 1886 (file page 527, book page 509): v.34 "por'el" (a raised
  stray ink mark sitting in the word-gap instead of a plain space,
  matching the established floating-mark precedent) and v.39
  "hiriere" (the printed "e" replaced by a solid over-inked blob with
  no discernible letter shape — the opposite defect from the
  "giandes"-style under-inked/dotless-stroke precedent). Neither
  needed an `errors in 1920.txt` entry (physical marks, not legible
  misprints). Session B independently re-verified all 4 Block 1
  entries and body markers from fresh crops, and re-ran the
  swash-letter check from fresh 1879 crops of both file pages 515 and
  516 — both reconfirmed exactly. Session C/D integrated cleanly
  (`insert_body_text.py 513`, `generate_block2.py 513`), both
  cross-references resolved with no unresolved targets (w's "Véase o."
  resolved to chapter 12's own o = 3676, confirming the content-fit
  self-citation reasoning; chapter 13's "a" resolved to Alma 16's own
  u = 2046). Session E: fresh pptext regeneration
  (`report_wsl_20260725f.html`) came back fully clean for this page's
  range — no new Spellcheck Suspect Words or Edit Distance hits,
  footnote-anchor check (1-3687, zero duplicates/out-of-range, only
  the pre-existing 812 gap) clean, scanno/curly-quote checks clean,
  the "spaced punctuation" section is absent from the report entirely
  (zero findings document-wide), dash check has no hyphens in this
  page's range (all four rejoins removed the only candidates),
  special-situations/paragraph-level checks and Jeebies all clean.
  Both of this page's suspected-artifact Corrections items were
  already settled against 1886 at transcription time; no `errors in
  1920.txt` or `permitted words.txt` entries needed anywhere on this
  page.
- **2026-07-25h**: Sessions A–E run for page 514 (III Nefi 13:3-22,
  footnote 3688, letter b). Session A: no chapter heading (continues
  chapter 13 from page 513); neither this page's own letter (b) nor
  its cross-reference target letter (t) is i/l/1, so no mandatory 1879
  check applied. Two suspected misprints preserved as printed per rule
  32: v.12 "libranos" (missing accent, expected "líbranos") and v.21
  "alli" (missing accent, expected "allí") — both later confirmed as
  genuine 1920-only errors. Two scan-artifact calls (v.7 "mucha"
  obscured by an ink blob rendering as "muqha"; a stray floating ink
  speck near v.12's "tentación,"), both matching the established
  floating/over-inked-mark precedent. `check_line_wrap.py` flagged a
  line-count gap explained by this page's unusually high count of
  short verse-final lines (Amén., ni roban., etc.), confirmed
  line-by-line against the image. Google-text cross-check flagged one
  candidate near v.18/19 (an extra "."), confirmed as another stray
  ink speck, not printed type. Session B independently reconfirmed the
  single Block 1 entry and body marker placement; no errors found.
  Session C/D integrated cleanly (`insert_body_text.py 514`,
  `generate_block2.py 514`), the one cross-reference (13b → Mosíah 27
  own letter t) resolved correctly and book-aware (1559, confirmed via
  book-header lookup). Session E: fresh pptext regeneration
  (`report_wsl_20260725g.html`) flagged "libranos" and "alli" as
  spellcheck suspects — both confirmed as genuine 1920-only errors via
  1886 (book page 511/file 529), RAE (both words' only DLE headword is
  the accented form), and the modern Spanish edition (3 Nefi 13:12,
  13:21, both accented) — added to `errors in 1920.txt` and `permitted
  words.txt`. Three archaic imperative+enclitic forms also flagged
  (laváos, amontonáos, ungíos) confirmed legitimate against 1886
  exactly (matching the established apoderáos/entregáos/salváos/uníos
  pattern) — added to `permitted words.txt` only. Full-document
  footnote-anchor check (max 3688, zero duplicates/out-of-range, only
  the pre-existing 812 gap), `check_spaced_punctuation.py`/
  `check_footnote_punctuation.py`/`check_verse_indent.py` (whole
  document), curly-quote scan, dash check (page has no hyphens at
  all), special-situations/paragraph-level checks, book-level checks,
  and Jeebies all clean for this page's range. Corrections-log sweep
  found nothing left unresolved. Separately noted: `chapter_map.csv`
  has a genuine gap — every III Nefi chapter (1-30) is entirely
  missing from the table (confirmed by row-count: exactly 30 rows
  missing between Helamán 16 and 4 Nephi 1), so 1886/1879 page lookups
  for this book have to be done by direct estimation/navigation
  instead of the normal `grep chapter_map.csv` shortcut — worth
  backfilling next time the table itself is touched.
- **2026-07-25i**: Sessions A–E run for page 515 (III Nefi 13:23-34
  chapter close, III Nefi 14:1-2 chapter open, footnote 3689, letter c).
  Session A: only one footnote, letter c (chapter 13's continuing
  lettering), a direct citation ("Mateo 6:25", not a "Véase"
  cross-reference) — not i/l/1, so no mandatory 1879 check applied.
  Chapter 14's own subtitle "(Véase Mateo 7.)" transcribed per the
  chapter-subtitle rule. v.26 "del aire" prints with a genuine
  zero-width gap ("delaire"), but per the 2026-07-22 rule-6 default
  (grammar requires two words) it was transcribed as "del aire", later
  confirmed against 1886 (also two words). Twelve space-before-
  semicolon/colon/exclamation instances normalized per rule 31 — this
  page had an unusually high concentration, on par with the pre-2026-
  07-24 pages. Two suspected misprints preserved as printed per rule
  32: v.24 "Dics" (for "Dios") and chapter 14 v.2 "còn"/"què" (for
  "con"/"que", both printed with a genuine grave accent — a mark
  otherwise unattested anywhere in this document, which only uses
  acute á/é/í/ó/ú). Session B independently reconfirmed the single
  Block 1 entry and marker placement; no errors found. Session C/D
  integrated cleanly via the scripts, but surfaced a real bug: the
  page file used a "Block 1:" label line (deviating from the
  established no-label convention on pages 511-514), which caused
  `insert_body_text.py`'s body/footnote split to swallow that label
  line into the body text, landing it in `librodm.txt` right before
  `Notas` (`librodm_foot.txt` was unaffected). Fixed by removing the
  label from both files and re-running pptext. Session E: fresh
  pptext regeneration (`report_wsl_20260725i.html`) flagged 5
  spellcheck suspects. "alfolíes" (v.26) confirmed legitimate — matches
  1886 exactly and RAE DLE has a full entry for "alfolí" (granary/salt
  warehouse); added to `permitted words.txt` only. "Dics", "còn", and
  "què" all initially confirmed as genuine 1920-only errors against
  1886 (book pages 511-512, file 529-530 — III Nefi still has no
  `chapter_map.csv` entries, so these were located by direct navigation
  from page 514's already-established file 529, per the CLAUDE.md-
  documented gap); all three added to `errors in 1920.txt` and
  `permitted words.txt`. Full-document footnote-anchor check (max
  3689, zero duplicates/out-of-range, only the pre-existing 812 gap),
  `check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py` (whole document), and an independent
  curly-quote scan all clean. No hyphens on this page, so no
  dash-check findings.
- **2026-07-25j, user correction**: user reviewed the 1920 page image
  themselves for v.24's "Dics" and determined it's a poor-inking
  artifact on the lower-right of the "o" (the intended word is "Dios"),
  not a genuine 1920 typesetting error — matching the established
  scan/print-artifact pattern (2026-07-18d and others: "giandes" page
  488, "c amó" page 482) where physical-looking damage isn't
  automatically a genuine substitution. The `errors in 1920.txt` entry
  was removed (not just edited) and `pages/page_515.txt`/`librodm.txt`
  corrected to read "Dios"; the `permitted words.txt` entry for "Dics"
  was also removed since the form no longer appears anywhere in the
  text. "còn" and "què" are unaffected — those remain confirmed 1920
  errors (a genuine grave-accent typesetting defect, not an inking
  question). [**Superseded 2026-07-26j**: this "còn"/"què" call was
  later found to be wrong too — see that entry below; both are stray
  specks, not accents, and the corresponding log entries were removed.]
- **2026-07-25k**: Sessions A–E run for page 516 (III Nefi 14:3-23
  chapter close, footnotes 3690-3691, letters a-b; continues chapter 14,
  opened on page 515). Session A: neither letter (a, b) nor footnote b's
  cross-reference target letter (a, in "Véase a, II Nefi 9") is i/l/1,
  so no mandatory 1879 check applied; both glyphs confirmed unambiguous
  at zoom. One rule-8 marker-caused overflow (inserting [3690] before
  "Pedid" pushed that line to 73 chars; moved "abrirá;" to the start of
  the next line, which begins "8. Puesque..."). A v.4 "t u ojo"
  justification-widened intra-word gap was closed to the normal word
  "tu" (not an inter-word gap, but the same spacing-normalization
  principle). Two suspected-misprint calls: v.22 "no. hemos" (a genuine
  period mid-question, preserved as printed) and v.23 "mí,." (a stray
  ink speck after the comma, matching the established floating-mark
  precedent, not transcribed). v.9's unaccented "a quién" matches the
  already-established recurring accentuation inconsistency (2026-07-22c/
  page 490), not logged as new. Session B independently re-verified
  both Block 1 entries and both body markers from fresh crops; no
  errors found. Session C/D integrated cleanly except one Block 2
  cross-reference `generate_block2.py` couldn't parse (a "Véase
  [letter], Book Chapter; [direct citation]" mixed form) — resolved by
  hand: II Nefi 9's own letter a (`librodm_foot.txt` line 421) gives
  sequential number 358, so 3691 reads "Véase 358; III Nefi 27:33."
  Session E: fresh pptext regeneration (`report_wsl_20260725j.html`)
  flagged one new spellcheck suspect, "Cógense" (v.16) — confirmed
  legitimate (matches 1886 exactly, RAE confirms "coger" as a standard
  verb in this archaic enclitic word order, modern edition uses the
  same root verb); added to `permitted words.txt` only. The "full stop
  followed by unexpected sequence" check confirmed v.22's "no. hemos"
  as a genuine 1920-only error against 1886 (same page, no punctuation
  at all between "no" and "hémos"); added to `errors in 1920.txt`. v.23's
  stray dot was independently confirmed as a scan artifact via the same
  1886 page. Full-document footnote-anchor check (max 3691, zero
  duplicates/out-of-range, only the pre-existing 812 gap), `check_spaced_
  punctuation.py`/`check_footnote_punctuation.py`/`check_verse_indent.py`
  (whole document), and an independent curly-quote scan all clean. No
  hyphens remain in this page's body text, so no dash-check findings.
- **2026-07-25l, user correction**: user reviewed a zoomed crop of page
  516 v.22's "no. hemos" directly and judged the mark between the two
  words to be a stray scan artifact, not genuine type — notably smaller
  and lower than the page's real periods. Checked the 1920 PDF's own
  embedded/OCR text layer (`google_text_1920/page_0538.txt`), which
  reads a plain space at that exact spot with no character at all,
  corroborating the artifact call (the same signal the
  `check_google_crosscheck.py` diff had already surfaced during Session
  A but which wasn't enough on its own to override the 1886-comparison-
  based errors-log entry at the time). Reversed: `pages/page_516.txt`
  and `librodm.txt` corrected to read "no hemos" (no punctuation); the
  `errors in 1920.txt` entry for III Nefi 14:22 was removed (no
  `permitted words.txt` entry existed for it, since it was a punctuation
  question, not spelling). Matches the established scan-artifact
  pattern (pages 472-473, 475, 483, 488, 500, 510, 515) — a mark that
  looks like clean printed type in a 1886-confirmed "error" can still
  turn out to be physical scan damage on direct inspection, and the
  editor's own look at the image overrides an image-crop-based call.
- **2026-07-26**: Session E run for page 517 (III Nefi 14:24-27 chapter
  close, III Nefi 15:1-7 chapter open, footnotes 3692-3701). Fresh
  pptext regeneration (`report_wsl_20260726.html`) flagged
  "compararéle" (v.24, legitimate archaic future+enclitic form,
  confirmed against 1886 — added to `permitted words.txt` only) and
  "exhaltado" (v.1 ch.15, already a Corrections-log suspect — confirmed
  against 1886 and the modern Spanish edition as a genuine "h"-inserted
  misprint for "exaltado" — added to both `errors in 1920.txt` and
  `permitted words.txt`). The mandatory Corrections-log sweep confirmed
  v.25's "cayo" (no accent) as genuine via 1886/modern edition (both
  "cayó") — added to `errors in 1920.txt` only, since "cayo" is itself
  a valid Spanish word (a reef/key) that aspell won't flag. Session E's
  own reading against 1886/the modern edition found three more genuine
  errors invisible to pptext (all valid dictionary words in the wrong
  grammatical form): v.1 (ch.15) "he...enseñada" for "enseñado" (RAE:
  the participle after "haber" is always invariable, "-o" ending,
  regardless of gender), v.2 (ch.15) "habían algunos" for singular
  "había algunos" (impersonal "haber" is always singular per RAE), and
  v.4 (ch.15) "se ha cumplida" for "cumplido" (same invariable-
  participle rule as "enseñada" — this page's own v.5-7 all correctly
  use "cumplido"). All three confirmed independently via both 1886 and
  the modern Spanish edition and added to `errors in 1920.txt`, no
  `permitted words.txt` entries needed. Full-document footnote-anchor
  check (max 3701, zero duplicates/out-of-range, only the pre-existing
  812 gap), `check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py` (whole document), and an independent
  curly-quote scan all clean; full pptext walkthrough (dash, scanno,
  special situations, book/paragraph-level, Jeebies) clean for this
  page's range. Page 517 now has Sessions A-E complete.
- **2026-07-26b**: Sessions A–E run for page 518 (III Nefi 15:8-23,
  footnotes 3702-3712, letters j-t continuing chapter 15's lettering
  from page 517). Session A: mandatory 1879 check for letter l (v.9
  "luz," chapter 15's own continuing lettering) confirmed via BOM 1879
  Pratt file page 520 ("l, see m, Mos. 16.") — at low zoom the 1920
  print's chapter number looked like "Mosíah :6" (a faint "1"
  resembling a colon), resolved as chapter 16 via 1879 plus a tighter
  re-zoom. Footnotes j and k's cross-reference targets were illegible
  over-inked-blob glyphs in 1920 (same font defect as page 517's 14c/
  15c) — resolved via BOM 1879 Pratt file page 519 to target letters e
  (I Nefi 15) and o (II Nefi 25) respectively; neither is i/l/1, so
  discretionary. Footnote o's own cross-reference chapter number ("Véase
  k, I Nefi 18") was crisp and unambiguous in the 1920 print but
  genuinely illegible in the parallel 1879 entry even at high zoom —
  settled via content-fit: I Nefi 18 (the ocean-voyage/arrival chapter)
  and I Nefi 18's own letter k (sequential 165) cites a landing-site
  footnote ("Se cree que fué en la costa de Chili"), an exact thematic
  match for this footnote's "Norte y Sur América" citation. v.18
  "obstinación é incredulidad" prints with a true zero-width gap
  ("obstinaciôné"); per the rule 6 default, transcribed as two words,
  confirmed via both BOM 1879 Pratt ("stiffneckedness and unbelief")
  and 1886 (book page 515/file 533, also two words) — not an error.
  Session B independently re-verified all 11 Block 1 entries and body
  markers from fresh crops, re-ran the mandatory letter-l check from a
  fresh 1879 crop (reconfirmed exactly), and re-examined the I Nefi 18
  digit at a fresh, tighter 1879 zoom — confirmed it's genuinely
  ambiguous there (a real print-quality limit, not an under-zoomed
  read), so the 1920-print-based "18" resolution stands. Session C/D
  integrated cleanly via the scripts; `generate_block2.py` resolved 9
  of 11 cross-references automatically (one, "Véase II Nefi 31," is a
  whole-chapter citation with no letter, correctly left unresolved by
  design, matching the existing "Véase Éther 1" precedent), and one
  ("Norte y Sur América; Véase k, I Nefi 18; III Nefi 15:13" — the
  known mixed direct-text-plus-Véase citation format the script can't
  auto-parse) was resolved by hand to "Véase 165". Session E: fresh
  pptext regeneration (`report_wsl_20260726b.html`) came back fully
  clean for this page's range — the sole document-wide spellcheck hit
  remains the pre-existing, unrelated "Profecia" (page 469).
  Footnote-anchor check (merging pptext's two buckets) confirmed
  3702-3712 fully and uniquely covered, zero duplicates/gaps beyond the
  pre-existing 812 gap. Mandatory Corrections-log sweep confirmed one
  new genuine 1920-only error against 1886 (book page 515/file 533):
  III Nefi 15:19 "no saben de no vosotros" (doubled "no," should be
  singular negation), matching BOM 1879 Pratt's "that they know not of
  you" already noted in Session A; added to `errors in 1920.txt` (no
  `permitted words.txt` entry — a grammatical duplication, not a
  spelling matter). `check_spaced_punctuation.py`,
  `check_footnote_punctuation.py`, and `check_verse_indent.py` all
  clean document-wide.
- **2026-07-26c**: Sessions A–E run for page 519 (III Nefi 15:22-24
  chapter close, III Nefi 16:1-8, footnotes 3713-3726, letters 15u-v
  then chapter 16 restarts a-l). Session A: chapter 15's tail letters
  u and v resolved via glyph shape plus content-fit and 1879
  confirmation (BOM 1879 Pratt file page 521, chapter_map III Nefi
  ch.15/16, exact page match, no drift — "v, vers. 17, 21." confirms
  v; u's own citation continues the same Acts passage begun by page
  518's t). A stray raised mark before chapter 16 v.4's "Y mándoos"
  was initially miscounted as a 13th footnote letter — cross-checking
  against 1879 (no footnote there either) and the block's own count
  (exactly 12 lettered entries, a-l) resolved it as a print/ink
  artifact, not a footnote, matching the established floating-mark
  precedent; this also fixed a resulting one-off mis-mapping of every
  marker from d onward. Mandatory 1879 check (letters i and l, this
  page's own chapter 16 lettering) confirmed via the same 1879 page;
  in the process, footnote h's cross-reference target (initially
  misread as "i" from a lower-zoom crop, which mattered since target
  letter i is mandatory) was corrected to "j" after a tighter crop
  showed a descender inconsistent with "i" and 1879 confirmed "h, see
  j, III. Nep. 15." — exactly the failure mode the mandatory i/l/1
  check exists to catch. One rule-8 marker-overflow cascade (v.6/v.7
  boundary, moving "Padre." to the start of v.7's own line). Session
  B independently reconfirmed everything from fresh crops, including
  re-running the mandatory 1879 check; no errors found. Session C/D
  integrated cleanly (`insert_body_text.py 519`, `generate_block2.py
  519`), all 14 Block 2 cross-references resolved automatically with
  no unresolved targets (spot-checked 16h→3702, III Nefi 15's own j,
  confirming the h-target correction). Session E: fresh pptext
  regeneration (`report_wsl_20260726c.html`) confirmed 2 genuine
  1920-only errors against 1886 (book page 516/file 534), RAE, and the
  reference corpora: v.2 "quiónes" (→ quiénes, wrong accented vowel)
  and v.4/v.7 "plentitud" (→ plenitud, extra "n", same misspelling
  twice on one page); both added to `errors in 1920.txt` and
  `permitted words.txt`. Full-document footnote-anchor check (max
  3726, zero duplicates/out-of-range, only the pre-existing 812 gap),
  curly-quote scan, and `check_spaced_punctuation.py`/
  `check_footnote_punctuation.py`/`check_verse_indent.py` all clean.
  Page has no hyphens at all, so no dash-check findings.
- **2026-07-26d**: Sessions A–E run for page 520 (III Nefi 16:8(continues)-17,
  footnotes 3727-3739, letters m-z, letter t entirely absent). Session A/B:
  mandatory 1879 check for footnote m and v's target letters (both initially
  read as "i" from the 1920 image but showing a hooked descender at closer
  zoom) confirmed via BOM 1879 Pratt file page 522 (chapter_map III Nefi
  ch.16, exact page match, no drift) as genuine "j": "m, see j, II. Nep.
  26." and "v, see j, III. Nep. 15."; footnotes q and r's targets
  independently confirmed as genuine "i" ("q, see i, II. Nep. 28.", "r, see
  i, II. Nep. 10."). Discovered and documented a genuine 1920-only
  structural anomaly: footnote letter "t" is entirely missing from this
  page -- no body-text marker anywhere near v.10's "que yo sacaré" (the
  position it should occupy) and no footnote-block entry between "s, Véase
  n." and "u, A los Lamanitas..." -- while 1879 (same file page) does carry
  a "t" entry ("fulfilled, when the Saints left the States and came to
  Utah."), confirming 1920 dropped an entire footnote, not just a citation.
  Three rule-7 hyphen rejoins (escarne-/cidos, ase-/sinatos, cono-/
  cimiento) with rule-8 marker-overflow cascades, one of which propagated
  through three lines before resettling under the 72-char cap. Session
  C/D integrated cleanly (`insert_body_text.py 520`, `generate_block2.py
  520`), all 13 Block 2 cross-references resolved automatically with no
  unresolved targets, each matching the content-fit reasoning from Session
  A/B (e.g. v's target resolved to III Nefi 15j = 3702, the gathering/
  covenant passage fitting v.12's "recordaré la alianza... oh casa de
  Israel"). Session E: fresh pptext regeneration (`report_wsl_20260726d.
  html`) confirmed all four of this page's Corrections-log suspects as
  genuine 1920-only errors against 1886 (book pages 516-517, file 534-535):
  v.8 "esta país" (gender-agreement misprint, 1886: "este pais") and
  "pistoteado" (1886: "pisoteado", spurious extra "t"; this page's own
  v.15 spells "pisoteada" correctly), and v.10 "sacredotales" (1886:
  "sacerdotales", transposed e/r) and a second "plentud" (1886:
  "plenitud"; distinct from page 519's separate "plentitud" misspelling)
  -- all four added to `errors in 1920.txt`, the three pptext-flagged
  ones (pistoteado, plentud, sacredotales) also mirrored into `permitted
  words.txt`. Also logged the missing-letter-t anomaly in `errors in
  1920.txt`, matching the established "falta la nota" style used for the
  pre-existing Jacob 2:15/footnote-812 gap. One more flagged word,
  "Siéndose" (footnote 16w's own text) was added to `permitted words.txt`
  only -- independent research found no other instance of "ser" taking a
  reflexive "se" anywhere in the document and no RAE/corpus attestation,
  but since it's footnote-only text (no 1886 comparison exists) and the
  meaning is unambiguous and matches 1879's parallel note, it was
  flagged for the editor's awareness rather than added to `errors in
  1920.txt` unilaterally. Full-document footnote-anchor check (max 3739,
  zero duplicates/out-of-range, only the pre-existing 812 gap),
  `check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py` (whole document), and an independent curly-quote
  scan all clean. Page has no hyphens post-rejoin, so no dash-check
  findings; the "full stop followed by unexpected sequence" paragraph-
  level check showed nothing new in this page's range.
- **2026-07-26e**: Sessions A–E run for page 521 (III Nefi 16:18-20
  chapter close, III Nefi 17:1-9 chapter open, footnotes 3740-3744,
  letters 16-2a then chapter 17 restarts a-d). Session A: none of this
  page's letters (2a, a, b, c, d) or the one cross-reference target
  (17b's "p") are i/l/1, so no mandatory 1879 check applied. Two rule-7
  hyphen rejoins (v.3 "en-/tendáis", v.7 "com-/pasión"). The Google-text
  cross-check tool only compared the first 8 lines (chapter 16's tail)
  before stopping at the blank line preceding "CAPÍTULO 17." -- the same
  known blind spot from page 505/2026-07-25a -- so the rest of the page
  was compared manually against `google_text_1920/page_0543.txt`
  directly; this caught a genuine misread (initial "vcsotros" corrected
  to "vcsotrcs", matching what's actually printed) that a first zoom had
  missed. A second, closely related glyph -- v.7's first "Traédmel_s" --
  was then independently found to show the same "o printed as a
  c-like shape" pattern at a tighter zoom, corrected from an initial
  "Traédmelos" read to "Traédmelcs" after Session C/D had already
  integrated the page, requiring a follow-up direct fix to `librodm.txt`
  to re-sync it (caught before Session E's pptext regeneration, via a
  fresh comparison against the page's own corrected Corrections log).
  Session B independently re-verified all 5 Block 1 entries and 5 body
  markers from fresh crops; footnote 17a's own glyph is a solid
  over-inked blob (matching the page 510 "12a" precedent), resolved as
  "a" via rule 13's strict chapter-restart sequencing rather than glyph
  shape. Session C/D integrated cleanly (`insert_body_text.py 521`,
  `generate_block2.py 521`); footnote 17b's "Véase p, III Nefi 15"
  resolved to 3708, and the resolution mutually confirmed itself since
  III Nefi 15p's own citation list already includes "III Nefi 17:4" --
  the very verse this footnote annotates. Session E: 1886 (book page
  518, file 536, chapter_map gap for III Nefi navigated by direct
  increment from pages 519-520's already-established file 534-535)
  confirmed two Corrections-log suspects as genuine 1920-only errors,
  both added to `errors in 1920.txt` and (since pptext flagged both this
  run) `permitted words.txt`: v.1 "concludio" (1886: "concluido") and
  v.4 "perididas" (1886: "perdidas"). RAE (via WebSearch) and the local
  reference corpora corroborated both independently (no RAE entry for
  either 1920 form; zero corpus hits for either misspelling). Two more
  flagged words confirmed legitimate and matching 1886 exactly at their
  positions -- v.7 "emaciado" and v.7's second "Traédmeles" -- added to
  `permitted words.txt` only. "Traédmelcs" (v.7's first occurrence) was
  also flagged this run and added to `permitted words.txt` (it is what's
  printed, regardless of the open question below), but NOT added to
  `errors in 1920.txt`. Full-document footnote-anchor check (max 3744,
  zero duplicates/out-of-range, only the pre-existing 812 gap),
  `check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py` (whole document), and an independent
  curly-quote scan all clean. **Two items left open for the editor,
  not decided unilaterally**: v.7 "vcsotrcs" and v.7's first
  "Traédmelcs" -- both transcribed exactly as printed and both confirmed
  to differ from 1886 (plain "vosotros" and "Traédmeles" at both spots
  in 1886), but whether the cause is genuine 1920 type damage, a
  genuine 1920-specific wording choice, or a scan/ink artifact on this
  particular copy could not be settled from the image alone -- matches
  several past cases (see `feedback_narrow_space_vs_merge` and the
  2026-07-18d scan-artifact precedents) where only the editor's own
  direct look at the page resolved what zooming could not. Also flagged
  for the editor's convenience, not as a blocking question: v.7's
  "óque"->"ó que" narrow-space default (grammar clearly requires two
  words here, matching the verse's own repeated "ó cojo, ó ciego..."
  construction, so no zoom/pixel analysis was performed per the
  standing 2026-07-22 default).
- **2026-07-26f, user correction**: user reviewed the two items left open
  at the end of the 2026-07-26e entry by looking directly at the 1920
  page image. Verdict: v.7's first "Traédmel_s" reads clearly as
  "Traédmeles" — not ambiguous at all on direct inspection (matching
  1886 and this verse's own second occurrence exactly), so the earlier
  "Traédmelcs" reading was simply a misread, not a genuine 1920 print
  question. v.7 "vosotros" (in "compasión de vosotros") is genuinely
  printed with two "o"s — but both are under-inked/missing ink, which
  is what made them look like "c"s in the scan crops; a scan/print-
  quality artifact on this particular copy, not a real letter
  substitution. Both corrected to "Traédmeles" and "vosotros" in
  `pages/page_521.txt` and `librodm.txt`; the `permitted words.txt`
  entry for "Traédmelcs" was removed since that form no longer appears
  anywhere in the text (no `errors in 1920.txt` entries existed for
  either, so nothing to remove there). Matches the established pattern
  (pages 472-473, 475, 483, 488, 500, 510, 515, 516) where a
  damaged-looking mark turns out, on the editor's own direct look, to
  be an ink-coverage defect rather than a genuine 1920 typesetting
  error — now the third and fourth instances of this exact page's own
  "o printed with missing ink" pattern, alongside the confirmed
  genuine errors "concludio" and "perididas" already logged. Page 521
  is now fully resolved, no open items remaining.
- **2026-07-26f**: Sessions A–E run for page 522 (III Nefi 17:9(continues)-21,
  footnotes 3745-3752, letters e-l). Session A: mandatory 1879 check for
  letters i (v.14 "turbado") and l (v.21 "tomando"), this page's own
  lettering, confirmed via BOM 1879 Pratt file page 524 (chapter_map has
  no III Nefi rows -- navigated by direct increment from page 521's
  established range; content matches exactly, no drift) -- the full
  letter sequence e-l matched 1879 letter-for-letter, citation-for-
  citation, and body-marker-position-for-position. The check caught a
  genuine Session A misread: footnote l's cross-reference, initially
  read off the worn 1920 swash glyph as "Véase e.", is actually "Véase
  g." -- 1879 reads "l, see g." and content-fit confirms it decisively
  (footnote g's own citation lists verse 21, the exact verse l
  annotates, while the misread "e" target has no connection to v.21 at
  all). Two suspected misprints preserved as printed per rule 32: v.17
  "marvillosas" and v.17 "concibir" (this same verse uses "concebir"
  correctly a few words earlier). One floating scan-artifact ink dot
  (not transcribed) after "sobrecogidos." (v.18/19 boundary), later
  corroborated rather than contradicted by the Google-text cross-check,
  which independently picked up the same mark as a stray ".". Session B
  independently re-verified all 8 Block 1 entries and body markers from
  fresh crops and re-ran the mandatory 1879 check from a fresh crop,
  reconfirming the l->g correction. Session C/D integrated cleanly
  (`insert_body_text.py 522`, `generate_block2.py 522`); footnote 3752
  correctly resolved to 3747 (footnote g), confirming the correction.
  Session E: fresh pptext regeneration (`report_wsl_20260726e.html`)
  confirmed both "marvillosas" and "concibir" as genuine errors despite
  1886 sharing the identical misspellings at the identical spots (file
  537, book 519) -- a shared-error case like "aparacerá"/"seperado"/
  "frustado" -- via RAE (no entry for either 1920 form), the reference
  corpora (zero hits for either misspelling), and the modern Spanish
  edition (3 Nefi 17:16-17, "maravillosas"/"concebir"); both added to
  `errors in 1920.txt` and `permitted words.txt`. Full-document
  footnote-anchor check (max 3752, zero duplicates/out-of-range, only
  the pre-existing 812 gap), `check_spaced_punctuation.py`/
  `check_footnote_punctuation.py`/`check_verse_indent.py` (whole
  document), curly-quote scan, dash check, special situations,
  paragraph-level checks, and Jeebies all clean.
- **2026-07-26g**: Sessions A–E run for page 523 (III Nefi 17:22-25
  chapter close, III Nefi 18:1-9 chapter open, footnotes 3753-3759,
  letter m then chapter 18 restarts a-f). Session A/B: none of this
  page's own letters (m, a-f) or footnote e's plain verse citation are
  i/l/1, but the target-letter glyph for both footnote m ("Véase o.")
  and footnote c ("Véase o, Mosiah 18") looked genuinely ambiguous
  between "o" and "g" in this print's small superscript font --
  extended the check anyway (discretion always runs toward more
  scrutiny) and found both readings were wrong: chapter 17 has no
  letter "o" of its own (lettering only reaches l as of page 522), so
  "m, Véase o." with no book name (matching this chapter's own
  established self-citation convention) couldn't resolve as printed.
  Confirmed via BOM 1879 Pratt (file page 525, chapter_map has no III
  Nefi rows -- navigated by direct increment from page 522's
  established 1879 range): both are "g," not "o" -- corrected to "Véase
  g." (chapter 17's own g = 3747) and "Véase g, Mosíah 18" (Mosíah 18's
  own g = 1342, resolved by hand since `generate_block2.py`'s parser
  doesn't handle this page's mixed direct-citation-plus-Véase-plus-
  direct-citation format). Content-fit corroborates both: 17g's fire/
  glory citation fits v.21 ("tomando," already-confirmed 17l) and v.24
  ("rodeados de fuego," this page's m) equally; Mosíah 18 (Alma's
  priesthood ordinances at the Waters of Mormon) fits v.5's "quedar
  ordenado" as an ordination footnote. Also noted footnote c's trailing
  citation differs between editions -- 1879 prints two separate bare-
  chapter citations ("Moro. 3. IV. 1.") where 1920 unambiguously prints
  "Moroni 3:4" (a genuine colon) -- transcribed as 1920 prints it,
  flagged per rule 26 rather than corrected. Session E's mandatory
  Corrections-log/image re-read caught a genuine Session A transcription
  slip missed by every other check: v.3 "se lo dío" (not a real word,
  wrong accent) was actually printed as plain unaccented "dio" -- fixed
  in `pages/page_523.txt` and `librodm.txt` (rule 12, no
  `permitted words.txt`/`errors in 1920.txt` entry for the transcription
  fix itself). That corrected reading is in turn a genuine 1920-only
  error: 1886 (book 520/file 538) prints "dió" with the accent, and
  ~63 other instances of this verb form elsewhere in `librodm.txt` are
  all accented, with zero other bare "dio" instances -- an isolated
  case (unlike the recurring, already-tolerated "vino a suceder"
  inconsistency), so it clears the bar for a logged error (III Nefi
  18:3); not pptext-flagged since "dio" is itself a rare-but-valid
  Spanish word. Also confirmed a second, independently-caught genuine
  error: III Nefi 17:24 "descedían" (missing "n," 1886: "descendían" at
  book 520/file 537), likewise not pptext-flagged (brand-new-single-
  occurrence quirk) so no `permitted words.txt` entry. Two floating
  scan-artifact marks (a stray dot after "discípulos:" before "He
  aquí," and a stray mark between "que" and "cuando" in v.8) confirmed
  as physical print artifacts, not transcribed. One rule-7 hyphen
  rejoin (v.5 "dis-/cípulos"); two rule-6 unconditional space
  normalizations (v.6, v.8 justification-widened gaps). Full-document
  footnote-anchor check (max 3759, zero duplicates/out-of-range, only
  the pre-existing 812 gap), `check_spaced_punctuation.py`/
  `check_footnote_punctuation.py`/`check_verse_indent.py` (whole
  document), curly-quote scan, dash check (only legitimate verse-range
  hyphens), book/paragraph-level checks, and Jeebies all clean.
  `check_line_wrap.py`'s undercount (13 lines) is the known blind spot
  where it stops at the blank line before a chapter heading, already
  documented on pages 505/521 -- not a real reflow signal here; every
  line was read directly from the image per rules 5/6. Google-text
  cross-check's one candidate (v.22 "Él" vs. Google's unaccented "El")
  confirmed as an OCR miss, not a transcription issue.
- **2026-07-26g**: Sessions A–E run for page 524 (III Nefi 18:10-22,
  footnotes 3760-3767, letters g-n). Session A: mandatory 1879 check for
  this page's own letters i (v.11, "siempre") and l (v.16, "yo soy la
  luz") confirmed via BOM 1879 Pratt file page 526 (chapter_map has no
  III Nefi rows; navigated by direct increment from page 523's
  established range, file 525 -> 526, no drift) -- "i, see f." and "l,
  see m, Mos. 16." matched letter-for-letter and target-for-target,
  including resolving footnote g's illegible over-inked-blob target
  glyph via 1879 alone ("g, see u, II Nefi 9", the recurring baptism-
  scripture citation). Two floating scan-artifact marks (not
  transcribed, matching the established precedent): v.20 (a stray ink
  blob on "haciéndolo"'s final "o") and v.22 (a stray diagonal mark
  between "sino" and "que"). Google-text cross-check
  (`check_google_crosscheck.py 524`) caught a genuine transcription
  error missed by the initial read: v.13 was typed "batán" (accented)
  but the print actually reads plain "batan" -- and the unaccented form
  is the grammatically correct one (third-person-plural present
  subjunctive of "batir," a llana word ending in "n," no accent needed);
  fixed directly (rule 12, not an `errors in 1920.txt` matter). Session
  B independently reconfirmed all 8 Block 1 entries and the mandatory
  1879 check from fresh crops. Session C/D integrated cleanly
  (`insert_body_text.py 524`, `generate_block2.py 524`), all 8 Block 2
  cross-references resolved book-aware with no unresolved targets
  (spot-checked several: h/i self-cite this chapter's own e/f; j/k/m/n
  all resolve to II Nefi 32's or Alma 26's own letter e, correctly
  distinguished from a different book's same chapter+letter via the
  book-scoped index). Session E: fresh pptext regeneration
  (`report_wsl_20260726f.html`) flagged 2 spellcheck suspects, both
  confirmed legitimate against 1886 (book pages 520-521/file 538-539)
  and the modern Spanish edition: v.18 "cerneros" and v.22
  "prohibiréis" -- both added to `permitted words.txt` only. The
  mandatory Corrections-log sweep confirmed both of Session A's
  preserved-as-printed suspects as genuine 1920 errors and added them to
  `errors in 1920.txt`: v.13 "hayan" for singular "haya" (impersonal
  "haber" pluralized incorrectly, same class of error as III Nefi 15:2's
  "habían algunos", confirmed via 1886) and v.19 "necessario" for
  "necesario" (double "s" -- 1886 shares the identical misspelling, a
  shared-error case like "aparacerá"/"seperado"/"frustado", but RAE has
  no entry for it and the reference corpora have zero hits vs. 70 for
  "necesario"). Full-document footnote-anchor check (max 3767, zero
  duplicates/out-of-range, only the pre-existing 812 gap),
  `check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py` (whole document), and an independent
  curly-quote scan all clean. Page has no hyphens at all, so no
  dash-check findings.
- **2026-07-26h**: Sessions A–E run for page 525 (III Nefi 18:23-34,
  footnotes 3768-3777, letters o-x, continuing chapter 18 from page 524).
  Session A/B: none of this page's own letters (o-x) or footnote
  cross-reference targets (m, c, u, u) are in the mandatory i/l/1 set,
  but this page's superscript font prints letters as small round blobs
  with little distinguishing shape, so a full discretionary 1879 check
  was run anyway (independently re-run in Session B from a fresh crop):
  BOM 1879 Pratt file page 527 (chapter_map has no III Nefi rows;
  navigated by direct increment from page 524's established range,
  526->527) matched 1920's own p-x letter-for-letter and citation-for-
  citation (1879's own "o" entry falls on the prior page, matching the
  established one-page-earlier-content drift pattern for this book).
  Footnote r's target resolved to "c" (III Nefi 12c) via 1879 -- a
  content-fit first guess (chapter 12's own "b", a "twelve disciples"
  citation list) was considered but was NOT what 1879 confirmed, so it
  was discarded. Footnote o's target "m" (Mosíah 16) is independently
  corroborated by a mutual cross-reference (Mosíah 16m already cites
  "III Nefi ... 18:16,24" -- the exact verse this footnote annotates).
  Footnote w's target "u" (Alma 16) fits by content too: Alma 16u cites
  Alma 21, where Lamanite "synagogues" are introduced, matching this
  page's own "vuestras sinagogas" (v.32). Four rule-7 hyphenated
  line-break rejoins, no rule-8 rebalancing needed. Session C/D
  integrated cleanly (`insert_body_text.py 525`, `generate_block2.py
  525`), all 10 Block 2 cross-references resolved automatically with no
  unresolved targets. Session E: fresh pptext regeneration
  (`report_wsl_20260726g.html`) flagged "ministrándoles" (v.32) --
  1886 uses a different verb here ("administrándoles"), but the modern
  Spanish edition confirms "ministrando" as an equally legitimate
  translation choice at this verse, so this is a genuine period word
  choice, not a misspelling; added to `permitted words.txt` only. Four
  of five suspected misprints/anomalies from Session A's Corrections
  log were confirmed as genuine 1920-only errors against 1886 (book
  pages 521-522/file 539-540) and added to `errors in 1920.txt`: v.24
  missing period between "mundo" and "He aquí"; v.24 missing semicolon
  before the em-dash (1886: "levantada;--lo", 1920: "levantada--lo");
  v.26 spurious comma in "volvió de, nuevo" (confirmed at zoom to be a
  genuine solid comma, not a scan artifact); v.26 "discipulos" missing
  its required accent (shared with 1886, but the document's own 17:1
  internal ratio, RAE's esdrújula rule, and the modern edition all
  confirm it's wrong). Two floating scan-artifact marks (v.30,
  v.33) were independently confirmed against 1886, which has plain
  unmarked text at both spots. Full-document footnote-anchor check (max
  3777, zero duplicates/out-of-range, only the pre-existing 812 gap),
  `check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py` (whole document), and an independent
  curly-quote scan all clean.
- **2026-07-26i, user correction**: user reviewed page 525 v.28's mark
  over the "o" in "cuando" directly and determined it is a random
  speck, not a genuine grave accent -- the initial reading had wrongly
  matched it to the page 515 "còn"/"què" precedent, and even dismissed
  the Google-OCR cross-check's plain "cuando" reading as expected
  diacritic-blindness rather than the correct answer it actually was.
  The word is plain "cuando", exactly as printed. Corrected in
  `pages/page_525.txt` and `librodm.txt`; the `errors in 1920.txt`
  entry for III Nefi 18:28 was removed (no `permitted words.txt` entry
  existed for it). Matches the established scan-artifact pattern
  (pages 472-473, 475, 483, 488, 500, 510, 515, 516, 521) where a mark
  that reads as genuine type on a zoomed crop turns out, on the
  editor's own direct look, to be print/scan noise -- and a reminder
  (after page 521's "vcsotrcs"/"Traédmelcs") that the Google-text
  cross-check's own signal deserves more weight before being explained
  away as "expected OCR behavior."
- **2026-07-26j, user correction**: the user then identified that the
  ORIGINAL "genuine grave accent" precedent this same day's page-525
  mistake had been modeled on — III Nefi 14:2 "còn"/"què" (page 515,
  logged 2026-07-25) — was itself wrong, for the identical reason:
  both marks are stray specks, not accents; the words are plain "con"
  and "que". `google_text_1920/page_0537.txt` (extracted fresh to
  confirm) reads plain "con"/"que" with no diacritic at all, matching
  the user's direct read. Fixed in `pages/page_515.txt` and
  `librodm.txt`; both `errors in 1920.txt` entries (III Nefi 14:2) and
  both `permitted words.txt` entries ("còn", "què") were removed. Added
  a new standing rule (rule 36, `libro_de_mormon_rules.md` Section 6):
  any unusual/unestablished accent mark must be checked against the
  Google OCR text before being logged as a genuine error — if Google's
  OCR doesn't show the mark either, treat it as a stray speck, not a
  real accent. Lesson explicitly captured in the rule: this pattern
  hit twice in one day, and the second instance was reasoned into
  existence partly by citing the first (already-wrong) one as
  precedent — a match to an earlier "established anomaly" is not
  itself evidence, each instance needs its own Google-OCR check.
- **2026-07-26k**: Sessions A–E run for page 526 (III Nefi 18:35-39
  chapter close, III Nefi 19:1-4, footnotes 3778-3786, letters
  y/z/2a-2c then chapter 19 restarts a-d). Session A: none of this
  page's own letters or cross-reference target letters (y, c) are in
  the mandatory i/l/1 set, but the first glyph after "y" ("z") printed
  as an over-inked blob, so a full discretionary 1879 check was run
  anyway: BOM 1879 Pratt file page 528 (chapter_map has no III Nefi
  rows; navigated by direct increment from page 525's established
  range, file 527->528, no drift) confirmed every letter and the full
  twelve-disciple name list (v.4) letter-for-letter and content-for-
  content, including confirming "Matoni" is correctly unaccented
  (distinct from "Matoníah", which is accented). Two rule-7 hyphen
  rejoins kept in place ("mos-/traría", "Jere-/míah"); one rule-7/8
  case where the rejoined marker+word moved to the next line instead
  ("[3782]dis-/cípulos", combined length would have been 77 chars).
  A short raised mark between "cubrió" and "á" (v.38) that first
  looked like a genuine dash was checked against the Google OCR text
  (`extract_google_text.py 526`), which reads that spot clean with no
  dash at all — treated as a scan artifact per rule 36's principle,
  not transcribed; later independently corroborated by 1886, which
  also prints plain "cubrió á" with no mark. `check_google_crosscheck.py`
  came back with 0 remaining candidates after one genuine catch (v.39
  "partio", confirmed missing its accent by direct zoom) and one
  false alarm (an apparent dropped "y" in "y á Shemnon, y á Jonás",
  confirmed via zoom that 1920 prints both instances; Google's OCR
  just missed one). Session E: fresh pptext regeneration
  (`report_wsl_20260726j.html`) flagged 11 words — 9 are the disciple-
  list proper nouns (Jonás, Kumen, Kumenonhi, Matoni, Matoníah,
  Shemnon, Timoteo, Zedekíah, Jeremíah), added to `permitted words.txt`
  only per rule 11. The other 2 are new genuine 1920-only errors, both
  added to `errors in 1920.txt` and `permitted words.txt`: III Nefi
  18:39 "partio" (missing accent, confirmed against 1886 book page
  522/file 540, which reads "partió"), and III Nefi 19:3 "seguiente"
  for "siguiente" — a shared error with 1886 (book page 523/file 541
  prints the identical misspelling), but RAE has no entry for
  "seguiente" at all, zero hits across all three reference corpora
  (vs. 71 for "siguiente"), the modern Spanish edition uses
  "siguiente" at this verse, and 1886 itself correctly uses
  "siguiente" the verse before (19:2) — confirmed genuine despite the
  1886 agreement, same pattern as "aparacerá"/"seperado"/"frustado".
  Full-document footnote-anchor check (max 3786, zero duplicates/
  out-of-range, only the pre-existing 812 gap),
  `check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py` (whole document), and an independent
  curly-quote scan all clean.
- **2026-07-27**: Sessions A–E run for page 527 (III Nefi 19:5-22,
  footnotes 3787-3798, letters e-p, continuing chapter 19 from page
  526's letter d). Session A: none of this page's own letters (e-p) or
  cross-reference target letters (h, v, u, c) are individually i/l/1,
  but two of the twelve DO happen to be i and l (this page's own i, at
  v.13's second "Santo"; and l, at v.16's "arrodillaran"), so the
  mandatory 1879 check applied to both. Confirmed via BOM 1879 Pratt
  file page 529 (chapter_map has no III Nefi rows; navigated by direct
  increment from page 526's established file 528, content matches
  exactly, no drift): 1879 independently uses the same letters i and l
  at the same positions, and every other letter/citation on the page
  (f, h, j, k, m, o) matched 1879 letter-for-letter and
  content-for-content exactly — including two genuine, expected
  edition differences per rule 26 (1920's four "Véase v, III Nefi 9"
  citations correspond to 1879's "see y, III. Nep. 9" for the identical
  Holy-Ghost content; and 1879 has no equivalent of 1920's extra
  footnote e). Two zero-width print merges (v.5 "que era", "tan
  grande") were normalized to two words per the 2026-07-22 rule-6
  default, no zoom/pixel analysis. Three rule-7 hyphen rejoins
  (palabras, ministrando, discípulos), the last one triggering rule 8
  rebalancing since the footnote marker pushed it over 72 chars.
  Session B independently re-verified all 12 Block 1 entries, all 12
  body markers, and re-ran the mandatory i/l check from fresh crops —
  all reconfirmed exactly. Session C/D integrated cleanly
  (`insert_body_text.py 527`, `generate_block2.py 527`), all 12 Block 2
  cross-references resolved automatically with no unresolved targets;
  notably III Nefi 17's own letter h (3748) cites "III Nefi 19:6,16-17"
  — a mutual cross-reference that independently confirms this page's
  own e and l resolutions (v.6 and v.16 are exactly the verses e and l
  annotate). One process bug found and fixed: this page's file
  originally included a "Block 1:" label line (deviating from the
  no-label convention established on pages 511+), which caused
  `insert_body_text.py` to swallow that label into `librodm.txt`'s body
  text right before `Notas` — the same bug documented on 2026-07-25i
  (page 515); `librodm_foot.txt` was unaffected. Fixed by removing the
  label from both files. The Google-text cross-check
  (`extract_google_text.py 527`/`check_google_crosscheck.py 527`)
  caught one genuine transcription error the initial read missed: v.10
  was typed "siguió" but the print (and Google's OCR) actually reads
  "seguió" — fixed directly per rule 12. Session E: fresh pptext
  regeneration (`report_wsl_20260727.html`) flagged two spellcheck
  suspects for this page's range. "Pusiéronse" (v.6) confirmed
  legitimate — matches 1886 exactly (book page 523/file 541), the same
  archaic enclitic-pronoun pattern already established elsewhere in the
  document; added to `permitted words.txt` only. "seguió" (v.10) turned
  out to itself be a genuine 1920 error despite being the very word the
  Google cross-check had just confirmed was actually printed: 1886
  shares the identical reading at the identical spot (a shared error,
  same pattern as "seguiente"/"aparacerá"/"seperado"/"frustado"/
  "necessario"/"discipulos"), but "seguir" is an irregular e→i
  stem-changing verb whose third-person preterite is always "siguió"
  per RAE, the local reference corpora have zero hits for "seguió"
  versus 5 for "siguió" in Don Quijote, and the modern Spanish LDS
  edition (3 Nefi 19:10) reads "siguió"; added to both `errors in
  1920.txt` and `permitted words.txt`. Full-document footnote-anchor
  check (max 3798, zero duplicates/out-of-range, only the pre-existing
  812 gap), `check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py` (whole document), and an independent
  curly-quote character-count scan of both master files all clean. No
  hyphens remain in this page's body text besides the two intentional
  em-dashes (v.8), so no dash-check findings.
- **2026-07-27b**: Sessions A–E run for page 528 (III Nefi 19:23-34,
  footnotes 3799-3805, letters q-w, continuing chapter 19 from page
  527's letter p). Session A: none of this page's own letters (q-w) are
  i/l/1, so no mandatory 1879 check applied; q and r were zoom-confirmed
  against their matching footnote-block glyph shapes, and s-w were
  assigned by strict sequential position plus strong content-fit (t/v
  are a mutual self-citation pair, "Versículo 30"/"Versículo 25",
  between v.25's and v.30's near-identical whiteness descriptions; q/u
  share an identical "Véase p, III Nefi 9" citation for the same
  recurring "esté yo en ellos" phrasing at v.23 and v.29). One rule-7
  hyphen rejoin (v.28 "puri-/ficado"). Three zero-width print merges
  normalized to two words per the 2026-07-22 rule-6 default (v.22 "ves
  que", v.25 "que eran", v.30 "que oraban"). Seven space-before-
  semicolon/colon instances normalized per rule 31, including one in
  footnote w's own citation (verses 16/17 of chapter 17 are consecutive,
  so per rule 23 they become a hyphenated range: "17:16-17"). The
  Google-text cross-check (`extract_google_text.py 528`/
  `check_google_crosscheck.py 528`) cleared two OCR misses (a dropped
  "y" at v.25, diacritic-blindness on v.29's "aquéllos") but caught one
  genuine transcription gap the initial read had missed entirely: v.31
  prints a solid period after "oró" ("...un poco de ellos, oró. de
  nuevo al Padre;") — confirmed at zoom (same size as the page's other
  periods, not a scan speck) and against 1886 (book page 525/file 543,
  which reads the clause continuously with no punctuation), a genuine
  1920-only error, transcribed as printed per rule 32 and added to
  `errors in 1920.txt` (III Nefi 19:31; no `permitted words.txt` entry,
  punctuation not spelling). Session B independently re-verified all 7
  Block 1 entries and all 7 body markers from fresh crops; no errors
  found. Session C/D integrated cleanly (`insert_body_text.py 528`,
  `generate_block2.py 528`); all 7 Block 2 cross-references resolved
  automatically with no unresolved targets, and III Nefi 9's own
  resolved footnote p (seq. 3576) independently corroborated the q/u
  letter identity and body-marker placement — its own citation list
  ("III Nefi 11:27; 19:23,29; Éther 3:14") names verses 23 and 29,
  exactly where q and u were placed. Session E: fresh pptext
  regeneration (`report_wsl_20260727b.html`) flagged one new spellcheck/
  edit-distance suspect, v.28 "excogido" (edit distance 1 from
  "escogido", which appears 29 other times in the document) — confirmed
  at zoom to print an unambiguous "x", confirmed against 1886 (book page
  525/file 543: "escogido", with "s"), confirmed via the reference
  corpora (zero hits for "excogido" vs. 73 combined for "escogido"; not
  a Spanish verb), and confirmed via the modern Spanish edition (3 Nefi
  19:28: "escogido") — a genuine 1920-only error, added to both `errors
  in 1920.txt` and `permitted words.txt`. The same run's "full stop
  followed by unexpected sequence" check independently re-surfaced the
  v.31 period finding, corroborating the Google cross-check catch.
  Independent full-document footnote-anchor check (direct regex scan):
  max 3805, zero duplicates, zero out-of-range, only the pre-existing
  812 gap. `check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py` (whole document) and an independent curly-quote
  scan of both master files all clean. Dash, hyphenation/spaced-pair,
  scanno, special situations, book-level checks, and Jeebies all clean
  for this page's range.
- **2026-07-27b**: Sessions A–E run for page 529 (III Nefi 19:34-36
  chapter close, III Nefi 20:1-11 chapter open, footnotes 3806-3810,
  letters 19x then chapter 20 restarts a-d). Session A: resolved page
  528's pending page-boundary hyphen split (rule 10) first — "pala-"
  completes as "palabras," appended to page 528's last line (63 chars,
  under the cap); page 529's body begins with the following word, "de,"
  instead (`pages/page_528.txt` and `librodm.txt` both revised). None of
  this page's own letters (x, a-d) or cross-reference targets (b, t, y,
  and d's direct citation) are i/l/1, but the block uses the same
  heavily stylized swash-italic font seen on several recent pages, so a
  full discretionary 1879 check was run anyway via BOM 1879 Pratt file
  page 531 (chapter_map has no III Nefi rows; navigated by direct
  increment from page 528's established file 530, content lands on the
  exact next page, no drift): confirmed the first footnote's glyph
  (which could plausibly read "a" at a glance) must continue chapter
  19's sequence as "x" per rule 13's no-gaps requirement — 1879 confirms
  ("x, see d, III. Nep. 17."). Also caught a v/y swash-font misread
  (footnote c's target, matching the page 510 11-2o/12e precedent):
  1879 reads "c, see y, III. Nep. 9.", not v, corroborated by content-
  fit (III Nefi 9's own y is the recurring "filled with the Holy Ghost"
  citation chain, an exact match for this page's own v.9 "sintióse
  llena del Espíritu"). Footnote d's citation ("III Nefi 16:17; Isaías
  52; 9,10.") has a confirmed punctuation defect — 1879 (file page 532)
  reads a colon between "52" and "9,10," not the semicolon 1920 prints,
  which otherwise doesn't parse as a citation; preserved as printed per
  rule 32 and logged in `errors in 1920.txt` as a footnote-text entry
  (no `permitted words.txt` entry, punctuation not spelling). Three
  rule-7 hyphen rejoins (multi-/tud, pala-/bras, examin-/adlas); four
  space-before-semicolon normalizations (rule 31); one stray scan-
  artifact ink speck near "Y" in v.35 ("Y aconteció"), not transcribed.
  Session B independently reconfirmed all 5 Block 1 entries and body
  markers from fresh crops. Session C/D integrated cleanly
  (`insert_body_text.py 529`, `generate_block2.py 529`), all 5 Block 2
  cross-references resolved automatically with mutual self-citation
  confirmation (III Nefi 18's own b/t footnotes already cite III Nefi
  20:3-9 and 20:8, exactly the verses they annotate here). Session E:
  fresh pptext regeneration (`report_wsl_20260727.html`) came back fully
  clean for this page's own new range — no spellcheck/edit-distance
  hits, footnote-anchor check (independent regex scan: max 3810, zero
  duplicates/out-of-range, only the pre-existing 812 gap) clean, curly-
  quote scan and Jeebies clean, `check_spaced_punctuation.py`/
  `check_footnote_punctuation.py`/`check_verse_indent.py` (whole
  document) all clean. Incidentally closed a `permitted words.txt`
  mirroring gap from an earlier page: "mándoos" (III Nefi 16:4, page
  519) was flagged by this run's spellcheck section but had never been
  added; confirmed legitimate (same archaic imperative+enclitic pattern
  as apoderáos/entregáos/salváos/etc.) and added. No other `permitted
  words.txt`/`errors in 1920.txt` entries needed for this page's own
  text — otherwise a fully clean orthography pass.
- **2026-07-27c**: Sessions A–E run for page 530 (III Nefi 20:12-23,
  footnotes 3811-3825, letters e-w — chapter 20's own lettering skips
  i,j,k,l entirely, jumping from h straight to m). Session A: this
  page's footnote-target-letter reads were unusually error-prone at
  first pass (a heavily stylized swash reference font, same class of
  issue as pages 501/509/510) — five of the seven "Véase" entries
  turned out to differ from an initial 1920-image read once compared
  against BOM 1879 Pratt (file page 532, navigated by direct increment
  from page 529's established file 531, content lands one page later)
  plus content-fit against the already-transcribed target chapters'
  own lettering: e→j (not i), f→e (not c), g→o (not e), h→l (mandatory
  letter, confirmed), m→c (not e), q→j (not i); r→o and w→m both
  matched the initial read. w's resolution was independently
  corroborated by a mutual cross-reference — I Nefi 22's own letter m
  (240) already cites "III Nefi 20:23," the very verse footnote w
  annotates. The missing i/j/k/l letters were confirmed via the same
  1879 page to be a genuine feature shared by both editions, not a
  1920-only defect or a miscount — 1879 shows the identical "h, see l...
  m, see c..." jump. Four suspected misprints preserved as printed
  per rule 32: v.16 "leon" (×2, missing accent), v.19 "qulén" (missing-
  looking "i" printed as "l") and "cuermo" (for "cuerno"), v.23
  "peofeta" (for "profeta") — all zoom-confirmed at high resolution. The
  Google-text cross-check flagged "qulén" as a candidate (reading
  "quién"), but a max-zoom re-read settled it in favor of "qulén" as
  genuinely printed (a tall, dotless stroke matching this line's own
  "l" shapes, not the short dotted "i" in the adjacent word "mi") — the
  OCR misread the tall stroke. One rule-7/8 hyphen rejoin (v.20 "arre-/
  pintieren" → "arrepintieren," moved to the next line since the
  rejoined line would have reached 74 characters). Session B
  independently re-verified all 15 Block 1 entries/body markers and
  re-ran the mandatory 1879 check for footnote h's target letter l from
  a fresh crop; reconfirmed exactly. Session C/D integrated cleanly;
  `generate_block2.py` left footnote w's citation unresolved (the known
  mixed "Véase X, Book; extra citation" format) — resolved by hand to
  "Véase 240; Deuteronomio 18:15,18,19; Actos 3:19-26." Session E: fresh
  pptext regeneration (`report_wsl_20260727b.html`) came back clean in
  Spellcheck Suspect Words for this page (none of the four suspected
  misprints are flagged — known brand-new-single-occurrence quirk, so
  no `permitted words.txt` entries). All four confirmed as genuine 1920
  errors via 1886 (book page 527, file 544-545) and added to `errors in
  1920.txt`: "leon" (1886 shares the identical unaccented spelling — a
  shared-error case like "aparacerá"/"seperado"/"necessario" — but RAE
  requires the tilde on this aguda word, the clean reference corpora
  show zero unaccented instances against 16 accented in Quijote, and
  the modern Spanish edition uses "león"), "qulén"→"quién" (1886: "quien"
  with "i", confirming the 1920 print's "l" is a genuine substitution),
  "cuermo"→"cuerno", and "peofeta"→"profeta" (both 1920-only, 1886 has
  the correct forms). Full-document footnote-anchor check (max 3825,
  zero duplicates/out-of-range, only the pre-existing 812 gap),
  `check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py` (whole document), and an independent
  curly-quote scan all clean. Page has zero hyphens in its final body
  text, so no dash-check findings; paragraph-level checks, book-level
  checks, and Jeebies all clean.
- **2026-07-27c**: Sessions A–E run for page 531 (III Nefi 20:23(continues)-35,
  footnotes 3826-3839, letters x-z then two-letter codes 2a-2k). Session A:
  this page's own footnote-reference font is the same heavily stylized
  swash italic already documented as ambiguous on pages 509/510 — an
  initial read of the first three letters looked like z, v, s (with no
  visible descender distinguishing the second glyph from a "v"), which
  would have violated rule 13 (page 530 ended at letter w, so page 531
  must continue x, y, z with no gap). Resolved via the mandatory 1879
  cross-check (BOM 1879 Pratt file page 533, chapter_map has no III Nefi
  rows — navigated by direct increment from page 530's established file
  532, content lands on the exact next page, no drift): 1879 reads "x,
  Acts 3:19-26. y, ver. 27. Gen. 22:18. Acts 3:25. z, see y." — confirming
  x, y, z, the same "looks like v with no visible descender, is actually
  y" pattern already documented on page 510 (11-2o/12e). Footnote 2f's
  target letter was similarly misread at first as "i" (mandatory check
  applied) — 1879 reads "2f, see j, III. Nep. 15.", and content-fit
  confirms j over i decisively: III Nefi 15j (3702) cites "III Nefi
  5:24-26; 16:5; Véase e, I Nefi 15" (the gathering/covenant theme v.29
  is actually about), while 15i (3701) cites the unrelated Sermon-on-
  the-Mount passage. This page's own literal letter "i" (2i, a direct
  citation) was independently confirmed via the same 1879 page. All
  other letters/targets matched 1879 letter-for-letter, including two
  mutual cross-reference confirmations (II Nefi 25f cites "III Nefi
  20:30", the exact verse footnote 2h annotates; II Nefi 31k cites "III
  Nefi 11:27-28,36", the Godhead-"one" doctrine matching v.35). Three
  rule-7 hyphen rejoins (iniquidades, evangelio, juntamente) and one
  rule-8 overflow (inserting [3829] before "Santo" pushed a line to 73
  chars, so "de" moved to the next line). A mark that looked, at low
  zoom, like a comma wedged into "Y sucederá" (v.30) was confirmed via
  progressively higher zoom plus the Google-text cross-check as a stray
  ink speck, not real type — transcribed as plain text, matching the
  established scan-artifact precedent (pages 472-473 through 525).
  Session B independently reconfirmed all 14 Block 1 entries and the
  mandatory 1879 check from fresh crops. Session C/D integrated cleanly
  (`insert_body_text.py 531`, `generate_block2.py 531`), all 14 Block 2
  cross-references resolved automatically, including 2f→3702 confirming
  the letter correction. Session E: fresh pptext regeneration
  (`report_wsl_20260727c.html`) confirmed 2 genuine 1920-only errors
  against 1886 (file 546, book 528): v.28 "plentitud" for "plenitud"
  (this page's own v.30 spells it correctly, matching the established
  III Nefi 16:4/16:7/16:10 pattern) and v.29 "ofredico" for "ofrecido"
  (c/d transposed; zero corpus hits for "ofredico"). Both added to
  `errors in 1920.txt`; "ofredico" also added to `permitted words.txt`
  (flagged this run); "plentitud" was not re-flagged since it's already
  in `permitted words.txt` from the earlier III Nefi 16 instances —
  blanket suppression, not evidence of a clean occurrence. "bendeciros"
  (v.26) also flagged this run — confirmed legitimate via 1886 (file
  545, identical word at the identical spot), added to `permitted
  words.txt` only. Full-document footnote-anchor check (max 3839, zero
  duplicates/out-of-range, only the pre-existing 812 gap),
  `check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py` (whole document), curly-quote scan, and
  Jeebies all clean. Page has no hyphens in its final body text, so no
  dash-check findings. One incidental edition punctuation difference
  noted but not logged as an error: v.34's colon before "cantad" vs.
  1886's comma-plus-dash at the same spot — both grammatically valid,
  not a case of 1920 diverging into nonsense.
- **Next page**: 532, full A–E cycle, first footnote 3840.
- **Completed pages**: 437–531, Sessions A–E fully done through page 531.
- **2026-07-28**: Sessions A–E run for page 532 (III Nefi 20:36-46, then
  CAPÍTULO 21:1, footnotes 3840-3847; chapter-20 letters l-q continuing
  from page 531's 2k, then chapter 21 resets to a-b). Session A: the
  first footnote glyph (2l, before "Isaías 52:1-3,6") looked at overview
  zoom like it could be superscript digit "1" rather than letter "l" —
  triggering the mandatory i/l/1 check regardless, and rule 13 already
  required "l" since page 531 ended its own lettering at 2k. Resolved
  via the mandatory BOM 1879 Pratt cross-check (file page 534, chapter_map
  has no III Nefi rows — navigated by direct increment from page 531's
  file 533/534): 1879's footnote block reads "2 k, see k, II. Nep. 31.
  2 l, Isaiah 52:1-3, 6. 2 m, Isaiah 52:7." etc., confirming the true
  letter is l. A second glyph, footnote 20p's cross-reference target
  letter (after "Véase"), was misread at first overview pass as "i"; a
  dedicated zoom crop showed a clear descender/tail below the baseline
  (unlike this document's "i," a short stroke with a separated dot and
  no descender), re-read as "j" before consulting 1879 — confirmed
  directly: "2 p, see j, III. Nep. 15." Both checks also confirmed the
  remaining four chapter-20 markers (2n, 2o, 2q) and chapter 21's own
  two letters (a, b) letter-for-letter and target-for-target against
  1879 (files 534/535). Three rule-7 hyphen rejoins (Despierta, apartáos,
  entenderán), all landing under the 72-char cap so none moved to the
  next line. Numerous rule-31 space-before-punctuation fixes throughout
  (this page's print consistently sets a space before colons, semicolons,
  and the closing "!"). No suspected misprints noticed on this page.
  Session B independently reconfirmed all 8 Block 1 entries and the
  mandatory 1879 checks from fresh crops of file 534 — both letters (l,
  j) reconfirmed exactly. Session C/D integrated cleanly
  (`insert_body_text.py 532`, `generate_block2.py 532`), all 8 Block 2
  cross-references resolved automatically, including 3844→3702 (III
  Nefi 15's own letter j, matching page 531's identical target and
  reconfirming the letter correction) and 3845/3847→128 (I Nefi 15e,
  matching page 531's 20-2j/20-2g identical target). Session E: fresh
  pptext regeneration (`report_wsl_20260728.html`) introduced zero new
  findings from this page — every distinctive word/phrase unique to
  this page's new text was searched against the report and found in
  none of the Spellcheck Suspect Words, Edit Distance, dash, scanno,
  curly-quote, or special-situations sections; the only nearby flagged
  spellcheck words (cuermo, leon, peofeta, Profecia, qulén) belong to
  the previous page's own text, not this page's. "limpiáos" (v.41, the
  same archaic accented reflexive-imperative form as "apartáos" and
  ~24 other already-permitted "-áos" words) was not flagged by aspell
  at all, so no `permitted words.txt` entry was added for it, per the
  "Jesu Cristo" precedent (an entry is only useful for a word aspell
  would otherwise flag). Full-document footnote-anchor check (max 3847,
  zero duplicates/out-of-range, only the pre-existing 812 gap),
  `check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py` (whole document), and an independent
  curly-quote character scan of both master files all clean. Page has
  no hyphens in its final body text, so no dash-check findings; Jeebies
  clean. No `permitted words.txt` or `errors in 1920.txt` additions
  this session.
- **2026-07-28b**: Sessions A–E run for page 533 (III Nefi 21:2-11,
  footnotes 3848-3870, chapter 21 continuing its own lettering from
  page 532's a/b straight through c-y, no chapter/book boundary on this
  page). Session A: this page's swash font proved unusually unreliable
  at overview zoom — the mandatory BOM 1879 Pratt cross-check (files
  535/536, chapter_map has no III Nefi rows, navigated by direct
  increment from page 532's established file 534/535) caught not only
  the two mandatory i/l/1 letters (this page's own i and l, both
  confirmed) but also a third i/l/1 case that was a genuine misread:
  footnote 21k's cross-reference target (III Nefi 15) was first read as
  "i" but 1879 says "see j," confirmed by a 20x zoom showing a clear
  descender the first overview pass had missed, and by content-fit
  (III Nefi 15's letter j is the same covenant-themed citation already
  established on page 532, matching this page's word "alianza"; letter
  i is an unrelated Sermon-at-the-temple citation). Discretionary
  extension of the same check (triggered by that miss) caught three
  more misread cross-reference target letters, all corrected against
  1879: 21d (v→y, III Nefi 9), 21m's second target (k→h, I Nefi 12,
  confirmed against 1879's "g and h" not "g and k"), and 21p (z→x, III
  Nefi 16). A fifth, 21y's target (c→e, II Nefi 3), stayed genuinely
  hard to read even at high zoom because the glyph sits under the
  page's "Digitized by Google" watermark, so it leans on 1879 plus a
  content-fit check (II Nefi 3's letter e is a seer/seer-stone citation
  fitting this page's "quién daré poder"; letter c is an unrelated
  Gentiles/scattering citation). None of the five corrected letters are
  this page's own lettering (all are cross-reference targets in other
  chapters), so none affect the c-y sequence or footnote numbers
  3848-3870 themselves. Two rule-7 hyphen rejoins ("considera-"/"rán",
  "mos-"/"trarles"); the first rejoin would have landed its line at 73
  characters, so per rule 8 the whole rejoined word moved to the start
  of the next line instead. One unrelated rule-8 overflow (v.7's line
  with two footnote markers plus "para" hit 73 characters; "para"
  moved to the next line). `check_google_crosscheck.py` caught one
  genuine, previously-undetected transcription error: v.7's "empieze"
  had first been transcribed as "empiece," but Google's OCR read "z"
  correctly — confirmed via high-zoom crop and via 1886 (file 548,
  book page 530), which prints "empiece" correctly at the parallel
  spot, isolating this to a fresh, location-specific 1920 typo distinct
  from the already-logged II Nefi 3:13 "empieze" (where 1886 shares the
  error). A second suspected misprint, v.10 "mi sabiduría en más
  grande" (grammar calls for "es"), was preserved as printed and
  confirmed via both 1879 ("is greater than") and 1886 ("es más
  grande," file 548) — likely a straightforward s/n typo that produces
  a real, common Spanish word, so aspell/pptext would never flag it on
  their own. "Jesu Cristo" (v.11, no hyphen) matches this document's
  long-established spelling convention (~19+ prior occurrences); 1886
  prints "Jesu-Cristo" with a hyphen at the same spot, a 1886-specific
  choice, not evidence 1920 is wrong. Session B independently
  reconfirmed all 23 Block 1 entries and both mandatory-plus-
  discretionary letter corrections from fresh crops of files 535/536,
  and reconfirmed "empieze" from a fresh crop — no further errors
  found. Session C/D integrated cleanly (`insert_body_text.py 533`,
  `generate_block2.py 533`); 22 of 23 Block 2 cross-references resolved
  automatically, including 3856→3702 (III Nefi 15's own letter j,
  reconfirming the k-letter correction) and 3870→276 (II Nefi 3's own
  letter e, reconfirming the y-letter correction); the 23rd (3858,
  "Véase g, y h, I Nefi 12") resolved to "Véase 82 y 83" but the script
  still flagged it for manual review — checked directly against
  librodm_foot.txt and confirmed correct (I Nefi 12's own letters g=82,
  h=83). Session E: fresh pptext regeneration
  (`report_wsl_20260728b.html`) via the efficient line-range filter
  (body lines 23806-23849, Block 2 lines 27978-28000) found only the
  already-known "short lines check" false-positive category, nothing
  new; a keyword search of the whole report for this page's distinctive
  vocabulary surfaced only pre-existing content from other pages or the
  book's own table-of-contents entry for page 533. Two new `errors in
  1920.txt` entries added, in book/chapter/verse order after the
  existing III Nefi 20:29 entry: III Nefi 21:7 empieze/empiece, and
  III Nefi 21:10 en/es más grande. No `permitted words.txt` addition
  needed ("empieze" already present from an earlier page's identical
  error; "en" is a common word aspell will never flag). Full-document
  footnote-anchor check (max 3870, zero duplicates/out-of-range, only
  the pre-existing 812 gap), `check_spaced_punctuation.py`/
  `check_footnote_punctuation.py`/`check_verse_indent.py` (whole
  document), and an independent curly-quote character scan of both
  master files all clean. Page has zero hyphens in its final body text
  (both rejoins removed the only candidates), so no dash-check
  findings. No narrow-space-vs-merge defaults were made on this page.
- **2026-07-28c**: Sessions A–E run for page 534 (III Nefi 21:12-26,
  footnotes 3871-3886, chapter 21 continuing). Session A: this page is
  where chapter 21's lettering exhausts the single-letter alphabet
  begun on page 532 (...w, x, y on page 533) — the page's first
  footnote is the lone single letter "z," and every remaining footnote
  switches to rule-16's two-letter "2a, 2b..." codes (confirmed both
  by the mandatory 1879 BOM Pratt cross-check, which prints the
  identical two-character superscripts throughout its own parallel
  block, and by the body text's own markers, set in a clearer
  non-swash font that reads unambiguously at normal zoom). The
  mandatory 1879 cross-check (1920 file 556; 1879 file 537 — the same
  physical 1879 page carries both the tail of old-chapter-21's
  footnote block, 2e-2s, and new-chapter-22's own a-d block below it,
  per that edition's older/longer chapter divisions; chapter_map has
  no III Nefi rows, navigated by direct increment from page 533's
  established file 536/537) confirmed this page's own letters i and l
  (3880, 3883) and caught two genuine misreads: footnote 21-2f's
  cross-reference target (III Nefi 15) was first read as "i" but 1879
  says "see j," confirmed by a high-zoom crop showing a hook/descender
  the overview pass had missed; the same error propagated into
  footnote 21-2m's self-reference (first read "Véase 2i," corrected to
  "Véase 2j" against 1879's "see 2j" and a matching zoom of that
  glyph). Content-fit confirms both: III Nefi 15's own letter j (=
  sequential 3702, already established on page 532) is a
  covenant-themed citation matching this page's own 2j entry (which
  cites the same III Nefi 20:22/Éther passage the 2m/2j pairing
  shares). Neither correction is this page's own lettering, so neither
  affects the z/2a-2o sequence or footnote numbers 3871-3886
  themselves. One rule-7 hyphen rejoin ("con-"/"tados" → "contados"),
  which cascaded two lines deep under rule 8 (the rejoined line hit 77
  characters, so the whole marked word moved to the next line, which
  itself then reached 77 characters and cascaded its own last word one
  line further); a second, unrelated rule-8 overflow moved the page's
  first line's final word ("serán") to the next line once its footnote
  marker was added. `extract_google_text.py`/`check_google_crosscheck.py`
  found zero candidates (fully clean), but Google's own OCR
  independently confirmed a genuine finding noticed by eye: footnote
  21-2k's "Géntiles" carries an unusual accent that Google's OCR
  reproduces too (real evidence it's actually printed, not a scan
  speck, per rule 36), even though "Gentiles" is correctly unaccented
  elsewhere on this same page's own body text. Two suspected
  misprints preserved as printed per rule 32 and confirmed against
  1886: v.12 "leon" (león) 2x, matching the already-documented III
  Nefi 20:16 pattern (1886 shares the same unaccented spelling, RAE
  requires the tilde on this aguda word); and v.24 "reuna" (reúna),
  also shared with 1886, RAE requiring the tilde per reunir's hiato
  rule (reúno, reúne, reúna...). Session B independently re-verified
  all 16 Block 1 entries and body markers from fresh crops, re-ran
  both mandatory 1879 checks from fresh crops, and reconfirmed both
  letter corrections (21-2f: j, 21-2m: 2j) exactly — no further errors
  found. Session C/D integrated cleanly (`insert_body_text.py 534`,
  `generate_block2.py 534`); all 16 Block 2 cross-references resolved
  automatically, including 3877→3702 (III Nefi 15's own letter j,
  reconfirming the f-letter correction) and 3884→3881 (this page's own
  2j entry, reconfirming the m-letter correction). Session E: fresh
  pptext regeneration (`report_wsl_20260728c.html`) via the efficient
  line-range filter (body lines 23850-23892, Block 2 lines
  28045-28060) plus a keyword search of the whole report surfaced all
  three findings already anticipated above ("leon" not flagged by
  spellcheck — a likely aspell false-negative from overlap with the
  proper noun "León" — while "Géntiles" and "reuna" were both flagged
  by spellcheck and corroborated by the edit-distance section); this
  session added the RAE/Fundéu confirmation that "reúna" always
  requires its tilde (WebSearch) and a reference-corpora check (zero
  hits either way for reuna/reúna in all three corpora — inconclusive,
  word is simply rare). Three `errors in 1920.txt` entries added in
  book/chapter/verse order after the existing III Nefi 21:10 entry
  (21:12 leon/león, footnote 21-2k Géntiles/Gentiles, 21:24
  reuna/reúna); `permitted words.txt` updated with all three forms,
  also backfilling "leon" for the pre-existing III Nefi 20:16
  occurrence which had never been added despite already being a
  documented error. No other pptext section (repeated word, duplicate
  lines, ellipsis, dash/hyphen, footnote check, scanno, curly quotes,
  special situations) produced any hit in this page's line range.
  Full-document footnote-anchor check (max 3886, zero
  duplicates/out-of-range, only the pre-existing 812 gap),
  `check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py` (whole document), and an independent
  curly-quote character scan of both master files all clean. Page has
  zero hyphens in its final body text (the one rejoin removed the only
  candidate), so no dash-check findings. No narrow-space-vs-merge
  defaults were made on this page.
- **2026-07-28d**: Sessions A–E run for page 535 (III Nefi 21:26–22:8,
  footnotes 3887-3896; chapter 21 finishes and chapter 22 opens
  mid-page — rule 20, no blank line/header needed in Block 1 since it
  stays within III Nefi). Session A: chapter 21 continues its
  two-letter codes from page 534 (2p-2s), then chapter 22 restarts
  cleanly at single letters a-f per rule 13; none of the ten letters or
  their cross-reference targets (b, p, e, c) are i/l/1, so the
  mandatory 1879 check did not apply. Footnote 21-2s's reference glyph
  read as a stylized swash "III" easily mistaken for "H"/"II" at a
  glance — resolved to "III Nefi 20:42" by content fit (II Nefi 20 only
  has 34 verses; III Nefi 20 is the chapter this whole passage already
  cites repeatedly; v.42 pairs with the paired Isaías 52:11-15
  citation, matching this footnote's annotated word
  "saldrán"/Isaiah 52:12's "no saldréis apresurados"), independently
  corroborated by Google's own garbled OCR reading ("FI Nefi 20 : 42").
  A genuine 1920-only misprint was caught and preserved as printed per
  rule 32: chapter 22 v.1 prints "sucererá" where 1886 (file 549, book
  page 531) has the correct "sucederá," and the page's own text two
  verses back on page 534 (III Nefi 21:20) already uses the correct
  spelling — confirmed by Google's independent OCR reading the
  identical "sucererá" at the same spot (real evidence it is actually
  printed that way), by a zero-result RAE search, and by zero hits in
  all three local reference corpora against one hit for "sucederá" in
  the Quijote corpus. One rule-7 hyphen rejoin ("aver-"/"güences" ->
  "avergüences"); no rule-8 overflow anywhere else on the page.
  `check_line_wrap.py` and `check_google_crosscheck.py` both flagged
  large discrepancies that turned out to be false positives from the
  same root cause: both scripts' body-text extraction helper stops at
  the first blank line, so a page with a mid-page chapter break (this
  page's CAPÍTULO 22 heading) silently truncates everything after it —
  chapter 22's 24 lines were never actually compared by either script.
  Manually cross-checked chapter 22 against the OCR/Google text
  directly instead; both came back clean, with Google's OCR itself
  corroborating the "sucererá" misprint as noted above. Session B
  independently re-verified all 10 Block 1 entries and body markers
  from fresh crops; no further errors found. Session D
  (`generate_block2.py 535`) surfaced two real, previously-undiagnosed
  bugs in the script itself (not page-specific): the cross-reference
  resolver's book/chapter regex could not handle a citation that
  included its own verse number (e.g. "III Nefi 20:22" instead of bare
  "III Nefi 20"), and `--fix-unresolved` was silently resetting its
  tracked book_id to None on every ordinary wrapped continuation line
  of a multi-line reference, breaking resolution for everything after
  it until the next real book header. Both fixed (the first by
  allowing an optional ":verse" suffix in the regex, the second by
  using the citing entry's own book_id from the already-correct
  footnote index instead of re-deriving it by scanning librodm.txt's
  headers at all, matching what the incremental path already did
  correctly). Re-running `--fix-unresolved` after the fixes resolved
  this page's stuck footnote 3888 (-> 3818, III Nefi 20's own letter p)
  plus five other long-stuck cross-references elsewhere in the
  document; a second run confirmed zero further changes, and
  whole-document rule-31/22/23/verse-indent checks stayed clean
  throughout. Session E: fresh pptext regeneration
  (`report_wsl_20260728d.html`); neither "sucererá" nor chapter 22
  v.6's "fuíste" appeared in the report's spellcheck section at all
  (confirmed via direct standalone aspell testing instead, both
  flagged as unrecognized — matching the already-documented
  pages-469-470 gap where a rare single-occurrence word can go
  unflagged in the full-document run). "sucererá" was added to `errors
  in 1920.txt` (III Nefi 22:1) and, per rule 10, to `permitted
  words.txt` as well. "fuíste" was resolved the opposite way: 1886
  independently prints the identical accented form at the identical
  spot, and RAE's own NGLE (via a WebSearch-sourced @RAEinforma
  citation, section 4.4f) documents "fuiste, viste, dijiste" as
  historically accented forms under the pre-simplification orthography
  — the same category already established in this project for
  "fué"/"vió"/"fuí" — so it was added to `permitted words.txt` only,
  not `errors in 1920.txt`, even though (unlike those three) it has
  zero hits in any of the three local reference corpora. No other
  pptext section produced a hit for this page. Full-document
  footnote-anchor check (max 3896, zero duplicates/out-of-range, only
  the pre-existing 812 gap), a fresh curly-quote character scan of both
  master files, and `check_spaced_punctuation.py`/
  `check_footnote_punctuation.py`/`check_verse_indent.py` (whole
  document) all clean. Page has zero hyphens in its final body text, so
  no dash-check findings. No narrow-space-vs-merge defaults were made
  on this page.
- **2026-07-28d**: Sessions A–E run for page 535 (III Nefi 21:26–22:8,
  footnotes 3887-3896; chapter 21 finishes and chapter 22 opens
  mid-page — rule 20, no blank line/header needed in Block 1 since it
  stays within III Nefi). Session A: chapter 21 continues its
  two-letter codes from page 534 (2p-2s), then chapter 22 restarts
  cleanly at single letters a-f per rule 13; none of the ten letters or
  their cross-reference targets (b, p, e, c) are i/l/1, so the
  mandatory 1879 check did not apply. Footnote 21-2s's reference glyph
  read as a stylized swash "III" easily mistaken for "H"/"II" at a
  glance — resolved to "III Nefi 20:42" by content fit (II Nefi 20 only
  has 34 verses; III Nefi 20 is the chapter this whole passage already
  cites repeatedly; v.42 pairs with the paired Isaías 52:11-15
  citation, matching this footnote's annotated word
  "saldrán"/Isaiah 52:12's "no saldréis apresurados"), independently
  corroborated by Google's own garbled OCR reading ("FI Nefi 20 : 42").
  A genuine 1920-only misprint was caught and preserved as printed per
  rule 32: chapter 22 v.1 prints "sucererá" where 1886 (file 549, book
  page 531) has the correct "sucederá," and the page's own text two
  verses back on page 534 (III Nefi 21:20) already uses the correct
  spelling — confirmed by Google's independent OCR reading the
  identical "sucererá" at the same spot (real evidence it is actually
  printed that way), by a zero-result RAE search, and by zero hits in
  all three local reference corpora against one hit for "sucederá" in
  the Quijote corpus. One rule-7 hyphen rejoin ("aver-"/"güences" ->
  "avergüences"); no rule-8 overflow anywhere else on the page.
  `check_line_wrap.py` and `check_google_crosscheck.py` both flagged
  large discrepancies that turned out to be false positives from the
  same root cause: both scripts' body-text extraction helper stops at
  the first blank line, so a page with a mid-page chapter break (this
  page's CAPÍTULO 22 heading) silently truncates everything after it —
  chapter 22's 24 lines were never actually compared by either script.
  Manually cross-checked chapter 22 against the OCR/Google text
  directly instead; both came back clean, with Google's OCR itself
  corroborating the "sucererá" misprint as noted above. Session B
  independently re-verified all 10 Block 1 entries and body markers
  from fresh crops; no further errors found. Session D
  (`generate_block2.py 535`) surfaced two real, previously-undiagnosed
  bugs in the script itself (not page-specific): the cross-reference
  resolver's book/chapter regex could not handle a citation that
  included its own verse number (e.g. "III Nefi 20:22" instead of bare
  "III Nefi 20"), and `--fix-unresolved` was silently resetting its
  tracked book_id to None on every ordinary wrapped continuation line
  of a multi-line reference, breaking resolution for everything after
  it until the next real book header. Both fixed (the first by
  allowing an optional ":verse" suffix in the regex, the second by
  using the citing entry's own book_id from the already-correct
  footnote index instead of re-deriving it by scanning librodm.txt's
  headers at all, matching what the incremental path already did
  correctly). Re-running `--fix-unresolved` after the fixes resolved
  this page's stuck footnote 3888 (-> 3818, III Nefi 20's own letter p)
  plus five other long-stuck cross-references elsewhere in the
  document; a second run confirmed zero further changes, and
  whole-document rule-31/22/23/verse-indent checks stayed clean
  throughout. Session E: fresh pptext regeneration
  (`report_wsl_20260728d.html`); neither "sucererá" nor chapter 22
  v.6's "fuíste" appeared in the report's spellcheck section at all
  (confirmed via direct standalone aspell testing instead, both
  flagged as unrecognized — matching the already-documented
  pages-469-470 gap where a rare single-occurrence word can go
  unflagged in the full-document run). "sucererá" was added to `errors
  in 1920.txt` (III Nefi 22:1) and, per rule 10, to `permitted
  words.txt` as well. "fuíste" was resolved the opposite way: 1886
  independently prints the identical accented form at the identical
  spot, and RAE's own NGLE (via a WebSearch-sourced @RAEinforma
  citation, section 4.4f) documents "fuiste, viste, dijiste" as
  historically accented forms under the pre-simplification orthography
  — the same category already established in this project for
  "fué"/"vió"/"fuí" — so it was added to `permitted words.txt` only,
  not `errors in 1920.txt`, even though (unlike those three) it has
  zero hits in any of the three local reference corpora. No other
  pptext section produced a hit for this page. Full-document
  footnote-anchor check (max 3896, zero duplicates/out-of-range, only
  the pre-existing 812 gap), a fresh curly-quote character scan of both
  master files, and `check_spaced_punctuation.py`/
  `check_footnote_punctuation.py`/`check_verse_indent.py` (whole
  document) all clean. Page has zero hyphens in its final body text, so
  no dash-check findings. No narrow-space-vs-merge defaults were made
  on this page.


- **2026-07-28e**: Sessions A–E run for page 536 (III Nefi 22:9–17,
  chapter 23:1–5 opens mid-page, footnotes 3897-3904; chapter 22 closes
  and 23 opens within the same book, so no blank line/header needed in
  Block 1 per rule 20 — only the letter reset g-l -> a-b signals it).
  Session A: mandatory i/l/1 check applied to chapter 22's own letters
  i ("Fatigada") and l ("contra") — both confirmed correct against a
  fresh 1879 crop (file 538, book page 530). The same check caught a
  real near-miss on two cross-reference TARGET letters: "h, Véase _,
  III Nefi 15" and "l, Véase _, I Nefi 22" both looked like "i" at a
  first glance, but 1879 reads both as "j" ("see j" in each case), and
  a tight re-zoom of the Spanish glyphs confirmed a hook/descender
  shape matching this page's own "j" label (not the plain dot+stroke
  "i" shape) — corroborated further by content-fit for the I Nefi 22
  target (its own footnote j, "those who fight against Zion shall be
  destroyed," fits v.15's "los que se reunan en contra de ti, caerán"
  far better than footnote i's content). Both corrected to "j" from an
  initial "i" misreading — exactly the failure mode this mandatory
  check exists to catch. Google OCR cross-check
  (`check_google_crosscheck.py`) caught a missed accent Session A's
  first pass had overlooked in bold-face capital type: v.10's "El
  Señor, El que" is actually "Él Señor, Él que" (reverential capital
  pronoun for Deity, accented both times) — confirmed via tight zoom
  after Google's OCR independently read the accent at both spots.
  Two stray printing specks (not real content, both confirmed absent
  in 1886 at the identical spots) were normalized away: v.13 "todos
  .tus hijos" -> "todos tus hijos", v.15 "se'reunan" -> "se reunan".
  One narrow-space-vs-merge default per the editor-guidance rule: v.1
  "quedebeis" (no visible gap) -> "que debeis" (1886 prints it as two
  words at the identical spot, and grammar requires two words) —
  flagged here for the editor per that rule's batching requirement,
  not raised as a blocking question during Sessions A-D. One rule-7
  hyphen rejoin ("dili-"/"gentemente" -> "diligentemente", landing at
  exactly 72 chars including its attached semicolon, so no rule-8
  rebalancing needed); no other rule-8 overflow on the page.
  `check_line_wrap.py` flagged the same mid-page-chapter-break false
  positive already documented for page 535 (txt_body_lines() stops at
  the first blank line, missing chapter 23's 12 lines) — manually
  confirmed the real total (39 body lines) is within 1 of the script's
  own OCR estimate (40), consistent with no reflow. Session B:
  independently re-verified all 8 Block 1 entries and body markers
  from a fresh crop, and redid the mandatory i/l/1 check against a
  fresh 1879 crop — both "Véase j" corrections and the i/l readings
  reconfirmed exactly; no further errors found. Session D
  (`generate_block2.py 536`): all 8 entries resolved cleanly on first
  pass (3898->3702 III Nefi 15j, 3902->237 I Nefi 22j, 3904->682 II
  Nefi 27c), zero unresolved. Session E: fresh pptext regeneration
  (`report_wsl_20260728e.html`). Three flagged words confirmed as
  legitimate archaic/period forms and added to `permitted words.txt`
  only: "acimentaré" (RAE's Tesoro de los diccionarios históricos has
  an entry for "acimentar" = "cimentar"; matches 1886 exactly; modern
  LDS edition uses "cimentaré" without the archaic "a-" prefix),
  "áscuas" (matches 1886's identical accented spelling exactly; local
  corpora only attest the modern unaccented "ascuas"), "debeis"
  (matches 1886's identical unaccented spelling exactly; modern LDS
  edition and RAE both confirm "debéis" is the standard accented form,
  but the 1886 agreement is the deciding evidence, same precedent as
  page 535's "fuíste"). Reading through this page's own Corrections
  log per the mandatory sweep caught one genuine `errors in 1920.txt`
  candidate that Session A's note had only flagged as "preserved, not
  an error": v.17 "no prosperará." followed by lowercase "y tú
  condenarás" is confirmed by pptext's "full stop followed by
  unexpected sequence" check and matches the already-established
  Alma 43:9/48:6/49:3/52:34/57:6 and Helamán 5:2 pattern exactly —
  1886 has a comma at this identical spot, not a period. Added as
  III Nefi 22:17 (punctuation-only, no `permitted words.txt` entry).
  Full-document footnote-anchor check (max 3904, zero duplicates/
  out-of-range, only the pre-existing 812 gap), a fresh curly-quote
  character scan of both master files, and
  `check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py` (whole document) all clean. Page has zero
  hyphens in its final body text, so no dash-check findings.
- **2026-07-28f**: Sessions A–E run for page 537 (III Nefi 23:5–14,
  chapter 24:1–3 opens mid-page, footnotes 3905-3911; page begins
  mid-verse continuing 23:5 from page 536, so no `Página 537` header
  per rule 1, same precedent as pages 535/536; chapter 23 closes and 24
  opens within the same book, so no blank line in Block 1 per rule 20
  — only the letter reset f-c signals it). Session A: no letter on this
  page is i, l, or 1 (own letters c-f/a-c, cross-reference targets u
  and g), so the mandatory 1879 check did not apply; all 7 markers and
  Block 1 entries confirmed via zoomed crops and a content-fit sanity
  check. Two rule-7 hyphen rejoins ("pala-"/"bras" -> "palabras",
  "es-"/"cribieras" -> "escribieras", both staying on their first line
  under 73 chars); numerous rule-31 space-before-colon/semicolon fixes
  and rule-6 double-space-after-punctuation normalizations (this page's
  print consistently does both). One narrow-space-vs-merge default:
  chapter 24 v.1 "templo el Señor" (near-zero gap, "temploel," but
  grammar requires two words) — flagged for the editor per that rule's
  batching requirement. `check_line_wrap.py` flagged the same
  mid-page-chapter-break false positive already documented for pages
  535/536 (stops at the first blank line, missing chapter 24's 14
  lines) — real total (41 lines) within range of the OCR estimate (38)
  once counted back in. Session B: independently re-verified all 7
  Block 1 entries and markers from a fresh crop; no further errors
  found. Session D (`generate_block2.py 537`): 6 of 7 resolved cleanly;
  3908 ("Véase g, Jacob 4; Helamán 14:25-26") came back unresolved due
  to a `generate_block2.py` parsing limitation (a "Véase" cross-
  reference followed by an additional semicolon-separated citation
  confuses the regex) — manually resolved to "Véase 846; Helamán
  14:25-26" (Jacob 4g, confirmed by content fit). Session E: fresh
  pptext regeneration (`report_wsl_20260728f.html`), walked against
  this page's specific line ranges. "há" (v.3 periphrastic future,
  matches 1886's own "há"/"hé" exactly) added to `permitted words.txt`
  alongside the existing "hé" entry. Two genuine 1920-only errors
  confirmed via 1886 + the modern Spanish edition + RAE and added to
  `errors in 1920.txt`: chapter 24 v.1 "vendra" (missing accent, both
  comparison sources have "vendrá"; also added to `permitted
  words.txt`) and "el cuál" (spurious accent on a relative pronoun; RAE
  confirms relative "cual" never takes a tilde). One deviation
  confirmed NOT an error: v.1 "á Quién vosotros buscáis" — 1886 has
  plain lowercase "quien," but pptext's edit-distance check surfaced
  three prior instances of this exact capitalized+accented pattern
  already in the document (lines 23683, 23703, 23715, all relative
  pronouns referring to Deity), confirming a genuine, consistent 1920
  house-style convention (the same reverential-pronoun elevation
  already established for "Él" on page 536) rather than an isolated
  misprint — preserved as printed. "ésto" (v.12) is an already-
  established `permitted words.txt` entry (13 prior occurrences), no
  new action needed. Full-document footnote-anchor check (max 3911,
  zero duplicates/out-of-range, only the pre-existing 812 gap), a
  fresh curly-quote scan, and `check_spaced_punctuation.py`/
  `check_footnote_punctuation.py`/`check_verse_indent.py` (whole
  document) all clean.
- **2026-07-28g**: Sessions A–E run for page 538 (III Nefi 24:3–16,
  footnotes 3912-3917, continuing chapter 24's own letters d-i; page
  begins mid-verse continuing 24:3 from page 537, so no `Página 538`
  header per rule 1, same precedent as pages 535-537; no chapter or
  book boundary occurs on this page, so no blank line in Block 1).
  Session A: mandatory 1879 check applied to letter 24i (3917, "libro
  de memoria") — chapter_map.csv maps III Nefi 24 to 1879 file page
  540, with the matching content (Malachi 3:16) continuing onto file
  page 541; a fresh zoomed crop there confirms the classic "i" shape
  (short stroke, separated dot) both on the body-text superscript and
  in 1879's own page-541 footnote footer, which also corroborates
  letters d-h by content and letter match against its own d-g footer
  (page 540) and h/i footer (page 541). No rule-7 hyphen rejoins occur
  anywhere on this page. Numerous rule-31 space-before-semicolon/colon
  fixes and rule-6 double-space normalizations (same recurring pattern
  as prior pages). A recurring stray ink speck after "á" and before
  "Dios" (v.8, v.14) was checked against this page's Google OCR text
  (`google_text_1920/page_0560.txt`), which reads plain "á Dios" both
  times with no mark — treated as a print speck per rule 36's
  principle, not logged as an error. Session B: independently
  re-verified all 6 Block 1 entries and markers from a fresh crop, plus
  an independent re-run of the mandatory 24i check against a second,
  differently-cropped 1879 page-541 image — same "i" conclusion, no
  further errors found. Session D (`generate_block2.py 538`): all 6
  entries resolved cleanly on first pass, including 3914's "Véase w,
  III Nefi 20" cross-reference resolving to 3825. Session E: fresh
  pptext regeneration (`report_wsl_20260728g.html`), walked against
  this page's specific line ranges. One genuine 1920-only error
  confirmed via a fresh 1886 comparison (pages_1886/page_0553.png, book
  page 535) and added to `errors in 1920.txt`: v.15 "orgullosos. sí" (a
  period where 1886 prints a comma, same pattern as the already-
  documented III Nefi 22:17 "prosperará." case; punctuation-only, no
  `permitted words.txt` entry needed). A second suspected error, v.16
  "quc" for "que" (misread as a crossbar-less "c" at zoom), was logged
  the same way but then **reversed after the user's own direct look at
  the page** confirmed the letter's crossbar is present, just faint —
  the word is genuinely "que" as printed. Fixed in the body text; the
  `errors in 1920.txt`/`permitted words.txt` entries were removed
  (2026-07-28g, same-day correction) — see page 538's Corrections log
  for the full account, including the reminder that Google's OCR and
  1886 both already read "que" at the time and should have prompted
  more skepticism before logging a misprint on a common function word.
  No narrow-space-vs-merge defaults occurred on this page.
  Full-document footnote-anchor check
  (max 3917, zero duplicates/out-of-range, only the pre-existing 812
  gap), a fresh curly-quote scan, and `check_spaced_punctuation.py`/
  `check_footnote_punctuation.py`/`check_verse_indent.py` (whole
  document) all clean.

- **2026-07-28h**: Sessions A–E run for page 539 (III Nefi 24:17-18,
  25:1-6, 26:1-2, footnotes 3918-3926: chapter 24's final letter j,
  chapter 25's full a-g set, chapter 26's opening letter a; page opens
  on a fresh verse — v.17 starts cleanly, not mid-sentence — so
  `Página 539` IS included per rule 1, immediately followed by body
  text with no blank line, matching the pattern of pages 530-536
  rather than page 538's mid-verse-continuation precedent). Chapter 24
  (Malachi 3) ends at v.18 on this page, matching Malachi 3's own
  18-verse length; chapter 25 (Malaquías 4) begins and ends entirely
  on this page, with its "(Véase Malaquías 4.)" subtitle printed on
  the SAME line as "CAPÍTULO 25." in the image, transcribed as one
  line per rule 6; chapter 26 begins with only its opening verse pair
  reached so far. Session A: rule-7 hyphen rejoin with rule-8
  rebalancing on chapter 26 v.2's "ob-"/"tenido," (rejoining to
  "obtenido," would hit exactly 73 chars on the first line, so the
  whole word moved to the next line instead). Two items preserved as
  printed per rule 32 for Session E: v.18 "dicerniréis" (missing the
  "s" a modern "discerniréis" would have) and chapter 26's 26a citation
  "III Nefi 24:25" (chapter 24 on this same page is confirmed to end
  at v.18, so this citation points to a verse that doesn't exist in
  this chapter as transcribed). Session B: independently re-verified
  all 9 Block 1 entries/markers from a fresh crop; ran the mandatory-
  adjacent 1879 check on 24j (visually similar to "i", though not
  itself in the mandatory i/l/1 set) — 1879 file page 541's own
  footnote footer explicitly reads "j, Doc. and Cov. 101:3." with a
  clearly italic "j" superscript on the matching body-text word
  ("make up my jewels"), definitively confirming both the letter and
  the target content match this page's own 24j entry exactly. Session
  D (`generate_block2.py 539`): all 9 entries resolved cleanly, no
  cross-references to chase. Session E: fresh pptext regeneration
  (`report_wsl_20260728h.html`). "dicerniréis" checked against 1886
  (pages_1886/page_0553.png, book page 537), which ALSO prints
  "dicerniréis" — not a 1920-only error; further confirmed as a real
  archaic form via RAE's Tesoro de los diccionarios históricos
  (has a "dicernir" entry) and the modern official Spanish edition
  (3 Nefi 24:18, "discerniréis" — the corrected modern spelling),
  added to `permitted words.txt` only. "Elías" (ordinary proper name)
  also added to `permitted words.txt`. The 26a "III Nefi 24:25"
  citation wasn't resolvable from this session's own 1879 look (found
  no footnote letter at all at v.2), but **the editor's own direct
  examination of 1879 resolved it after the fact**: 1879 reads
  "III Nefi 24,25" (comma) at footnote a, citing the whole of chapters
  24-25 (the Malachi 3-4 passages just quoted) rather than a single
  verse — fits v.2's "these scriptures ye had not obtained" far better
  thematically (1886 has no footnote apparatus at all, so it isn't a
  comparison point here). 1920 alone prints a colon in place of the
  comma, producing an invalid chapter:verse cite to a verse that
  doesn't exist (chapter 24 ends at v.18 on this page). Genuine
  1920-only error, added to `errors in 1920.txt` (punctuation in a
  citation, no `permitted words.txt` entry needed).
  No narrow-space-vs-merge defaults occurred on this page.
  Full-document footnote-anchor check (max 3926, zero
  duplicates/out-of-range, only the pre-existing 812 gap), a fresh
  curly-quote scan, and `check_spaced_punctuation.py`/
  `check_footnote_punctuation.py`/`check_verse_indent.py` (whole
  document) all clean.

- **2026-07-29**: Sessions A–E run for page 540 (III Nefi 26:3-14,
  footnotes 3927-3943, 17 letters b-r, continuing chapter 26 from page
  539 — no new chapter heading on this page). Page opens on a fresh
  verse (v.3), so `Página 540` IS included per rule 1, immediately
  followed by body text with no blank line. Session A: no rule-7 hyphen
  splits anywhere on the page. Several swash cross-reference letters in
  the footnote block were visually ambiguous (a bare diagonal stroke
  with no dot/curve, and a loop-with-tail easily mistaken for "o") —
  resolved via the mandatory/discretionary 1879 cross-check
  (chapter_map.csv: III Nefi 26 → 1879 file pages 542-543, book pages
  534-535): 26b/26h's target letter is "f" ("b, see f, III. Nep. 25.";
  "h, see f, I. Nep. 1."); 26i/26q's target letter, initially misread
  as "o," is actually "g" ("i, see g."; "q, see g, III. Nep. 17.");
  26r's target letter is "w" ("r, see w, III. Nep. 19."), confirmed
  despite the glyph being obscured by the "Digitized by Google"
  watermark in the 1920 scan. Footnote 26c: 1920 prints "Isaías 24:17;"
  wrapping to "20; 24:1-4;" (a genuine semicolon, not a hyphen, zoom-
  confirmed) — 1879 shows this as one consecutive range ("Isaiah
  24:17-20"), so per rule 23 it's transcribed as "24:17-20" using 1879
  as evidence of the intended range; "24:1-4" stays a separate
  semicolon-delimited item, matching how both editions keep it apart.
  Footnote 26d: two consecutive-verse pairs ("27:14, 15" and "9:13,
  14") converted to hyphenated ranges per rule 23; "16:1, 2, 10"
  converted to the mixed form "16:1-2,10" per rule 25. Two suspected
  misprints preserved as printed per rule 32: v.5 "esixtía" (x/s
  transposed) and v.8 "proninciadas" (missing "u"). v.14 has a
  noticeably wide gap between "que" and "ministró," normalized to a
  single space per rule 6; 1886 shows a different anomaly at the same
  spot ("que que ministró," a duplicated "que"), suggesting a shared
  source-level defect (possibly a dropped subject word) that neither
  edition's print resolves — flagged for the editor's awareness only,
  no `errors in 1920.txt` entry since no correction could be
  confidently supplied. Session B: independently re-verified all 18
  Block 1 entries and all 17 `[N]` body markers from a fresh crop; ran
  the mandatory 1879 check for this chapter's own "i" and "l" letters
  (both in the i/l/1 mandatory set) — 1879 file page 542 shows "i, see
  g." with the classic short-stroke-plus-dot "i" shape, and file page
  543 shows "l, all on the plates of Nephi..." with a tall unbroken
  curve, no dot — both confirmed correctly identified. Session D
  (`generate_block2.py 540`): all 17 entries resolved cleanly,
  including 26r→"w" resolving to III Nefi 19w (sequential 3805), whose
  own citation text ("III Nefi 17:16-17;26:14;28:14,16") cites this
  very chapter's v.14 — strong corroboration the letter resolution was
  correct. Session E: fresh pptext regeneration
  (`report_wsl_20260729.html`). "esixtía" confirmed a genuine 1920-only
  error via 1886 (pages_1886/page_0554.png, book page 536: "existía")
  and RAE (no entry for "esixtía"); not flagged by pptext's spellcheck
  section on this run, so no `permitted words.txt` entry added (same
  no-op precedent as "Jesu Cristo") — added to `errors in 1920.txt`
  only. "proninciadas" confirmed a genuine 1920-only error the same way
  via 1886 (pages_1886/page_0555.png, book page 537: "pronunciadas")
  and RAE (no entry); IS flagged by pptext, so added to both
  `permitted words.txt` and `errors in 1920.txt`. Both words returned
  zero hits in all three reference corpora (uninformative, not
  contradicting — the correctly-spelled forms are also rare/absent in
  those corpora). Full-document footnote-anchor check (max 3943, zero
  duplicates/out-of-range, only the pre-existing 812 gap), a fresh
  curly-quote scan, and `check_spaced_punctuation.py`/
  `check_footnote_punctuation.py`/`check_verse_indent.py` (whole
  document) all clean. No narrow-space-vs-merge defaults occurred on
  this page.

- **2026-07-29**: Sessions A–E run for page 541 (III Nefi 26:15-21,
  footnotes 3944-3952, chapter boundary to III Nefi 27:1-5, footnotes
  3953-3956 — 13 footnote letters total: chapter 26's continuing
  s-through-2a, then chapter 27's a-d; no subtitle line on the chapter
  27 opening, checked directly against the image). Page opens on a
  fresh verse (v.15), so `Página 541` IS included per rule 1,
  immediately followed by body text with no blank line. Session A: two
  rule-7 hyphen rejoins ("levan-tado" → "levantado" in v.15; "bauti-
  zando" → "bautizando" in III Nefi 27:1), both under the 73-char cap
  with no rebalancing needed; one rule-8 rebalance in v.16 once
  [3945] pushed a line to 73 chars ("abrían" moved to the next line).
  v.4 "A lo que el Señor" zoomed and confirmed a genuine bare
  unaccented "A" in the 1920 print (ordinary usage, not an error). This
  page's continuing chapter-26 footnote block sits in the same heavily
  stylized swash font flagged on pages 451/540, and several letters
  were initially misread from the 1920 image alone before a fresh,
  tighter (16x) zoom — and, for one letter, the mandatory 1879 check —
  resolved them, all confirmed against 1879 (chapter_map.csv: III Nefi
  26 → 1879 file page 543, book page 535; III Nefi 27 → 1879 file page
  544, book page 536), which lists the exact same sequence/content in
  the same order: entry 2's current letter is literally "i"-shaped in
  the 1920 image (triggering the mandatory i/l/1 check) but is "t" per
  1879 and alphabetical position; entry 3's target (initially "e") is
  "c"; entry 5's target (initially "v") is "y" (has a descender the
  1920 "v" lacks); entry 6's current letter (initially "z") is "x"
  (unmistakable crossed strokes once zoomed, vs. the closed-loop "z"
  confirmed separately at entry 8). Every target's content-fit against
  its 1920 body-text anchor word was independently confirmed against
  the 1879 English wording (e.g. "s" lands on "curado"/"healed all
  their sick"; full entry-by-entry list checked, all fit). The
  chapter-26 extension letter ("26-2a") is formatted per the document's
  own established "2a"/"2b" convention (grep-confirmed against existing
  `librodm_foot.txt` entries), regardless of the source glyph's exact
  visual form. Footnote y (3950): "IV Nefi 1:2,3,25,26" is two separate
  consecutive pairs (2-3 and 25-26, not one continuous span), converted
  to the mixed form "1:2-3,25-26" per rule 25. No suspected misprints
  and no narrow-space-vs-merge candidates found on this page. Session
  B: independently re-verified all 13 Block 1 entries and all 13 `[N]`
  body markers from a fresh crop; ran the mandatory 1879 check for
  entry 2 (t) using a fresh, independently-pulled 1879 crop (not reused
  from Session A) — confirmed unambiguous crossbarred "t" in ordinary
  1879 italic type, not the "i"-looking 1920 swash glyph. Session D
  (`generate_block2.py 541`): all 13 entries resolved cleanly with no
  unresolved cross-references; footnote 3945 (26t → w) resolved to
  3805 (III Nefi 19w), the same target page 540's 26r independently
  resolved to — cross-confirms both pages' letter resolutions. Session
  E: fresh pptext regeneration (`report_wsl_20260729b.html`) — zero new
  spellcheck/edit-distance hits, zero footnote-anchor gaps/duplicates
  in the new 3937-3956 range (the two-bucket "anchor" vs. "footnote"
  split briefly makes 3936/3950 look missing from one list, but both
  are accounted for in the other — a start-of-line-marker quirk, not a
  real gap), zero curly quotes, zero new hyphen-compound words, and a
  clean full-document run of `check_spaced_punctuation.py`/
  `check_footnote_punctuation.py`/`check_verse_indent.py`. No new
  `permitted words.txt` or `errors in 1920.txt` entries needed. No
  narrow-space-vs-merge notes to surface this session.

- **2026-07-29**: Sessions A–E run for page 542 (III Nefi 27:6-17,
  footnotes 3957-3961 — 5 footnote letters, all continuing chapter 27's
  lettering from page 541, e-i; no chapter boundary, no subtitle; verse
  17 cut off mid-sentence at "será él que yo", continues on page 543).
  Page opens on a fresh verse (v.6, chapter 27 already opened on page
  541), so `Página 542` is included per rule 1, immediately followed by
  body text with no blank line. Session A: one rule-7 hyphen rejoin
  ("habéis edi-" / "ficado" → "edificado" in v.9, appended to the first
  line at 67 chars, under the cap, no rebalancing needed); one rule-6
  justification-widened gap normalized to a single space (v.8 "nombre?
  Porque,", no exception, not logged as an error); no narrow-space-vs-
  merge candidates and no suspected misprints (rule 32) found. All 5
  footnote letters (e-i) were identified via same-page swash-glyph
  comparison against the fn block's own labeled letters (e: teardrop/
  comma shape anchored at "caerán" v.11; f: slanted stroke at "hubiere"
  v.14; g: solid oval/loop, the letter that wraps to the next line
  before "Levantados de la tumba", at "fueren" v.14; h: short stroke
  with a bump at "bautice" v.16; i: short stroke with a separated dot,
  the classic i-shape, at "perseverare" v.16), then confirmed via the
  mandatory 1879 check for "i" (in the i/l/1 set per Section 8):
  chapter_map.csv's III Nefi 27 → 1879 file page 544 only carries that
  page's own a-d entries, so the matching e-i block is on the next 1879
  file page (545, book page 537) — read directly as "e, see k, I. Nep.
  15. f, ver. 15. I. Nep. 19:10. III. Nep. 28:6. g, raised from the
  grave. h, see u, II. Nep. 9. i, see h, II. Nep. 31.", an exact
  content-for-content match to all five 1920 entries in the same
  alphabetical order. Content-fit: f/g both gloss "levantado"/"elevados"
  by cross-referencing this same page's own v.15 ("Por cuyo motivo he
  sido levantado") and defining "elevados" as "levantados de la tumba"
  (raised from the grave/tomb); i's target (II Nefi 31, substantively
  about enduring to the end and baptism) fits "si perseverare hasta el
  fin" extremely well. Session B: independently re-verified all 5 Block
  1 entries and all 5 `[N]` body markers from a fresh crop; re-ran the
  mandatory 1879 check for "i" using a second, independently-pulled
  crop of 1879 file page 545 (not reused from Session A) — confirmed
  the same reading. Session D (`generate_block2.py 542`): all 5 entries
  resolved cleanly with no unresolved cross-references. Session E:
  fresh pptext regeneration (`report_wsl_20260729c.html`) — zero new
  spellcheck/edit-distance hits in the new page's line range (all hits
  landed in the pre-existing, already-benign "short lines check"
  category, expected for this project's multi-line verse-wrapping
  format), zero footnote-anchor gaps/duplicates introduced by this page
  (a whole-document `\[(\d+)\]` scan found exactly one gap, footnote
  812, the long-since-documented Jacob 2:15 case — unrelated to this
  page), zero curly quotes, and a clean full-document run of
  `check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py`. No new `permitted words.txt` or `errors in
  1920.txt` entries needed. No narrow-space-vs-merge notes to surface
  this session. One Google-text cross-check candidate (the em-dash in
  v.8 "iglesia;—si fuere") was Google's own OCR dropping the dash
  character, not a letter misread — confirmed genuine via the zoom
  already done at transcription time.
- **2026-07-29**: Sessions A–E run for page 543 (III Nefi 27:17
  cont.-30, footnotes 3962-3974 — 13 footnote letters, j-v, continuing
  chapter 27's lettering from page 542; no chapter boundary, no
  subtitle; page opens mid-sentence on v.17's tail ("separaré y
  arrojaré al fuego...") and v.30 is cut off mid-sentence at
  "generación; sí,", continues on page 544). Page continues a verse
  already in progress, so per rule 1 `Página 543` is followed
  immediately by body text with no blank line. Session A: two rule-7
  hyphen rejoins (v.19 "arrepenti-"/"miento" → "arrepentimiento",
  appended to the first line at 68 chars; v.30 "pleni-"/"tud," →
  "plenitud,", appended to the first line at 65 chars; neither needed
  rebalancing); a rule-6 wide gap with no punctuation in v.18
  ("hombres" / "Por esto", normalized to one space, no period
  inserted); no narrow-space-vs-merge candidates found. One suspected
  misprint (rule 32) confirmed genuine and formalized into `errors in
  1920.txt` this session: v.18's missing period after "hombres" —
  1886 (file page 557/book page 539) clearly prints "hombres.  Por
  esto..." with a period, while 1920 has only a wide gap and no
  punctuation at all. All 13 footnote letters were confirmed via
  same-page glyph comparison against the fn block's own labeled
  letters, with the mandatory 1879 check run for the current-chapter
  letter "l" (3964, in the i/l/1 set per Section 8): chapter_map.csv's
  III Nefi 27 → 1879 file page 544 only carries a-d, so the matching
  j-n block is on the next 1879 file page (545, book page 537) — read
  directly as "j, see k, I. Nep. 15. k, Alma 11:37. See r, Alma 7. l,
  see h, II. Nep. 31. m, see u, II. Nep. 9. n, see y, III. Nep. 9.",
  an exact content-for-content match to 1920's j/k/l/m entries,
  confirming "l" (not an i/1 misread). Two cross-reference
  target-letter discrepancies were noted and preserved as printed
  (expected translation-order divergence per rule 26, not logged as
  errors, flagged for the editor): 27r's target reads clearly as
  "Véase i, II Nefi 29" in 1920 (independently zoom-confirmed twice,
  satisfying the mandatory i/l/1 check) vs. 1879's "see j" for the
  same citation — content-checked against II Nefi 29's own
  already-transcribed Block 1, where 1920's implied target (29i →
  "Véase c, II Nefi 27") is a weaker thematic fit for v.25's "por los
  libros...será juzgado este pueblo" than 1879's likely target (29j →
  cites Revelation 20:12, the "judged out of the books" passage) —
  neither reading is implausible on its own, so preserved as printed
  rather than resolved; and 27n's target ("Véase v, III Nefi 9" vs.
  1879's "see y"), not independently investigated further since v/y
  are outside the mandatory set. Rule-23 verse-range formatting
  applied to 27u ("I Nefi 12:9,10" → "9-10") and 27v ("III Nefi 14:7,8"
  → "7-8"), both consecutive-verse citations; 27p's non-consecutive
  "16,18" stayed comma-separated per rule 24. Session B: independently
  re-verified all 13 Block 1 entries and all 13 `[N]` body markers
  from a fresh crop; re-ran the mandatory 1879 check for "l" using a
  second, independently-pulled crop of 1879 file page 545 (not reused
  from Session A) — confirmed the same reading. Session D
  (`generate_block2.py 543`): all 13 entries resolved cleanly with no
  unresolved cross-references. Session E: fresh pptext regeneration
  (`report_wsl_20260729d.html`) — zero new spellcheck/edit-distance
  hits in the new page's line range (all hits landed in the
  pre-existing, already-benign "short lines check" category, plus one
  expected "paragraph ends in comma" hit at the page's own current
  cut-off point, normal for the currently-latest transcribed page),
  zero footnote-anchor gaps/duplicates introduced by this page (a
  whole-document `\[(\d+)\]` scan found exactly one gap, footnote 812,
  the long-since-documented Jacob 2:15 case — unrelated to this page),
  zero curly quotes, and a clean full-document run of
  `check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py`. The v.18 missing-period misprint (above)
  was formalized into `errors in 1920.txt` this session; no
  `permitted words.txt` entry needed (punctuation, not spelling). No
  other new `permitted words.txt` entries needed. No narrow-space-vs-
  merge notes to surface this session.
- **2026-07-29**: Sessions A–E run for page 544 (III Nefi 27:30
  cont.-33, then CAPÍTULO 28 begins mid-page through v.6, footnotes
  3975-3980 — six footnote letters: w, x, y, z, 2a continuing chapter
  27's lettering from page 543 for v.32-33, then chapter 28 resets to
  "a" for v.3; no subtitle at the chapter 28 opening, checked directly
  against the image; page opens mid-sentence continuing v.30 from page
  543 and is cut off mid-sentence at v.6 "...deseó mi muy amado",
  continuing on page 545). Per rule 1, `Página 544` is followed
  immediately by body text with no blank line. Session A: no rule-7
  hyphen rejoins needed (no line-end hyphens on this page); several
  rule-6 wide-gap normalizations (a period or colon followed by a
  double/triple space, all collapsed to one) and matching rule-31
  space-before-punctuation fixes. Footnote lettering confirmed via
  strict alphabetical sequencing (rule 13) plus same-page glyph checks
  for the first and fourth letters (w, z); none of this page's letters
  are i/l/1, so the mandatory 1879 check did not apply. The "2a"
  cross-reference target ("Véase 2a, II Nefi 9") follows the
  established two-letter-code convention (rule 16); chapter 28's new
  footnote "a" cites IV Nefi 1:14, a strong content match for v.3's
  "setenta y dos años". Google-text cross-check
  (`check_google_crosscheck.py 544`) caught one genuine transcription
  error: v.32 "hijo de perdición" had been typed with an accent that
  the image doesn't show — corrected to "perdicion". Session B:
  independently re-verified all 6 Block 1 entries and all 6 `[N]` body
  markers from a fresh crop; no i/l/1 letters present, so no 1879
  re-check applied. Session D (`generate_block2.py 544`): all 6
  entries resolved cleanly, no unresolved cross-references. Session E:
  fresh pptext regeneration (`report_wsl_20260729e.html`) surfaced two
  spellcheck-suspect words from this page, both investigated with the
  full mandatory research pass (1886 image + RAE DLE + modern Spanish
  edition + local reference corpora) despite 1886 agreeing with 1920
  in both cases, and both resolved as genuine 1920 errors on the
  strength of that independent evidence rather than the 1886 match
  alone: v.30 "recocija" (RAE has no entry for "recocijar" at all;
  modern edition and all three corpora point unanimously to
  "regocija", 26 clean corpus hits vs. 0) and v.32 "perdicion" (RAE
  requires the accent; the document itself already uses "perdición"
  accented elsewhere; 16 clean corpus hits for the accented form vs. 0
  unaccented, ignoring one OCR-noise hit). Both added to `errors in
  1920.txt` (inserted in book/chapter/verse order right after the
  existing III Nefi 27:18 entry, not appended to the file's end) and
  to `permitted words.txt`. v.31 "supierais" (missing accent vs.
  1886's "supiérais") was left as a routine Corrections-log note only,
  per rule 11, since pptext's spellcheck doesn't flag it at all —
  no independent signal beyond the bare 1886 divergence. Whole-document
  sweep clean: `check_spaced_punctuation.py`/
  `check_footnote_punctuation.py`/`check_verse_indent.py` all clean
  across `librodm.txt`/`librodm_foot.txt`; a full `\[(\d+)\]` anchor
  scan found zero duplicates and exactly one gap (footnote 812, the
  long-since-documented Jacob 2:15 case, unrelated to this page); zero
  curly quotes. No narrow-space-vs-merge candidates on this page.
- **2026-07-29**: Sessions A–E run for page 545 (III Nefi 28:6
  cont.-17, continuing the chapter 28 opening from page 544, footnotes
  3981-3994 — fourteen footnote letters b through o, continuing
  chapter 28's lettering from page 544 which ended at "a"; page opens
  mid-sentence "Juan, quién me acompañó..." and is cut off mid-verse
  at v.17 "...no lo sé;", continuing on page 546). Per rule 1, `Página
  545` is followed immediately by body text with no blank line.
  Session A: five rule-7 hyphen rejoins (padeceréis, completa,
  palabras, transportados, permanecieron — the last two both land the
  merged line at exactly the 72-char cap); rule-31 space-before-
  semicolon cleanup applied throughout (this page's print consistently
  sets a space before every semicolon). Two notable findings, both
  investigated to a confirmed conclusion and logged in `errors in
  1920.txt`: (1) footnote letter "e" is present in the body text
  (v.7, "venga") but its own "e," marker is entirely missing from the
  printed footnote block — the citation text runs on directly after
  "d"'s citation with no letter, comma, or other signal of a new
  entry; confirmed via 1879 (page_0547.png/page_0548.png), which
  prints this as its own separate entry, "e, III. Nep. 20:22. 21:25."
  (1920 itself also drops the ":22" verse number, so Block 1 entry
  28e was written as "III Nefi 20; 21:25" per rule 32, matching what
  1920 actually prints rather than 1879's fuller citation); (2) v.15
  "para poder. contemplar" has a genuine extraneous period
  mid-sentence — initially suspected as a stray speck, but the Google
  OCR cross-check independently transcribed a punctuation mark at the
  same spot (as a comma, though direct zoom confirms it's a period —
  round, baseline-level, matching this page's other sentence-ending
  periods), and 1886 (page_0560.png) prints "para poder contemplar"
  with no mark at all, confirming a 1920-only error. Footnote
  lettering confirmed via strict alphabetical sequencing (rule 13) and
  near-verbatim content/letter parallelism with the 1879 edition for
  this entire page. Mandatory 1879 check for letter "l" (v.13,
  "fueron"): 1920 glyph is ambiguous at zoom (could read as "i"), but
  "i" was already used earlier on the page (v.9) so alphabetical
  sequencing requires "l"; confirmed via 1879's clear continuous
  sloping stroke (matching "l", not "i"'s short-stroke-plus-dot).
  Session B: independently re-verified all 14 Block 1 entries and all
  14 `[N]` body markers from a fresh crop, plus an independent
  re-check of the 1879 "l" evidence. Session D (`generate_block2.py
  545`): all 14 entries resolved cleanly, no unresolved
  cross-references. Session E: fresh pptext regeneration
  (`report_wsl_20260729f.html`) — no spellcheck/edit-distance hits in
  this page's line range; footnote-check anchor/footnote buckets
  fully consistent with a whole-document `\[(\d+)\]` scan (zero
  duplicates, only the long-documented footnote-812 gap); short-lines/
  dash-check/special-situations hits in this page's range all matched
  established false-positive categories. Whole-document sweep clean:
  `check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py`, zero curly quotes. Neither of this page's
  two `errors in 1920.txt` entries needed a `permitted words.txt`
  companion (both structural/punctuation, not spelling). No
  narrow-space-vs-merge candidates on this page.

- **2026-07-29**: Sessions A-E run for page 546 (III Nefi 28:18-30,
  continuing chapter 28 from page 545 which ended mid-verse at v.17;
  footnotes 3995-4002, eight footnote letters p through w, continuing
  chapter 28's lettering from page 545 which ended at "o"; page opens
  with the start of a new verse number (v.18, "18. Solo sé..."), not
  a chapter heading or mid-verse continuation -- confirmed via
  precedent (pages 530/535/542) that this convention also gets no
  blank line after the `Página N` line, same as a mid-verse
  continuation). Session A: two rule-7 hyphen rejoins ("minis-"/
  "trado" -> "ministrado", v.26, landing at exactly 72 chars with the
  [4000] marker and attached semicolon; "Gen-"/"tiles" -> "Gentiles",
  v.27); four rule-6 wide-gap normalizations ("iglesia.  Y", "tierra,
  pero", "convirtieron  al", "hallarán  entre"); rule-31 space-
  before-punctuation cleanup throughout (semicolons and one colon).
  One rule-8 rebalance needed after the [4001]/[4002] marker insertions
  pushed a line to 73 chars (v.29, moved "halla" to the start of the
  next line). Three genuine 1920-only misprints found this session, all
  confirmed against 1886 (pages_1886/page_0560.png book p.541 for
  v.18-22, page_0561.png book p.543 for v.23-36) and logged in `errors
  in 1920.txt`: (1) v.25 "hombres" printed where "nombres" (names) is
  required by both grammar and 1886 -- Mormon explains he was going to
  write the *names* of those who would never taste death, corroborated
  by this verse's own footnote t (III Nefi 19:4, the chapter naming the
  twelve disciples); (2) v.30 "cualqiuer" (i/u transposed) for
  "cualquier", confirmed via 1886 and zero attestation in any of the
  three reference corpora versus 226+69+9 hits for the correct
  spelling; (3) v.28 "concerán" missing the "o" of "conocerán",
  confirmed via 1886, this page's own correctly-spelled "conocerán" two
  lines earlier in v.27, and independently by the Google OCR cross-
  check reading the word the same abbreviated way. A fourth
  discrepancy (second "Judios" in v.28 missing its accent, present on
  the first "Judios" two words earlier) was noted but NOT logged as an
  error per rule 11's missing-accent carve-out. Footnote lettering
  confirmed via strict alphabetical sequencing (rule 13); no i/l/1
  letters anywhere on the page (own lettering or cross-reference
  targets). Session B: independently re-verified all 8 Block 1 entries
  and all 8 `[N]` body markers from a fresh crop. Session C
  (`insert_body_text.py 546`): body text and 8 Block 1 entries
  inserted cleanly. Session D (`generate_block2.py 546`): all 8
  entries resolved cleanly, no unresolved cross-references -- but
  spot-checking the resolved targets surfaced a fourth genuine error:
  entry 28q ("Véase v, III Nefi 9") resolves to a weak content-fit
  target (the "other sheep" passage) for what it annotates
  ("recibieron [Espíritu Santo]", v.18) -- the same v/y cross-reference
  letter ambiguity pattern already documented for footnote 27n on an
  earlier page. Confirmed via 1879 (pages_1879/page_0548.png): 1879
  explicitly prints "q, see y, III. Nep. 9." (not "v"), and III Nefi
  9's own letter y is a Holy-Ghost/baptism-themed citation chain, a
  strong fit. The 1920 glyph itself is unambiguously "v" at zoom, so
  this is a genuine cross-reference-letter misprint, not a
  transcription misread; preserved as printed ("v") in Block 1 per
  rule 32 and logged in `errors in 1920.txt`. Session E: fresh pptext
  regeneration (`report_wsl_20260729g.html`). Spellcheck flagged
  "concerán", "cualqiuer" (both already-confirmed errors above) and
  "Judios" (missing-accent variant, not an error) -- all three added
  to `permitted words.txt` per rule 10. Footnote check: whole-document
  scan confirms zero duplicates, last number 4002, and the only gap
  remains the long-documented footnote 812. Short-lines/dash-check/
  special-situations hits in this page's range all matched established
  false-positive categories. Whole-document sweeps clean:
  `check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py`, zero curly quotes. No narrow-space-vs-merge
  candidates on this page.
- **2026-07-29**: Sessions A-E run for page 547 (III Nefi 28:31-40,
  continuing chapter 28 from page 546 which ended mid-verse at v.30;
  footnotes 4003-4011, nine footnote letters x, y, z, 2a-2f, continuing
  chapter 28's lettering from page 546 which ended at "w"; page opens
  with the start of a new verse number (v.31, "31. Por lo tanto..."),
  not a chapter heading or mid-verse continuation -- confirmed via
  precedent (pages 530/535/542/546) that this convention also gets no
  blank line after the `Página N` line). Session A: two rule-7 hyphen
  rejoins ("rea-"/"lizadas" -> "realizadas", v.31, landing at 69 chars
  with the [4003] marker; "relativa-"/"mente" -> "relativamente", v.36,
  67 chars) plus one hyphen rejoin ("2atrans-"/"portados") that did NOT
  fit on its original line even before rejoining (74 chars with the
  [4006] marker), so the whole rejoined word moved to the start of the
  next line per rule 7, which then needed its own rule-8 rebalance (83
  chars once the second half's text was appended, "purificados" moved
  down again, landing at 71 chars); rule-31 space-before-punctuation
  cleanup throughout (semicolons and one question mark). A discretionary
  (non-mandatory, not i/l/1) footnote-letter check: the second footnote
  letter (v.33, "y, III Nefi 26:6-12") looked more like "v" than "y" in
  the swash font at normal zoom; confirmed as "y" via 1879
  (pages_1879/page_0549.png, "y, III. Nep. 26:6-12", unambiguous serif
  italic) and by strict alphabetical sequencing (x, y, z, 2a...), which
  a "v" reading would have broken. Three genuine 1920-only misprints
  found, all confirmed against 1886 (pages_1886/page_0561.png book
  p.543 for v.31-35, page_0562.png book p.544 for v.36-40) and logged
  in `errors in 1920.txt`: (1) v.31 "aparacer" for "aparecer" (a/e
  swap); (2) v.32 "juico" for "juicio" (missing second "i"); (3) v.40
  "jucio" for "juicio" (i/c transposed) -- the same underlying word
  misprinted two different wrong ways nine lines apart on the same
  page, ruling out a shared deliberate spelling. All three were also
  independently caught by the Google OCR cross-check
  (`check_google_crosscheck.py 547`), which read the same three
  misspellings from the PDF's own text layer. A fourth Google-crosscheck
  candidate (v.35, an apparent period between "haber" and "nacido" at
  20x zoom) was investigated and resolved as a false alarm: a 30-40x
  re-zoom showed the "dot" is the ball-terminal serif on the arm of the
  bold-face "r" ending "haber", not a separate mark -- Google's silent
  "nohabernacido" reading (no period) was the correct signal, matching
  1886's own "no haber nacido" with no stray punctuation. A fifth
  candidate (a stray comma/apostrophe-shaped mark at the very start of
  the "ni las palabras" line, v.34) was confirmed present in the print
  and corroborated by Google's OCR, but serves no grammatical function
  and was treated as print debris, not transcribed, consistent with
  this page's other unexplained isolated dots. Session B: independently
  re-verified all 9 Block 1 entries and all 9 `[N]` body markers from a
  fresh crop. Session C (`insert_body_text.py 547`): body text and 9
  Block 1 entries inserted cleanly. Session D (`generate_block2.py
  547`): all 9 entries resolved cleanly; content-fit check passed for
  both cross-references (28x "Véase w" -> 4002, this chapter's own
  great-and-marvellous-works verses, fits v.31; 28-2c "Véase d" -> 3983,
  this chapter's recurring three-Nephites citation chain, fits v.37's
  bodily-change-avoiding-death-pains theme). Session E: fresh pptext
  regeneration (`report_wsl_20260729h.html`). Spellcheck flagged
  "aparacer"/"juico"/"jucio" (all three already-confirmed genuine 1920
  errors, logged above and in `errors in 1920.txt`; independent research
  per Session E requirements -- 1886 comparison, RAE DLE (no entry for
  any of the three), and zero hits for all three across all three local
  reference corpora versus 5 ("aparecer") and 310 combined ("juicio")
  for the correctly-spelled forms, plus the pptext Edit Distance Checks
  section's own internal corroboration (6 and 37 correct-form hits
  elsewhere in this document) -- corroborating all three as typos, not
  period variants; one nuance noted: RAE's Diccionario Panhispánico del
  Español Jurídico has a narrow, unrelated medieval-Castilian-legal
  entry for "jucio," which does not change the verdict since 1886
  doesn't reproduce it here either). All three added to
  `permitted words.txt` per rule 10. Footnote check: whole-document
  scan confirms zero duplicates, last number 4011, and the only gap
  remains the long-documented footnote 812. Dash check: this page
  introduced zero hyphens (all rule-7 rejoins resolved). Short-lines/
  standalone-1/paragraph-level hits in this page's range all matched
  established false-positive categories. Whole-document sweeps clean:
  `check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py`, zero curly quotes. No narrow-space-vs-merge
  candidates on this page.
- **2026-07-30**: Sessions A-E run for page 548 (III Nefi 29:1-9, a new
  chapter opening — CAPÍTULO 29, no subtitle line — immediately after
  page 547 closed chapter 28 cleanly at v.40 with no cross-page word
  split; footnotes 4012-4020, nine footnote letters a-i, restarting at
  "a" per rule 13). Session A: one rule-7 hyphen rejoin ("necesi-"/
  "dad" -> "necesidad", v.2, 67 chars, kept on the first line) and one
  rule-8 rebalance (the [4018] marker pushed v.8's "alianza" line to
  exactly 73 chars, so "jurado;" moved to the start of the next line,
  which already began with "9. Por lo tanto..."); rule-31
  space-before-punctuation cleanup throughout (four semicolons, one
  exclamation mark, one comma); one rule-6 wide-gap normalization
  ("del  Padre", v.1). A significant footnote-letter investigation:
  entries b, c, g, i's cross-reference target (Véase [x], III Nefi 15)
  was initially misread as "i" by both the transcriber and the Google
  OCR text layer, but a dedicated high-zoom re-read (with enough room
  below the baseline to see the descender) showed the swash glyph is
  actually "j" — confirmed via a same-page comparison, 1879
  (pages_1879/page_0550.png, unambiguous serif italic: "c, see j, III.
  Nep. 15."), and decisive content-fit (chapter 15's own footnote 3702
  is a covenant citation matching all four of this page's "alianza"
  mentions; chapter 16's own already-transcribed "16h" independently
  cites this same "j" as a valid target). Entry b was a special case:
  1879 clearly prints "b, see 2j, III. Nep. 15." — but 1920's own
  already-transcribed chapter-15 footnote block ends at letter "v"
  (3714), with chapter 16 beginning immediately at 3715, so no "2j"
  target exists in either edition. Initially resolved editorially to
  "j" to match content, but the editor caught this and corrected the
  approach: per rule 32, the actual printed "2j" must be preserved
  (not silently substituted for the content-correct reading), so the
  transcription was reverted to "Véase 2j, III Nefi 15." and the
  finding logged as a genuine error inherited from 1879 into 1920 —
  see `errors in 1920.txt`. Two independent letter-level misprints were
  also found via manual comparison against `google_text_1920/
  page_0570.txt` (the automated `check_google_crosscheck.py`/
  `check_line_wrap.py` scripts both return empty/zero for this page —
  a tooling gap specific to chapter-opening pages, since their shared
  body-extraction helper stops at the blank line rule 1 mandates before
  a chapter heading, immediately after `Página N`): v.2 "Senor" prints
  with no tilde (unlike every other "Señor" on the page), and v.3
  "debeís" carries its accent on the í rather than the é (grammar wants
  "debéis") — the same accent-shift pattern already documented for
  page 504's "habeís". Mandatory i/l/1 check: this page's own final
  letter "i" (v.9) confirmed as a genuine short-stroke-plus-dot "i", no
  descender, ruling out l/1. Session B: independently re-verified all 9
  Block 1 entries and all 9 `[N]` body markers against a fresh
  `process_page.py` crop; the mandatory i/l/1 check was independently
  re-confirmed via a genuinely separate 1879 source — chapter 29's own
  g/h/i entries turned out to be on the *following* 1879 file page (551,
  not 550), since 1879's pagination lags 1920's here — printed in clear
  serif type matching every letter already resolved in Session A.
  Session C (`insert_body_text.py 548`): body text and 9 Block 1 entries
  inserted cleanly; chapter 28->29 boundary is same-book, no blank line
  per rule 20. Session D (`generate_block2.py 548`): 8 of 9 entries
  resolved cleanly; footnote 4013 ("Véase 2j, III Nefi 15") stayed
  correctly unresolved, matching the editor-confirmed error verdict.
  Content-fit confirmed for all resolved targets, including 4015/4019
  -> 3873, which explicitly cites "III Nefi 29:4,9" — this page's own
  verses. Session E: fresh pptext regeneration
  (`report_wsl_20260730.html`); zero new Spellcheck Suspect Words (both
  "Senor" and "debeís" pre-suppressed via `permitted words.txt`, the
  latter added this session). Per the mandatory Corrections-log sweep,
  all three suspected-error items from Sessions A/B were resolved and
  logged in `errors in 1920.txt`: the "2j" cross-reference (shared with
  1879, per the editor's guidance above); "Senor" (confirmed shared
  with 1886 too, at the identical spot on book page 544/file 562 --
  not a 1920-only error); and "debeís" (1886 uses a different verb
  construction here so offers no direct word-for-word comparison, but
  RAE and all three local reference corpora confirm "debéis" is the
  only attested form, zero hits for "debeís"). Footnote check:
  whole-document `\[(\d+)\]` scan confirms zero duplicates, last number
  4020, only gap remains the long-documented footnote 812. Dash check:
  zero hyphens introduced by this page. Curly-quote scan: zero
  instances in either master file. Special-situations "mixed letters
  and numbers in word" correctly (and expectedly) flagged the new "2j"
  Block 2 entry -- no further action, matches the already-logged error.
  Short-lines hits in this page's range all matched established
  false-positive categories. No long lines found anywhere in the
  document. Whole-document mechanical sweeps --
  `check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py` all clean. No narrow-space-vs-merge candidates
  on this page.
- **2026-07-30b**: Sessions A-E run for page 549 (end of III Nefi 30,
  v.1-2, immediately followed mid-page by the book boundary into IV
  Nefi -- book header "IV NEFI." / "LIBRO DE NEFI," / two-line subtitle
  "QUIEN ES HIJO DE NEFI, UNO DE LOS DISCIPULOS DE JESU CRISTO." /
  "CAPITULO 1." / italic argument "Relacion del pueblo de Nefi, segun
  sus anales.", then IV Nefi 1:1-2; footnotes 4021-4032, twelve letters
  across two chapters, both restarting at "a" per rule 13). Session A:
  one rule-7 hyphen rejoin ("verdadera-"/"mente" -> "verdaderamente,"
  IV Nefi 1:1); one rule-8 rebalance (the [4027]/[4028] markers pushed
  III Nefi 30:8's line to 75 chars, so "mi" moved to the start of the
  next line); rule-31 space-before-punctuation cleanup ("Jesús ;" ->
  "Jesús;"); the narrow-space default-to-two-words rule applied to
  "sepasó" -> "se pasó" (IV Nefi 1:1, flagged for the editor's Session E
  summary per the standing rule, not raised mid-pipeline); confirmed via
  zoom that "al rededor" (IV Nefi 1:1) carries no hyphen at its line
  break, genuinely two printed words. Three suspected misprints were
  preserved as printed and flagged: III Nefi 30:2 "remisióm" (ends in
  "m" not "n"), IV Nefi 1:1 "trienta" (extra "i," unlike "treinta"
  spelled correctly three other times on the same page), and IV Nefi
  1:2 "ocurrio" (missing its accent). A fourth, "abomínaciones" (III
  Nefi 30:2, accented, unlike the correctly-unaccented "abominaciones"
  earlier in the same sentence), was transcribed correctly per rule 32
  but not separately flagged in Corrections -- caught instead by
  Session E's spellcheck pass, exactly the kind of gap that step exists
  to catch. Mandatory i/l/1 check: entry 30d's cross-reference letter
  ("Véase i, II Nefi 10") confirmed as genuine "i" via 1879
  (pages_1879/page_0551.png, unambiguous serif type, "d, see i, II.
  Nep. 10." -- matching 1920's own reading exactly). Session B:
  independently re-verified all 12 Block 1 entries and all 12 `[N]`
  body markers from a fresh crop; the mandatory i/l/1 check was
  independently re-confirmed via a fresh crop of the same 1879 page
  (not a same-image re-read). No corrections needed. Session C
  (`insert_body_text.py 549`): body text inserted cleanly in one pass
  (unaffected by Block 1 structure), but Block 1 append hit a genuine,
  previously-unexercised tooling gap: `split_page()` in
  `insert_body_text.py` locates the end of a page's Block 1 section at
  the FIRST blank line, so this page's page-internal book boundary
  (originally hand-formatted with a blank/"IV NEFI"/blank header
  between the chapter-30 and IV-Nefi-1 entries, mirroring the final
  `librodm_foot.txt` output) caused the script to silently truncate
  Block 1 to just the first 8 entries -- confirmed by the script's own
  "Appended 8 Block 1 entries" report. This is a different failure mode
  from page 481's (a header-text-selection ambiguity across a page
  boundary, which the script already handles correctly); this one is a
  page-internal boundary tripping the line-range parser. Resolved by
  hand: appended the missing `1a`-`1d` entries to `librodm_foot.txt`
  directly in the exact form `append_block1()` would have produced
  (blank line, "IV NEFI" header, blank line, then the four entries),
  and removed the manual header from `page_549.txt`'s own Block 1
  section to match the established convention (per page 481's
  precedent) that book headers are never hand-typed in a page's own
  Block 1 file -- only the master files carry them, inserted by the
  script. Session D (`generate_block2.py 549`): all 12 entries resolved
  cleanly to sequential numbers on the first pass; the "IV NEFI" header
  was correctly auto-inserted into `librodm.txt`'s Notas section this
  time, since Block 1 no longer had a page-internal blank line to trip
  on after the Session C fix. Content-fit spot-checked for several
  entries including the mandatory-check target (4024 -> 379 -> 265, a
  broad Atonement/redemption reference chain) and multiple baptism-verse
  citations matching their annotated words exactly. Session E: fresh
  pptext regeneration (`report_wsl_20260730b.html`). Spellcheck flagged
  three of this page's words directly ("abomínaciones," "remisióm,"
  "trienta"); the fourth ("ocurrio") was not flagged by aspell, a known
  gap, so it was researched anyway per the mandatory-check procedure.
  All four were checked against 1886 (pages_1886/page_0563.png and
  page_0564.png, book pages 545-546/file 563-564), the modern LDS
  Spanish edition (churchofjesuschrist.org, III Nefi 30 and IV Nefi 1),
  RAE DLE, and the three local reference corpora -- all four confirmed
  as genuine 1920-only errors, none shared with 1886 (1886 has
  "abominaciones," "remision," "tréinta," and "ocurrió" respectively at
  the equivalent spots). All four logged in `errors in 1920.txt`; the
  three aspell-flagged words also added to `permitted words.txt`
  ("ocurrio" was not, per the established "Jesu Cristo" no-op
  precedent, since it isn't actually pptext-flagged). Full report
  walkthrough for this page's new line range found nothing further:
  Edit Distance, Dash check (hyphen-minus bucket: two legitimate verse
  ranges), Special situations (only the already-known page-548 "2j"
  entry appears nearby), "paragraph ends in comma" (the "LIBRO DE
  NEFI," book-header line matches the established false-positive
  pattern exactly), and short-lines hits all clean or already-explained.
  Footnote check: whole-document scan confirms zero duplicates, last
  number 4032 (matching this page's final marker), only gap remains the
  long-documented footnote 812. Curly-quote scan: zero instances in
  either master file (re-verified with a reliable method after an
  initial unreliable character-count approach over-reported). Dash
  check: this page introduced zero new hyphens. Whole-document
  mechanical sweeps -- `check_spaced_punctuation.py`/
  `check_footnote_punctuation.py`/`check_verse_indent.py`/
  `check_lines.py` all clean. One narrow-space-vs-merge note surfaced
  for the editor's own convenience: IV Nefi 1:1 "se pasó" (see Session A
  above).
- **2026-07-30c**: Sessions A-E run for page 550 (IV Nefi 1:2-14
  continuation, no book/chapter boundary; footnotes 4033-4044, letters
  1e-1p, continuing the single chapter-1 lettering sequence from page
  549 with no restart). Session A: three rule-7 hyphen rejoins
  ("con-"/"tiendas" -> "contiendas," carried over from page 549's final
  sentence; "levanta-"/"ban" -> "levantaban," v.5; "hun-"/"dido" ->
  "hundido," v.9); one rule-8 rebalance (the [4040]/[4041] markers on
  v.12's "reunirse...orar...escuchar" line pushed it to 73 chars, so
  "escuchar" moved to the start of the next line); extensive rule-31
  space-before-semicolon cleanup (this page's print consistently sets a
  space before every semicolon, ~9 instances, all mechanical). Five
  suspected misprints preserved as printed and flagged: v.3 "escavos"
  (missing "l"), v.4 and v.6 "trienta" (same letter-transposition
  pattern already logged for v.1 on page 549), v.12 "Sénor" (acute
  accent instead of tilde) and "ordenzas" (missing "an"), v.14
  "unicamente" (missing accent), plus two suspected period-for-comma
  punctuation slips (v.2 "disputas. y obraron"; v.14 "pasado ya.
  cuando"). Google cross-check flagged three candidates: "cojos" vs.
  Google's "cojcs" dismissed as OCR noise (not a word); the two
  period/comma spots were re-zoomed at 15-20x and confirmed as genuine
  periods in the 1920 print (Google misread both as commas) — the
  transcription was correct as originally read, not changed at the
  time. Mandatory i/l/1 check: this chapter's own letters i ("habían
  hundido," v.9) and l ("reunirse," v.12) confirmed via strict
  alphabetical sequence plus exact 1879 content match. Two cross-
  reference TARGET letters also fell in the mandatory set and proved
  genuinely hard to distinguish by glyph shape alone in this page's
  font even after repeated 25-40x zoom crops — resolved instead via a
  same-target-chapter back-reference method (Section 8 procedure step
  7): entry k ("Véase [?], Mosiah 27," annotating "ayunos") resolved to
  "t" because 1920's own Mosiah 27 footnote block explicitly
  cross-references this exact verse (IV Nefi 1:12); entry o ("Véase
  [?], II Nefi 9," annotating "paraíso") resolved to "l" because
  1920's own II Nefi 9 footnote block explicitly cross-references IV
  Nefi 1:14. Both independently cross-checked against 1879. Session B:
  independently re-verified all 12 Block 1 entries and all 12 `[N]`
  body markers against a fresh crop; independently re-ran the mandatory
  i/l/1 check via fresh 1879 crops (different crop ranges than Session
  A) — all confirmed, no corrections needed. Session C
  (`insert_body_text.py 550`): clean single-pass insertion, no
  book-boundary complications (chapter continues). Session D
  (`generate_block2.py 550`): 9 of 12 entries resolved cleanly; 2 (4036
  "Omni 1; III Nefi 8:8,24;9:3", 4038 "II Nefi 25; III Nefi
  9:19;15:2-8") stayed unresolved as a script parsing limitation with
  compound (semicolon-separated) references — target letters confirmed
  valid, left in letter form for a later `--fix-unresolved` pass. The
  third (4041, "Véase o, II Nefi 32") was a genuine transcription
  error, not a script limitation: II Nefi 32's own footnote block only
  runs letters a-e, so "o" was an impossible target. Re-investigated
  and corrected to "e" -- II Nefi 32's own letter e is directly
  attached to the word "orar" in its own body text, Alma 25's footnote
  block independently cross-references the same "e, II Nefi 32"
  target, and 1879's parallel entry also reads "e." Fixed in
  page_550.txt, librodm_foot.txt, and librodm.txt's Block 2 (now
  "4041: Véase 783."). A good demonstration of Session D's resolution
  step catching a letter-level misread outside the mandatory i/l/1
  set. Session E: fresh pptext regeneration (`report_wsl_20260730c.html`).
  Spellcheck flagged "escavos," "unicamente" (already known), plus two
  new catches: "éntre" (v.5, edit-distance-matched to an existing
  correct "Entre" elsewhere in the document) and "multiplicóse" (v.10,
  no edit-distance match). All suspected words checked against 1886,
  the modern LDS edition, RAE, and the three reference corpora:
  "escavos," "éntre," "Sénor," and "ordenzas" all confirmed genuine
  1920-only errors (1886 and the modern edition both have the correct
  form; RAE has no entry for the 1920 spelling; near-zero corpus hits)
  and added to `errors in 1920.txt` (escavos/éntre/Sénor also to
  `permitted words.txt`; ordenzas is not aspell-flagged, so no
  permitted-words entry, matching the "Jesu Cristo" no-op precedent).
  "multiplicóse" confirmed as a legitimate archaic reflexive
  construction shared verbatim with 1886 -- added to `permitted
  words.txt` only. "unicamente" confirmed shared with 1886 (missing
  accent both editions) -- permitted-words only, no errors-log entry
  per rule 11. The two period-for-comma punctuation items were
  re-confirmed against 1886 (which has a comma at both spots) and
  logged in `errors in 1920.txt`, matching the established "full stop
  followed by unexpected sequence" pattern from prior sweeps. While
  researching "Sénor," the identical accent-instead-of-tilde error was
  found already present and previously undetected at Alma 13:16
  (librodm.txt line 12582) -- confirmed against 1886 and added to
  `errors in 1920.txt` at its correct earlier position in the file, a
  good example of Session E's investigation surfacing an old,
  unrelated defect. Full report walkthrough beyond spellcheck: Edit
  Distance (above), Dash check (only this page's own legitimate
  "15:2-8" verse range in the hyphen-minus bucket, zero new hyphens),
  "full stop followed by unexpected sequence" (confirmed only this
  page's two already-logged instances belong to this page; many other,
  unrelated instances exist elsewhere in the document from earlier
  pages -- out of scope for this session, noted for the editor), "mixed
  letters and numbers in word" (routine footnote-citation false
  positive, nothing new). Footnote-anchor whole-document scan: zero
  duplicates, max 4044 (matches this page's final marker), only the
  long-documented footnote 812 gap remains. Curly-quote scan: zero
  instances in either master file. Whole-document mechanical sweeps --
  `check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py`/`check_lines.py` all clean.

- **2026-07-30c**: Sessions A–E run for page 550 (IV Nefi 1:2-14
  continuation, no book/chapter boundary; footnotes 4033-4044, letters
  1e-1p, continuing the single chapter-1 lettering sequence from page
  549 with no restart). Session A: three rule-7 hyphen rejoins; one
  rule-8 rebalance (v.12); extensive rule-31 space-before-semicolon
  cleanup (~9 instances, this page's print consistently sets a space
  before every semicolon). Five suspected misprints preserved as
  printed and flagged: v.3 "escavos," v.4/v.6 "trienta" (same pattern
  already logged for page 549's v.1), v.12 "Sénor"/"ordenzas," v.14
  "unicamente," plus two suspected period-for-comma slips (v.2
  "disputas. y obraron"; v.14 "pasado ya. cuando"). Google cross-check:
  "cojos" vs. Google's "cojcs" dismissed as OCR noise; the two
  period/comma spots were re-zoomed at 15-20x and confirmed genuine
  periods in the 1920 print (Google misread both as commas). Mandatory
  i/l/1 check: this chapter's own letters i/l confirmed via sequence +
  1879. Two cross-reference TARGET letters (entries k and o) proved
  genuinely hard to distinguish by glyph shape even at 25-40x zoom —
  resolved via same-target-chapter back-references instead: entry k
  ("Véase [?], Mosiah 27") resolved to "t" (1920's own Mosiah 27
  footnote block explicitly cross-references IV Nefi 1:12); entry o
  ("Véase [?], II Nefi 9") resolved to "l" (1920's own II Nefi 9
  footnote block explicitly cross-references IV Nefi 1:14). Both
  cross-checked against 1879. Session B: independently re-verified all
  12 Block 1 entries/markers and the mandatory i/l/1 check via fresh
  crops — all confirmed, no corrections needed. Session C: clean
  single-pass insertion, no book-boundary complications. Session D: 9
  of 12 Block 2 entries resolved cleanly; 2 stayed unresolved as a
  script parsing limitation with compound (semicolon-separated)
  references (target letters confirmed valid, left for a later
  `--fix-unresolved` pass); the third (4041, entry m) was a genuine
  transcription error, not a script limitation — II Nefi 32 only has
  letters a-e, so "Véase o, II Nefi 32" was an impossible target.
  Corrected to "e" (II Nefi 32's own letter e is attached to the word
  "orar" in its own body text; Alma 25 independently cross-references
  the same "e, II Nefi 32"; 1879's parallel entry also reads "e"),
  fixed in all three files. A good demonstration of Session D catching
  a letter-level misread outside the mandatory i/l/1 set. Session E:
  fresh pptext regeneration (`report_wsl_20260730c.html`). Spellcheck
  flagged "escavos," "unicamente" (already known), plus two new
  catches: "éntre" (v.5, edit-distance-matched to an existing correct
  "Entre" elsewhere) and "multiplicóse" (v.10). All suspected words
  checked against 1886, the modern LDS edition, RAE, and the reference
  corpora: "escavos," "éntre," "Sénor," and "ordenzas" confirmed
  genuine 1920-only errors, added to `errors in 1920.txt`
  (escavos/éntre/Sénor also to `permitted words.txt`; ordenzas isn't
  aspell-flagged, so no permitted-words entry). "multiplicóse"
  confirmed a legitimate archaic reflexive form shared verbatim with
  1886 — permitted-words only. "unicamente" confirmed shared with 1886
  (missing accent both editions) — permitted-words only, no
  errors-log entry per rule 11. The two period-for-comma items
  re-confirmed against 1886 (comma at both spots) and logged in
  `errors in 1920.txt`. While researching "Sénor," the identical
  accent-instead-of-tilde error was found already present and
  previously undetected at Alma 13:16 (librodm.txt line 12582) —
  confirmed against 1886 and added to `errors in 1920.txt` at its
  correct earlier position, a good example of Session E surfacing an
  old, unrelated defect from a much earlier page. Full report
  walkthrough beyond spellcheck: Dash check (only this page's own
  legitimate "15:2-8" verse range, zero new hyphens), "full stop
  followed by unexpected sequence" (confirmed only this page's two
  already-logged instances belong to this page — many other, unrelated
  instances exist elsewhere in the document from earlier pages, out of
  scope for this session, noted for the editor), "mixed letters and
  numbers in word" (routine false positive, nothing new). Footnote
  scan: zero duplicates, max 4044, only the long-documented 812 gap
  remains. Curly-quote scan: zero instances. Whole-document mechanical
  sweeps all clean.
- **2026-07-30d**: Sessions A–E run for page 551 (IV Nefi 1:15-25, no
  book/chapter boundary; footnotes 4045-4048, letters 1q-1t,
  continuing the single chapter-1 lettering sequence from page 550
  with no restart). Session A: two rule-7 hyphen rejoins (v.16
  "men-"/"tiras", v.23 "exten-"/"sión", both well under the 73-char
  cap, no rule-8 rebalance needed); six rule-31 space-before-semicolon
  fixes. Mandatory i/l/1 check: none of this page's own four letters
  (q,r,s,t) are themselves i/l/1, but entry s's cross-reference target
  letter ("Véase [?], I Nefi 1:17") was genuinely ambiguous by glyph
  shape (single unbroken diagonal stroke, no dot, no visible
  crossbar) — resolved to "f" via content-fit + back-reference rather
  than shape alone: 1920's own I Nefi chapter 1 "1f, 6" entry is an
  exact citation-list match for the "abridgment of my father's
  record" annotation, independently confirmed against 1879's parallel
  "f" entry, and against a direct glyph comparison to 1920's own "f"
  marker elsewhere in I Nefi 1 (page_0025.png) — same shape. One
  suspected misprint preserved as printed and flagged: v.18 "benijo"
  (missing "d," should be "bendijo"). Google cross-check caught a
  second, more subtle one Session A's own reading missed on the first
  pass: v.20 "por to tanto" — the transcription initially read "lo,"
  but Google's OCR read "t," and a 15-20x re-zoom confirmed Google was
  right (the glyph has a crossbar, unlike "l"); corrected in the page
  file before integration. Checked and confirmed NOT an error: v.17
  "ninguna especie de itas" (matches 1886 identically — a deliberate
  period translation of the English source's generic "-ites" suffix,
  not a misprint); v.21 "Jesu Cristo" (no hyphen, unlike this same
  page's own v.18 "Jesu-Cristo") was initially logged as a 1920-only
  inconsistency but corrected by the editor — this unhyphenated form
  is an archaic spelling used extensively throughout this edition, not
  an error; both hyphenated and unhyphenated forms are legitimate and
  coexist in this edition, see `feedback_jesu_cristo_hyphen` memory.
  Session B:
  independently re-verified all 4 Block 1 entries/markers and the
  mandatory i/l/1 check via fresh crops (including a fresh 1879 crop
  for entry s) — all confirmed, no corrections needed. Session C:
  clean single-pass insertion, no book-boundary complications. Session
  D: all 4 Block 2 entries resolved cleanly on the first pass; strong
  independent confirmation for entry t ("Véase v, III Nefi 26" ->
  3947): III Nefi's own "26v, 3947" entry explicitly back-references
  "IV Nefi 1:1," the exact "all things common" description this
  page's v.25 is contrasting against. Session E: fresh pptext
  regeneration (`report_wsl_20260730d.html`, re-confirmed after
  `permitted words.txt` updates via `report_wsl_20260730e.html`).
  Spellcheck flagged "benijo," "to" (both already caught above), plus
  "empezóse" (v.24) — confirmed a legitimate archaic enclitic
  reflexive form matching page 550's "multiplicóse" precedent exactly
  (1886 uses the identical construction at the same verse). All
  checked against 1886, RAE, and the reference corpora: "benijo" and
  "to" confirmed genuine 1920-only errors, added to `errors in
  1920.txt` and `permitted words.txt`; "empezóse" added to `permitted
  words.txt` only. Full report walkthrough beyond spellcheck: zero new dash,
  footnote-check, curly-quote, or special-situations hits for this
  page's line range. Footnote scan: zero duplicates, max 4048, only
  the long-documented 812 gap remains. Whole-document mechanical
  sweeps (`check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py`/`check_lines.py`) all clean.
- **2026-07-30e**: Sessions A–E run for page 552 (IV Nefi 1:26-36, no
  book/chapter boundary; footnotes 4049-4053, letters 1u-1y,
  continuing the single chapter-1 lettering sequence from page 551
  with no restart). Page opens with a fresh verse number (26.) rather
  than mid-verse, so no blank line follows "Página 552" (matches
  page 500/505/509/etc. precedent). Session A: no rule-7 hyphen
  rejoins or rule-31 space-before-punctuation instances on this page.
  Mandatory i/l/1 check: none of this page's five letters (u,v,w,x,y)
  or the one cross-reference target letter (entry v's "Véase d, III
  Nefi 28") are i/l/1. Swash-font letter ambiguity (same technique as
  page 451): the 1st/3rd markers (u,w) and 2nd/5th markers (v,y) each
  share an identical glyph shape in this stylized font, undistinguishable
  by shape alone; resolved via strict alphabetical position (5 markers
  = 5 Block 1 entries, continuing from page 551's final letter "t")
  and independently CONFIRMED via 1879 (pages_1879/page_0554.png,
  book page 546): "t, see y, III. Nep. 26. u, III. Nep. 18:28,29. v,
  the three. See d, III. Nep. 28. w, ver. 5. III. Nep. 28:19. x, III.
  Nep. 28:21. y, III. Nep. 28:22." — an exact letter-for-letter and
  content match to all five 1920 entries. Content-fit: entries
  annotate the passage about the three Nephite disciples' persecution/
  imprisonment (III Nefi 28:19-22), an exact thematic match verse-by-
  verse. Google cross-check: one candidate ("discípulos" vs. Google's
  accent-less OCR) confirmed via 20x zoom to be a genuine printed
  accent that Google simply dropped — no correction needed. Session
  B: independently re-verified all 5 Block 1 entries and body markers
  against a fresh crop, plus a fresh independent 1879 crop — all
  confirmed, no corrections needed. Session C: clean single-pass
  insertion, no book-boundary complications. Session D
  (`generate_block2.py 552`): all 5 entries resolved cleanly; entry
  v's cross-reference ("Véase d, III Nefi 28" -> "Véase 3983") strongly
  confirmed by III Nefi's own "28d, 3983" entry, whose citation list
  explicitly back-references "IV Nefi 1:14,37" — directly tying to
  this chapter's three-disciples narrative. Session E: fresh pptext
  regeneration (`report_wsl_20260730f.html`). Caught two genuine
  1920-only errors that Session A did not flag at transcription time
  (found by direct reading against 1886, not via a pptext spellcheck
  hit): v.26 "obrener" (misprint for "obtener," confirmed via 1886
  "obtener," RAE has no entry for "obrener"); v.36 "Zoramítas" (a
  superfluous accent on a word that takes none by regular Spanish
  stress rules — confirmed via 1886 "Zoramitas" no accent, the modern
  LDS Spanish edition "zoramitas" no accent, and this document's own
  consistent unaccented spelling everywhere else since Alma 31; same
  error pattern as the existing Alma 31:7 "Zoranitas" entry). Also
  resolved the page's own flagged inconsistency: v.35 "descientos"
  (missing "o," should be "doscientos," inconsistent with this same
  page's correct "doscientos" at v.27/v.34) — confirmed via 1886, RAE
  (no entry), and reference corpora (0 hits for "descientos" vs. 43
  for "doscientos"). All three added to `errors in 1920.txt` and
  `permitted words.txt`. Full report walkthrough beyond spellcheck:
  zero new dash, footnote-check, curly-quote, or special-situations
  hits for this page's line range (footnote-check re-verified via a
  direct Python whole-document scan rather than the pptext report's
  line-number-range display, which is line-based rather than
  footnote-number-based and not useful for this purpose). Footnote
  scan: zero duplicates, max 4053, only the long-documented 812 gap
  remains. Whole-document mechanical sweeps
  (`check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py`/`check_lines.py`) all clean.
- **2026-07-31**: Sessions A–E run for page 553 (IV Nefi 1:37-48, no
  book/chapter boundary; footnotes 4054-4059, letters z/2a-2e,
  continuing the single chapter-1 lettering sequence from page 552's
  final letter "y" with no restart, wrapping past z into two-letter
  form per rule 16). Page opens with a fresh verse number (37.), no
  blank line after "Página 553" (matches page 500/505/509/552/etc.
  precedent). Session A: 4 rule-7 hyphen rejoins (verda-/deros,
  Laman-/itas, cuaren-/ta, habién-/dose), all well under the 72-char
  cap after rejoining; a handful of rule-31 space-before-punctuation
  and one justification-widened gap normalized per the standing rules.
  A print smudge before "Josefitas" (v.37) was identified as NOT a
  genuine footnote superscript (unlike the real "z" marker on "tres"
  two lines above) — confirmed via `check_google_crosscheck.py`
  (Google's OCR reads "Jacobitas, Josefitas y Zoramitas." with no
  glued character there at all, while it does misread the genuine "z"
  marker as a stray quote mark) and via 1879 showing no mark at the
  parallel tribe-name-list spot either. Mandatory i/l/1 check: only
  entry 1-2c's cross-reference target letter "i" ("Véase i, II Nefi
  10") falls in the mandatory set; independently CONFIRMED via 1879
  (pages_1879/page_0555.png, book page 547) both in Session A and
  again from a fresh crop in Session B: "2c, see i, II. Nep. 10" —
  clear italic "i" with a separated dot, unambiguously distinct from
  "l." Full 1879 cross-check: all six Block 1 entries confirmed
  letter-for-letter and reference-for-reference against the same 1879
  page's footnote block ("z, see d, III. Nep. 28. 2a, III. Nep. 27:32.
  Mor. 1:16. 2b, see n, Jacob 7. 2c, see i, II. Nep. 10. Hela. 2:3-14.
  2d, III. Nep. 28:9. 2e, see 2c."), an exact match, including entry
  2e's same-chapter self-reference to 2c (no book/chapter needed since
  both live in this same chapter) — Session D's `generate_block2.py`
  correctly resolved this to "Véase 4057," matching entry 1-2c's own
  sequential number exactly. Content-fit sanity check: all six
  plausible (entry z/tres-discípulos repeats page 552's established
  three-disciples cross-reference; entry 2c/secretos-juramentos cites
  Helamán 2:3-14, the literal introduction of Gadianton's secret
  combinations — an exact thematic match). Session B: independently
  re-verified all 6 Block 1 entries, all 6 body markers, and the
  mandatory i/l/1 letter against fresh crops of both the 1920 and 1879
  images (not reused from Session A) — all confirmed, no corrections
  needed. Session C: clean single-pass insertion, no book-boundary
  complications. Session D (`generate_block2.py 553`): all 6 entries
  resolved cleanly, including the same-chapter self-reference noted
  above. Session E: fresh pptext regeneration
  (`report_wsl_20260731.html`, built via a live WSL run, not reused).
  Three suspected misprints flagged at Session A transcription time
  were all confirmed as genuine, isolated 1920-only errors: v.38
  "princiopio" (extra "o"; 1886 prints "principio," RAE has no entry,
  zero corpus hits); v.40 "occurrió" (double c; 1886 prints "ocurrió,"
  same recurring error pattern already documented at 1 Nefi 13:20 and
  Alma 55:4); v.41 "adonándolas" (missing "r"; 1886 prints
  "adornándolas" complete, and although "adonar" is a genuine RAE-
  attested 14th-century archaic variant of "adornar," it has zero
  hits in all three reference corpora — combined with the exact 1886
  mismatch and this document's own consistent "adornar" spelling
  elsewhere, judged a typo rather than a deliberate archaic form). All
  three added to `errors in 1920.txt` and `permitted words.txt`. Full
  report walkthrough beyond spellcheck: zero new dash, footnote-check,
  scanno, curly-quote, or special-situations hits for this page's line
  range; edit-distance section only reconfirmed the already-handled
  princiopio/principio pair. Footnote scan: zero duplicates, max 4059,
  only the long-documented 812 gap remains. Whole-document mechanical
  sweeps (`check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py`/`check_lines.py`) all clean against both
  master files; an independent curly-quote character scan of both
  master files also found zero curly quotes.

- **2026-07-31**: Sessions A–E run for page 554 (IV Nefi 1:48-49,
  concluding IV Nefi, then a book boundary into Mormón — "LIBRO DE
  MORMÓN" — CAPÍTULO 1:1-8, continuing to page 555; footnotes
  4060-4071, continuing the IV Nefi chapter-1 "2f/2g" two-letter
  lettering from page 553, then restarting fresh at "a" for Mormón 1
  per rule 13). Session A: 3 rule-7 hyphen rejoins (tres-/cientos,
  guar-/darlas, Mor-/món), one separate rule-8 rebalance (v.3's
  "...depositado para" line hit 73 chars once both footnote markers
  were inserted; "para" moved to the next line). A genuine zero-width
  merge in the print, "dondese hallan" (v.4), was transcribed as two
  words ("donde se hallan") per the standing narrow-space-vs-merge
  default (grammar requires two words), not raised mid-pipeline.
  Two suspected misprints were preserved as printed pending Session E:
  v.48(cont.) "viente" (transposed for "veinte" — same paragraph
  correctly prints "veinte" three lines later) and v.5 "recodré"
  (missing "r" for "recordé"). The book-title heading itself prints as
  "LIBRO DF MORMON." (D-F typo, no accent) immediately before
  "CAPÍTULO 1." — preserved as printed in the body text per rule 32,
  but the Block 1 book-name header (rule 19) uses the corrected form
  "LIBRO DE MORMÓN" instead, since that header is a structural
  navigation label (matching the index and this page's own running
  header), not verbatim body text — a judgment call with no prior
  precedent, flagged explicitly in the page's Corrections log.
  Mandatory i/l/1 check: Mormón chapter 1's own new letter "i" (Sur
  América, v.6) is in the mandatory set; confirmed via 1879
  (pages_1879/page_0557.png, book page 549) in both Session A and
  again from a fresh crop in Session B: "i, South America... l, the
  three, who were not to taste of death" — a clear italic "i" with a
  separated dot, unambiguously distinct from "l." Full 1879
  cross-check: all 12 Block 1 entries (1-2f/1-2g plus 1a-1j) confirmed
  letter-for-letter and reference-for-reference against
  pages_1879/page_0556.png and page_0557.png, an exact match. Session
  B: independently re-verified all 12 entries/markers against a fresh
  crop, no corrections needed. Session C
  (`insert_body_text.py 554`): body text inserted correctly, but the
  script's own book-boundary detection ("chapter < last_chapter")
  never fires here, since IV Nefi's only chapter and Mormón's first
  chapter are both numbered "1" — it silently appended only 2 of the
  12 Block 1 entries (the script's own `split_page()` mistook this
  page's internal blank-line/header/blank-line for a book boundary as
  the end of the whole Block 1 section). The book-name header and the
  10 missing entries (1a-1j) were appended to `librodm_foot.txt` by
  hand instead, verified against the page's own Block 1 listing;
  flagged in the page's Corrections log as the first page to exercise
  a same-chapter-number book boundary, for future multi-page runs.
  Session D (`generate_block2.py 554`): all 12 entries resolved
  cleanly, including three cross-references (Véase f, I Nefi 1 → 6;
  Véase b, Mosíah 18 → 1337; Véase h, Omni 1 → 1003), all
  thematically consistent on inspection. Entry 4062 wrapped across
  three lines rather than two due to its first semicolon-delimited
  segment alone exceeding 72 characters — valid mechanical output,
  not a defect. Session E: fresh pptext regeneration
  (`report_wsl_20260731b.html`, live WSL run). All three suspected
  misprints confirmed as genuine, isolated 1920-only errors via 1886
  (pages_1886/page_0568.png and page_0569.png) plus RAE and, for
  "recodré," the modern LDS Spanish edition (Mormón 1:5 "recordé");
  added to `errors in 1920.txt` (IV Nefi 1:48 "viente"; a new "Mormón
  (encabezado del libro)" entry for the title misprint; Mormón 1:5
  "recodré") and to `permitted words.txt` ("recodré" — "viente" was
  already present, but with no matching errors-log entry, an
  undetected gap since some earlier session). While researching, found
  this same "vient-" typo family (already documented at III Nefi
  5:7/6:9/6:10) also appears, undocumented, at Omni 1:5's identical
  phrase "trescientos viente" — retroactively added in correct book
  order. Spellcheck flagged three words from this page ("Antum",
  "DF", "cuerdo" — the last a common, correctly-spelled word matching
  1886 exactly, apparently just outside aspell's base dictionary); all
  three added to `permitted words.txt`, none logged as errors. The
  edit-distance check paired this page's "cuerdo" with an unrelated
  pre-existing word, "cuermo" (III Nefi 20:19) — already a genuine,
  documented `errors in 1920.txt` entry from an earlier session that
  had never been mirrored into `permitted words.txt`; added now,
  closing that gap (same class of oversight as the already-documented
  Helamán 5:35 "seperado" gap). Full report walkthrough beyond
  spellcheck: zero new dash, footnote-anchor, scanno, curly-quote,
  repeated-word, long-line, duplicate-line, or special-situations hits
  for this page's range. Footnote scan: footnotes 4055-4071 form one
  contiguous, gap-free, duplicate-free range. Whole-document mechanical
  sweeps (`check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py`/`check_lines.py`) all clean against both
  master files.

- **2026-07-31**: Sessions A–E run for page 555 (Mormón 1:8(cont.)-19,
  continuing the same chapter opened on page 554, no book/chapter
  boundary on this page; footnotes 4072-4079, continuing chapter 1's
  own letter sequence from page 554's "j" with "k" through "r"). Session
  A: no rule-7 hyphen rejoins (every line ending was a genuine word
  boundary) and no rule-8 rebalancing needed (every marker-lengthened
  line stayed at or under 72 chars, longest exactly 72). A genuine
  zero-width merge in the print, footnote 1l's own citation text
  "queno" (for "que no habían de gustar la muerte"), was transcribed as
  two words per the standing narrow-space-vs-merge default (grammar and
  1879's "who were not to taste of death" both require "no"), not
  raised mid-pipeline. Two justification-tight-but-real gaps (v.12 "la
  que duró", v.19 "Y ocurrió") were double-checked at high zoom and
  confirmed as ordinary narrow spaces, not merges. A false alarm (v.12
  "paz" looked like it had a stray mark after it at low zoom) resolved
  at high zoom as just this font's serif "z" glyph, nothing to log.
  Two suspected misprints were preserved as printed pending Session E,
  both in the same v.15 sentence: "tante" (expected "tanto") and
  "vistó" (expected "visitó", missing "i"). Mandatory i/l/1 check:
  this chapter's own letter "l" recurs three times on this page (its
  own definition, entry n's "Véase l" cross-reference back to it, and
  the body-text superscript itself before "amados," v.13); confirmed
  via 1879 (pages_1879/page_0557.png, book page 550) in both Session A
  and again from a fresh crop in Session B: "l, the three, who were not
  to taste of death" — a clear continuous curve, unambiguously distinct
  from "i." Full 1879 cross-check: all 8 Block 1 entries (1k-1r)
  confirmed reference-for-reference against pages_1879/page_0557.png
  and page_0558.png, an exact content match (entry 1k's target LETTER
  differs, "o" vs. 1879's "g" within Alma 2's own lettering — a
  translation-artifact letter mismatch per rule 26, not an error).
  Session B: independently re-verified all 8 entries/markers against a
  fresh crop, no corrections needed. Session C (`insert_body_text.py
  555`): no book/chapter boundary on this page, so the script's normal
  path handled both body text and all 8 Block 1 entries correctly with
  no manual intervention needed (unlike page 554's same-chapter-number
  boundary case). Session D (`generate_block2.py 555`): all 8 entries
  resolved cleanly, including four cross-references (Véase o, Alma 2 →
  1656; Véase d, III Nefi 28 → 3983; Véase 2a, IV Nefi 1 → 4055; Véase
  d, II Nefi 1 → 249, cited twice by entries o and q), all thematically
  consistent on inspection — notably entry o/q's target (II Nefi 1d)
  itself cites "Mormón 1:17," this very page's own verse. Session E:
  fresh pptext regeneration (`report_wsl_20260731c.html`, live WSL
  run). Both suspected misprints confirmed as genuine, isolated
  1920-only errors via 1886 (pages_1886/page_0570.png, book page 552)
  plus RAE (no entry for either "tante" or "vistó") plus the modern LDS
  Spanish edition (Mormón 1:15 "por tanto, me visitó el Señor") plus
  zero standalone hits in all three reference corpora: added to `errors
  in 1920.txt` (Mormón 1:15 "tante"; Mormón 1:15 "vistó") and
  `permitted words.txt` ("tante" — "vistó" was already present from an
  earlier page). Spellcheck Suspect Words and Edit Distance sections:
  zero hits from this page's range. Full report walkthrough beyond
  spellcheck: zero new dash, footnote-anchor, scanno, curly-quote,
  repeated-word, long-line, duplicate-line, or special-situations hits
  for this page's range. Footnote scan: footnotes 4072-4079 form one
  contiguous, gap-free, duplicate-free range (only pre-existing gap in
  the whole document remains the long-documented footnote 812). Whole-
  document mechanical sweeps (`check_spaced_punctuation.py`/
  `check_footnote_punctuation.py`/`check_verse_indent.py`/
  `check_lines.py`) all clean against both master files; an independent
  curly-quote character scan of both master files also found zero
  curly quotes.

- **2026-07-31d**: Sessions A–E run for page 556 (Mormón 2:1-10, opening
  a new chapter — CAPÍTULO 2, no subtitle line present in the image, no
  book-name header needed since the book itself doesn't change (rule
  20); footnotes 4080-4086, letters restart fresh at "2a" through "2g"
  per rule 13). Session A: one rule-7 hyphen rejoin (Lamani-/tas,
  rejoined onto the first line at 67 chars, no rule-8 rebalancing
  needed). Six rule-31 space-before-punctuation instances found in the
  original print and normalized (v.2 "Lamanitas ; bhabiendo", v.3(cont.)
  "ejércitos ; por", v.8 "Lamanitas ; y", v.8(cont.) "maldades ; por",
  v.9 "Aarón ;", v.10 "Samuel ; porque"). Rule 23/24 verse-citation
  formatting applied to Block 1 (not the printed original): entry 2a's
  "1:12, 15" → "1:12,15" (non-consecutive), entry 2b's "2:7, 8" →
  "2:7-8" (consecutive). Letter-to-verse mapping required active
  disambiguation: a 1920 image mark that looked like a genuine raised
  superscript appeared in v.6 before "fuímos," which would have made 8
  body-text marks against only 7 lettered entries (a-g); cross-checked
  against 1879 (pages_1879/page_0558.png, top crop) which shows no
  footnote at all in the corresponding position, confirming the 1920
  mark is stray print noise, not a genuine footnote letter, and it was
  not transcribed. This also resolved which verse entries e/f/g
  annotate: e → "robbers" (v.8, thematically fits its IV Nefi 1 "2c"
  Gadianton-robbers target), f → "Aaron" (v.9, matches its own "Moroni
  9:17" content), g → "Samuel" (v.10, matches its "Véase r, Mormón 1"
  self-reference back to page 555's own prophecy-fulfillment entry 1r).
  Content-fit sanity check on entries a-d also confirmed consistent
  (mismo año/Mormón 1:12,15; year-count/III Nefi 2:7-8; países del
  Norte/direct geographic gloss; fortificamos/Alma 48's own
  city-fortification account). Two suspected misprints/anomalies were
  preserved as printed pending Session E: v.9(cont.) "trescientos
  trienta años" (expected "treinta," an apparent metathesis) and Block
  1 entry 2e's "Véase; 2c, IV. Nefi 1." with a semicolon directly after
  "Véase" (confirmed at high zoom as a genuine semicolon glyph, with no
  equivalent punctuation in 1879's parallel entry). Mandatory i/l/1
  check: not triggered — none of this page's own letters (a-g) or
  cross-reference target letters are i, l, or 1. Google cross-check:
  this page opens with a chapter heading, so the required blank line
  after "Página 556" means the automated script's "stop at first blank
  line" body-extraction convention reads zero body lines (a known blind
  spot, see page 505); did the manual equivalent instead, reading
  google_text_1920/page_0578.txt in full — exact word-for-word match,
  including corroborating "trienta" (not "treinta") and confirming no
  letter/word at the v.6 "fuímos" stray-mark position. Session B:
  independently re-verified all 7 Block 1 entries and all 7 `[N]` body
  markers against a fresh crop, no corrections needed. Session C
  (`insert_body_text.py 556`): body text and all 7 Block 1 entries
  appended cleanly, no blank line (same book, chapter boundary only per
  rule 20), no manual intervention needed. Session D
  (`generate_block2.py 556`): 6 of 7 entries resolved cleanly, including
  two cross-references (Véase c, Alma 48 → 2823; Véase r, Mormón 1 →
  4079, matching page 555's own entry 1r as expected). Entry 2e (Véase
  2c, IV Nefi 1) stayed unresolved, as expected — IV Nefi comes before
  Mormón in canonical order but hasn't been transcribed yet at this
  point in the project (pages being done out of canonical order); will
  resolve via a future `generate_block2.py --fix-unresolved` run once
  IV Nefi 1 is done. Session E: fresh pptext regeneration
  (`report_wsl_20260731d.html`, live WSL run). Both suspected misprints
  confirmed: "trienta" is already a documented recurring 1920 error
  pattern (prior instances at IV Nefi 1:1,1:4,1:6 and Omni 1:5) — 1886
  (pages_1886/page_0571.png, book page 553) confirms "tréinta" and the
  modern LDS Spanish edition uses "treinta"; added as a new instance at
  Mormón 2:9 in `errors in 1920.txt` (already covered in `permitted
  words.txt` via the earlier entries, no new addition needed). The
  Block 1 entry 2e semicolon anomaly was also confirmed via 1879 (no
  equivalent punctuation) and added to `errors in 1920.txt` as a
  Footnote-style entry; preserved as printed. Spellcheck Suspect Words:
  two hits, both reviewed and added to `permitted words.txt` — "Angola"
  (Book of Mormon place name, no error) and "séis" (archaic accented
  form matching 1886 exactly, consistent with this document's
  established "veintiséis" pattern). Edit Distance Checks: "séis" also
  paired against seis/dais/sois/usáis/veis, same explanation, no
  further action. "trienta" itself was not flagged by pptext's
  spellcheck section (expected — already suppressed via `permitted
  words.txt` from the earlier entries), logged regardless on the
  strength of the 1886/modern-edition comparison. Full report
  walkthrough beyond spellcheck: all remaining hits fell into
  already-established non-issue categories (short lines, the legitimate
  verse-range hyphen in "2:7-8," mixed letters/numbers in "2c"/"2j," and
  the standalone "Mormón 1:12,15" citation). Footnote scan: footnotes
  4080-4086 form one contiguous, gap-free, duplicate-free range, only
  pre-existing gap remains the long-documented footnote 812.
  Whole-document mechanical sweeps (`check_spaced_punctuation.py`/
  `check_footnote_punctuation.py`/`check_verse_indent.py`/
  `check_lines.py`) all clean against both master files (two
  pre-existing `librodm_foot.txt` lines over 79 chars, at lines 541 and
  664, are unrelated to this page and predate it). An independent
  curly-quote character scan of both master files also found zero
  curly quotes.

- **2026-08-01**: Sessions A-E run for page 557 (Mormón 2:11-20,
  continuing the same chapter opened on page 556, no book/chapter
  boundary on this page; footnotes 4087-4092, continuing chapter 2's
  own letter sequence from page 556's "g" with "h" through "m").
  Session A: 3 rule-7 hyphen rejoins (lamenta-/ción, perse-/guido,
  abomina-/ciones), none needing rule-8 rebalancing. Six rule-31
  space-before-punctuation instances normalized. A genuine zero-width
  merge in the print, v.20 "quellegamos," was transcribed as two words
  ("que llegamos") per the standing narrow-space-vs-merge default, not
  raised mid-pipeline; batched into this session's summary as an
  editor pointer per that rule's usual practice. Google cross-check
  (`check_google_crosscheck.py 557`) caught one genuine transcription
  slip missed on the first pass: v.16 "perseguieron" had been silently
  "corrected" to the grammatically-expected "persiguieron" from memory
  rather than transcribed as printed; a fresh zoomed re-read confirmed
  the image genuinely shows "perseguieron," and the text was fixed to
  match. Mandatory i/l/1 check: this chapter's own letters "i" (2i,
  "depositado") and "l" (2l, "estas") both appear on this page;
  confirmed via same-page glyph comparison and via 1879
  (pages_1879/page_0559.png, book page 551, entries h/i/j;
  pages_1879/page_0560.png, book page 552, entries k/l/m) in both
  Session A and again independently in Session B from a fresh crop —
  exact letter-for-letter and content match in both editions. Full
  1879 cross-check: all 6 Block 1 entries (2h-2m) confirmed
  reference-for-reference; entry 2l's target letter differs ("o" vs.
  1879's "g" within III Nefi 5's own lettering) — a translation-
  artifact letter mismatch per rule 26, the same phenomenon already
  logged on page 555 for a different target chapter. Block 1
  formatting normalized per this document's own conventions: entry
  2h's printed "Mormón 1:3. 4:23." → "Mormón 1:3; 4:23."; entry 2i's
  "IV Nefi 1:48, 49" (consecutive) → "48-49"; entry 2j's printed
  "Mormón 1:4. Véase I Nefi 1," (period between references, trailing
  comma instead of a period) → "Mormón 1:4; Véase I Nefi 1." — the
  1920 print itself gives no cross-reference letter before "I Nefi 1"
  there (1879's parallel entry cites letter "f"), matching this
  document's existing precedent for a letter-less book/chapter
  reference elsewhere, not treated as an error. Session B:
  independently re-verified all 6 entries/markers against a fresh
  crop, no corrections needed. Session C (`insert_body_text.py 557`):
  no book/chapter boundary on this page, so the script's normal path
  handled both body text and all 6 Block 1 entries correctly with no
  manual intervention. Session D (`generate_block2.py 557`): 5 of 6
  entries resolved cleanly to bare sequential numbers (including a
  multi-step chained resolution for entry 2l, III Nefi 5's own "o" →
  I Nefi 15's own "e" → 128, a scattering/gathering-of-Israel
  citation, consistent with I Nefi 15's own content); entry 2j (Véase
  I Nefi 1, no specific letter) stayed in letter-less book/chapter
  form as expected, not an unresolved-cross-reference case. Session E:
  fresh pptext regeneration (`report_wsl_20260801.html`, live WSL
  run). All three suspected misprints from Session A turned out to be
  genuine non-issues rather than 1920-only errors: v.15 "aflijí," v.16
  "perseguieron," and v.18 "reflección" are all confirmed via 1886
  (pages_1886/page_0571.png, book page 553; pages_1886/page_0572.png,
  book page 554) as exact matches to the 1920 reading — added to
  `permitted words.txt` ("aflijí," "reflección" — "perseguieron" was
  already present from an earlier page). Independent research
  corroborated all three beyond the 1886 match alone: RAE's Tesoro de
  los diccionarios históricos has a period entry for "aflijo" (the
  same j-spelling family); "perseguieron" (vs. modern "persiguieron")
  is a documented historical vowel-alternation variant predating the
  e→i stem-change regularization; "reflección" has no RAE DLE entry
  and zero hits in the local reference corpora, but the exact 1886
  same-lineage match is decisive regardless per the standing
  convention. The modern LDS Spanish edition (Mormón 2:15-16) wasn't
  directly comparable for any of the three, since its wording is
  independently reworded at all three spots. Spellcheck Suspect Words:
  two hits, both Book of Mormon place names ("Jashón," "Shem," v.16-
  20), added to `permitted words.txt`, no errors logged. Edit Distance
  Checks: zero hits from this page's range. Footnote scan (whole
  document): footnotes 4087-4092 contiguous, gap-free, duplicate-free,
  in-range; only pre-existing gap remains the long-documented footnote
  812. Full report walkthrough beyond spellcheck: all remaining hits
  fell into already-established non-issue categories (short lines);
  the "full stop followed by unexpected sequence" paragraph-level
  check specifically returned zero hits from this page's text (checked
  by phrase search since that subsection doesn't cite line numbers).
  Whole-document mechanical sweeps (`check_spaced_punctuation.py`/
  `check_footnote_punctuation.py`/`check_verse_indent.py`/
  `check_lines.py`) all clean against both master files; an independent
  curly-quote character scan of both master files also found zero
  curly quotes. Also backfilled this session: `sessions-log.md` was
  missing entries for both page 555 (existed only in CLAUDE.md's
  Current Progress snapshot, never appended here) and page 556 (fully
  completed A-E per the master files' own content, but never logged
  anywhere at all) — both were reconstructed from the master files and
  page_556.txt's own Corrections log and inserted immediately before
  this entry, in chronological order.
- **2026-08-01**: Sessions A–E run for page 557 (Mormón 2:11-20,
  continuing the same chapter opened on page 556, no book/chapter
  boundary on this page; footnotes 4087-4092, continuing chapter 2's
  own letter sequence from page 556's "g" with "h" through "m").
  Session A: 3 rule-7 hyphen rejoins (lamenta-/ción, perse-/guido,
  abomina-/ciones), none needing rule-8 rebalancing. Six rule-31
  space-before-punctuation instances normalized. A genuine zero-width
  merge in the print, v.20 "quellegamos," was transcribed as two words
  ("que llegamos") per the standing narrow-space-vs-merge default, not
  raised mid-pipeline; batched into this session's summary as an
  editor pointer per that rule's usual practice. Google cross-check
  (`check_google_crosscheck.py 557`) caught one genuine transcription
  slip missed on the first pass: v.16 "perseguieron" had been silently
  "corrected" to the grammatically-expected "persiguieron" from memory
  rather than transcribed as printed; a fresh zoomed re-read confirmed
  the image genuinely shows "perseguieron," and the text was fixed to
  match. Mandatory i/l/1 check: this chapter's own letters "i" (2i,
  "depositado") and "l" (2l, "estas") both appear on this page;
  confirmed via same-page glyph comparison and via 1879
  (pages_1879/page_0559.png, book page 551, entries h/i/j;
  pages_1879/page_0560.png, book page 552, entries k/l/m) in both
  Session A and again independently in Session B from a fresh crop —
  exact letter-for-letter and content match in both editions. Full
  1879 cross-check: all 6 Block 1 entries (2h-2m) confirmed
  reference-for-reference; entry 2l's target letter differs ("o" vs.
  1879's "g" within III Nefi 5's own lettering) — a translation-
  artifact letter mismatch per rule 26, the same phenomenon already
  logged on page 555 for a different target chapter. Block 1
  formatting normalized per this document's own conventions: entry
  2h's printed "Mormón 1:3. 4:23." → "Mormón 1:3; 4:23."; entry 2i's
  "IV Nefi 1:48, 49" (consecutive) → "48-49"; entry 2j's printed
  "Mormón 1:4. Véase I Nefi 1," (period between references, trailing
  comma instead of a period) → "Mormón 1:4; Véase I Nefi 1." — the
  1920 print itself gives no cross-reference letter before "I Nefi 1"
  there (1879's parallel entry cites letter "f"), matching this
  document's existing precedent for a letter-less book/chapter
  reference elsewhere, not treated as an error. Session B:
  independently re-verified all 6 entries/markers against a fresh
  crop, no corrections needed. Session C (`insert_body_text.py 557`):
  no book/chapter boundary on this page, so the script's normal path
  handled both body text and all 6 Block 1 entries correctly with no
  manual intervention. Session D (`generate_block2.py 557`): 5 of 6
  entries resolved cleanly to bare sequential numbers (including a
  multi-step chained resolution for entry 2l, III Nefi 5's own "o" →
  I Nefi 15's own "e" → 128, a scattering/gathering-of-Israel
  citation, consistent with I Nefi 15's own content); entry 2j (Véase
  I Nefi 1, no specific letter) stayed in letter-less book/chapter
  form as expected, not an unresolved-cross-reference case. Session E:
  fresh pptext regeneration (`report_wsl_20260801.html`, live WSL
  run). All three suspected misprints from Session A turned out to be
  genuine non-issues rather than 1920-only errors: v.15 "aflijí," v.16
  "perseguieron," and v.18 "reflección" are all confirmed via 1886
  (pages_1886/page_0571.png, book page 553; pages_1886/page_0572.png,
  book page 554) as exact matches to the 1920 reading — added to
  `permitted words.txt` ("aflijí," "reflección" — "perseguieron" was
  already present from an earlier page). Independent research
  corroborated all three beyond the 1886 match alone: RAE's Tesoro de
  los diccionarios históricos has a period entry for "aflijo" (the
  same j-spelling family); "perseguieron" (vs. modern "persiguieron")
  is a documented historical vowel-alternation variant predating the
  e→i stem-change regularization; "reflección" has no RAE DLE entry
  and zero hits in the local reference corpora, but the exact 1886
  same-lineage match is decisive regardless per the standing
  convention. The modern LDS Spanish edition (Mormón 2:15-16) wasn't
  directly comparable for any of the three, since its wording is
  independently reworded at all three spots. Spellcheck Suspect Words:
  two hits, both Book of Mormon place names ("Jashón," "Shem," v.16-
  20), added to `permitted words.txt`, no errors logged. Edit Distance
  Checks: zero hits from this page's range. Footnote scan (whole
  document): footnotes 4087-4092 contiguous, gap-free, duplicate-free,
  in-range; only pre-existing gap remains the long-documented footnote
  812. Full report walkthrough beyond spellcheck: all remaining hits
  fell into already-established non-issue categories (short lines);
  the "full stop followed by unexpected sequence" paragraph-level
  check specifically returned zero hits from this page's text (checked
  by phrase search since that subsection doesn't cite line numbers).
  Whole-document mechanical sweeps (`check_spaced_punctuation.py`/
  `check_footnote_punctuation.py`/`check_verse_indent.py`/
  `check_lines.py`) all clean against both master files; an independent
  curly-quote character scan of both master files also found zero
  curly quotes.

- **2026-08-01**: Sessions A–E run for page 558 (Mormón 2:21-29, closing
  the chapter opened on page 556, then CAPÍTULO 3 opens mid-page with
  vv.1-2, cut off mid-verse; footnotes 4093-4097, chapter 2's own
  letter sequence continuing from page 557's "m" with "n" through "r";
  no footnotes yet in chapter 3's own opening verses on this page).
  Session A: 1 rule-7 hyphen rejoin (exhor-/tándoles), well under the
  73-char cap, no rule-8 rebalancing needed. Seven rule-31
  space-before-punctuation instances normalized, plus four
  justification-widened double-spaces. Two narrow-space-vs-merge
  defaults applied per the standing rule (v.21 "ciudad de Shem," v.26
  "por lo tanto"), batched into this session's summary as editor
  pointers rather than raised mid-pipeline. Two suspected misprints
  investigated at transcription time: CAP.3 v.1 "sus tierras armas"
  shows a distinctly wide gap with no connecting word present, zoom-
  confirmed; both 1886 (pages_1886/page_0573.png, book page 555) and
  1879 (pages_1879/page_0561.png, book page 553) confirm a missing "y,"
  so this was promoted to `errors in 1920.txt` in Session E. v.26's
  "vimos" initially looked like it might read "vimbs" at moderate zoom;
  a very high zoom crop showed the extra mark is an ink blob on an
  ordinary "o" bowl rather than a genuine ascender, and this was
  independently corroborated by both the Google OCR cross-check
  (`check_google_crosscheck.py 558`, which read "vimos" at that exact
  position) and 1886 (same page, "vímos") — resolved as print damage,
  not a misprint, no `errors in 1920.txt` entry. Mandatory i/l/1 check:
  this page's own chapter-2 letters (n-r) contain no i/l/1, but two
  cross-reference target codes (2o, 2q) are hard-to-read two-character
  swash forms ("2c," "2v"); confirmed via 1879 (pages_1879/page_0560.png,
  book page 552, entry o; pages_1879/page_0561.png, book page 553,
  footnote line below v.9, entry q) in both Session A and again
  independently in Session B from a fresh crop — exact match in both.
  Full 1879 cross-check: all 5 Block 1 entries (2n-2r) confirmed
  reference-for-reference, no translation-artifact letter mismatches
  this page. Session B: independently re-verified all 5 entries/markers
  against a fresh crop, no corrections needed. Session C
  (`insert_body_text.py 558`): no book/chapter boundary within Mormón,
  so the script's normal path handled both body text and all 5 Block 1
  entries correctly with no manual intervention. Session D
  (`generate_block2.py 558`): all 5 entries resolved cleanly to bare
  sequential numbers, including entry 2q's resolution to 2248 (Alma
  22's own "2v" entry), whose own reference text already cited forward
  to "Mormón 2:29" from whenever Alma 22 was originally transcribed —
  confirmed as a pre-existing forward citation, not a new circular
  reference. Session E: fresh pptext regeneration
  (`report_wsl_20260801b.html`, live WSL run). Spellcheck Suspect
  Words: one hit, "energicamente" (v.23) — confirmed via 1886
  (pages_1886/page_0572.png, book page 554) as an exact match to the
  1920 reading (same unaccented spelling), added to `permitted
  words.txt`, no error logged. RAE DLE has no entry for the unaccented
  form and all three local reference corpora returned zero hits for
  it, consistent with a simple missing-accent case (1886 omits it too)
  rather than a genuine misspelling. Edit Distance Checks: zero hits
  from this page's range. Footnote scan (whole document): footnotes
  4093-4097 contiguous, gap-free, duplicate-free, in-range (footnote
  4094's separate listing in the report is a line-start bucketing
  quirk, not a defect); only pre-existing gap remains the long-
  documented footnote 812. Full report walkthrough beyond spellcheck:
  all remaining hits fell into already-established non-issue
  categories (short lines). Whole-document mechanical sweeps
  (`check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py`/`check_lines.py`) all clean against both
  master files; an independent curly-quote character scan of both
  master files also found zero curly quotes. `check_line_wrap.py`'s
  advisory OCR line-count cross-check flagged this page (33 vs. 38);
  re-verified by recounting the raw print lines directly against the
  image crops (39 total content lines, matching this file exactly) —
  treated as the tool's own quirk around the chapter-heading boundary,
  not a transcription defect.
- **2026-08-01**: Sessions A–E run for page 559 (Mormón 3:2-12, all
  within chapter 3, opened mid-page on 558; footnotes 4098-4103,
  chapter 3's own letter sequence starting fresh at "a" through "f"
  since chapter 3 had no footnotes yet on page 558). Session A: 4
  rule-7 hyphen rejoins (apo-/deraran, ba-/talla, matán-/doles,
  abomina-/ciones — the last fully consumed its raw second line since
  nothing but the hyphen remainder was on it), all well under the
  73-char cap, no rule-8 rebalancing needed. Nine rule-31
  space-before-punctuation instances normalized, plus three
  justification-widened double-spaces. No narrow-space-vs-merge
  defaults needed this page. One suspected misprint investigated at
  transcription time and resolved as normal print, not a misprint:
  v.12 "corazón" looked at standard zoom like the accent might be a
  fused "b" (same visual phenomenon as page 558's "vimos"/"vimbs"
  case); a 30x crop isolated to just that letter showed an ordinary
  acute accent above a normal "o" bowl, later corroborated against
  1886 (pages_1886/page_0574.png, book page 556, same word, unaccented
  "corazon") in Session E — no `errors in 1920.txt` entry. Google-text
  cross-check (`check_google_crosscheck.py 559`) surfaced 2 candidates
  beyond the auto-dismissed footnote-marker-glue noise, both resolved
  as OCR noise (a superscript-letter glue variant just past the
  auto-dismiss threshold near v.2, and a stray printer's-ornament dot
  google inserted near the v.10/11 boundary) — no corrections needed.
  Mandatory i/l/1 check: this page's own chapter-3 lettering (a-f) has
  no i/l/1 directly, but two cross-reference target codes (3b, 3f)
  are hard-to-read swash "2l" forms; confirmed via 1879
  (pages_1879/page_0561.png, book page 553) in both Session A and
  independently again in Session B from a fresh crop — exact match
  both times, 1879's clearer serif font leaving no ambiguity. Full
  1879 cross-check: all 6 Block 1 entries (3a-3f) confirmed
  reference-for-reference, no translation-artifact letter mismatches
  this page. Session B: independently re-verified all 6 entries/markers
  against a fresh crop, no corrections needed. Session C
  (`insert_body_text.py 559`): no book/chapter boundary within Mormón,
  handled body text and all 6 Block 1 entries correctly with no manual
  intervention. Session D (`generate_block2.py 559`): all 6 entries
  resolved cleanly to bare sequential numbers, including both 3b and
  3f resolving to the same target (2248, Alma 22's own "2v" entry) and
  3e/page 558's 2n both resolving to 2823 (Alma 48's own "c" entry) —
  consistent cross-page resolution, not a new circular reference.
  Session E: fresh pptext regeneration (`report_wsl_20260801c.html`,
  live WSL run). Spellcheck Suspect Words: zero hits from this page's
  range. Edit Distance Checks: zero hits from this page's range.
  Footnote scan (whole document): footnotes 4098-4103 contiguous,
  gap-free, duplicate-free, in-range; only pre-existing gap remains
  the long-documented footnote 812. Full report walkthrough beyond
  spellcheck: all hits in this page's line ranges fell into the
  already-established "short lines check" non-issue category.
  Whole-document mechanical sweeps
  (`check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py`/`check_lines.py`) all clean against both
  master files (two pre-existing `check_lines.py` hyphen-rejoin
  advisories are on unrelated earlier pages); an independent
  curly-quote character scan of both master files also found zero
  curly quotes. `check_line_wrap.py` advisory OCR cross-check: no red
  flag (42 OCR-estimated vs. 43 transcribed, well within the tool's
  own advisory tolerance).

- **2026-08-01**: Sessions A–E run for page 560 (Mormón 3:13-22, all
  within chapter 3, continuing page 559's letter sequence at "g"
  through "r", 12 entries; footnotes 4104-4115). Session A: 1 rule-7
  hyphen rejoin (cruci-/ficaron -> crucificaron) that hit exactly 73
  chars after a naive rejoin, so rule 8 rebalancing moved the whole
  word to start the next line instead (matching page 559's
  "abomina-/ciones" precedent). Eleven rule-31 space-before-punctuation
  instances normalized. Five suspected misprints investigated
  immediately against 1886 (not deferred to Session E, since the 1886
  lookup was already open for other work this page): v.14 "por. sí"
  (genuine extraneous period, confirmed absent in 1886) and v.16
  "postrar" (1886/modern-edition both read "mostrar" — "to show," the
  only grammatical fit) and v.20's missing semicolon after "Adam"
  (1886 has one) and v.21 "mimo" (1886 reads "mismo") all confirmed as
  genuine 1920-only errors and logged in `errors in 1920.txt`; a fifth,
  v.16's smaller mark after "el," was initially transcribed as a
  period ("el. Señor") and flagged rather than logged, since it read
  differently from v.14's clean period — the editor's own look at the
  page (a snip, `el-dot-Senor.png`) confirmed it's a tiny scan speck,
  not print, so it was corrected to plain "el Señor" in both
  `pages/page_560.txt` and `librodm.txt`, not logged as an error. Mandatory i/l/1 check: this page's own
  lettering includes both "i" (Mormón 6) and "l" (I Nefi 12:9);
  confirmed via 1879 (pages_1879/page_0562.png, book page 554) in both
  Session A and independently again in Session B from a fresh crop —
  exact match both times. Full 1879 cross-check: all 12 Block 1
  entries (3g-3r) confirmed reference-for-reference against
  pages_1879/page_0562.png (entries g-o) and page_0563.png (entries
  p-r, book page 555), including the "g" first-letter identification
  itself (alphabetical continuation from page 559's final "f",
  independently corroborated by 1879's own clearer type). Rule 23
  formatting applied to entry g ("Versículos 7,8" -> "7-8"), h ("9,10"
  -> "9-10"), and p ("41,42" trailing an existing range -> "41-42"),
  matching established document convention. Session B: independently
  re-verified all 12 entries/markers against a fresh crop, no
  corrections needed. Session C (`insert_body_text.py 560`): no book/
  chapter boundary within Mormón, handled body text and all 12 Block 1
  entries correctly with no manual intervention. Session D
  (`generate_block2.py 560`): all 12 entries resolved cleanly to bare
  sequential numbers (targets in already-transcribed I/II/III Nefi),
  none left as unresolved letter forms. Session E: fresh pptext
  regeneration (`report_wsl_20260801d.html`, live WSL run). Spellcheck
  Suspect Words: one hit from this page's range, "determinadamente"
  (v.16) — confirmed via 1886 (identical word at the parallel spot)
  and RAE's Tesoro de los diccionarios históricos (a legitimate,
  standardly-formed -mente adverb simply absent from aspell's Spanish
  dictionary); added to `permitted words.txt`, no error logged. Edit
  Distance Checks: zero hits from this page's range. Footnote scan
  (whole document, computed directly from `[N]` markers): footnotes
  4104-4115 contiguous, gap-free, duplicate-free, in-range; only
  pre-existing gap remains the long-documented footnote 812. Full
  report walkthrough beyond spellcheck: all remaining hits in this
  page's line ranges fell into the already-established "short/long
  lines check" non-issue category. Whole-document mechanical sweeps
  (`check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py`/`check_lines.py`) all clean against both
  master files; an independent curly-quote character scan of both
  master files also found zero curly quotes. `check_line_wrap.py`
  advisory OCR cross-check: no red flag (42 OCR-estimated vs. 42
  transcribed, exact match).
- **2026-08-01**: Sessions A–E run for page 561 (Mormón 4:1-10, a new
  chapter opening — CAPÍTULO 4 begins right at the top of the page
  with no subtitle, letters restart at "a", 7 entries; footnotes
  4116-4122). Session A: 1 rule-8 rebalancing (v.1's inserted
  `[4116]` marker pushed the line to 74 chars, so "ejércitos" moved
  to start the next line) and 1 rule-7 hyphen rejoin (v.10
  "continua-/mente" -> "continuamente", well under the cap, no
  further rebalancing needed). Six rule-31 space-before-punctuation
  instances normalized. Two double-space justification artifacts
  normalized to single spaces (v.3, v.8). Mandatory i/l/1 check: this
  chapter's own lettering (a-g) has no i/l/1 directly, but four
  "Véase" cross-references (entries a, b, d, g) target Alma 22's own
  two-letter "2l" code, which falls in the mandatory set — confirmed
  via 1879 (pages_1879/page_0563.png, book page 555, entries a-f, and
  page_0564.png, book page 556, entry g) in both Session A and
  independently again in Session B from a fresh crop — exact match
  both times, resolving a swash-font ambiguity between "l" and "2l"
  that the 1920 image alone couldn't settle. Full 1879 cross-check:
  all 7 Block 1 entries (4a-4g) confirmed reference-for-reference,
  including body-marker placement and a content-fit check (a/b/d/g
  all annotate "país/ciudad de Desolación", matching Alma 22's
  geography content; c/e both annotate "ciudad de Teáncum"; f's
  "Mormón 3:9" matches the chapter 3 boasting precedent for v.8's
  "se jactaron otra vez"). One narrow-space-vs-merge default applied
  per the established editor-guidance rule (v.10 "que se había",
  1920 print shows the words essentially touching but grammar
  requires two words) — not raised as a standalone question, batched
  into this session's summary and additionally corroborated by 1886
  printing normal unmerged spacing at the parallel spot. One
  preserved-as-printed accent note (v.5 "por quiénes") checked
  against 1886 in Session E rather than flagged as an error — 1886
  reads unaccented "por quienes", confirming the 1920 accent is the
  same house-style addition already established for "dónde" (v.3
  here and prior pages' Corrections logs), not a substantive error;
  no `errors in 1920.txt` or `permitted words.txt` entry needed.
  `check_line_wrap.py`/`check_google_crosscheck.py` both reported 0
  body lines for this page — a pre-existing tool limitation (their
  shared body-extraction heuristic stops at the first blank line
  after "Página N", which here is the blank line before the chapter
  heading itself), confirmed not page-specific by reproducing the
  identical 0-line result on page 556 (an earlier accepted page with
  the same opens-with-chapter-heading structure); the actual rule 5/6
  per-line image read was still done directly against the crops.
  Session B: independently re-verified all 7 Block 1 entries and all
  7 `[N]` body markers against a fresh `process_page.py` crop, no
  corrections needed. Session C (`insert_body_text.py 561`): no book
  boundary (still within Mormón), handled body text and all 7 Block 1
  entries correctly with no manual intervention. Session D
  (`generate_block2.py 561`): all 7 entries resolved cleanly — the
  four "2l" cross-references all resolved to Alma 22's own sequential
  number 2238, and entry e's "Véase c" resolved to this page's own
  entry c (4118). Session E: fresh pptext regeneration
  (`report_wsl_20260801e.html`, live WSL run). Spellcheck Suspect
  Words: zero hits from this page's range. Edit Distance Checks: zero
  hits from this page's range. Footnote scan (whole document,
  computed directly from `[N]` markers): footnotes 4116-4122
  contiguous, gap-free, duplicate-free, in-range; only pre-existing
  gap remains the long-documented footnote 812. Full report
  walkthrough beyond spellcheck: special situations and
  paragraph-level checks (including "full stop followed by
  unexpected sequence") produced zero hits from this page's content.
  Whole-document mechanical sweeps
  (`check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py`) all clean against both master files; an
  independent curly-quote character scan of both master files also
  found zero curly quotes. No new `permitted words.txt` or `errors in
  1920.txt` entries resulted from this page.
- **2026-08-01**: Sessions A–E run for page 563 (Mormón, chapter
  boundary: chapter 4 closes on page 562, chapter 5 opens here with
  `CAPÍTULO 5.` immediately after `Página 563` per the established
  chapter-opening convention -- no subtitle line present at this
  opening, confirmed by checking the actual image; footnotes
  4131-4134, letters a-d). Session A: 5 rule-31 space-before-semicolon
  instances normalized (v.3, 5 x2, 6, 7). 2 rule-7 hyphen rejoins
  (v.1 considerán-/dome -> considerándome, 69 chars; v.5 ar-/ruinadas
  -> arruinadas, 69 chars), neither requiring rule-8 rebalancing. No
  i/l/1 letters anywhere on this page (footnote letters run a-d only,
  and cross-reference target letter "c" in entry 5c, "Véase c, II Nefi
  27," is not in the mandatory set), so the Section 8 1879 cross-check
  did not apply -- confirmed and noted explicitly rather than silently
  skipped. Footnote 5d's citation ("III Nefi 16:8 9; 20:27, 28.")
  prints no comma between the consecutive verses 8 and 9, just an
  unusually wide gap (confirmed via high-zoom crop and independently
  corroborated by Google's own OCR reading the identical gap); since
  rule 23 already normalizes consecutive verse numbers to a hyphenated
  range regardless of source punctuation, this became "16:8-9" like
  the entry's other bare-verse-list citations without needing an
  `errors in 1920.txt` entry (footnotes have no 1886 typesetting to
  compare against in the first place, per the Reference PDFs section).
  One other footnote-5d gap (before "10:18") was a justification
  artifact, normalized to one space per rule 6. `check_line_wrap.py`
  and `check_google_crosscheck.py` both returned 0/empty for this page
  -- the known, previously-documented tool limitation for any page
  whose body text starts with a chapter heading immediately after
  `Página N` (their shared body-extraction helper stops at that first
  blank line; same root cause as pages 536, 559, 570). Worked around
  manually: `check_line_wrap.py`'s own OCR line-count estimate (39)
  landed within 1 of the true hand-counted total (40), and a full
  manual read of `google_text_1920/page_0585.txt` against the page's
  body text and footnote block found an exact match throughout
  (including the footnote-d "16:8 9" gap, independently reproduced by
  Google's OCR) -- no reflow, no undetected misreads. Google's OCR did
  drop one letter elsewhere ("no quero" for "no quiero," v.8), a known
  OCR weak spot, not a transcription error (confirmed via direct zoom
  that the image plainly prints "quiero" in full). Session B:
  independently re-verified all 4 Block 1 entries and all 4 `[N]` body
  markers against a fresh `process_page.py` crop (page label 563b, not
  reused from Session A) -- exact match, no corrections needed.
  Session C (`insert_body_text.py 563`): no book-boundary header
  needed (still within Mormón, just a new chapter), body text and all
  4 Block 1 entries inserted cleanly. Session D (`generate_block2.py
  563`): all 4 entries resolved cleanly on first pass, including
  entry 5c's "Véase c, II Nefi 27" resolving to sequential number 682
  -- sanity-checked directly against the identical resolution already
  on record for this same target from page 536's session ("3904->682
  II Nefi 27c"), an exact match confirming both the cross-reference
  reading and the existing index entry. Session E: fresh pptext
  regeneration (`report_wsl_20260801g.html`, live WSL run). Spellcheck
  Suspect Words and Edit Distance Checks: zero hits from this page's
  range (the 6 pre-existing flagged words in the report all sit well
  before page 563's line range, unrelated to this session). Footnote
  scan (whole document, computed directly from `[N]` markers):
  footnotes 4131-4134 contiguous, gap-free, duplicate-free, in-range;
  only pre-existing gap remains the long-documented footnote 812.
  Whole-document mechanical sweeps (`check_spaced_punctuation.py`/
  `check_footnote_punctuation.py`/`check_verse_indent.py`) all clean
  against both master files; an independent curly-quote character scan
  of both master files also found zero curly quotes. Walked the
  character-checks, hyphenation (both non-hyphenated and spaced-pair),
  dash-check (hyphen-minus bucket confirms footnotes 4132/4134's
  verse-range hyphens match the established no-space convention), and
  special-situations sections of the full pptext report and confirmed
  no new page-563-specific findings in any of them -- the only
  page-563 citations that surfaced were in already-cleared categories
  (short-lines check, on every Block 2 entry by construction; the
  paragraph-level "unexpected paragraph end" false positive, since
  this page's last transcribed line is currently the true end of the
  body-text section pending page 564). No new `permitted words.txt` or
  `errors in 1920.txt` entries resulted from this page -- no suspected
  1920 printing errors were found in the body text or footnotes.
- **2026-08-02**: Sessions A–E run for page 564 (Mormón 5, verses
  9(cont.)-19; footnotes 4135-4145, letters e-o). Session A: page
  continues verse 9 mid-sentence from page 563. 11 footnote markers
  (e-o) placed and matched letter-for-letter against a fresh 1879
  cross-check (chapter_map file pages 566-567) covering all of this
  page's own footnote content and body-marker placement -- exact match
  throughout. The mandatory i/l/1 check (Section 8) caught a genuine
  misread: entry 5o's cross-reference target letter, first read as "i"
  from the fn_zoom overview ("Véase i; Mormón 4"), was shown by 1879's
  clear "o, see j, Mor. 4." to actually be "j" -- confirmed on the 1920
  image itself via high-zoom shape comparison against this page's own
  "i" (plain stroke + separate dot) and "j" (stroke with a below-
  baseline hook) specimens; the disputed glyph matches "j". Corrected
  to "Véase j; Mormón 4." Two other findings: v.9 "que he recibido" and
  v.18 "he aquí" have justification-narrowed (but real, unambiguous)
  inter-word gaps, normalized per rule 6, not escalated to the editor
  since no single-word reading is grammatically plausible either way
  (unlike the "quefueron"-style ambiguous case rule 6 asks Session E to
  flag). V.15 "idolatría" prints with a genuine internal gap,
  "idola tría," confirmed via high-zoom crop as real ink (not
  justification kerning) and confirmed against 1886's unsplit
  "idolatría" at the same spot -- preserved as printed, later promoted
  to `errors in 1920.txt` in Session E. 12 rule-31 space-before-
  semicolon instances normalized. No rule-7 hyphen rejoins needed (no
  line-break hyphens anywhere on the page). `check_line_wrap.py`/
  `check_google_crosscheck.py` both ran cleanly (43 transcribed lines
  vs. 44 OCR estimate; zero cross-check candidates after the routine
  footnote-marker/glue dismissals). Session B: independently
  re-verified all 11 Block 1 entries and all 11 `[N]` body markers
  against a fresh crop (page label 564b) -- exact match, including the
  "idola tría" gap and the resolved letter "j." Session C
  (`insert_body_text.py 564`): caught and fixed a real omission --
  the page's own `Página 564` header line (rule 1) had been left out of
  the Session A draft entirely (this page continues mid-verse from 563,
  so the omission wasn't visually obvious), only surfacing once the
  script's insertion left a bare blank line in `librodm.txt` where the
  header belonged. Fixed in both `pages/page_564.txt` and the
  already-inserted copy in `librodm.txt`. Session D
  (`generate_block2.py 564`): 9 of 11 entries resolved automatically;
  entries 4135 ("Véase a; Mormón 1.") and 4145 ("Véase j; Mormón 4.")
  were left unresolved because the script's cross-reference parser only
  splits the letter from the Book/Chapter clause on a comma, not a
  semicolon -- 1879's comma-form equivalents ("e, see a, Mor. 1.", "o,
  see j, Mor. 4.") confirm these are the same single-reference pattern
  as the comma-form entries elsewhere on this page, just printed with a
  semicolon. Resolved by hand against `librodm_foot.txt`'s own index
  (Mormón 1a = 4062, Mormón 4j = 4125) and fixed directly in
  `librodm.txt`'s Notas section. Three older `librodm_foot.txt` entries
  (29c/740, 5g/861, 22-2r/2244) show this same semicolon pattern and
  were apparently hand-resolved the same way previously -- a known,
  unfixed script limitation, not addressed here per scope. Session E:
  fresh pptext regeneration (`report_wsl_20260802.html`, live WSL run).
  Only "idola" (from the already-logged "idola tría" gap) appeared in
  Spellcheck Suspect Words from this page's range; added to `permitted
  words.txt` as a genuine documented error being preserved as printed.
  Independent research (mandatory regardless of pptext's silence) found
  a second, pptext-unflagged error: v.16 "rastojo" is missing its first
  "r" ("rastrojo") -- confirmed against 1886's correct "rastrojo" at
  the same spot, RAE DLE having no entry at all for "rastojo," and zero
  corpus hits for "rastojo" vs. 2 for "rastrojo" in Quijote (modern
  edition uses the unrelated word "paja" here, not directly comparable
  since it's an independent translation). Both errors added to `errors
  in 1920.txt` (Mormón 5:15, 5:16); "idola"/"rastojo" added to
  `permitted words.txt`. Whole-document mechanical sweeps
  (`check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py` against both master files, a curly-quote
  character scan, and a footnote-anchor continuity scan of the whole
  body) all clean -- 4144 anchors spanning 1-4145, zero duplicates,
  zero out-of-range, only the pre-existing footnote-812 gap remains. No
  new hyphen compounds or adjacent-dash instances on this page.
- **2026-08-02**: Sessions A-E run for page 565 (Mormón 5, verses
  19(cont.)-24, plus Mormón 6, verses 1-6(partial); footnotes 4146-4153,
  letters p-u then chapter 6's a-b). Session A: page continues verse 19
  mid-sentence from page 564; chapter 6 opens partway down the page with
  no subtitle line, and the page ends mid-word on a page-boundary
  hyphen split ("Mor-", to be rejoined once page 566 is transcribed per
  rule 10). None of this page's 8 footnote letters (p,q,r,s,t,u,a,b) or
  cross-reference targets (d,c,o) are i/l/1, so the mandatory Section 8
  check didn't apply; letter identity was corroborated instead by exact
  content-match against the six-entry chapter-5 footnote block (p-u)
  and content-fit against chapter 6's a-b block. 3 rule-31
  space-before-punctuation instances normalized (v.22 "caminos !", v.24
  "vuestra ; ó", cap.6 v.4 "fuentes ;"); one rule-6 widened-gap
  normalization (v.23 "Dios?  ¿No" -> "Dios? ¿No"); Block 1 verse-range
  reformatting per rules 23-25 (commas -> hyphens for consecutive
  verses) in entries 5p, 5s, 6a, 6b. A first draft incorrectly split
  the cap.6 v.5 line early (moved "años," to the next line) before
  double-checking against the image showed the full original line with
  its footnote marker fit under 72 chars intact -- caught and fixed
  before finalizing, a reminder that rule 7/8 rebalancing should only
  be applied after confirming the unrebalanced line actually doesn't
  fit, not preemptively. Several small isolated ink/scan specks
  scattered near line ends throughout the page (including one right
  between the "q" and "r" markers) were checked against the possibility
  of being a missed 7th footnote letter but ruled out, since the Block 1
  list for this section contains exactly six entries (p-u) matching the
  six body superscripts with no seventh. `check_line_wrap.py` flagged a
  large mismatch (18 vs. 37 lines) that turned out to be a script
  limitation, not a reflow defect: its body-line reader stops at the
  first blank line, which this page hits early (the blank line before
  "CAPÍTULO 6."), so it only saw the chapter-5 tail while Tesseract OCR'd
  the whole page; the counts reconcile exactly once that's accounted
  for (38 total non-blank lines minus 1 for the OCR's own header-regex
  filter = 37). `check_google_crosscheck.py` found zero candidates.
  Session B: independently re-verified all 8 Block 1 entries and all 8
  `[N]` body markers against a fresh crop (page label 565b) -- exact
  match throughout, including marker placement and the "Mor-"
  page-boundary hyphen. Session C (`insert_body_text.py 565`): clean
  insertion, no issues. Session D (`generate_block2.py 565`): all 8
  entries auto-resolved with no manual intervention, including the
  letter-only cross-reference "5q, Véase d." -> 4134. Session E: fresh
  pptext regeneration (`report_wsl_20260802b.html`, live WSL run). Only
  "Manchester" (a real English place name in footnote 6a) appeared in
  Spellcheck Suspect Words from this page's range -- added to
  `permitted words.txt` as an expected proper-noun flag, not an error.
  Independent research on a Corrections-log-flagged item found a
  genuine error: footnote 6a prints "nueva York" with a lowercase "n"
  despite being a proper place name; 1886 has no footnotes to compare,
  but 1879's matching footnote prints "N. York" capitalized, and this
  same document already uses "Nueva York" correctly elsewhere (footnote
  699, "Profesor Anthon de Nueva York") -- confirmed as a genuine 1920
  inconsistency and added to `errors in 1920.txt` (Mormón 6, nota a). A
  targeted search of the full pptext report for this page's distinctive
  vocabulary (edit distance, hyphenation, special-situations sections)
  found nothing else in this page's range beyond expected structural
  noise (short-lines check). Whole-document mechanical sweeps
  (`check_spaced_punctuation.py`/`check_footnote_punctuation.py`/
  `check_verse_indent.py` against both master files, a curly-quote
  character scan, and a footnote-anchor continuity scan of the whole
  body) all clean -- 4152 anchors spanning 1-4153, zero duplicates,
  zero out-of-range, only the pre-existing footnote-812 gap remains. No
  new hyphen compounds or adjacent-dash instances on this page.
- **2026-08-02**: Sessions A–E run for page 565 (Mormón 5, verses
  19(cont.)-24, plus Mormón 6, verses 1-6(partial); footnotes 4146-4153,
  letters p-u then chapter 6's a-b). Session A: no i/l/1 letters on this
  page, so letter identity was corroborated via exact content-match
  against the footnote block instead of the mandatory 1879 check. Page
  ends mid-word on a page-boundary hyphen ("Mor-", rule 10 — to be
  rejoined once page 566 is transcribed). Caught and fixed a
  self-introduced error before finalizing: an early draft split the
  cap.6 v.5 line one word too soon ("años," moved down) when the full
  original line actually fit under 72 chars with its footnote marker.
  3 rule-31 space fixes, 1 rule-6 gap fix, Block 1 verse-range
  reformatting (rules 23-25) in 4 entries. `check_line_wrap.py`'s
  large-looking mismatch (18 vs. 37 lines) was a script limitation
  (stops at the first blank line, which this page hits early at the
  chapter-6 heading), not a reflow defect — counts reconcile once
  accounted for. Session B: fresh crop (565b) confirmed all 8 Block 1
  entries/markers exact match. Session C/D: clean, no manual
  intervention needed (`generate_block2.py` auto-resolved all 8
  entries). Session E: fresh pptext regeneration
  (`report_wsl_20260802b.html`). Only "Manchester" flagged (proper
  noun, added to `permitted words.txt`). Independent research on a
  Corrections-log item confirmed a genuine error: footnote 6a's "nueva
  York" (lowercase) vs. 1879's capitalized "N. York" and this
  document's own correct "Nueva York" elsewhere (footnote 699) — added
  to `errors in 1920.txt` (Mormón 6, nota a). Whole-document mechanical
  sweeps all clean — 4152 anchors, zero duplicates/out-of-range, only
  the pre-existing footnote-812 gap remains.
- **2026-08-02**: Sessions A–E run for page 566 (Mormón 6, verses
  6(cont.)-15(partial); footnotes 4154-4164, letters c-m). Session A:
  resolved page 565's trailing "Mor-" page-boundary split (rule 10) —
  appending "Mormón," to page 565's last line kept it at 61 chars, so
  the whole word moved there and page 566 begins with "empezaba"
  instead; revised `pages/page_565.txt` and its already-integrated copy
  in `librodm.txt` to match. Letters i and l both present in this
  page's own lettering (mandatory Section 8 check): resolved via a full
  1879 page-image read (file pages 567-569, not a same-crop re-read) —
  both d and i cross-reference the swash-digit target "2f, IV Nefi 1"
  (confirmed via 1879's "see 2f, IV. Nep. 1", twice), k targets "2p,
  Alma 43", l targets bare "a", and m's "Versículo II" is confirmed to
  be the digits "11" (this font's small swash numerals resembling Roman
  "II" at a glance), not an actual Roman numeral, via 1879's "m, ver.
  11." All 11 entries (not just the mandatory two) cross-checked
  against 1879 given the font's frequent 2/s ambiguity. Rule-8
  rebalancing cascaded across three consecutive lines once footnote
  markers were inserted into a dense stretch ("planchas de Nefi ...
  escondí ... cerro de Cumórah ... habían sido"). Session D: a
  Block-1-to-Block-2 resolution failure was traced to the page's own
  Block 1 print anomaly — footnote 6f/4157 originally transcribed
  literally as "I Nefi.1." (a period where every sibling entry in the
  same footnote block has a space) broke `generate_block2.py`'s
  book/chapter regex; reconsidered under rules 16-25 (which already
  normalize Block 1 reference punctuation regardless of print, e.g. the
  comma-to-hyphen verse-range rule) rather than rule 32's body-text
  verbatim standard, and normalized to "I Nefi 1." in both
  `pages/page_566.txt` and `librodm_foot.txt`; the already-appended
  Block 2 line was hand-resolved to "Véase 6." (I Nefi ch. 1 letter f).
  Session E: fresh pptext/WSL regeneration
  (`report_wsl_20260802c.html`, following on from 565's
  `...802b.html` — renamed from a bare `...802.html` after publishing
  to avoid clobbering that same-day file). Only 4 new Spellcheck
  Suspect Words hits, all proper names (Cameníhah, Jonéam, Límhah,
  Shiblom), added to `permitted words.txt`; three other page-566 names
  with irregular diacritics (Lámah, Gidgiddónah, Antiónum) are not
  flagged by the actual report despite absence from that list, so
  nothing was added for them (no-op precedent, pages 469-470). The
  page's own suspected-misprint note ("ricibirles" for "recibirles",
  v.7) was run through the full mandatory check: 1886 (book page
  562/file 580) prints the identical misspelling, hyphenated
  "ricibir-les" — a shared-edition error, not 1920-only — but RAE DLE
  has no entry for "ricibir" and none of the three reference corpora
  contain it either, so per the `seperado`/`marvillosas` precedent
  (1886 agreement alone doesn't establish legitimacy) it was added to
  `errors in 1920.txt` as Mormón 6:7; not added to `permitted words.txt`
  since the fresh pptext report doesn't flag it at all (same
  unexplained-gap pattern as "Poi"/"dsesaría"/"aninciado", pages
  469-470). Independently verified "tallaron"/"tallados" (v.10-11,
  double-l) is not a new error — matches 1886 exactly and is already
  established document-wide vocabulary (~15 prior instances, never
  needing a `permitted words.txt` entry since aspell already accepts
  "tallar" conjugations). Whole-document mechanical sweeps all clean —
  max footnote 4164, zero duplicates/out-of-range, only the
  pre-existing footnote-812 gap remains; zero curly quotes; no new
  hyphen compounds.
- **2026-08-02**: Sessions A–E run for page 567 (Mormón 6:15(cont.)-22,
  footnotes 4165-4167 letters n-p, then Mormón 7:1-3, footnote 4168
  letter a; user initially asked for page 467, already long completed
  back on 2026-07-20 — confirmed with the user and redirected to 567,
  the actual next page per this file's progress marker). No i/l/1
  letters in this page's own lettering (n, o, p, a) — mandatory
  Section 8 check not triggered. Session A: a low-zoom first read of
  the Chapter 7 footnote letter mistook the swash "a" for "q"
  (superficially similar in this font); a dedicated high-zoom crop
  resolved it as "a", consistent with rule 13's chapter-restart rule
  and matching the body-text marker's own letter. Two narrow-space-vs-
  merge instances defaulted to two words per grammar (rule 6, not
  raised as a standalone question during A-D): "álos" -> "á los"
  (preposition + article) and "sino" -> "si no" (v.18's conditional
  negation, not the adversative conjunction) — batched for Session E's
  editor summary. `check_line_wrap.py` flagged a 30-vs-37 line-count
  mismatch; traced to the script's own limitation (its
  `txt_body_lines()` stops at the first blank line, so it never counted
  this page's 8-line Mormón 7 continuation after the chapter break) —
  not a real reflow issue, confirmed by the per-line image read.
  Session D: `generate_block2.py` left 6p/4167 unresolved as predicted
  (a print misprint, "II Nfie 2" for "II Nefi 2", broke the book-name
  regex); hand-resolved via `librodm_foot.txt`'s own "2d, 263: II Nefi
  9:4,..." entry (LIBRO SEGUNDO DE NEFI section) to "Véase 263.".
  Session E: fresh pptext/WSL regeneration (`report_wsl_20260802d.html`).
  Zero new Spellcheck Suspect Words hits from this page. The page's own
  two suspected-misprint notes were run through the full mandatory
  check: (1) v.21 "en él que" (×2) — 1886 (book page 564/file 581)
  prints the unaccented relative "el que" both times, the only
  grammatically valid reading ("the day in which"/"and in which"),
  confirming a genuine 1920-only accent error; added to `errors in
  1920.txt` as Mormón 6:21. (2) Block 1 6p/4167 "II Nfie 2" — BOM 1879
  Pratt (same footnote numbering) prints the equivalent entry with the
  correct book name ("p, see d, II. Nep. 2."), independently confirming
  both the misprint and the Session D manual resolution (263); added to
  `errors in 1920.txt` as a Footnote entry, matching the existing
  "Footnote Mormón 2e, 4084" precedent's format. Neither addition
  mirrored into `permitted words.txt`: "el"/"él" are too common to be
  flagged by aspell regardless of accent, and "Nfie" (exact form)
  doesn't appear anywhere in the fresh pptext report at all (same
  unexplained-gap pattern as "ricibirles"/"Poi"/"dsesaría"). A separate
  Google cross-check candidate (v.22 "Él que", Google's OCR dropping the
  accent on the capital É) was zoomed and confirmed as OCR noise, not a
  transcription error. Whole-document mechanical sweeps all clean — max
  footnote 4168, zero duplicates/out-of-range, only the pre-existing
  footnote-812 gap remains; zero curly quotes; this page's own
  line-number citations (body 25283-25322, Block 2 29790-29792) all
  fell within the already-established, benign "short lines check"
  category — no hits in any other pptext section.
- **2026-08-02**: Sessions A–E run for page 567 (Mormón 6:15(cont.)-22,
  footnotes 4165-4167 letters n-p, then Mormón 7:1-3, footnote 4168
  letter a; user initially asked for page 467, already long completed
  back on 2026-07-20 — confirmed with the user and redirected to 567,
  the actual next page per this section's progress marker). No i/l/1
  letters in this page's own lettering (n, o, p, a) — mandatory
  Section 8 check not triggered. Session A: a low-zoom first read of
  the Chapter 7 footnote letter mistook the swash "a" for "q"; a
  dedicated high-zoom crop resolved it as "a", matching rule 13's
  chapter-restart rule and the body-text marker's own letter. Two
  narrow-space-vs-merge instances defaulted to two words per grammar
  (rule 6): "álos" -> "á los" and "sino" -> "si no" (v.18's conditional
  negation) — batched for Session E's editor summary.
  `check_line_wrap.py` flagged a 30-vs-37 line-count mismatch, traced
  to the script's own limitation (its line counter stops at the first
  blank line, so it never saw this page's 8-line Mormón 7 continuation
  after the chapter break) — not a real reflow issue. Session D:
  `generate_block2.py` left 6p/4167 unresolved as predicted (a print
  misprint, "II Nfie 2" for "II Nefi 2", broke the book-name regex);
  hand-resolved via `librodm_foot.txt`'s own "2d, 263: II Nefi
  9:4,..." entry to "Véase 263.". Session E: fresh pptext/WSL
  regeneration (`report_wsl_20260802d.html`), zero new Spellcheck
  Suspect Words hits. Both of this page's suspected-misprint notes
  confirmed as genuine 1920-only errors and added to `errors in
  1920.txt`: (1) v.21 "en él que" (×2) — 1886 (book page 564/file 581)
  prints the unaccented relative "el que" both times, the only
  grammatically valid reading; logged as Mormón 6:21. (2) Block 1
  6p/4167 "II Nfie 2" — BOM 1879 Pratt prints the equivalent entry with
  the correct book name ("p, see d, II. Nep. 2."), independently
  confirming both the misprint and the Session D manual resolution
  (263); logged as a Footnote entry, matching the existing "Footnote
  Mormón 2e, 4084" precedent's format. Neither mirrored into `permitted
  words.txt` — "el"/"él" too common to be aspell-flagged regardless of
  accent, and "Nfie" doesn't appear anywhere in the fresh pptext report
  at all (same gap pattern as "ricibirles"/"Poi"/"dsesaría"). A separate
  Google cross-check candidate (v.22 "Él que", Google dropping the
  accent) was zoomed and confirmed as OCR noise, not a transcription
  error. Whole-document mechanical sweeps all clean — max footnote
  4168, zero duplicates/out-of-range, only the pre-existing
  footnote-812 gap remains; zero curly quotes; this page's own
  line-number citations all fell within the already-established,
  benign "short lines check" category.
- **2026-08-02b**: Sessions A–E run for page 568 (Mormón 7:4-10,
  footnotes 4169-4182 letters b-o, then Mormón 8:1, footnote 4183
  letter a). This page's own lettering includes i (verse 8) and l
  (verse 9), plus i/l cross-reference target letters (7d→i, 7j→l,
  7l→l) — mandatory Section 8 check triggered and run against BOM
  1879 Pratt (pages_1879/page_0570.png, book page 562; note
  chapter_map.csv's listed file 571 for Mormon/8 lands one page late,
  the correct page is 570) — all confirmed correct. Discretion (Section
  8) then extended the same 1879 check to every other cross-reference
  target letter on this swash-font page, since several were genuinely
  hard to read even at high zoom, and this caught 3 real misreads from
  the first low-zoom pass: 7h/7n's target (both "II Nefi 9") is "u",
  not "m"; 7m's target ("II Nefi 3") is "g", not "o"; 7o's target
  ("III Nefi 9") is "y", not "v". All three re-confirmed independently
  in Session D via content-fit: the resolved Block 2 numbers' own
  citation text matches this page's verse topics exactly (378's
  baptism proof-texts for 7h/7n "bautizáos"/"bautizados"; 4142 citing
  "Mormón 7:8-9" itself for 7j/7l; 278 citing "Mormón 7:5,10" itself
  for 7b/7m) — strong independent corroboration the corrected letters,
  not the first-pass ones, are right. One rule-7 hyphen rejoin
  ("se-"/"pultura" → "sepultura") and one rule-8 overlength-line fix
  (moved "[4177]de" to the next line). Suspected misprint, preserved as
  printed and confirmed via 1886 (pages_1886/page_0583.png, book page
  565): Mormón 8:1 "me padre" for "mi padre" — 1886 and the modern
  Spanish edition both read "mi padre"; added to `errors in 1920.txt`.
  Google cross-check: 2 candidates (v.5 "Él"/"Judíos" accents), both
  zoomed and confirmed as OCR noise on accented letters, same pattern
  as page 567's "Él que obra". Session E: fresh pptext/WSL regeneration
  (`report_wsl_20260802e.html`) — zero hits anywhere in the report from
  this page's text (targeted phrase search, not just the spellcheck
  section); v.9 "creereis" (missing accent vs. 1886's "creéreis") isn't
  flagged by pptext at all, so no `permitted words.txt` entry needed,
  and per rule 11 a bare missing accent isn't logged as an error either.
  Whole-document mechanical sweeps all clean — max footnote 4183, zero
  duplicates/out-of-range, only the pre-existing footnote-812 gap
  remains; zero curly quotes.
- **2026-08-02c**: Sessions A–E run for page 569 (Mormón 8:2-12,
  footnotes 4184-4198, letters b-p). Mandatory Section 8 check (i/l/1):
  triggered by this page's own lettering (i, v.5 "cuanto"; l, v.9
  "ladrones"). Same-page glyph comparison plus a fresh 1879 cross-check
  (pages_1879/page_0571.png, book page 563 — this time landing exactly
  on the matching content, unlike page 568's one-page-late 1879
  offset) confirmed both letters, along with the two cross-reference
  target letters checked alongside them (8e→g, Mormón 5; 8l→2c, IV
  Nefi 1, a two-letter code per rule 16). One rule-7 hyphen rejoin
  ("mara-"/"villosa" → "maravillosa", kept on the second line per rule
  8). Three narrow-space-vs-merge defaults applied per the standing
  rule (grammar requires two words, no zoom/pixel analysis): v.7 "que
  los", v.8 "que fué", v.8 "mano del" — all three independently
  confirmed as genuine two-word spacing via the 1886 comparison in
  Session E. Suspected misprint, preserved as printed and confirmed
  via 1886 (pages_1886/page_0583.png, book page 565): Mormón 8:7 "los,
  Nefitas," — the 1920 print carries a stray extra comma between "los"
  and "Nefitas" inside the "mi pueblo, los Nefitas," appositive; 1886
  has no such comma; added to `errors in 1920.txt`. Footnote g's
  printed citation shows "Mormón 6; 6." (semicolon, not colon, between
  chapter and verse) — transcribed per rule 22 as the normalized
  "Mormón 6:6" in Block 1/2 (not an errors-log case, since Block 1/2
  citations are always normalized regardless of the original's
  punctuation there); confirmed via 1879's equivalent "Mor. 6:6."
  Footnote i's "10:1, 2" (two consecutive verses) formatted as the
  range "10:1-2" per rule 23. Session D: `generate_block2.py 569`
  resolved all 15 Block 1 entries automatically; content-fit sanity
  check on the two i/l/1-adjacent resolutions both corroborated
  strongly (8e→4137, whose own citation names this page's own v.4;
  8l→4057, whose Block 1 source text directly cites Helamán 2:3-14,
  the Gadianton-robbers chapter, matching "ladrones"). That same check
  surfaced a pre-existing, out-of-scope issue for the editor: footnote
  4057's own Block 2 entry ("4057: Véase 268.") appears to have dropped
  the direct "Helamán 2:3-14" half of its Block 1 source's two-part
  citation when it was first resolved (before page 569, during IV Nefi
  1's own transcription) — flagged, not fixed, since it belongs to a
  different page's footnote. Session E: fresh pptext/WSL regeneration
  (`report_wsl_20260802f.html`) — zero new Spellcheck Suspect Words
  hits from this page (same pre-existing 7-word list as page 568's
  run); footnote check clean (no duplicates/missing near this page's
  range); this page's line-number citations only ever land in the
  already-established, benign "short lines check" category. Whole-
  document mechanical sweeps all clean — max footnote 4198, zero
  duplicates/out-of-range, only the pre-existing footnote-812 gap
  remains; zero curly quotes.
- **2026-08-02d**: Sessions A–E run for page 570 (Mormón 8:12(cont)-23,
  footnotes 4199-4208, letters q-z). No i/l/1 in this page's own
  lettering, so the mandatory Section 8 case didn't apply, but
  discretionary 1879 cross-checks (pages_1879/page_0572.png, book page
  564 — lands exactly on this page's content) resolved two genuinely
  hard-to-read glyphs: entry 8v's target letter (1920 looked like it
  could be "e", matching neighboring entries 8t/8u — 1879 confirms "c")
  and the final entry, where both the marker and target glyphs looked
  alike enough to read as a same-page self-reference ("z, Véase z.") —
  1879 confirms "z, see x." (entry z citing entry x, not itself),
  matching the page's own strict q-through-z alphabetical sequence.
  Two rule-7 hyphen rejoins ("con-"/"dene"→"condene", marker moved to
  the next line per rule 8; "'pro-"/"hibido"→"prohibido", landing
  exactly at the 72-char rule 9 limit) plus one rule-8 cascading
  rebalance (marker+semicolon-fix pushed a line over, which pushed the
  next line over in turn — "obscuridad,"/"poder" both moved down one
  line in a single pass). Block 1 entry 8x's own citation prints
  "IIINefi" with zero space between "III" and "Nefi" (confirmed at high
  zoom, a true run-together, not a narrow gap) — normalized to "III
  Nefi" per the standing default (this exact "III Nefi" form is used
  everywhere else on the page and throughout the document). Entry 8s's
  line ends with an unexplained bold, full-cap-height "8" glyph right
  after "I Nefi 13;" — zoomed repeatedly, doesn't fit as citation
  content (13's digits are already complete; too large/bold to be a
  footnote letter) and this page's own Google/embedded OCR text layer
  independently produced the same stray "8" in the same spot,
  corroborating it's really printed there — treated like the "Digitized
  by Google" watermark (rule 33) and excluded from the transcription,
  not logged as an error. Vease/Véase and Ether/Éther accent
  inconsistencies preserved exactly as printed on this page (both
  spellings genuinely appear side by side); not error-log cases per the
  standing missing-accent guidance. Session D: `generate_block2.py 570`
  left 3 of this page's own entries unresolved; two had real,
  already-transcribed targets and were fixed by hand directly in
  `librodm.txt` after the script's two separate parsing gaps were
  diagnosed (its VEASE_CLAUSE regex only matches accented "Véase", so
  entry 8v's unaccented "Vease c, II Nefi 27." never reached the
  resolver even though 27c=682 already exists in LIBRO SEGUNDO DE NEFI;
  its letters-vs-book/chapter comma-splitting can't handle a second
  citation tacked on after a semicolon, so entry 8s's "Véase s, I Nefi
  13; Moroni 10:1-2." never resolved even though 13s=102 already exists
  in PRIMER LIBRO DE NEFI) — corrected to "Véase 102; Moroni 10:1-2."
  and "Vease 682." respectively. The third (8w/8x's "Véase página
  titular") stays unresolved permanently, not a defect — no lettered
  footnote section exists anywhere for the title page. Flagged for the
  editor, not fixed: the unaccented-"Vease" regex gap is likely
  systemic across `librodm.txt`'s 45 pre-existing unaccented "Vease"
  Block 2 entries, similar in spirit to the footnote-4057 citation gap
  flagged on page 569. Session E: fresh pptext/WSL regeneration
  (`report_wsl_20260802g.html`) — two NEW Spellcheck Suspect Words hits
  from this page, both researched and added to `permitted words.txt`
  (not `errors in 1920.txt`): "realize" (v.15) matches 1886
  word-for-word at the same spot (pages_1886/page_0584.png, book page
  566/file 584), strong same-lineage period evidence outweighing RAE's
  modern-only "realizar/realice" standard; "destruirémos" (v.21) is the
  pre-1999 RAE-orthography-reform accentuation of "destruiremos"
  (confirmed via WebSearch research, corroborated by the modern LDS
  Spanish edition using the same unaccented stem post-reform). Whole-
  document footnote-number sweep: max=4208, zero duplicates either
  side, only the pre-existing footnote-812 gap on the anchor side;
  surfaced (not investigated — out of scope, pre-existing, unrelated to
  this page) six Notas-entries-without-a-body-anchor gaps: 365, 530,
  805, 909, 1724, 1725. This page's own report hits all landed in the
  established benign short-lines-check category; zero curly quotes;
  spaced-punctuation/footnote-punctuation/verse-indent sweeps all clean
  on both master files.
- **2026-08-02e**: Sessions A–E run for page 571 (Mormón 8:23(cont)-31,
  footnotes 4209-4223, letters 2a-2o). Chapter 8's lettering continues
  past "z" (reached page 570) into two-letter "2a" codes per rule 16,
  all formatted "8-2[letter]" in Block 1 per the rule's own example; no
  new chapter/subtitle, no book-name header needed. Mandatory Section 8
  check (i/l/1) genuinely applied this time: 2i (own letter), 2l (own
  letter), and 2i's cross-reference target letter "i" all required the
  1879 check. Verified via BOM 1879 Pratt (pages_1879/page_0573.png,
  book page 565) — this page's marker sequence turned out to be a
  letter-for-letter 1:1 match with 1879's own sequence (both editions
  annotate the exact same words in the exact same verse-by-verse
  order), so 1879's target letters were trusted directly rather than
  matched purely by content per rule 26's general caveat. No i/l
  discrepancy found. Discretionary extension of the same 1879 check
  caught a genuine misread: entries 8-2a and 8-2c (both "Véase [letter],
  Mormón 5") were first read as target "b" from the 1920 image alone
  (an anchor-bias trap — entry 2b sits right next to 2a) but 1879 reads
  "s" for both; re-zoomed the 1920 glyphs at 20x independently for each
  entry and confirmed a small cursive "s" shape, not "b" — corrected
  before the page file was finalized. Session D later corroborated this
  independently of 1879: `generate_block2.py 571` resolved both 8-2a
  and 8-2c to the identical footnote (4149, Enos 1:12-18; Mormón
  8:24-26; 9:36-37), which content-fits both annotated verses
  (testimony/records coming forth "from the dust"), all 15 of this
  page's Block 1 entries resolved on the first pass with zero
  unresolved cross-references. Suspected extraneous printer's mark
  (not logged in `errors in 1920.txt`, treated like the "Digitized by
  Google" watermark per rule 33, matching page 570's stray-"8"-glyph
  precedent): v.23's "...y como el Señor vive," is followed by a short
  diagonal fleck before "que" — zoomed to 20x, doesn't read as a hyphen
  (wrong placement) or an accent (no letter to accent under it); this
  page's own Google/embedded OCR text layer reads straight through
  "...vive, que" with nothing there, corroborating it isn't real
  content. Narrow-space-vs-merge, not raised as a standalone question
  (surfaced for Session E per rule 6): v.23 "os digo" is a genuine
  zero-width "osdigo" merge in the 1920 print (confirmed at 10x zoom,
  unlike the normally-spaced "aquí, os" on the same line) but was
  transcribed as two words per the standing default, since "os digo"
  is a complete, ordinary two-word phrase. Two rule-7 hyphen rejoins
  ("bene-"/"ficio"→"beneficio", "segura-"/"mente"→"seguramente"), both
  landing under 72 chars with no rule-8 rebalancing needed. Google
  cross-check: 2 candidates, both the same known "Él" read as
  unaccented "El" OCR pattern (v.23/v.24), confirmed correct by direct
  zoom — a capital-É-vs-E OCR miss, not a transcription issue. Session
  B: independent re-read of fn_zoom against the finished page_571.txt —
  all 15 body-text [N] markers and all 15 Block 1 entries confirmed,
  including the corrected 8-2a/8-2c "s" and the mandatory i/l checks.
  No discrepancies found; no changes made. Session E: fresh pptext/WSL
  regeneration (`report_wsl_20260802h.html`) — one NEW Spellcheck
  Suspect Words hit, "masetros" (v.28, "y sus masetros se
  enorgullecerán en sus corazones"): 1886 (pages_1886/page_0586.png,
  book page 568/file 586) prints the correctly-spelled "maestros" at
  the same spot; confirmed at 12x zoom that 1920 genuinely prints
  "masetros" (a/e transposed), not a transcription misread; no RAE DLE
  entry, zero hits in all three reference corpora, modern LDS Spanish
  edition uses "maestros" — no archaic-legitimacy evidence found, added
  to both `permitted words.txt` and `errors in 1920.txt` (Mormón 8:28
  masetros (maestros)). Whole-document footnote-number sweep: max=4223
  (this page's own 8-2o), zero duplicate anchors; the long-documented
  pre-existing anchor/note gaps (365, 530, 805, 909, 1724, 1725 with no
  note; 812 with no anchor) remain unchanged and unrelated to this
  page. One NEW-to-this-sweep finding surfaced, but NOT caused by this
  page: a duplicate Block 2 note for footnote 3185 exists both at its
  correct original position within LIBRO DE HELAMÁN's own range and
  again, spuriously, at the very end of `librodm.txt`, preceded by a
  misplaced second "LIBRO DE HELAMÁN" header appearing right after this
  page's own "LIBRO DE MORMÓN" section — confirmed via `git show
  HEAD:librodm.txt` that the last commit ended at footnote 4164, well
  before this duplicate, so it was introduced during one of the earlier
  uncommitted pages' sessions (567-570). Flagged for the editor, not
  fixed here (out of scope for page 571's own session, same treatment
  as the pre-existing footnote-gap and unaccented-"Vease" findings
  flagged on pages 569/570); the fix itself is simple (delete the
  trailing blank line + "LIBRO DE HELAMÁN" header + duplicate "3185:
  Véase 2046." line, four lines at the very end of the file) but
  touches content this page's session didn't introduce. This page's own
  report hits all landed in the established benign short-lines-check
  category (verse/paragraph-boundary short lines, short Block 2
  entries); zero curly quotes; zero new hyphenated compounds; scanno
  and curly-quote checks both fully clean; spaced-punctuation/footnote-
  punctuation/verse-indent sweeps all clean on both master files.

- **2026-08-02f**: Sessions A–E run for page 572 (Mormón 8:32-40,
  footnotes 4224-4234, letters 2p-2z). Chapter 8's two-letter lettering
  continues from page 571's "2o" through "2z" (reaching the alphabet's
  end again); still chapter 8 throughout, so no book-name header or
  letter-reset applies in Block 1; next page expected to roll over to
  "3a" per the three-letter/second-rollover convention, matching 1879's
  own "3 a, see k, I. Nep. 14" entry immediately following this page's
  last entry. Mandatory Section 8 check (i/l/1): this page's
  cross-reference target letters include i (8-2s, 8-2y) and l (8-2v,
  8-2x); none of this page's own footnote letters (p-z) are themselves
  i/l/1. Verified via BOM 1879 Pratt (pages_1879/page_0574.png, book
  page 566, consistent with page 571's own 1879 page 573/book 565
  precedent) — 1879's marker sequence (2p-3b) is a letter-for-letter
  1:1 match with this page's 1920 sequence, so 1879's target letters
  were used directly: 2s→i (II Nefi 25), 2v→l (Mosíah 4), 2x→l (Mosíah
  4), 2y→i (II Nefi 10) — all four confirm the 1920 reading, no
  discrepancy. Content-fit sanity check: 2v/2x (Mosíah 4, caring for
  the poor) fit v.37/v.39's "amáis á los pobres"/"los desnudos,
  necesitados... pasen"; 2s/2y fit their verses as part of a
  cross-reference chain rather than a direct thematic match, same
  pattern as several of page 571's "Véase" entries. Additional target
  letter resolved by the same 1879 comparison though not itself i/l/1,
  since it was visually ambiguous in the 1920 print (easy confusion
  with the two neighboring "l" targets at 2v/2x): 8-2z was
  provisionally read as "l" at first pass, but 1879 reads "2 z, see f,
  II. Nep. 28" — confirmed "f" is correct, fitting v.40's "sangre de
  sus padres" theme already cited directly (unresolved-by-letter) at
  2t/2u earlier on this page. Not logged in `errors in 1920.txt` since
  this was a read correction via 1879, not a genuine 1920 print defect
  — same treatment as page 571's 8-2a/8-2c "b"→"s" correction. Four
  genuine 1920 print defects found and logged in `errors in 1920.txt`:
  (1) 8-2r's citation prints "I Nefi 14:18-7;27" where 1879 (same
  page/position) reads a clean "I. Nep. 14:18-27" — the stray "7" and
  semicolon zoomed repeatedly at up to 20x, unambiguously a "7" (same
  glyph shape as the "7" in "27" immediately following), no plausible
  non-error reading exists; (2) v.33 "obtener ganacias?" — Google's own
  OCR layer already read "ganacias" (one "n") against this session's
  initial reflex-typed "ganancias"; zoomed at 12x and confirmed the
  print genuinely has only one "n"; 1886 (pages_1886/page_0586.png,
  book page 568/file 586) prints the correct "ganancias" at the same
  spot, confirming a 1920-only dropped-letter misprint, not an archaic
  variant; corrected before the page file was finalized; (3) v.38
  "vosotros masetros" — repeat of page 571's masetros/maestros
  transposition (a/e swapped), confirmed at 10x zoom against 1920,
  1886 (pages_1886/page_0587.png, book page 569) prints "maestros";
  "masetros" already in `permitted words.txt` from page 571, no new
  addition needed; (4) v.40 "la sangre de sus ¿padres" — a genuine
  printed inverted question mark "¿" mid-sentence with no grammatical
  function (the sentence already opened its question with "¿porqué" at
  the start of v.40); zoomed at 8x, confirmed a real full "¿" glyph,
  not a stray speck; checked against 1886 (pages_1886/page_0587.png,
  book page 569, since 1879 is English and wouldn't preserve Spanish
  punctuation) which prints plain "de sus padres" with no mark,
  confirming it's extraneous. Three rule-7 hyphen rejoins ("pala-"/
  "bra"→"palabra", "per-"/"donaré"→"perdonaré", "contami-"/"narse"→
  "contaminarse"), all landing under 72 chars, no rule-8 rebalancing
  needed. Google cross-check (`check_google_crosscheck.py 572`): 1
  candidate surfaced (the v.33 "ganacias"/"ganancias" defect above,
  already resolved via the process described). Session B: independent
  re-read of fn_zoom against the finished page_572.txt — all 11
  body-text [N] markers (2p-2z) and all 11 Block 1 entries confirmed,
  including the preserved 8-2r misprint and the mandatory i/l 1879
  cross-check; also independently re-verified v.40's own separate,
  correctly-spelled "ganancias" is not the same defect as v.33's
  "ganacias" (a fresh zoom of the v.40 spot specifically, so the
  Session A fix wasn't mistakenly over-applied to the wrong
  occurrence). No discrepancies found; no changes made. Session E:
  fresh pptext/WSL regeneration (`report_wsl_20260802i.html`) — zero
  new Spellcheck Suspect Words hits (both this page's preserved errors,
  "ganacias" and "masetros", already suppressed via `permitted
  words.txt`); every Corrections-log entry this page's own Sessions A/B
  left behind was already checked against 1886/1879 and promoted to
  `errors in 1920.txt` at transcription time, none left unresolved.
  Whole-document footnote-number sweep: max=4234 (this page's own
  8-2z), this page's own range 4224-4234 confirmed exactly one body
  anchor and one Block 2 note each, no duplicates or gaps introduced;
  the same long-documented pre-existing gaps as every prior session
  remain unchanged and unrelated to this page. Whole-document
  mechanical sweeps re-run clean: spaced-punctuation/footnote-
  punctuation/verse-indent all clean on both master files; zero curly
  quotes. The 8-2r "18-7;27" misprint lives only in `librodm_foot.txt`
  (Block 1), which pptext's dash check never scans (only Block 2's
  already-resolved "Véase NNNN"-style entries are scanned), so it's
  invisible to pptext by construction — already fully handled via the
  direct 1879 comparison in Session A. Scanno, curly-quote, and
  special-situations checks: this page's distinctive text produced no
  hits outside the established benign short-lines-check category. No
  narrow-space-vs-merge flags on this page.

- **2026-08-02g**: Sessions A-E run for page 573 (Mormón 8:41 (closing) +
  CAPÍTULO 9:1-8, footnotes 4235-4239, letters 8-3a/8-3b then chapter 9's
  own a-c). Chapter 8's two-letter lettering rolls over from page 572's
  "2z" to "3a"/"3b" (closing that chapter's own footnote block), then
  chapter 9 opens with no subtitle and its own lettering restarts fresh
  at "a" per rule 13. A swash-font ambiguity required discretionary 1879
  cross-checking (none of this page's own letters/targets -- k, f, c, f,
  e, 2f -- are i/l/1, so the mandatory Section 8 check didn't formally
  apply, but the digit-vs-letter glyphs were genuinely hard to read):
  the "3a"/"3b" rollover digit and entry 9c's "2f" cross-reference digit
  looked similar at first glance in this font, and entry 9c's first
  target glyph was briefly uncertain between "e" and a stray digit.
  Verified via BOM 1879 Pratt (pages_1879/page_0575.png, book page 567,
  via chapter_map.csv's Mormon,9 row): 1879 confirms "a, see c, III. Nep.
  26. b, see f, II. Nep. 2. c, see e, III. Nep. 29. See 2f, Mor. 8." --
  an exact content match for all three new chapter-9 letters, settling
  both ambiguous glyphs (target is "e", not a digit; the rollover digit
  is genuinely "3", distinguishable from "2" by a clear stroke-shape
  difference confirmed at high zoom). Google cross-check
  (`check_google_crosscheck.py` style comparison via
  `google_text_1920/page_0595.txt`) caught one genuine 1920 misprint not
  otherwise obvious: v.5 "la santitad de Jesu Cristo" prints "santitad"
  (a "t" for the expected "d"); confirmed at 12x zoom, corroborated
  against 1886 (pages_1886/page_0588.png, book page 570/file 588) which
  prints the correct "santidad" -- logged in `errors in 1920.txt` and
  `permitted words.txt` (confirmed actually flagged by a fresh pptext
  spellcheck run before adding, per the standing "verify before adding"
  rule). A small stray dot/fleck floating above verse 7's "7." was
  treated as an extraneous printer's mark per rule 33 (matching the
  page 570/571 precedent), not logged as an error: this page's own
  Google OCR text reads straight through with nothing there, and 1886
  independently shows a similar stray artifact elsewhere on its own
  corresponding page, suggesting a press-level phenomenon rather than
  content. Session D (`generate_block2.py 573`) hit a known script
  limitation on entry 9c: its Block 1 text has two "Véase" clauses
  joined by a semicolon with no period between them, which the script's
  regex can't split (same limitation as historical entries 995, 2050,
  2060, 2257, 3290, 661, all previously fixed by hand -- confirmed by
  testing the current unchanged script against entry 995's original
  text and reproducing the same non-resolution). Resolved manually:
  "Véase e, III Nefi 29" -> 4016 and "Véase 2f, Mormón 8" -> 4214 --
  the first lookup attempt actually landed on the wrong book's chapter
  29 letter e (742, in II Nefi's own section) before the book-section
  header boundaries in `librodm_foot.txt` were checked properly and the
  correct III Nefi entry (4016) was found; both final targets content-fit
  well (4016, Mormón 9:7-11, points forward to this very chapter's own
  continuation of the "revelations have ceased" argument). Bookkeeping
  note: this session also found and fixed two pre-existing gaps from
  the prior page-572 session that had never been closed out --
  sessions-log.md was missing its own page-572 entry entirely (backfilled
  from page_572.txt's own detailed Corrections notes, since CLAUDE.md's
  progress snapshot already had a full 572f write-up but sessions-log.md
  did not), and a page-571 entry had been accidentally duplicated
  back-to-back in sessions-log.md (removed). The previously-flagged
  duplicate-3185/misplaced-header defect noted on pages 571/572 (extra
  "LIBRO DE HELAMÁN" header + duplicate note at the file's end) was
  found already resolved as of this session -- confirmed only one "3185:"
  entry exists and the file now ends cleanly with page 573's own
  entries; not something this session fixed, just confirmed already
  gone. Whole-document footnote-number sweep: max=4239 (this page's own
  9c), zero duplicate anchors; the long-documented pre-existing gaps
  (365, 530, 805, 909, 1724, 1725 with no note; 812 with no anchor)
  remain unchanged and unrelated to this page (a naive first-pass sweep
  script also produced a large spurious "duplicate notes" list caused by
  wrapped Block 2 continuation lines that happen to start with a bare
  "N:" verse citation -- confirmed false positive by inspecting several
  hits directly, not a real defect; the bracket-anchor duplicate check
  and the established gap list are unaffected and reliable). Whole-
  document mechanical sweeps (`check_spaced_punctuation.py`,
  `check_footnote_punctuation.py`, `check_verse_indent.py`) all clean on
  both master files. Fresh pptext/WSL regeneration
  (`report_wsl_20260802j.html`): "santitad" correctly flagged in
  Spellcheck Suspect Words (now suppressed); no other new findings in
  this page's body or Block 2 line ranges beyond an edit-distance pairing
  of this page's correctly-spelled "creeréis" against another page's
  correctly-spelled instance (no error). Zero curly quotes; zero new
  hyphenated compounds; short-lines-check hits all in the established
  benign category (verse starts, short Block 2 entries).
- **2026-08-03**: Sessions A-E run for page 574 (Mormón 9:9-18, mid-chapter
  continuation of chapter 9 opened on page 573; no new chapter/subtitle),
  footnotes 4240-4250, letters d-n continuing chapter 9's own lettering
  from page 573's a-c. Mandatory Section 8 check applied to letters i
  (4245, v.13 "todos") and l (4248, v.14 "impuros") -- neither the
  chapter's own lettering position nor the same-page glyph comparison
  (this page's "i" has a short stroke with a clearly separated dot,
  distinct from "l"'s continuous unbroken curve) left real doubt, but the
  1879 check was still run per the mandatory rule regardless. Verified via
  BOM 1879 Pratt (pages_1879/page_0576.png, book page 568 -- chapter_map.csv's
  Mormon,9 row lists file_page 575, but this page's own verses 9-18 land one
  page later at file 576): matched by content (rule 26 -- letter identity
  across editions isn't expected to match when translation word order
  differs, only the target book/chapter) rather than by letter. Entry i's
  target book/chapter (II Nefi 9) matched 1879's own "i, see j, II. Nep. 9"
  (same chapter, different target letter, expected divergence); entry l
  matched 1879's "l, see o, II. Nep. 9" exactly, including the letter
  itself. The other 7 entries on this page (e, f, g, h, j, m, n) all
  matched 1879 letter-for-letter and content-for-content, giving strong
  overall corroboration for the full letter sequence. Session B did an
  independent fresh re-read of fn_zoom plus a fresh independent re-crop of
  the same 1879 page, reproducing identical findings -- no discrepancies,
  no changes. No rule-7 hyphenated line-break splits on this page; no
  suspected misprints found (a small stray mark beyond the text column's
  right edge near the header row was checked and is not part of any
  letter or word, not logged). Google cross-check
  (`check_google_crosscheck.py 574`): zero candidates after dismissing 5
  footnote-marker-glue hits and 1 trailing footnote-block hit. Session D
  (`generate_block2.py 574`) resolved all 11 entries automatically, no
  manual intervention needed (unlike page 573's 9c). Whole-document
  footnote-number sweep via the fresh pptext footnote-check section:
  max=4250, the new range 4235-4250 fully contiguous across both of
  pptext's anchor buckets, zero duplicates, zero out-of-range values.
  Fresh pptext/WSL regeneration (`report_wsl_20260803.html`): zero new
  Spellcheck Suspect Words from this page's vocabulary (all of the
  page's distinctive words checked individually against the spellcheck
  section, which has only 6 total flagged words document-wide, none from
  this page); the only report hits touching this page's line range were
  the already-established benign short-lines-check pattern and the
  hyphen-minus bucket picking up this page's own legitimate verse-range
  hyphens (4240, 4242 entries). Zero curly quotes; zero new hyphenated
  compounds (87 unique letter-hyphen-letter tokens document-wide, all
  previously-vetted ordinals/proper-noun compounds, none introduced by
  this hyphen-free page). Whole-document mechanical sweeps
  (`check_spaced_punctuation.py`, `check_footnote_punctuation.py`,
  `check_verse_indent.py`) all clean on both master files. No
  `permitted words.txt` or `errors in 1920.txt` additions needed.
- **2026-08-03**: Sessions A–E run for page 574 (Mormón 9:9-18, mid-chapter
  continuation of chapter 9 opened on page 573; no new chapter/subtitle),
  footnotes 4240-4250, letters d-n continuing chapter 9's own lettering
  from page 573's a-c. Mandatory Section 8 check applied to letters i
  (4245, v.13 "todos") and l (4248, v.14 "impuros") — neither the
  chapter's own lettering position nor the same-page glyph comparison
  (this page's "i" has a short stroke with a clearly separated dot,
  distinct from "l"'s continuous unbroken curve) left real doubt, but the
  1879 check was still run per the mandatory rule regardless. Verified
  via BOM 1879 Pratt (pages_1879/page_0576.png, book page 568 —
  chapter_map.csv's Mormon,9 row lists file_page 575, but this page's
  own verses 9-18 land one page later at file 576): matched by content
  (rule 26 — letter identity across editions isn't expected to match
  when translation word order differs, only the target book/chapter)
  rather than by letter. Entry i's target book/chapter (II Nefi 9)
  matched 1879's own "i, see j, II. Nep. 9" (same chapter, different
  target letter, expected divergence); entry l matched 1879's "l, see o,
  II. Nep. 9" exactly, including the letter itself. The other 7 entries
  on this page (e, f, g, h, j, m, n) all matched 1879 letter-for-letter
  and content-for-content, giving strong overall corroboration for the
  full letter sequence. Session B did an independent fresh re-read of
  fn_zoom plus a fresh independent re-crop of the same 1879 page,
  reproducing identical findings — no discrepancies, no changes. No
  rule-7 hyphenated line-break splits on this page; no suspected
  misprints found (a small stray mark beyond the text column's right
  edge near the header row was checked and is not part of any letter or
  word, not logged). Google cross-check (`check_google_crosscheck.py
  574`): zero candidates after dismissing 5 footnote-marker-glue hits
  and 1 trailing footnote-block hit. Session D (`generate_block2.py
  574`) resolved all 11 entries automatically, no manual intervention
  needed (unlike page 573's 9c). Whole-document footnote-number sweep
  via the fresh pptext footnote-check section: max=4250, the new range
  4235-4250 fully contiguous across both of pptext's anchor buckets,
  zero duplicates, zero out-of-range values. Fresh pptext/WSL
  regeneration (`report_wsl_20260803.html`): zero new Spellcheck Suspect
  Words from this page's vocabulary (only 6 flagged words exist
  document-wide, none from this page); the only report hits touching
  this page's line range were the already-established benign
  short-lines-check pattern and the hyphen-minus bucket picking up this
  page's own legitimate verse-range hyphens (4240, 4242 entries). Zero
  curly quotes; zero new hyphenated compounds (87 unique
  letter-hyphen-letter tokens document-wide, all previously-vetted,
  none introduced by this hyphen-free page). Whole-document mechanical
  sweeps (`check_spaced_punctuation.py`, `check_footnote_punctuation.py`,
  `check_verse_indent.py`) all clean on both master files. No
  `permitted words.txt` or `errors in 1920.txt` additions needed.
- **2026-08-03**: Sessions A–E run for page 575 (Mormón 9:19-28, mid-chapter
  continuation of chapter 9 opened on page 573; no new chapter/subtitle),
  footnotes 4251-4259, letters o-w continuing chapter 9's own lettering
  from page 574's d-n. None of this page's own letters or cross-reference
  target letters are i/l/1 (o,p,q,r,s,t,u,v,w source; d,f,d,c,d,c,u,c
  targets), so the mandatory Section 8 1879 check did not apply to any
  entry on this page. Two hard-to-read letters (body "s" before v.22
  "que debían"; footnote-block "s" before "Los tres") were resolved via
  the alphabetical-sequence-plus-content-fit technique instead (sequence
  position between r and t, plus thematic fit with "the three"/"the
  twelve" disciple footnotes matching v.22's "que debían quedarse"/
  "también a todos sus discípulos"). A small irregular ink blot (not a
  clean letter shape) before "empezad" in v.27 was identified as a stray
  print mark, not a footnote letter — the footnote block ends cleanly at
  w with no truncation and no x entry, later corroborated by BOM 1886
  (pages_1886/page_0590.png, book page 572) printing plain "y empezad"
  with no special mark at that spot either. Session B did an independent
  fresh re-read of fn_zoom against the finished page — all 9 Block 1
  entries and all 9 [N] marker placements confirmed, no discrepancies.
  Google cross-check (`check_google_crosscheck.py 575`): zero candidates
  after dismissing 5 footnote-marker-glue hits and 1 trailing
  footnote-block hit. Session D (`generate_block2.py 575`) resolved 7 of
  9 entries automatically; 2 (4253, 4258) were left unresolved by the
  script because each packs a second same-chapter "Véase <letter>"
  clause after a semicolon within one period-terminated sentence, and
  the script's cross-reference regex matches greedily from the first
  "Véase" to the final period, swallowing both clauses as one
  unparseable span rather than resolving them separately — resolved by
  hand instead (4253's "Véase d, III Nefi 17" → III Nefi's own 17d =
  3744, confirmed via librodm_foot.txt's III NEFI section; both entries'
  bare "Véase c" → this chapter's own 9c = 4239, confirmed via
  librodm_foot.txt's LIBRO DE MORMÓN section, page 573's entry).
  Whole-document footnote-number sweep via the fresh pptext
  footnote-check section: max=4259, the new range 4237-4259 fully
  contiguous across both of pptext's anchor buckets, zero duplicates,
  zero out-of-range values. Fresh pptext/WSL regeneration
  (`report_wsl_20260803b.html`): 3 new Spellcheck Suspect Words from
  this page's vocabulary — "bautize" (v.23), "dias" (v.28, this
  document's only unaccented instance vs. 154 accented "días"
  elsewhere), "despojáos" (v.28) — all three checked directly against
  BOM 1886 (pages_1886/page_0589.png-page_0590.png, book pages 571-572)
  and found to match 1886 exactly at the same verses, confirming genuine
  shared 1920/1886 period forms rather than 1920-only errors; added to
  `permitted words.txt`, no `errors in 1920.txt` entries needed. The
  same 1886 pages also independently corroborated this page's body text
  verse-for-verse (v.19-28). Whole-document mechanical sweeps
  (`check_spaced_punctuation.py`, `check_footnote_punctuation.py`,
  `check_verse_indent.py`) all clean on both master files; zero curly
  quotes in either master file.

- **2026-08-03**: Sessions A–E run for page 576 (Mormón 9:29-37, mid-chapter
  continuation of chapter 9 opened on page 573; no new chapter/subtitle —
  chapter 9, and the whole book LIBRO DE MORMÓN, ends this page at v.37
  "Amén."; LIBRO DE ÉTER's own heading begins on page 577), footnotes
  4260-4272, letters x,y,z completing the single-letter alphabet begun at
  page 573's "a", then wrapping per rule 16 into two-letter codes 2a-2j.
  Mandatory Section 8 1879 check applied to this page's own letter "2i"
  and cross-reference target letter "2j" (both contain "i"): fetched 1879
  pages 576-578 (book pages 568-570), whose parallel footnote block
  confirmed every entry on this page letter-for-letter, catching two
  initial Session A misreadings before the page was finalized — entry
  2i's target was first misread as "e" (1879 shows "s"; confirmed via
  content-fit, Mormón 5's own "s" = footnote 4149 "oraciones de los
  justos," matching v.36's "oraciones") and entry 2j's target was first
  misread as "i" (1879 shows "j"; confirmed via content-fit, III Nefi
  15's own "j" = footnote 3702 directly annotating "alianza" in v.8,
  matching v.37's "alianza"). Same-page swash-vs-plain-italic font
  comparison separately settled a "2a" vs. superficially "g"-like
  descender-shape question (the strict alphabetical count already
  established the letter had to be "2a"). Session B did an independent
  fresh re-read of fn_zoom against the finished page — all 13 Block 1
  entries and all 13 [N] marker placements confirmed, no discrepancies.
  Google cross-check (`check_google_crosscheck.py 576`): zero candidates
  after dismissing 6 footnote-marker-glue hits and 1 trailing
  footnote-block hit. Session D (`generate_block2.py 576`) resolved 12 of
  13 entries automatically (including 2i→4149 and 2j→3702, independently
  corroborating Session A's 1879-based letter corrections a third time);
  entry 4266 was left unresolved because it packs two "Véase <letter>,
  <Book> <Chapter>" clauses (a, Mormón 1; g, Mormón 8) joined by a
  semicolon inside one period-terminated sentence — same double-clause
  parsing limitation as page 575's 4253/4258 — resolved by hand instead
  (Mormón 1's own 1a = 4062; Mormón 8's own 8g = 4189, both a strong
  content fit for v.33's "nuestras planchas"). Whole-document footnote-
  number sweep (direct scan of librodm.txt's [N] body anchors vs Notas-
  section "N:" definitions, not just pptext's report): this page's own
  range 4260-4272 fully contiguous in both anchors and definitions, zero
  duplicates, zero out-of-range values anywhere in the document. Fresh
  pptext/WSL regeneration (`report_wsl_20260803c.html`): one new
  Spellcheck Suspect Word from this page's vocabulary — "ciudado" (v.29,
  "Tened ciudado de que no seáis bautizados") — checked directly against
  BOM 1886 (pages_1886/page_0590.png, book page 572), which prints the
  identical "ciudado," so this is a shared 1886/1920 error rather than a
  1920-only slip (same pattern as this document's existing "ricibirles"/
  "seperado" precedents, where 1886 agreement does NOT clear a word);
  RAE DLE has no entry for "ciudado" (only "ciudad"/"ciudadano"/
  "ciudadela"), zero hits across all three reference corpora vs. 68 for
  "cuidado" in Quijote, and the modern Spanish edition (Mormón 9:29) uses
  "Cuidaos" from the same "cuidar" root — added to both `errors in
  1920.txt` and `permitted words.txt`. "carácteres" (v.32) was already in
  `permitted words.txt` from an earlier page. Scanno check, curly-quote
  check, and Jeebies all clean document-wide; dash/special-situations/
  paragraph-level/book-level sections show nothing new from this page's
  line ranges. Whole-document mechanical sweeps
  (`check_spaced_punctuation.py`, `check_footnote_punctuation.py`,
  `check_verse_indent.py`) all clean on both master files; zero curly
  quotes in either master file.

- **2026-08-03**: Sessions A–E run for page 577 (Éther 1:1-20, the first
  page of a new book — LIBRO DE MORMÓN and chapter 9 ended cleanly at
  v.37 "Amén." on page 576), footnotes 4273-4278, letters a-f (fresh
  restart per rule 13, new book). The 1920 print shows only ONE all-caps
  title line before "CAPÍTULO 1." ("EL LIBRO DE ETHER.", no separate
  ordinal marker or subtitle paragraph, unlike III/IV Nefi's multi-line
  title blocks). None of this page's own letters (a-f) or the one
  cross-reference target ("Véase k, Mosíah 8") is i/l/1, so the
  mandatory Section 8 1879 check did not apply; Session B independently
  re-verified all 6 Block 1 entries and all 6 `[N]` markers against a
  fresh crop, no discrepancies. `insert_body_text.py 577` auto-inserted
  the Block 1/Notas book-header as "EL LIBRO DE ETHER" (literal title
  line, minus trailing period) — corrected by hand to "EL LIBRO DE
  ÉTHER" (accent added) in both `librodm_foot.txt` and (after Session D)
  `librodm.txt`'s Notas section, since the header is a structural
  navigation label (page 554 "LIBRO DF MORMON"→"LIBRO DE MORMÓN"
  precedent) and every other appearance of this book's name on the same
  page — the page's own running header (discarded per rule 2) and every
  body/footnote instance — carries the accent; 1886 (pages_1886/
  page_0591.png, book page 573/file 591) independently confirms
  "EL LIBRO DE ÉTHER." with the accent, settling it as a genuine
  1920-only title misprint (logged in `errors in 1920.txt`), not a
  disambiguation case like page 481's "III NEFI" (no ambiguity for a
  book named Éther — the "EL" prefix itself was correctly kept, since
  the document's convention preserves literal prefixes like "PRIMER" in
  "PRIMER LIBRO DE NEFI", not just this book's name). Session D
  (`generate_block2.py 577`) resolved all 6 entries cleanly, including
  "Véase k, Mosíah 8" → 1187 (Mosíah 8k, the twenty-four-plates/
  interpreters citation — exact content-fit for v.2's "veinticuatro
  planchas") and the self-reference "Véase d" → 4276 (this page's own
  entry d). Fresh pptext/WSL regeneration (`report_wsl_20260803.html`):
  Edit Distance independently corroborated the "antíguos"/"antiguos"
  finding (paired against the existing unaccented instance at line
  22912); Spellcheck flagged 7 new proper nouns/words from this page's
  Jaredite genealogy (Amnigáddah, Com, Heth, Heárthom, Kish, Seth,
  Éthem, antíguos) — all confirmed correct as printed via zoom, added to
  `permitted words.txt`. Three flagged-by-eye words were NOT caught by
  pptext (known gap, checked anyway per the mandatory-check procedure)
  and confirmed as genuine 1920-only errors via 1886 (pages_1886/
  page_0591.png) plus the modern LDS Spanish edition
  (churchofjesuschrist.org, Éter 1): v.1 "antíguos" (extra accent; RAE
  has no entry for it either), v.3 "primer parte" (should be "primera
  parte" — wrong gender agreement; this document's own footnote 1043
  already uses "primera parte" correctly elsewhere), and v.3 "Judios"
  (missing accent, should be "Judíos") — all four (including the title)
  added to `errors in 1920.txt` in book order after the existing Mormón
  9:29 entry. Separately, while cross-checking 1886's genealogy verses
  (v.7-14), found 1886 uses different accent placement for two proper
  names — "Móron"/"Shíblon" vs. 1920's "Morón"/"Shiblón" — but the
  modern edition sides with 1920's placement for both, and per the
  proper-noun exemption (rule 11, Session E step 4) this was NOT logged
  as an error, just noted for the record. Scanno check flagged "Com"
  (English stealth-scanno collision) — confirmed a genuine proper noun
  via zoom, covered by the same permitted-words addition. Dash,
  footnote-anchor (4265-4278 contiguous, no dupes), curly-quote, and
  special-situations sections all clean for this page's line range.
  Incidental whole-document finding (unrelated to this page, not
  investigated further — flagged for the editor): a footnote-anchor/
  Block-2-definition cross-check found 6 pre-existing `[N]` body anchors
  with no matching Block 2 "N:" definition anywhere in the document
  (365, 530, 805, 909, 1724, 1725), beyond the one already-documented
  Jacob 2:15/812 print-original gap — worth a dedicated look in a future
  session. Whole-document mechanical sweeps (`check_spaced_punctuation.py`,
  `check_footnote_punctuation.py`, `check_verse_indent.py`) all clean on
  both master files; zero curly quotes in either master file (direct
  character search, both files).

- **2026-08-03b**: Ad hoc whole-document integrity audit, prompted by a
  user question about 6 footnote numbers found (during page 577's
  Session E) to have a body `[N]` anchor but no matching Block 2 `N: `
  definition anywhere in `librodm.txt`'s Notas section: 365, 530, 805,
  909, 1724, 1725. All 6 predate the current per-page Session A-E
  workflow (all are low numbers from books transcribed before page 437,
  which is where individual `pages/page_NNN.txt` files begin) and were
  invisible to every previous Session E's footnote check because that
  check only ever verified anchor contiguity/no-duplicates/no-out-of-
  range for the page(s) currently being transcribed — never a full
  anchors-vs-Block-2-definitions cross-check spanning the whole document
  back to footnote 1. pptext's own footnote check has the same blind
  spot: it only inventories `[N]` anchors for dupes/range, and never
  looks at the Notas section's `N: ` definitions at all. Findings, each
  a distinct failure mode:
  - **365** (II Nefi 9h, "el ángel que cayó..." v.8): NOT actually
    missing from Block 1 — `librodm_foot.txt` had "9h, 365, Véase f, II
    Nefi 2." with a comma typo in place of the colon after "365",
    which is why a colon-anchored search missed it. Worse, the citation
    letter itself ("f") was also wrong — this is exactly the mandatory
    i/l/1-adjacent case (a cross-reference target letter), and running
    the Section 8 1879 check for the first time on this entry
    (pages_1879/page_0086.png + page_0087.png, book page 79, footnote
    key block: "h, see i, II. Nep. 2.") confirmed the target is "i", not
    "f" — content-fit is exact (II Nefi 2i = 268 = "II Nefi 9:8; Perla
    de Gran Precio, Moisés 4:3-4," the Moses account of Lucifer's fall,
    matching v.8's "aquel ángel que cayó de ante la presencia del Dios
    eterno" precisely; entry 9f=363 already independently cites II Nefi
    2f for the unrelated "expiación infinita" of v.7, so a second
    identical "f" citation would have been an odd duplicate — a red
    flag in hindsight). Fixed both the punctuation and the letter in
    `librodm_foot.txt` ("9h, 365: Véase i, II Nefi 2."). Block 2 side
    had a matching, independently-discovered artifact: a line "365,
    Véase 268." already existed (comma typo again, hence invisible to a
    colon-anchored regex sweep) — and its target, 268, already agreed
    with the freshly-derived correct answer, suggesting a past session
    once correctly worked out the resolution but never fixed the
    punctuation or propagated the letter correction back to Block 1.
    Fixed the comma to a colon.
  - **530, 909**: present in `librodm.txt`'s Notas section with fully
    correct reference text, but missing their own leading "NNN: "
    label — e.g. 530's line just read "Isaías 10:17; Malaquías 4:1."
    with nothing before it, immediately after 529's own (unrelated,
    complete) "Véase 522." line, so it silently read as an orphaned
    fragment rather than a numbered entry. Same pattern for 909
    ("Véase 908." with no "909: " prefix). Fixed by prepending the
    missing label in both cases; no research needed since the reference
    text was already correct, just unlabeled.
  - **805, 1724, 1725**: genuinely absent, no trace in any form (no
    orphaned content line, no mislabeled line) — clean jumps from N-1
    straight to N+1 in the Notas section. Resolved each from Block 1's
    own already-correct entries (no image work needed, since none of
    these are transcription questions — Block 1's chapter+letter
    entries were already right, they just never got carried over to
    Block 2): 805 (Jacob 2b) is a direct citation, copied verbatim:
    "Versículos 9,28,33,35; Jacob 3:7; Moroni 9:9-10." 1724 (Mosíah 5v,
    "Véase l, Mosiah 5") resolves within Mosíah's own chapter 5 lettering
    to 1138 (5l). 1725 (Mosíah 5w, "Véase d, II Nefi 2; También j, y m,
    II Nefi 9") is a double-clause cross-reference — resolved by hand to
    "Véase 263; También 367, y 370." (d/II Nefi 2=263; j/II Nefi 9=367;
    m/II Nefi 9=370), a resolution independently corroborated by finding
    an *already-correct* twin entry elsewhere in the document (1324)
    citing the exact same Block 1 target text and already resolved to
    the identical "Véase 263; También 367, y 370." — confirming both the
    individual letter lookups and the multi-clause format convention.
  Post-fix, a full document-wide anchors-vs-definitions sweep (`[N]`
  body anchors vs. Notas `N: ` definitions, footnotes 1 through 4278)
  comes back with zero duplicate Block 2 definitions, zero anchored-but-
  undefined numbers, and exactly one defined-but-unanchored number (812,
  the already-known and already-documented Jacob 2:15 print-original
  omission — see `errors in 1920.txt`). Whole-document mechanical
  sweeps (`check_spaced_punctuation.py`, `check_footnote_punctuation.py`,
  `check_verse_indent.py`) re-run clean on both master files after these
  direct edits. This class of defect (isolated single-entry gaps in the
  pre-437 portion of the book, likely dating to whatever manual/bulk
  process originally built out that section of Block 2 before the
  current script-driven workflow existed) may still have other instances
  beyond these 6 — this was a targeted fix of the specific numbers found,
  not a proof the pre-437 section is now exhaustively clean. Worth
  considering a standing periodic full-document anchors-vs-definitions
  sweep (the Python snippet used here is short and fast) as a permanent
  addition to Session E's checklist, rather than a one-off.

- **2026-08-03**: Sessions A–E run for page 578 (Éther 1:21-41, mid-
  chapter continuation — genealogy list Leví...Jared plus the Tower/
  language-confounding narrative through v.41), footnotes 4279-4285,
  letters g-m (continuing chapter 1's alphabet from page 577's a-f).
  This page's own letters i and l are both in the mandatory Section 8
  i/l/1 set: fetched 1879 pages 579-580 (book pages 571-572), whose
  parallel footnote block confirmed every 1920 entry letter-for-letter
  ("i, vers. 38-43...", "l, see i."). The same 1879 check also resolved
  a non-mandatory but closely related ambiguity: the swash-adjacent
  italic glyph for letter j (third body marker, v.34) reads visually
  near-identical to "i" in this font; strict alphabetical sequencing
  (g-h-i-j-k-l-m, no gaps/repeats possible, since row 2 already used
  "i") already implied it had to be j, and 1879 page 580's "j, see h."
  independently confirmed it — extended the check per Section 8's
  discretionary-extension clause. Session B independently re-verified
  all 7 Block 1 entries, all 7 `[N]` markers, and re-ran the i/l/j
  1879 check with fresh (not reused) crops — no discrepancies. Rule 8
  cascade: inserting marker `[4281]` pushed the v.33 "cólera que
  serían...tierra;" line to 74 chars; the overflow had to cascade
  across two further lines (first retry also landed at 74), ending
  with "dispersados." pushed onto the same output line as "34." — a
  mechanical rule-8 consequence of marker length, not a content
  change. The Google OCR cross-check (`check_google_crosscheck.py
  578`) caught one genuine transcription-worthy finding: v.37's
  "también" — Google read "tambien" (no accent) where mine had
  "también"; a high-zoom look at the print showed the acute accent
  sits squarely over the "i", not the "e" — the 1920 print genuinely
  reads "tambíen", a misprint, not "también". Corrected the
  transcription to match the print exactly (rule 32) and confirmed via
  1886 (pages_1886/page_0592.png, book page 574/file 592), which
  prints "tambien" with no accent at all — the same underlying pattern
  as the pre-existing `errors in 1920.txt` entry "Mosiah 25:4 tambíen
  (también) (tambien en 1886)". This page's OTHER instance of the same
  word, v.41's line-ending "y también" (the last word on the page), is
  correctly accented in the same print, confirming an isolated
  misprint rather than a page-wide convention. New entry added to
  `errors in 1920.txt` in book order (after the existing Éther 1:3
  entries); "tambíen" was already present in `permitted words.txt`
  from the earlier Mosíah 25:4 finding, so no new addition needed
  there. Fresh pptext/WSL regeneration (`report_wsl_20260803b.html`):
  Spellcheck Suspect Words did not list any of this page's 10 new
  Jaredite-genealogy proper nouns (Leví, Kim, Moriánton, Riplákish,
  Shez, Coriántum, Émer, Omer, Kib, Oríhah) despite standalone `aspell`
  confirming all 10 as misspelled — matches the documented 2026-07-17
  "known gap" (a word can fail to appear in this section for reasons
  unrelated to `permitted words.txt`); added all 10 to `permitted
  words.txt` regardless, following the "don't let a clean/missing flag
  talk you out of it" guidance, after independently confirming each
  against the 1879/1886 crops already pulled for the letter checks
  above. Scanno, curly-quote (also independently confirmed via direct
  character search, zero curly quotes in either master file), dash,
  and "full stop followed by unexpected sequence" sections all clean
  for this page's content — no new hits. Whole-document
  footnote-anchor/Block-2-definition cross-check re-run clean: zero
  duplicate definitions, zero anchored-but-undefined numbers beyond
  the one already-documented Jacob 2:15/812 print-original gap (the 6
  pre-437 gaps flagged during page 577's session were already resolved
  in the 2026-08-03b ad hoc audit, confirmed still clean here). A minor
  Block 2 wrap quirk in `generate_block2.py`'s `wrap_entry()` was
  noticed and hand-fixed for entry 4285 (a short semicolon-separated
  trailing segment landed on its own near-empty line instead of
  merging back with the prior wrapped line; not a rule violation since
  all lines were still under 72 chars, just untidy) — not worth a code
  fix for one occurrence, but worth knowing the wrap function can do
  this if it recurs. Whole-document mechanical sweeps
  (`check_spaced_punctuation.py`, `check_footnote_punctuation.py`,
  `check_verse_indent.py`) all clean on both master files.
- **2026-08-04**: Sessions A–E run for page 579 (Éther 1:41-43, finishing
  chapter 1, plus the CAPÍTULO 2 opening through mid-v.7), footnotes
  4286-4297, letters n-p (continuing chapter 1's alphabet from page
  578's g-m) then a-i (chapter 2's own alphabet restart per rule 13).
  Block 1 entry 1p ("Éther 15:2.") required extensive investigation: the
  superscript "p" that should precede it in the footnote block is
  genuinely unprinted in the 1920 scan (confirmed via many high-zoom
  crop attempts — truly blank ink, not a narrow-space-vs-merge or
  i/l/1 misread) even though the citation text itself IS printed and
  the body's own "p" marker (v.43, before "grande") is fully legible.
  Resolved via alphabetical sequence (n/o/p must follow chapter 1's
  a-m) plus the mandatory-adjacent 1879 cross-check
  (pages_1879/page_0580.png: "n, Ether 6:16. o, The Lord brought them
  upon the western coast of North America. p, Ether 15:2." — three
  separate entries, confirming the letter and settling an initial
  misreading of "El Señor...América." as one continuous two-reference
  sentence for entry o alone). On Session E review this was promoted to
  `errors in 1920.txt` as "Footnote Éther 1p faltando la letra p en el
  bloque de notas", matching the existing "Footnote Alma 9g faltando la
  g." precedent for a missing footnote-key letter — a change from
  Session A's initial call not to log it, since the established
  precedent covers exactly this defect class. Mandatory Section 8 1879
  check also performed for this page's own letter i (v.7, "país de
  promisión"): pages_1879/page_0581.png fn block confirmed "i, vers.
  8:12-15. See o, Ether 1. Also see d, II. Nep. 1." matching the 1920
  reading exactly, including both cross-references (entry i's "Véase o"
  targets this same page's entry o; "también véase d" targets II Nefi
  1's own letter d, a different book, left unresolved by
  `generate_block2.py` along with the "Véase o" clause — the script's
  single-`Véase`-clause parser can't split a "Véase X...; también véase
  Y..." entry into two separate resolutions, a known limitation also
  visible in a few older pre-437 entries in the document that
  apparently WERE resolved by hand at some point; entry 4297 was left
  in letter form as the script's own documented behavior, not
  hand-patched). Session B independently re-verified all 12 Block 1
  entries and all 12 `[N]` body markers against fresh crops (not reused
  from Session A) — no discrepancies, including a fresh independent
  redo of the i/n/o/p 1879 checks. Rule 8 cascade applied twice: v.4's
  "que cuando llegaron al [4292]valle de Nimrod, [4293]descen-" hit 76
  chars after both markers, resolved by moving the rejoined word
  "descendió" (with its marker) to start the next line instead of
  splitting it back apart; v.7's "al [4297]país de promisión...sobre
  todos los" hit 77 chars, resolved by moving "todos los" to the next
  line. Two straightforward rule-7 rejoins (v.5 "desierto;", v.43
  "posteridad.") needed no cascade. New proper nouns Nimrod and Deseret
  were already in `permitted words.txt` from earlier pages; no other
  new-page word was flagged anywhere in a freshly regenerated pptext
  report (`report_wsl_20260804.html`) — spellcheck, edit distance,
  hyphenation, character checks, scanno, curly quote, special
  situations (this page's four "standalone 1" hits are the
  long-established `Book Chapter:Verse` false-positive category), book
  level, and paragraph level all clean. Footnote check confirmed all 12
  new anchors present exactly once, split across pptext's two anchor
  buckets only because the rule-8 cascade placed [4293] at the start of
  its line (a known, harmless bucketing quirk, not a real duplicate/
  missing-anchor finding). Whole-document footnote-anchor/Block-2-
  definition cross-check re-run clean: zero duplicate definitions, zero
  anchored-but-undefined numbers beyond the already-documented Jacob
  2:15/812 print-original gap. Whole-document
  `check_spaced_punctuation.py`, `check_footnote_punctuation.py`, and
  `check_verse_indent.py` all clean on both master files.

- **2026-08-04**: Sessions A–E run for page 579 (Éther 1:41-43, finishing
  chapter 1, plus the CAPÍTULO 2 opening through mid-v.7), footnotes
  4286-4297, letters n-p (continuing chapter 1's alphabet from page
  578's g-m) then a-i (chapter 2's own alphabet restart per rule 13).
  Block 1 entry 1p ("Éther 15:2.") required extensive investigation: the
  superscript "p" that should precede it in the footnote block is
  genuinely unprinted in the 1920 scan (confirmed via many high-zoom
  crop attempts — truly blank ink, not a narrow-space-vs-merge or
  i/l/1 misread) even though the citation text itself IS printed and
  the body's own "p" marker (v.43, before "grande") is fully legible.
  Resolved via alphabetical sequence (n/o/p must follow chapter 1's
  a-m) plus the mandatory-adjacent 1879 cross-check
  (pages_1879/page_0580.png: "n, Ether 6:16. o, The Lord brought them
  upon the western coast of North America. p, Ether 15:2." — three
  separate entries, confirming the letter and settling an initial
  misreading of "El Señor...América." as one continuous two-reference
  sentence for entry o alone). On Session E review this was promoted to
  `errors in 1920.txt` as "Footnote Éther 1p faltando la letra p en el
  bloque de notas", matching the existing "Footnote Alma 9g faltando la
  g." precedent for a missing footnote-key letter — a change from
  Session A's initial call not to log it, since the established
  precedent covers exactly this defect class. Mandatory Section 8 1879
  check also performed for this page's own letter i (v.7, "país de
  promisión"): pages_1879/page_0581.png fn block confirmed "i, vers.
  8:12-15. See o, Ether 1. Also see d, II. Nep. 1." matching the 1920
  reading exactly, including both cross-references (entry i's "Véase o"
  targets this same page's entry o; "también véase d" targets II Nefi
  1's own letter d, a different book, left unresolved by
  `generate_block2.py` along with the "Véase o" clause — the script's
  single-`Véase`-clause parser can't split a "Véase X...; también véase
  Y..." entry into two separate resolutions, a known limitation also
  visible in a few older pre-437 entries in the document that
  apparently WERE resolved by hand at some point; entry 4297 was left
  in letter form as the script's own documented behavior, not
  hand-patched). Session B independently re-verified all 12 Block 1
  entries and all 12 `[N]` body markers against fresh crops (not reused
  from Session A) — no discrepancies, including a fresh independent
  redo of the i/n/o/p 1879 checks. Rule 8 cascade applied twice: v.4's
  "que cuando llegaron al [4292]valle de Nimrod, [4293]descen-" hit 76
  chars after both markers, resolved by moving the rejoined word
  "descendió" (with its marker) to start the next line instead of
  splitting it back apart; v.7's "al [4297]país de promisión...sobre
  todos los" hit 77 chars, resolved by moving "todos los" to the next
  line. Two straightforward rule-7 rejoins (v.5 "desierto;", v.43
  "posteridad.") needed no cascade. New proper nouns Nimrod and Deseret
  were already in `permitted words.txt` from earlier pages; no other
  new-page word was flagged anywhere in a freshly regenerated pptext
  report (`report_wsl_20260804.html`) — spellcheck, edit distance,
  hyphenation, character checks, scanno, curly quote, special
  situations (this page's four "standalone 1" hits are the
  long-established `Book Chapter:Verse` false-positive category), book
  level, and paragraph level all clean. Footnote check confirmed all 12
  new anchors present exactly once, split across pptext's two anchor
  buckets only because the rule-8 cascade placed [4293] at the start of
  its line (a known, harmless bucketing quirk, not a real duplicate/
  missing-anchor finding). Whole-document footnote-anchor/Block-2-
  definition cross-check re-run clean: zero duplicate definitions, zero
  anchored-but-undefined numbers beyond the already-documented Jacob
  2:15/812 print-original gap. Whole-document
  `check_spaced_punctuation.py`, `check_footnote_punctuation.py`, and
  `check_verse_indent.py` all clean on both master files.
- **2026-08-04**: Sessions A–E run for page 580 (Éther 2:8-15, continuing
  chapter 2), footnotes 4298-4301, letters j-m (continuing chapter 2's
  alphabet from page 579's a-i). Mandatory Section 8 1879 check on
  letter l (v.14 marker, "desde") caught a real misread before it became
  an error: an initial zoomed read of the 1920 glyph after "Véase"
  looked like it could be "j", but the independent 1879 cross-check
  (pages_1879/page_0582.png: "l, see f.") confirmed it's actually "f"
  — cross-referencing back to page 579's own letter f (v.4, "una
  nube"), a strong content-fit match with v.14's own cloud reference.
  Also confirmed via pages_1879/page_0581.png and page_0582.png: the
  two "Véase i" cross-references (letters j and m) both correctly
  target chapter 2's own letter i (page 579, footnote 4297, v.7 "país
  de promisión"); letter k's direct citation ("I Nefi 13:19; II Nefi
  1:7; 10:10-14.") also confirmed matching exactly. Session B
  independently re-verified all 4 Block 1 entries and all 4 `[N]` body
  markers against fresh crops (not reused from Session A) — no
  discrepancies, including a fresh independent redo of all three i/l/1
  checks above. `check_google_crosscheck.py` caught one genuine
  transcription error (Session A had mistakenly added an accent,
  "únicamente", not present in the print — corrected to "unicamente";
  1886 confirmed the same unaccented form, so not a 1920-only error,
  no `errors in 1920.txt` entry) and flagged one spot that turned out
  to be genuine 1920 print content, not a transcription error: v.10's
  "la posea. tiene" — a period where a comma belongs, confirmed via a
  dedicated high-zoom crop (a plain round dot on the baseline, no
  comma tail) and via Google's OCR reading a comma at the same spot (a
  classic period/comma OCR confusion, correctly not treated as
  counter-evidence against the direct zoom). The editor independently
  confirmed against 1886 (book page 576/file 594) that this is a
  genuine 1920-only misprint (1886 correctly has a comma) — logged in
  `errors in 1920.txt` as "Éther 2:10 posea. (posea,)". The editor also
  had v.14's unaccented "a la conclusión" (missing the expected "á")
  checked against 1886: it matches 1886 exactly (also unaccented), so
  not a 1920-only error, but the editor asked for it to be logged
  anyway as a departure from the preposition's standard accented form
  and from this same page's own consistent "á" usage elsewhere —
  logged as "Éther 2:14 a la conclusión (á la conclusión)". This is the
  first `errors in 1920.txt` entry in this project logged despite
  matching 1886, on editor instruction rather than the usual
  1886-divergence criterion — worth remembering as precedent if a
  similar "matches 1886 but still worth flagging" case comes up again.
  `Moriáncumer` and `unicamente` were already in `permitted words.txt`
  from earlier pages; no new page-580 word was flagged anywhere in a
  freshly regenerated pptext report (`report_wsl_20260804.html`) —
  spellcheck, edit distance, hyphenation, scanno, curly quote checks
  all clean for this page's content. The "full stop followed by
  unexpected sequence" paragraph-level check independently surfaced
  the same v.10 "posea." finding (already resolved above); no other
  new hits in that section belonged to this page — the section's
  other listed hits are pre-existing, outside page 580's own content,
  and out of scope for a routine per-page Session E (per the skill's
  documented "efficient re-walkthrough" guidance, which scopes routine
  runs to the new page's own line range, not a full historical
  backlog re-audit). Whole-document footnote-anchor/Block-2-definition
  cross-check re-run clean: zero duplicate definitions, zero
  anchored-but-undefined numbers beyond the already-documented Jacob
  2:15/812 print-original gap. Whole-document
  `check_spaced_punctuation.py`, `check_footnote_punctuation.py`, and
  `check_verse_indent.py` all clean on both master files.
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
- **2026-08-05**: Sessions A–E run for page 582 (Éther 2:25, finishing
  chapter 2 mid-sentence, then CAPÍTULO 3 opens and runs 1-6, ending
  mid-verse-6), footnotes 4307-4313, letters a-g (chapter 3's own
  alphabet restart). None of this page's seven superscripts (a-g) are
  i/l/1, so the mandatory Section 8 1879 check did not apply to any of
  them; confirmed via direct zoom of each. One hyphenated line-break
  split rejoined per rule 7 (v.25 continuation "sum-/mergidos"), one
  more within CAPÍTULO 3 (v.6 "pro-/nunciado"); neither needed a rule 8
  cascade, but a footnote-marker-caused overflow on the page's own last
  line did — with both [4312]/[4313] markers inserted, "...vió el dedo
  del Señor," reached 76 characters with no following image line on the
  page to absorb the overflow, so "Señor," was displaced to the start
  of page 583 per the same page-boundary logic as rule 10 (there for a
  split word, here for marker overflow); page 582 itself ends "...vió
  el dedo del".
  Three genuine 1920-only findings this page, two resolved as NOT
  errors and one confirmed as a real error: (1) v.25 "veáis
  summergidos" — genuine double-m in print, confirmed archaic and
  shared with 1886 (pages_1886/page_0596.png, book page 578), added to
  `permitted words.txt`, no errors-log entry. (2) v.3 "estos años" — an
  initial medium-zoom crop looked like it showed an accent on the "a"
  (flagged per rule 36), but Google's OCR read plain "años" and a
  follow-up 20x-zoom crop confirmed no diacritic at all — the apparent
  mark was a scan artifact, not real type; matches the 2026-07-26
  "trust Google's silence" precedent exactly. (3) v.2 "la caída."
  (footnote c marker on "la") — the 1920 print genuinely shows a period
  where the sentence continues ("nuestra naturaleza ha venido..." stays
  lowercase), caught by the Google cross-check after an initial raw
  read had silently smoothed it to a comma; confirmed via 1886
  (pages_1886/page_0596.png, book page 578): a comma. This is now the
  *third* instance of this exact 1920 misprint pattern in this same
  neighborhood (after page 580 v.10 "posea." and page 581 footnote q
  "volteados."); logged in `errors in 1920.txt` as "Éther 3:2 caída.
  (caída,)", inserted in book/chapter/verse order after the existing
  Éther 2:24 "superficia" entry. v.1 "subío" (non-standard í-accent)
  also flagged but confirmed matching 1886 exactly — legitimate archaic
  form, added to `permitted words.txt` alongside the new place name
  "Shelem" (chapter 3's mountain, first occurrence in the document).
  Session B independently re-verified all 7 Block 1 entries and all 7
  `[N]` body markers against fresh crops (not reused from Session A) —
  no discrepancies. Both `check_google_crosscheck.py` and
  `check_line_wrap.py` turned out to only inspect this page's first 5
  lines (their shared line-reading helper stops at the first blank line
  after `Página N`, and this page's rule-3 blank line before `CAPÍTULO
  3.` was mistaken for end-of-body) — noted as a tool limitation in the
  page's Corrections log; the rest of the page was cross-checked
  manually against `google_text_1920/page_0604.txt` directly, which is
  in fact how the "la caída."/"años" findings above were caught.
  Session E regenerated a fresh pptext report via WSL
  (`workspace/report_wsl_20260805.html`) and used the line-range
  technique to isolate this page's citations; besides the three
  spellcheck words above, every other citation in range was the
  already-documented "paragraph starts with upper-case word"/
  standalone-number false-positive category. Whole-document
  `check_spaced_punctuation.py`, `check_footnote_punctuation.py`, and
  `check_verse_indent.py` all clean on both master files; whole-document
  footnote-anchor/Block-2-definition cross-check re-run clean (zero
  duplicate definitions, zero anchored-but-undefined numbers beyond the
  already-documented Jacob 2:15/812 gap; footnote-number range 1-4313
  fully accounted for, zero duplicates, zero missing beyond 812).
- **2026-08-05**: Sessions A–E run for page 583 (Éther 3:6-17, the tail
  of the "vió el dedo del Señor" theophany through Christ's declaration
  "Yo soy Jesu Cristo... el Padre y el Hijo" and Moroni's closing note
  that Jesus showed himself to this man as he did to the Nephites),
  footnotes 4314-4323, letters h-q (continuing chapter 3's own a-g
  alphabet from page 582). Two of this page's ten superscripts (i, l)
  are on the mandatory Section 8 1879-check list; both confirmed via
  fresh zoom (i = short stroke, separated dot; l = continuous unbroken
  stroke) and independently against 1879 (file_page 585, book page
  577, reached by paging forward from chapter_map.csv's listed 1879
  page 583 — that page turned out to still be 1879's own longer,
  differently-divided "Chapter III," containing unrelated earlier
  verses; 1879's chapter divisions don't track 1920's page-for-page
  here even within the same nominal chapter number). The discretionary
  extension of that same 1879 check to a non-i/l/1 letter caught a
  real letter misread: footnote p's cross-reference target, initially
  read "Véase o, Éther 1." from a medium-zoom crop, was corrected to
  "Véase e, Éther 1." after a tighter zoom crop and the 1879 page
  ("p, see e, Ether 1.") both confirmed a script "e", not "o". A page-
  boundary case new to this project's precedent: page 582's Corrections
  log (previous session) had displaced the word "Señor," off its own
  last line, reasoning that marker overflow ([4312]/[4313] brackets)
  pushed the transcribed line past 72 chars with no following image
  line on that page to absorb it. Direct inspection of the actual 1920
  print this session showed the source line itself (with slim
  superscript letters, not bracketed numbers) fits "...vió el dedo del
  Señor," in full — the apparent word-split was purely an artifact of
  this project's own bracketed footnote-marker notation, not a real
  print-level word break. Per rule 8/10's page-boundary mechanism, this
  page's transcription still begins with "Señor," prepended to the
  actual first printed line, exactly as the prior session's Corrections
  note anticipated. A second, ordinary rule-8 overflow (v.13's
  redimido-marker line hitting 73 chars) needed one word moved to the
  next line, no further cascade. A Google-crosscheck candidate (v.9 "Á
  causa" — Google read plain "A") was confirmed via high-zoom crop to
  be a genuine, clearly-printed accent and an ordinary OCR miss on an
  accented capital, not a real ambiguity — no action taken. Session B
  independently re-verified all 10 Block 1 entries and all 10 `[N]`
  body markers against fresh crops of both the 1920 and 1879 pages (not
  reused from Session A) — all reference text and marker placements
  confirmed matching, including the corrected footnote-p reading; no
  discrepancies. Session E regenerated a fresh pptext report via WSL
  (`workspace/report_wsl_20260805b.html`) and used the line-range
  technique to isolate this page's citations. One genuine new
  spellcheck flag, "Enoch" (BoM/Biblical proper name in footnote
  4318's text, matches 1920/1879 spelling exactly) — added to
  `permitted words.txt`, no errors-log entry. One structural false
  positive: "line starts with suspect punctuation" flagged the line
  beginning "; y se convertirán..." — a direct, unavoidable consequence
  of the v.14 "eterna-"/"mente" hyphen rejoin (rule 7) pushing the
  following (already space-stripped, rule 31) semicolon to the start of
  the next line, not a transcription defect. This page's own
  Corrections log was swept against the mandatory 1886-comparison
  check; none of its entries describe a suspected 1920 print misprint,
  so no new `errors in 1920.txt` entries resulted. Whole-document
  `check_spaced_punctuation.py`, `check_footnote_punctuation.py`, and
  `check_verse_indent.py` all re-run clean on both master files;
  whole-document footnote-anchor/Block-2-definition cross-check re-run
  clean (zero duplicate definitions, zero anchored-but-undefined
  numbers beyond the already-documented Jacob 2:15/812 gap;
  footnote-number range 1-4323 fully accounted for, zero duplicates,
  zero missing beyond 812); direct curly-quote character scan also
  clean.
- **2026-08-05**: Sessions A–E run for page 584 (Éther 3:18-28, the
  brother of Jared's certain knowledge from having seen the Lord's
  finger, through the Lord's instructions to write, seal, and later
  reveal the sealed record and the two interpreter-stones), footnotes
  4324-4337, letters r-2e (continuing chapter 3's own alphabet from
  page 583, running past z into the two-letter 2a-2e forms). None of
  this page's footnote letters or cross-reference target letters (r,
  s, t, u, v, w, x, y, z, 2a-2e; targets f, e, n, h) fell in the
  mandatory i/l/1 set, so no Section 8 1879 cross-check was
  triggered — confirmed independently on both Session A's and
  Session B's fresh crops. A real rule 7 hyphen-rejoin was caught in
  the raw line-by-line pass: v.25's "le 2cmos-"/"tró al hermano"
  split across the line break, rejoined to "mostró". Three Google
  cross-check candidates were investigated and all resolved in favor
  of the existing transcription: v.19 "sabía" (an apparent second
  accent mark on the "a" was confirmed a stray speck via Google's
  plain, ordinarily-accented OCR reading, per rule 36); v.25
  "mostró" (Google misread a letterpress-damaged "ó" glyph as "í";
  kept as "mostró" both on strong thematic grounds — the whole
  passage repeats "mostrar" in v.18/25/26/27 — and the damaged
  glyph's own faint accent-stroke remnant); and v.26 "cosas—le" (an
  ordinary Google omission of a genuine em-dash, not a real
  ambiguity). A genuine, if inconsistent, printed spelling was noted
  and preserved: v.24 "hé aquí" carries an acute accent (confirmed by
  tight zoom and independently corroborated by Google's OCR), while
  v.23's "he aquí" earlier on the same page does not — both
  transcribed exactly as printed, no misprint question since this
  uses the document's normal acute accent, not an unusual mark under
  rule 36. Session B independently re-verified all 14 Block 1
  entries/markers against a fresh crop — no discrepancies. Session D
  content-fit sanity check passed cleanly for every cross-reference,
  including two book cross-references confirmed by direct lookup:
  "z, Véase h, Éther 1" resolved to Éther 1h (the Tower-of-Babel
  language-confounding footnote, matching "confundido" in v.24) and
  "y/2b/2e, Véase n, Mosiah 8" all resolved to Mosíah 8n (the
  interpreter-stones footnote, matching the "dos piedras" theme
  running through v.23-28). Session E's pptext sweep found zero new
  spellcheck or edit-distance flags from this page's vocabulary — no
  `permitted words.txt` additions this session. No suspected 1920
  misprints on this page, so no new `errors in 1920.txt` entries.
  Whole-document `check_spaced_punctuation.py`,
  `check_footnote_punctuation.py`, `check_verse_indent.py`, and the
  footnote-anchor/Block-2-definition cross-check all re-run clean
  (footnote range 1-4337 fully accounted for, zero duplicates, zero
  missing beyond the already-documented Jacob 2:15/812 gap); direct
  curly-quote character scan also clean.
- **2026-08-05b**: Sessions A–E run for page 585 (Éther 4:1-10, the
  start of a new chapter: Moroni's editorial explanation of why the
  brother of Jared's sealed vision was hidden by King Mosíah and will
  stay hidden until the Gentiles repent, plus the Lord's own words on
  faith, sanctification, and the coming forth of these things),
  footnotes 4338-4350, letters a-m (chapter 4's own alphabet, restarting
  at `a`). This page's own lettering includes both i (9th letter, on
  "Padre de los cielos" v.7) and l (12th letter, on "la tierra" v.9),
  so the Section 8 mandatory 1879 check was triggered and run twice
  (Sessions A and B, independently): pages_1879/page_0587.png confirms
  i lands on "the Father of the heavens" and l on "the earth shall
  shake," matching exactly, with every other letter/target (a-h, j, k,
  m; targets s, n, a, a) also confirmed against the same 1879 page.
  Two rule 7 hyphen rejoins ("excep-"/"ción" -> "excepción",
  "santifi-"/"carse" -> "santificarse") and one rule 8 rebalance
  (v.7's marker-lengthened "...de la tierra," line, 75 chars, moved
  "tierra," to the next line) were caught in the mechanical pass.
  Block 1 required several rule 23/24 range normalizations (consecutive
  verse pairs printed with a comma in the original — "1, 2", "21, 22",
  "7, 8", "29, 30" — hyphenated per rule 23). A genuine, if
  inconsistent, printed accent variation was found and preserved:
  footnotes c/f print "Mosíah" (accented) while footnote i prints
  "Mosiah" (unaccented) twice, and footnotes a/b/e's "Éther" citations
  are accented while footnote h's "Ether 3." is not — both confirmed
  via tight zoom crops (including a Google-OCR conflict on the "Mosiah"
  case: Google read it accented, but an extreme close-up crop showed no
  diacritic glyph at all, so Google was judged to be over-reading its
  own prior rather than evidence of a missed mark); treated as an
  established non-error missing-accent pattern, not logged in `errors
  in 1920.txt`. This page opens with a chapter heading right at the
  very top (`Página 585` / blank / `CAPÍTULO 4.` / blank / v.1), which
  is the known blind spot (first documented at page 505) that makes
  `check_google_crosscheck.py`'s body_lines() helper find 0 chars and
  skip the actual diff entirely; compensated with a manual line-by-line
  read of `google_text_1920/page_0607.txt` against the transcription,
  which confirmed everything including both of this page's suspected
  misprints below.
  Two genuine 1920-only grammar errors were found and logged in
  `errors in 1920.txt` (Éther 4:7): "ejerzen" for "ejerzan" (1886,
  RAE DLE, and the modern Spanish LDS edition all confirm "ejerzan";
  "ejerzen" is not a valid form of "ejercer" in any mood at all, and
  pptext's spellcheck section genuinely flags it, so it was also added
  to `permitted words.txt`) and "pueden" for "puedan" (1886 doesn't
  contain the corresponding clause at all — 1920 adds a phrase absent
  from 1886 but present in 1879 English — so this was settled instead
  by a whole-document grep showing this is the *only* exception among
  15+ other "para que pued-" instances in `librodm.txt`, all
  correctly subjunctive, plus RAE DLE and the modern edition's
  reflexive rewording, which is also subjunctive; "pueden" is a
  correctly-spelled ordinary word so no `permitted words.txt` entry
  was needed).
  Session D's `generate_block2.py 585` run mis-resolved footnote i
  (4346) to the wrong number and silently dropped its three trailing
  bare citations, producing "4346: Véase 1311." instead of the correct
  "4346: Véase 1096; Mosiah 3:8; 4:2; 7:27; Helamán 16:18." Root cause:
  the script's regex for a "Véase" clause runs to the entry's first
  period (the very end for an entry combining a cross-reference with
  trailing bare citations under one unterminated sentence), so the
  whole span got fed to the single-clause resolver; its comma-based
  book/chapter split then misparsed the trailing citation text as a
  garbled "book name," and `FootIndex.find_book_id()`'s fuzzy
  subset-match fallback let that garbage match the real "MOSIAH" book
  section purely because the token "MOSIAH" happened to appear inside
  it — landing on the wrong chapter (16 instead of 3). Manually
  corrected in `librodm.txt`; footnote d (4341, "Véase s, I Nefi 13;
  Mormón 8:14; Moroni 10:1-2.") hit the identical mis-parse path but
  happened to stay safely unresolved only because I Nefi chapter 10 has
  no letter s in `librodm_foot.txt` — not something to rely on for a
  future page. This is a general `generate_block2.py` bug (any Block 1
  entry mixing a "Véase" cross-reference with trailing bare citations
  under one sentence is at risk), documented in the page's Corrections
  log and flagged for the editor rather than patched this session.
  Session E's pptext sweep (fresh WSL regeneration,
  `report_wsl_20260805d.html`) found exactly one new spellcheck flag
  from this page's vocabulary ("ejerzen," handled above); no edit-
  distance match, no hyphenation/dash findings, no short/long-line
  issues beyond the established benign verse-boundary/short-Block2-
  entry pattern. Whole-document `check_spaced_punctuation.py`,
  `check_footnote_punctuation.py`, `check_verse_indent.py`, and the
  footnote-anchor/Block-2-definition cross-check all re-run clean
  (footnote range 1-4350 fully accounted for, zero duplicates, zero
  missing beyond the already-documented Jacob 2:15/812 gap); direct
  curly-quote character scan also clean.
- **2026-08-05c**: Sessions A–E run for page 586 (Éther 4:10-19, the
  continuation of chapter 4 — the Lord's promises of manifestations,
  greater things, and revelation to those who believe, closing with
  the call to repent, be baptized, and the promise given to Moroni's
  own generation), footnotes 4351-4364, letters n-z plus the two-letter
  code 2a (chapter 4's own alphabet, continuing from page 585's `m`).
  The page begins mid-verse (v.10 continuation) with no chapter
  heading, so no blank line follows `Página 586` per rule 1 — this was
  initially transcribed with a stray blank line by mistake and caught
  by `check_line_wrap.py`'s 0-body-lines blind spot (the same one
  documented at page 585, but this time a real bug rather than a
  legitimate chapter-heading case), then fixed. Four rule 7 hyphen
  rejoins and one rule 8 rebalance were caught mechanically. Two stray
  ink specks (extra marks after "el" in "hacer el bien" and after the
  comma in "estos anales,") were confirmed via 1886 comparison to be
  printing debris rather than real punctuation, and not transcribed as
  such — one of these was independently corroborated by Google's OCR
  also picking up a stray period at the same spot. This page's own
  footnote lettering contains no i or l itself, but cross-reference
  target letter "i" (footnote t, "Véase i, II Nefi 25") triggered the
  mandatory Section 8 check; the same 1879 comparison
  (pages_1879/page_0588.png) also caught and corrected an independent
  misread of footnote z's target letter, initially read from the 1920
  image alone as "r" but confirmed by 1879 ("z, see e, III Nep. 29")
  to be "e" instead — a swash-font shape-confusion case, not an i/l/1
  ambiguity, resolved by the same cross-check procedure. One genuine
  1920-only misprint was found and logged in `errors in 1920.txt`
  (Éther 4:18): "ne" for "en" in "los que crean ne mi nombre" (a
  letter transposition, confirmed via 1886 and the modern edition;
  not flagged by pptext's spellcheck since "ne" is a novel one-off
  non-word, so no `permitted words.txt` entry needed, per the "Jesu
  Cristo" precedent). Session D's `generate_block2.py 586` run hit the
  same known VEASE_CLAUSE-regex bug documented on page 585 (footnote z,
  4363, a "Véase" clause followed by trailing content under one
  un-terminated sentence); manually resolved both references ("e" to
  this chapter's own footnote e, 4342; "2f, Mormón 8" to 4214, after
  distinguishing it from an identically-numbered "8-2f" entry that
  belongs to III Nefi's chapter 8 elsewhere in `librodm_foot.txt`).
  Session E's fresh pptext regeneration (`report_wsl_20260805e.html`)
  found no new spellcheck or edit-distance flags from this page's
  vocabulary. Whole-document `check_spaced_punctuation.py`,
  `check_footnote_punctuation.py`, `check_verse_indent.py`, and the
  footnote-anchor/Block-2-definition cross-check all re-run clean
  (footnote range 1-4364 fully accounted for, zero duplicates, zero
  missing beyond the already-documented Jacob 2:15/812 gap); direct
  curly-quote character scan also clean.
- **2026-08-05d**: Sessions A–E run for page 587 (Éther 4:19's closing
  two lines, then all of chapter 5 in full, then chapter 6 opening
  verses 1-3 — Moroni's closing testimony of Éther, then the sealed-
  plates/three-witnesses chapter, then the start of the account of the
  shining stones), footnotes 4365-4377: chapter 4's continuing letter
  2b (resolving the "2b, see d, Mos. 4" cross-reference that page 586's
  Corrections log had flagged as present in 1879 but with no matching
  1920 marker found on page 586 itself — the marker turned out to be
  on this page instead, on "desde" in the v.19 continuation), chapter
  5's full alphabet a-i (9 footnotes), and chapter 6's opening a-c (3
  footnotes). No rule 7 hyphen rejoins were needed (no line-break
  hyphens on this page). Three ambiguous-letter cases were resolved via
  the mandatory/discretionary 1879 check (pages_1879/page_0589.png,
  independently re-cropped fresh for Session B): footnote 5b's
  cross-reference target letter, read as "c" from the 1920 image alone,
  was corrected to "e" (Éther 4's own footnote e, 4342) — strongly
  corroborated by content-fit, since 4342 itself cites "Éther 5:1"
  directly, a natural mutual back-reference; footnote 5g's first target
  letter, which looked close to "i" at zoom, was corrected to "t" (I
  Nefi 13's own footnote t) via the mandatory i/l/1 check; and 5g's
  second target mark, which looked like "gf", was corrected to "2f"
  (Mormón 8's own footnote 2f), matching the identical pattern already
  seen on page 586's footnote z. Chapter 5's own letter i (marking
  "cuando" in v.6) was independently confirmed via the same mandatory
  check with no change needed. `check_line_wrap.py` and
  `check_google_crosscheck.py` both flagged false positives from the
  same underlying limitation (their body-text extraction stops at the
  page's FIRST blank line) — this page has an early chapter-heading
  blank line after just 2 lines, before 30 more body lines across two
  further chapters — so both were worked around manually: careful
  direct per-line image reads for the line-wrap check, and a full
  manual read of `google_text_1920/page_0609.txt` for the Google
  cross-check, which corroborated every word of the transcription
  including all three resolved ambiguous letters. Session D's
  `generate_block2.py 587` hit the same known VEASE_CLAUSE-regex bug
  documented on pages 585-586 (multi-clause "Véase" entries) for two
  entries (4369, 4372); manually resolved to 410, and to 103/4016/4214
  respectively — content-fit sanity check passed emphatically, with
  three of the resolved targets (410, 790, 4310) directly citing this
  very page's own verses back (Éther 5:3-4, 5:4-6, and 6:2-3,10). No
  suspected 1920 misprints were found on this page (unlike page 586's
  "ne" error), so no new `errors in 1920.txt` entries. Session E's
  fresh pptext regeneration (`report_wsl_20260805f.html`) found no new
  spellcheck or edit-distance flags from this page's vocabulary.
  Whole-document `check_spaced_punctuation.py`,
  `check_footnote_punctuation.py`, `check_verse_indent.py`, and the
  footnote-anchor/Block-2-definition cross-check all re-run clean
  (footnote range 1-4377 fully accounted for, zero duplicates, zero
  missing beyond the already-documented Jacob 2:15/812 gap); direct
  curly-quote character scan also clean.
- **2026-08-06**: Sessions A–E run for page 588 (Éther 6:4-13),
  footnotes 4378-4382: chapter 6's continuing letters d-h (rebaños v.4,
  furioso v.5, cerrados v.7, luz v.10, costas v.12). None of this page's
  own letters or cross-reference targets (b, d) were i/l/1, so the
  mandatory 1879 check didn't apply; Session B independently re-verified
  all 5 entries/markers against a fresh crop with no discrepancies. Two
  rule-7 hyphen rejoins (superficie, multitud) kept at end of line; one
  (prosternaron) moved to start of next line instead since appending it
  would have reached 74 chars. Three suspected misprints were flagged in
  Session A and resolved in Session E via the 1886 image
  (pages_1886/page_0602.png, book page 584/file 602): "pudía" (v.7,
  1920 misprints "u" for "o" — 1886 has "podía"; genuine 1920-only
  error, added to `errors in 1920.txt` and `permitted words.txt`); the
  lowercase "y" opening a new sentence after the period at v.12 (1886
  has capital "Y" at the identical spot — the period itself matches
  1886, only the capitalization is wrong; genuine 1920-only error,
  added to `errors in 1920.txt`); and "puesque" (v.7, one word — 1886
  prints the identical spelling at the same spot, so this is a
  legitimate archaic form shared by both editions, already in
  `permitted words.txt` from an earlier page, no new entry needed).
  Google's OCR (`google_text_1920/page_0610.txt`) independently
  corroborated all three anomalies. `generate_block2.py 588` resolved
  all 5 entries automatically, no unresolved cross-references; two
  targets (4378, 4381) directly cite this page's own chapter 6 verses
  back at itself. Session E's fresh pptext regeneration
  (`report_wsl_20260806.html`) found no new spellcheck or edit-distance
  flags for this page's vocabulary. Whole-document
  `check_spaced_punctuation.py`, `check_footnote_punctuation.py`,
  `check_verse_indent.py`, and the footnote-anchor/Block-2-definition
  cross-check all re-run clean (footnote range 1-4382 fully accounted
  for, zero duplicates, zero missing beyond the already-documented
  Jacob 2:15/812 gap); direct curly-quote character scan also clean.
- **2026-08-06**: Sessions A–E run for page 589 (Éther 6:14-29),
  footnotes 4383-4388: chapter 6's continuing letters i-n (desea v.19,
  era v.20, desearon v.22, lleva v.23, Oríhah v.27, que/murió v.29).
  Both i (v.19) and l (v.23) are in the mandatory ambiguous-letter set;
  the 1879 cross-check (pages_1879/page_0589.png-0591.png) confirmed
  both letters and all six targets content-for-content, with no
  discrepancy; Session B independently re-verified all 6 entries/markers
  against a fresh crop. No rule-7 hyphen rejoins reached the 73-char
  threshold requiring relocation (both — "Reunamos", "descendiesen" —
  stayed at end of line, 65 and 72 chars). Google's OCR
  (`google_text_1920/page_0611.txt`) independently corroborated three
  suspected misprints flagged in Session A and resolved in Session E via
  the 1886 image (pages_1886/page_0603.png, book page 585/file 603):
  "contrarle" (v.19, 1920 inserts an extra "r" — 1886 has "contarle";
  genuine 1920-only error, added to `errors in 1920.txt` and `permitted
  words.txt`); "veintiedós" (v.20, transposed letters — this same page's
  own v.16 correctly spells "veintidós"; genuine 1920-only error, added
  to both files); and "mandánoles" (v.25, missing a syllable — 1886 has
  "mandándoles"; genuine 1920-only error, added to both files, found via
  a direct standalone `aspell -a` check after the full-document pptext
  report failed to flag it — see the pages-469-470 suppression-gap
  precedent). Proper nouns "Jacom"/"Gílgah"/"Máhah"/"Pagag" added to
  `permitted words.txt` only (rule 11, unique BoM names). "elegieron"
  (v.25, v.26 — standard modern Spanish preterite of "elegir" is
  "eligieron") matched 1886's identical spelling "elegiéron" at both
  spots, treated as a legitimate archaic/period form per the page-588
  "puesque" same-lineage-agreement precedent, added to `permitted
  words.txt` only. `generate_block2.py 589` resolved all 6 entries
  automatically, no unresolved cross-references (none were
  cross-references at all — all six are direct verse/chapter citations).
  Whole-document `check_spaced_punctuation.py`,
  `check_footnote_punctuation.py`, `check_verse_indent.py`, and the
  footnote-anchor/Block-2-definition cross-check all re-run clean
  (footnote range 1-4388 fully accounted for, zero duplicates, zero
  missing beyond the already-documented Jacob 2:15/812 gap); direct
  curly-quote character scan also clean. One unrelated pre-existing
  finding (pptext "line starts with suspect punctuation",
  `librodm.txt` line 26004, Éther 3, predates page 589) was noticed
  in-passing and flagged for a future sweep rather than investigated now.
- **2026-08-10**: Sessions A–E run for page 590 (end of Éther 6:30, then
  Éther 7:1-11, the chapter opening), footnotes 4389-4398: chapter 7's
  new letters a-j (treinta y uno v.2, Kib v.3, Corihor v.3, país de
  Nehor v.4, Morón v.5 and again v.6, reducidos v.5, Desolación v.6,
  acero v.9, ciudad v.9). Letter i (v.9) and cross-reference target
  letter l (in entry h's "Véase 2l, Alma 22") are in the mandatory
  ambiguous-letter set; the 1879 cross-check
  (pages_1879/page_0592.png) confirmed the full 4-letter run
  "g, see e. h, see 2l, Alma 22. i, see e, I. Nep. 16. j, ver. 4."
  matching this page's own 4 body superscripts after f
  letter-for-letter and by content; Session B independently
  re-verified all 10 entries/markers against a fresh crop, including a
  fresh independent re-run of the 1879 check. Content-fit for both
  ambiguous cross-reference targets was additionally corroborated
  against already-transcribed entries elsewhere in `librodm_foot.txt`:
  I Nefi 16e (140) already cites "Éther 7:9" directly (this page's own
  v.9 "acero"), and Alma 22's continuing letter 2l (2238) cites
  recurring "tierra de Desolación" passages (this page's v.6
  "Desolación") — both zero-discrepancy matches. Entry 7g's own
  citation text is genuinely unprinted in the 1920 image (confirmed
  via multiple high-zoom crops of the blank gap between "f, Éther
  6:23." and "h, Véase 2l, Alma 22.", and independently corroborated by
  Google's OCR text showing the same blank — no garbled fragment at
  all, unlike every other tiny key letter on that line); reconstructed
  from 1879 ("g, see e.") as "Véase e." and logged as "Footnote Éther
  7g, 4395" in `errors in 1920.txt`, matching the existing "Footnote
  Alma 9g"/"Footnote Éther 1p" precedent for a wholly-omitted footnote
  entry. "occurió" (v.1, double c + single r — "Y occurió que Oríhah
  juzgó") confirmed via 1886 (pages_1886/page_0604.png, book page
  586/file 604: "Y ocurrió que Oríhah juzgó") as a genuine 1920-only
  misprint, a third distinct misspelling pattern of "ocurrió" alongside
  the already-documented "occurrió" (double c + double r) and "ocurrio"
  (accent-only) patterns; added to `errors in 1920.txt`. While
  researching this, found the identical "occurió" spelling already
  sitting in `permitted words.txt` from a much older page (1 Nefi
  18:25, `librodm.txt` line 2715) with no matching errors-log entry —
  confirmed via 1886 (pages_1886/page_0065.png, book page 47/file 65:
  "Y ocurrió que cuando viajábamos") as the same genuine error and
  added retroactively to `errors in 1920.txt` in its correct
  book/chapter/verse position, a missed-promotion gap of the kind
  Session E's mandatory sweep exists to catch. Proper nouns Corihor,
  Morón, and Desolación added to `permitted words.txt` only (rule 11)
  — bare accent variants against 1886's unaccented forms, not logged
  as errors (same precedent as page 589's "Jacom"/"Jácom"); Efraim
  (vs. 1886's "Ephraim") likewise added to `permitted words.txt` only
  — a legitimate Hispanicized spelling (ph->f), not an error.
  `generate_block2.py 590` resolved all 10 entries automatically
  (including both ambiguous cross-references, to 2238 and 140), no
  unresolved cross-references. Fresh pptext regeneration
  (`workspace/report_wsl_20260810.html`) shows zero new Spellcheck
  Suspect Words or Edit Distance hits for any of this page's words;
  the only report section any of them appear in is the already-covered
  "short lines check" category. Whole-document
  `check_spaced_punctuation.py`, `check_footnote_punctuation.py`,
  `check_verse_indent.py`, and the footnote-anchor/Block-2-definition
  cross-check all re-run clean (footnote range 1-4398 fully accounted
  for, zero duplicates, zero missing beyond the already-documented
  Jacob 2:15/812 gap); direct curly-quote character scan also clean.
  `check_line_wrap.py`/`check_google_crosscheck.py`'s body-line parsers
  both stop at the first blank line and so only ever compared this
  page's opening 4 lines (v.30) — a known limitation for any page with
  a mid-page chapter-heading blank line, not a defect in this page;
  the rest of the page (all of chapter 7) was cross-checked manually
  against `google_text_1920/page_0612.txt` directly instead, with full
  agreement throughout. No narrow-space-vs-merge candidates arose on
  this page.
- **2026-08-10**: Sessions A–E run for page 591 (Éther 7:12-27, continuing
  chapter 7 from page 590), footnotes 4399-4401: chapter 7's letters k
  (v.16, "primera herencia"), l (v.17, "Morón"), m (v.23, "vinieron").
  Letter l is in the mandatory ambiguous-letter set; the 1879 cross-check
  (pages_1879/page_0593.png) confirmed the full 3-letter run "k, ver. 17.
  See e. l, see k. m, vers. 24-26." matching this page's own lettering
  and content, re-verified independently in Session B against a fresh
  crop. Entry k's own "Véase [letter]" citation glyph looked
  heavily-inked/hard-to-distinguish in this session's zoomed crops, but
  the editor confirmed via direct look at the page that it clearly reads
  "e" — matches the 1879 parallel ("See e.") and content-fit against
  page 590's entry 7e ("Versículos 6,16,17..." already includes verse
  17); no `errors in 1920.txt` entry needed. Two narrow-space-vs-merge
  defaults arose and were transcribed as two words per the standing
  rule (grammar requires it; not escalated mid-pipeline): v.17 "dando la"
  and v.24 "de los" — flagged here for the editor's own convenience, not
  as pending questions. "tirra" (v.16, missing the "e" of "tierra")
  confirmed via 1886 (pages_1886/page_0605.png, book page 587/file 605:
  "conquistó la tierra de su primera herencia") as a genuine 1920-only
  misprint — RAE DLE has an entry for "tirra" but only as a colloquial
  variant of "tirria" (antipathy), an unrelated sense, and none of the
  three reference corpora contain it either; added to `errors in
  1920.txt` and `permitted words.txt`. "Nímrod" (v.22, accented) added to
  `permitted words.txt` as a legitimate accent variant of the
  already-listed "Nimrod" — confirmed via 1886 (same page) which prints
  the identical accented form "Ním-/rod" at the same verse.
  "Cohor" (distinct from "Corihor," both genuine Book of Mormon
  characters per the text) was not flagged by pptext at all (no
  `permitted words.txt` addition needed, matching the "Jesu Cristo"
  precedent for words aspell already accepts on its own).
  `generate_block2.py 591` resolved both cross-references automatically
  (4399→4393, 4400→4399), no unresolved cross-references. Fresh pptext
  regeneration (`workspace/report_wsl_20260810b.html`) flagged only
  "Nímrod" and "tirra" for this page in Spellcheck Suspect Words/Edit
  Distance, both resolved above; every other report hit in this page's
  line range was a whole-line highlight from the already-covered "short
  lines check" category. Whole-document `check_spaced_punctuation.py`,
  `check_footnote_punctuation.py`, `check_verse_indent.py`, and the
  footnote-anchor/Block-2-definition cross-check all re-run clean
  (footnote range 1-4401 fully accounted for, zero duplicates, zero
  missing beyond the already-documented Jacob 2:15/812 gap); direct
  curly-quote character scan also clean. `check_google_crosscheck.py`
  came back clean (zero candidates); `check_line_wrap.py` flagged a +2
  line-count difference against its Tesseract OCR estimate, manually
  re-verified against the image crops as an OCR under-count, not a
  reflow defect (raw 45-line count matches the image exactly).
- **2026-08-19**: Sessions A–E run for page 592 (Éther 7:27 chapter close
  + Éther 8:1-10, a new chapter opening mid-page), footnotes 4402-4404:
  chapter 7's continuing letter n (v.27, "através", the chapter's last
  footnote) and chapter 8's own restarted letters a (v.9, "anales") and
  b (v.9, "secretos", a long entry whose citation trails off with "Véase
  i, II Nefi 10,"). Letter n was heavily-inked/hard-to-distinguish in
  1920 zoomed crops (same difficulty class as page 591's k); the
  mandatory-for-i/l/1 1879 cross-check also applied to entry b's own
  internal cross-reference letter i — both independently confirmed via
  pages_1879/page_0594.png in both Session A and a fresh Session B
  crop, letter-for-letter and content-fit ("n, Ether 6:1-12."; "See i,
  II. Nep. 10."). Several suspected 1920-only misprints found and
  preserved as printed per rule 32, all later confirmed via 1886
  (pages_1886/page_0606.png) and promoted to `errors in 1920.txt`:
  v.9 "ledío" for "leído" (letter transposition; zero RAE/corpus hits,
  Google OCR corroborates the misread); v.9 "¿Porque, está" for
  "¿Porqué está" (missing accent + spurious comma; this document
  accents this exact interrogative 29/31 other times, RAE DPD confirms
  the accent is mandatory); "através" for "a través" at both its v.27
  and v.9 occurrences (genuine zero-gap merge confirmed at high zoom,
  not a narrow-space case; 1886 doesn't even print the "a" at either
  spot, so offered no direct letter-for-letter precedent either way;
  RAE has no entry for the fused form). Footnote 8b's own citation text
  ends in a comma rather than the expected period ("...II Nefi 10,");
  1879 confirms a period there ("...II. Nep. 10."), so also logged in
  `errors in 1920.txt` — this same comma caused `generate_block2.py` to
  leave the entry's "Véase i, II Nefi 10" cross-reference unresolved
  (its regex requires a terminating period), so the Block 2 entry
  (4404) was manually resolved to "Véase 398." (10i in the II Nefi
  section) rather than left in letter form, since the target was
  genuinely already known, not actually unresolvable. "Esrom" (v.4,
  proper name) added to `permitted words.txt` — flagged by a fresh
  pptext spellcheck run, confirmed via 1886 (same spelling) and
  distinguished from the unrelated currency-unit words "exrom"/"ezrom"
  (Alma 11) that Edit Distance Checks paired it against. Whole-document
  `check_spaced_punctuation.py`, `check_footnote_punctuation.py`,
  `check_verse_indent.py`, and the footnote-anchor/Block-2-definition
  cross-check all re-run clean (footnote range 1-4404 fully accounted
  for, zero duplicates, zero missing beyond the already-documented
  Jacob 2:15/812 gap); direct curly-quote character scan also clean.
  `check_google_crosscheck.py` and `check_line_wrap.py` both only
  compared this page's first 3 lines (Éther 7:27's chapter-close blank
  line before `CAPÍTULO 8.` triggers both scripts' first-blank-line
  cutoff) — the rest of the page (all of chapter 8) was cross-checked
  manually against `google_text_1920/page_0614.txt` directly instead,
  with full agreement throughout, including reproducing both suspected
  misprints. No narrow-space-vs-merge candidates arose on this page
  (the "através" merge is a true zero-gap fusion, not a narrow-space
  case, so it went to `errors in 1920.txt` rather than the batched
  narrow-space-vs-merge editor note).
- **2026-08-20**: Sessions A–E run for page 593 (Éther 8:10-22, all
  mid-chapter continuation), footnotes 4405-4407: chapter 8's
  continuing letters c (v.14, "juraron", oaths sworn), d (v.15, "los
  antiguos", cross-references back to the chapter's own b/4404), and e
  (v.18, "secreta"). Both c and e's own cross-reference target letter
  "i" (the mandatory i/l/1 check) were confirmed via 1879 — but 1879's
  pagination has drifted well past its nominal book_page+8 offset by
  this point in Éther: file_page 601 (nominal) and 600 both showed
  unrelated later-chapter content, and the actual match was found at
  file_page 595 (printed page "587"). That page's footnote block reads
  "c, see i, II. Nep. 10.  d, see b.  e, see i, II. Nep. 10." —
  confirmed identically in both Session A and a fresh, independent
  Session B crop. The `check_google_crosscheck.py` step caught a real
  transcription slip this run (not just a suspected-misprint
  candidate): v.20 "Moroni" was initially transcribed with an accent
  ("Moroní") from a zoomed read that saw a mark above the i, but
  Google's OCR read it plain, and a grep of `librodm.txt` confirmed
  this document's overwhelming, exclusive convention spells the name
  "Moroni" unaccented (hundreds of instances) — corrected before
  integration. Three suspected misprints were investigated against
  1886 (pages_1886/page_0606.png for v.10, page_0607.png for v.15/
  v.21) in Session E and all three were added to `errors in
  1920.txt`: v.10 "sí me trajeres" and v.21 "Neñtas" BOTH turned out
  to be shared with 1886 at the exact same spots (confirmed at high
  zoom, including a genuine tilde on 1886's own "Neñtas") — inherited
  from a common source rather than introduced by 1920, but still
  logged per user correction (2026-08-21): a shared 1886 reading only
  clears a word if it reflects a legitimate archaic/period spelling
  variant, not merely because 1886 happens to share the same mistake.
  Neither "sí" (yes/emphatic) for the unaccented conditional "si" (if)
  nor "Neñtas" for "Nefitas" is a legitimate variant of anything —
  both are obvious errors regardless of which edition originated them.
  v.15 "administro" was confirmed as a 1920-only error: 1886 uses a
  different verb entirely at that spot ("ministró"), so it offered no
  direct letter comparison, but the other 3 occurrences of this same
  verb elsewhere in `librodm.txt` (Alma 15:18, III Nefi 7:17, III Nefi
  10:19) are all correctly accented "administró" — this page's
  unaccented "administro" is the sole exception, and grammatically
  wrong (present tense in a past-tense narrative) rather than a merely
  decorative missing accent. None of the three flagged words
  ("administro", "formula", "Neñtas") appeared in a
  freshly-regenerated pptext report's
  Spellcheck Suspect Words section at all (all are real/acceptable
  word-forms to aspell in isolation) — consistent with the
  orthography-check skill's documented gap that a clean spellcheck
  section doesn't clear a word already confirmed problematic by other
  means, and confirms no `permitted words.txt` entries were needed
  (would have been no-ops, per the "Jesu Cristo" precedent). Report
  saved as `workspace/report_wsl_20260820.html`. Whole-document
  `check_spaced_punctuation.py`, `check_footnote_punctuation.py`,
  `check_verse_indent.py`, and the footnote-anchor/Block-2-definition
  cross-check all re-run clean (footnote range 1-4407 fully accounted
  for, zero duplicates, zero missing beyond the already-documented
  Jacob 2:15/812 gap). `check_line_wrap.py`'s advisory OCR line-count
  comparison flagged a +2 difference, but a direct recount of every
  raw printed line straight from the top/mid/bot crops matched the
  transcription's 45 body lines exactly, confirming the OCR undercount
  (a known OCR line-merging weakness) rather than a transcription
  defect. Body text ends mid-sentence at v.22 (no hyphen — an ordinary
  page-boundary break); verse 22 continues on page 594.
- **2026-08-21**: Sessions A–E run for page 594 (Éther 8:22-26, then
  chapter 9 opens mid-page with vv.1-2), footnotes 4408-4415: chapter
  8's continuing letters f-l (v.22 "sangre", v.23 "muertes"/"espada",
  v.24 "secreta"/"sangre", v.25 "destruir", v.26 "satán"), then chapter
  9 resets to a (v.1 "secretas"). The mandatory 1879 check (letters i
  and l, plus three "Véase i, II Nefi 10" cross-reference targets) was
  extended on editorial judgment to three OTHER swash-font targets that
  an initial 1920-only read misjudged as h/j/m — 1879's plain italic
  type (pages_1879/page_0596.png, printed page "588") unambiguously
  resolved all of them to k/f/n instead, confirmed via two independent
  crop passes (Session A and a fresh Session B re-crop at different
  coordinates). Two genuine 1920-only errors were found and added to
  `errors in 1920.txt` plus `permitted words.txt`: v.25 "ibertad"
  (missing initial "l" for "libertad," confirmed against 1886/RAE/
  modern-edition/corpora), and v.25 "apderearan" (letters "d"/"e"
  transposed vs. correct "apedrearan" — notable back-and-forth: an
  intermediate zoom crop briefly misread this as the correct spelling
  before a final crop with full ascender/descender visibility confirmed
  the transposition; Google's independent OCR agreed with the
  transposed reading throughout, and 1886/RAE/modern-edition all
  confirm "apedrearan" is correct, making 1920's form 1920-exclusive).
  A third candidate, v.23's apparent stray period ("la obra. de
  destrucción"), was initially logged as a genuine error after an
  extreme-zoom crop read it as a real, properly-formed period — this
  was WRONG and reversed same-day per user correction: the editor's own
  look at the scan showed the mark's stroke weight is visibly lighter
  than an ordinary period, and `google_text_1920/page_0616.txt`
  (Google's OCR, already checked at the time but its silence was
  mis-weighed against the mark's shape/position alone rather than its
  weight) independently confirms no period at that spot at all —
  transcription and `errors in 1920.txt` both corrected back to "la
  obra de destrucción" with no entry logged. Lesson: a mark's stroke
  weight against surrounding genuine punctuation is independent
  evidence from its shape/position, and pptext's own "full stop
  followed by unexpected sequence" check flagging the same spot is not
  itself confirmation the mark is real print — it only means the
  *transcribed* text (right or wrong) reads as an odd sequence.
  Whole-document `check_spaced_punctuation.py`,
  `check_footnote_punctuation.py`, `check_verse_indent.py`, the
  footnote-anchor/Block-2-definition cross-check, and a footnote-number
  duplicate/out-of-range/missing sweep (max anchor 4415) all re-ran
  clean (zero new gaps beyond the already-documented Jacob 2:15/812
  case). A "line starts with suspect punctuation" pptext flag on two
  rule-7 rejoin remainder lines (opening with ";" / ",") was checked
  against document precedent (an identical pre-existing case at line
  26004) and confirmed as an expected artifact of the mechanical
  rejoin rule, not a defect. `check_line_wrap.py` flagged a body-line-
  count difference that traced entirely to the script's own txt-side
  counter stopping at the first blank line (this page's mid-page
  chapter-heading break) rather than any reflow issue — confirmed by
  hand-counting all lines through the chapter 9 portion the script
  skips. Body text ends mid-sentence at v.2 of chapter 9 (no hyphen —
  an ordinary page-boundary break); verse 2 continues on page 595.
- **2026-08-22**: Sessions A–E run for page 596 (Éther 9:15-25,
  footnotes 4422-4428, chapter 9's continuing letters h-n: v.17 "toda"/
  "y de sedas"/"y de oro", v.18 "toda", v.19 "caballos", v.20
  "escogido"/"destruidos"). Note: page 595 (Éther 9:3-14, footnotes
  4416-4421) was found already fully integrated into `librodm.txt`/
  `librodm_foot.txt` with Sessions A-E complete when this session
  began — its own session apparently ran to completion in an earlier
  conversation but was never logged here or in CLAUDE.md's Current
  Progress snapshot (CLAUDE.md still listed "595" as the next page to
  do); not reconstructed retroactively here, only noted so the gap is
  visible. The mandatory 1879 check (letters i, l, and cross-reference
  target letter i in "Véase i, Éther 2") required locating the right
  1879 page by content rather than trusting chapter_map.csv's listed
  file_page 596 for chapter 9, which is only the chapter's *opening*
  page (1879 pages_1879/page_0596.png, printed page 588, showed
  chapter 8 v.22-24 followed by chapter 9 v.1-2) — the matching verses
  for this page's footnotes were two 1879 pages later
  (pages_1879/page_0598.png, printed page 590), confirmed via Session
  A's initial crop and independently re-confirmed at different crop
  coordinates in Session B. All letters matched 1920 exactly, no
  ambiguity. Three genuine errors were found and added to `errors in
  1920.txt` (plus `permitted words.txt` where flagged by pptext): v.22
  "Dedpués" (missing/wrong initial consonant for "Después," confirmed
  1920-exclusive against 1886 page_0610.png, zero corpus hits, flagged
  by pptext); v.22 "glorifició" (spurious "i" for "glorificó," caught
  by the Google-text cross-check — my initial transcription had
  silently "corrected" this to "glorificó" before the cross-check
  flagged the discrepancy and a fresh zoom crop confirmed the image
  genuinely prints the extra "i" — but confirmed SHARED with 1886,
  which prints the identical "glorifició," so logged per the
  established "error compartido entre ambas ediciones" pattern rather
  than as 1920-exclusive; RAE has no entry for the form and none of
  the three reference corpora attest it); v.25 "engendro" (missing
  accent on what should be "engendró," confirmed 1920-exclusive against
  1886 — the missing accent happens to spell a different real Spanish
  word, "engendro" the noun, so pptext's spellcheck never flags it at
  all, matching the documented "full pptext report is not proof a rare
  misprint won't be flagged" gap; both this and "glorifició" were
  therefore researched and logged independent of pptext's silence, per
  standing instruction, with no `permitted words.txt` entry for either
  since one would be a no-op). A fourth Google-crosscheck candidate
  (v.24 "hijas; viviendo," which Google's OCR read as a comma) was
  investigated and the ";" reading confirmed correct — a wider,
  higher-zoom crop showed both the semicolon's upper dot and lower
  comma-tail, which a first narrower crop had cropped out, causing
  Google's misread. v.20's justification-widened "sobre  todos" was
  silently normalized to one space per the blanket rule (not logged as
  an error). `curelomes`/`cumomes` (unique Book of Mormon animal names)
  and `jóven` (archaic accented form, confirmed matching 1886 exactly)
  were added to `permitted words.txt` with no errors-log entry.
  Whole-document sweeps (`check_spaced_punctuation.py`,
  `check_footnote_punctuation.py`, `check_verse_indent.py`, the
  footnote-anchor/Block-2-definition cross-check, a footnote-number
  duplicate/out-of-range/missing sweep [max anchor 4428], and a curly-
  quote scan) all re-ran clean, with only the already-documented
  Jacob 2:15/812 gap remaining. A fresh full pptext report was
  regenerated (`workspace/report_wsl_20260822.html`) and walked using
  the efficient line-range-filtering technique scoped to this page's
  new content (body lines 26549-26592, Block 2 lines 31359-31365);
  every section checked out clean or matched already-established
  benign patterns (the short-lines/adjacent-spaces/duplicate-lines
  sections' hits on this page's footnote lines were confirmed to be
  the same pre-vetted structural artifacts already documented for this
  project, not new defects). `check_line_wrap.py` reported a -1 body-
  line-count difference, matching the expected rule-7 rejoin (one
  hyphenated line split, "suma-"/"mente ricos.", rejoined into a
  single 72-character line in v.16) — no red flag.
- **2026-08-22**: Sessions A–E run for page 596 (Éther 9:15-25),
  footnotes 4422-4428, chapter 9's continuing letters h-n (v.17 "toda"/
  "y de sedas"/"y de oro", v.18 "toda", v.19 "caballos", v.20
  "escogido"/"destruidos"). Page 595 (Éther 9:3-14, footnotes
  4416-4421) was found already fully integrated with Sessions A-E
  complete when this session began, apparently from an earlier
  conversation whose log entry was never written — not reconstructed
  retroactively, just noted. The mandatory 1879 check (letters i, l,
  and cross-reference target i in "Véase i, Éther 2") required going
  two pages past chapter_map.csv's listed chapter-9-opening page
  (pages_1879/page_0598.png, printed page 590, not page_0596.png) to
  reach the matching verses; confirmed via independent crops in both
  Session A and B, all letters matching 1920 exactly. Three genuine
  errors added to `errors in 1920.txt`: v.22 "Dedpués" (1920-exclusive
  vs. "Después," flagged by pptext, zero corpus hits); v.22
  "glorifició" (spurious "i," caught by the Google-text cross-check
  after my initial transcription silently read it as "glorificó" —
  confirmed SHARED with 1886, which prints the identical form, so
  logged as an error compartido rather than 1920-exclusive; RAE has no
  entry for it); v.25 "engendro" (missing accent for "engendró,"
  1920-exclusive, invisible to pptext because the unaccented form
  happens to spell a different real word). Neither "glorifició" nor
  "engendro" got a `permitted words.txt` entry since pptext never
  flags them (would be a no-op, per the "Jesu Cristo" precedent). A
  second Google-crosscheck candidate (v.24 "hijas; viviendo," which
  Google read as a comma) was investigated and the semicolon reading
  confirmed correct via a wider zoom crop that showed both dot and
  comma-tail (a first, narrower crop had cut off the lower tail).
  `curelomes`/`cumomes` (unique Book of Mormon animal names) and
  `jóven` (archaic accented form matching 1886) were added to
  `permitted words.txt`, no errors-log entry. Whole-document sweeps
  (spaced punctuation, footnote punctuation, verse indent, the
  footnote-anchor/Block-2-definition cross-check, a footnote-number
  duplicate/out-of-range/missing sweep [max anchor 4428], curly-quote
  scan) all re-ran clean, only the already-documented Jacob 2:15/812
  gap remaining. A fresh pptext report
  (`workspace/report_wsl_20260822.html`) was walked scoped to this
  page's new content via the line-range-filtering technique; every
  section checked out clean or matched already-established benign
  patterns. `check_line_wrap.py` reported a -1 body-line-count
  difference matching the expected rule-7 rejoin (one hyphenated split,
  "suma-"/"mente ricos.", rejoined into one 72-char line in v.16) — no
  red flag.
- **2026-08-22**: Sessions A–E run for page 597 (Éther 9:26-35),
  footnotes 4429-4434, chapter 9's continuing letters o-t (v.26
  "secretos", v.28 "otra"/"gran", v.31 "venenosas"/"Sud"/"Zarahemla").
  The mandatory 1879 check (cross-reference target letter i in "Véase
  i, II Nefi 10") required going 3 file-pages past chapter_map.csv's
  listed chapter-9-opening page (pages_1879/page_0599.png, printed
  page 591, not the chapter-opening page_0608.png) to reach the
  matching verses — same pattern as pages 595-596, confirmed via
  independent crops in both Session A and B, letter "i" matching 1920
  exactly. A file-formatting bug was caught and fixed early in Session
  A: a stray blank line had been inserted between "Página 597" and the
  body text (violating rule 1, since this page continues mid-chapter
  rather than opening one) — `check_line_wrap.py` immediately flagged
  it (0 body lines detected instead of 38) because its parser expects
  no gap after a continuation page's header line; fixed before
  proceeding. Two genuine errors added to `errors in 1920.txt`: v.26
  "orta" (metathesis misprint of "otra," 1920-exclusive, no RAE entry,
  zero standalone corpus hits, not flagged by pptext); v.30
  "rapidamente" (missing accent for "rápidamente," shared with 1886 at
  this exact spot but still logged per the Alma 62:21 precedent, since
  "-mente" adverbs must keep the base adjective's accent regardless of
  1886 agreement). Two Corrections-log candidates were checked against
  1886 and confirmed as legitimate shared readings, not errors: v.28
  "prepararen" (archaic future subjunctive of "preparar," matches 1886
  exactly, same paradigm as "arrepintieren" two lines later) and v.34
  "Sucediendo que" (unusual phrasing vs. the "Y sucedió, que" pattern
  used in every other verse on this page, but 1886 prints the
  identical wording — a shared translation quirk, not a 1920-only
  deviation). None of the four got a `permitted words.txt` entry since
  a fresh full pptext run flagged none of them anywhere in the report
  (confirmed via direct substring search, not just the spellcheck
  section — per the "Jesu Cristo" precedent, an addition would be a
  no-op). The Google-text cross-check's one candidate (v.33 "más las
  serpientes" vs. Google's OCR dropping the "l") was confirmed via
  zoom to be a genuine "l" in print, Google's OCR error, no correction.
  Whole-document sweeps (spaced punctuation, footnote punctuation,
  verse indent, the footnote-anchor/Block-2-definition cross-check, a
  footnote-number duplicate/out-of-range/missing sweep [max anchor now
  4434], curly-quote scan) all re-ran clean, only the already-
  documented Jacob 2:15/812 gap remaining. A fresh full pptext report
  (`workspace/report_wsl_20260822b.html`) was regenerated and walked
  via distinctive-substring search for this page's new content (zero
  hits anywhere in the report for any of this page's flagged phrases).
  `check_line_wrap.py` reported an exact 38/38 match against the OCR
  line count once the blank-line bug above was fixed — no red flag.
- **2026-08-24**: Sessions A–E run for page 598 (Éther 10:1-9, chapter
  opening), footnotes 4435-4437, chapter 10's fresh letters a-c. Page
  598 opens Éther chapter 10 with no subtitle line (confirmed via
  image — CAPÍTULO 10. is followed directly by verse 1). The mandatory
  1879 check applied to footnote 10b's cross-reference letters k/l/q
  (l is in the ambiguous i/l/1 set) and 10c's target letter i, both
  checked in one pass against pages_1879/page_0600.png (printed page
  592): "b, see k, l, and q, Jacob 2. c, see i, II. Nep. 28." — exact
  letter-for-letter match with 1920, independently re-confirmed in
  Session B via fresh crops at different coordinates than Session A.
  The "l" glyph was also independently verified at high zoom on the
  1920 image itself as a continuous unbroken stroke (not "i"'s short
  stroke with a separated dot). No suspected misprints or genuine
  errors found on this page — all Corrections-log entries were
  mechanical (space-before-semicolon/comma normalization per rule 31,
  two justification-widened-gap normalizations per rule 6, one rule-7
  hyphen rejoin: "des-"/"cendientes" → "descendientes") or purely
  informational. Two whole-document scripts (`check_line_wrap.py`,
  `check_google_crosscheck.py`) both reported 0 body lines/chars for
  this page — traced to a real script limitation, not a transcription
  defect: both scripts' body-text parser stops at the first blank line
  after "Página N", and rule 1 mandates exactly that blank line before
  a chapter-heading page (confirmed against other already-completed
  chapter-opening pages using the identical layout, e.g. pages 449,
  456, 459). The Google cross-check was done manually instead — direct
  line-by-line comparison against `google_text_1920/page_0620.txt`
  found no letter-level discrepancies, only expected Google-OCR
  artifacts (dropped superscript letters, one word-fusion "sobrelos
  hombros" for "sobre los hombros"). No `permitted words.txt`
  additions needed: a fresh full pptext report
  (`workspace/report_wsl_20260824.html`) was regenerated, and its
  Spellcheck Suspect Words section has zero hits from this page's
  vocabulary (checked directly), so entries like "aquéllos,"
  "rehusare," "quienquiera," "sobrellevar," "subyugar," and
  "coronándose" are already accepted or unflagged — an addition would
  be a no-op per the "Jesu Cristo" precedent. Whole-document sweeps
  (spaced punctuation, footnote punctuation, verse indent, the
  footnote-anchor/Block-2-definition cross-check, a footnote-number
  duplicate/out-of-range/missing sweep [max anchor now 4437],
  curly-quote scan) all re-ran clean, only the already-documented
  Jacob 2:15/812 gap remaining. This page's body/footnote text has no
  letter-hyphen-letter compound words and no mixed-case-within-word
  tokens (checked directly). `generate_block2.py`'s own "unresolved
  cross-reference" flag on footnote 4436 ("Véase 814 y 815 y 820") was
  confirmed a false positive — its regex catches any bare letter in the
  resolved text, and "y" (Spanish "and") triggered it even though all
  three targets (814, 815, 820) resolved correctly to Jacob 2's own
  k/l/q footnotes, verified against `librodm_foot.txt` directly.
- **2026-08-24**: Sessions A–E run for page 599 (Éther 10:10-21),
  footnotes 4438-4445, chapter 10's letters d-k. No chapter heading on
  this page — it continues verse 10 immediately after "Página 599"
  with no blank line, per rule 1's mid-chapter new-verse convention.
  The mandatory 1879 check (this typeface's swash "i" and "j" are
  drawn almost identically, so the check was extended past the literal
  i/l/1 set per rule 8's discretion) resolved two glyphs misread from
  the 1920 image alone: footnote e's cross-reference target letter
  (first read as "i") is actually "j," and footnote i's own definition
  ("Éther 9:32") does carry a printed letter after all, not a stray
  mark — checked against pages_1879/page_0601.png and page_0602.png
  (printed pages 593-594), independently re-confirmed in Session B via
  fresh crops. Content-fit cross-checked cleanly against chapter 9's
  own footnotes (9j/9k/9r already cite forward to this exact page's
  gold/flocks/serpents content). The Google cross-check (Session A
  step 10) caught two genuine transcription errors missed on first
  read: v.11 "misno" (not "mismo" — a single-hump "n," not "m," per
  20x zoom) and v.16 "quién" (accented in print, matching v.14's usage
  on the same page). It also flagged an isolated margin dot after
  v.12's short line, investigated and concluded to be press debris
  (solid ink, but floating with no adjacent letter/word — not
  transcribed, not logged as an error). Two suspected 1920-only
  misprints — v.11 "misno" (mismo) and v.19 "czador" (cazador) — were
  fully researched in Session E (1886 comparison, RAE DLE, reference
  corpora, modern edition) and added to `errors in 1920.txt`; "misno"
  (pptext-flagged) also went into `permitted words.txt`, "czador"
  (unflagged by pptext) did not, per the "Jesu Cristo" no-op
  precedent. v.12 "que se" (printed with a reduced-but-real gap)
  defaulted to two words per the 2026-07-22 convention and was
  independently confirmed by 1886, which prints it as two ordinary
  words. Whole-document sweeps (spaced punctuation, footnote
  punctuation, verse indent, the footnote-anchor/Block-2-definition
  cross-check, a footnote-number duplicate/out-of-range/missing sweep
  [max anchor now 4445], curly-quote scan) all re-ran clean, only the
  already-documented Jacob 2:15/812 gap remaining. This page's
  body/footnote text has no letter-hyphen-letter compound words and no
  mixed-case-within-word tokens (checked directly via script).
- **2026-08-25**: Sessions A–E run for page 600 (Éther 10:22-34), footnotes 4446-4451, chapter 10's letters l-q (chapter's last page — chapter 11 begins on page 601). No chapter heading on this page — it continues verse 22 immediately after "Página 600" with no blank line, per rule 1's mid-chapter new-verse convention. The mandatory 1879 check resolved one glyph misread from the 1920 image alone: footnote l's cross-reference target letter (first read as "i") is actually "j" — the same swash i/j confusion documented on page 599 — confirmed via fresh crops of pages_1879/page_0602.png (printed page 594: "l, see j, Ether 9.") in both Session A and an independent Session B re-check. Footnote q's target letter "i" (Véase i, II Nefi 10) has no 1879 entry anchored to the same word ("oaths"/"juramentos") — 1879 instead anchors the identical citation content to a different word two verses later ("wicked combinations," letter d) — resolved via rule 26 (match by target content, not letter/position), independently confirming "i" is correct. A stray mark between "clase" and "de" in v.27 was checked against Google OCR first per rule 36 (silent) and not transcribed. Three suspected 1920-only/shared misprints were fully researched in Session E (1886 comparison, RAE DLE, reference corpora, modern edition): v.22 "obrener" (obtener, 1920-only, already in `permitted words.txt` from an earlier page), v.28 "póspero" (próspero, shared with 1886 but RAE/corpora/modern edition confirm it's still an error — not added to `permitted words.txt` since the actual pptext report doesn't flag it in-document despite standalone aspell flagging it, matching the known page 469-470 gap), and v.32 "espació" (espacio, 1920-only — a real conjugated verb form of "espaciar" so aspell never flags it either, matching the "czador" no-op precedent); all three added to `errors in 1920.txt`. "Amgid" (proper noun, pptext-flagged) added to `permitted words.txt`; "Hearthom" was not (not flagged by the actual pptext report, same gap pattern). A full pptext report was regenerated and walked end to end, filtering every section for page 600's line range specifically — only the "Amgid" spellcheck flag was new; short-lines-check hits all matched the established page/verse-boundary false-positive pattern; no dash, footnote-check, repeated-word, hyphenation, special-situations, or paragraph-level findings touched this page. Whole-document sweeps (spaced punctuation, footnote punctuation, verse indent, the footnote-anchor/Block-2-definition cross-check, a footnote-number duplicate/out-of-range/missing sweep [max anchor now 4451], curly-quote scan) all re-ran clean, only the already-documented Jacob 2:15/812 gap remaining. This page's body/footnote text has no letter-hyphen-letter compound words and no mixed-case-within-word tokens (checked directly via script). No narrow-space-vs-merge defaults were needed on this page.
- **2026-08-26**: Sessions A–E run for page 601 (Éther 11:1-11), footnotes 4452-4456, chapter 11's letters a-e. Page opens with a chapter heading: blank line after "Página 601", then "CAPÍTULO 11.", per rule 1 — no subtitle (1879 chapter 11 has none either). One line-break hyphen rejoined (v.7 "pesti-"/"lencias" → "pestilencias", 65 chars, kept). Mandatory 1879 check (pages_1879/page_0603.png, printed page 595) for footnote d's cross-reference target "i" (Véase i, II Nefi 10): 1879 reads "d, see i, ii. Nep. 10." — a short dotted letter, not "l"/"1"; also confirms footnote a's target "p" (Véase p, Éther 9). Both re-confirmed by an independent Session B process_page.py look. Block 2: 4452 resolved to 4430 (Éther 9p, whose own text cites "Éther 11:1" — a clean cross-check of marker a's placement); 4455 resolved to 398 (II Nefi 10i, same as page 600's 4451). Three stray marks handled per rule 36 (Google OCR silent, then weight-comparison zoom): a fleck before "y" in v.1, a fleck after "profetizaron" in v.1 (a period/comma there is also grammatically out of place), and a grave-accent-like speck over the first "i" of "vivió" in v.4 (plus a descending ink squiggle from that line's "Y" that is scan smudge) — none transcribed, no errors-log entries. Session E's full 1886 comparison (pages_1886/page_0615.png, printed page 597) of all 11 verses found no 1920-only substantive deviation: 1886 has none of the three stray marks, and prints a comma after "hacian" in v.8 matching 1920's "hacían," — so no permitted-words or errors-in-1920 additions. Fresh full pptext report (workspace/report_wsl_20260826.html) regenerated and walked end to end — page-601 hits are only short-lines-check verse-boundary / short-Block-2-entry false positives plus one "standalone 1" false positive for "4456: Éther 1:11"; no spellcheck, edit-distance, dash, footnote-check, repeated-word, special-situations, or paragraph-level findings touch this page. Whole-document sweeps (spaced punctuation, footnote punctuation, verse indent, footnote-anchor/Block-2 cross-check, footnote-number duplicate/out-of-range/missing sweep [max anchor now 4456], curly-quote scan) all re-ran clean, only the already-documented Jacob 2:15/812 gap remaining. No narrow-space-vs-merge notes on this page.
- **2026-08-26**: Sessions A–E run for page 602 (Éther 11:12-23, then CAPÍTULO 12 opens mid-page, then 12:1-2), footnotes 4457-4461, chapter 11's letters f-j. Page starts mid-chapter (continuation of Éther 11 from page 601) — no blank line after "Página 602" per rule 1. Chapter 12 opens after v.23 (centered rule, then "CAPÍTULO 12.", blank line, verse 1); no subtitle in 1920, and 1879 file-page-604 "CHAPTER 12." and 1886 file-page-616 "CAPÍTULO 12." both have none either. Three line-break hyphens rejoined per rule 7: v.15 "organi-"/"zada" → "organizada" (71 chars, kept at line end, "para" starts next line); v.20 "arre-"/"pentimiento" → "arrepentimiento" (70, kept); v.20 "destruc-"/"ción" → "destrucción" with the following ";" attached (68, kept) — the fragment-only image line "ción ;" is absorbed, which (plus the mid-page CAPÍTULO 12 break) explains check_line_wrap's txt-34-vs-OCR-38 body-line flag. Rule 31: spaces removed before every ";" on the page ("pueblo ;", "palabras ;", "días ;", "ganancias ;", "reino ;", "ción ;", "país ;", "Señor ;") plus footnote "Jerusalem ;" and spaced colon "Éther 13 : 20, 21". Mandatory i/l/1 check (Section 8): footnote targets "p" (Éther 9) in 11f/11h and "i" (II Nefi 10) in 11g/11j, plus the 11i chapter letter — 1879 file page 604 footnote block reads "e, see p, Ether 9.  f, see i, ii. Nep. 10.  g, see p, Ether 9.  h, A small colony from Jerusalem.  Ether 13:20, 21.  i, see i, ii. Nep. 10." (1879's chapter-11 lettering runs one letter behind 1920's, since 1920 has an extra chapter-11 footnote on page 601). Matched by target content per rule 26: 1879 e/g = 1920 11f/11h, 1879 f/i = 1920 11g/11j, 1879 h = 1920 11i. Every "i" is a short dotted glyph in both editions, not "l"/"1"; re-confirmed by an independent Session B high-zoom re-read of both the 1920 fn_zoom and the 1879 block. Block 2: 4457/4459 resolved to 4430 (Éther 9p — whose own text cites "Éther 7:23; 11:1,12,20", a clean cross-check of markers f/h at v.12/v.20); 4458/4461 resolved to 398 (II Nefi 10i, same target as page 601's 4455 and page 600's 4451); 4460 is 1920-only ("Una pequeña colonia de Jerusalem; Éther 13:20-21."). check_google_crosscheck flagged only the acute on "Éthem" (mine "É" vs Google "E") in v.12 and v.14 — Google drops capital-letter accents; high-zoom confirms the acute, and page 601 v.11 already established "Éthem" with the accent (1886 also prints "Éthem" accented). Session E full 1886 comparison (pages_1886/page_0616.png, printed page 598): no 1920-only substantive deviation; 1886 prints v.13 "se endurecía en", v.15 "se levantó", v.18 "venció á" with normal word spacing, confirming the two-word transcriptions (narrow-space-vs-merge notes surfaced for the editor: Éther 11:13 "endurecía"/"en", 11:15 "se"/"levantó", 11:18 "venció"/"á" — all committed as two words). One genuine 1920 error logged: Éther 11:14 "sucedio" (sucedió) — missing preterite accent in "y engendró á Morón, y sucedio, que Morón reinó", confirmed at zoom and by Google OCR; 1886 shares the unaccented "sucedio" at the exact spot (inherited-error pattern, same as Éther 9:30 "rapidamente" / 9:22 "glorifició" / "seperado"), but RAE requires the accent, the rest of the document accents it (including v.12 and v.14's own opening), and the modern Spanish edition uses "sucedió"; pptext flags it as a Spellcheck Suspect Word. Added to `permitted words.txt` and `errors in 1920.txt`; text preserved as printed. Fresh full pptext report (workspace/report_wsl_20260826b.html) regenerated and walked end to end — the only page-602 findings are "sucedio" (spellcheck/edit-distance, now logged), short-lines-check verse-boundary / short-Block-2-entry false positives, and the dash-check hyphen-minus entry "4460: ... Éther 13:20-21" (legitimate verse range); no repeated-word, duplicate-line, ellipsis, scanno, curly-quote, special-situations, book-level, or paragraph-level findings touch this page. Whole-document sweeps (spaced punctuation, footnote punctuation, verse indent, footnote-anchor/Block-2 cross-check, footnote-number duplicate/out-of-range/missing sweep [max anchor now 4461], curly-quote scan) all re-ran clean, only the already-documented Jacob 2:15/812 gap remaining. Process note: the user asked for "Sessions A through E" to run in one session without stopping between steps — CLAUDE.md's "Review Pass — One Step Per Session" now carries an explicit exception for an explicit multi-session range request.
- **2026-08-26**: Sessions A–E run for page 603 (Éther 12:2 continuation, then 12:3-14), footnotes 4462-4467, chapter 12's letters a-f (the first page carrying chapter-12 Block 1 entries — chapter 12 opened mid-page on 602). Page begins mid-verse (12:2, continuing "Éther vino en" from page 602) — first body line follows "Página 603" with no blank line per rule 1; no page-boundary hyphen split. Two line-break hyphens rejoined per rule 7: v.4 "inque-"/"brantables," → "inquebrantables," (comma travels with the second half, 72 chars, kept at line end); v.5 "mara-"/"villosas" → "maravillosas" (66, kept). Rule 31: spaces removed before every ";" on the page (13 instances: "él ;", "cosas ;", "mejor ;", "Dios ;" ×2, "ve ;", "prueba ;", "muertos ;", "Él ;", "visto ;", "excelente ;", "fe ;", "ellos ;") plus footnote spaced colons ("Éther 11 : 12", "Moroni 7 : 40-44", "8 : 26", "10 : 20-22", "Helamán 5 : 20-52", "III Nefi 9 : 20"). Cross-reference-letter check (no i/l/1 in chapter 12's own lettering or its "g"/"d" cross-ref targets, so the mandatory check does not trigger; done anyway for the swash letter): 12c's cross-ref reads ambiguously v/o/g at low zoom — extreme zoom shows a looped descender (g), and 1879 file page 605 (Éther 12 footnote block) confirms it: "c, see g, Mos. 26." 1920 letters a-f line up one-for-one with 1879 a-f; 1920's g (Alma 17-29) falls on page 604. Block 1 formatting: 12b "Versículos 6, 8, 9, 32" → "6,8-9,32" (8-9 range per rule 23; 6/32 non-consecutive per rule 24), and "Moroni 7:40-44. 8:26. 10:20-22" (periods in the original) joined with semicolons per rule 21; 12e "Alma 14; 26-29" → "Alma 14:26-29" (1879 "e, Alma 14:26—29" confirms a single citation). Block 2: 4464 → 1520 (Mosíah 26g), 4465 → 3744 (III Nefi 17d, whose own text cites back to "Ether 12:12" — a clean cross-check of marker d at v.12). check_google_crosscheck: 0 candidates. v.6 has a printed comma after "no" ("por tanto, no, disputéis") — Google OCR reads it as a comma too, and a weight-comparison zoom matches a genuine comma (not scan debris); Session E's 1886 comparison (pages_1886/page_0617.png, printed page 595) shows 1886 prints "por tanto, no disputeis sobre las cosas que no veis" with NO comma, and the modern edition ("no contendáis porque no veis") has none either — a 1920-only spurious comma, logged in `errors in 1920.txt` (Éther 12:6), text kept as printed; same error class as the "punto seguido de secuencia inesperada" cases (Alma 43:9 etc.). v.14 "Nefl" is the bold-face "fi" ligature reading as "fl" at a glance (same phenomenon documented on page 461) — read as "Nefi" per rule 29; 1886 and the modern edition both print a clean "Nefi", so it is a ligature/scan-rendering artifact, not a 1920 error (no errors-log entry, matching page 461). One wording variant noted for the editor but NOT an error: v.6 1920 "no recibís el testimonio hasta cuando vuestra fe ha sido puesta á prueba" vs 1886 "no recibís el testimonio más que cuando..." — a translation-lineage difference; the modern edition also uses "hasta", so 1920's rendering stands as printed. Narrow-space-vs-merge flags for the editor (committed as two words, 1886 + grammar agree, no decision pending): Éther 12:10 "por"/"medio" (1886 "por medio de la fé"), 12:14 "que"/"la" (1886 "que la fé de Nefi"). Full pptext report (workspace/report_wsl_20260826c.html) regenerated and walked end to end — the only page-603 findings are short-lines-check verse-boundary / short-Block-2-entry false positives and three dash-check hyphen-minus entries (4463 "6,8-9,32 … 7:40-44 … 10:20-22", 4466 "Alma 14:26-29", 4467 "Helamán 5:20-52", all legitimate digit-flanked verse ranges); "Versículos" (accented, in 12b) is NOT flagged by aspell so needs no permitted-words entry; "disputéis" not flagged; no spellcheck/edit-distance/repeated-word/duplicate-line/ellipsis/scanno/curly-quote/special-situations/book-level/paragraph-level finding touches this page, and "full stop followed by unexpected sequence" has no page-603 hit. Whole-document sweeps (spaced punctuation, footnote punctuation, verse indent, footnote-anchor/Block-2 cross-check [max anchor now 4467, all defined, no dupes], curly-quote scan of both master files) all re-ran clean, only the already-documented Jacob 2:15/812 gap remaining. `permitted words.txt`: no additions. `errors in 1920.txt`: one addition (Éther 12:6 spurious comma).
- **2026-08-27**: Sessions A–E run for page 604 (Éther 12:14 continuation, then 12:15-24), footnotes 4468-4478, chapter 12's letters g-q. Page begins mid-verse (12:14, continuing "...fué la que [4467]hizo que" from page 603) — first body line follows "Página 604" with no blank line per rule 1; no page-boundary hyphen split. No end-of-line hyphenated word splits anywhere on the page (rule 7 — nothing to rejoin; 42 raw image lines = 42 output lines). Rule 31: the 1920 print sets a space before punctuation throughout — normalized at v.15 "Lamanitas :", v.17 "muerte ; no", v.18 "fe ; por", v.19 "fe ; en", v.20 "dado ; palabra", v.21 "fe ; el Señor" and "vista ; por", v.22 "Gentiles ; por" and "mandado ; sí", v.23 "dije : Señor" and "escritos ;porque" (space before, none after — both fixed) and "dado ;"; rule 6 double sentence-spacing normalized at v.23 "escritura.  Porque" and v.24 "manos.  He aquí". Mandatory i/l/1 check (Section 8): body markers i (v.19, on "dentro"/"within the vail") and l (v.21, on "no"/"the Lord could not withhold") — both confirmed against 1879 file page 606 body text, which sets a superscript "i" and "l" at the same spots in the same gapless run g-q; the 1920 "l" glyph is a clean dotless vertical stroke at high zoom. All eleven [N] markers (g-q) placement-checked against 1879 file page 606. Block 1 cross-reference target letters resolved from 1879's clean type on file page 606 (the 1920 swash target glyphs — j's "e", n's "c", o's "w" especially — are genuinely hard to read by shape, Section 8 swash case): 12h Véase d, III Nefi 28 / 12i Véase f, Éther 3 / 12j Véase e, Éther 3 / 12m Véase f Éther 3 (1920 omits the comma after the target letter, kept as printed per the "Véase d Mosíah 4."-style precedent already in librodm_foot.txt) / 12n Véase c, Enos 1 / 12o Véase w, Mormón 8 (Google OCR also reads "w"; 1920 glyph is a heavily-inked blob). All matched by target content per rule 26. 12g: 1920 prints "Alma 17:29-39" (Google OCR agrees) where 1879's g reads "Alma 17—29" (a chapter range) — a genuine edition difference, transcribed as 1920 prints it. Block 2: 4469 → 3983 (III Nefi 28d), 4470 → 4312 (Éther 3f), 4471 → 4311 (Éther 3e), 4474 → 4312 (same target as 4470 — resolved by hand since the missing comma in "Véase f Éther 3" blocks generate_block2.py's regex), 4475 → 975 (Enos 1c), 4476 → 4205 (Mormón 8w). Éther 3e/3f (4311/4312) and Mormón 8w (4205) all cite forward to "Éther 12:19-21"/"Éther 12:19,21"/"Ether 12:22-28,35" — clean mutual cross-checks of markers i/j/m/o. check_google_crosscheck: 0 candidates. Footnote p "Egípcios" first-pass misread corrected to "Egipcios" (plain "i", no accent — Google OCR agrees; consistent with existing document usage at Éther 3:27 and 1 Nefi 1:2); footnote q's low mark between "fué" and "más" (Google reads "fué,más") is inter-row descender bleed-through, not a comma — transcribed "fué más" per rule 36. One genuine 1920-only error logged: Éther 12:21 "harmano" (hermano) — "a" for "e" in the first syllable of "el harmano de Jared"; the same verse prints "hermano" correctly at v.20 and again later in v.21; Google OCR corroborates "harmano"; RAE DLE has no entry for "harmano"; the clean reference corpora have zero "harmano" (one OCR-noise hit in the scanned full Reina-Valera) vs hundreds of "hermano"; 1886 (pages_1886/page_0618.png, printed page 600) prints "el hermano de Jared"; the modern edition (Éter 12:21) uses "hermano" twice; pptext flags it in both Spellcheck Suspect Words and Edit Distance ("harmano(1):hermano(1)"). Added to `permitted words.txt` and `errors in 1920.txt`; text preserved as printed. Not errors: footnote p "carácteres" (archaic accented plural — already in `permitted words.txt`, also used at footnote 1483); footnote p "Egipcios" (capitalised, unaccented — house style); v.22 "Jesu Cristo" unhyphenated vs 1886 "Jesu-Cristo" (legitimate archaic form, feedback_jesu_cristo_hyphen). Narrow-space-vs-merge flag for the editor (committed as two words, 1886 + Google + grammar agree, no decision pending): Éther 12:23 "debilidad"/"de" (1886 "la debilidad de nuestra escritura", normal spacing). Fresh full pptext report (workspace/report_wsl_20260827.html) regenerated and walked end to end — the only page-604 findings are "harmano" (now logged), short-lines-check verse-boundary / short-Block-2-entry false positives, and three dash-check hyphen-minus entries (4468 "Alma 17:29-39", 4476 "Versículos 26-28", 4478 "Éther 3:22-24", all legitimate digit-flanked verse ranges); no repeated-word, duplicate-line, ellipsis, scanno, curly-quote, special-situations, book-level, or paragraph-level finding touches this page, and "full stop followed by unexpected sequence" has no page-604 hit. Smart Quote Scan, Jeebies, book level checks all clean. Whole-document sweeps (spaced punctuation, footnote punctuation, verse indent, footnote-anchor/Block-2 cross-check [max anchor now 4478, all defined, no dupes], curly-quote scan of both master files) all re-ran clean, only the already-documented Jacob 2:15/812 gap remaining. Also this session: emailed III Nefi Capítulo 16 to the family recipients (chapters_emailed/III_Nefi_16.txt, logged). `permitted words.txt`: one addition ("harmano"). `errors in 1920.txt`: one addition (Éther 12:21 harmano).
- **2026-08-27b**: Sessions A–E run in one session for page 605 (Éther
  12:25-35, continuation from page 604), footnotes 4479-4484, chapter
  12's letters r-w. Page opens on verse 25 (not mid-verse, not a
  chapter heading) — first body line follows "Página 605" with no blank
  line per rule 1 / the page 599/600/602 precedent. 43 raw image lines
  = 43 output lines; two rule-7 hyphen rejoins, both fitting on their
  first line so no cascade: v.31 "dis-"/"cípulos." → "discípulos." (66
  chars), v.34 "pre-"/"parado" → "preparado" (70). Rule 31: space
  before punctuation removed throughout (v.25 "escribir ; por" /
  "debilidad ; y" / "palabras ; y", v.26 "Señor :" / "lamentarán ; y" /
  "debilidad ;", v.27 "humillaren ; y", v.29 "dije : Oh" / "voluntad ;"
  / "su fe ;", v.30 "Zerín :" / "Remuévate ; y" / "removido ; por" /
  "la fe ;", v.31 "poder ;", v.32 "hombre ; sí" / "esperanza ;", v.34
  "caridad ; por", footnote r "idea ; mientras"); v.29 "hombres;
  según" was already tight in the print. Rule 6: wide sentence gaps
  normalized at v.30 "removió.  Y" and v.31 "cípulos.  Porque". Six [N]
  markers (r-w) all placement-checked against 1879 file pages 606-607
  body text, matched by content per rule 26: podamos (v.25), burlen
  (v.25), removió (v.30), mansión (v.32), esperanza (v.32), caridad
  (v.34). Mandatory i/l/1 check not triggered — no page letter (r-w)
  and no cross-ref target (t→c, u→m, v→b) is i/l/1; targets c/m/b
  confirmed against 1879 file page 607's clean type anyway ("t, see c,
  Jacob 4." / "u, vers. 33, 34, 37. See m, Enos 1." / "v, see b.").
  12v "Véase b." is a bare back-reference to letter b of the same
  chapter (Éther 12), no book/chapter — kept exactly as printed (1879
  also "v, see b."). Block 1 verse-range reformatting per rules 23-24:
  12s "Versículos 23, 27." → "23,27"; 12u "Versículos 33, 34, 37" →
  "33-34,37" + "; Véase m, Enos 1."; 12w "35-37." kept. Block 2
  cross-refs resolved: 4481 → 842 (Jacob 4c), 4482 → 985 (Enos 1m,
  which cites "Éther 12:32-34" — mutual check of marker u), 4483 →
  4463 (Éther 12b, the faith-hope-charity passage citing v.32 — mutual
  check of marker v). Rule 36 — two small low specks in v.32 dropped
  as stray marks: one between "el" and "hombre" (Google OCR did read a
  comma here, but a weight/size zoom shows it lighter/smaller than the
  real "sí," comma on the same line; 1879 has plain "a house for man"),
  one between "excelente" and the [4483] marker (Google OCR silent);
  both grammatically impossible as punctuation, transcribed without
  them, flagged for the editor. check_google_crosscheck: 2 candidates,
  both benign — "sufficiente" (Google drops the ffi-ligature "i") and
  "mí—fuente" (Google drops the em dash; 1879 confirms "me—the
  fountain"). Session E — 1886 comparison of Éther 12:25-35
  (pages_1886/page_0619.png, printed page 601): two 1920-only errors
  confirmed and logged. (1) Éther 12:26 "en sufficiente" — 1886 and
  the modern edition both read "es suficiente"; 1920 deviates twice at
  once: "en" for the copula "es" (zoom + Google confirm "en", e-n) and
  "sufficiente" double-f for "suficiente" (RAE has no "sufficiente";
  0 corpus hits vs 7+; modern single-f). (2) Éther 12:25 footnote r
  "símbalos" — 1879 Pratt footnote r reads "symbols and hieroglyphics"
  → "símbolos"; "símbalos" (a for o) is not valid Spanish (RAE: only
  "símbolo"), 0 corpus hits; 1886 has no footnotes. Both flagged by
  pptext (Spellcheck Suspect Words + Edit Distance,
  "sufficiente(1):suficiente(9)" / "símbalos(1):símbolos(1)",
  report_wsl_20260827b.html). Both preserved as printed per rule 32,
  added to permitted words.txt and errors in 1920.txt. Not errors:
  v.27 "dí" (archaic accented preterite, already permitted; 1886 also
  "Yo les dí"); v.28 "mí—fuente" em dash (1886 file page 619 also
  "atraen á mí—fuente de toda rectitud"). No narrow-space-vs-merge
  flags this page. Fresh pptext report walked end to end — only
  page-605 findings are the two spellcheck/edit-distance words (logged),
  short-lines-check verse-boundary / short-Block-2-entry false
  positives, and dash-check entries 4482 "Versículos 33-34,37" / 4484
  "Versículos 35-37" (legitimate digit-flanked verse ranges); no
  repeated-word, duplicate-line, ellipsis, scanno, curly-quote,
  smart-quote, special-situations, book-level, paragraph-level, "full
  stop followed by unexpected sequence", or Jeebies finding touches
  this page. Whole-document sweeps all re-ran clean
  (check_spaced_punctuation, check_footnote_punctuation,
  check_verse_indent, footnote-anchor/Block-2 cross-check [max anchor
  now 4484 = max def, no dupes, no anchored-without-def; only the
  documented Jacob 2:15/812 defined-without-anchor gap remains],
  curly-quote character scan of both master files). `permitted
  words.txt`: two additions ("sufficiente", "símbalos"). `errors in
  1920.txt`: two additions (Éther 12:25 nota r símbalos; Éther 12:26
  "en sufficiente").
- **2026-08-27c**: Sessions A–E run in one session for page 606
  (Éther 12:35-41, then chapter 13 opens mid-page with vv.1-4),
  footnotes 4485-4491. Page begins mid-verse 35 (continues from foot
  of page 605) — first body line follows "Página 606" with no blank
  line per rule 1. 38 raw body lines (Éther 12: 25, Éther 13: 13) plus
  the "CAPÍTULO 13." heading; one rule-7 rejoin, v.39 "relativa-"/
  "mente" → "relativamente" (67 chars, fits first line, no cascade).
  check_line_wrap flagged a 25-vs-38 body-line gap — false positive:
  the script stops counting at the blank line before "CAPÍTULO 13."
  and sees only the 25 Éther-12 lines, while its OCR estimate (38)
  matches the true full-page total. Rule 31: space before punctuation
  removed throughout (v.37 "me dijo :", "importa ;", "fiel ;"; v.38
  "sangre ;"; v.39 "cara ;", "cosas ;"; Éther 13:2 "Éther ;",
  "hombre ;", "Señor ;", "sirvan ;"; Block 1 13b "10 ;", "3 : 12",
  "21 : 2"). Rule 6: wide sentence gaps normalized at v.37
  "limpiados.  Y" and v.41 "jamás.  Amén.". Footnote letters: Éther
  12 continues x, y, z, 2a (4485-4488) after page 605's w; Éther 13
  restarts at a, b, c (4489-4491) — same-book chapter boundary, no
  blank line / book header in Block 1 (rule 20). The four Éther-12
  superscripts are heavy swash italics (look like z/v/s/2a) —
  resolved x/y/z/2a by alphabetical continuation + body order +
  content-fit + an exact entry-for-entry match against 1879 file
  page 608's clean type ("x, vers. 26--28, 35, 40." / "y, see u." /
  "z, see e, Ether 1." / "2a, iii. Nep. 11 : 32, 36." / "a, see t,
  iii. Nep. 20." / "b, ver. 10. Rev. 3 : 12. 21 : 2." / "c, see t,
  iii. Nep. 20."). All seven [N] markers placement-checked against
  1879 file page 608 by content (rule 26): visto (v.37), mansiones
  (v.37), poco (v.40), testimonio (v.41), lugar (13:3), descendiere
  (13:3), Nueva (13:4). Mandatory i/l/1 check not triggered (no page
  letter x/y/z/2a/a/b/c and no cross-ref target u/e/t/t is i/l/1);
  the ambiguous-looking swash "t" of 13a/13c was cross-checked
  against 1879 anyway ("see t" both). Block 1 formatting: 12x
  "Versículos 26-28, 35, 40." → "26-28,35,40" (rules 23-24); 12-2a
  joins chapter + two-letter code with a hyphen (rule 16); 12-2a
  "III Nefi 11:32, 36." → "11:32,36"; 13b keeps the two Revelation
  refs joined by the semicolon as 1920 prints ("Revelaciones 3:12;
  21:2") — "Revelaciones" is the established 1920 name for Revelation
  (20+ prior instances in librodm_foot.txt). Block 2 cross-refs: 4486
  (12y "Véase u") → 4482 (12u, the Éther 12:32 mansion footnote);
  4487 (12z "Véase e, Éther 1") → 4277 (Éther 1e); 4489/4491
  (13a/13c "Véase t, III Nefi 20") → 3822 (III Nefi 20t, which itself
  cites "Éther 13:1-12" — mutual cross-check). Rule 36 — stray dash
  after "abundantemente." (v.35) dropped as a speck: Google OCR
  silent, 1886 file page 619 has plain "abundantemente.", zoom shows
  it thin/light/off-baseline; flagged for the editor.
  check_google_crosscheck: 0 candidates (the "quela" /
  "desecharontodas laspalabras" fusions never reach the diff;
  dropped superscript letters at marker positions auto-dismissed).
  Default-to-two-words (rule 6 editor guidance, surfaced for the
  editor): Éther 13:2 "desecharon todas las palabras" and v.41 "que
  la gracia" both printed tight in 1920 but set as separate words in
  1886 (file page 620) — transcribed as separate words. "Jesu
  Cristo" (v.41) kept unhyphenated (1886 hyphenates "Jesu-Cristo"
  but the bare form is legitimate throughout this edition,
  feedback_jesu_cristo_hyphen). Session E — 1886 comparison of Éther
  12:35-41 / 13:1-4 (pages_1886/page_0619-0620): one 1920-only error
  confirmed and logged. Éther 12:38 "en él que" (en el que) — 1920
  accents the personal pronoun "él" where the relative "el que"
  ("wherein", referring to "el tribunal de Cristo") is required;
  1886 file page 620 has "en el que todos los hombres sabrán", 1879
  file page 608 "where all men shall know"; a high-zoom crop shows
  the acute accent unmistakably (matches "quiénes"/"á" on the
  adjacent lines), Google OCR also reads "él"; same error class as
  the documented Mormón 6:21 "en él que" entry. Preserved as printed
  per rule 32; not flagged by pptext ("él"/"que" both valid) so no
  permitted words.txt entry, matching the Mormón 6:21 precedent. Not
  errors: 1920's added commas after "sucedió,"/"ocurrió,"/"ahora,",
  the reverential capital "Quién" and accented relative "quiénes"
  (consistent house style). Fresh pptext report
  (workspace/report_wsl_20260827c.html) walked end to end — zero
  page-606 findings in Spellcheck Suspect Words or Edit Distance (all
  13 spellcheck flags are on pages ≤605); short-lines-check flags
  only verse-end lines; dash-check "4485: Versículos 26-28,35,40" is
  a legitimate digit-flanked range; no repeated-word, duplicate-line,
  ellipsis, scanno, curly-quote, smart-quote, special-situations,
  book-level, paragraph-level, "full stop followed by unexpected
  sequence", or Jeebies finding touches this page (the paragraph-
  level "CAPÍTULO 13. (Véase Isaías 3.)" hit is II Nefi/Isaiah
  ch.13, not Éther 13). Whole-document sweeps all re-ran clean
  (check_spaced_punctuation, check_footnote_punctuation,
  check_verse_indent, footnote-anchor/Block-2 cross-check [max anchor
  now 4491 = max def, no dupes, no anchored-without-def; only the
  documented Jacob 2:15/812 defined-without-anchor gap remains],
  curly-quote character scan of both master files). `permitted
  words.txt`: no additions. `errors in 1920.txt`: one addition
  (Éther 12:38 "en él que").
- **2026-08-28**: Sessions A–E run in one session for page 607
  (Éther 13:5-14, a mid-chapter continuation — Éther 13 continues
  from page 606's 13a-13c), footnotes 4492-4505. Page opens on a
  fresh verse (13:5), not a chapter heading and not mid-verse, so the
  first body line follows "Página 607" with no blank line (rule 1,
  matches page 605). 43 raw body lines, no hyphenated line-break
  splits (rule 7 not triggered). Rule 31: space before punctuation
  removed throughout (body vv.5-13 and Block 1 13e/13g/13j/13o/13q).
  Rule 6: several justification-widened inter-word gaps normalized
  (v.11 "participan  del", "también  la antigua"; v.12 "dice :
  [o]Los"). Rule 36: a small raised speck between "de" and "José" in
  v.8 dropped — Google OCR (google_text_1920/page_0629.txt), 1879
  file page 609, and 1886 file page 621 all print the spot plain;
  flagged for the editor. Footnote letters: Éther 13 continues d-q
  after page 606's c; same-book same-chapter, no blank line / book
  header in Block 1 (rule 20). MANDATORY i/l/1 check TRIGGERED — the
  chapter's own sequence includes "i" (13i) and "l" (13l); both
  cross-checked against 1879 file page 609's clean type ("i, see t,
  iii. Nep. 20." / "l, see x, iii. Nep. 16.") regardless of the 1920
  reading looking settled. All 14 Block 1 entries match 1879 file
  page 609 entry-for-entry; all 14 body [N] markers placement-checked
  by content against 1879 (rule 26). 13l cross-reference target
  resolved as "x", NOT "z": the 1920 swash superscript is heavily
  degraded (low-res fn_zoom first suggested "z"), but a tight
  high-zoom crop shows a compact angular x-shape matching page 606's
  confirmed swash "x", 1879 prints clean "x", and content settles it
  — III Nefi 16x = "II Nefi 10:18-19; III Nefi 21:22-25; 30", and
  2 Nefi 10:18-19 is exactly about others being "numbered among the
  house of Israel", matching Éther 13:10 "contados entre el resto de
  la posteridad de José, que son de la casa de Israel" (III Nefi 16z
  = "Véase o, III Nefi 15", the other-sheep passage, fits poorly).
  Session D independently corroborated by auto-resolving Block 2 4500
  -> 3737 (= the III Nefi 16x entry). "Éther" (v.13) kept with acute
  accent per established convention (Google OCR drops it, reading
  "Ether"); "fué" (v.13) archaic, kept. Session B: independent
  re-read of the fn_zoom and all 14 marker positions, i/l/1 check
  re-run against 1879 — no changes. Session C: body text inserted
  once (Página count 615 -> 616), 14 Block 1 entries appended
  (13d-13q, no blank line — rule 20). Session D: 14 Block 2 entries
  appended; cross-refs resolved 13f/13i -> 3822 (20t, mutual
  cross-check — 20t itself cites Éther 13:1-12), 13h -> 3707 (15o),
  13k -> 4490 (13b, same chapter), 13l -> 3737 (16x), 13m -> 4493
  (13e, same chapter). Session E — 1886 comparison of Éther 13:5-14
  (pages_1886/page_0620-0621): no 1920-only error. All 1920-vs-1886
  differences are non-errors — house-style accent additions
  ("también"/"después"/"según"/"aquéllos"/"entonces" vs 1886
  "tambien"/"despues"/"segun"/"aquellos"/archaic "entónces";
  "fueron"/"estimaron" vs archaic "fuéron"/"estimáron"), "José"
  (1920) vs "Joseph" (1886) naming convention, and v.13 "echándole
  fuera" (1920) vs "echándole afuera" (1886) — a minor lexical
  variant, both grammatical for "casting him out" (1879 "cast him
  out"), a wording choice between editions, not a defect. Fresh
  pptext report (workspace/report_wsl_20260828.html) walked end to
  end — ZERO page-607 findings in any section. Spellcheck Suspect
  Words (12 flags) and Edit Distance all fall on pages <=606 (max
  suspect line 26962; page 607 body starts at librodm.txt line
  27027). "Jerusalem"/"Lehi"/"fué"/"Éther" on this page are
  aspell-flaggable alone but pptext auto-accepts each (>=5 doc
  occurrences), so no permitted-words entry needed (matches page
  606). Short-lines check flags only verse-end / footnote-definition
  lines; dash-check hyphen-minus for page 607's Block 2 ("I Nefi
  1-18", "21:10-27", "3:5-24", "46:24-26") are all digit-flanked
  ranges; footnote check shows anchors 4491-4505 as one contiguous
  run, no dupes/gaps/out-of-range. No repeated-word, duplicate-line,
  ellipsis, scanno, curly-quote, smart-quote, special-situations,
  comma-spacing, book-level, paragraph-level ("full stop followed by
  unexpected sequence" — page 607 has no period+lowercase), or
  Jeebies finding touches this page. Whole-document sweeps all re-ran
  clean (check_spaced_punctuation, check_footnote_punctuation,
  check_verse_indent, footnote-anchor/Block-2 cross-check [max anchor
  now 4505 = max def 4505, no dupes, no anchored-without-def; only
  the documented Jacob 2:15/812 defined-without-anchor gap remains],
  curly-quote character scan of both master files). `permitted
  words.txt`: no additions. `errors in 1920.txt`: no additions.
- **2026-08-28b**: Sessions A–E run in one session for page 608
  (Éther 13:14 tail, then 13:15-25 — a mid-chapter continuation;
  Éther 13 continues from page 607's d-q with letters r-x), footnotes
  4506-4512. Page opens mid-verse (13:14, continuing "...concluyó el"
  from page 607) so the first body line follows "Página 608" with no
  blank line (rule 1). 42 raw image lines. Rule 7: three line-break
  hyphen rejoins — "destruc-"/"ciones" (v.14, rejoined
  "destrucciones"; +[4506] marker would push line 1 to 74 chars so
  rule 8 moves it to line 2 start), "pode-"/"rosos," (v.15 →
  "poderosos,", 67 chars, kept), "arrepin-"/"tieran" (v.17 →
  "arrepintieran", 71 chars, kept). Rule 31: space-before-";" removed
  throughout (body vv.17/21/22; Block 1 13r "15 : 33", 13w "15 :
  29-32"). Rule 6: v.15 justification-widened gaps ("hubieron
  muchos", "y eran hombres") normalized. MANDATORY i/l/1 check
  TRIGGERED: the cross-reference target in BOTH 13s and 13u is "i"
  ("Véase i, II Nefi 10"); cross-checked against 1879 file page 610's
  clean type ("s, see i, ii. Nep. 10." / "u, see i, ii. Nep. 10.") —
  dotted italic "i", not "l"/"1"; a tight high-zoom of the 1920
  swash superscripts (p608_row1.png) independently shows the dotted
  "i" in both. Session D corroborated: 4507 and 4509 both auto-resolve
  to 398 = II Nefi 10i, whose text is "II Nefi 9:9; 26:22; 27:27;
  Alma 37:21-32; Helamán ..." — the secret-combinations chain, an
  exact content fit for 13s ("secretos planes de iniquidad", v.15)
  and 13u ("secretas combinaciones", v.18). All 7 Block 1 entries
  match 1879 file pages 609-610 entry-for-entry (r on p609, s-x on
  p610); all 7 body [N] markers (r-x) placement-checked by content
  against 1879 (rule 26): r→"resto"/remainder v.14, s→"secretos"
  v.15, t→"cavidad" v.18 (1879 puts its t on v.15 "hath been spoken"
  — translation word-order artifact, 1920 has no marker there),
  u→"secretas" v.18, v→"otro" v.21, w→"perecería" v.21, x→"cavidad"
  v.22. Session B: 13w's book name is printed "Ether" WITHOUT the
  acute accent (contrast 13r "Éther" with a clear accent stroke on
  the same page — side-by-side crop p608_cmp.png); Block 1 entry
  corrected "Éther 15:29-32." → "Ether 15:29-32." per rule 32 (both
  forms already coexist in librodm_foot.txt, 132 vs 43). Session A
  Google cross-check (check_google_crosscheck) caught one accent
  misread: draft "profecías" (v.21) vs the printed "profecias" — a
  high-zoom crop confirmed the 1920 sets a plain "i" (next word
  "habían" shows the press's real í-accent for contrast); reverted to
  the printed "profecias". Rule 36: nine suspected stray specks/marks
  (verse-number "15:" speck, low mark after "sucedió" v.15 read at
  first as a comma, comma-like fleck after "no" v.17, speck between
  "en"/"el" v.18, floating dot after "mucho." v.19, tick over "fuere"
  v.20, speck after "modo" v.21, dot between "vez"/"en" v.22, tick
  over "por" v.25) — the v.15 and v.17 marks confirmed by the editor
  as scan/press debris on a direct look at the page (oversized head
  and tail vs. genuine period/comma), the rest all Google-silent → all
  transcribed without them, none logged. Kept as printed: "fué" (v.15,
  archaic); "Éther" (vv.18,22 — Google drops the É); archaic
  future-subjunctives "fuere/profetizare/arrepintiere/pudiere".
  Session E — 1886 comparison of Éther 13:14-25
  (pages_1886/page_0621.png book page 603 tail; page_0622.png book
  page 604). ONE genuine 1920-only error found and logged in `errors
  in 1920.txt` (also added to `permitted words.txt`): Éther 13:21
  "profecias" — dropped í-accent; flagged by pptext in BOTH Spellcheck
  Suspect Words and Edit Distance ("profecias(1):profecías(43)"); 1886
  accents it, 1920 itself accents it 43x elsewhere incl. page 607
  v.13, RAE has only the accented form (obligatory hiatus), modern BoM
  Éter 13:21 accents it, clean corpora always accent it — internal
  inconsistency. Checked and NOT logged: Éther 13:15 "sucedió que" —
  Session E first proposed logging a missing-space defect (Google OCR
  rendered the spot "sucedió,que"; 1886 has "Y sucedió que" with no
  comma; 1920's own vv.19/20/22/23 set "Y sucedió, que" normally), but
  the editor examined the page and ruled the mark scan debris, not a
  typed comma; transcribed "sucedió que" (mark dropped) per rule 36,
  the drafted errors-in-1920 entry removed. Éther 13:17 stray mark
  after "no" (rule 36 — Google reads "Pero no se" clean; weight-aware
  zoom p608_nocomma.png shows the mark lacks a real comma's tail
  unlike the clean "hombres," comma on v.16 directly above, looks like
  an ink blot fused to the "o"; 1886 has no comma after "no" either;
  editor confirmed directly it is a stray mark — contrast Éther 12:6
  where Google DID read the spurious comma and the glyph had proper
  comma weight). Éther 13:17 missing comma after "arrepintió" (1886
  v.17 and 1920's own v.22 both have it, so 1920 v.17 is internally
  inconsistent — but a bare serial-comma omission is within normal
  edition variance and the errors log has no precedent for logging
  pure "falta coma"; flagged for the editor's optional review). 13w
  "Ether" vs 13r "Éther" footnote-citation accent (inconsistent
  Pratt-footnote typesetting, both forms coexist doc-wide, preserved). Fresh pptext
  report (workspace/report_wsl_20260828b.html) walked end to end —
  page-608 flags are only "profecias" (logged) and "Shared" (v.23-24,
  Jaredite king, first appearance in the book — proper noun, added to
  permitted words, not an error); Edit Distance's only page-608 hit is
  the same "profecias(1):profecías(43)". No page-608 hit in smart
  quote, short/long lines, repeated word, duplicate line, ellipsis,
  dash (only hyphen is the digit-flanked "15:29-32" range in Block
  2), scanno, curly quote, special situations, book/paragraph level,
  or Jeebies. Footnote check: anchors 4506-4512 one contiguous run,
  no dupes/gaps/out-of-range. Whole-document sweeps all re-ran clean
  (check_spaced_punctuation, check_footnote_punctuation,
  check_verse_indent, footnote-anchor/Block-2 cross-check [max anchor
  now 4512 = max def 4512, no dupes, no anchored-without-def; only the
  documented Jacob 2:15/812 gap remains], curly-quote character scan
  of both master files). No narrow-space-vs-merge notes on this page.
  `permitted words.txt`: added "profecias", "Shared". `errors in
  1920.txt`: added Éther 13:21 (an Éther 13:15 entry was drafted then
  removed after the editor ruled the v.15 mark scan debris).
- **2026-08-28c**: Sessions A–E run in one session for page 609
  (Éther 13:26-31, then CAPÍTULO 14. opens mid-page, Éther 14:1-4),
  single footnote 4513 = 14a. Page opens with a fresh verse (13:26;
  page 608 ended 13:25 complete) — not mid-verse, not a chapter
  heading — so the first body line follows "Página 609" with no blank
  line (blank line reserved for chapter headings; matches the
  convention on every page that carries a chapter over). CAPÍTULO 14.
  falls mid-page with blank lines before/after; no subtitle (checked
  the image). Chapter boundary within the same book (Éther) so Block 1
  gets no blank line / book header (rule 20); Éther 14 letters reset to
  "a", global number continues at 4513. 37 raw body lines (19 for
  13:26-31, 18 for 14:1-4), unchanged after rejoins. Rule 7 — four
  line-break hyphen rejoins, all kept at first-line end: "derra-"/
  "maron" → "derramaron" (68), "acostum-"/"braba" → "acostumbraba"
  (66), "en-"/"contrar" → "encontrar" with the following ";" attaching
  after rule 31 normalization → "encontrar;" (61), "de-"/"fender" →
  "defender" (64). Rule 31: space-before-";" removed (13:27 ×2, 13:29,
  14:1 ×2). Rule 6: justification-widened gaps normalized (13:27
  "contra él", 13:28 "días. Y", 13:29 "en las"). MANDATORY i/l/1 check
  TRIGGERED: 14a's cross-reference target prints as a swash superscript
  reading as "l" with a raised separated tick; cross-checked against
  1879 file page 611 clean type — "a, see l, Hela. 13." shows an
  unambiguous tall undotted italic "l" (same line's "c, see i, ii.
  Nep. 10." shows a dotted "i" for contrast). Resolved "l"; content fit
  = Helamán 13 (Samuel the Lamanite) curse-on-the-land / slippery-
  treasures prophecy, exact match for Éther 14:1. Session D
  corroborated: 4513 auto-resolves to 3347 = Helamán 13l "Versículos
  33-37; Mormón 1:17-19; ..." (book-aware match, not one of the other
  "13l" entries in Mosíah/III Nefi). Session A Google cross-check
  caught one misread: draft bot-crop "esposas ó hijos" (14:1) vs the
  printed "esposas é hijos" — high-zoom (p609_ehijos.png) confirmed a
  clear acute "é" matching the press's other acutes on the same lines;
  corrected. Rule 36 — two suspected stray marks, both Google-silent:
  13:28 raised speck after "Heshlón." (weight-aware zoom shows it
  lighter/higher than a real period), 13:29 faint mark in the
  justified "en las" gap — both dropped, not logged. Session B
  independent re-verification: fn re-read fresh; body marker re-cropped
  at 16x (p609_supA.png — small single-story italic "a" flush before
  "maldición"); 1879 p611 footnote block re-cropped at 12x
  (p1879_611_fn2.png) re-confirming "l" not "i"/"1"; 1879's own "a"
  marker lands on "curse" in Éther 14:1 = 1920 "maldición" (rule 26
  content match). No changes from Session B. Session E — fresh pptext
  report workspace/report_wsl_20260828c.html generated and walked end
  to end. Only page-609 Spellcheck Suspect Words flag: "Heshlón"
  (13:28, line 27125) → added to permitted words.txt (Jaredite battle-
  plains place name, first appearance; 1886 book page 605 prints
  "Heshlon" no accent, modern Spanish BoM Éter 13:28 "Heslón" — variant
  spellings of an invented proper noun, NOT logged in errors in
  1920.txt per Session E rule 11 first bullet). Edit Distance: no
  page-609 hit. Every other report section touching page 609's line
  range (27116-27157) is a documented structural false positive —
  "short lines check" (verse-end short lines) and "special situations"
  line 27156 "...por la espada," (paragraph-ends-in-comma, because
  Éther 14:4 continues onto page 610, not yet integrated). Checked and
  NOT logged in errors in 1920.txt: Éther 13:29 "Coriantumr" (missing
  acute accent) — 1886 prints "Coriantumr" WITHOUT the accent at this
  identical verse (pages_1886/page_0623.png, book page 605) while
  accenting "Coriántumr" in the surrounding vv.28,30,31, so the v.29
  drop is a shared-lineage typesetting inconsistency inherited from
  1886, not a 1920-only deviation; the name is an invented BoM proper
  noun (RAE/corpora checks don't apply) and a bare missing accent
  shared with 1886 is the documented skip case; contrast page 608's
  "profecias" (logged because 1886 accented it and the accent is
  dictionary-obligatory). "Coriantumr" already in permitted words.txt;
  transcription preserves the printed form (rule 32). Éther 14:3 "he
  aquí" set tight in the 1920 print (Google OCR fuses it "heaquí") —
  NARROW-SPACE-VS-MERGE POINTER for the editor; committed default
  already written as two words per rule 6 / feedback_narrow_space_vs_
  merge (1886/grammar: always two words; Éther 13:29 on the same page
  spaces it normally); no file change. "quién" (14:3 relative pronoun,
  archaic accent) kept — aspell-accepted, pptext doesn't flag it, a
  permitted-words entry would be a no-op (cf. "Jesu Cristo" precedent).
  Whole-document sweeps all re-ran clean: check_spaced_punctuation
  (librodm.txt), check_footnote_punctuation (librodm_foot.txt),
  check_verse_indent (librodm.txt), footnote-anchor <-> Block-2 cross-
  check (max anchor 4513 = max def 4513, no duplicate defs, no
  anchored-without-def; only the long-documented Jacob 2:15 / 812 gap
  remains), curly-quote character scan of both master files (zero).
  Footnote check: anchors 4508-4513 contiguous, no dupes/gaps/out-of-
  range. Kept as printed (rule 32): "fué" (13:28, 14:4), archaic
  accented preterites (dió/batió/mató/irritó/obligó/acaeció). "Shared",
  "Akish", "Gilgal" already in permitted words.txt. permitted
  words.txt: added "Heshlón". errors in 1920.txt: no new entry.
  - **Editor follow-up (2026-08-28)**: the Éther 14:3 "he aquí"
    narrow-space pointer was resolved — the editor looked at the image
    directly and confirmed the gap, though tight, is slightly wider
    than most interior letter-spacing and reads as two separate words.
    The two-word transcription "he aquí" stands; no change to any file.
- **2026-08-28d**: Sessions A–E run in one session for page 610
  (Éther 14:5-18, all one chapter), footnotes 4514-4516 =
  14b/14c/14d. Page opens with a FRESH verse (14:5), not mid-verse:
  Éther 14:4 actually completes on page 609 ("...por la espada,", a
  comma-for-period shared with 1886, already handled on 609) —
  CLAUDE.md's prior "Next page" note wrongly anticipated a mid-verse
  continuation. First body line follows "Página 610" with no blank
  line (carried-over chapter). 44 raw image lines; one rule 7 rejoin
  ("bo-"/"rrachos." → "borrachos.", 66 chars, kept at first-line
  end) → 43 body lines. Rule 31: space-before-punct removed ×8 (v.10
  ";" ×2, v.12, v.16, v.17, v.18 ";"/":"/"!"). Rule 6: justification
  gaps normalized (v.15 "Agosh.  Y", v.17 "Shiz.  Y", v.18
  "de :  ¿Quién"). 3 markers: 14b=[4514] before "país" (v.6),
  14c=[4515] before "secretas" (v.8), 14d=[4516] before "país"
  (v.11). Cross-ref resolution — the 1920 superscript letters after
  "Véase" are illegible ink-blobs at 40x: 14b & 14d (both annotate
  "país de Morón", vv.6 & 11) → "Véase e, Éther 7." DECISIVE via
  1920's own Éther 7 footnote e (seq 4393) reading "Versículos
  6,16,17; Ether 14:6,11." (book-aware back-reference); Google OCR
  reads entry b as "Véase e"; 1879 file p.612 prints "d, see e,
  Ether 7." (1879 file p.611 prints "b, see c" — 1879's own
  different Éther 7 lettering, rule 26). 14c MANDATORY i/l/1 check →
  "Véase i, II Nefi 10." — 1879 file p.611 unambiguous short dotted
  "i"; 1920's own II Nefi 10 footnote i (seq 398) back-references
  "...Ether ... 14:8-10". Session D: 4514→4393, 4515→398, 4516→4393,
  all resolved. Session B — independent re-verification: fn block
  re-cropped fresh; 3 markers re-cropped 16x; i/l/1 re-run against
  1879 process_page fn_zoom + 30x crop (re-confirmed "i"); 14b/14d
  1879 letters re-checked (c on p.611, e on p.612). No changes from
  Session B. Session E — fresh pptext report report_wsl_20260828d.html
  (and -e.html to confirm suppression). Page-610 flags: Spellcheck
  Suspect Words ("acondeció", "Agosh", "ilevó") + Edit Distance
  ("acondeció:aconteció", "acondeció:aconieció", "ilevó:llevó").
  Decisions (1886 image + RAE + modern Spanish BoM + reference
  corpora): "acondeció" (14:11) → GENUINE 1920 ERROR for "aconteció"
  (1886 book p.606 & modern BoM both "aconteció"; no verb
  "acondecer"; 0 corpus hits) — permitted words + errors log,
  preserved as printed. "ilevó" (14:15) → GENUINE 1920 ERROR for
  "llevó" (1920 press genuinely set a dotted x-height "i" + tall
  "l", verified 34x crop p610_llevo2.png; 1886 "se llevó", modern
  "se había llevado"; no verb "ilevar"; Google normalizes to
  "llevó" — rule 14) — permitted words + errors log, preserved as
  printed per rule 32 / the page-442 "al año" precedent (NOT
  silently corrected). "perseguió" (14:17) → ERROR for "persiguió",
  SHARED WITH 1886 (inherited, not 1920-introduced): 1886 book p.606
  also prints "Shiz perseguió"; but modern BoM "persiguió", RAE
  "perseguir" is irregular with preterite "persiguió" (e>i), corpora
  attest only "persigui-" stem preterites, and v.15 same page prints
  correct "persiguió"; NOT flagged by pptext (aspell accepts it, but
  a clean section is not proof) — permitted words + errors log with
  a note that 1886 shares the reading. "Agosh" (14:15,16) → NOT an
  error, Jaredite place name, 1886/modern consistent — permitted
  words only ("Gilead"/"Shiz"/"Shared" already listed). Éther 14:16
  "Y cuando, llegó" spurious comma also LOGGED (1886 & modern BoM
  have no comma; punctuation-placement deviation, no permitted-words
  entry). NOT logged in errors: "Lib le dió a batalla" (14:13)
  unaccented "a" (shared with 1886); "dió la batalla a Lib" (14:11) unaccented "a"
  (reworded clause, bare missing accent). Narrow-space-vs-merge
  pointers surfaced for editor: 14:9 "por su", 14:15 "Lib le" (both
  committed as two words per 1886/grammar). Whole-document sweeps all
  re-ran clean (check_spaced_punctuation, check_footnote_punctuation,
  check_verse_indent, footnote-anchor/Block-2 cross-check [max anchor
  now 4516 = max def 4516, no dupes, no anchored-without-def; only
  the documented Jacob 2:15/812 gap remains, and 812 is the sole
  number missing from the 1..4516 anchor range], curly-quote
  character scan of both master files zero). Footnote check: anchors
  4514-4516 contiguous with 4513, no dupes/gaps/out-of-range.
  `permitted words.txt`: added "acondeció", "ilevó", "perseguió",
  "Agosh". `errors in 1920.txt`: added Éther 14:11 "acondeció",
  Éther 14:15 "ilevó", Éther 14:17 "perseguió".
- **2026-08-28e**: Sessions A–E run in one session for page 611
  (Éther 14:19-31, all one chapter; page opens with a fresh verse
  14:19 on a carried-over chapter, first body line follows
  "Página 611" with no blank line; page ends MID-verse 31
  ("...de que no"), last word not hyphenated, so page 612 continues
  v.31; Éther 14 runs to v.31 so the chapter ends early on 612).
  Footnotes 4517-4518 = 14e/14f, both in verse 24. 44 raw image
  lines; three rule 7 hyphen rejoins ("Corián-"/"tumr." v.20 → the
  only one whose second line was fully consumed, −1 line;
  "ca-"/"dáveres" v.22 and "Corián-"/"tumr," v.28 rejoined in place,
  second line retained) → 43 body lines. Rule 31: space-before-punct
  removed ×7 (v.21 ";", v.22 ";", v.23 ";", v.26 ";", v.27 ";",
  v.28 ";", v.29 ";"). Rule 6: justification gaps normalized ×5
  (v.22 "muertos.  Sino", v.27 "retirada.  Refugiáronse", v.28
  "Corihor.  Y" and "Shurr.  Ahora", v.29 "vez.  Y"). Markers:
  14e=[4517] before "muerte" (v.24, "la muerte de su hermano, que
  había sido matado" → Shiz's brother Lib, killed v.16), 14f=[4518]
  before "no" (v.24, "no perecería por la espada"). Block 1:
  "14e, 4517: Versiculo 16." (printed unaccented, matching the
  existing 18c/18d "Versiculo" entries), "14f, 4518: Éther 13:21."
  Footnote-entry letters heavily over-inked in the 1920 fn image
  (blob + slash shape); Google OCR read the 14f letter as "1"
  (i/l/1-adjacent) → MANDATORY 1879 check: 1879 file page 613 prints
  "e, ver. 16." and "f, Ether 13 : 21." in a clean typeface,
  unambiguous italic "e"/"f", reference content matching 1920 on
  both. Session D: 4517 and 4518 are direct references (not
  cross-refs), appended verbatim. Session B — independent
  re-verification: fn block + both body markers re-cropped fresh
  (18x); 1879 p.613 confirmation of letters and references (as
  above); no changes. Session C note: the git diff looked large
  because pages 588-610's integration was in the working tree but
  uncommitted (HEAD at page 587) — line counts reconcile exactly
  with page 610's Session E snapshot (librodm.txt 32071 → 32116,
  +45 for page 611; librodm_foot.txt 4845 → 4847). Session E —
  fresh pptext report report_wsl_20260828e.html walked;
  report_wsl_20260828f.html regenerated to confirm suppression.
  Page-611 flags: Spellcheck Suspect Words ("acamparse", "large",
  "persiguir", "Refugiáronse", "Shurr") + Edit Distance
  ("large:larga/largo", "persiguir:perseguir/persiguió") +
  paragraph-level "full stop followed by unexpected sequence" (v.19
  "suceder. que"). All other page-611 report hits are structural
  "short lines check" flood. Decisions (1886 file pp.624-625, book
  pp.606-607 + modern Spanish BoM + reference corpora): "large"
  (14:21) → GENUINE 1920 ERROR for "larga" (1886 "larga", modern
  BoM "larga", not a Spanish word, 0 corpus hits) — permitted words
  + errors log. "persiguir" (14:24) → ERROR for infinitive
  "perseguir", SHARED WITH 1886 (1886 book p.607 also "persiguir";
  but modern BoM "perseguir", normative infinitive is "perseguir"
  with e, 0 corpus hits for infinitive "persiguir", "perseguir" 8×
  in librodm.txt; same pattern as page 610's 14:17 "perseguió",
  feedback_errors_log_diligence) — permitted words + errors log with
  a note that 1886 shares it. "Coríantumr" (14:26) → GENUINE 1920
  ERROR for "Coriántumr" (acute accent misplaced onto the first "i",
  none over the "a"; 1886 & modern BoM "Coriántumr"; every other
  occurrence "Coriántumr"); NOT flagged by pptext (correct name in
  permitted words, aspell accepts the variant) but a clean section
  is not proof — errors log only, NOT added to permitted words
  (no-op). "suceder. que" (14:19) → INITIALLY logged as a 1920-only
  spurious period (pptext "full stop / unexpected sequence" flag +
  high-zoom crop + Google OCR also reading a period), then REVERSED
  2026-08-29 on the editor's direct look at the page: the mark is a
  stray speck, its type much smaller/lighter than a genuine period
  (rule 36 — the editor's own look is decisive; same outcome as
  III Nefi 14:2, 18:28, page 594 Éther 8:23). Period removed; body
  text now reads "suceder que" (= 1886) in page_611.txt and
  librodm.txt; the Éther 14:19 entry was deleted from
  errors in 1920.txt (no permitted-words entry had been made). Sweeps
  + pptext re-run after the fix, still clean, page-611 "full stop"
  flag now gone. "acamparse" (14:28) → NOT an error, valid reflexive
  infinitive — permitted words only. "Refugiáronse" (14:27) → NOT
  an error, legitimate archaic enclitic construction (1886
  "Refugiáronse") — permitted words only. "Shurr" (14:28) → NOT an
  error, Jaredite place name, 1886/modern consistent — permitted
  words only ("Corihor" already listed; "Comnor" not flagged by
  pptext, so no entry per the noticed-by-eye/no-op precedent).
  Rule 36 stray marks (v.24 speck before "en", v.20 speck after
  "Shiz,") checked against Google OCR (both absent) and dropped.
  Narrow-space-vs-merge pointer for editor: 14:19 "los habitantes"
  (Google fuses "loshabitantes"; committed as two words per
  1886/grammar). Whole-document sweeps all re-ran clean
  (check_spaced_punctuation librodm.txt 32118 lines,
  check_footnote_punctuation librodm_foot.txt 4847 lines,
  check_verse_indent librodm.txt, footnote-anchor/Block-2
  cross-check [max anchor 4518 = max def 4518, no dupes, no
  anchored-without-def; only the documented Jacob 2:15/812 gap
  remains, 812 the sole number missing from the 1..4518 anchor
  range], curly-quote character scan of both master files zero).
  `permitted words.txt`: added "acamparse", "large", "persiguir",
  "Refugiáronse", "Shurr". `errors in 1920.txt`: added Éther 14:21
  "large", Éther 14:24 "persiguir", Éther 14:26 "Coríantumr" (the
  Éther 14:19 "suceder. que" entry was added then removed same-cycle
  — editor reversed it as a stray speck, 2026-08-29).
- **2026-08-29**: Sessions A–E run in one session for page 612
  (tail of Éther 14:31, then Éther 15:1-10), first footnote 4519.
  Page OPENS mid-verse Éther 14:31, continuing from page 611 (611
  ended "...de que no", not hyphenated) — first body line
  "persiguiera más al ejército de Coriántumr; por lo tanto, se
  volvieron á su campo," follows "Página 612" with NO blank line
  (carried-over-chapter convention). Éther 14 ENDS here at v.31; a
  chapter-break ornament, then "CAPÍTULO 15." (blank line before/
  after), then verse 1 — checked for an Éther 15 subtitle, there is
  NONE (1879 p.613 and 1886 p.626 confirm: no subtitle). Page ends
  mid-verse Éther 15:10 at "...obligándoles á", last word not
  hyphenated → no page-boundary word-split; page 613 continues v.10.
  37 raw image body lines (2 for the 14:31 tail + 35 for 15:1-10);
  one rule 7 hyphen rejoin — v.8 "inter-"/"pretado" → "interpretado",
  which would make its line 74 chars so moved to the start of the
  next line, second image line retained → 37 output body lines.
  check_lines clean. Rule 31: space-before-semicolon removed ×12
  (v.31 "Coriántumr ;", v.1 "anunciado ;", v.2 "corazón ;", v.3
  "hecho ;"/"profetas ;"/"puntos ;", v.6 "iniquidades ;"/"Shiz ;"/
  "Coriántumr ;", v.8 "todo ;"/"tiendas ;"/"ellos ;"). Rule 6:
  justification gaps normalized ×2 ("toda  consolación." v.3,
  "que el  ejército" v.6). 3 footnote markers, all in Éther 15 (Éther
  14 has no footnote on this page; letters RESTART at 15a while the
  global number continues from 4518): 15a=[4519] before "palabras"
  (v.1) = "Éther 13:20-21." (1920 fn "Éther 13 : 20, 21." → rule
  22/23); 15b=[4520] before "dos" (v.2) = the population note
  "Incluyendo esposas y niños, el número fué probablemente entre diez
  y quience millones."; 15c=[4521] before "aguas" (v.8) = "Supuesto
  ser el lago Ontario." Footnote letters a/b/c all clean italic, none
  i/l/1 — no mandatory check triggered; Session B still ran the 1879
  content cross-check (Éther 15 = 1879 file pp.613-614): 15a matches
  1879 "a, Ether 13 : 20, 21." and 1879 places its "a" marker before
  "words" in 15:1 (exact positional match); 15b matches 1879 "b,
  including wives and children... from ten to fifteen millions."
  (1879's "fifteen" independently confirms "quience" = "quince"); 15c
  matches 1879 "c, supposed to be Lake Ontario." All CONFIRMED, no
  changes from Session B. Session D: generate_block2.py mishandled the
  wrapped 15b entry — appended a duplicate "4520: Incluyendo... / y
  quience millones." AFTER the 4521 line (same wrapped-Block-1-entry
  bug class the integrate-page skill notes for append_block1); the
  stray pair was removed by hand, librodm.txt ends correctly at 4521
  (32164 lines). Session C: librodm.txt 32118→32160 (+42: 41 body
  lines + 1 separator), librodm_foot.txt 4847→4851; no book/chapter
  blank line (same book, Éther 14→15, rule 20); big git diff on the
  master files is just pages 588-611's uncommitted integration (HEAD
  at page 587). Session E: fresh pptext report_wsl_20260829.html
  walked; report_wsl_20260829b.html regenerated to confirm
  suppression. Page-612 pptext flags: Spellcheck Suspect Words
  ("quience", "Ripliáncum") + Edit Distance ("quience:quince") +
  paragraph-level "paragraph ends in comma" (the v.31 "campo," — a
  real error here, not the usual boundary-wrap false positive); all
  other hits are the structural short-lines / standalone-1 flood.
  Decisions (1886 Éther 14 end = file p.625, Éther 15 = file p.626;
  1879 file pp.613-614; modern BoM; reference corpora): Éther 14:31
  "campo," → GENUINE 1920 ERROR (comma where verse/chapter 14 ends;
  1886 "campo." + 1879 "camp." + modern BoM all end with a period) —
  errors log only (punctuation, no permitted-words entry). Éther 15:2
  fn b "quience" → GENUINE 1920 ERROR for "quince" (1879 fn "fifteen
  millions"; not in RAE; 0 corpus hits vs. "quince" 57×; edit-distance
  to 4 correct occurrences; 1886 has no footnotes so no direct 1886
  compare) — permitted words + errors log ("Éther 15:2 (nota b)" per
  the Éther 2:24/12:25 footnote-error precedent). Éther 15:8 "ó es él
  que sobrepuja" → GENUINE 1920 ERROR (spurious acute on the átono
  relative "el que"; 1886 "el que" unaccented) — NOT flagged by
  pptext (aspell accepts "él"), errors log only, NOT added to
  permitted words (no-op, cf. page 611's "Coríantumr"). "Ripliáncum"
  (v.8, Jaredite place name, first appearance; 1886 + modern BoM
  identical) → NOT an error, permitted words only. Narrow-space
  word-pairs surfaced for the editor (all committed as two words,
  1886 file pp.625-626 prints every one as two words): Éther 15:4 "á
  suceder", 15:5 "que contestó" / "cuando hubo", 15:6 "sucedió, que",
  15:8 "que llegó", 15:10 "acaeció, que" / "que los" (this last the
  tightest, Google fused it). Google full-page manual cross-check
  (the automated script only compared the 2-line 14:31 tail, its body
  extractor stopping at the first blank line before the chapter
  heading): after ignoring word-fusion and glued superscripts,
  Google's OCR matches letter-for-letter, including the preserved
  anomalies "quience", "él", and the "campo," comma. Whole-document
  sweeps all re-ran clean (check_spaced_punctuation librodm.txt 32164,
  check_footnote_punctuation librodm_foot.txt 4851, check_verse_indent
  librodm.txt, curly-quote scan of both master files zero,
  footnote-anchor ↔ Block-2 cross-check [max anchor 4521 = max def
  4521, no dupes, no anchored-without-def, no gaps in the 1..4521 def
  range; only the documented Jacob 2:15/812 defined-without-anchor gap
  remains]). `permitted words.txt`: added "quience", "Ripliáncum"
  (1272→1274). `errors in 1920.txt`: added Éther 14:31 "campo,",
  Éther 15:2 (nota b) "quience", Éther 15:8 "él", appended in
  book/chapter/verse order after the Éther 14:26 entry.
  2026-08-29 editor correction: the Éther 15:8 "él" entry was
  REVERSED and removed from `errors in 1920.txt`. 1920's accented
  "él que" in this relative construction ("es él que sobrepuja á
  todo") is consistent house style, not an error — "él que" occurs
  178× in librodm.txt vs. a single unaccented "el que" (line 3763),
  including the identical "es él que + verb" frame at 6101/12246/
  15894/25005/26148 etc. This is a legitimate 19th-century
  orthographic convention (tilde on "él" before "que" when "él" has
  pronominal/emphatic force, standard before the RAE tightened the
  tilde-diacrítica rules in the 20th century); 1886's unaccented
  "el que" there is just 1886 dropping an accent as it often does.
  Lesson: a deviation from 1886 is NOT an error when 1920 does it
  consistently document-wide — check 1920's own internal frequency,
  not only 1886 (cf. feedback_errors_log_diligence, the inverse of
  its usual direction). Body text unchanged; no permitted-words
  entry (pptext never flagged "él").
- **2026-08-29b**: Sessions A–E run in one session for page 613
  (Éther 15:10-21, all one chapter — Éther 15, opened on page 612),
  first footnote 4522. Page OPENS mid-verse Éther 15:10, continuing
  from page 612 (612 ended "...obligándoles á", not hyphenated) —
  first body line "emprender la retirada; lo que hicieron hacia el
  [4522]Sud, plantando" follows "Página 613" with NO blank line
  (carried-over-chapter convention). Whole page is one chapter; ends
  mid-chapter at v.21 ("...pelearon otra vez hasta que llegó la
  noche;" — semicolon), last word not hyphenated → no page-boundary
  word-split; page 614 continues with v.22. 43 raw image lines, NO
  rule 7 hyphen rejoins on the page → 43 body lines. Rule 31:
  space-before-semicolon removed ×15 (vv.10,11,12,13×3,15×2,16×2,17,
  19×2,20,21) + rule 22 colon-spaces removed in fn block (15f "6 : 6",
  15g "13 : 14", 15h "10 : 27"). Rule 6: column set evenly, no
  wider-than-justified gaps to normalize. 8 markers, all Éther 15
  (chapter opened page 612 with 15a-15c; letters d..k here, global
  number continues from 4521): 15d=[4522] before "Sud" (v.10), an
  explanatory note; 15e=[4523] before "cerro" (v.11); 15f=[4524]
  before "ocultó" (v.11) = Mormón 6:6; 15g=[4525] before "presenció"
  (v.13) = Éther 13:14; 15h=[4526] before "armaron" (v.15) = Éther
  10:27; 15i=[4527] before "empezaron" (v.16) = Versículo 17;
  15j=[4528] before "llenaron" (v.17) = Versículo 16; 15k=[4529]
  before "otra" (v.18) = Versículo 4. MANDATORY 1879 check (15i is an
  "i", 15j a "j"): chapter_map lists Éther 15 = 1879 file p.613, but
  1879 pagination runs behind — 15a on 1879 p.613, d-g on 1879 p.614,
  h-k on 1879 p.615. 1879 p.615 fn block (clean italic): "h, Ether
  10 : 27.  i, ver. 17.  j, ver. 16.  k, ver. 4." — i/j unambiguous.
  1879 body p.614/615 marker positions all match 1920 letter-for-
  letter (v.10 "flee ^d southward", v.11 "by the ^e hill Ramah" /
  "did ^f hide up the records", v.13 "Ether ^g did behold", v.15
  "being ^h armed", v.16 "they ^i took up a howling", v.17 "they did
  ^j rend the air", v.18 "wrote ^k again"). 1879 p.614 fn also
  corroborates 15d/15e content. Session B: fresh 5x fn-block crop +
  independent 1879 p.615 re-crop + 9x body-marker re-crops; no
  changes. Session C: 43 body lines + 1 blank inserted before "Notas",
  librodm.txt 32164→32209; Block 1 15d-15k appended to librodm_foot.txt
  (4851→4860, +9 lines: 15d wraps to two lines); no book/chapter blank
  line (same book, all Éther 15, rule 20). Big git diff on the master
  files is still just pages 588-612's uncommitted integration (HEAD at
  page 587). Session D: 15d-15k are all direct references (no "Véase"),
  resolved to 4522-4529 and appended to librodm.txt's Notas —
  generate_block2.py AGAIN mishandled the wrapped 15d entry, re-emitting
  spurious duplicate lines "4523 / 4525 / 4527 / 4529" after the real
  4529 (same wrapped-Block-1-entry bug as pages 611/612); the 4 stray
  lines removed by hand, librodm.txt ends correctly at 4529 (32218).
  Session E: fresh pptext report_wsl_20260829c.html walked;
  report_wsl_20260829d.html regenerated to confirm suppression ("Ogath"
  and "Yendose" gone from Spellcheck Suspect Words). Page-613 pptext
  flags: Spellcheck Suspect Words "Ogath" (v.10) + "Yendose" (Block 2
  fn 4522) only — no Edit Distance / Dash / Footnote / Scanno /
  Curly-quote / Special-situations / paragraph-level hits for page 613;
  all other report hits are the structural short-lines flood.
  "ahullar" (v.16) and "satán" (v.19) not flagged by aspell.
  Decisions (1886 Éther 15 = file pp.626-627, book pp.608-609; 1879
  file pp.613-615; modern BoM Éter 15; reference corpora): "Ogath"
  (v.10, Jaredite place name, first appearance) → NOT an error, 1886
  p.626 "Ogath" identical (modern BoM "Ogat" is an independent modern
  transliteration) — permitted words only. "Yendose" (fn 15d = [4522])
  → initially called permitted-words-only ("just a missing accent"),
  then corrected to GENUINE 1920 ERROR for "Yéndose" on the editor's
  same-session challenge: "yendo" is llano/unaccented but the enclitic
  "se" makes "yéndose" esdrújula, which always takes a tilde (RAE);
  "yendose" is not a valid/archaic form (0 corpus hits for "yéndose"
  bar one accent-less OCR'd-Bible hit); the rule-11 "missing accents
  aren't errors" shortcut needs 1886 to share the pattern, but 1886
  has no footnotes AND 1920 accents gerund+enclitic esdrújulas with
  total regularity everywhere else (volviéndose, diciéndole, dándoles,
  regocijándose, … hundreds, all tilded) — a lone deviation, exactly
  parallel to Éther 8:15 "administro"; also consistent with the
  editor's own "él que" reasoning (house style Nx vs. 1 lone slip →
  the slip is the error). Google OCR also reads "Yendose"; pptext
  flagged it. → permitted words + errors log ("Éther 15:10 (nota d)").
  Éther 15:15 "mujeres ó
  hijos" → GENUINE 1920 ERROR for "mujeres é hijos": 1920 prints the
  disjunctive "ó" (or) where the copulative "é" (and) is required;
  1886 p.627 "con sus mugeres é hijos", 1879 "with their wives and
  their children", modern BoM "con sus esposas y sus hijos" — all
  copulative; confirmed at 12x zoom (closed "o" loop with acute, no
  e-crossbar); Google OCR "corrects" it to "é". Letter/conjunction
  question, 1886 comparison suffices. NOT flagged by pptext (aspell
  accepts both "ó"/"é") → errors log only, NOT added to permitted
  words (no-op, cf. page 611 "Coríantumr" / page 612 "él").
  fn 15d "llevó a la región" (unaccented "a") → NOT an error, missing
  accent, not pptext-flagged, no-op. "ahullar" (v.16) → NOT a new
  finding: already in permitted words (line 1038, from Mormón 8:22),
  1886 p.627 also prints "ahullar" (shared). "satán" (v.19, lowercase)
  → NOT an error, the 1920 translation's consistent form (~25× in
  librodm.txt, aspell auto-accepts). Google-text cross-check
  (`google_text_1920/page_0635.txt`): the automated body extractor
  worked line-by-line here; after ignoring word-fusion and glued
  superscripts, Google matches letter-for-letter EXCEPT 3 spots, all
  re-zoomed — v.15 "mujeres ó hijos" (Google "é"; 1920 image "ó",
  logged as error), v.17 "Y acaeció" (Google no mark; a faint speck
  between "Y" and "acaeció" — rule 36, Google silence = stray speck,
  transcribed with plain space), v.20 "día, y cuando" (Google drops
  the "y"; 9x zoom shows "y cuando", kept). Narrow-space word-pairs
  surfaced for the editor (all committed as two words, 1886 file
  pp.626-627 prints every one as two words): Éther 15:15 "vino á
  suceder", 15:16 "vino á suceder", 15:12/15:13 "sucedió, que", 15:18
  "escribió [4529]otra". Whole-document sweeps all re-ran clean
  (check_spaced_punctuation librodm.txt 32218, check_footnote_
  punctuation librodm_foot.txt 4860, check_verse_indent librodm.txt,
  curly-quote scan of both master files zero, footnote-anchor ↔
  Block-2 cross-check [max anchor 4529 = max def 4529, no dupes, no
  anchored-without-def, no gaps in the 1..4529 def range; only the
  documented Jacob 2:15/812 defined-without-anchor gap remains]).
  `permitted words.txt`: added "Ogath", "Yendose" (1274→1276).
  `errors in 1920.txt`: added Éther 15:10 (nota d) "Yendose" and
  Éther 15:15 "mujeres ó hijos", inserted in book/chapter/verse order
  after the Éther 15:2 (nota b) entry. (Note: page 612's Éther 15:8
  "él" entry had been removed by a separate 2026-08-29 editor reversal
  before this session's errors-log edits — 1920's accented "él que" is
  consistent house style, 178× vs. 1, not an error; see the 2026-08-29
  page-612 log entry.)
- **2026-08-29c**: Sessions A–E run in one session for page 614
  (Éther 15:22-34), footnotes 4530-4533, chapter 15's letters l-o.
  Page opens MID-verse Éther 15:22 on a carried-over chapter (page 613
  ended v.21 "...llegó la noche;", last word not hyphenated → no
  page-boundary word-split; first body line follows "Página 614" with
  no blank line). Verse 34 is the LAST verse of Éther 15 and of the
  entire Book of Éther — page ends "...el reino de Dios. Amén.", then
  the divider + fn block, no end-of-book colophon line on this page.
  Page 615 opens the Book of Moroni. 44 raw image lines; one rule 7
  hyphen rejoin whose second line was fully consumed — v.25
  "Corián-"/"tumr." (66 chars, kept at line end, −1 line) → 43 body
  lines; a second rejoin v.29 "aconte-"/"ció," was in-place (67
  chars), second line retained. Rule 8: v.33's "[4531]concluyó sus
  anales, (cuya [4532]centésima parte no he escrito yo,)" = exactly 73
  chars with markers, last word "yo,)" moved to next line. Rule 31:
  space-before-punct removed ×11 (";" at vv.22×2, 23, 24, 28×2, 29;
  ":" at v.33 "Éther:", v.34 "estas:"; ";" v.33 "ahora;", v.34
  "importa;"). Rule 6: sentence double-spacing collapsed ×5 (v.26
  "siguiente.  Y", v.29 "espadas.  Y", v.31 "cayó.  Y", v.33
  "Éther:  Sal", v.34 "Dios.  Amén."). 4 markers, all Éther 15:
  15l=[4530] before "Coríantumr" (v.32), 15m=[4531] before "concluyó"
  (v.33), 15n=[4532] before "centésima" (v.33), 15o=[4533] before
  "pueblo" (v.33). Block 1: "15l, 4530: Omni 1:20-22." /
  "15m, 4531: Éther 13:14." / "15n, 4532: Véase e, Éther 1." /
  "15o, 4533: Véase k, Mosíah 8." Footnote-entry letter 15l is an
  "l" → MANDATORY 1879 check: 1879 file page 616 (which also carries
  the end of Éther + opening of Moroni 1; 1879 pagination runs behind,
  15d-15k were on 1879 pp.614-615) prints in clean italic
  "l, Omni 1 : 20—22.   m, Ether 13 : 14.   n, see e, Ether 1.
  o, see k, Mos. 8." — "l" a single dotless stroke (not i/1); 15n
  target a clean "e" (not "c"); 15o target a clean "k" (not "b").
  1879 p.616 body confirms all four marker positions (^l Coriantumr,
  ^m finished, ^n hundredth, ^o people of Limhi). Session D: 4530/4531
  direct refs; 4532 → 4277 (Éther 1e, whose own text cites "15:33" — a
  clean cross-check of marker n's placement), 4533 → 1187 (Mosíah 8k,
  people-of-Limhi / gold plates — content-fit for "pueblo de Limhi los
  encontró"). generate_block2.py again mishandled the run (re-emitted 2
  spurious duplicate lines "4531"/"4533" AFTER the real 4533 — same
  wrapped-Block-1-entry bug as pages 611-613; the wrapped entry this
  time is page 613's 15d still in the working set); removed by hand,
  librodm.txt ends correctly at 4533 (32267 lines). Session B —
  independent re-verification: fresh 1920 fn crop (7x) + fresh 1879
  p.616 crop (5x) + fresh body-marker crops (9x); no changes.
  Session C: librodm.txt 32218 → 32263 (+45 for page 614, wait: was
  32218 after page 613's Session E; page 614 adds 43 body + "Página
  614" + blank separator = 45 → 32263), then +4 Block 2 = 32267;
  librodm_foot.txt 4860 → 4864 (15l-15o, all single-line). Session E —
  fresh pptext report report_wsl_20260829e.html walked;
  report_wsl_20260829f.html regenerated to confirm suppression.
  Page-614 flags: "sù" (v.34) in Spellcheck Suspect Words + Edit
  Distance ("sù:su", "sù:se") + character checks; "Coríantumr" (v.32)
  NOT flagged; dash-check "Omni 1:20-22" (legit verse range);
  "standalone 1" for "Omni 1:20-22" (structural); all other page-614
  report hits are the "short lines check" flood. Decisions (1886 file
  pp.627-628, book pp.609-610 + modern Spanish BoM Éter 15): Éther
  15:32 "Coríantumr" → GENUINE 1920 ERROR for "Coriántumr" (acute
  misplaced onto first "i", none over "a"; 1886 & modern BoM
  "Coriántumr"; every other occurrence on page 614 correct; identical
  to page 611's Éther 14:26 finding) — errors log only, NOT added to
  permitted words (no-op, per page 611 "Coríantumr" / page 612 "él"
  precedent). Éther 15:34 "sù" → INITIALLY logged as a GENUINE 1920
  ERROR for the possessive "su" (a mark over the "u"; Google OCR read
  "sù", pptext flagged it in Spellcheck + Edit Distance + character
  checks, a same-page zoom read a grave stroke; grave accents occur
  nowhere else in this document; 1886 p.628 "su voluntad" unaccented),
  then REVERSED 2026-08-29 on the editor's direct look at the page: the
  mark is too light to be typeset — a stray speck, not real type
  (rule 36 — the editor's own look is decisive; cf. III Nefi 14:2,
  18:28, page 594 Éther 8:23, page 611 Éther 14:19). Body text changed
  "sù voluntad" → "su voluntad" (matches 1886) in page_614.txt and
  librodm.txt; the Éther 15:34 entry was removed from errors in
  1920.txt and "sù" removed from permitted words.txt; pptext re-run
  (report_wsl_20260829g.html) confirms "sù" now absent from every
  section. Net logged error for page 614: ONE (Éther 15:32
  "Coríantumr"). Coríantumr preserved as printed (rule 32); no other
  text changes. Narrow-space pointers for editor (all committed as two
  words, 1886 file p.628 prints every one spaced): Éther 15:26
  "comieron y durmieron" / "durmieron, y se", 15:27 "espacio de tres",
  15:28 "Y ocurrió" / "cuando los", 15:31 "que hubo". Whole-document
  sweeps all re-ran clean (check_spaced_punctuation librodm.txt 32267,
  check_footnote_punctuation librodm_foot.txt 4864, check_verse_indent
  librodm.txt, curly-quote scan of both master files zero,
  footnote-anchor ↔ Block-2 cross-check [max anchor 4533 = max def
  4533, contiguous 1..4533, no dupes, no anchored-without-def; only
  the documented Jacob 2:15/812 defined-without-anchor gap remains]).
  `permitted words.txt`: net no change (added "sù" then removed it on
  the reversal — back to 1276).
  `errors in 1920.txt`: net +1 — added Éther 15:32 "Coríantumr" (plain
  append; the Éther 15:34 "sù" entry was added then removed same-cycle
  on the editor's reversal; file 887 → 888 lines).
- **2026-08-29d**: Sessions A–E run in one session for page 615
  (Moroni 1:1-4 and Moroni 2:1-3), first footnote 4534, chapter 1's
  letters a-c and chapter 2's letters a-d. Page OPENS the Book of
  Moroni (Éther ended on page 614, 15:34). Body begins with the
  all-caps title line "EL LIBRO DE MORONI." (transcribed as a body
  header, blank-line separators), then a centered decorative rule (not
  transcribed), then "CAPÍTULO 1." NO book subtitle/argument line. Per
  rule 1 "Página 615" is separated from the title by a blank line
  (page does not open mid-verse). Two complete chapters: Moroni 1
  (vv.1-4) + a second decorative rule + "CAPÍTULO 2." + Moroni 2
  (vv.1-3). 28 body print lines (title + "CAPÍTULO 1." + 14 verse
  lines + "CAPÍTULO 2." + 11 verse lines). NO hyphen splits anywhere
  (rule 7 N/A); no line reaches 73 chars with markers → no rule 8
  rebalancing. Rule 31: 1920 prints a space before ";" and ":"
  throughout — removed ×11. Rule 6: reduced-width spaces at Moroni 1:1
  "de los" and 1:2 "que sus guerras" normalized (Google fused both).
  7 markers: 1a=[4534] before "extracto" (v.1) = Véase el Libro de
  Éther; 1b=[4535] before "excesivamente" (v.2) = I Nefi 12:20-23;
  Mormón 5:15; 1c=[4536] before "utilidad" (v.4) = II Nefi
  3:7,11,12,19-21; Véase c, II Nefi 27; 2a=[4537] before "discípulos"
  (2:1) = Véase c, III Nefi 12:1; 2b=[4538] before "recibiréis" (2:2)
  = Versículo 3; III Nefi 18:37; 2c=[4539] before "oídas" (2:3) = III
  Nefi 18:37; 2d=[4540] before "impusieron" (2:3) = Véase b. MANDATORY
  i/l/1 check NOT triggered — every entry-letter (a-d) and every
  cross-ref target ("c"×2, "b") is a/b/c/d; no i/l/1, so no 1879
  check required. Session B: fresh high-zoom crops of both fn blocks +
  fresh body-marker crops; the "Véase c" targets confirmed as clean
  "c" (round open glyph), "Véase b" target a clean "b"; no changes.
  Session C: librodm.txt 32267→32302 (+35 for page 615: 34 content
  lines + blank separator), then +7 Block 2 in Session D → 32312;
  librodm_foot.txt 4864→4874, with book-boundary header "EL LIBRO DE
  MORONI" auto-inserted (chapter 1 < previous chapter 15; header text
  from this page's own title line minus the period, matching the "EL
  LIBRO DE ÉTHER" precedent). Chapter boundary 1→2 within Moroni = no
  blank line in Block 1 (rule 20). Session D: cross-refs resolved
  4536→682 (II Nefi 27c), 4537→3664 (III Nefi 12c), 4540→4538 (Moroni
  2b); 4534 "Véase el Libro de Éther." left as descriptive text
  (whole-book ref, not a chapter+letter cross-ref — matches the
  original). generate_block2.py's wrapped-Block-1-entry bug did NOT
  trigger this time (no Block 1 entry on page 615 wraps). Session E:
  fresh pptext report report_wsl_20260829h.html walked end to end.
  Page 615 produced ZERO Spellcheck/Edit-Distance/Footnote/Scanno/
  Curly-quote/repeated-word/duplicate-line hits; only the structural
  short-lines flood and the legit verse-range hyphens "12:20-23"/
  "19-21" in the dash check. Two inherited spelling quirks from
  Session A's flags, BOTH resolved as GENUINE 1920 errors SHARED with
  1886 (editor decision "Log both", after a corpus double-check):
  (1) Moroni 1:1 "no hé perecido" — accented "hé" as perfect
  auxiliary; 1886 file p.629 also "no hé perecido todavia"; same verse
  has correct "me he dado"; "hé" not a valid form of haber; cero
  corpus attestation of "hé perecido" or accented "hé aquí" (all 22
  "he aquí" in Quijote/RV1909/RV-full unaccented); modern BoM "he".
  (2) Moroni 2:1 "había escojido" — j for g; 1886 file p.629 also
  "que habia escojido"; "escojido" only here + Alma 46:17 (already
  logged — direct precedent) vs "escogido" 60+×; RAE only accepts
  "escoger"/"escogido"; cero "escojido" in all 3 corpora (the
  escoja/escojo/escojáis j-forms present are orthographically
  mandatory ante a/o); modern BoM "escogido". Both "hé" and "escojido"
  were ALREADY in permitted words.txt (from earlier sessions — "hé"
  via "hé aquí", "escojido" line 952) → no new permitted-words
  entries. Both added to errors in 1920.txt (plain append after the
  Éther 15:32 entry — Moroni is the last book, these are its first
  entries, so append = correct book order). Accent difference NOT
  logged (house style): Moroni 2:2 1920 "los cuáles impongáis" vs
  1886 unaccented "cuales impongais" — 1920 accents relative pronouns
  document-wide. Whole-document sweeps all re-ran clean
  (check_spaced_punctuation librodm.txt 32312, check_footnote_
  punctuation librodm_foot.txt 4874, check_verse_indent librodm.txt,
  curly-quote scan of both master files zero, footnote-anchor ↔
  Block-2 cross-check [max anchor 4540 = max def 4540, contiguous
  1..4540, no dupes, no anchored-without-def; only the documented
  Jacob 2:15/812 defined-without-anchor gap remains]). Narrow-space
  pointers for editor (both committed as two words, 1886 file p.629
  prints both spaced): Moroni 1:1 "de los", Moroni 1:2 "que sus
  guerras". `permitted words.txt`: net no change (1276). `errors in
  1920.txt`: net +2 — Moroni 1:1 "hé" and Moroni 2:1 "escojido"
  (file 888 → 890 lines).

- **2026-08-29e**: Sessions A–E run in one session for page 616
  (Moroni 3:1-4 and Moroni 4:1-3), first footnote 4541, chapter 3's
  letters a-c and chapter 4's letters a-e. Page CONTINUES the Book of
  Moroni (opened page 615; Éther ended page 614). Page 615 ended
  Moroni 2:3, so page 616 OPENS with a chapter heading "CAPÍTULO 3." —
  "Página 616" separated from it by a blank line (rule 1); running
  header "616  LIBRO DE MORONI.  (CAP. III, IV." discarded. NO
  book-title header on this page (still within Moroni). Two complete
  chapters: Moroni 3 (vv.1-4), a centered decorative rule (NOT
  transcribed), "CAPÍTULO 4.", Moroni 4 (vv.1-3); decorative rules also
  before "CAPÍTULO 3." and after Moroni 4:3 (none transcribed). 25 body
  print lines. NO hyphen splits (rule 7 N/A). Rule 8: one rebalance —
  "Dios, Padre Eterno, ... el [4548]nombre de tu" = 74 chars with the
  marker → "tu" moved to next line. Rule 31: space-before-";"/":"
  removed ×6 body + spaced colons/semicolons in fn block. Rule 6:
  double-spacing after sentence punctuation collapsed; NO narrow-space
  word-pairs on this page (Google OCR of page 0638 keeps the same word
  boundaries). 8 markers: 3a=[4541] "dicípulos" (3:1)=Versículos 2-4;
  Véase c, Mosíah 6; 3b=[4542] "ordenaron" (3:1)=Véase c, III Nefi
  12:1; 3c=[4543] "poder" (3:4)=I Nefi 13:37; Moroni 6:9; 4a=[4544]
  "carne" (4:1)=Véase t, III Nefi 18; 4b=[4545] "Élderes" (4:1)=
  Versículo 1; Moroni 3:1; 4c=[4546] "arrodillándose" (4:2)=Doctrinas y
  Convenios 20:76; 4d=[4547] "cuerpo" (4:3)=Véase t, III Nefi 18;
  4e=[4548] "nombre" (4:3)=Véase e, Mosíah 5. ANOMALY — Moroni 4:3
  prints a well-formed superscript "d" before "Él" ("mandamientos que
  [d]Él les ha dado"), a THIRD superscript in v.3 with NO corresponding
  footnote (Moroni 4 has only a-e, all placed at carne/Élderes/
  arrodillándose/cuerpo/nombre) and NO 1879 counterpart (1879 file
  p.618 Moroni 4 markers = a Elders, b flesh, c kneel, d body, e name;
  nothing at "which he hath given them"). Google OCR registers a mark
  there but can't read it ("¿El"). Preserved by NOT inserting a body
  marker; logged in errors in 1920.txt. MANDATORY i/l/1 check NOT
  triggered (entry-letters a-c / a-e; cross-ref targets "c"×2 for
  Moroni 3, "t"×2 + "e" for Moroni 4 — no i/l/1). Discretionary "t"
  cross-check (Moroni 4a/4d, "Véase t, III Nefi 18"): both 1920 and
  1879 (file p.618, three times — 4b, 4d, and Moroni 5a) print a SHORT
  crossbarred italic letter = "t", not "f". NOTE for editor: content-fit
  would mildly favour "f" (III Nefi 18f reciprocally cites Moroni 4:3),
  but both editions visually print "t" → rule 32, transcribed "t", NOT
  logged as an error. Also confirmed 1920 4a↔4b are swapped vs 1879
  4a↔4b (word order "carne...Élderes" vs "Elders...flesh" — translation
  artifact, rule 26; matched by content); 1920's Moroni 3 adds a 3c
  with no 1879 equivalent (1879 Moroni 3 has only a,b). Session B:
  fresh full fn crop + fresh 1879 p.618 crop + fresh body-marker crops;
  all confirmed unchanged. Session C: librodm.txt 32312→32345 (+33: 25
  body lines + 2 "CAPÍTULO N." + 5 blanks + "Página 616" + blank sep);
  librodm_foot.txt 4874→4882 (8 Block 1 entries, NO book header, NO
  blank lines — chapters 2→3→4 same book, rule 20). Session D:
  generate_block2.py AGAIN emitted a spurious duplicate ("4545:
  Versículo 1; Moroni 3:1." re-appended after the real 4548 — same
  wrapped-Block-1-entry bug as pages 611-614) — removed by hand;
  librodm.txt ends at 4548 (32353). Cross-refs resolved (book-aware):
  4541→1141 (Mosíah 6c), 4542→3664 (III Nefi 12c, same target as page
  615's 4537), 4544 & 4547→3773 (III Nefi 18t), 4548→1131 (Mosíah 5e);
  4543/4545/4546 direct. Anchor↔Block-2 cross-check after fix: max
  anchor 4548 = max def 4548, contiguous 1..4548, no dupes, no
  anchored-without-def; only the documented Jacob 2:15/812 gap remains.
  Session E: fresh pptext report_wsl_20260829i.html walked end to end.
  Page-616 Spellcheck hits: "dicípulos" (Moroni 3:1), "perserverancia"
  (Moroni 3:3); Edit Distance: "dicípulos:discípulos" (same) + "Élder"
  (established term, benign); everything else page-616 is the structural
  short-lines flood + the legit "2-4" verse-range hyphen in 4541's dash
  line. Footnote/scanno/curly-quote/repeated-word/duplicate-line/
  paragraph/Jeebies sections: nothing for page 616. FIVE entries added
  to errors in 1920.txt (890→895): (1) Moroni 3:1 "dicípulos"
  (discípulos) — missing first "s"; 1886 has a different wording for
  this verse but prints "discipulos" with the "s" in Moroni 2:1,3; 1920
  uses "discípulos" everywhere else (65 corpus hits, 0 for the typo);
  RAE only "discípulo"; modern BoM "discípulos". (2) Moroni 3:3
  "perserverancia" (perseverancia) — extra "er"; 1886 file p.630
  "perseverancia"; RAE only "perseverancia"; 0 corpus hits; modern BoM
  "perseverancia". (3) Moroni 3:4 "Masetros" (Maestros) — "e"/"s"
  transposed; the same verse's line 1 prints "Maestros" correctly; 1886
  file p.630 "Maestros"; 0 corpus hits; modern BoM "maestros"; same
  pattern as Mormón 8:28/8:38; not pptext-flagged (suppressed by
  "masetros" in permitted words.txt from page 571). (4) Footnote Moroni
  4:3 spurious superscript "d" before "Él" (the ANOMALY above).
  (5) Mormón 8:38 "masetros" (maestros) — PRE-EXISTING GAP surfaced by
  this run's pptext report: page 572's Session E Corrections log says it
  checked this vs 1886 (which prints "maestros") and "logged in errors
  in 1920.txt", but the entry was never actually added; added now,
  inserted before the Mormón 8:40 entry to keep verse order; no text
  change (already preserved as printed in page 572 / librodm.txt).
  permitted words.txt: +2 (1276→1278) — "dicípulos", "perserverancia"
  (both pptext-flagged this run, added per rule 10 regardless of
  verdict); "masetros" already present (page 571). NOT logged (checked,
  cleared): Moroni 3:4 "residía" (1886 also "residía", correct Spanish,
  used correctly elsewhere e.g. Éther 12:6); "Élderes"/"Élder" (1886
  also "Élderes"/"Élder", established BoM transliteration); 1920↔1886
  accent-drop differences (1886 house style, hundreds of cases). Whole-
  document sweeps all re-ran clean (check_spaced_punctuation librodm.txt
  32353, check_footnote_punctuation librodm_foot.txt 4882,
  check_verse_indent librodm.txt, curly-quote scan of both master files
  zero). `permitted words.txt`: net +2 (1276→1278). `errors in
  1920.txt`: net +5 (890→895) — Moroni 3:1, 3:3, 3:4, Footnote Moroni
  4:3, and the back-filled Mormón 8:38.

- **2026-08-30**: Sessions A–E run in one session for page 617
  (Moroni 5:1-2 and Moroni 6:1-7), first footnote 4549, chapter 5's
  single letter "a" and chapter 6's letters a-h. Page CONTINUES the
  Book of Moroni. Page 616 ended Moroni 4:3 (end of Moroni 4), so page
  617 OPENS with a chapter heading "CAPÍTULO 5." — "Página 617"
  separated from it by a blank line (rule 1); running header
  ("CAP. V, VI.)  LIBRO DE MORONI.  617") discarded. NO book-title
  header (still within Moroni). Moroni 5 is COMPLETE here (vv.1-2 only,
  a very short chapter), then "CAPÍTULO 6." (no subtitle — image
  checked), then Moroni 6 vv.1-7 ending MID-verse-7
  ("...á cualesquiera que se les encontraban") which carries to page
  618. Decorative rules before ch.5, between ch.5 and ch.6, and after
  ch.6 v.7 (none transcribed). In the footnote block the two chapters
  keep SEPARATE groups split by a short centered rule: Moroni 5's lone
  "5a" above, Moroni 6's a-h below (short rule not transcribed). 32
  body print lines. ONE hyphen split (rule 7): "ninguna ini-"/"quidad"
  → "iniquidad" stays on line 31 (= 61 chars < 73), "quidad" consumed;
  line count stays 32. Rule 8: no rebalancing (longest marker line =
  Moroni 5:2 "de la [4549]sangre..." = 71). Rule 31: space-before-";"/
  ":" removed ×6 body + spaced colons/semicolons in fn block. Rule 6:
  sentence double-spacing collapsed; ONE narrow-space pair reported to
  editor (Moroni 6:4 "de la Iglesia", printed tight / Google "dela";
  1886 file p.631 prints "de la iglesia" as two words → two-word
  transcription confirmed). 9 markers: 5a=[4549] "sangre" (5:2);
  6a=[4550] "Élderes", 6b=[4551] "Presbíteros", 6c=[4552] "bautizados"
  (all 6:1); 6d=[4553] "nombre" (6:3); 6e=[4554] "poder" (6:4);
  6f=[4555] "oración" (6:4); 6g=[4556] "ayunar" (6:5); 6h=[4557]
  "participar" (6:6). MANDATORY i/l/1 check NOT triggered (letters 5:a,
  6:a-h; cross-ref targets t×2, c, u, e×2, y, b — no i/l/1).
  Discretionary 1879 checks (file pp.618-619, Moroni 5-6 fn blocks):
  5a "Véase t, III Nefi 18" = 1879 "a, see t, III. Nep. 18." (short
  crossbarred "t"); 6c "Véase u, II Nefi 9" = 1879 "c, see u, II. Nep.
  9." (rounded "u"); 6g "Véase t, Mosíah 27" = 1879 "g, see t, Mos.
  27." 6e cross-ref letter INITIALLY read "v" from the fn_zoom crop —
  CORRECTED to "y" on 40x ultra-zoom (clear italic-y descender hooking
  left below the baseline) + 1879 file p.619 "e, see y, III. Nep. 9." +
  decisive content-fit (III Nefi 9y, seq. 3585, is the Holy-Ghost /
  baptism-of-fire footnote; III Nefi 9v = "III Nefi 15:2-8" does not
  fit "poder del Espíritu Santo"). 1879's Moroni 6 block has 11 entries
  (a-k); 1920's 8 (a-h) match position-for-position, 1879's extra i/j/k
  have no 1920 equivalent. Session B: fresh fn/1879/body-marker crops,
  all 9 entries + markers confirmed; "entre les del pueblo" (6:4)
  re-confirmed as "les". Session C: insert_body_text.py 617 —
  librodm.txt 32353→32393 (+40); librodm_foot.txt 4882→4891 (9 Block 1
  entries, NO blank line / NO book header — Moroni chs.4→5→6 same book,
  rule 20). Session D: generate_block2.py 617 — 9 Block 2 entries
  appended, NO spurious duplicate this run (5a's Block 1 entry does not
  wrap). But NEW generate_block2.py bug class: 5a "Véase t, III Nefi
  18; Doctrinas y Convenios 20:79; 27:2-4." is a COMPOUND entry
  (cross-ref + trailing refs); the script grabbed "27" from the
  trailing "27:2-4" as the cross-ref chapter, matched III Nefi "27t"
  (= seq 3972) and silently DROPPED the D&C text, emitting
  "4549: Véase 3972." → fixed by hand to
  "4549: Véase 3773; Doctrinas y Convenios 20:79; 27:2-4." (3773 =
  III Nefi 18t, same target as page 616's 4a/4d). Other cross-refs
  resolved OK: 4551→1141 (Mosíah 6c), 4552→378 (II Nefi 9u), 4553→1131
  (Mosíah 5e), 4554→3585 (III Nefi 9y), 4555→783 (II Nefi 32e),
  4556→1559 (Mosíah 27t), 4557→3755 (III Nefi 18b); 4550 direct.
  librodm.txt 32393→32402. Anchor↔Block-2 cross-check after fix: max
  anchor 4557 = max def 4557, contiguous 1..4557, no dupes; only the
  documented Jacob 2:15/812 gap ("defined but no anchor: [812]")
  remains. Session E: fresh pptext report_wsl_20260830.html walked end
  to end. NOTHING page-617 in Spellcheck / Edit Distance / scanno /
  curly-quote / "full stop followed by unexpected sequence"; page-617
  hits are all structural (short-lines flood; "4549 ... 27:2-4" legit
  verse-range hyphen; "[4550]Élderes" starting a wrapped line in the
  footnote-check line-start bucket; Moroni 6:7's mid-sentence
  page-boundary line in "query: unexpected paragraph end", clears when
  page 618 is integrated). ONE entry added to errors in 1920.txt
  (895→896): Moroni 6:4 "les" (los) in "entre les del pueblo de la
  Iglesia de Cristo" — 1886 file p.631 "entre LOS del pueblo de la
  iglesia de Cristo" (and 1886 Moroni 6:7 likewise "los"); "entre les
  del pueblo" is ungrammatical (sense needs demonstrative "los"; "les"
  is only an IO clitic); modern BoM "los"; Google OCR page_0639.txt
  also reads "les"; 1920-only error, preserved as printed. NOT added to
  permitted words.txt ("les" is valid, aspell-accepted, never pptext-
  flagged → no-op). `permitted words.txt`: net +1 (1278→1279) —
  "Élder" (singular), pptext Spellcheck-flagged this run at librodm.txt
  line 27436 (page 616's Moroni 4:1); established BoM term, no error,
  added per rule 10 (pre-existing gap — only plural "Elderes" was on
  the list). Whole-document sweeps all clean (check_spaced_punctuation
  librodm.txt 32402, check_footnote_punctuation librodm_foot.txt 4891,
  check_verse_indent librodm.txt, anchor↔Block-2 sweep, curly-quote
  scan of both master files zero). NOT promoted (checked, cleared):
  "Élderes" (6:1; 1886 also, established BoM term), "Jesu Cristo" (5:2;
  legitimate archaic form), "perfeccionador" (6:4; 1886 also, correct),
  archaic accented forms (house style, rule 32).

- **2026-08-30b**: Sessions A–E run in one session for page 618
  (Moroni 6:7-9 completing chapter 6, then Moroni 7:1-9), first
  footnote 4558, Moroni 6's letters i-k and Moroni 7's letters a-d.
  Page CONTINUES the Book of Moroni. Page 617 ended MID-Moroni-6:7
  ("...á cualesquiera que se les encontraban"), so page 618 OPENS
  mid-verse with NO blank line and NO chapter heading (rule 1) — first
  body line "cometiendo iniquidad, y hubiere [4558]tres testigos...".
  Running header "618  LIBRO DE MORONI.  (CAP. VII." discarded. NO
  book-title header (still Moroni). Moroni 6 COMPLETES here (vv.7-9),
  then a decorative rule, then the heading "CAPÍTULO 7." (1920 prints a
  SPURIOUS PERIOD after "CAPÍTULO" — see errors log; transcription
  normalizes to "CAPÍTULO 7."), then Moroni 7 vv.1-9 ending MID-verse-9
  ("...si un hombre ruega, y no lo hace con") which carries to page
  619. Decorative rules before "CAPÍTULO 7." and above the fn divider
  (none transcribed). In the fn block the two chapters keep SEPARATE
  groups split by a short centered rule: Moroni 6's tail i-k above,
  Moroni 7's a-d below. 39 body print lines + 1 heading. FOUR hyphen
  splits (rule 7), all rejoined and kept at line end (<73):
  "condema-"/"ban" -> "condemaban" (70), "her-"/"manos" -> "hermanos"
  (59), "voca-"/"ción" -> "vocación," (72, exactly at limit),
  "verda-"/"dera" -> "verdadera" (65). Rule 8: no rebalancing. Rule 31:
  space-before-";"/":" removed x10 body + spaced colons/semicolons in
  fn block. Rule 6: sentence double-spacing collapsed; NO narrow-space
  word-pairs. 7 markers: 6i=[4558] "tres" (6:7), 6j=[4559] "pronto"
  (6:8), 6k=[4560] "poder" (6:9), 7a=[4561] "relativas" (7:1),
  7b=[4562] "sinagoga" (7:1), 7c=[4563] "don" (7:2), 7d=[4564] "Por"
  (7:5). ANOMALY — 6i's footnote-block superscript label "i," is
  MISSING from the 1920 print (entry text "Doctrinas y Convenios
  42:80,81." starts at the paragraph indent with no letter; confirmed
  16-22x + Google OCR of page 0640, which also shows no letter there
  but does show "i," before "Mosíah"). This CORRECTS page 617's Session
  A conclusion that "1920 carries fewer footnotes here" — 1920 Moroni 6
  DOES have a-k; i-k simply fell at the top of page 618's fn block.
  Identity of the unlabelled entry as 6i is certain: body marker "i" at
  6:7 present; sequence h(p617)->i->j->k; 1879 (Pratt, file p.619,
  Moroni ch.6) i = "Doc. and Cov. 42:80,81" exact content match. Logged
  in errors in 1920.txt. MANDATORY i/l/1 check — resolved against 1879
  file p.619 (Moroni 6 d-k and 7 a-c fn blocks): 1879 Moroni 6
  i="Doc. and Cov. 42:80,81", j="Mos. 26:31", k="see c, Moro. 3";
  1879 Moroni 7 a=verse groups + "Ether 12:3-37; Moro. 8:14,26;
  10:20-23", b="see u, Alma 16", c="III. Nep. 5:13. See j, III. Nep. 5.
  See q, IV. Nep. 1." This confirms 6j IS "j" not "i" (the small
  italic superscript j — dot + below-baseline hook — which Google OCR
  misreads as "i" at both 6j and 7c's "Véase j"), and 7c's first
  cross-ref IS "Véase j, III Nefi 5" (content-fit: III Nefi 5j, seq.
  3485, "Probablemente uno de los sucesores de los Doce Discípulos" <->
  "el don de mi vocación"). 7c's second cross-ref: 1920 "Véase e, IV
  Nefi 1" vs 1879 "See q, IV. Nep. 1" — rule-26 word-order letter
  difference, 1920's "e" kept. Session B: fresh fn/1879/body-marker
  crops; all 7 entries + markers confirmed. NEW ITEM found in Session
  B — Moroni 7:1 "constrúido": a small mark over the "u" of
  "construido"; per rule 36 Google OCR of page 0640 reads "construido"
  plain (checked first) and the mark is lighter than genuine same-page
  acutes -> stray speck, transcribed "construido", NOT logged (Session
  E 1886 file p.632 corroborates: "construido" plain). Session C:
  insert_body_text.py 618 — librodm.txt 32402->32446 (+44: 39 body
  lines + 1 heading + "Página 618" + separators); librodm_foot.txt
  4891->4899 (7 Block 1 entries on 8 lines — 7a wraps; NO blank line /
  NO book header, Moroni 6->7 same book, rule 20). Session D:
  generate_block2.py 618 appended Block 2 4558-4564, BUT (a) the
  wrapped-Block-1-entry bug fired again (7a/4561 wraps to "10:20-23.")
  — the script emitted a spurious trailer after 4564 (blank line,
  "PRIMER LIBRO DE NEFI", blank line, bogus "7: II Crónicas 36:16."
  duplicating the real footnote-7 def) -> removed by hand; librodm.txt
  ends cleanly at "4564: III Nefi 14:15-20." (32454); (b) the
  compound-cross-ref bug (same class as page 617's 4549): 4563 left in
  letter form "III Nefi 5:13; Véase j, III Nefi 5; Véase e, IV Nefi 1."
  -> resolved by hand to "4563: III Nefi 5:13; Véase 3485; Véase 4033."
  (3485 = III Nefi 5j, 4033 = IV Nefi 1e). Script-resolved OK:
  4560->4543 (Moroni 3c), 4562->2046 (Alma 16u); 4558/4559/4561/4564
  direct. Anchor<->Block-2 after fixes: max anchor 4564 = max def 4564,
  contiguous 1..4564, no gaps/dupes; only the documented Jacob 2:15/812
  gap remains. Session E: fresh pptext report_wsl_20260830b.html walked
  end to end; 1886 comparison against file p.631 (Moroni 6) and file
  p.632 (Moroni 7:1-5). TRANSCRIPTION MISREAD CORRECTED — Moroni 6:8
  "ó" -> "é": Sessions A/B read the conjunction between "arrepintían,"
  and "imploraban" as "ó" (or) on a heavy-ink glyph; a fresh 34x crop
  shows an unmistakable "e" (mid crossbar, open lower-right lobe), NOT a
  closed "o" bowl — it is "é imploraban" (archaic-accented "e" = "and",
  house style), matching Google OCR ("é"), 1886 file p.631 ("é
  imploraban"), 1879 English ("and"), and modern BoM Moroni 6:8 ("y").
  Corrected in page_618.txt + librodm.txt; NOT a 1920 error (1886
  concurs), logged as a Session-E transcription fix (rule 12), same
  class as the page 442 "al/el" and page 504 "habéis/habeís"
  precedents. The same-page "ó" at 6:9 ("suplicar, ó cantar") and 7:6
  ("ó una oración") ARE genuine closed-bowl "ó" (= "or"), 1886/modern
  concur — no change. errors in 1920.txt: FIVE entries added
  (896->901), in Moroni verse/apparatus order: (0) Footnote Moroni 6:i
  missing footnote-block label (above); (1) Moroni 6:7 "condemaban"
  (condenaban) — 1886 file p.631 "condenaban", RAE no "condemar" (only
  "condenar" < Lat. condemnare), corpora "condenaban" 1 / "condemaban"
  0, modern BoM "eran condenados", 1879 "condemned", pptext Spellcheck-
  flagged; 1920-only; (2) Moroni 6:8 "arrepintían" (arrepentían) — 1886
  file p.631 ALSO "arrepintían" (shared translation-lineage error, cf.
  Helamán 7 encabezado "arrepiéntese"), not a valid conjugation (the
  same page prints "arrepentían" correctly at 6:7), no dictionary/
  corpus/modern support, modern BoM "se arrepentían", pptext Spellcheck
  + Edit-Distance flagged; error shared with 1886; (3) Moroni 6:9
  "obrabran" (obraban) — 1886 file p.631 ALSO "obrabran" (shared),
  non-existent verb "obrabrar", corpora "obraban" 1 / "obrabran" 0,
  modern reworded ("así se hacía"), 1879 "so it was done", pptext
  Spellcheck-flagged; error shared with 1886; (4) Moroni 7 heading
  "CAPÍTULO. 7." spurious period after "CAPÍTULO" — 1886 file p.631 and
  1920 pages 616-617 all clean "CAPÍTULO N.", 1920-only typesetting
  defect, transcription normalizes to standard "CAPÍTULO 7." (no text
  affected), logged for the record. permitted words.txt: net +3
  (1279->1282) — "condemaban", "arrepintían", "obrabran" (all pptext-
  flagged, added per rule 10). NOT promoted (checked, cleared):
  "construido" (7:1, 1886 concurs, not flagged); "arrepentían" (6:7,
  correct); Moroni 7:2 "el Padre y nuestro Señor" (1886 "el Padre DE
  nuestro" — translation-lineage variant, 1920's "y" matches modern BoM
  better, not an error, noted for editor); "Jesu Cristo" (legit
  archaic, feedback_jesu_cristo_hyphen); "discípulos"/"recuerdo" (7:3,
  7:5, correct). Narrow-space pairs: NONE this page. Full pptext
  walkthrough: page-618 hits are all structural (short-lines flood incl.
  wrapped "10:20-23."; dash-check digit-flanked verse ranges in 4561/
  4564; "query: unexpected paragraph end" on page 618's mid-sentence
  last line, clears when 619 is integrated); NOTHING page-618 in
  repeated-word / duplicate-lines / ellipsis / scanno / curly-quote /
  special-situations / book-level / "full stop followed by unexpected
  sequence". Whole-document mechanical sweeps all clean
  (check_spaced_punctuation librodm.txt 32454, check_footnote_
  punctuation librodm_foot.txt 4899, check_verse_indent librodm.txt,
  anchor<->Block-2 sweep [only 812 remains], curly-quote scan of both
  master files zero). Net: page_618.txt + librodm.txt one char each
  ("ó"->"é"); permitted words.txt 1279->1282; errors in 1920.txt
  896->901.
- **2026-08-30c**: Sessions A–E run in one session for page 619
  (Moroni 7:9 tail + vv.10-19), first footnote 4565, Moroni 7's
  letters e-h. Page CONTINUES the Book of Moroni and CONTINUES Moroni
  7. Page 618 ended MID-7:9 ("...no lo hace con"), so page 619 OPENS
  mid-verse with NO blank line, NO chapter heading, NO subtitle, NO
  book header (rule 1); running header discarded. Page ends MID-7:19
  ("...lo bueno de lo malo;") -> page 620. Centered decorative rule
  above the fn divider (not transcribed). 44 body print lines, 0
  heading. NO hyphen splits (rule 7 N/A). Rule 8: no rebalance
  (longest output line = 7:19 line 2 at 72, exactly the cap). Rule 31:
  x16 body semicolons de-spaced + fn-block spaced colons ("14 : 2" ->
  "14:2"; "8 : 19" -> "8:19", the latter confirmed a colon not a
  semicolon by Google OCR "8: 19" and 1879 "Mor. 8 : 19."). Rule 6:
  sentence double-spacing collapsed; NO narrow-space pairs (Google OCR
  of page 0641 keeps the same word boundaries; only routine fusion
  "he aqui"->"heaqui"). 4 markers: 7e=[4565] "todo" (7:12); 7f=[4566]
  "no" (7:14); 7g=[4567] "todo" (7:16); 7h=[4568] "juzgueis" (7:18).
  The 1920 fn block on this page is heavily over-inked/blotchy and its
  swash entry/cross-ref letters are individually hard to read -- used
  the Section 8 provisional-sequence + content-fit + 1879 cross-check
  (discretionary path; MANDATORY i/l/1 NOT triggered -- entry letters
  e-h, cross-ref targets o/o/f). Fresh 1879 crops file pp.620-621:
  Book of Moroni ch.7 "e, see o, Ether 4. / f, ver. 18. III. Nep.
  14 : 2. Mor. 8 : 19. / g, see o, Ether 4. / h, see f." -- 1920's
  7e-7h match one-for-one in target content. Block 1: 7e/7g "Vease o,
  Ether 4."; 7f "Versiculo 18; III Nefi 14:2; Mormon 8:19."; 7h "Vease
  f." (1879 prints f's citations period-separated; transcribed as
  1920's semicolons, rule 21.) STRAY MARK (rule 36) -- Moroni 7:11
  "que. si": raised middot between "que" and "si"; Google OCR of page
  0641 reads "que si" with no mark (checked first) + dot lighter than
  same-line punctuation -> stray speck, transcribed "que si", NOT
  logged. Session B: fresh fn-block crop (6x) + body-marker crops
  (9-11x) -- all 4 entries and markers confirmed UNCHANGED; 1879
  cross-check re-affirmed. Session C: insert_body_text.py 619 --
  librodm.txt 32454->32500 (+46); librodm_foot.txt 4899->4903 (4 Block
  1 entries, NO blank line / NO book header, Moroni ch.7 continues,
  rule 20). Session D: generate_block2.py 619 appended 4565-4568
  (librodm.txt 32500->32504) -- NO wrapped-Block-1-entry bug this run
  (all 4 entries one line each; Notas tail ends cleanly at "4568:
  Vease 4566."). Cross-refs: 4565 & 4567 -> 4352 ("4o, 4352: Moroni
  7:5-22; 10:6-7." -- Ether 4's note o, whose content is a RECIPROCAL
  cross-ref back to Moroni 7:5-22, i.e. exactly where 7e/7g sit --
  independently confirms the 1920 letter "o"); 4568 -> 4566 (7h "Vease
  f" -> 7f); 4566 direct. Anchor<->Block-2 after append: max anchor
  4568 = max def 4568, contiguous 1..4568, no gaps/dupes; only the
  documented Jacob 2:15/812 gap remains. Session E: fresh pptext
  report_wsl_20260830c.html walked end to end; 1886 comparison vs
  Moroni 7 file p.632 (opening) + file p.633 (vv.13-18). errors in
  1920.txt: TWO entries added (901->903), after the "Moroni 7
  (encabezado)" entry: (1) Moroni 7:13 "sirvirle" (servirle) -- 1920
  prints the infinitive with "sirv-" stem; RAE: no "sirvir"
  (infinitive always "servirle"); corpora 0 hits for "sirvir*"
  infinitive vs well-attested "servirle" ("sirviendo" is the regular
  vowel-raising gerund, not the infinitive); Google OCR of page 0641
  also "sirvirle"; 1886 file p.633 ALSO "sirvirle" (SHARED lineage
  error, cf. 6:8/6:9); modern BoM "a servirle"; pptext Spellcheck +
  Edit-Distance flagged ("sirvirle(1):servirle(7)"). (2) Moroni 7:18
  "equivocamente" (equivocadamente) -- 1920 drops the "-da-" syllable;
  "equivocamente" is not a Spanish word (adverb = "equivocado" +
  "-mente"; accented "equivocamente"/"equivocamente" from adj.
  "equivoco" is a different word, not printed here); Google OCR of
  page 0641 also "equivocamente"; 1886 file p.633 prints the full
  correct "equivocadamente" -- 1920-ONLY error; modern BoM
  "equivocadamente"; NOT pptext-flagged (logged on 1886/RAE/modern
  evidence regardless). permitted words.txt: net +1 (1282->1283) --
  "sirvirle" (pptext-flagged, rule 10); "equivocamente" NOT added
  (never pptext-flagged -- permitted-words entry would be a no-op,
  cf. "Jesu Cristo" precedent). NOT promoted: "obscuridad" (7:15,
  archaic house style, 1886 concurs), "Jesu Cristo" (7:11, legit
  archaic; 1886 hyphenates), "o" (7:14, archaic "or", 1886 concurs),
  "que." stray mark (above). Whole-document sweeps all clean
  (check_spaced_punctuation librodm.txt 32504, check_footnote_
  punctuation librodm_foot.txt 4903, check_verse_indent librodm.txt,
  anchor<->Block-2 [only 812 remains], curly-quote scan of both master
  files zero). Full pptext walkthrough: page-619 hits all structural
  (short-lines flood incl. the short Block-2 "Vease 4352." entries; no
  page-619 dash / repeated-word / paragraph-level / scanno /
  curly-quote / special-situations / book-level findings). NO text
  changes to page_619.txt or librodm.txt this session (both errors
  preserved as printed). Net: permitted words.txt 1282->1283; errors
  in 1920.txt 901->903.

- **2026-08-30d**: Sessions A–E run in one session for page 620
  (Moroni 7:19 tail + vv.20-29), first footnote 4569, Moroni 7's
  letters i-s (11 footnotes, 4569-4579). Page CONTINUES the Book of
  Moroni and CONTINUES Moroni 7. Page 619 ended MID-7:19 ("...lo bueno
  de lo malo;"), so page 620 OPENS mid-verse with NO blank line, NO
  chapter heading, NO subtitle, NO book header (rule 1); running header
  discarded. Page ends with 7:29 COMPLETE ("...entre los hijos de los
  hombres.") → page 621 opens "30.". Centered decorative rule above the
  fn divider (not transcribed). 43 body print lines, 0 heading. Rule 7:
  5 hyphen splits rejoined — "cierta-/mente", "mani-/festaba",
  "sal-/varon", "mila-/gros" kept on line 1 (all <73); "eterna-/mente"
  rejoined = 73 exactly → "eternamente" moved to start of next line.
  Rule 8: no rebalance (longest = line 8 at 72). Rule 31: ×10 body
  ";"/":" de-spaced + fn-block "18 : 20" → "18:20" (7n). Rule 6: ×6
  justification double-spaces collapsed; NO narrow-space pairs. Rule 23:
  7s "30-32, 36, 37" → "Versículos 30-32,36-37" (36,37 consecutive →
  range). 11 markers: 7i=[4569] "fe" (7:21); 7j=[4570] "conoce" (7:22);
  7k=[4571] "siendo" (7:22); 7l=[4572] "nada" (7:24); 7m=[4573] "fe"
  (7:25); 7n=[4574] "Todo" (7:26); 7o=[4575] "reclamar" (7:27);
  7p=[4576] "fe" (7:28); 7q=[4577] "defiende" (7:28); 7r=[4578] "¿Han"
  (7:29); 7s=[4579] "cesado" (7:29). fn block heavily over-inked (same
  as p619); full 1879 cross-check on every entry (MANDATORY i/l/1
  TRIGGERED by entry letters "i" and "l" — both confirmed vs 1879 file
  p.621 "i, see a." / "l, see b and c, II. Nep. 2."). Fresh 1879 crops
  file pp.621-622: ch.7 "i, see a. / j, see r, II. Nep. 9. / k, see a,
  Mos. 3. / l, see b and c, II. Nep. 2. / m, see a. / n, III. Nep.
  18:20. / o, see e, II. Nep. 2. / p, see a. / q, see e, II. Nep. 2. /
  r, see r, II. Nep. 26. / s, vers. 30-32, 36, 37." — 1920's 7i-7s
  match one-for-one in target content. Block 1: 7i/7m/7p "Véase a.";
  7j "Véase r, II Nefi 9."; 7k "Véase a, Mosíah 3."; 7l "Véase b, y c,
  II Nefi 2."; 7n "III Nefi 18:20."; 7o/7q "Véase e, II Nefi 2."; 7r
  "Véase r, II Nefi 26."; 7s "Versículos 30-32,36-37." OVER-INKING NOT
  a marker (rules 14/15): Moroni 7:22 "Cristo ĥa de venir" — ink mark
  fused to the "h" ascender; 1879 has no marker there, 1920 block has
  exactly 11 entries = 11 clean markers; transcribed "ha" plain, NOT
  logged. Session B: fresh fn-block crop (6x) + body-marker crops
  (7-10x) + fresh 1879 pp.621-622 — all 11 entries and markers
  UNCHANGED; MANDATORY i/l/1 re-affirmed. Session C: insert_body_text.py
  620 — librodm.txt 32504→32549 (+45); librodm_foot.txt 4903→4914 (11
  Block 1 entries, NO blank line / NO book header, Moroni ch.7
  continues, rule 20). Session D: generate_block2.py 620 appended
  4569-4579 (librodm.txt 32549→32560) — NO wrapped-Block-1-entry bug.
  Cross-refs: 7i/7m/7p → 4561 (Moroni 7a, the faith passage —
  reciprocal fit); 7j → 375 (II Nefi 9r); 7k → 1096 (Mosíah 3a); 7l →
  "Véase 261 y 262" (II Nefi 2 notes b & c — compound form; script
  prints a spurious "unresolved" warning but the appended entry is
  fully numeric and matches the "Véase N y M." convention, no hand-fix);
  7o/7q → 264 (II Nefi 2e, whose own content cites "Moroni 7:27-28" —
  reciprocal, independently confirms letter "e"); 7r → 671 (II Nefi
  26r); 7n/7s direct. Anchor↔Block-2 after append: max anchor 4579 =
  max def 4579, contiguous 1..4579, no gaps/dupes; only the documented
  Jacob 2:15/812 gap remains. Session E: fresh pptext
  report_wsl_20260830d.html walked end to end; 1886 comparison vs
  Moroni 7 file pp.633-634 (vv.13-27). errors in 1920.txt: TWO entries
  added (903→905), plain append after "Moroni 7:18 equivocamente":
  (1) Moroni 7:24 "habían" (había) — 1920 pluralizes existential
  "haber" ("habían diferentes vías"); RAE: impersonal haber always
  singular; 1886 file p.633 has singular "había diferentes vias";
  matches III Nefi 15:2 / 18:13 precedent; modern BoM rephrases; Google
  OCR also "habían"; NOT pptext-flagged; not shared with 1886 at this
  spot (though "habían muchos..." recurs in earlier un-audited pages).
  (2) Moroni 7:27 "mios" (míos) — dropped accent on postposed
  possessive; 1920 internal 118× "míos" vs 2× "mios" (this + one
  un-audited II Nefi 9:40); RV1909 NT 3:0 for "míos"; modern BoM
  "amados hermanos míos"; 20x zoom confirms no accent (vs genuine "í"
  in "aquí" one line up); Google OCR normalizes to "míos"; 1886 file
  p.634 ALSO "mios" (and at 7:14) but 1886 drops accents pervasively;
  NOT pptext-flagged. permitted words.txt: NO change (1283→1283) —
  neither word pptext-flagged (no-op, cf. p619 "equivocamente"). NOT
  promoted: "os aceptáis" (7:19, 1886 also "si os aceptais" — shared,
  not an error), "posible" (7:20, standard; 1886 concurs), "Jesu
  Cristo" (7:26, legit archaic; 1886 hyphenates), "¿Cómo"/"¿Han"
  (capital after ¿, house style; 1886 same), v22 "ĥa" over-inking
  (above), terminal "hombres." (Google "T" = margin speck, resolved
  Session A). Whole-document sweeps all clean (check_spaced_punctuation
  librodm.txt 32560, check_footnote_punctuation librodm_foot.txt 4914,
  check_verse_indent librodm.txt, anchor↔Block-2 [only 812], curly-quote
  scan of both master files zero, letter-hyphen-letter scan of p620
  additions — no new compounds). Full pptext walkthrough: page-620 hits
  all structural (short-lines flood incl. short Block-2 "Véase 4561."
  etc.; dash-check 4579 "30-32,36-37" legit rule-23 ranges); no
  page-620 spellcheck / edit-distance / repeated-word / duplicate-line /
  ellipsis / footnote / scanno / curly-quote / spaced-punctuation /
  special-situations / book-level / paragraph-level / Jeebies findings.
  NO text changes to page_620.txt or librodm.txt this session (both
  errors preserved as printed). Net: permitted words.txt 1283→1283;
  errors in 1920.txt 903→905.
- **2026-08-31**: Sessions A–E run in one session for page 621
  (Moroni 7:30-39 partial), first footnote 4580, Moroni 7's letters
  t-z + 2a-2e (12 footnotes, 4580-4591). Page CONTINUES the Book of
  Moroni and CONTINUES Moroni 7. Page 620 ended with 7:29 COMPLETE, so
  page 621 OPENS with verse 30 as continuous-paragraph flow: NO blank
  line after "Página 621", NO chapter heading, NO subtitle, NO book
  header (rule 1); running header "CAP. VII.)  LIBRO DE MORONI.  621"
  discarded. Page ends MID-verse 39 ("...porque supongo que tenéis fe
  en Cristo") → page 622 opens with the next word. 41 body print
  lines, 0 heading. Rule 7: 3 hyphen splits rejoined — "pre-/parar" →
  "preparar" (kept line 1, 65), "testi-/monio" → "testimonio" (kept
  line 1, 66), "igual-/mente" → "igualmente" (rejoined = 73 exactly
  WITH the [4591] marker → "igualmente" moved to start of next line,
  rule 8). Rule 8: no other rebalance (longest = 71, v.32). Rule 31:
  ×10 body ";"/":" de-spaced (1920 sets a space before punctuation
  throughout this page). Rule 6: v.32 justification double-space "las
  [4581]alianzas" collapsed. 12 markers: 7t=[4580] "Santo" (7:32);
  7u=[4581] "alianzas" (7:32); 7v=[4582] "Arrepentíos" (7:34);
  7w=[4583] "bautizáos" (7:34); 7x=[4584] "con" (7:35); 7y=[4585]
  "días" (7:35); 7z=[4586] "cesado" (7:36); 7-2a=[4587] "retirado"
  (7:36); 7-2b=[4588] "fe" (7:37); 7-2c=[4589] "ángeles" (7:37);
  7-2d=[4590] "causa" (7:37); 7-2e=[4591] "fe" (7:38). Fresh 1879
  crops file pp.622-623: ch.7 "t, see y, III. Nep. 9. / u, see j,
  III. Nep. 15. / v, III. Nep. 27:20. Ether 4:18. / w, see u, II.
  Nep. 9. / x, see g, II. Nep. 33. / y, see r, II. Nep. 26. / z, see
  s. / 2a, I. Nep. 10:17-19. II. Nep. 28:4. Moro. 10:4,5,7,19,24-27. /
  2b, see a. / 2c, see s. / 2d, ver. 38. Moro. 10:19,23-27. / 2e, ver.
  37. See 2d." — 1920's 7t-7-2e match one-for-one; 1879 body markers
  on file pp.622-623 confirm every marker word placement. MANDATORY
  i/l/1-class check TRIGGERED by Google OCR: Google's text layer reads
  7u's cross-reference letter as "i" ("Véase i, III Nefi 15"), but
  1879 p.622 unambiguously prints "u, see j, III. Nep. 15." (dot ABOVE
  + descender hook below the baseline = "j", not a dotless-descender
  "i"); the 1920 glyph matches "j"; resolved 7u = "j" (Google misread,
  rule 14). Block 1: 7t "Véase y, III Nefi 9."; 7u "Véase j, III Nefi
  15."; 7v "III Nefi 27:20; Éther 4:18."; 7w "Véase u, II Nefi 9.";
  7x "Véase g, II Nefi 33."; 7y "Véase r, II Nefi 26."; 7z "Véase
  s."; 7-2a "I Nefi 10:17-19; II Nefi 28:4; Moroni 10:4-5,7,19,24-27."
  (rule 23/24: "4,5"→"4-5"); 7-2b "Véase a."; 7-2c "Véase s."; 7-2d
  "Versículo 38; Moroni 10:19,23-27."; 7-2e "Versículo 37; Véase 2d."
  (rule 16: two-letter codes 7-2a…7-2e joined with a hyphen; "Véase
  2d" same-chapter cross-ref keeps the bare form, cf. footnote 772).
  check_google_crosscheck: only the two v.35 em-dashes surface (Google
  renders "—" as "-" which the check strips) — not a misread; Google
  body text otherwise matches line-for-line. Session B: fresh 1920
  fn-block crops (thirds) + fresh 1920 body-marker crops (5x) + the
  Session-A 1879 crops — all 12 entries and markers UNCHANGED;
  MANDATORY i/l/1 re-affirmed (7u = "j"). Session C:
  insert_body_text.py 621 — librodm.txt 32560→32603 (+43);
  librodm_foot.txt 4914→4926 (12 Block 1 entries, NO blank line / NO
  book header, Moroni ch.7 continues, rule 20). Session D:
  generate_block2.py 621 appended 4580-4591 (librodm.txt
  32603→32615) — no unresolved warnings, no wrapped-Block-1-entry
  bug. Cross-refs: 7t→3585 (III Nefi 9y); 7u→3702 (III Nefi 15j);
  7w→378 (II Nefi 9u); 7x→790 (II Nefi 33g); 7y→671 (II Nefi 26r —
  same target as page 620's 7r); 7z/7-2c→4579 (Moroni 7s, same
  chapter); 7-2b→4561 (Moroni 7a, the faith passage — reciprocal
  content-fit on "fe"); 7-2e "Véase 2d"→4590 (Moroni 7-2d); 7v/7-2a/
  7-2d direct. Anchor↔Block-2 after append: max anchor 4591 = max def
  4591, contiguous 1..4591, no gaps/dupes; only the documented Jacob
  2:15/812 gap remains. Session E: fresh full pptext report
  report_wsl_20260831.html walked end to end; 1886 comparison vs
  Moroni 7 file pp.634-635 — ALL of Moroni 7:30-39 compared
  word-for-word, NO 1920-only substantive deviation (every difference
  is 1886-archaic-accent vs 1920-modern-accent house style —
  fé/fe, segun/según, miéntras/mientras, entónces/entonces,
  redencion/redención, hé aquí/he aquí, hán/han, via/vía, cáusa/causa
  — plus minor connective-punctuation variation that is not an error
  in any edition: v.35 1920 em-dash where 1886 has a colon at the
  SECOND spot "verdaderas: y si", v.36 dash placement after
  "hombres?"). KEY: the v.35 FIRST em-dash ("verdaderas,--y Dios") is
  present in BOTH 1886 and 1920 — genuine print. "¿O han" / capital
  after "¿" (7:36) confirmed house style (1886 also "¿O hán … ¿há …
  ¿lo"). TEXT CHANGE this session: page 621's two v.35 em-dashes
  normalised from the "—" (U+2014) character to "--" (two ASCII
  hyphens) in BOTH page_621.txt and librodm.txt, per the established
  project convention (rules doc "Dash check"; page 475's Corrections
  log "left as '--' per existing project convention"; pptext
  recognises "--" as "the book's em-dash"). Transcription-formatting
  normalisation only — NOT an errors-in-1920 matter. Editor pointer
  (pre-existing, NOT touched): librodm.txt still has 6 BODY em-dashes
  typed as "—" instead of "--" (lines ~20739 "meditación—", ~20742
  "iniquidades—sucedió", ~23224 "saben—para", ~24204 "iglesia;—si",
  ~26051 "cosas—le", ~26956 "mí—fuente") — worth a one-pass "—"→"--"
  normalisation whenever convenient. errors in 1920.txt: NO change
  (905→905). permitted words.txt: NO change (1283→1283) — the only
  aspell-flagged page-621 body words ("bautizáos" v.34, "salvos"
  v.34) are ALREADY in permitted words.txt (lines 425, 295). Full
  pptext walkthrough: page-621 hits all structural (short-lines flood
  incl. short Block-2 "Véase NNNN." entries; dash-check hyphen-minus
  4587/4590 digit-flanked rule-23/24 verse ranges; dash-check
  "em-dash:" bucket listed the pre-fix "verdaderas,--y" line 27644,
  resolved by the "--" normalisation); NO page-621 spellcheck /
  edit-distance / repeated-word / duplicate-line / ellipsis /
  footnote-check / scanno / curly-quote / spaced-punctuation /
  special-situations / book-level / paragraph-level ("full stop
  followed by unexpected sequence" has no page-621 hit) / Jeebies
  findings. Whole-document mechanical sweeps all clean
  (check_spaced_punctuation librodm.txt 32615 + page_621.txt 5 hits
  all inside its Corrections log = historical quotes of the rule-31
  fixes; check_footnote_punctuation librodm_foot.txt 4926;
  check_verse_indent librodm.txt; anchor↔Block-2 [only 812];
  footnote-number duplicate/out-of-range/missing sweep max anchor
  4591 contiguous; curly-quote scan of both master files + page_621
  zero; letter-hyphen-letter scan of the page-621 body — no
  compounds). No narrow-space-vs-merge notes on this page. Net:
  librodm.txt em-dash normalisation (2 lines); permitted words.txt
  1283→1283; errors in 1920.txt 905→905.
- **2026-08-31b**: Sessions A–E run in one session for page 622
  (Moroni 7:39 tail + vv.40-48), first footnote 4592, Moroni 7's
  letters 2f-2k (6 footnotes, 4592-4597). Page CONTINUES the Book of
  Moroni and CONTINUES Moroni 7 — page 621 ended MID-7:39, so page
  622 OPENS mid-verse: NO blank line, NO chapter heading, NO subtitle,
  NO book header (rule 1); running header "622  LIBRO DE MORONI.
  (CAP. VII." discarded. Page ENDS Moroni chapter 7 ("...tal como Él
  es puro. Amén.") — Moroni 8 begins on page 623 (no CAPÍTULO VIII
  heading here). 38 body print lines, 0 heading. Rule 7: 1 hyphen
  split — "puri-/ficados" → "purificados" (rejoined = 82 ≥ 73 →
  rule 7/8 moves it to the next line). Rule 8: no other rebalance
  (longest 71, v.41). Rule 31: ×16 body ";" de-spaced. Rule 6: ×4
  sentence double-spaces collapsed (v.40/41/46/48); no zero-width
  merges. 6 markers: 7-2f=[4592] "esperanza" (7:40); 7-2g=[4593]
  "expiación" (7:41); 7-2h=[4594] "resucitados" (7:41); 7-2i=[4595]
  "caridad" (7:44); 7-2j=[4596] "seáis" (7:48); 7-2k=[4597] "tal"
  (7:48). Fresh 1879 read file p.623: "2f, see a. / 2g, see f, II.
  Nep. 2. / 2h, see d, II. Nep. 2. / 2i, see a. / 2j, III. Nep.
  27:27. / 2k, III. Nep. 19:28,29." — 1920's 2f-2k match one-for-one;
  1879 body markers on file p.623 confirm every marker word placement.
  MANDATORY i/l/1-class check TRIGGERED by entry letter "2i" [4595]:
  1879 p.623 prints "2i, see a." (short dotted stroke), matching body
  marker before "charity"; 1920 swash glyph matches — resolved 2i =
  "i". No i/l/1 in any cross-ref target (a, f, d, a; Google rendered
  the 2f/2i targets as a bare quote, an unread superscript). Block 1:
  7-2f/7-2i "Véase a."; 7-2g "Véase f, II Nefi 2."; 7-2h "Véase d,
  II Nefi 2."; 7-2j "III Nefi 27:27."; 7-2k "III Nefi 19:28-29."
  (rule 23: "28,29"→"28-29"; rule 16: two-letter codes hyphen-joined).
  STRAY MARK (rule 36) — raised dot over "causa" (7:39 opening):
  Google OCR page 0644 silent → stray speck, transcribed "causa"
  plain, NOT logged (1886 prints an intentional archaic accent
  "cáusa" here — 1886 house style, unrelated). check_google_
  crosscheck: 5 candidates, all benign — 4 × Google rendering
  capital "Él" as "El" (no accent on capital E; 1920 print has the
  accent, zoom-confirmed) + 1 × Google dropping standalone "á" in
  7:46 "uníos á la caridad" (zoom-confirmed printed). Session B:
  fresh 1920 fn-block crops (left/right halves) + fresh body-marker
  crops (v.40-41, v.48) + Session-A 1879 read — all 6 entries and
  markers UNCHANGED; MANDATORY i/l/1 re-affirmed (2i = "i"). Session
  C: insert_body_text.py 622 — librodm.txt 32615→32655 (+40);
  librodm_foot.txt 4926→4932 (6 Block 1 entries, NO blank line / NO
  book header, Moroni ch.7 continues, rule 20). Session D:
  generate_block2.py 622 appended 4592-4597 (librodm.txt
  32655→32661) — no unresolved warnings, no wrapped-Block-1-entry
  bug. Cross-refs (book-aware): 7-2f/7-2i "Véase a" → 4561 (Moroni
  7a, same target as page 621's 7-2b); 7-2g "Véase f, II Nefi 2" →
  265 (II Nefi 2f); 7-2h "Véase d, II Nefi 2" → 263 (II Nefi 2d);
  7-2j/7-2k direct. Anchor↔Block-2 after append: max anchor 4597 =
  max def 4597, contiguous 1..4597, no gaps/dupes; only the documented
  Jacob 2:15/812 gap remains. Session E: fresh full pptext report
  report_wsl_20260831b.html walked end to end; 1886 comparison vs
  Moroni 7 file pp.635-636 — ALL of Moroni 7:39-48 compared
  word-for-word. Every 1920/1886 difference is 1886-archaic-accent vs
  1920-modern-accent house style (fé/fe, mios/míos, teneis/tenéis,
  debeis/debéis, habeis/habéis, expiacion/expiación,
  resurreccion/resurrección, cáusa/causa, segun/según,
  corazon/corazón, dia/día, Amen/Amén) plus minor
  connective-punctuation variation not an error in any edition (v.42
  1886 colon vs 1920 ";"; v.43 1920's extra comma "vez, os digo," /
  "como,"; v.47 1886 "aquellos que lo posean" vs 1920 "aquéllos que
  la posean", pronoun agreeing with "la caridad"). TWO 1920 errors
  found in Moroni 7:45, BOTH also in 1886 (shared translation
  lineage), logged in errors in 1920.txt (905→907): (1) "facilmente"
  (fácilmente) — esdrújula, always accented (RAE); 1886 file p.636
  also "facilmente"; matches the documented Alma 7:15/46:8/59:3/59:9
  pattern; modern BoM "no se irrita fácilmente"; Google OCR page
  0644 also "facilmente"; already in permitted words.txt (line 738),
  NOT re-added. (2) "recocija" (regocija) — 1920 prints "no se
  recocija en la iniquidad, mas se regocija en la verdad" (wrong form
  first, correct second in the same clause); "recocijar" has no RAE
  entry; 0 corpora hits vs dozens for "regocija"; 1886 file p.636
  also "recocija … regocija" (same pattern as the documented III
  Nefi 27:30 entry); 1879 "rejoiceth not … but rejoiceth"; modern
  BoM "no se regocija en la iniquidad"; Google OCR page 0644 also
  "recocija"; already in permitted words.txt (line 1161), NOT
  re-added. permitted words.txt: NO change (1283→1283). errors in
  1920.txt: 905→907 (two Moroni 7:45 entries appended — plain append
  is correct book order, 7:45 > 7:27). Full pptext walkthrough:
  page-622 hits all structural (short-lines flood incl. short Block-2
  "Véase NNNN." entries; dash-check hyphen-minus 4597 "III Nefi
  19:28-29" digit-flanked rule-23 range); NO page-622 spellcheck
  (recocija / facilmente already suppressed) / edit-distance /
  repeated-word / duplicate-line / ellipsis / adjacent-dash /
  footnote-check (anchors 4590-4597 present, contiguous) / scanno /
  curly-quote / spaced-punctuation / special-situations / book-level /
  paragraph-level ("full stop followed by unexpected sequence" has no
  page-622 hit) / Jeebies findings. Whole-document mechanical sweeps
  all clean (check_spaced_punctuation librodm.txt 32661;
  check_footnote_punctuation librodm_foot.txt 4932; check_verse_indent
  librodm.txt; anchor↔Block-2 [only 812]; footnote-number
  duplicate/out-of-range/missing sweep max anchor 4597 contiguous;
  curly-quote scan of both master files + page_622 zero). Narrow-space
  word-pairs for the editor (two-word transcription committed; listed
  for a convenience image check): Moroni 7:44 "del Espíritu", "Santo
  que", "es el Cristo"; Moroni 7:48 "para que", "á ser". Net: no text
  changes to page_622.txt or librodm.txt (both Moroni 7:45 errors
  preserved as printed); librodm.txt 32615→32661; librodm_foot.txt
  4926→4932; permitted words.txt 1283→1283; errors in 1920.txt
  905→907.
- **2026-08-31c**: Sessions A–E run in one session for page 623
  (Moroni 8:1-10), first footnote 4598, Moroni 8's letters a-f (6
  footnotes, 4598-4603). Page CONTINUES the Book of Moroni and BEGINS
  Moroni chapter 8. Page 622 ENDED Moroni 7 ("...tal como Él es puro.
  Amén."), so page 623 OPENS fresh: blank line after "Página 623",
  then "CAPÍTULO 8." (blank line before/after, rule 3), then v.1. NO
  book header (Book of Moroni continues — did not restart), NO chapter
  subtitle (checked image; 1879/1886 print a chapter argument, 1920
  does not — house style, not logged). Running header "CAP. VIII.)
  LIBRO DE MORONI. 623" discarded (rule 2). Page 622 ended with the
  complete word "Amén." — no page-boundary word split (rule 10 N/A).
  Page ENDS at Moroni 8:10 ("...con sus niños pequeñitos.") — Moroni
  8 continues on page 624. 40 body print lines + the CAPÍTULO 8
  heading. Rule 7: 4 hyphen splits — "constante-/mente" →
  "constantemente" (rejoined onto line 9 = 73 ≥ 73, so rule 7/8 moves
  "[4598]constantemente" to the next line); "dis-/putas" → "disputas"
  (line 12, 66, kept); "consigui-/ente" → "consiguiente" (line 28,
  67, kept); "arre-/pentimiento" → "arrepentimiento" (line 35, 71,
  kept). Rule 8: no further rebalance (longest = 71, v.10 line 35).
  Rule 31: ×10 body ";"/":" de-spaced (1920 sets a space before
  ";"/":" throughout) + Block 1 8e "17 : 9-14" → "17:9-14" (rule 22),
  8f "23 ;" → "23;". Rule 24: Block 1 8f "Versículos 14, 23" →
  "14,23" (non-consecutive verses). Rule 6: ×3 sentence double-spaces
  collapsed (v.7 "punto. Y", v.8 "Dios. He", v.10 "pequeñitos. Y");
  NO true zero-width merges. 6 markers: 8a=[4598] "constantemente"
  (8:3); 8b=[4599] "bautismo" (8:5); 8c=[4600] "poder" (8:7);
  8d=[4601] "quitada" (8:8); 8e=[4602] "ley" (8:8); 8f=[4603]
  "solemne" (8:9). MANDATORY i/l/1-class check NOT triggered — entry
  letters a-f and cross-ref targets (8a→h, 8c→c, 8d→m, 8f→b)
  contain no i/l/1. Block 1: 8a "Véase h, II Nefi 31."; 8b
  "Versículos 9-26."; 8c "Véase c, Moroni 3."; 8d "Véase m, Mosíah
  3."; 8e "Génesis 17:9-14."; 8f "Versículos 14,23; Véase b."
  STRAY MARKS (rule 36): (1) Moroni 8:4 "entre vosotros" — raised
  speck over the gap after "entre"; Google OCR reads "entré" (picked
  up the speck) BUT 1886 file p.636 prints "entre vosotros" plain,
  grammar requires the preposition, and the mark is lighter/displaced
  vs genuine acutes — stray speck, transcribed "entre", NOT logged,
  flagged for editor. (2) Moroni 8:8 "los sanos" — speck between the
  two words; 1886 file p.637 "los sanos" two words; transcribed two
  words, NOT logged. Google-text cross-check page 0645: body matches
  letter-for-letter except the two specks + dropped superscripts (rule
  14); check_google_crosscheck candidates "entré" (speck) and
  "bautizeis" (zoom confirms "z", matches transcription) — no text
  change. Session B: fresh 1920 fn-block crop (7x) + fresh body-marker
  read + independent 1879 cross-check (Moroni 8 = 1879 file p.624).
  1879 p.624 fn block: "a, see h, II. Nep. 31. / b, vers. 9—26. / c,
  see c, Moro. 3. / d, see m, Mos. 3. / e, Gen. 17 : 9—14. / f,
  vers. 14, 23. See b." (1879 also has "g" for Moroni 8:11, which
  falls on 1920 page 624). 1879 body markers on p.624 confirm every
  placement (v.3 letter on "endurance"/1920's adverb "constantemente"
  — translation word-order, rule 26; v.5 "baptism", v.7 "power", v.8
  "taken"/"law", v.9 "solemn"). All 6 entries + 6 markers UNCHANGED.
  Session C: insert_body_text.py 623 — librodm.txt 32661→32706
  (+45); librodm_foot.txt 4932→4938 (6 Block 1 entries, NO blank
  line / NO book header — Moroni ch.8 continues within the Book of
  Moroni, rule 20). Session D: generate_block2.py 623 appended
  4598-4603 (librodm.txt 32706→32712) — no unresolved warnings, no
  wrapped-Block-1-entry bug. Cross-refs (book-aware): 8a "Véase h, II
  Nefi 31" → 775 (II Nefi 31h); 8c "Véase c, Moroni 3" → 4543
  (Moroni 3c); 8d "Véase m, Mosíah 3" → 1108 (Mosíah 3m — whose own
  citation list back-references "Moroni 8:8", reciprocal confirmation);
  8f "Véase b" → 4599; 8b/8e direct. Anchor↔Block-2 after append:
  max anchor 4603 = max def 4603, contiguous 1..4603, no gaps/dupes;
  only the documented Jacob 2:15/812 gap remains. Session E: fresh
  full pptext report report_wsl_20260831c.html walked end to end; 1886
  comparison vs Moroni 8 file p.636 (heading + vv.1-6) + file p.637
  (vv.6-10) — ALL of Moroni 8:1-10 compared word-for-word. Only
  routine 1886-archaic vs 1920-modern house-style differences (fé/fe,
  mio/mios, despues/después, circuncision/circuncisión,
  Jesu-Cristo/Jesu Cristo, dropped commas). THREE 1920 errors found in
  Moroni 8, logged in errors in 1920.txt (907→910): (1) Moroni 8:5
  "han habido" (ha habido) — impersonal "haber" pluralized to agree
  with "disputas"; RAE: impersonal haber always singular; same pattern
  as documented Moroni 7:24 / III Nefi 15:2 / III Nefi 18:13; 1886
  file p.636 "ha habido dis-putas" SINGULAR; modern BoM "ha habido
  disputas"; Google page 0645 also "han habido"; NOT pptext-flagged
  (both words valid) — 1920-only, not shared with 1886. (2) Moroni
  8:8 "concluida" (concluido) — participle made feminine after
  "haber" ("la ley de la circuncisión ha concluida"); RAE: participle
  invariable in compound tenses with haber; 1920 uses "concluido"
  after haber everywhere else; 1886 file p.637 "ha concluido en mi"
  (correct) — 1920-ONLY error; modern BoM reworded ("se ha
  abrogado"); Google page 0645 also "concluida"; valid Spanish word
  so aspell does not flag it — NOT added to permitted words.txt. (3)
  Moroni 8:9 "bautizeis" (bauticéis) — "-zar" verb keeps "z" before
  "e" + drops the "-éis" accent; RAE has no "bautizeis"; aspell flags
  it standalone but the full report does not list it
  (whole-document-suppression phenomenon, cf. pages 469-470's "Poi");
  0 corpora hits; 1920 mostly correct "bautic-" before e (bautices,
  bauticen ×6, bautice ×2) with sporadic "bautiz-" ("bautizen" 2
  Nefi 9:23 — already logged; "bautize" Mormón 9:23); 1886 file
  p.637 ALSO "bautizeis" (SHARED lineage error, same as documented 2
  Nefi 9:23); modern BoM "bauticéis"; 1879 "baptize"; Google page
  0645 also "bautizeis". ADDED to permitted words.txt (rule 10).
  permitted words.txt: 1283→1284 ("bautizeis"). errors in 1920.txt:
  907→910 (Moroni 8:5, 8:8, 8:9 appended in verse order — all >
  Moroni 7:45, page 623 = true end of file). NOT promoted: "Jesu
  Cristo" (8:2, legit archaic; 1886 hyphenates; pptext does not flag
  "Jesu"). Observed but NOT logged (per the error-904 policy for
  earlier unaudited pages): Éther 12:19 "Y han habido también
  muchos" in librodm.txt is the same existential-haber pluralization
  on an already-integrated earlier page — surfaced only as a
  short-lines coincidence, no check flags it as an error.
  Whole-document mechanical sweeps all clean
  (check_spaced_punctuation librodm.txt 32712;
  check_footnote_punctuation librodm_foot.txt 4938; check_verse_indent
  librodm.txt; anchor↔Block-2 [only 812]; curly-quote scan of
  librodm.txt / librodm_foot.txt / page_623.txt zero). Full pptext
  walkthrough: every page-623 hit is structural — the short-lines
  flood (verse-boundary wrapped body lines + short Block-2 "Véase
  NNNN." entries); NO page-623 spellcheck / edit-distance /
  repeated-word / duplicate-line / dash (only digit-flanked rule-23
  ranges "9-26" / "9-14") / scanno / curly-quote / spaced-punctuation
  / special-situations / paragraph-level ("full stop followed by
  unexpected sequence" no Moroni 8 hit) / book-level / Jeebies
  findings. NO text changes to page_623.txt or librodm.txt this
  session (all three Moroni 8 errors preserved as printed).

- **2026-09-01**: Sessions A–E run in one session for page 624 (Moroni
  8:11-22), first footnote 4604, Moroni 8's letters g-s (13 footnotes,
  4604-4616). Page CONTINUES the Book of Moroni and Moroni chapter 8,
  opening MID-CHAPTER: page 623 ended at Moroni 8:10 ("...con sus niños
  pequeñitos."), so page 624's body begins immediately with "11." on
  the first line — NO blank line after "Página 624", NO chapter
  heading, NO book header (rule 1). Running header "624  LIBRO DE
  MORONI.  (CAP. VIII." discarded (rule 2). Page 623 ended with the
  complete word "pequeñitos." — no page-boundary word split (rule 10
  N/A). Page ENDS mid-verse 22 ("...Porque el") — Moroni 8:22
  continues on page 625. 43 body print lines. Rule 7: 5 hyphen splits
  — "arre-/pentimiento," to "arrepentimiento," (rejoined onto line 2 =
  74 >= 73, so rule 7/8 moves "arrepentimiento," to the next line);
  "eterni-/dad." to "eternidad." (rejoined onto line 27 = 79 >= 73, so
  "eternidad." moves to its own next line, as printed);
  "con-/siguiente" to "consiguiente" (line 29, 65, kept);
  "miseri-/cordias" to "misericordias" (line 30, 61, kept);
  "pala-/bras;" to "palabras;" (line 38, 63, kept). Rule 8: no further
  rebalance (longest = 69, line 14). Rule 31: 12 body ";"/"!"
  de-spaced (1920 sets a space before ";" throughout, plus one "tales
  !" to "tales!"). Rule 6: 5 sentence double-spaces collapsed (v.11
  "bautizados. He", v.16 "arrepintiere. He", v.21 "fin. Lo" / "Dios.
  Escuchalas", v.22 "ley. Porque"); v.17 justification-widened gaps
  ("amor ;  y    todos ellos    son") normalized; NO true zero-width
  merges. Rule 21/22: Block 1 8g "III Nefi 12 : 2, 30 : 2." to "III
  Nefi 12:2; 30:2." (1920 comma between the two chapter refs, 1879
  period; normalized to a semicolon per rule 21 + the "I Nefi 1:13;
  3:18." pattern). Rule 24: 8o "Versiculos 20, 23" to "20,23"
  (non-consecutive). 13 markers: g=[4604] "la" (8:11); h=[4605]
  "desde" (8:12); i=[4606] "no" (8:14); j=[4607] "infierno" (8:14);
  k=[4608] "participantes" (8:17); l=[4609] "invariable" (8:18);
  m=[4610] "eternidad" (8:18, on "de eternidad" — 1879 "from (m)all
  eternity", rule 26); n=[4611] "todos" (8:19); o=[4612]
  "misericordia" (8:19); p=[4613] "expiacion" (8:20); q=[4614]
  "infierno" (8:21); r=[4615] "viven" (8:22); s=[4616] "aquellos"
  (8:22). MANDATORY i/l/1 check TRIGGERED (entry letters i, l present;
  8p target superscript ambiguous f-vs-j). Resolved against 1879:
  Moroni 8 footnotes span 1879 file p.624 (g) + file p.625 (h-s).
  1879 p.625 block reads one-for-one: "h, see d, Mos. 4. / i, see a,
  Moro. 7. / j, see k, I. Nep. 15. / k, see m, Mos. 3. / l, see d,
  Mor. 9. / m, see a, Mos. 3. / n, ver. 22. / o, vers. 20, 23. / p,
  see f, II. Nep. 2. / q, see k, I. Nep. 15. / r, ver. 19. / s, see
  j, Mos. 3." (1879 p.624: "g, III. Nep. 12:2. 30:2."). 8p target
  first read as "j" off the process_page fn_zoom, but a 14x-16x crop
  shows an italic "f" (curved ascender + left-hooking descender, NO
  dot) and 1879 confirms "f"; II Nefi 2f (#265) cites the atonement,
  content-fit for the marker on "expiacion". 8s target = "j"
  (dotted), 1879 confirms; Google OCR's "i" is the unreliable
  superscript weak spot. Reciprocal back-references confirm every
  "Vease": Moroni 7a->Moroni 8:14,26; Mormon 9d->Moroni 8:18; Mosiah
  3a->Moroni 8:18; Mosiah 3j->Moroni 8:22; Mosiah 3m->Moroni
  8:8,12,22. Block 1: 8g "III Nefi 12:2; 30:2."; 8h "Vease d, Mosiah
  4."; 8i "Vease a, Moroni 7."; 8j "Vease k, I Nefi 15."; 8k "Vease m,
  Mosiah 3."; 8l "Vease d, Mormon 9."; 8m "Vease a, Mosiah 3."; 8n
  "Versiculo 22."; 8o "Versiculos 20,23."; 8p "Vease f, II Nefi 2.";
  8q "Vease k, I Nefi 15."; 8r "Versiculo 19."; 8s "Vease j, Mosiah
  3." STRAY MARKS (rule 36): (1) Moroni 8:14 "si pereciere con este"
  — raised speck over the second "e" ("pereciere"?); Google OCR page
  0646 reads plain "pereciere" (silent) -> stray speck, transcribed
  without accent, NOT logged; 1886 file p.637 confirms plain
  "pereciere". (2) This page's scan carries many raised specks/blobs
  in the verse-end margins (after "recibido." v.15 where 1879 has no
  footnote, after "misericordia." v.19, after "Cristo." v.21, over
  "todos" v.19) — none represent type, none transcribed.
  Google-text cross-check page 0646: body matches letter-for-letter
  except the stray speck at v.14, dropped/garbled superscripts (rule
  14 — 8l as apostrophe, 8n as double-quote, 8p as "P"), and fn-block
  letter noise (Google read 8p target as "1", 8s target as "i" — both
  overridden by 1879 + zoom). v.14 "el que" accent cross-confirmed by
  Google (really printed). Session B: fresh 7x fn-block crops (three
  bands) + fresh body-marker read + independent 1879 cross-check
  (Moroni 8 = 1879 file pp.624-625). All 13 Block 1 entries + 13 body
  markers UNCHANGED. 1879 body markers on pp.624-625 confirm every
  placement (v.11 "the remission of sins", v.12 "from the foundation",
  v.14 "neither faith" / "down to hell", v.17 "partakers of
  salvation", v.18 "unchangeable" / "all eternity", v.19 "all alive in
  him" / "his mercy", v.20 "the atonement", v.21 "hell", v.22 "alive
  in Christ" / "they that are without the law"). Session C:
  insert_body_text.py 624 — librodm.txt 32712->32757 (+45);
  librodm_foot.txt 4938->4951 (13 Block 1 entries, NO blank line / NO
  book header — Moroni ch.8 continues, rule 20). Body landed before
  "Notas" with the blank-line separator, "Pagina 624" straight into
  verse 11. Session D: generate_block2.py 624 appended 4604-4616
  (librodm.txt 32757->32770) — no unresolved warnings, no
  wrapped-Block-1-entry bug (Notas tail ends cleanly at "4616: Vease
  1105."). Cross-refs (book-aware): 8h->1117 (Mosiah 4d); 8i->4561
  (Moroni 7a); 8j/8q->134 (I Nefi 15k); 8k->1108 (Mosiah 3m); 8l->4240
  (Mormon 9d); 8m->1096 (Mosiah 3a); 8p->265 (II Nefi 2f); 8s->1105
  (Mosiah 3j); 8g/8n/8o/8r direct. Anchor<->Block-2 after append: max
  anchor 4616 = max def 4616, contiguous 1..4616, no gaps/dupes; only
  the documented Jacob 2:15/812 gap remains. Session E: fresh full
  pptext report report_wsl_20260901.html walked end to end; 1886
  comparison vs Moroni 8 file p.637 (vv.6-16) + file p.638 (vv.16-24)
  — ALL of Moroni 8:11-22 compared word-for-word. Only routine
  1886-archaic vs 1920-modern house-style differences
  (fundacion/fundacion, excepcion/excepcion, remision/remision,
  circuncision, vias/vias, concluido, aquellos/aquellos, unaccented
  aun/estos in 1886). Corrections-log sweep — every flagged item run
  through the 1886 + errors-log + independent-research check; ALL
  resolve as NON-errors, NOTHING logged: (1) Moroni 8:14 "el que
  supone" — 1886 & modern BoM print unaccented "el que", but
  librodm.txt carries 179 instances of 1920's accented relative "el
  que" (feedback_errors_log_diligence mirror case — overwhelming
  internal consistency = 1920 house style); preserved, NOT logged, not
  pptext-flagged, no permitted-words entry. (2) Moroni 8:14
  "pereciere" — 1886 file p.637 confirms plain "pereciere" (no
  accent), rule-36 stray speck, NOT logged. (3) Moroni 8:13 "estos
  hubieran ido" — 1886 file p.637 ALSO unaccented "estos", NOT logged.
  (4) Moroni 8:16 "Ay del que pervierta" (no opening inverted mark) —
  1886 file p.637 ALSO prints "Ay" with no inverted mark (both
  editions), NOT logged. (5) Moroni 8:21 "haz atencion" — 1886 file
  p.638 ALSO "haz atencion" (archaic "hacer atencion a" construction,
  shared lineage), NOT logged. NO new permitted words.txt entries, NO
  new errors in 1920.txt entries (both files unchanged). NO
  narrow-space/merge items (Session A found no tight word-pairs).
  Whole-document mechanical sweeps all clean (check_spaced_punctuation
  librodm.txt 32770; check_footnote_punctuation librodm_foot.txt 4951;
  check_verse_indent librodm.txt; anchor<->Block-2 [only 812];
  curly-quote scan of librodm.txt / librodm_foot.txt / page_624.txt
  zero). Full pptext walkthrough: every page-624 hit is structural —
  the short-lines flood (verse-boundary wrapped body lines + short
  Block-2 "Vease NNNN." entries); NO page-624 spellcheck /
  edit-distance / repeated-word / duplicate-line / dash (no page-624
  hyphens at all) / scanno / curly-quote / spaced-punctuation /
  special-situations / paragraph-level ("full stop followed by
  unexpected sequence" no Moroni 8:11-22 hit) / book-level / Jeebies
  findings. OUT-OF-SCOPE OBSERVATION surfaced for the editor (not
  touched): the regenerated pptext "adjacent spaces check" flags 95
  lines in librodm.txt (lines 26381-26718 = pages 592-600, Ether
  ch.8-10, integrated earlier) that keep a double space after a
  sentence period (and after some verse numbers), contrary to rule 6 —
  wants its own dedicated cleanup pass. NO text changes to
  page_624.txt body or librodm.txt this session.
- **2026-09-01b** (same session, editor follow-up): Double-space
  cleanup. The page-624 Session E pptext walkthrough had surfaced 95
  librodm.txt body lines (26381-26718 = pages 592-599, Ether ch.8-13,
  integrated in earlier sessions) that kept a double space after a
  sentence period or after a verse number, contrary to rule 6.
  Collapsed every run of 2+ spaces to one space on those 95
  librodm.txt lines and on the matching body text of
  pages/page_592.txt through page_599.txt (95 body lines across the 8
  page files, matching the librodm.txt count). Only body text touched
  — page-file Corrections logs (which quote pre-fix spacing and 1879
  fn-block lines) left as-is; librodm.txt Notas section was already
  clean. No emailed chapter affected (chapters_emailed runs only
  through III Nefi 18; Ether is far past it). Verified: fresh pptext
  report workspace/report_wsl_20260901b.html "adjacent spaces check"
  now reads "no adjacent spaces found in text."; whole-document
  residual double-space scan returns 0; check_lines on all 8 page
  files shows the only over-72 / trailing-hyphen hits are inside their
  Corrections logs (pre-existing, not body, not caused by this edit —
  collapsing spaces only shortens lines). Separately noted while
  scoping: librodm.txt is missing its "Página 537" and "Página 538"
  divider lines (jump from "Página 536" at line 23937 to "Página 539"
  at 24067 — the body text of both pages is present, just no page
  markers); pre-existing, unrelated to this cleanup, left for a future
  pass. 5 Session-E Corrections-log items for page 624 re-examined at
  the editor's question ("are any genuine Spanish errors with no
  archaic usage?") — answer: none is a clean error. (1) Moroni 8:14
  "él que" = 1920's consistent house-style accentuation of the
  relative (179x in librodm.txt vs 38x unaccented; period-orthography
  practice, same class as preserved "fué/vió/aquél"); NOT a
  shared-1886 argument (1886 has unaccented "el que") — it is
  internal-consistency-as-house-style. (2) "pereciere" = correct
  future subjunctive; the only issue was a stray speck, not a spelling
  question. (3) Moroni 8:13 "estos" (demonstrative pronoun,
  unaccented) = acceptable under current RAE (2010+ drops the pronoun
  accent) and the modern BoM ALSO prints unaccented "estos" here;
  period-normal, shared with 1886. (4) Moroni 8:16 "Ay" with no
  opening "¡" = era-typical typographic omission, shared with 1886,
  and 1920 is itself inconsistent (has "¡Ay de los tales!" five verses
  later); the errors-log's punctuation entries are all 1920-only
  deviations FROM 1886 (Mormón 8:40 spurious "¿", III Nefi 28:15
  spurious ".", Éther 8:9 comma), which this is not. (5) Moroni 8:21
  "haz atención" = the older locution "hacer atención (á)" = reparar /
  advertir / considerar con cuidado (maps to 1879 "give heed");
  attested as a period locution and shared with the 1886 edition of
  the same era; modern standard is "prestar/poner atención" (RAE), and
  the modern BoM reworded the clause away entirely; corpora
  uninformative ("atención" appears 0-1x total across Quijote / RV1909
  / full RV — not a Golden-Age/biblical-register word). This is the
  thinnest of the five but still a documented period form, not a
  malformation. NOTHING logged; no permitted words.txt or errors in
  1920.txt changes.
- **2026-09-01c** (same session, editor follow-up): Fixed the missing
  "Página 537" and "Página 538" divider lines. Root cause: pages 537
  and 538 both open mid-verse (III Nefi 23:5 continues from page 536;
  24:3 continues from page 537), and their Session A entries
  (2026-07-28f / 2026-07-28g) omitted the `Página N` first line
  entirely, citing rule 1 -- but rule 1 only drops the BLANK line
  between `Página N` and the continuation text, it does not drop the
  `Página N` marker itself. Pages 534/535/536, transcribed immediately
  before and also opening mid-verse, all keep their markers (marker
  line, then body immediately, no blank after) -- that is the correct
  pattern and pages 537/538 were the only two deviations in the entire
  437-624 range. Fix: prepended `Página 537` to pages/page_537.txt and
  `Página 538` to pages/page_538.txt (as line 1, matching
  page_535/536/539), and inserted the same two marker lines into
  librodm.txt at the existing blank-line page separators (line 23981
  between "...y se arrepienta, y" / blank / "sea [3905]bautizado..."
  and line 24024 between "...purificador de plata, y" / blank /
  "purificará á los [3912]hijos de Leví..."). librodm.txt
  32770->32772 (+2, exactly the two marker lines). Verified: Página
  sequence 534..540 now complete and evenly spaced (~43-44 lines
  apart); no page in 437-624 is missing a marker; both new junctions
  match the established "<content> / blank / Página NNN / <content
  immediately>" convention (same as pages 535/536/539);
  check_verse_indent, check_spaced_punctuation, check_footnote_
  punctuation all clean; anchor<->Block-2 unchanged (contiguous
  1..4616, only the documented 812 gap). No body text altered -- only
  the two structural marker lines added. (The rules-doc wording of
  rule 1 could be tightened to say explicitly that mid-verse pages
  still get the `Página N` line; not changed this session.) Separately
  visible in `git diff HEAD` but from an earlier uncommitted session,
  not this one: a `CAPTULO 12.` -> `CAPÍTULO 12.` accent fix at
  librodm.txt line 22822.
- **2026-09-02**: Sessions A–E run in one session for page 625 (Moroni
  8:22-30), first footnote 4617, Moroni 8's letters t-z + 2a (8
  footnotes, 4617-4624). Page CONTINUES the Book of Moroni and Moroni
  chapter 8, opening MID-VERSE. Page 624 ended mid-verse 22 ("...Porque
  el"), so page 625's body begins immediately with "poder de la
  redención alcanza también..." on the first line — NO blank line after
  "Página 625", NO chapter heading, NO book header (rule 1). Running
  header "CAP. VIII.)  LIBRO DE MORONI.  625" discarded (rule 2). Page
  624 ended with the complete word "el" — no page-boundary word split
  (rule 10 N/A). Page ENDS the chapter at Moroni 8:30 ("...ó te
  encuentre otra vez. Amén."); Moroni chapter 9 begins on page 626. 35
  body print lines. Rule 7: 6 hyphen splits — "condena-/ción," ->
  "condenación," (line 9, 67, kept); "manda-/mientos ;" ->
  "mandamientos;" (line 12, 68, kept); "re-/misión" -> "remisión"
  (line 13, 59, kept); "manse-/dumbre" -> "mansedumbre" (line 15, 66,
  kept); "Consola-/dor," -> "Consolador," (line 17, 72, kept);
  "arre-/pentimiento." -> "arrepentimiento." (line 25, 71, kept). Rule
  8: no rebalance (longest = 72, line 17). Rule 31: ×6 body ";"
  de-spaced (1920 sets a space before ";" throughout — v.22
  "arrepentirse ;", v.25 "bautismo ;" / "mandamientos ;" / "pecados ;",
  v.26 "oración ;", v.28 "Dios ;"). Rule 6: ×5 sentence double-spaces
  collapsed (v.22 "ley. Porque", v.26 "corazón. Y", v.27 "Lamanitas.
  He", v.28 "arrepentimiento. Porque", v.30 "vez. Amén."); no
  zero-width merges; Session A found no tight word-pairs. Rule 23/24:
  Block 1 8u "Versículos 19, 20, 23." -> "19-20,23." (19-20 consecutive
  range, 23 non-consecutive); 8z "Alma 39 : 5, 6." -> "Alma 39:5-6."
  (5-6 consecutive range, colon de-spaced). 8 markers: 8t=[4617]
  "burlarse" (8:23); 8u=[4618] "misericordias" (8:23); 8v=[4619]
  "cumplimiento" (8:25); 8w=[4620] "visitación" (8:26); 8x=[4621] "de"
  (8:26, on "de esperanza" — 1879 "with hope", rule 26); 8y=[4622]
  "oración" (8:26); 8z=[4623] "negando" (8:28); 8-2a=[4624] "dadas"
  (8:29). MANDATORY i/l/1 check NOT triggered by letter identity (entry
  letters t-z,2a; target letters f,g,y,a,e,d). Discretionary 1879
  cross-check run on 3 over-inked/ambiguous 1920 target glyphs: 8t
  target = "f" (slender italic; 1879 "t, see f."); 8v target = "g"
  (rounder bulbous glyph vs the slender 8t "f"; 1879 file p.626 "v, see
  g."; content-fit Moroni 8g = "III Nefi 12:2; 30:2." — remission of
  sins — over Moroni 8f = baptism); **8w target CORRECTED in Session B
  from "v" to "y"** — a 24x crop shows a left-hooking descender (italic
  y, not descender-less v), 1879 file p.626 prints "w, see y, III. Nep.
  9.", and content-fit is decisive (III Nefi 9y #3585 = "I Nefi
  10:17...; II Nefi 31:11-14...; 32:2-5;..." doctrine-of-Christ /
  Holy-Ghost footnote, matching the marker on "la visitación del
  Espíritu Santo"; III Nefi 9v #3582 = "III Nefi 15:2-8." law of Moses,
  does not fit). Moroni 8 footnotes span 1879 file p.625 (g-u) + file
  p.626 (v-2a): 1879 p.626 block "v, see g. / w, see y, III. Nep. 9. /
  x, see a, Moro. 7. / y, see e, II. Nep. 32. / z, Alma 39 : 5, 6. /
  2 a, see d, I. Nep. 12." — matches this page's 8 entries one-for-one
  after the 8w fix. 1879 body markers (file pp.625-626) confirm every
  placement. Block 1: 8t "Véase f."; 8u "Versículos 19-20,23."; 8v
  "Véase g."; 8w "Véase y, III Nefi 9."; 8x "Véase a, Moroni 7."; 8y
  "Véase e, II Nefi 32."; 8z "Alma 39:5-6."; 8-2a "Véase d, I Nefi
  12." Google cross-check page 0647: 0 candidates (6 dismissed
  fn-marker glue, 1 fn-block content); body matches letter-for-letter.
  Session B: fresh 3-band fn-block crops + fresh body-marker read +
  independent 1879 cross-check — 7 of 8 Block 1 entries UNCHANGED, 8w
  "v"->"y" corrected (see above); all 8 body markers UNCHANGED. Session
  C: insert_body_text.py 625 — librodm.txt 32772->32809 (+37);
  librodm_foot.txt 4951->4959 (8 Block 1 entries, NO blank line / NO
  book header — Moroni ch.8 continues, rule 20). Página sequence
  616..625 contiguous. Session D: generate_block2.py 625 appended
  4617-4624 (librodm.txt 32809->32817) — no unresolved warnings, no
  wrapped-Block-1-entry bug (Notas tail ends cleanly at "4624: Véase
  79."). Cross-refs (book-aware): 8t->4603 (Moroni 8f); 8v->4604
  (Moroni 8g); 8w->3585 (III Nefi 9y); 8x->4561 (Moroni 7a); 8y->783
  (II Nefi 32e, "pray always"); 8-2a->79 (I Nefi 12d); 8u/8z direct.
  Anchor<->Block-2 after append: max anchor 4624 = max def 4624,
  contiguous 1..4624, no gaps/dupes; only the documented Jacob
  2:15/812 def-without-anchor remains. Session E: fresh full pptext
  report report_wsl_20260901c.html walked end to end — every page-625
  hit structural (short-lines flood + 2 legit digit-flanked
  verse-range hyphens in dash check: 4618 "19-20,23", 4623 "39:5-6");
  NO page-625 spellcheck / edit-distance / repeated-word /
  duplicate-line / scanno / curly-quote / spaced-punctuation /
  special-situations / paragraph-level / book-level / Jeebies
  findings. Whole-document mechanical sweeps clean
  (check_spaced_punctuation librodm.txt 32817; check_footnote_
  punctuation librodm_foot.txt 4959; check_verse_indent librodm.txt;
  anchor<->Block-2 only [812]; curly-quote scan zero). 1886 comparison
  vs Moroni 8 file p.638 (vv.16-26) + file p.639 (vv.27-30) — ALL of
  Moroni 8:22-30 compared word-for-word. ONE genuine 1920-only
  deviation found and LOGGED in errors in 1920.txt (verse order, after
  Moroni 8:9): **Moroni 8:22 "el bautismo no es ningún efecto" (no es
  de ningún efecto)** — 1920 drops the preposition "de" from the
  locution "ser de ningún efecto"; 1886 file p.638 prints "no es de
  ningun efecto" WITH "de"; 1879 "baptism availeth nothing"; modern
  Spanish BoM reformulates ("de nada sirve"); Google OCR page 0647
  also reads "no es ningún efecto" (1920 really omits it); without
  "de" the predicate nominal is ungrammatical; elsewhere 1920 uses
  "ningún efecto" only with "tener" (where "de" is not needed).
  Preserved as printed; not pptext-flagged, no permitted-words entry
  (no non-dictionary token). All other Moroni 8:22-30 differences are
  routine 1886-archaic vs 1920-modern house style (1886 unaccented
  redencion/condenacion/remision/corazon/visitacion/oracion/nacion/
  destruccion/despues/Adios/Amen, "fé"/"Hé"/"mio", "el que"/"aquellos";
  1886 semicolon vs 1920 comma before "porque" v.28; 1886 omits the
  commas 1920 sets around "he aquí"). NOT logged. Corrections-log
  sweep: "á quiénes" (1886 "á quienes"; 24 accented in librodm.txt —
  house style), "él que" ×2 (1886 "el que"; ~179 accented — house
  style), "país solo tratan" (1886 ALSO "pais solo" — shared),
  v.25 "re-" stray dot (rule-36 speck, Google silent) — all NON-errors,
  nothing further logged. NO narrow-space/merge items. NO new permitted
  words.txt entries. ONE new errors in 1920.txt entry (Moroni 8:22).
  NO text changes to page_625.txt body or librodm.txt this session.
- **2026-09-03**: Sessions A–E run in one session for page 626 (Moroni
  9:1-9), first footnote 4625, Moroni 9 letters a-d (4 footnotes,
  4625-4628). Page CONTINUES the Book of Moroni and BEGINS Moroni
  chapter 9. Page 625 ENDED Moroni 8 ("...ó te encuentre otra vez.
  Amén."), so page 626 OPENS fresh: blank line after "Página 626", then
  "CAPÍTULO 9." (blank before/after, rule 3), then the italic chapter
  subtitle "Segunda Epistola de Mormón á su Hijo Moroni." on its own
  line with blank-line separators (chapter subtitles always
  transcribed). NO book header (Book of Moroni continues). 1920 prints
  "CAPÍTULO 9." BEFORE the subtitle (house-style order; 1886 same on
  file p.639). Running header "626  LIBRO DE MORONI.  (CAP. IX."
  discarded (rule 2). Page 625 ended with the complete word "Amén." — no
  page-boundary word split (rule 10 N/A). Page ENDS mid-verse 9 ("...que
  era la castidad y la virtud;") — Moroni 9 continues on page 627. 37
  body print lines + CAPÍTULO 9 heading + subtitle line. Rule 7: 2
  hyphen splits — "con-/stantemente" -> "constantemente" (rejoined onto
  line 10 = exactly 72, kept; "á la cólera los unos contra los otros."
  becomes the next line); "cora-/zones" -> "corazones" (line 14, 66,
  kept). Rule 8: no rebalance (longest = 72). Rule 31: x9 body ";"
  de-spaced. Rule 6: x3 sentence double-spaces collapsed (v.1 "todavía.
  Pero", v.2 "ventajosos. Y", v.6 "condenación. Porque"); no zero-width
  merges. Rule 23: Block 1 9d "Mormón 4:11, 12." -> "Mormón 4:11-12."
  4 markers: 9a=[4625] "destruyan" (9:3); 9b=[4626] "dureza" (9:4);
  9c=[4627] "que" (9:4, the 2nd "que" in "por lo que, temo que el
  Espíritu"); 9d=[4628] "sed" (9:5). Block 1: 9a "Véase d, I Nefi 12.";
  9b "Véase a, I Nefi 16."; 9c "Moroni 8:28."; 9d "Mormón 4:11-12."
  MANDATORY i/l/1 check NOT triggered by letter identity (entry letters
  a-d; target letters d, a). Discretionary 1879 cross-check on the 9b
  target (an over-inked superscript blob on the 1920 scan): 1879 file
  p.626 "b, see a, I. Nep. 16." — unambiguous italic "a"; resolved
  "Véase a, I Nefi 16." Moroni 9 footnotes span 1879 file p.626 (a-c) +
  file p.627 (d): 1879 p.626 "a, see d, I. Nep. 12. / b, see a, I. Nep.
  16. / c, Moro. 8 : 28.", 1879 p.627 "d, Mor. 4 : 11, 12." — this
  page's 4 entries match one-for-one. 1879 body markers confirm every
  placement: (a) "destroy this people" v.3; (b) "with sharpness" v.4;
  (c) "lest the Spirit of the Lord" v.4 (1920 letter on "que", rule
  26); (d) "thirst after blood and revenge" v.5. Google cross-check
  page 0648: check_google_crosscheck.py parsed 0 body chars (known
  parser quirk on a page opening with a CAPÍTULO/subtitle block) so a
  manual line-by-line comparison was done — Google's OCR matches the
  transcription letter-for-letter except dropped superscripts, accent
  drops ("Epistola"), word-fusion ("entreellos", "lashijas"); crucially
  Google INDEPENDENTLY reads both suspected misprints as printed (v.4
  "enojen", v.9 "he"). Session B: fresh 3-band 1920 fn-block crops (~9x)
  + fresh ~12x body-marker crops + independent 1879 cross-check — all 4
  Block 1 entries and all 4 body markers UNCHANGED. Session C:
  insert_body_text.py 626 — librodm.txt 32817->32861 (+44);
  librodm_foot.txt 4959->4963 (4 Block 1 entries, NO blank line / NO
  book header — Moroni ch.9 continues, rule 20). Página sequence
  623..626 contiguous. Session D: generate_block2.py 626 appended
  4625-4628 (librodm.txt 32861->32865) — no unresolved warnings, no
  wrapped-Block-1-entry bug (Notas tail ends cleanly at "4628: Mormón
  4:11-12."). Cross-refs (book-aware): 9a->79 (I Nefi 12d — same target
  page 625's 8-2a resolves to, same theme of prophesied Nephite
  destruction); 9b->136 (I Nefi 16a — whose own citation list
  back-references "Moroni 9:4", reciprocal confirmation of target AND
  verse); 9c/9d direct. Anchor<->Block-2 after append: max anchor 4628 =
  max def 4628, contiguous 1..4628, no gaps/dupes; only the documented
  Jacob 2:15/812 def-without-anchor remains. Session E: fresh full
  pptext report report_wsl_20260901e.html walked end to end. SPELLCHECK:
  4 new proper-name suspects — "Archeantus" (9:2), "Emrón" (9:2),
  "Luram" (9:2), "Sherrízah" (9:7) — all Book-of-Mormon proper nouns,
  ADDED to permitted words.txt (rule 10), NO errors-log entry.
  permitted words.txt: 1284->1288. "Amorón" (9:7) / "Moriántum" (9:9)
  NOT flagged (5+-occurrence aspell auto-accept from earlier books; no
  action). Every other page-626 hit structural (short-lines flood + 1
  legit digit-flanked verse-range hyphen "4:11-12" in dash check + the
  v.9->Notas boundary in the paragraph-level "unexpected paragraph end"
  list, page 626 being the last transcribed page). NO page-626
  edit-distance / repeated-word / duplicate-line / scanno / curly-quote
  / spaced-punctuation / special-situations / book-level / "full stop
  followed by unexpected sequence" findings. Jeebies clean.
  Whole-document mechanical sweeps clean (check_spaced_punctuation
  librodm.txt 32865; check_footnote_punctuation librodm_foot.txt 4963;
  check_verse_indent librodm.txt; anchor<->Block-2 only [812];
  curly-quote scan zero). 1886 comparison — Moroni 9 heading + vv.1-6 on
  1886 file p.639, vv.6-9 on file p.640 — ALL of Moroni 9:1-9 compared
  word-for-word. TWO genuine 1920 deviations found and LOGGED in errors
  in 1920.txt (911->913, verse order at end of file): (1) **Moroni 9:4
  "se enojen" (se enojan)** — present-subjunctive where the parallel
  indicative "tiemblan" requires "se enojan"; 1886 file p.639 ALSO "se
  enojen" (SHARED lineage error, cf. Moroni 6:8 "arrepintían" / 6:9
  "obrabran"); 1879 "they tremble and anger against me"; modern BoM
  "tiemblan y se enojan conmigo"; Google page 0648 also "enojen"; not
  pptext-flagged (valid word); no permitted-words entry. (2) **Moroni
  9:9 "muchas he las hijas" (muchas de las hijas)** — 1920 prints "he"
  where the partitive "de" is required; 1886 file p.640 prints "muchas
  de las hijas" CORRECTLY (1920-ONLY error); 1879 "many of the daughters
  of the Lamanites"; modern BoM "muchas de las hijas de los lamanitas";
  Google page 0648 also "he" ("muchas he lashijas"); not pptext-flagged
  (valid word); no permitted-words entry. NOT logged: (a) subtitle
  "Epistola" without acute — 1886 file p.639 ALSO "Epistola"/"Mormon"
  unaccented, missing-accent-only, 1886 drops accents throughout —
  house-style accent omission (subtitle rule: do not supply missing
  accents; 1879 prints no Spanish subtitle, no wording discrepancy);
  (b) v.3 "satán" lowercase — 1886 "Satan" capitalized, but librodm.txt
  carries 25+ lowercase "satán" and ZERO capitalized "Satán"/"Satanás",
  overwhelming 1920 internal consistency = house style
  (feedback_errors_log_diligence mirror case); (c) proper-name accents
  "Emrón"/"Sherrízah" vs 1886 "Emron"/"Sherrizah" — 1920 accent
  modernization; (d) v.2/v.3 commas 1920 sets after "aquí"/"ahora"
  (1886 omits) — 1920 house-style comma addition (page 625 precedent).
  Narrow-space vs. two words (feedback_narrow_space_vs_merge; editor may
  double-check the image, two-word transcription is the committed
  default): Moroni 9:4 "entre ellos" and 9:9 "las hijas" both printed
  with a reduced gap in 1920, both two words in 1886, transcribed as two
  words. NO text changes to page_626.txt body or librodm.txt this
  session — both Moroni 9 errors preserved exactly as printed.
- **2026-09-04**: Sessions A–E run in one session for page 627 (Moroni
  9:10-22), first footnote 4629, Moroni 9 letters e-f (2 footnotes,
  4629-4630). Page CONTINUES the Book of Moroni and Moroni chapter 9 (no
  book header, no chapter heading, rule 1). Page 626 actually ended with
  Moroni 9:9 COMPLETE ("...que era la castidad y la virtud;" — 1920
  renders the modern em dash after "virtue" as a semicolon), NOT
  mid-verse as the previous session's "Next page" note anticipated —
  page 627 OPENS with a fresh verse number "10." (rule 1 treatment
  identical either way: blank line before "Página 627", body text on the
  next line, no blank line after, no heading). Running header "CAP. IX.)
  LIBRO DE MORONI. 627" discarded (rule 2). Page ENDS with v.22 COMPLETE
  ("...ó de su entera destrucción."); no page-boundary word split (rule
  10 N/A). Body = 44 output lines (= 44 print lines). Rule 7: 3 hyphen
  rejoins — "conside-/rándolo" → "considerándolo" (rejoined line = 70,
  kept); "los La-/manitas" → "Lamanitas" (68, kept); "sufri-/mientos" →
  "sufrimientos" (69, kept). Rule 8: no rebalance (longest line = 71, the
  v.22 "conserve la vida, para que" line with [4630]). Rule 31: ×11
  de-spaces before ";" / ":" / "!" (1920 sets a space before these
  throughout the page). Rule 6: ×3 sentence double-spaces collapsed (v.18
  "pueblo! No", "misericordia. He aquí"; v.19 "fuere bueno. Y los"). No
  zero-width merges. No narrow-space-vs-merge flags on this page. Rule
  22: Block 1 9e "Mormón 2 : 9." → "Mormón 2:9.", 9f "Mormón 8 : 3." →
  "Mormón 8:3." (1879 also spaces the colons). 2 markers: 9e=[4629]
  "Aarón" (9:17, "los que han huido al ejército de Aarón"; 1879 "fled to
  the army of (e)Aaron"); 9f=[4630] "conserve" (9:22, "le pido al Señor
  que te conserve la vida"; 1879 "that he would (f)spare thy life",
  translation word-order, rule 26). Block 1: 9e "Mormón 2:9.", 9f "Mormón
  8:3." — both direct citations, no cross-references. MANDATORY i/l/1
  check NOT triggered by letter identity (entry letters e, f; no
  cross-ref target letters). Discretionary 1879 cross-check run on 9e
  (the 1920 fn-block glyph and body superscript are both an over-inked
  blob): Moroni 9 vv.17-22 fall on 1879 file p.628 (NOT p.627 — 1879
  pagination doesn't track 1920; 1879 p.627 fn-block has only page 626's
  "d, Mor. 4 : 11, 12."). 1879 file p.628 fn-block, clean italic type:
  "e, Mor. 2 : 9.   f, Mor. 8 : 3.   g, Ether 13—[wrap] 4 : 11, 12.
  i, I. Nep. 13 : 31.   Alma 45 : 14." — 9e unambiguous italic "e", 9f
  unambiguous italic "f"; g/h/i annotate Moroni 9:23-25 (1920 page 628).
  1879 body markers confirm: (e) before "Aaron" v.17, (f) before "spare"
  v.22. Google cross-check page 0649: 3 candidates — (1) v.13
  "abominaciones--" vs Google "abominaciones" (Google drops trailing
  dashes; zoom confirms printed em dash); (2) v.17 "Lamanitas" vs Google
  "Lȧmanitas" (stray OCR dot); (3) v.18 "He aquí;" vs Google "He aquí,"
  — Session A/E zoom wrongly read a semicolon (dot-over-tail); the
  editor's direct look at the scan (2026-09-04) confirmed Google was
  right, the mark is a plain comma + stray speck (rule 36), so v.18 was
  CORRECTED to "He aquí," in page_627.txt + librodm.txt. Google
  INDEPENDENTLY reads v.17 "ejírcitos" the same (í, not é) — corroborates
  that misprint.
  Session B: fresh independent fn-block crop (16×), fresh body-marker
  crops (18×), fresh independent 1879 file p.628 cross-check — all 2
  Block 1 entries and both body markers UNCHANGED; over-inked "e" blob
  resolved off 1879's clear italic type. Session C: insert_body_text.py
  627 — librodm.txt 32865→32911 (+46 = 44 body lines + "Página 627" +
  blank separator); librodm_foot.txt 4963→4965 (2 Block 1 entries, NO
  blank line / NO book header — Moroni ch.9 continues, rule 20). Página
  sequence 620..627 contiguous. Session D: generate_block2.py 627
  appended 4629-4630 (librodm.txt 32911→32913) — both direct citations,
  no unresolved warnings, no wrapped-Block-1-entry bug (Notas tail ends
  cleanly at "4630: Mormón 8:3."). Anchor↔Block-2: max anchor 4630 = max
  def 4630, contiguous 1..4630, no gaps/dupes; only the documented Jacob
  2:15/812 def-without-anchor remains. Session E: fresh full pptext
  report report_wsl_20260902e.html regenerated (WSL) and walked end to
  end. SPELLCHECK: 1 new suspect — "Zenefi" (9:16), a Book-of-Mormon
  proper noun; 1886 file p.640 ALSO prints "Zenefi" (1879 / modern BoM
  "Zenephi"). ADDED to permitted words.txt (rule 10), NO errors-log entry
  (proper noun, shared with 1886). permitted words.txt: 1288→1289. 1886
  comparison — Moroni 9:10-18 on 1886 file p.640, 9:18-22 on file p.641 —
  ALL of Moroni 9:10-22 compared word-for-word. ONE genuine 1920
  deviation found and LOGGED in errors in 1920.txt (913→914, appended in
  book order at end of file — Moroni 9 = true end): **Moroni 9:17
  "ejírcitos" (ejércitos)** — 1920 prints "ejírcitos" (í for é) where the
  SAME verse prints "ejército" correctly twice; 1886 file p.640
  "ejércitos" CORRECT (1920-ONLY error); "ejírcitos" zero hits in the 3
  corpora, aspell flags it standalone (→"ejércitos"); modern BoM "los
  ejércitos de los lamanitas"; 1879 "the armies of the Lamanites"; NOT
  listed in the full pptext Spellcheck section (same whole-document
  suppression as "Poi"/"dsesaría" pp.469-470, "bautizeis" Moroni 8:9), so
  NO permitted-words entry (no-op); preserved as printed. **Withdrawn
  intra-session:** a Moroni 9:18 "He aquí; que" (He aquí, que) entry was
  drafted and appended (913→915), then REMOVED after the editor's direct
  look at the scan showed the mark is a plain comma with a stray speck,
  not a semicolon — v.18 was CORRECTED to "He aquí," in page_627.txt +
  librodm.txt (a correct comma, no error; rule 12/36). errors in 1920.txt
  back to 914 lines. (My mistake: I dismissed Google's comma reading as
  "normalization" instead of treating it as evidence — the exact failure
  rule 36 warns against; cf. the III Nefi 14:2 / 18:28 / Éther 8:23
  precedents.) NOT logged: (a) v.11 "civilización--", v.13
  "abominaciones--" —
  1886 file p.640 ALSO prints an em dash at both, just the
  em-dash-representation convention (see below); (b) 1886 typos/accent
  drops "anmentado", "extension del pais", "órden", "hijo mio" — 1920 has
  the correct forms; (c) v.15 1886 "Hé aquí que clama" no comma vs 1920
  "He aquí, que clama" — 1920 house-style comma addition (page 625/626
  precedent). DASH CHECK: pptext's em-dash
  bucket flagged librodm.txt lines 27886/27890 — this page's Session A
  transcription used the real U+2014 em-dash char for
  "civilización—"/"abominaciones—". Per the documented dash convention
  (em-dash → "--", the form pptext self-recognizes as "book uses '--' as
  em-dash"), BOTH converted to "--" in pages/page_627.txt AND librodm.txt
  this session. Body-text changes this session: the ×2 em-dash → "--",
  plus v.18 "He aquí;" → "He aquí," (stray-speck correction, editor's
  direct read + Google OCR, rule 36); the ejírcitos error preserved as
  printed. WHOLE-DOCUMENT em-dash cleanup (same session, finally
  clearing the pointer left by page 621's Session E ~2026-08-31): the
  scan turned up 6 more U+2014 chars in librodm.txt from earlier pages
  — 20739+20742 (Helamán 10:3, p.462), 23224 (III Nefi 16:4, p.519),
  24206 (III Nefi 27:8, p.542, a ";—" pair), 26053 (Éther 3:26, p.584),
  26958 (Éther 12:28, p.605). pptext's em-dash bucket only displays the
  first 2, which is why the other 4 sat unnoticed on their pages. Each
  was checked against its own page file's Session A note and confirmed
  a genuine em dash, NOT a masked transcription error — my earlier
  "má—fuente" worry was a misread: page_605 and librodm both have
  "mí—fuente" ("unto me—the fountain", modern Éther 12:28). All 6
  converted "—" → "--" in librodm.txt AND their page files (462, 519,
  542, 584, 605 — body lines only; prose em-dashes in the Corrections
  logs left alone; a one-line dated note appended to each). Also fixed
  the two already-emailed archive copies for consistency (NOT resent,
  per the 2026-07-24b / 2026-07-25 retroactive-fix precedent):
  chapters_emailed/Helaman_10.txt (×2), chapters_emailed/III_Nefi_16.txt
  (×1). librodm.txt / librodm_foot.txt / every chapters_emailed/*.txt
  now hold ZERO U+2014 (only chapters_emailed/_log.txt keeps 2, in its
  own prose comments). Whole-document mechanical sweeps clean
  (check_spaced_punctuation librodm.txt 32913; check_footnote_punctuation
  librodm_foot.txt 4965; check_verse_indent librodm.txt; anchor↔Block-2
  only [812]; curly-quote scan of librodm.txt / librodm_foot.txt /
  page_627.txt all zero). Jeebies clean. No page-627 edit-distance /
  repeated-word / duplicate-line / ellipsis / adjacent-dashes / scanno /
  special-situations / book-level / "full stop followed by unexpected
  sequence" findings (all such hits are pre-existing / earlier pages).
  Short-lines + "unexpected paragraph end" page-627 hits are the usual
  structural verse-boundary false positives (page 627 is now the last
  transcribed page).
- **2026-09-02**: Sessions A–E run in one session for page 628 (Moroni
  9:23-26 and Moroni 10:1-4), first footnote 4631. Page CONTINUES the
  Book of Moroni; it finishes Moroni chapter 9 and BEGINS Moroni chapter
  10 (the last chapter of the Book of Mormon). Page 627 ended with Moroni
  9:22 COMPLETE ("...ó de su entera destrucción."), so page 628 OPENS
  mid-chapter with the continuation of v.22 ("Porque sé que han de
  perecer, excepto que se arrepintieren y volvieren á Él;") — "Página
  628" on its own line, body text on the next line, no blank line after
  the marker, no heading (rule 1). No page-boundary word split (rule 10
  N/A). Running header "628  LIBRO DE MORONI.  (CAP. X" discarded (rule
  2); the short rule between Moroni 9:26 and "CAPÍTULO 10." (and the
  divider inside the footnote block separating the two chapters'
  footnotes) discarded. Body = 37 print/output lines + the "CAPÍTULO
  10." heading (blank line before/after, rule 3). Moroni 10 has NO
  chapter subtitle — verse 1 begins immediately after the heading
  (confirmed against 1886 file p.641, same). Page ENDS mid-verse 10:4
  ("...la verdad de ellas, por el poder del Espíritu Santo;") — Moroni
  10 continues on page 629. Rule 7: 2 hyphen rejoins, both kept at the
  end of the first line — "miseri-/cordia" → "misericordia" (9:25,
  rejoined = 69); "miseri-/cordioso" → "misericordioso" (10:3, rejoined
  = 72). Rule 8: no rebalance. Rule 31: x8 body ";" de-spaced (1920 sets
  a space before ";" throughout this page): v.22 "Él ;", v.24
  "todavía ;", v.24 "prolongada ;", v.25 "mío ;", v.25 "muerte ;", 10:1
  "plazca ;", 10:4 "verdaderas ;", 10:4 "Santo ;". Rule 6: x2 sentence
  double-spaces collapsed (v.24 "más.  No obstante", v.26
  "contigo.  Amén."); also v.26 "se . asienta" (a speck) → "se asienta".
  No zero-width merges. Rule 23: Block 1 9h "Mormón 4:11, 12." → "Mormón
  4:11-12." Rule 24: 10d "Versículos 5, 7" → "Versículos 5,7" (5 and 7
  non-consecutive). 8 markers: 9g=[4631] "como" (9:23); 9h=[4632] "de"
  (9:23, "el derrame de sangre y la venganza"); 9i=[4633] "pasado"
  (9:24); 9j=[4634] "confiarte" (9:24); 10a=[4635] "señal" (10:1);
  10b=[4636] "estos" (10:2); 10c=[4637] "creación" (10:3); 10d=[4638]
  "por" (10:4). Block 1: 9g "Éther 13-15."; 9h "Versículo 5; Mormón
  4:11-12."; 9i "I Nefi 13:31; Alma 45:14."; 9j "Mormón 6:6."; 10a "III
  Nefi 2:8."; 10b "Mormón 6:6."; 10c "Véase m, Mosíah 2."; 10d
  "Versículos 5,7; Véase c, Moroni 3." Chapter boundary Moroni 9->10 is
  within the same book, so Block 1 gets NO blank line / NO book header
  (rule 20). MANDATORY i/l/1 check — entry letter 9i is "i": 1879's
  Moroni 9 footnote set (file pp.626-627) is only letters a-d (a=see d I
  Nefi 12; b=see a I Nefi 16; c=Moroni 8:28; d=Mormón 4:11-12), so there
  is NO 1879 counterpart citing I Nefi 13 or Alma 45 (rule 26 — the two
  editions' Moroni 9 footnote sets diverge: 1920 a-j, 1879 a-d).
  Resolved by the unambiguous alphabetical sequence g-h-i-j (all four in
  the block AND each with its own body marker in vv.23-24) plus glyph
  shape at 8x zoom (short x-height letter with a dot, no
  ascender/descender — excludes "l" and "1"); the 9j glyph confirmed "j"
  by its clear descender. Target "I Nefi 13:31" — Roman "I" is the book
  name (rule 34). 10c "Véase m" target — over-inked squat wide mark,
  "m", not i/l/1; 1879 Moroni 10 carries no footnotes. Session B: fresh
  independent 1920 fn-block zoom crops (9x, both chapter groups) + fresh
  body-marker crops (5-8x, all 8 markers) + independent re-examination
  of 1879 file p.626 bot / p.627 fn_zoom — all 8 Block 1 entries and all
  8 body markers UNCHANGED; the 9i "i" resolution re-confirmed. Session
  C: insert_body_text.py 628 initially pulled the literal "Block 1
  footnotes:" header line into librodm.txt as body text (this page's
  Session A file used a non-standard header; house convention is entries
  directly after a blank line, "Corrections" with no colon) — the stray
  line + trailing blank were deleted from librodm.txt by hand and
  page_628.txt corrected to house format; librodm_foot.txt got the 8
  entries correctly and was unaffected. Final: librodm.txt 32913->32955
  (+42); librodm_foot.txt 4965->4973 (+8, NO blank line / NO book
  header, rule 20). Página sequence 623..628 contiguous. Session D:
  generate_block2.py 628 appended 4631-4638 (librodm.txt 32955->32963) —
  no unresolved warnings, no wrapped-Block-1-entry spurious-trailer bug
  (Notas tail ends cleanly at "4638: Versículos 5,7; Véase 4543.").
  Cross-refs resolved: 4637 (10c) -> 1086 = Mosíah 2m, whose own
  citation list explicitly ends "...Éther 3:15-16; Moroni 10:3."
  (reciprocal confirmation of both target and verse); 4638 (10d "Véase
  c, Moroni 3") -> 4543 = Moroni 3c ("I Nefi 13:37; Moroni 6:9."),
  correct book section. Anchor<->Block-2 after append: max anchor 4638 =
  max def 4638, contiguous 1..4638, no gaps/dupes; only the documented
  Jacob 2:15/812 def-without-anchor remains. Session E: fresh full
  pptext report report_wsl_20260902e.html regenerated and walked end to
  end. SPELLCHECK: ZERO new page-628 suspects ("misericordioso",
  "confiarte", "Jareditas", "cuatrocientos", "meditéis", "recibáis",
  "Adam", "cuan" all unflagged) — NO permitted words.txt additions.
  Every other page-628 hit is a known structural false positive: the
  short-lines flood over the 8 new Block 2 entries; the v.4->Notas
  boundary in the paragraph-level "unexpected paragraph end" list (page
  628 is the last transcribed page, ending mid-verse 10:4); the TOC
  "Moroni 628" line. Dash check hyphen-minus: the 2 new Block 2 range
  hyphens ("Éther 13-15", "Mormón 4:11-12") are both properly
  digit-flanked. NO page-628 edit-distance / repeated-word /
  duplicate-line / adjacent-space / trailing-space / scanno /
  curly-quote / spaced-punctuation / special-situations / book-level /
  "full stop followed by unexpected sequence" findings. Jeebies clean.
  Letter-hyphen-letter blind-spot scan: 0 tokens in the page-628
  segment. Whole-document mechanical sweeps all clean
  (check_spaced_punctuation librodm.txt 32963; check_footnote_punctuation
  librodm_foot.txt 4973; check_verse_indent librodm.txt; curly-quote
  scan of librodm.txt / librodm_foot.txt / page_628.txt all zero;
  anchor<->Block-2 only [812]). 1886 comparison — Moroni 9:22-26 on 1886
  file p.641 (book p.623), Moroni 10:1-4 on 1886 file pp.641-642 (book
  pp.623-624) — ALL of page 628's verses compared word-for-word. NO
  genuine 1920 deviations; NO errors in 1920.txt additions. Differences
  are all previously-established house style: (a) 1920 supplies acute
  accents 1886 omits throughout ("todavía/aparición/mío/después/vía/
  según/también/corazón/intención" etc.) — accent modernization; (b)
  1920 adds house-style commas 1886 omits — 9:26 "de Dios, el Padre",
  10:1 "Ahora, yo", 10:3 "He aquí, os exhorto" (page 625/626 comma-
  addition precedent); (c) 9:26 "Jesu Cristo" unhyphenated vs 1886
  "Jesu-Cristo" — documented legitimate archaic form of this edition
  (feedback_jesu_cristo_hyphen; librodm.txt carries 26 unhyphenated
  "Jesu Cristo"); (d) 10:3 "cuan misericordioso" without the exclamative
  accent — 1886 prints "cuan" here TOO (shared reading); "cuan" is a
  valid RAE form (apocope of "cuanto"); librodm.txt has 10 unaccented
  "cuan + adj." including "cuan grandes" on the title page and in
  footnote text — established minority house pattern; not pptext-flagged
  (valid word); NO permitted-words entry, NO errors-log entry
  (feedback_errors_log_diligence mirror case); (e) 10:3 "Adam" — 1886
  prints "Adam" too (shared); proper noun, document-wide usage from the
  Éther chapters; not flagged; no action; (f) 10:4 page ends on ";"
  where 1886 ends the (continuing) verse on ":" — non-substantive
  continuation-punctuation variance. feedback_narrow_space_vs_merge flag
  for the editor: 10:1 "voy á escribir" — 1920 sets "voy á" with a
  reduced gap; 1886 file p.641 prints "voy á escribir" as two clearly
  separated words; grammar requires two words; committed as two words
  "voy á" (editor may double-check the 1920 image at leisure — not a
  blocker). NO text changes to page_628.txt or librodm.txt in Session E.

- **2026-09-03**: Sessions A–E run in one session for page 629 (Moroni
  10:5-21), first footnote 4639, Moroni 10 letters e-m (9 footnotes,
  4639-4647). Page CONTINUES Moroni chapter 10 within the Book of
  Moroni. Page 628 ENDED at a complete verse boundary — the end of
  Moroni 10:4 ("...Él os manifestará la verdad de ellas, [4638]por el
  poder del Espíritu Santo;") — so page 629 OPENS with a FRESH verse
  number "5." (not a mid-verse continuation, contrary to the CLAUDE.md
  prediction; rule 1 treatment is the same either way): "Página 629"
  on its own line, body text on the very next line, no blank line
  after the marker, no chapter heading. NO book header, NO Block 1
  blank line (Moroni 10 continues within the Book of Moroni, rule 20).
  Running header "CAP. X.)  LIBRO DE MORONI.  629" discarded (rule 2).
  Page 628 ended on the complete word "Santo;" — no page-boundary word
  split (rule 10 N/A). Page ENDS mid-verse 21 ("...ni podréis
  salvaros en el reino") — Moroni 10 continues on page 630. 40 output
  body lines (42 raw print lines − 2 hyphen rejoins). Rule 7: 2 hyphen
  splits — "minis-/tradores" → "ministradores" (v.14, rejoined line =
  68 after rule-31 de-spacing of trailing ";", kept at end of line);
  "sola-/mente" → "solamente" (v.19, rejoined line = 65, kept; next
  line becomes "en proporción á la incredulidad de los hijos de los
  hombres."). Rule 8: no rebalance (longest resulting line = 72).
  Rule 31: ×17 body ";" de-spaced (1920 sets a space before ";"
  throughout this page). Rule 6: 1 sentence double-space collapsed
  (v.8 "del mismo Dios.  Y estos dones"); no zero-width merges.
  Rule 22/23: Block 1 10i "I Corintios 12 : 8-11" → "I Corintios
  12:8-11" (colon de-spaced; 8-11 consecutive range). 9 markers:
  10e=[4639] "no" (v.7, before "no neguéis el poder de Dios");
  10f=[4640] "según" (v.7); 10g=[4641] "mismo" (v.7, "mismo hoy que
  mañana"); 10h=[4642] "neguéis" (v.8); 10i=[4643] "Porque" (v.9,
  verse-initial); 10j=[4644] "todo" (v.18, "todo buen don");
  10k=[4645] "mismo" (v.19, "mismo ayer, hoy y siempre"); 10l=[4646]
  "nunca" (v.19, "nunca de existir"); 10m=[4647] "Por" (v.20,
  verse-initial). Block 1: 10e "Véase r, II Nefi 26."; 10f "Véase d,
  III Nefi 17."; 10g "Véase d, Mormón 9."; 10h "Véase e, III Nefi
  29."; 10i "Véase e, III Nefi 29; I Corintios 12:8-11."; 10j "Véase
  o, Éther 4."; 10k "Véase d, Mormón 9."; 10l "Véase 2d, Moroni 7.";
  10m "Véase a, Moroni 7." MANDATORY i/l/1 check — entry letters 10i
  ("i") and 10l ("l") both in the set. 1879's Moroni 10 footnotes DO
  exist for this page's range — on 1879 file p.629 (book p.621), a-i:
  "a, III. Nep. 2:8. b, Mor. 6:6. c, see m, Mos. 2. d, vers. 5,7. See
  c, Moro. 3. e, see r, II. Nep. 26. f, see d, III. Nep. 17. g, see
  d, Mor. 9. h, see e, III. Nep. 29. i, see e, III. Nep. 29. I.
  Corinth. 12:8-11." (Note: CLAUDE.md's page-628 "Next page" note said
  1879 Moroni 10 = file p.627 with NO footnotes — that's where 1879's
  Moroni 10 chapter BEGINS; its footnote block is on file p.629.)
  This 1879 set pins 10e-10i letter-for-letter (entry "i" confirmed:
  clean short x-height italic "i", content III Nefi 29 + I Corintios
  12:8-11 matches exactly; 1879 body markers confirm each placement —
  e "deny not the power of God" v.7, f "he worketh by power,
  according to" v.7, g "the same to-day and to-morrow" v.7, h "ye
  deny not the gifts of God" v.8, i "For behold, to one is given"
  v.9). 1879's Moroni 10 stops at "i" (1920 has a-m — rule 26
  divergence), so 10l "l" has no 1879 counterpart: resolved by the
  unbroken e-f-g-h-i-j-k-l-m sequence (all nine in the block, each
  with its own body marker in vv.7-20) + glyph (thin vertical stroke,
  ascender, no descender). 10j-10m cross-ref TARGETS have no 1879
  counterpart and the 1920 fn-block superscripts are heavily
  over-inked/illegible; resolved by content-fit + reciprocal
  back-reference against librodm_foot.txt: 10k "Véase d, Mormón 9"
  (Mormón 9d = "Versículos 10,19..." = "God is the same yesterday,
  to-day, and forever" — fits marker on "mismo ayer, hoy y siempre");
  10l "Véase 2d, Moroni 7" (Moroni 7-2d = "Versículo 38; Moroni
  10:19,23-27" — reciprocal to this v.19; also recurs as a cross-ref
  in page 630's fn block per google_text); 10j "Véase o, Éther 4"
  (Éther 4o = "Moroni 7:5-22; 10:6-7" — mutual cross-ref for "todo
  buen don viene de Cristo"; established form used by Moroni 7e, 7g)
  — glyph illegible, FLAGGED for editor; 10m "Véase a, Moroni 7"
  (Moroni 7a = "Versículos 21-39,40-44,45-48; ...; Moroni 8:14,26;
  10:20-23" — reciprocal to this v.20 faith/hope/charity chain;
  established form used by Moroni 8i, 8x; "Véase e, Moroni 7" is
  unattested) — glyph illegible, FLAGGED for editor. 10e "Véase r, II
  Nefi 26" cross-checked via 1920's own II Nefi 26r [671] = "II Nefi
  28:5-6..." ("deny the power of God"); 10f "Véase d, III Nefi 17"
  via III Nefi 17d [3744] = "II Nefi 27:23..." ("according to their
  faith"). Google cross-check page 0651: UNAVAILABLE — the 1920 PDF's
  embedded text layer for file 651 is corrupt, returning Éther 13
  content ("una Nueva Jerusalem... Los que fueren primeros, serán los
  últimos...") instead of Moroni 10:5-21. Adjacent file pages extract
  correctly (650 = book 628 = Moroni 9:22-10:4; 652 = book 630 =
  Moroni 10:21-32). No independent OCR second opinion for this page;
  it rests on the per-line image read + the full 1879 cross-check
  (10a-10i exact) + content-fit/reciprocal resolution for 10j-10m.
  Session B: fresh independent 1920 fn-block crops (5× whole block +
  per-entry zooms) + fresh body-marker crops (3×, all 9) + fresh
  independent re-read of 1879 file p.629 Moroni 10 footnote block —
  all 9 Block 1 entries and all 9 body-marker placements UNCHANGED;
  entry "i" and "l" re-confirmed; 10j "o" / 10m "a" reads remain
  flagged for the editor. No text changes. Session C:
  insert_body_text.py 629 — librodm.txt 32963→33006 (+43);
  librodm_foot.txt 4973→4982 (+9 Block 1 entries, NO blank line / NO
  book header, rule 20). Página sequence 625..629 contiguous. Session
  D: generate_block2.py 629 appended 4639-4647 (librodm.txt
  33006→33015). 8 of 9 cross-refs auto-resolved: 4639→671, 4640→3744,
  4641→4240, 4642→4016, 4644→4352, 4645→4240, 4646→4590, 4647→4561.
  The KNOWN compound-Block-1-entry bug hit 4643 (10i = "Véase e, III
  Nefi 29; I Corintios 12:8-11.") — the script grabbed the "12" out
  of "I Corintios 12:8-11" and matched III Nefi *12*e (→ 3666)
  instead of III Nefi 29e, and dropped the "I Corintios" text. Fixed
  by hand: librodm.txt line 33011 = "4643: Véase 4016; I Corintios
  12:8-11." (matches the CLAUDE.md "compound Block 1 entry" warning
  and the page-573 precedent). Anchor↔Block-2 after append + fix: max
  anchor 4647 = max def 4647, contiguous 1..4647, no gaps/dupes; only
  the documented Jacob 2:15/812 def-without-anchor remains; no
  wrapped-Block-1-entry spurious-trailer (Notas tail ends cleanly at
  "4647: Véase 4561."). Session E: fresh full pptext report
  report_wsl_20260903e.html regenerated and walked end to end.
  SPELLCHECK: ZERO new page-629 suspects — every word in Moroni
  10:5-21 is common; "excesiva" (v.11) NOT flagged (valid RAE word,
  recurs throughout librodm.txt). NO permitted words.txt additions.
  Every other page-629 hit is a known structural false positive: the
  short-lines flood over the 40 body lines + 9 new Block 2 entries;
  the v.21→Notas boundary in the paragraph-level "unexpected paragraph
  end" list (page 629 is the last transcribed page, ending mid-verse
  10:21); the TOC "Dones del Espíritu 629" line. Dash check
  hyphen-minus: the 1 new Block 2 range hyphen ("I Corintios 12:8-11")
  is properly digit-flanked. Footnote check: 4643-4647 in the anchor
  bucket, 4641-4642 in the "footnotes" bucket (both coincidentally
  begin a wrapped line) — union 4639-4647 complete, contiguous, no
  dupes, no out-of-range. NO page-629 edit-distance / repeated-word /
  duplicate-line / adjacent-space / trailing-space / scanno /
  curly-quote / spaced-punctuation / special-situations / book-level /
  "full stop followed by unexpected sequence" findings. Jeebies
  clean. Letter-hyphen-letter blind-spot scan: 0 tokens in the
  page-629 segment. Whole-document mechanical sweeps all clean
  (check_spaced_punctuation librodm.txt 33015; check_footnote_punctuation
  librodm_foot.txt 4982; check_verse_indent librodm.txt; curly-quote
  scan of librodm.txt / librodm_foot.txt / page_629.txt all zero;
  anchor↔Block-2 only [812]). 1886 comparison — Moroni 10:5-9 and
  10:9-16 on 1886 file p.642 (book p.624), 10:17-21 on 1886 file
  p.643 (book p.625) — ALL of page 629's verses compared
  word-for-word. NO genuine 1920 deviations; NO errors in 1920.txt
  additions. Differences are all previously-established house style:
  (a) 1920 supplies acute accents 1886 omits throughout ("también/
  míos/según/manifestación/tengáis/acordéis/proporción" etc.) —
  accent modernization; (b) 1920 modernizes 1886's archaic accented
  forms — "fé"→"fe" (×6), "hé"→"he" (v.9), "miéntras"→"mientras"
  (v.19), "réino"→"reino" (v.21), "tuviéreis"→"tuviereis" (v.21); (c)
  v.9 "Porque, he aquí" — 1920 adds a house-style comma after
  "Porque" (1886 "Porque hé aquí" no comma) — page 625/626/628
  comma-addition precedent; (d) v.11 "fe excesiva" — 1886 prints "fé
  excesiva" TOO (shared reading); "excesiva" is a valid RAE word
  (feminine of "excesivo", here the archaic "exceeding/abundant"
  sense — modern BoM Moroni 10:11 "exceeding faith"); not
  pptext-flagged; NO permitted words.txt entry, NO errors-log entry
  (feedback_errors_log_diligence mirror case). feedback_narrow_space_
  vs_merge: nothing noticed on this page. FOR THE EDITOR (footnote
  cross-ref letter reads, not text errors): 10j "Véase o, Éther 4"
  and 10m "Véase a, Moroni 7" — the 1920 fn-block superscripts are
  illegibly over-inked; resolved by content-fit + reciprocal, but
  worth a direct look at the page if convenient. NO text changes to
  page_629.txt body or librodm.txt in Session E (the 4643 Block 2 fix
  was a Session D bookkeeping correction).

- **2026-09-03**: Sessions A–E run in one session for page 630 (Moroni
  10:21-32), first footnote 4648. NOTE: CLAUDE.md's "Next page: 629"
  line was stale — page 629 was already fully A–E complete (through
  footnote 4647, integrated into librodm.txt/librodm_foot.txt); page
  630 is the correct next page. Page 630 CONTINUES Moroni 10 (the last
  chapter of the Book of Mormon); it does NOT finish it — the page
  ENDS mid-verse 10:32 ("...y si por la gracia de Dios os hiciereis").
  Page 629 ended mid-verse 10:21 ("...ni podréis salvaros en el
  reino"), so page 630 OPENS mid-chapter with the continuation of v.21
  ("de Dios, si no tenéis fe;...") — "Página 630" on its own line,
  body text on the next line, NO blank line after the marker, NO
  heading (rule 1). Running header "630  LIBRO DE MORONI.  (CAP. X."
  discarded (rule 2). Body = 42 print/output lines. No chapter
  heading (Moroni 10 continues). Rule 7: 2 hyphen rejoins, both kept
  at end of first line — "pala-/bras" -> "palabras" (v.26); "pro-/
  fecias." -> "profecías." (v.28). Rule 8: 1 rebalance — v.30 line hit
  exactly 73 chars with both markers [4654]/[4655] inserted, "malo,"
  moved to next line. Rule 31: x16 body space-before-";" (plus one ":"
  and one "!") de-spaced (1920 spaces before ";" throughout). Rule 6:
  x6 sentence double-spaces collapsed (v.23 "padres:  Si", v.24
  "tierra.  Que", v.25 "solo.  Porque", v.26 "Dios.  Y digo", v.27
  "muertos?  Si", v.28 "profecias.  Y, he aqui"). No zero-width
  merges. v.23 "Si tenéis fe": the over-inked 10n superscript before
  "Si" was misread by Google OCR as an opening quote; 1920 prints NO
  quotation marks (nor a closing one at "mí."), 1886 also none —
  transcribed without quotes; word is "Si" (conditional), not "Sí"
  (tittle, no accent; matches 1886 "Si"). v.24 same for the 10o
  superscript before "Que". 11 markers, letters 10n-10x: 10n=[4648]
  "Si" (v.23); 10o=[4649] "Que" (v.24); 10p=[4650] "sabréis" (v.27);
  10q=[4651] "gritara" (v.27); 10r=[4652] "silbará" (v.28); 10s=[4653]
  "mostrará" (v.29); 10t=[4654] "buen" (v.30); 10u=[4655] "toquéis"
  (v.30); 10v=[4656] "levántate" (v.31); 10w=[4657] "no" (v.31, "no
  seas confundida"); 10x=[4658] "alianzas" (v.31). Block 1: 10n
  "Moroni 7:33."; 10o "Véase 2d, Moroni 7."; 10p "Véase g, II Nefi
  33."; 10q "Véase s, Mormón 5."; 10r "Véase d, II Nefi 29."; 10s
  "Véase g, II Nefi 33."; 10t "Véase o, Éther 4."; 10u "II Nefi
  18:19."; 10v "Isaías 52:1-2."; 10w "Éther 13:8."; 10x "Véase j, III
  Nefi 15." Chapter continues within Book of Moroni -> Block 1 gets NO
  blank line / NO book header (rule 20). MANDATORY i/l/1 check: entry
  letters 10n-10x — none i/l/1; cross-ref targets 2d/g/s/d/g/o/j —
  none i/l/1. IMPORTANT CORRECTION to page 629's Session A note: 1879's
  Moroni 10 footnote set does NOT "stop at i" — it continues on 1879
  file p.630 (letters j-q) and file p.631 (letters r-2c), and its
  letter sequence aligns EXACTLY, letter-for-letter, with 1920's
  (a-2c). All 11 page-630 entries confirmed three ways against 1879 —
  by footnote letter, by target content, and by body-marker
  placement. 10x: Google OCR read the cross-ref target letter as "i",
  but 1879 file p.631 prints "x, see j, III. Nep. 15." with a clear
  descender "j", AND 1920's own III Nefi 15j [3702] = "III Nefi
  5:24-26; 16:5; Véase e, I Nefi 15." is an exact content-fit for the
  marker on "alianzas que el Eterno Padre ha hecho contigo, oh casa
  de Israel" (covenants to the house of Israel), whereas III Nefi 15i
  [3701] = "III Nefi 12:46-47." (law of Moses) does not fit —
  resolved 10x = "Véase j, III Nefi 15." Rule 22/23/34: 10u "II Nefi
  18 : 19" -> "II Nefi 18:19"; 10v "Isaías 52 : I, 2" -> "Isaías
  52:1-2" (colon de-spaced; Roman "I" -> digit "1"; consecutive
  verses -> hyphen range); 10w "Éther 13 : 8" -> "Éther 13:8".
  Google-text cross-check AVAILABLE (file 652): only body diffs were
  the two over-inked-superscript-as-quote artifacts at v.23/v.24
  (auto-dismissed category). Session B: fresh independent 1920
  fn-block + body-marker crops (5x) and fresh 1879 file p.630/p.631
  crops — all 11 Block 1 entries and all 11 markers UNCHANGED; 10x "j"
  re-confirmed from the clean 1879 "j" glyph. No text changes.
  Session C: insert_body_text.py 630 — librodm.txt 33015->33059 (+44);
  librodm_foot.txt 4982->4993 (+11, NO blank line / NO book header,
  rule 20). Página sequence 623..630 contiguous; "Página 630" appears
  once. Session D: generate_block2.py 630 appended 4648-4658
  (librodm.txt 33059->33070) — all 11 cross-refs resolved cleanly, no
  unresolved letter-forms, no wrapped/compound-entry bugs. 4648 Moroni
  7:33.; 4649->4590 (Moroni 7-2d); 4650/4653->790 (II Nefi 33g, whose
  own text ends "...Moroni 7:35; 10:27" — reciprocal); 4651->4149
  (Mormón 5s); 4652->741 (II Nefi 29d, ends "...Moroni 10:28" —
  reciprocal); 4654->4352 (Éther 4o); 4655 II Nefi 18:19.; 4656 Isaías
  52:1-2.; 4657 Éther 13:8.; 4658->3702 (III Nefi 15j). Anchor<->Block-2:
  max anchor 4658 = max def 4658, contiguous 1..4658, no gaps/dupes,
  only the documented Jacob 2:15/812 def-without-anchor. Session E:
  fresh full pptext report report_wsl_20260903e.html walked end to
  end. TRANSCRIPTION MISREAD FIXED (rule 12): v.27 Session A had "!No
  os" (inverted exclamation) before "No os he declarado..."; the 1920
  print sets an inverted QUESTION mark there (26x zoom — curved
  hook, dot above; sentence closes "?" at "...los muertos?"), 1886
  and the modern LDS Spanish edition also read the question mark —
  corrected in pages/page_630.txt AND librodm.txt (line length
  unchanged); our reading error, NOT a 1920 defect, so no errors-log/
  permitted-words entry. SPELLCHECK: sole new page-630 suspect
  "perfeccionáos" (v.32) -> ADDED to permitted words.txt (1290 lines),
  NO errors-in-1920 entry — valid imperative+enclitic construction,
  1886 file p.644 prints the identical accented form (SHARED reading),
  retained stress accent is a standard 19th-c. orthographic
  convention; modern form "perfeccionaos" (RAE-form research + modern
  edition "perfeccionaos en él"); feedback_errors_log_diligence
  homework done. Every other page-630 pptext hit is a known
  structural false positive (short-lines flood over 42 body + 11
  Block 2 lines; v.32->"Notas" boundary in "unexpected paragraph end"
  — page 630 is the LAST transcribed page, ending mid-verse 10:32).
  NO page-630 findings in edit-distance / repeated-word / duplicate-
  line / adjacent-space / trailing-space / scanno / curly-quote /
  spaced-punctuation / special-situations / book-level / "full stop
  followed by unexpected sequence" (v.24 "tierra. Que si" NOT flagged
  — 1920 capitalises "Que", so not the period+lowercase pattern).
  Jeebies clean. Dash check: only new Block 2 range hyphen "Isaías
  52:1-2" is digit-flanked; letter-hyphen-letter blind-spot scan of
  the page-630 segment = 0 tokens. Whole-document mechanical sweeps
  all clean (check_spaced_punctuation librodm.txt 33070;
  check_footnote_punctuation librodm_foot.txt 4993; check_verse_indent
  librodm.txt; curly-quote scan of librodm.txt / librodm_foot.txt /
  page_630.txt all zero; anchor<->Block-2 only [812]). 1886 comparison
  — Moroni 10:21-28 on 1886 file p.643 (book p.625), 10:29-32 on file
  p.644 (book p.626) — ALL of page 630's verses compared word-for-
  word. NO genuine 1920 deviations requiring an errors-in-1920 entry.
  Differences all previously-established house style: (a) 1920
  supplies acute accents 1886 omits throughout; (b) 1920 modernizes
  1886's archaic accented forms — "fé"->"fe", "réino"->"reino",
  "segun"->"según", "hé"->"he", "entónces"->"entonces",
  "hiciéreis"->"hiciereis", "fuéron"->"fueron", "cáusa"->"causa"; (c)
  1920 adds house-style commas 1886 omits — v.24 "Ahora, hablo", v.28
  "Y, he aquí" (page 625/626/628/629 precedent); (d) 1920 modernizes
  spelling "trages"->"trajes" (v.31); (e) 1920 accents demonstratives
  "éste" (v.25), "aquéllos" (v.26) where 1886 does not — established
  1920 house pattern, not pptext-flagged, no permitted-words / no
  errors-log entry. FOR THE EDITOR (non-blocking, not logged): (i)
  v.24 "hablo á todos los extremos de la tierra. [4649]Que si..." —
  1920 sets a full stop + capital "Que" where 1886 (file p.643) and
  the modern edition use a colon + continuation; 1920 is internally
  consistent (period paired with a capital) and it is NOT the
  period+lowercase error pattern, so left as printed and flagged only
  as a 1920/1886 divergence to be aware of. (ii) the 1920 Moroni 10
  fn-block superscript cross-ref letters on this page are heavily
  over-inked, but all 11 were pinned exactly by the full 1879
  cross-check (1879 file pp.630-631) — no letter rests on the 1920
  glyph alone. feedback_narrow_space_vs_merge: nothing noticed on
  this page. Text changes in Session E: only the v.27 exclamation->
  question mark fix (page_630.txt + librodm.txt).
- **2026-09-03**: Sessions A–E run in one session for page 631 (Moroni
  10:32-34), first footnote 4659. **THIS IS THE FINAL PAGE OF THE BOOK
  OF MORMON.** Page CONTINUES and FINISHES Moroni chapter 10 (the last
  chapter). Page 630 ended mid-verse 10:32 ("...y si por la gracia de
  Dios os hiciereis"), so page 631 OPENS mid-chapter with the
  continuation of v.32 ("perfectos en Jesu Cristo, de ningún modo
  negaréis entonces el poder de Dios.") — "Página 631" on its own line,
  body text on the next line, NO blank line after the marker, NO
  heading (rule 1). Body = 12 print lines; ends "...vivos y muertos.
  Amén." (Moroni 10:34). Nothing printed after it — no "FIN", no
  colophon (mid/bot crops blank; 1886 file p.644 ends the same way with
  only a decorative flourish after "Amen."). Running header "CAP. X.)
  LIBRO DE MORONI. 631" discarded (rule 2). No page-boundary word split
  (rule 10 N/A — page 630 ended on complete word "hiciereis"). No
  hyphen rejoins (rule 7 N/A). Rule 8 cascade: the 5 footnote markers
  pushed raw lines 9-11 past 72 chars, cascading three word-moves
  ("reunan"+[4662] -> next line start; "encontraros" -> next line
  start; "Eterno de" -> last line start); output stays 12 body lines,
  matching the image. Rule 6: 2 sentence double-spaces collapsed (v.34
  "de todos.  Pronto", "muertos.  Amén."). No zero-width merges. Rule
  31 N/A (no body semicolons this page; commas/periods all tight).
  Rule 36: a faint speck between "34." and "Ahora" (v.34) — Google OCR
  (google_text_1920/page_0653.txt) AND 1886 file p.644 both print
  "34. Ahora" with no mark; treated as stray debris, transcribed
  without it, NOT logged. 5 markers: 10y=[4659] "ningún" (v.32);
  10z=[4660] "derrame" (v.33); 10-2a=[4661] "paraíso" (v.34);
  10-2b=[4662] "reunan" (v.34); 10-2c=[4663] "agradable" (v.34).
  Block 1: 10y "Véase e, III Nefi 29."; 10z "Véase f, II Nefi 2.";
  10-2a "Véase l, II Nefi 9."; 10-2b "Véase d, II Nefi 2."; 10-2c
  "Jacob 6:13." Same book, same chapter (Moroni 10 continues) -> Block
  1 gets NO blank line / NO book header (rule 20). MANDATORY i/l/1
  check — 10-2a's cross-ref target letter: the 1920 fn-block
  superscripts on this page are ALL heavily over-inked blobs (entry
  letters y/z/2a/2b/2c AND every "Véase" target letter unreadable from
  the 1920 glyph alone), so all 5 entries were resolved entirely from
  1879 file p.631 (Moroni 10 fn continuation, letters r-2c, clean
  italic type): "y, see e, III. Nep. 29. z, see f, II. Nep. 2. 2a,
  see l, II. Nep. 9. 2b, see d, II. Nep. 2. 2c, Jacob 6:13." The 2a
  target letter in 1879 is an unmistakable "l" — plain tall ascender,
  no dot, no descender, no crossbar — contrasting the dotted,
  below-baseline "j" of "x, see j," directly above it. NOT "i".
  Content-fit: 10-2c "Jacob 6:13" on "el agradable tribunal del gran
  Jehová" — Jacob 6:13 = "hasta que os encuentre ante la agradable
  barra de Dios" ("the pleasing bar of God"), exact match. 10-2a
  "II Nefi 9" (Jacob's resurrection-and-paradise discourse) on "el
  paraíso de Dios" — strong fit for "l". Session B: fresh independent
  1920 fn-block crop (8x) + fresh body-marker crops (5x, both bands) +
  fresh independent 1879 file p.631 crop — all 5 Block 1 entries and
  all 5 markers UNCHANGED; 10-2a "l" re-confirmed. Session C:
  insert_body_text.py 631 — librodm.txt 33070->33084 (+14: 13 body
  lines + separator); librodm_foot.txt 4993->4998 (+5, NO blank line /
  NO book header, rule 20). Página sequence 620..631 contiguous.
  Session D: generate_block2.py 631 appended 4659-4663 (librodm.txt
  33084->33089) — no unresolved warnings, no wrapped-Block-1-entry
  spurious-trailer bug (none of the 5 entries wrap). Cross-refs:
  4659 -> 4016 (III Nefi 29e, whose text = "Mormón 9:7-11,15-26;
  Moroni 7:35-38; 10:19-29." — cites this very chapter's preceding
  verses, reciprocal); 4660 -> 265 (II Nefi 2f); 4661 -> 369 (II Nefi
  9l = "Alma 40:12,14; IV Nefi 1:14; Moroni 10:34." — cites this exact
  verse, reciprocal); 4662 -> 263 (II Nefi 2d); 4663 = direct "Jacob
  6:13." Anchor<->Block-2: max anchor 4663 = max def 4663, contiguous
  1..4663, no gaps/dupes; only the documented Jacob 2:15/812
  def-without-anchor remains. Session E: fresh full pptext report
  report_wsl_20260903e2.html regenerated and walked end to end.
  SPELLCHECK: ZERO new page-631 suspects ("perfeccionáis", "negaréis",
  "vengáis", "seréis", "reunan" all unflagged) — NO permitted words.txt
  additions. Every other page-631 hit is a known structural false
  positive: the short-lines flood over the 12 body lines + 5 new Block
  2 entries; the page 630/631 mid-verse boundary ("...os hiciereis" +
  blank + "Página 631") in the paragraph-level "unexpected paragraph
  end" list. The book now ends on a complete sentence so page 631's own
  last line is NOT flagged. NO page-631 edit-distance / repeated-word /
  duplicate-line / adjacent-space / trailing-space / character /
  scanno / curly-quote / spaced-punctuation / special-situations /
  book-level / "full stop followed by unexpected sequence" findings.
  Jeebies clean. Footnote check: union of both buckets = 4643-4663
  contiguous, no dupes, no out-of-range. Dash check: the 5 new Block 2
  entries have NO hyphens (bare-number targets + direct "Jacob 6:13").
  Letter-hyphen-letter blind-spot scan of the page-631 segment: 0
  tokens. Whole-document mechanical sweeps all clean
  (check_spaced_punctuation librodm.txt 33089; check_footnote_punctuation
  librodm_foot.txt 4998; check_verse_indent librodm.txt; curly-quote
  scan of librodm.txt / librodm_foot.txt / page_631.txt all zero;
  anchor<->Block-2 only [812]). 1886 comparison — Moroni 10:32-34 all
  on 1886 file p.644 (book p.626); the ENTIRE text of page 631 compared
  word-for-word. NO genuine 1920 deviations; NO errors in 1920.txt
  additions. Differences all previously-established house style: (a)
  1920 supplies acute accents 1886 omits — "perfeccionáis"/"negáis"/
  "vengáis"/"ningún" for 1886 "perfeccionais"/"negais"/"vengais"/
  "ningun"; (b) 1920 modernizes 1886's archaic forms — "entonces"<-
  "entónces" (x2), "remisión"<-"remision", "aire"<-"áire", "paraíso"<-
  "paraiso"; (c) "Jesu Cristo" unhyphenated vs 1886 "Jesu-Cristo" —
  documented legitimate archaic form (feedback_jesu_cristo_hyphen); (d)
  "Amén" vs 1886 "Amen" — acute-accent modernization, document-wide;
  (e) v.34 sentence double-spaces present in 1886 too — collapsed per
  rule 6 (transcription normalization). 1886 also ends the Book of
  Mormon here (flourish after "Amen.", no "FIN" text). Rule 36 recheck
  of the "34. Ahora" speck against 1886: 1886 prints clean "34. Ahora",
  matching Google's silence — confirmed stray debris. feedback_narrow_
  space_vs_merge: nothing noticed on this page. NO text changes to
  page_631.txt or librodm.txt in Session E.
- **THE BOOK OF MORMON BODY TRANSCRIPTION IS NOW COMPLETE (pages
  437-631, Sessions A–E).** Remaining project-level cleanup, per
  CLAUDE.md: (1) run `generate_block2.py --fix-unresolved` as the final
  whole-document cross-reference cleanup pass (re-resolves any Block 2
  entries that were stuck on not-yet-transcribed targets when first
  generated); (2) the blanket-suppression pptext re-run with `permitted
  words.txt` set aside, cross-referencing every fresh flag against
  `errors in 1920.txt` (see the orthography-check skill). Chapter
  emailing (Session F) also continues independently.
- **2026-09-03**: Final cross-reference cleanup pass —
  `generate_block2.py --fix-unresolved` run on the completed document
  (all 631 pages transcribed). Script re-resolved 0 entries: every
  Block 2 cross-reference that CAN be resolved against librodm_foot.txt
  already was, page-by-page during each page's Session D (pages were
  transcribed in book order, so most forward-references were already
  resolvable by the time their targets landed). Two letter-form
  clauses remain, both examined by hand:
  (1) **4341** (Moroni 4d) — `Véase s, I Nefi 13; Mormón 8:14; Moroni
  10:1-2.` The script's parser can't handle a `Véase <letter>, <Book>
  <Chapter>` clause followed by `;` + more direct citations before the
  period (the documented COMPOUND-entry limitation). Resolved by hand:
  I Nefi 13 letter s = footnote 102 (librodm_foot.txt: `13s, 102: II
  Nefi 27:6-26; III Nefi 16:4; Mormón 8:4.`). Block 2 line changed to
  `4341: Véase 102; Mormón 8:14; Moroni 10:1-2.` (librodm.txt only;
  Block 1 keeps its letter form per rule 17). librodm.txt stays 33089
  lines.
  (2) **4013** (III Nefi 29b) — `Véase 2j, III Nefi 15.` GENUINELY
  UNRESOLVABLE and ALREADY DOCUMENTED: `errors in 1920.txt` line 766
  (logged when page 570 was transcribed) has the full write-up — III
  Nefi 15's footnote letters run only a-v (notes 3693-3714), so no "2j"
  target exists; 1879 file p.550 prints the identical "b, see 2j, III.
  Nep. 15." so the error is inherited from the 1879 Pratt edition, not
  1920-only; the intended target is note "j" (3702, the covenant/
  gathering citation) — matching sibling entries 29c/29g/29i which all
  correctly read "Véase j, III Nefi 15", and chapter 16's own "16h".
  Preserved as printed ("2j") per rule 32, so it correctly stays in
  letter form in Block 2 too. No new action from this pass.
  Post-run integrity: max Block 2 def 4663, contiguous 1..4663, no
  duplicate defs, no anchors without a def; only the long-documented
  Jacob 2:15/812 def-without-anchor remains.
- **2026-09-05**: Editor correction — Helamán 13:22 "envidia. de
  antipatías" -> "envidia, de antipatías". This spot was logged in
  `errors in 1920.txt` (period-for-comma, grouped with the Alma
  43:9 / 48:6 / 49:3 / 52:34 / 57:6 / Helamán 5:2 / 10:15 / 13:21
  pattern), on the strength of "1886 has a comma" alone — the Google-OCR
  and stroke-weight-zoom due diligence per feedback_stray_mark_google_
  ocr_order was never done. Editor reviewed the high-res scan and read
  the mark as defective / ink-blobbed type, not a deliberate period.
  Corroboration: the 1920 PDF's own Google-OCR text
  (`google_text_1920/page_0493.txt`, file page 493 / book page 471)
  reads "jactancia, vanidad, envidia, de antipatías, de malicia, de
  perse-" — a comma; 1886 reads a comma; grammar requires a mid-list
  comma; and page 471 carries other damaged-comma / print-quality
  artifacts in the same verses ("requezas" for "riquezas", "aunuciado"
  for "anunciado", both still logged). Changes: comma written in
  `librodm.txt` (line 21146, length unchanged) and `pages/page_471.txt`
  (line 37); that page's Corrections log entry rewritten from
  "preserved as printed; a period appears..." to the defective-comma
  finding; the `errors in 1920.txt` entry removed. NOT touched: the
  Helamán 13:21 "también. porque" entry one line earlier (same page,
  same print-quality cluster) — left as logged pending its own editor
  look. `workspace/fulltext_pptext_review_20260903.md` §3 updated
  (17 -> 16 already-logged period-for-comma entries).
- **2026-09-05b**: Editor correction — IV Nefi 1:14 "pasado ya. cuando"
  -> "pasado ya, cuando" (same treatment as Helamán 13:22 earlier
  today). This spot was logged in `errors in 1920.txt` as a
  period-for-comma error; page 550's Session E had re-zoomed it at
  15-20x from the 400dpi crop and called the mark "marca redonda sin
  cola, inequívocamente un punto", overriding a Google-OCR comma read.
  Editor reviewed the high-res scan and saw a descender / leftward hook
  on the mark. Corroboration: the 1920 PDF's own Google-OCR
  (`google_text_1920/page_0572.txt`, file page 572 / book page 550)
  reads "años habían pasado ya, cuando los discípulos de Jesús, todos"
  — a comma; 1886 reads a comma; grammar requires a mid-sentence comma;
  page 572 is a poor-quality print ("ordenzas", "Sénor", "ocurrio" all
  on it). Per CLAUDE.md the 400dpi crop is known to lose exactly this
  detail. Changes: comma in `librodm.txt` (line 24576, length
  unchanged) and `pages/page_550.txt` (line 42); that page's
  Corrections notes updated in three places (item 7, the Session E
  re-zoom block, the "Both added to errors in 1920.txt" bullet); the
  `errors in 1920.txt` entry removed. NOT touched: the sibling IV Nefi
  1:2 "ni disputas. y obraron" entry (`errors in 1920.txt`, same page)
  — editor looked and did not find comma evidence there; stays logged.
  Also corrected `workspace/fulltext_pptext_review_20260903.md` §3: IV
  Nefi 1:2 had been mis-listed there as "not yet logged" (it is logged,
  line 772) — moved to the logged list; the unlogged period-for-comma
  count is now 8, not 9.
- **2026-09-05c**: Helamán 9:4 "he aquí." period-for-comma — 1886
  check done at editor request. 1886 (pages_1886/page_0474.png, book
  page 456 / file 474) prints "Y ahora hé aquí, que cuando hubiéron
  visto esto" — a COMMA after "hé aquí" (and "cuando" spelled
  correctly, no comma between "ahora" and "hé"). 1920 prints
  "Y ahora, he aquí. que caundo hubieron visto esto". Unlike Helamán
  13:22 and IV Nefi 1:14 (both reversed earlier today as defective
  commas): here the 1920 mark is a genuine round baseline period with
  no descending hook (confirmed at ~18x zoom), and the 1920 PDF's own
  Google-OCR (google_text_1920/page_0481.txt) also reads a period
  ("he aquí. quecaundo"). So this stays a genuine 1920 period-for-comma
  error, preserved as printed (rule 32); NO text change. An entry
  already existed in errors in 1920.txt (line 560, terse:
  "he aquí. (he aquí,) (hé aquí, en 1886)"); ENRICHED it with the full
  1886 citation, the genuine-period determination, the Google-OCR
  corroboration, and the cross-reference to the established
  Alma/Helamán/III Nefi pattern.
  Also corrected workspace/fulltext_pptext_review_20260903.md §3: its
  "8 not yet logged" list was WRONG — a proper recheck shows ALL of
  those (Helamán 9:4, 9:6; III Nefi 1:13, 9:22, 24:15, 28:15; Mormón
  4:11; Éther 6:12) are already in errors in 1920.txt. The original
  grep-based "logged?" detection missed them because it searched for
  long distinctive phrases that don't match the terse errors-log entry
  format. §3 now correctly states there is NO unlogged period-for-comma
  backlog. The one still-open item in that class is III Nefi 1:13
  "por. boca" (errors line 627), which carries a standing unresolved
  editor note that it may be a scan speck rather than a real period.
- **2026-09-05d**: Two more editor reversals in the period-for-comma /
  stray-mark class.
  (1) **Helamán 9:6 "al pueblo. levantanado" -> "al pueblo, levantanado".**
  Editor reviewed the high-res scan and identified the mark as a comma
  with a print defect: page 481 / this field of view carries several
  ink-and-dust letter defects (a stray speck before "su" in v.6, broken
  "m" in "mismo"/"miedo", broken "inm" in "inmediatamente"). Grammar
  requires a comma (the gerund clause "levantando el grito..." attaches
  to "al pueblo"); 1886 prints a comma. Google-OCR of the 1920 PDF read
  a PERIOD here (unlike Helamán 13:22 / IV Nefi 1:14, where Google also
  read a comma) — noted, but the editor's higher-res read + grammar +
  1886 + this page's condition outweigh a single Google period-read on
  a print this degraded. Comma written in librodm.txt (line 20605) and
  pages/page_459.txt (line 28); that page's Corrections entry rewritten;
  errors in 1920.txt entry ("Helamán 9:6 al pueblo.") removed. The
  sibling "Helamán 9:6 levantanado (levantando)" spelling entry stays.
  (2) **III Nefi 1:13 "por. boca" -> "por boca".** The dot between "por"
  and "boca" was a long-standing unresolved item — its errors-in-1920
  entry already carried a 2026-07-21 editor note that connected-
  components analysis at native resolution found the mark smaller
  (40px^2 vs 46-50) and 2px higher off the baseline than genuine
  periods on the same pages, "evidencia cuantitativa" for a scan
  speck. Editor has now done the manual image review and confirmed:
  STRAY MARK, not printed type. The dot was REMOVED from the text
  (librodm.txt line 21616, pages/page_482.txt line 29 -> "he anunciado
  por boca de mis santos profetas"); the errors in 1920.txt entry
  removed; page_482.txt's three relevant Corrections blocks (the [v.13]
  entry, the Session E 1886-check bullet, and the 2026-07-21 reopened-
  unresolved block) all updated to the resolved state. 1886 prints
  "por boca" with no punctuation.
  errors in 1920.txt: 912 -> 910 lines. review file
  workspace/fulltext_pptext_review_20260903.md §3 updated — four
  reversals now (13:22, 1:14, 9:6, 1:13); the rest of the
  period-for-comma category confirmed genuine and staying logged;
  nothing left open in that section.
- **2026-09-05e**: Two more editor reversals, plus a general rule for
  `errors in 1920.txt` scope.
  **RULE (editor):** only *textual* errors go in `errors in 1920.txt`
  — wrong / misspelled / missing words, or a punctuation mark the
  typesetter genuinely *set* wrong. *Print defects* — stray specks,
  weak / broken / half-inked type — are fixed silently in the
  transcription and NOT logged.
  (1) **III Nefi 9:22 "quienquiera. que" -> "quienquiera que".** Editor
  ruled the dot a STRAY SPECK (small, floating mid-height in the word
  gap; Google-OCR of the 1920 PDF, google_text_1920/page_0527.txt,
  reads "quienquiera que" with no mark — rule-36 silence). Dot removed
  from librodm.txt (line 22584) and pages/page_505.txt (line 2);
  errors-log entry deleted; page_505.txt Corrections updated. The
  "época" (v.7) spelling entry on the same page stays — it's a textual
  error.
  (2) **III Nefi 24:15 "orgullosos. sí" -> "orgullosos, sí".** Editor
  reviewed the high-res scan: the character is very weak / partly
  inked, its lower piece (and part of even a period) missing — a
  misprinted character, most likely a comma. 1886 (book p.535/file
  553) prints a comma; grammar requires one. Google-OCR had read a
  period and Session A's 400dpi zoom had called it "un punto normal, no
  una coma mal impresa" — both overridden by the editor's better scan.
  Comma written in librodm.txt (line 24061) and pages/page_538.txt
  (line 38); errors-log entry deleted; page_538.txt Corrections
  updated in two places.
  errors in 1920.txt 910 -> 908 lines. Helamán 9:4's entry (line 560)
  had its "mismo patrón" cross-reference list trimmed to drop the
  now-reversed III Nefi 9:22 (22:17 stays — still a valid logged
  entry). review file §3 updated — SIX
  reversals now in the period/speck class (13:22, 1:14, 9:6, 1:13,
  9:22, 24:15); the rest confirmed genuine textual errors and staying
  logged; the new textual-vs-print rule recorded there too.
- **2026-09-05f**: Three more editor reversals in the period/speck
  class — all print defects, per the 2026-09-05e rule (only textual
  errors go in errors in 1920.txt).
  (1) **III Nefi 28:15 "poder. contemplar" -> "poder contemplar".**
  Editor: the mark is visibly LARGER than a real period -> stray
  speck. It sat where grammar admits nothing ("para poder contemplar"
  = "to be able to behold"); 1920 Google-OCR actually read it as a
  comma (google_text_1920/page_0567.txt); 1886 (book p.542/file 560)
  prints "poder contemplar" with nothing between. Mark removed from
  librodm.txt (24362) + pages/page_545.txt (37); errors entry deleted;
  page_545 Corrections paragraph rewritten (the earlier note had
  called it "un punto genuino, redondo").
  (2) **Mormón 4:11 "corazón. se" -> "corazón se".** Editor: stray
  speck, not a period. 1920 printed "corazón.se" jammed together, no
  following capital; Google-OCR read "corazón.se"; 1886 (book p.558/
  file 576) reads "todo corazon se endureció" with normal spacing, no
  mark. Speck removed from librodm.txt (25070) + pages/page_562.txt
  (5); errors entry deleted; page_562 Corrections updated.
  (3) **IV Nefi 1:2 "ni disputas. y obraron" -> "ni disputas, y
  obraron".** Editor: print defect — the neighbouring "s" of
  "disputas" is also damaged. 1920 Google-OCR (google_text_1920/
  page_0572.txt) AND 1886 (book p.546/file 564) both read a comma;
  grammar wants one. Comma written in librodm.txt (24537) +
  pages/page_550.txt (3); errors entry deleted; page_550 Corrections
  updated in four places (this had been the last un-reversed member of
  the IV Nefi 1 pair — see the 2026-09-05b entry).
  errors in 1920.txt 908 -> 905 lines. review file §3: NINE reversals
  now (13:22, 1:14, 9:6, 24:15, 1:2 — defective commas; 1:13, 9:22,
  28:15, Mormón 4:11 — stray specks). librodm.txt unchanged at 33089;
  check_spaced_punctuation clean; anchor<->Block-2 unchanged (max
  4663, only [812]).
- **2026-09-05g**: Review file §4 ("line begins with stranded
  punctuation") — editor reviewed, clear of issues. The three
  librodm.txt lines were already in the corrected form (`;`/`,` bound
  to the preceding word: Éther 3:14 "...eternamente;", Éther 8:23
  "...ganancias;" and "...exterminación,"). Found the page files out
  of sync — pages/page_583.txt (line 25-26) and pages/page_594.txt
  (lines 11-15) still had the old form with the mark opening the
  wrapped line. Synced both page files to match librodm.txt and
  updated their Corrections notes (which had argued a "decorative
  space" kept the mark detached from the rejoined hyphenated word —
  superseded; per rule 31 a space-stripped `;`/`,` binds left, and a
  line must not start with one). No errors in 1920.txt change (pure
  transcription formatting). check_spaced_punctuation clean on
  librodm.txt + both page files (page_594's 4 hits are all historical
  quotes inside its Corrections log). §4 marked DONE.
- **2026-09-05h**: Helamán 11:3 "septusgésimo-tercio" — editor verified
  the error in the 1920 image; 1886 check done at editor request.
  1886 (pages_1886/page_0479.png, book page 461/file 479) prints
  "septuagésimo-tercio" correctly at v.3, and "en el año septuagésimo
  segundo" correctly at v.1 of the same chapter. 1920's "septusgésimo"
  has an "s" where "a" belongs (confirmed at ~13x zoom). RAE has only
  "septuagésimo". The same 1920 page writes "septuagésimo-" correctly
  seven other times (vv.1, 6, 8, 17, 21 + two more), so it's an
  isolated slip, not a house spelling. An errors in 1920.txt entry
  ALREADY existed (line 572, terse: "septusgésimo-tercio
  (septuagésimo-tercio) (septuagésimo-tercio en 1886; ...)"); ENRICHED
  it with the full 1886 citation, the zoom confirmation, RAE, and the
  same-page consistency evidence. NO text change (preserved as
  printed, rule 32 — it's a textual error, correctly logged). The
  review file's §5A note that this was "Not in errors in 1920.txt"
  was wrong (same phrase-grep detection failure as the §3 items) —
  corrected. Sibling Helamán 11:2 "detrucción" (destrucción) is also
  already logged (line 571) — no action.
- **2026-09-05i**: Compound-word hyphen fixes (review file §5A) — editor
  did the librodm.txt edits; synced the page files.
  **Mosiah 11:11 "sumosacerdotes" -> "sumo-sacerdotes":** in the 1920
  image "sumo-sacerdote" straddled a line break and Session A dropped
  the hyphen when rejoining. Editor restored it in librodm.txt (line
  8757; pre-437 text, no page file). **No errors in 1920.txt entry
  exists or is needed** — a transcription slip, not a 1920 defect.
  Distinct from the Alma 13:9-10 "Sumo Sacerdotes"->"Sumo-Sacerdotes"
  entries (opposite error, different spot; those stay).
  **Also fixed by the editor, same class (compound ordinal / compound
  noun split across a line break at its own hyphen -> rejoined onto one
  line, hyphen kept):** Helamán 6:1 "sexagésimo-segundo" (librodm
  20139), Helamán 6:14 "sexagésimo-quinto" (20193), Helamán 6:33
  "sexagésimo-octavo" (20286), III Nefi 6:22 "[3505]sumo-sacerdote"
  (22237-22238, marker moved down). Synced pages/page_449.txt,
  page_450.txt, page_452.txt, page_496.txt to match librodm.txt and
  added/updated their Corrections notes (page_496's Session A note had
  deliberately kept the v.22 split at the hyphen — superseded; 1886
  also hyphenates there, no errors-log entry). check_lines clean on all
  four page files' body text and on librodm.txt (0 over 72, 0 trailing
  hyphens); check_spaced_punctuation clean. librodm.txt 33089 -> 33088
  (one line absorbed at Helamán 6:14 where "quinto." had been alone on
  its own line). review file §5A: these five items marked DONE; still
  open there: Bienamado/Bien-amado consistency.
- **2026-09-05j**: Two more review-pass items (editor finished §5A/§5B,
  started §5C).
  (1) **Helamán 8:21 "ha-sido" -> "ha sido"** (§5A). Editor confirmed
  the mark between "ha" and "sido" is a STRAY SPECK, not a printed
  hyphen — 1920 itself writes "ha sido destruida" correctly one clause
  earlier in the same verse. Session A had preserved it as printed
  ("stray hyphen ... verify against 1886") and it was logged. Speck
  removed from librodm.txt (line ~20541) + pages/page_458.txt (line 8);
  page_458 Corrections updated; errors in 1920.txt entry
  ("Helamán 8:21 no ha-sido destruida") deleted. Print defect, not
  logged. Tenth print-defect reversal in this pass.
  (2) **Footnote 1 Nefi 3d / fn 15 "II Crónicas 36, 14-20"** (§5C).
  Editor verified the 1920 print genuinely sets a COMMA where the
  chapter:verse colon belongs. Corroboration: every other citation in
  I Nefi 3's footnote block uses a colon ("Josué 18:6,10", "Jueces
  20:9", "I Nefi 2:4", "I Nefi 1:3", "Mosíah 1:4"), and 1920's own
  notes 1c/1d/1g cite this same II Chronicles 36 passage correctly as
  "36:15-16 / 36:17-20 / 36:16"; confirmed at zoom
  (pages_1920/page_0028.png). 1886 has no footnote apparatus; 1879's
  equivalent "d" cites different content (translation divergence, rule
  26). This is a faithful transcription of a genuine 1920 misprint, so
  the text is PRESERVED AS PRINTED in both Block 1 (librodm_foot.txt
  line 22) and Block 2 (librodm.txt Notas) and a NEW errors in 1920.txt
  entry was added, in I Nefi 3 position ("Footnote 1 Nefi 3d, 15 'II
  Crónicas 36, 14-20' ('II Crónicas 36:14-20') (...)").
  review file §5A / §5B / §5C rows updated; CLAUDE.md status updated.
  Editor will commit and push after this.
