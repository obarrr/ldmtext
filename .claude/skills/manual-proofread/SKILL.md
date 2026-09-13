---
name: manual-proofread
description: Manual, high-resolution, chapter-by-chapter proofread of librodm.txt (body + both footnote blocks) directly against the 1920 PDF's own page images — a real word-for-word image read, not an automated text diff. One unit (front matter, or one chapter) per session by default. Starts with the title page and the Testimony of Three/Eight Witnesses, then proceeds 1 Nefi 1 through Moroni 10 in order. Use when the user asks to "proofread chapter X", "do the manual proofread pass", "continue the proofread", "start the proofread at the title page/testimonies", or names this pass by name.
---

# Manual proofread pass — image vs. librodm.txt, one unit at a time

## Why this exists

`ocr-diff-pilot` finished a full automated pass (book pages 1-631) that diffs
`librodm.txt` against the 1920 PDF's own embedded Google-OCR text layer. That
method has a structural blind spot: if the transcriber and Google's OCR both
read a clean misprint the same way, the diff produces zero signal even though
the underlying 1920 print is wrong. This was proven directly by the book-page-337
manual spot-audit (see `workspace/diff1920ocr-trans.md`), which found 2 real
errors invisible to the diff method, and confirmed independently when Google's
own raw OCR for that page was checked and read the identical wrong spelling.

This skill is the editor's planned follow-up: an actual human-style read of the
page image itself, word for word, against `librodm.txt` — the same method as
the page-337 audit, just organized chapter by chapter instead of as a one-off.
It is slower and more expensive per page than the diff pilot, which is exactly
why it runs one chapter at a time rather than in large batches.

## Trigger

"Proofread chapter X", "do the next chapter of the manual proofread", "continue
the proofread pass", "start the proofread pass" (defaults to the front matter
first if nothing has been done yet — check the Current Progress section of
`workspace/proofread-1920.md`).

## Scope and order

- **Unit of work: ONE unit per session by default.** A unit is either the
  front-matter group (title page + Testimony of Three Witnesses + Testimony of
  Eight Witnesses, done together as the first unit since they're one short
  contiguous block) or exactly one chapter thereafter.
- **Exception — explicit multi-chapter/range request.** If the user explicitly
  names a range ("proofread 1 Nefi 1 through 5", "do the next three chapters"),
  run them in order in one session without stopping to ask between chapters,
  same as the Session A-E range exception in `CLAUDE.md`
  ([[feedback_ae_range_no_stopping]]). Otherwise, one unit, then stop and report.
- **Order:** front matter, then 1 Nefi 1, 1 Nefi 2, … sequentially through
  Moroni 10, following `chapter_map.csv`'s row order for each book/chapter's
  starting 1920 file page. A chapter's page range runs from its own starting
  page (chapter_map.csv `page_1920` column) to the page before the next
  chapter's (or next book's) starting page.
- **Not in scope for this skill:** the índice (pages vii-xiv) and the rest of
  the front matter beyond the witnesses — these already got a dedicated review
  in the OCR-diff pilot's "Índice review" section. Don't re-do them here unless
  the user specifically asks.
- **Covers, for every page the unit spans:** body verse text, the `CAPÍTULO N.`
  heading, Block 1 footnotes (`librodm_foot.txt`) and Block 2 footnotes
  (`librodm.txt`).

## Workflow per unit

1. **Determine the page range.** Look up the chapter's starting file page in
   `chapter_map.csv`. For the front matter, the mapping is non-formulaic (see
   `workspace/diff1920ocr-trans.md`'s "Front-matter pilot" section): i=file 9,
   iii=file 11, iv=file 12, v=file 13.
2. **Check prior findings BEFORE re-deriving anything** — don't re-litigate a
   decision already made:
   - `workspace/diff1920ocr-trans.md` (OCR-diff pilot's findings and
     false-positive taxonomy for these exact pages — e.g. the multi-column
     signature-block false positive on page v).
   - `errors in 1920.txt` — grep for the book/chapter (and, for front matter,
     for keywords from the passage; some existing entries are filed under an
     inaccurate "Indice página v" label even though they're actually in the
     witness testimonies' body text, not the índice — grep by wording, not
     just by page-label prefix).
   - If any page in range is 437-631: that page's `pages/page_NNN.txt`
     "Corrections" section (decisions already made during Session A/B/E) — see
     [[feedback_errors_log_diligence]] and the critical-protocol-difference
     note in `ocr-diff-pilot`'s SKILL.md.
3. **Render the page images.** The pre-rasterized 400dpi PNGs already exist in
   `pages_1920/page_NNNN.png` (4-digit, zero-padded file page number) — read
   them directly, no need to re-invoke `process_page.py`'s PDF rasterization
   step when the PNG already exists.
4. **Read the image word-for-word against the transcription** — actually read
   it, the way a human proofreader would, not a mechanical diff. Compare body
   text against `librodm.txt`, footnote citation/letter text against
   `librodm_foot.txt` (Block 1) and the resolved cross-references in
   `librodm.txt` (Block 2).
5. **For anything that looks off, faint, ambiguous, or like a print defect**
   (tight spacing, a questionable letter, a mark that could be a comma or a
   period or debris): escalate resolution for that specific spot only —
   don't guess from the base 400dpi crop.
   - Suspected merged/narrow space: crop and zoom that spot at higher
     resolution (see `measure_word_gap.py` for the 1200dpi re-rasterization
     approach) and compare the gap to the word's own intra-letter kerning, not
     to other word-gaps on the line. See [[feedback_narrow_space_vs_merge]] —
     standard 400dpi crops have been shown to understate real gaps by roughly
     an order of magnitude.
   - Suspected stray mark or ambiguous letter/punctuation: crop tightly and
     resize 2-6x with PIL (`Image.crop(...).resize(..., Image.LANCZOS)`) rather
     than relying on the full-page overview — a period/comma distinction in
     particular is often only resolvable at this level. See
     [[feedback_stray_mark_google_ocr_order]] (check Google's OCR text first
     when available, then confirm with a stroke-weight zoom) and the
     period-vs-comma policy below.
   - Cross-check 1886 at the same book page (`chapter_map.csv`'s `page_1886`
     column) to classify shared-vs-1920-exclusive, when 1886 covers the same
     content — note that the front matter's witness testimonies are a
     *different, revised translation* in 1920 (per the title page's own
     "diligentemente comparado con anteriores ediciones y revisado"), so 1886
     wording won't line up sentence-for-sentence there; use it for
     spelling/word-choice comparison only where the underlying phrase is
     actually shared.
6. **If it looks like a genuine Spanish-language error** (misspelling, wrong
   word, grammar/agreement break, nonsensical citation), investigate before
   concluding anything — don't log on a hunch:
   - 1886 at the same location, first (as every existing `errors in 1920.txt`
     entry does).
   - RAE/DLE — both the modern dictionary and the historical dictionaries
     (Terreros 1786, Autoridades, older DRAE editions) — a form attested even a
     century before this edition can still be legitimate period archaism, not
     an error. See [[feedback_biblical_register_lag]].
   - Quijote and Reina-Valera corpora for period attestation, the same sources
     already cited throughout `errors in 1920.txt`.
   - The modern (current) Spanish Libro de Mormón at churchofjesuschrist.org
     for the same verse/passage (WebFetch) — useful for confirming whether a
     construction is a real grammatical break or an intentional period usage.
   - Internal consistency — grep `librodm.txt` for the same word/form
     elsewhere. Overwhelming internal consistency = house style, not a fixable
     error; a single, isolated, self-contradicting instance (especially one
     that breaks basic number/gender agreement the document doesn't break
     anywhere else) is a real error candidate. See
     [[feedback_errors_log_diligence]].
7. **Classify and act:**
   - **Confirmed 1920 textual error** (wrong/missing/misspelled word, a
     genuine grammar break, misset citation punctuation) → add an entry to
     `errors in 1920.txt` in the file's existing format (location, what's
     printed, what's correct, 1886 comparison, sources checked, resolution) —
     preserve the misprint as printed in `librodm.txt`/`librodm_foot.txt`,
     per this project's standing convention.
   - **Print defect** (speck, weak/broken type, not a real character) → fix
     silently in the text, no `errors in 1920.txt` entry. See
     [[feedback_errors_log_textual_not_print]].
   - **Footnote reference-separator punctuation** (comma for ;/:, spaced
     colons, doubled marks) → normalize silently in both blocks, no log entry
     — but a misspelled word within a footnote is still logged. See
     [[feedback_footnote_separator_punct_silent]].
   - **Period/comma print-defect ambiguity** → do not resolve unilaterally.
     Leave the transcription untouched and add it to a flagged list in
     `workspace/proofread-1920.md` for the editor's own inspection — same
     policy as `ocr-diff-pilot`'s SKILL.md.
   - **Already documented** (present in the diff pilot's findings, already in
     `errors in 1920.txt` under any label, or already resolved in a page's own
     Corrections section) → skip re-deciding; record "already covered, see X"
     in the proofread log. If the existing entry's location label looks wrong
     (e.g. filed as "Indice" when it's actually body/testimony text), note the
     apparent mislabel in the proofread log for the editor rather than editing
     the existing entry unilaterally.
   - **Image genuinely doesn't match the transcription AND none of the above
     resolves it** → do not decide. Record it as an open/flagged note in
     `workspace/proofread-1920.md`: book/chapter:verse, PDF page number(s),
     what's seen in the image, what's in the transcription, and what was
     checked.
8. **Append the unit's results to `workspace/proofread-1920.md`** (create it on
   first use — a template is described below). One dated section per unit,
   covering every page in range, its PDF page number(s), any silent fixes,
   any new `errors in 1920.txt` entries, any flagged/open notes, and anything
   confirmed to already be documented. **Give a unit a one-line "checked,
   clean" entry even with zero findings** — the running log's value is
   complete coverage, not just a list of problems.
9. **Update the "Current Progress" line at the top of
   `workspace/proofread-1920.md`** so the next session picks up at the right
   chapter, and update `CLAUDE.md`'s pointer to it if this was the very first
   unit (front matter) or otherwise notable.

## Output log format (`workspace/proofread-1920.md`)

```
# Manual proofread pass — image vs. librodm.txt

## Current Progress
Last completed: <unit name>. Next: <unit name>.

---

# <Unit name> (<date>)

Pages: file <NNNN>-<NNNN> (book <label(s)>)

- <Book Chapter:Verse or section name>, PDF page <NNNN> — <finding, or
  "checked, matches image", or "already logged, see errors in 1920.txt">
- ...

Errors logged this unit: <list, or "none">
Flagged/open (needs editor's eyes): <list, or "none">
```

## Relationship to other skills/passes

- Distinct from `ocr-diff-pilot` (automated OCR-text diff, complete for all 631
  pages) — this is the manual image-read follow-up that pilot's own findings
  said was still needed; it catches the class of error the diff structurally
  cannot see (a clean misprint both sides read identically).
- Distinct from Sessions A/B (`transcribe-page`/`verify-footnotes`), which
  happened once per page during initial transcription — this is a second,
  independent read, done later and by a different method.
- Findings are logged exactly the way Session E and the OCR-diff pilot do:
  `errors in 1920.txt` format for textual errors, `permitted words.txt` only
  for a spellchecker false-positive, never for print defects.

## Current progress

Front matter through 1 Nefi 11 complete — see `workspace/proofread-1920.md`.
Next: 1 Nefi 12.
