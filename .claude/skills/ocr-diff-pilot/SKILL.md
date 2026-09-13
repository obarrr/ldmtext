---
name: ocr-diff-pilot
description: Verifies librodm.txt against the 1920 PDF's own embedded OCR text for book pages 1-631 (the whole book). Originally scoped to 1-436 (the pre-Session-A-E range never covered by the tracked per-page pipeline), extended 2026-09-12 to also re-check 437-631 since this diff catches integration-stage errors the per-page pipeline can miss. Use when the user asks to "check pages NNN-NNN", "run the OCR diff", "continue the pilot", or similar, for any page 1-631.
---

# OCR-diff pilot — pages 1-631 verification

## Why this exists

`librodm.txt` contains the entire Book of Mormon (book pages 1-631), but the tracked
Session A-E per-page image-verification pipeline (see the other 6 skills in this
directory) only ever covered pages 437-631 — `sessions-log.md`'s earliest entry is
"pages 453-460," and individual `pages/pageNNN.txt` working files exist only for
437-631. Pages 1-436 (1 Nefi through most of Alma, ~430 pages) got *some* earlier
editorial attention (`errors in 1920.txt` has hundreds of entries spanning those
books) but never this project's image-reverification pipeline, and never the
Google-OCR crosscheck tool (`extract_google_text.py`/`check_google_crosscheck.py`,
added 2026-07-25, postdates that phase of work). This pilot, started 2026-09-10,
methodically works through that gap in batches.

**Full history, methodology detail, resource-cost notes, and the complete
batch-by-batch findings log live in `workspace/diff1920ocr-trans.md` — read it before
starting a new batch** to pick up exactly where the last one left off (it has a
running total at the end of each batch section) and to see the established
false-positive taxonomy in full with real examples.

**SCOPE EXTENDED (2026-09-12): pilot now continues through book page 631**, not
just 1-436. Original 1-436 sweep is COMPLETE, no gaps (batches 1-17) — see
`diff1920ocr-trans.md`'s "Pilot batch 17" section for that summary (10 fixes + 1
archaism, the batch-16 "Pagina 411" marker-typo catch, 3 pending period/comma
ambiguities, and the page-337 manual-audit findings). Front matter also done
separately (see "Front-matter pilot"/"Índice review" sections).

**Why extended past 436:** finding the "Pagina 411" marker bug in the
already-completed 1-436 range showed this diff method catches things the tracked
Session A-E per-page pipeline (which covers 437-631) can still miss — it checks
the FINAL assembled `librodm.txt`, not the per-page draft, so it can catch
integration-stage slips. Batch 18 (437-500) confirmed this: found 2 NEW
`errors in 1920.txt`-worthy defects on book page 458 alone (a double
accent-drop at v.23, and FOUR "punto por coma" instances in v.27) that the
original tracked pipeline's Session A/B pass never caught.

**Critical protocol difference for 437-631** (vs. 1-436): pages in this range
have `pages/page_NNN.txt` working files with a "Corrections" section recording
decisions already made during Session A/B/E. **Before finalizing any comma/
period/stray-mark candidate in this range, check that page's Corrections section
first** — it may already document the exact decision (including "scan/print
artifact of this particular copy" calls: marks that look like genuine defects
under a quick zoom but were determined NOT to be real 1920 print errors on
closer inspection — confirmed examples on pages 472, 475). Only do fresh
image/1886 analysis when the note is silent on the spot in question. This
doesn't apply to 1-436 (no per-page files exist there).

**PILOT COMPLETE (2026-09-12): book pages 1-631, the entire Book of Mormon, done,
no gaps** (batches 1-23). Full final summary in `diff1920ocr-trans.md`'s "Pilot
batch 23" section. Headline results: 1-436 found 10 fixes + 1 archaism + 1
marker-format bug ("Pagina 411") + 3 still-pending period/comma ambiguities for
the editor, plus a separate manual page-337 spot-audit that found 2 more errors
invisible to this diff method by construction. 437-631 found 1 more silent fix +
3 new `errors in 1920.txt` entries (5 instances) + 1 integration-stage
regression caught and reversed (a verified misprint, "CAPTULO 12.", had drifted
back to its corrected spelling in `librodm.txt` — grep `librodm.txt` directly
whenever a diff candidate points at an already-logged "preserved misprint,"
don't assume the log entry guarantees the text still matches it). Page 631
itself produces a large but meaningless diff (the script sweeps the trailing
"Notas" appendix into it, since 631 is the last `Página N` marker in the file) —
not a real finding, documented in the batch-23 section.

**If the user asks to "continue" or "do the next batch" again: there is no next
batch.** Per the editor's standing plan (below), point them to the manual
page-by-page proofreading follow-up instead, or ask what they'd like to do.

**Editor's plan (set 2026-09-12):** after a manual full-image spot-audit of book
page 337 found 2 real errors this diff-based pilot structurally cannot see (both
transcriber and Google read the same clean misprint identically, so no diff signal
is ever produced), the editor confirmed this pilot is a cheap first pass, not a
substitute for eventual manual page-by-page proofreading. Plan: finish this
diff-based sweep through 1-436 as normal, then run a manual image-verification
pass over the same range afterward (same method as the page-337 audit) — see the
"Methodology spot-audit — book page 337" section of `diff1920ocr-trans.md` for the
full writeup and reasoning.

## Trigger

"Check pages NNN-NNN", "continue the OCR pilot", "run the next batch", or the user
naming a page range in the 1-436 span without further explanation (they mean this).

## Workflow per batch (25 pages is the established default size)

1. **Extract Google's OCR text** for the batch (only if not already present in
   `google_text_1920/` — check first):
   ```
   "/c/Users/rober/AppData/Local/Programs/Python/Python313/python.exe" extract_google_text.py <NNN> <NNN+1> ... <NNN+24>
   ```
   (Windows Python, not `wsl python3` — the latter lacks `pdfplumber`.)
2. **Run the diff**:
   ```
   "/c/Users/rober/AppData/Local/Programs/Python/Python313/python.exe" workspace/_pilot_ocr_diff.py <start> <end>
   ```
   This script (already written, reusable) extracts each page's body text directly
   from `librodm.txt` between consecutive `Página N` markers (since no
   `pages/pageNNN.txt` exists for this range), strips the same running-header lines
   `extract_google_text.py` strips from the PDF side, and reuses
   `check_google_crosscheck.py`'s exact character-stream diff logic (whitespace/
   hyphens/`[NNNN]` footnote markers stripped, so word-fusion/hyphenation can never
   be a false hit).
3. **Triage every candidate** against the established noise taxonomy below —
   dismiss on sight without opening an image. What's left, actually check the 1920
   image for (and 1886 where useful for shared-vs-exclusive classification).
4. **Before logging anything, check `errors in 1920.txt` for an existing entry** at
   that book/chapter/verse — skip if already covered.
5. **Classify and act:**
   - Our own transcription slip (doesn't match either edition) → fix `librodm.txt`
     silently, no log entry.
   - Genuine 1920-exclusive misprint (1886 differs) → fix `librodm.txt` to match the
     1920 print if it was wrong, or leave/note if it was already right, **and** add
     an entry to `errors in 1920.txt` in the standard format.
   - Period/comma ambiguity (see below) → leave transcription untouched, add to the
     flagged list, do not decide unilaterally.
6. **Update `workspace/diff1920ocr-trans.md`** with the batch's resource cost,
   findings, and a new running total — this file is the persistent record a future
   session (or this skill) relies on.
7. **Update the "Current progress" line above** in this file.

## Established false-positive taxonomy (dismiss without opening an image)

- **"Nefi" → Google reads the final "i" as "l" or drops it** — a consistent OCR/font
  weak spot, generalizes to other words too (confirmed on "infierno"). Not a real
  question.
- **Running-header or footnote-block text bleeding into the body stream** — Google's
  raw PDF extraction doesn't respect the structural separation this project's
  transcription maintains (body vs. Block 1 footnotes in a separate file). Shows up
  as citation-like fragments, page-number/chapter-header fragments, or garbled
  running-header text glued onto the first/last line of a page.
- **Google drops or garbles a single punctuation mark or accent** — commas, periods,
  colons, semicolons vanishing entirely, or an accent (í/i, é/e, á/a) dropped on
  Google's side. The reverse also happens sometimes (Google adds a spurious accent
  we don't have) — same underlying unreliability either direction.
- **Digit-for-accent or script-for-letter OCR garbles** — "ó" misread as "6", stray
  Cyrillic/Thai characters substituted for accented letters or footnote brackets.
- **Word-boundary drops at page/line boundaries** — Google's extraction sometimes
  drops the first syllable of a line ("contriste"→"triste") or fails to carry a
  hyphenated word's second half across a line break.
- **A whole page of scrambled word-salad from Google** — happens on dense,
  small-caps- or footnote-letter-heavy pages (confirmed on an Isaiah-quotation list
  page); ALWAYS spot-check the image once for the page rather than assume, but this
  has been 100% Google-failure, 0% real issue every time so far.
- **Multi-column layouts** (signature blocks, possibly other tabular content) —
  Google's row-based extraction interleaves columns into a scrambled reading order.
  Confirmed on the Eight Witnesses' signature block. Needs the image to confirm the
  real column order either way, not investigatable from the text diff alone.

## Editor policy: period-vs-comma print-defect ambiguity

**Do not resolve unilaterally.** When 1920 appears to show a period with lowercase
continuation but the transcription has a comma (matching or not matching 1886):
leave the transcription exactly as it reads, and add the instance to a flagged list
in `diff1920ocr-trans.md` for the editor's own inspection — don't silently correct it
either direction, and don't log it in `errors in 1920.txt` until the editor decides.
Two project precedents conflict here (the `orthography-check` skill's "keep the
literal period + log the 1886 difference" rule vs. `CLAUDE.md`'s 2026-09-03
reclassification of 9 similar cases as print defects fixed silently) — per the
editor (2026-09-12): "Often a period combines with a spec to look like a comma but
inspection may indicate otherwise. Similarly for comma that looks like period
because of print defect." This needs eyes on the actual page, not a zoomed crop or
Google's OCR reading alone.

## Verified findings so far (see `diff1920ocr-trans.md` for full detail)

10 silent fixes + 1 logged archaism (2 Nefi 8:12 "Quíen", added as the 10th instance
of the `FAMILIA acento agudo espurio` master entry) across book pages 1-150, plus 3
flagged period/comma ambiguities pending the editor's review. The overwhelming
majority of findings are concentrated on book pages 1-2 — pages 3-150 are otherwise
very clean after noise-filtering (batch 6, pages 126-150, added zero new findings;
its only notable candidate cluster, book page 138, turned out to be genuine 1920
print wear that the transcription already reads through correctly).

## A caution from experience

Don't assume the existing transcription is correct just because a candidate "looks
like" an established noise pattern — actually check when uncertain. Two real,
substantive errors (a missing "¿No" negation changing a rhetorical question's
meaning, and a genuinely dropped 2-word phrase) were found specifically because a
candidate was checked rather than pattern-matched away. Conversely, don't over-fix:
one instance (2 Nefi 3:24, "Dios hasta traer") was wrongly diagnosed as a print
defect needing a comma-fix before the editor's own inspection revealed the mark was
plain print debris unrelated to any real character, and the actual 1920 print has
no punctuation there at all.
