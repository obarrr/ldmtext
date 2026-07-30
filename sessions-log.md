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
