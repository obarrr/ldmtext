# Libro de Mormón 1920 — Transcription Rules
## For Project Gutenberg Preparation

---

## 1. Page Structure

1. Each page begins with `Página N` on its own line. If the page begins
   mid-verse (continuation from the prior page), the first line of text
   follows immediately with no blank line. If the page begins with a
   chapter heading, a blank line separates `Página N` from the heading.
2. The running page header (e.g. "CAP. III.) LIBRO DE HELAMÁN") is
   discarded entirely.
3. Chapter headings appear as `CAPÍTULO N.` on its own line, with a
   blank line before and after.
4. Verses flow as continuous paragraphs.

**Verse numbers always start at column 1 — never indented (confirmed
failure mode, pages 453/454/489-493/508, fixed 2026-07-25).** When a
new verse's number begins a line, write it flush left with zero
leading whitespace, exactly like every other body line. This project's
plain-text transcription format never indents anything in the body
text — not chapter openings, not verse starts — regardless of how an
English reader's eye might expect a paragraph's first line to be set
off. This defect first appeared on page 493 and was noted informally
in a CLAUDE.md progress-log entry (2026-07-22g) at the time, but that
note only changed how later pages were transcribed going forward — it
was never converted into an actual rule here, and page 493 itself
(plus its already-integrated copy in `librodm.txt`) was left
unfixed. With nothing mechanical in place to prevent a recurrence, the
identical defect reappeared independently on page 508. Fixed 2026-07-25
across pages 453, 454, 489-493, and 508 (66 body-text instances total),
`librodm.txt` (77 lines), and the two already-emailed chapter files
affected (`chapters_emailed/Helaman_6.txt`, `Helaman_7.txt` — chapters
Helamán 6-7 had already been sent to family before this was caught;
the emails were not resent, but the archive copy was corrected for
consistency, matching the 2026-07-24b precedent for this class of
retroactive text fix). `check_verse_indent.py`, added the same day, is
the mechanical backstop — wired into `transcribe-page` step 9 and
`orthography-check`'s document-wide sweep, alongside
`check_spaced_punctuation.py`/`check_footnote_punctuation.py`. Note
its one known false-positive shape: a Corrections-log paragraph can
happen to word-wrap so that a quoted verse excerpt starts a line with
a few spaces of ordinary prose indentation (not a real defect) — check
context, as with the other two checker scripts, before "fixing"
a hit inside a Corrections section.

**Chapter/book subtitles — always transcribe, never omit (corrected
2026-07-22).** Many chapter and book openings print an additional
descriptive line — sometimes bold small-caps (e.g. Helamán 7's
"PROFECÍA DE NEFI, HIJO DE HELAMÁN.", page 453), sometimes italic
mixed-case (e.g. Helamán 13's "Profecía de Samuel, el Lamanita, á los
Nefitas.", page 469) — immediately before or after the
`CAPÍTULO N.`/book-name heading, occasionally followed by a longer
descriptive paragraph as well (Helamán 7 has a 4-line argument after
its subtitle). These subtitles are NOT limited to whole-book title
pages: the same convention covers an entire book, a single book, a
span of several chapters, one chapter, or even just part of a chapter.
**Always transcribe every one of these exactly as printed**, on its
own line with blank-line separators (the same "blank line, text, blank
line" convention used for book-name headers), regardless of what level
it applies to. Never assume a chapter has no subtitle just because
neighboring chapters don't — some chapters have one and some don't,
with no reliable pattern (Helamán 8-12 have none; 7 and 13 do) — always
check the actual image at each new chapter opening.

1920's placement of a subtitle relative to the chapter number can
differ from 1879/1886: 1920 sometimes prints `CAPÍTULO N.` BEFORE the
subtitle (confirmed at Helamán 7 and 13), while 1879/1886 consistently
print the subtitle first, before the chapter number, in those same
spots. This is a genuine, repeatable 1920 house-style difference, not
a transcription error — transcribe in whatever order 1920 actually
prints, never reorder to match 1879/1886. Do not modernize or supply
missing accents in a subtitle; transcribe exactly as printed (rule 32)
like any other text, but do check the corresponding 1879/1886 wording
and note any substantive discrepancy (missing accents, reordering,
wording differences) in `errors in 1920.txt`, even though the
page-level ordering difference itself is not logged as an error.

**Confirmed failure mode (2026-07-17 through 2026-07-22, Helamán 13,
page 469):** Helamán 13's own subtitle was omitted from the body text
entirely, justified in the page's Corrections log as analogous to rule
19's precedent of skipping a subtitle line when picking a `LIBRO DE
X`-style header for `librodm_foot.txt`. That analogy was wrong: rule
19 (Section 4) is narrowly about which single line becomes the short
header text in a completely different file (the Block 1 footnote
listing) — it has never governed what belongs in the body text itself,
and every subtitle-like line encountered while transcribing the body
belongs there per this rule, independent of whatever gets picked out
later as a Block 1 header. The omission also rested on a false premise
("no chapter-heading subtitle has been transcribed on any completed
page so far") that was already contradicted by Helamán 7's subtitle,
transcribed correctly back on page 453. Restored 2026-07-22 in both
`pages/page_469.txt` and `librodm.txt`.

---

## 2. Body Text — Line Wrapping

5. Read every line ending directly from the image crop. NEVER approximate
   or guess line breaks from the OCR text or character-count estimation.
   Every line ending must be image-confirmed.
6. Reproduce the image line endings exactly, subject to rules 7 and 8.
   Transcribe strictly line-by-line: for each line as it appears in the
   image, write it as one output line before moving to the next. Do NOT
   compose the page as flowing prose/paragraphs and then wrap or reflow
   it to a target width — that produces line breaks with no relationship
   to the source and violates rules 5/6 even if every resulting line
   happens to satisfy the rule 9 length cap. Before transcribing, note
   how many print lines are visible in each crop (top/mid/bot); the raw
   line-by-line transcript (before any rule 7/8 adjustment) must have
   that same count.
   **Confirmed failure mode (2026-07-19, page 475):** the entire body
   text was generated as continuous prose and then broken into lines at
   roughly even ~72-character intervals, with zero correspondence to the
   image's actual line endings — every single line boundary was wrong,
   even though every line satisfied rule 9. This is a distinct and more
   serious failure than the rule 7 lapse documented below: there, most
   lines were still image-derived and only two hyphen rejoins were
   missed; here, no line was image-derived at all. The root cause is
   that rule 9 (character count) is self-checkable while generating
   flowing text, while rules 5/6 require actively cross-referencing the
   image line-by-line — a much higher-friction habit that silently
   drops out unless the transcription is done as a literal line-by-line
   copy from the start. Spot-checks of two other completed pages (470,
   474) against their images found no such problem, so this does not
   appear to be a chronic, document-wide pattern — but it means a clean
   `check_lines.py` report (which only checks length and trailing
   hyphens) is NOT sufficient evidence that a page's line breaks are
   image-derived. `check_line_wrap.py <book_page> <page_txt_path>` was
   added as a partial backstop — it OCRs the page image independently
   and flags a body-line-count mismatch or suspiciously uniform line
   lengths — but it is advisory only (OCR line-splitting is itself
   imperfect) and does not replace the per-line image read.
   Regardless of how literally line endings are copied, inter-word
   spacing within a line is always normalized to exactly one space in
   the output. Never preserve a wider gap from the source — even a
   gap only slightly wider than the surrounding spacing on the same
   line — and this applies uniformly to every such instance on a page,
   not only the ones that happen to get individually noticed. This is
   unconditional: it does not require citing precedent from another
   page's Corrections log, though a page-level Corrections note is
   still fine for the reader's benefit. It does not need an `errors in
   1920.txt` entry — justification-driven gap width is not a misprint.
   **Confirmed failure mode (2026-07-19, page 465):** a fresh
   transcription correctly normalized one justification-widened gap
   (v.20, "mar del  Oeste") by citing precedent from page 464's
   Corrections log, but left three other instances of the identical
   phenomenon un-normalized elsewhere on the same page (v.11
   "humildad?  ¿No", v.16 "sirven?  Si", v.17 "abundancia.  Y", v.21
   "sexto.  Y" — all confirmed via zoom to be genuinely wider gaps in
   the print, not a transcription slip). Root cause: this
   normalization had only ever existed as ad hoc precedent cited in
   individual pages' Corrections logs, never as a standing rule, so
   applying it depended on the transcriber separately noticing and
   citing precedent each time rather than following one blanket
   instruction. This paragraph closes that gap.
   **Narrow-but-real space vs. true zero-space merge (2026-07-20, page
   479):** when two words appear to run together with little or no
   gap, don't assume it's a genuine merged-word print defect (like page
   474's "esesto," preserved as printed per rule 32) without checking
   the gap at high zoom. Page 479 v.7 was transcribed and carried
   through Session B as "quese" (treated as a true merge), but on
   closer inspection the print has a real, if reduced-width, space
   between "que" and "se" — not a zero-width merge. A reduced-but-
   present gap is normalized to one space per this rule (like any other
   inter-word spacing), not preserved as a merge and not logged in
   `errors in 1920.txt`. Only treat a tight word-pair as a genuine
   merge — with no space inserted, per rule 32 — when zoomed inspection
   confirms there is truly no gap between the letters at all.
   **Default to two words when 1886/grammar says two words (editor
   guidance, 2026-07-22):** don't lean on zoom/pixel-measurement analysis
   to decide this call at all, and don't default to writing it as one
   merged word. If 1886 prints the corresponding text as two separate
   words (or the phrase is simply not a word any other way — grammar
   requires two words there), transcribe it as two words with a normal
   single space, exactly as if it were any other inter-word gap — this
   is the default even if the 1920 image looks, at a glance or even
   under zoom, like it could be a single run-together word. Note the
   spot in the page's Corrections log at transcription time
   (book/chapter/verse, the two words involved) as usual, but do NOT
   raise it to the editor as a standalone question during Sessions
   A-D — those sessions should run through without stopping for this.
   Instead, surface every such note collected across the page as part
   of Session E's summary to the editor (grouped with that session's
   other findings), so the editor can double-check against the actual
   page whenever convenient, without it holding up integration/Block 2
   generation. Write "que fueron," not "quefueron," immediately in
   Session A either way — the editor's later review is a check on an
   already-committed default, not a gate before proceeding.
   Reserve the true zero-space "merge, preserved as printed" treatment
   (rule 32) for the rare case where 1886 ALSO merges the same two words
   (matching page 474's "esesto" precedent) or no two-word reading makes
   sense at all — not for "the pixels looked like zero gap to me." See
   `feedback_narrow_space_vs_merge`: even a carefully-isolated pixel
   column-projection measurement (page 490 v.12, "que fueron") was
   overridden by the editor's direct look at the page, so pixel analysis
   has proven to be the wrong tool for settling this call by itself —
   1886/grammar plus an editor flag is more reliable and much less work.
7. Hyphenated word at end of line: remove the hyphen and rejoin the word.
   Any punctuation immediately attached to the second half (e.g. a comma
   or period directly after the word fragment) travels with the rejoined
   word as a unit. If the rejoined word (plus any attached punctuation)
   appended to the first line is under 73 characters, keep it at the end
   of the first line. If 73 or more characters, move it to the start of
   the next line. Never preserve the hyphen split.
   **Confirmed failure mode (2026-07-14, Helamán 7, page 455):** this
   rule is easy to apply reliably when something else is already forcing
   a stop on that exact line (e.g. a footnote marker being inserted
   nearby, which requires a character-count anyway) — a marker-adjacent
   hyphen got rejoined correctly for exactly that reason. Two other
   hyphens on the same page, with no adjacent marker to force a stop,
   were transcribed straight through with the hyphen still in place: the
   page also required an unusually large amount of other per-line
   investigation that session (an 1879 swash-font cross-check across
   four footnote letters, plus two separate suspected-misprint zooms),
   and by the time the body text was actually written out, those two
   lines were being reconstructed from earlier notes rather than
   re-derived fresh from the image. The rejoin/rebalance step is
   mechanical and judgment-free — it should be done as one complete pass
   over every raw line, immediately after reading the image crops and
   *before* any typo or footnote-letter investigation begins, rather
   than left to be noticed opportunistically while attention is on
   something else (see the `transcribe-page` skill's step 5, added for
   this reason). `check_lines.py` now also flags any line still ending
   in a bare `-` as a mechanical backstop, but that catches the mistake
   after the fact — sequencing the mechanical pass first is what
   prevents it.
8. If a line as read from the image exceeds 72 characters in the output
   (e.g. due to added footnote markers), remove the last word and place
   it at the start of the next line. Repeat until the line is under 73
   characters. The removed words are prepended to the next image line.
9. Lines must be strictly less than 73 characters (i.e. 72 or fewer).
   (Chosen to match Distributed Proofreaders' own PPV line-length target
   of 72 — see Section 8 for the research behind this.)
10. A word split by a page boundary (the last word on page N is
    hyphenated and completes on page N+1) follows the same rejoin logic
    as rule 7, but the two halves live in two different output files
    (`page_N.txt` and `page_(N+1).txt`). Rejoin the word as a whole, then
    decide which file it belongs to: if appending the completed word
    (plus any attached punctuation) to the end of page N's last line
    keeps that line under 73 characters, place the whole word there and
    begin page (N+1)'s body text with the following word instead — do
    not carry over any fragment. If the line would reach 73 characters
    or more, place the whole word at the start of page (N+1)'s first
    line instead, and leave it off the end of page N entirely. Since
    page N is normally already written by the time page N+1 is
    transcribed, this may require revising the previously-written
    page_N.txt.

---

## 3. Footnote Markers in Body Text

11. Superscript letters in the original (a, b, c … z, 2a, 2b …) become
    `[N]` bracketed sequential numbers placed immediately before the word
    the superscript annotates — same position as in the original.
12. Footnote numbers run sequentially across the entire document and
    never restart.
13. Each chapter's footnotes restart at letter `a` in the original. If a
    new chapter begins mid-page, the letter sequence restarts at `a` for
    that chapter, but the global sequential number continues from where
    it left off.
14. NEVER trust the PDF OCR layer for superscript letters — it routinely
    misreads them. ALWAYS read superscript letters directly from the
    image (fn_zoom crop) before assigning footnote numbers.
15. Similarly, read inline superscripts from the body text image, not
    from the OCR text layer, to confirm which letter annotates which word.

---

## 4. Footnote Output — Block 1 Only

Output Block 1 only after the body text. Block 2 (sequential-number block)
is generated in a later review pass, not during initial transcription.

### Block 1 — Chapter+Letter Block

16. One entry per footnote, prefixed with chapter number and original
    letter, followed by the sequential number.
    Format: `[chapter][letter], [number]: Reference.`
    Note: ONE space after the colon — this matches the existing
    convention in `librodm_foot.txt` (confirmed consistent across all
    entries in that file). Do not use two spaces.
    When footnote letters extend past z into two-letter codes (2a, 2b,
    etc.), join the chapter number and letter code with a hyphen:
    `[chapter]-[2-letter code], [number]: Reference.`
    Example: `3-2a, 3185: Véase u, Alma 16.`
17. Cross-references use the original printed letters exactly.
18. Lines must be strictly less than 80 characters (79 or fewer).
    If a reference wraps, the continuation is flush left (no indent).
    Block 1 (librodm_foot.txt) is NOT scanned by pptext and gets
    reformatted into Block 2 anyway (different length entirely once
    cross-references resolve to bare numbers), so it keeps the looser
    79-char width rather than the 72-char target used for librodm.txt
    (rule 9) — precise Block 1 wrapping is not worth the effort. When a
    Block 1 line does need to wrap, prefer breaking at a semicolon
    between whole references over breaking a single reference apart
    (see rule 9's note on Block 2 wrapping — the same preference
    applies here if it's convenient, but is not enforced).
19. If a new book of the Book of Mormon begins within the block, insert
    the book name on its own line with a blank line above and below it.
    **Scope note:** this rule and its "ignore subtitle lines" guidance
    below apply ONLY to picking the single header line used here in
    Block 1 (`librodm_foot.txt`) — they say nothing about the body
    text in `librodm.txt`. Every subtitle/argument line encountered
    while transcribing the body belongs there regardless of what gets
    picked as this header (see Section 1's chapter/book subtitle rule);
    do not use this rule as precedent for omitting anything from the
    body text. (This distinction was missed once — see the Helamán 13
    failure mode documented in Section 1 — so it is spelled out here
    too.)
20. Chapter boundaries within the same book do NOT get a blank line in
    Block 1.

### Footnote Reference Formatting

21. Semicolons between multiple references; period at end of entry.
22. No spaces around colons in references (e.g. `18:22` not `18 : 22`).
23. When a footnote cites two or more consecutive verse numbers, format
    them as a hyphenated range, regardless of how the original prints
    them: `24,25` → `24-25` (e.g. `Alma 13:24-25`).
24. When a footnote cites non-consecutive verse numbers, use a comma with
    no space: `2,4` (e.g. `Helamán 4:2,4`), not `2, 4`.
25. Mixed: e.g. `4,17-18` means verse 4 (non-consecutive) and verses
    17-18 (consecutive range).
26. The 1879 English and 1920 Spanish editions can differ in footnote
    order, or in which word a footnote letter lands on, purely because
    the translations put words in a different order — this is a
    translation artifact, not a transcription error. When cross-checking
    the two editions (including for ambiguity resolution, see Section 8),
    match footnote entries by their target reference content (the
    book/chapter/verse being cited), never by letter or list position.

### Examples

Single chapter, no boundary:
```
3a, 3159: Norte América.
3b, 3160: Versículos 5, 9.
```

New book beginning mid-block:
```
63p, 3137: Estas numerosas copias de sagrados libros fueron
indudablemente copiadas directamente de ó comparadas con los
anales sobre las originales planchas de bronce.
63q, 3138: Alma 37:27-32.

LIBRO DE HELAMÁN

1a, 3143: Alma 50:40.
1b, 3144: Véase c, Mosíah 29.
```

Chapter boundary mid-page, same book (chapter 2 closes, chapter 3 opens) —
no blank line; the letter reset (e.g. 2a -> 3a) is the only visual signal.
A blank line plus book-name header (rule 19) is used only when the book
itself changes, e.g. Alma -> Helamán:
```
2a, 3158: Véase f, I Nefi 1.
3a, 3159: Véase 3166, Omni 1.
3b, 3160: Norte América.
```

The book-name header text itself is taken from the page's own body text —
the first all-caps title line encountered before any verse content (skip
a `Página N` line if present; ignore subtitle lines like "HIJO DE ALMA."
that may follow the main title), with any trailing period or comma
stripped. This matches the headers already present in `librodm_foot.txt`
(e.g. body text "LIBRO DE JACOB." → header `LIBRO DE JACOB`).

---

## 5. Corrections Log

27. After the two footnote blocks, include a `Corrections` section
    listing every OCR error or typo corrected, in the format:
    `[verse or footnote ref] "original" → "corrected" — reason`

---

## 6. OCR Corrections

28. Rejoin hyphenated word splits from line breaks
    (e.g. "sepa-rados" → "separados"). See rule 7 for placement.
29. Fix name OCR errors: "Nef" / "Nefl" → "Nefi".
30. Fix word OCR errors as identified by visual inspection of the image
    (e.g. "fileles"→"fieles", "hahogó"→"ahogó", "coro"→"oro",
    "Covenios"→"Convenios").
31. Remove spaces before punctuation — this applies to original print spaces
    as well as OCR-added ones, with NO exception for a run of pages where the
    1920 print itself consistently sets a space before a mark. No space
    between the last letter of a word and the following comma, semicolon,
    colon, exclamation mark, or question mark.
    (e.g. "dijo :" → "dijo:", "sí ," → "sí,", "jamás ;" → "jamás;",
    "cielo !" → "cielo!").
    **(2026-07-24, user correction, pages 496-502):** a run of Session E
    notes wrongly declared "space before ; and !" an "established
    recent-pages convention" to be preserved as printed, on the theory
    that it was intentional 1920 house style. This was never actually
    supported by this rule — rule 31 already named "semicolon" explicitly
    — and directly contradicted it. Fixed on page 502 (and `librodm.txt`);
    pages 471-495, which contain earlier sporadic instances of the same
    pattern, have not been swept yet as of this correction. If a future
    page shows the same pattern, remove the space; do not re-invent this
    "established convention" exception again.
32. Preserve 1920 Spanish spelling conventions exactly: á, vió, fué, etc.
    Do NOT modernize. This includes suspected misprints: **never silently
    substitute what a word or phrase "should" say for what is actually
    printed, even when you are confident it is a misprint** (confirmed
    failure mode 2026-07-13, Helamán 4:5). A Session A transcription of
    page 442 read the 1920 image as printing "en al año" (grammatically
    wrong; "al" for "el"), correctly noted the anomaly in a Corrections-log
    comment ("likely misprint... verify against 1879 or zoomed crop"), but
    then typed the *expected* reading "en el año" into the actual
    transcribed text anyway — silently fixing what the note itself flagged
    as unverified. This went undetected through Sessions B and C (both of
    which read the Corrections note and, seeing no error was actually
    being reported in the text, moved on) until a later full audit
    compared the page image directly against `page_442.txt` and found the
    mismatch, then confirmed via 1886 ("el año" there) that 1920 really
    does misprint "al". When a suspected misprint is noticed at
    transcription time, ALWAYS type exactly what the image shows (never
    the "corrected" reading) and log it in Corrections as "preserved as
    printed; verify against 1886" — resolving whether it is a genuine
    error is Session E's job (see the "Mandatory check for any suspected
    error" section of the `orthography-check` skill), not something to
    pre-empt by quietly typing the expected word during Session A.
33. Remove "Digitized by Google" watermark text entirely.
34. Roman numeral "I" mis-read as digit "1" in book/chapter references
    should be corrected by context.
35. Quotation marks: always type plain straight ASCII quotes — `"` (not
    `“`/`”`) and `'` (not `‘`/`’`) — everywhere, including inside
    footnote text (Block 1/Block 2), never curly/smart quotes. This
    matches Distributed Proofreaders' own proofreading-stage convention
    (confirmed via DPWiki's Proofreading Guidelines Explanation:
    "Proofread 'double quotes' as plain ASCII \" double quotes"). Curly
    quotes are a deliberate LATER step — DP's Post-Processing FAQ
    prefers curly quotes in the final .txt AND .html output, even when
    the original printed straight quotes — but that conversion is meant
    to happen as one dedicated pass at the very end of the whole
    project (tools like Guiguts' "Convert to Curly Quotes" exist for
    exactly this), not typed by hand page-by-page. If a text editor
    auto-corrects a straight quote to curly while transcribing, fix it
    back to straight before saving — see the `errors in 1920.txt`/
    `orthography-check` skill note on the one stray instance
    (footnote 425, "la palabra 'no'") found and corrected 2026-07-11
    after being in the document undetected for some time, since
    pptext's curly quote check only flags MISUSE of curly quotes
    already present, not their mere existence.
36. An unusual accent mark — one that doesn't fit this document's
    established usage (which uses only acute á/é/í/ó/ú; anything else,
    e.g. a grave accent, is already suspect on its face) or that looks
    like it might just be print/scan damage rather than real type —
    must be checked against the Google OCR text
    (`extract_google_text.py`/`check_google_crosscheck.py`, or a direct
    look at `google_text_1920/page_NNNN.txt`) before being logged as a
    genuine 1920 error, in addition to (not instead of) the usual 1886/
    1879 comparison. **If Google's OCR doesn't transcribe the mark
    either, treat it as a stray speck and transcribe the plain letter
    with no accent — do not log it in `errors in 1920.txt`.** Google's
    OCR is trained on real type; it reliably drops accents that aren't
    actually printed, so its silence on a mark you're unsure about is
    real evidence, not noise to explain away.
    **(2026-07-26, user correction, twice in one day):** two separate
    "genuine grave accent" findings — III Nefi 14:2 "còn"/"què" (page
    515, logged 2026-07-25) and III Nefi 18:28 "cuandò" (page 525) —
    were both wrong. Both were confirmed by the user's own direct look
    at the page to be stray specks, not real accents; both cases'
    Google OCR text had *already* read the plain unaccented word all
    along (`google_text_1920/page_0537.txt` for "con"/"que",
    `page_0547.txt` for "cuando"), but that signal was dismissed each
    time as "expected OCR behavior for a rare diacritic" instead of
    being treated as the answer. Worse, the second case was reasoned
    into existence partly *by citing the first, already-wrong, case as
    precedent* — a good demonstration of how an unverified "established
    anomaly" can compound. Going forward: an unusual accent claim needs
    the Google OCR check before it can be logged, and a match to an
    earlier such claim is not itself evidence — each instance still
    needs its own check.

---

## 7. Session Workflow

Scripts and PDFs all live in the project folder. All three source PDFs
are pre-rasterized once (via `split_pdfs.py`) into `pages_1920\`,
`pages_1879\`, `pages_1886\` as 400dpi PNGs — normal per-page work reads
those PNGs and never touches Poppler. Poppler (`pdftoppm`) is only needed
for the one-time `split_pdfs.py` run, or if a specific page ever needs
re-rasterizing above the standard 400dpi (the source scans' native
resolution is ~600dpi — see `environment_setup.md` for the install path
if that's ever needed). Use the `py` launcher, not `python`, for every
script invocation below (confirmed working on this project's Windows
setup; a bare `python` can resolve to a non-functional Microsoft Store
stub on some machines).

1. Run from the project folder, passing the pre-rasterized PNG from
   `pages_1920\` (never the source PDF — see note below):
   `py process_page.py pages_1920\page_0NNNN.png <page_label> <first_fn_number>`
   where `NNNN` is the FILE page (book_page + 22, per Key Constants in
   CLAUDE.md), zero-padded to 4 digits. Image crops are saved to the
   Windows temp folder (%TEMP%).
2. Read fn_zoom image to identify all footnote superscript letters.
3. Read top/mid/bot images to confirm body text line endings.
   Use crop_page.py only when a specific region needs closer inspection.
4. Write output file: body text, then Block 1, then Corrections.
   Save as page_NNN.txt in the project folder.
5. Run: `py check_lines.py page_NNN.txt` — fix any lines ≥ 80.
6. Proceed to the Review Pass (Section 9) before integrating into
   master files.

**The starting footnote number for each session is provided by the
editor. Example: page 437 starts at footnote 3151.**

Scripts:
- **process_page.py** — takes a pre-rasterized PNG (from `pages_1920\`,
  `pages_1879\`, or `pages_1886\`) and saves crops: top (0-40%), mid
  (30-70%), bot (65-90%), fn (87-100%), fn_zoom (footnote area at 3×
  zoom). Can also accept a raw PDF path and rasterize it at 400dpi via
  pdftoppm (requires Poppler), but that path is redundant for any page
  already covered by the pre-rasterized folders — use the PNG instead.
- **check_lines.py** — flags any lines ≥ 73 characters (default; pass a
  second argument to override).
- **crop_page.py** — zooms into a specific vertical band of the page.
- **insert_body_text.py** — inserts one or more verified pages' body text
  into librodm.txt immediately before `Notas`, and appends their Block 1
  entries to librodm_foot.txt, including book-boundary headers where
  needed (Review Pass Step 2). Pass `--footnotes-only` to skip the
  body-text insertion, or `--body-only` to skip the Block 1 append.
- **generate_block2.py** — resolves Block 1 cross-references to bare
  sequential numbers (book-aware, handles multi-letter forms like
  "p y q") and appends Block 2 entries to librodm.txt (Review Pass
  Step 3). `--fix-unresolved` rescans the whole document for
  previously-unresolvable cross-references now resolvable — run once
  the entire text is transcribed.

---

## 8. Master Files and Broader Project Workflow

All master files live one level up from the `extracted pages` workspace,
in `libro_de_mormon_1920\`. The `extracted pages\` folder is a workspace
only; the four master files are the product output.

### Master Files

- **librodm.txt** — The complete working document. Structure:
  1. Body text of the Book of Mormon (all processed pages so far).
  2. A `Notas` divider line, followed by book-name headers and the
     running Block 2 (sequential-number) footnotes.
  When integrating a new page, body text is **inserted** immediately
  before the `Notas` line. Block 2 footnotes are **appended** to the
  end of the file. To avoid scanning the growing body-text section,
  locate `Notas` by scanning backwards from the end of the file.
- **librodm_foot.txt** — Running Block 1 (chapter+letter) footnotes,
  **appended** after each page. These are the source used to generate
  the `Notas` section of librodm.txt.
- **permitted words.txt** — pptext good-words list. One word per line.
  Contains proper names, archaic forms, and intentional 1920 spellings
  not found in a standard Spanish dictionary.
- **errors in 1920.txt** — Documented 1920 original errors (not
  corrected in the transcription). Each entry cites location, the 1920
  reading, the correct form, and supporting evidence.
  Format: `Book Chapter:Verse error (correction) (evidence note)`.
  The evidence note is usually 1886 (same-lineage, digitized, primary
  source of comparison — see Reference PDFs below), but may cite 1946
  or RAE instead/in addition when those are what settled the call — see
  Additional Reference Resources under Section 8.

### Reference PDFs and Pre-Processing

Three PDFs are used:

- **Libro_de_Mormon 1920.pdf** — Primary source.
- **BOM 1879 Pratt.pdf** — 1879 English, same Orson Pratt footnotes.
  Used to resolve ambiguous superscript characters (i/l/1) and
  cross-reference letters.
- **Libro_de_Mormon 1886.pdf** — 1886 Spanish, better typesetting,
  no footnotes. Used to verify whether a 1920 oddity is a genuine
  error or a legitimate archaic form.

**Pre-processing (one-time setup):** All three PDFs are split into
individual page images at 400dpi and stored in subfolders:

- `pages_1920\`
- `pages_1879\`
- `pages_1886\`

This is done once with a split script (`split_pdfs.py`, to be written)
and avoids re-rasterizing on every session.

### Chapter/Page Lookup Table

A lookup table (`chapter_map.csv`, to be built) records for each book
and chapter of the Book of Mormon the corresponding page number in each
of the three editions:

  Book, Chapter, page_1920, page_1879, page_1886

This table enables the automation to locate the matching 1879 or 1886
page when resolving ambiguities or checking errors, and to track which
1920 pages have been processed and which come next. The table is built
incrementally as pages are processed.

### Ambiguity Resolution (i / l / 1 in Footnotes)

**The 1879 cross-check below is MANDATORY, not discretionary, for every
superscript or cross-reference letter that is i, l, or 1** — in either
the current chapter's own lettering or a "Véase [letter], Book Chapter"
cross-reference target letter. This applies regardless of how clear or
confident the 1920 reading looks. "It looks clear to me" is exactly the
failure mode this rule exists to prevent: on 2026-07-12 (Helamán 6,
footnote 6n → 3255), an "i" was transcribed as "l" from the 1920 image
alone during Session A, and a second look at the *same* 1920 crop during
Session B "confirmed" the wrong letter again — described in the
verification notes as "tall stem, no dot," which does not match the
glyph's actual shape (a short stroke with a separated dot). The error
was only caught when the user challenged it and 1879 was actually
consulted, which settled it immediately and unambiguously ("n, see i,
II. Nep. 10."). A same-image re-read is not independent verification and
does not satisfy this check — Session B must not skip the 1879 step for
an i/l/1 letter just because the 1920 reading already looks settled from
Session A.

**Beyond the mandatory i/l/1 case, you always have discretion to extend
this same procedure to any other letter** if your own judgment says the
glyph might be ambiguous, even letters not in this named set — that
discretion runs only in the direction of doing more checking, never less.
There is never discretion to skip the check for i, l, or 1 specifically.

**Provisional alphabetical-sequence inference for hard-to-read swash
letters (validated 2026-07-13, Helamán 6, page 451):** some pages print
Block 1 reference letters in a heavily stylized cursive/swash font where
several individual letters in a row (that page's s, t, v, x, y, z) are
genuinely difficult to distinguish by shape alone, even at high zoom.
Since footnote letters within a chapter always run strictly alphabetically
(rule 13) with no gaps or reordering, it is valid to provisionally assign
letters by position in the sequence plus a content-fit check against each
target reference (Section 8's content-fit sanity check), then treat that
assignment as unconfirmed until Session B's independent 1879 check —
do not skip Session B's check just because the sequence "must" be right.
On page 451 this approach was later fully confirmed letter-for-letter
against the clearer 1879 typeface, including body-text marker placement,
validating both the technique and the specific glyph shapes involved (the
1879 font renders these as ordinary italic letters, unlike 1920's swash
style). This is not a substitute for the mandatory i/l/1 check above when
the ambiguous letter is actually i, l, or 1 — it is a separate, discretionary
technique for the *other* letters that also happen to be hard to read in
this particular font.

Procedure:

1. **Same-page reference comparison first.** Before reaching for 1879,
   crop the uncertain glyph and a same-page (ideally same footnote block)
   instance of a known letter — the letter you believe it to be, plus at
   least one visually distinct neighbor (e.g. if you read it as "l," also
   grab an "i" or "c" from the same block if one is present) — at matching
   zoom, and compare stroke shape directly: a continuous unbroken curve
   ("l") reads differently from a short stroke with a separated dot ("i")
   or a small open hook ("c"). Do this from a fresh crop each time, not
   from memory of an earlier read of the same image.
2. Use the chapter/page lookup table (`chapter_map.csv`) to find the
   corresponding 1879 page. Note 1879's own pagination does not track
   1920's page-for-page — the matching content may land a page or two
   later than the listed file_page number suggests; check adjacent pages
   if the expected verses aren't on the first one loaded.
3. Read the 1879 page image at the same footnote position. The 1879
   printing is generally clearer for these characters.
4. If still uncertain, crop the 1886 body text at the annotated verse
   to identify which word is being referenced, then infer the letter.
5. For very small superscripts, re-run crop_page.py on the 1920
   full-page image at 5× or 6× zoom on just the superscript line.
6. When comparing 1920 against 1879, match entries by their TARGET
   reference content (the book/chapter/verse being cited), not by letter
   or list position — the two editions' own letter sequences, and even
   the order footnotes are listed, can diverge because of translation
   word-order differences (see rule 26). A mismatch in position alone is
   not evidence of an error.
7. As an independent check, the target chapter's own footnote block can
   sometimes be searched for a back-reference to the current verse,
   which can resolve an ambiguous letter even without consulting 1879.
8. **Content-fit sanity check.** Once a target is resolved, check whether
   its citation content is thematically plausible for the verse being
   annotated. This is corroborating evidence, not proof by itself — but a
   resolved target that reads as thematically odd (e.g. a robbery/murder
   verse citing an unrelated genealogy passage) is a reason to double
   back and re-verify, not something to wave through because the letter
   "looked right."

### pptext and Spanish Word Review

pptext (https://github.com/DistributedProofreaders/pptext) is written
in Go and uses aspell internally for spell-checking. It takes the source
file, a good-words file, a language flag, and a verbose flag. The
command when run locally is:

```
pptext -i librodm.txt -g "permitted words.txt" -a es -v
```

pptext suppresses any word already in `permitted words.txt`, so the
flagged output shrinks as that list grows. Remaining flagged words
require human judgment: archaic words go to `permitted words.txt`;
genuine 1920 errors go to `errors in 1920.txt`. The transcription
(librodm.txt) is never changed at this stage.

**Line-length target (72, not 80) — 2026-07-11 decision:** rule 9's
72-character line-length cap was chosen over the project's earlier
79-character cap after checking both pptext's own source and
Distributed Proofreaders' official guidance:
- pptext's "long lines check" hardcodes a threshold of `> 72` chars
  (confirmed by reading `tcLongLines()` in `pptext.go`) — 72 or under
  never gets flagged, 73+ always does. A separate `LONGEST_PG_LINE = 75`
  constant exists in the source but is never actually referenced
  anywhere else — dead code, not the real enforced threshold.
- DPWiki's own guidelines (the organization pptext and pgdp.net belong
  to) state the target for PPV (Post-Processing Verification) readiness
  is explicitly 72 characters — this is DP's stated standard, not a
  rule of thumb.
- General gutenberg.org guidance is looser and vaguer (~65-70, with
  historical mentions of ~72 from the fixed-width-terminal era), but
  since this project's tooling (pptext) is DP's own, DP's specific
  72-character figure is the most directly relevant number.
- A statistical check of line lengths across the document found the
  79-character ceiling was essentially never approached naturally (only
  ~0.16% of lines fell in the 76-79 range; the actual mode was ~59-63
  chars) — so 79 was not a "natural" cutoff being organically produced
  by the transcription process, just a looser ceiling than necessary.
  Retroactively tightening to 72 therefore only required fixing ~124
  lines in librodm.txt and 22 entries in librodm_foot.txt (all fixed
  2026-07-11 via a word-cascade / per-entry reflow, verified against
  backups by exact word-count and non-whitespace-character-count match
  — no content lost or altered, only line-break positions moved).

### Additional Reference Resources for Orthography Decisions

These sources split into two roles (see Step 3 in Section 9 for how
they combine into a decision): pptext/aspell and the modern edition
judge whether a word matches **current** Spanish usage; 1886, RAE, and
1946 judge whether a word unrecognized by those is a **legitimate
archaic/period form**. When a flagged word's status isn't settled by
the 1886 comparison alone, these additional resources are available,
roughly in order of how directly they bear on the archaic-legitimacy
question:

- **1886 Spanish edition** — same translation lineage as 1920, just
  cleaner typesetting. Primary source of comparison; see Reference PDFs
  above. Already integrated into the automated pipeline via
  chapter_map.csv page lookups.
- **1946 Spanish edition** — a later printing of essentially the same
  1920 translation, with many of the exact kinds of errors this project
  runs into (misspellings, typos) already corrected. This is the single
  most direct source of evidence for "is this a genuine 1920 printing
  error," but it is **not digitized or in the public domain**, and the
  editor's copy is a physical book — Claude cannot access it. This stays
  a manual, editor-only lookup. When it informs a decision, cite it in
  `errors in 1920.txt` as a `(1946: ...)` note, same style as the
  existing `(1886 note)`.
- **RAE DLE** (https://dle.rae.es/) and **DPD** (https://www.rae.es/dpd/,
  *Diccionario panhispánico de dudas*) — no stable public API, and
  **direct `WebFetch` to dle.rae.es returns HTTP 403 every time**
  (confirmed repeatedly, e.g. 2026-07-12 — the site blocks the fetcher,
  not a transient failure). Use `WebSearch` instead
  (`dle.rae.es "<word>" definición`) — Google's index surfaces the DLE
  page as a result with a snippet/summary. This is a real but weaker
  form of evidence than reading the live entry: a search snippet may
  not surface usage labels like *desusado*, so treat a WebSearch-sourced
  RAE confirmation as good evidence a word exists/doesn't exist at all,
  but not as conclusive on subtler questions (register, archaic marking)
  the way actually reading the DLE page would be. If a claim needs that
  level of certainty, flag it to the editor for a manual browser check
  rather than treating the WebSearch snippet as definitive.
  DLE is the primary reference for confirming archaic (desusado) forms;
  DPD is used for specific grammatical usage questions. These check the
  word against the broader Spanish language, independent of this
  particular translation.
- **Modern Spanish Book of Mormon**
  (https://www.churchofjesuschrist.org/study/scriptures/bofm?lang=spa) —
  a current official LDS Spanish edition. Claude can fetch individual
  chapters directly (URL pattern:
  `.../study/scriptures/bofm/{book}/{chapter}?lang=spa`, e.g. `hel/5` or
  `alma/48`; tested working, full verse text renders without JS issues).
  Important caveat: **this is an independent, modern translation, not a
  corrected/modernized 1920** — sentence wording differs substantially
  verse-by-verse even where the meaning matches, confirmed by direct
  comparison (Helaman 5:1-4 phrased quite differently in each). So do not
  expect a full-sentence match, and don't treat a word's absence from the
  modern verse as meaningful either way. But within the same verse,
  individual vocabulary words often DO recur unchanged despite the
  surrounding sentence being reworded — when a flagged 1920 word also
  appears in the corresponding modern verse, the modern spelling and
  accentuation of that shared word is good evidence for the correct
  current form (useful for judging whether the 1920 form is a legitimate
  archaic/period spelling, an OCR misread, or a genuine printing error).
  It's also useful for: confirming proper name/place name spellings
  (stable across translations) and a general sanity check that the right
  content was transcribed for the right verse. No
  PDF/EPUB download was found for it; per-chapter fetching is used
  instead.
- **Local reference corpora** (`workspace/reference_corpora/`) — large
  public-domain Spanish texts, downloaded once and kept locally so a
  flagged word can be grep'd against them directly (exact string search,
  no summarization/lossiness the way a WebFetch-through-a-model call
  would have). Run this check routinely for every flagged word, not just
  when other evidence is ambiguous — a zero-hit result across all three
  is itself informative (word not attested in general literary or
  biblical-register Spanish), and a genuine hit can settle a spelling
  question outright (e.g. Reina-Valera's one hit for "separado", zero
  for "seperado", 2026-07-12).
  - `quijote_gutenberg2000.txt` — *Don Quijote de la Mancha* (Cervantes),
    Project Gutenberg ebook #2000
    (`https://www.gutenberg.org/cache/epub/2000/pg2000.txt`). Classic
    17th-century literary Spanish — good for "is this word attested in
    Spanish at all, historically," not for period-accurate spelling
    circa 1880-1920 (300+ years earlier than this project's editions).
  - `reina_valera_1909_nt_gutenberg5881.txt` — Reina-Valera New
    Testament, 1909 revision, Project Gutenberg ebook #5881
    (`https://www.gutenberg.org/cache/epub/5881/pg5881.txt`). Clean
    plain text, not OCR. The 1909 revision date sits almost exactly
    between the 1886 and 1920 editions used in this project, making it
    the closest-vintage corpus available — the best of the three for
    judging whether a spelling was a live period variant versus a
    genuine typo.
  - `reina_valera_full_bible_archiveorg_ocr.txt` — full Old+New
    Testament Reina-Valera (Casiodoro de Reina 1569 / Cipriano de Valera
    1602 lineage; exact revision year not stated by the source, BYU/
    archive.org scan, item `lasantabibliaant00rein`), fetched via
    `https://archive.org/download/lasantabibliaant00rein/
    lasantabibliaant00rein_djvu.txt`. Much larger vocabulary coverage
    (full OT+NT vs. NT-only) at the cost of being OCR'd — expect some
    scanno noise, so treat a single hit cautiously (check the surrounding
    OCR'd context isn't garbled) but treat a zero-hit result the same as
    the other corpora.
  - Search with plain `grep -i` (or the Grep tool) for the exact
    flagged spelling, its dictionary-correct counterpart, and (as a
    sanity check that the search itself is working) a common word known
    to appear frequently — an unexpected zero on the sanity-check word
    means something is wrong with the search, not the corpus.
  - If a corpus file is ever missing/deleted, re-download with the URLs
    above (Gutenberg files: `curl -sL -o <name> <url>`; the archive.org
    file is the largest at ~5.4MB and can take a few seconds longer).

---

#### Option A — Fully automated pptext (future goal)

Requires: Go installed (`winget install GoLang.Go`), aspell with Spanish
dictionary installed via MSYS2, pptext compiled from source, and
`scannos.txt` + `hebelist.txt` placed next to the executable.

Once set up, the automation script calls pptext directly, parses its
output, cross-references the 1886 PDF for each flagged word, and
produces a draft update to `permitted words.txt` and `errors in 1920.txt`
for editor review. No web interface needed.

#### Option B — Semi-automated (current approach)

The automation script handles the preparatory work:

1. **Python spell-check pre-pass:** `pyspellchecker` (pip install
   pyspellchecker) with Spanish word list runs against the new page
   text only (not the full librodm.txt). Words not in `permitted words.txt`
   and not passing the Spanish spell-check are flagged.
2. **1886 comparison:** For each flagged word, the automation locates
   the corresponding 1886 page (via chapter_map.csv), crops that region,
   and reads the text to find how the word appears in the 1886 edition.
   It reports: same form in 1886, different form in 1886, or not found.
3. **Review report:** The automation writes a short `review_NNN.txt`
   listing each flagged word, its location, and the 1886 finding —
   giving the editor the context needed to make a quick decision.

The editor then:

4. Runs pptext via the web interface on the updated `librodm.txt` for
   the authoritative full-document check.
5. Cross-references the automation's `review_NNN.txt` to resolve each
   flagged word quickly.
6. Adds approved words to `permitted words.txt` or `errors in 1920.txt`
   using RAE DLE for any uncertain cases.

**Option B is the current approach.** Option A can be adopted later
once Go and aspell are set up.

### Automation Pipeline

The goal is a single command such as:

```
python add_pages.py 441 442 443
```

which performs all of the following, leaving only a review step for
the editor:

1. Rasterize 1920 page images (from pre-split `pages_1920\` folder).
2. Extract body text and footnotes from image crops.
3. Resolve superscript ambiguities using the 1879 page (via lookup
   table).
4. Write page_NNN.txt (body + Block 1 + Corrections log).
5. Proceed through Review Pass (Section 9): footnote check; insert body
   text into librodm.txt before `Notas` and append Block 1 footnotes to
   librodm_foot.txt (both via insert_body_text.py); orthography check;
   permitted_words.txt / errors in 1920.txt updates.
6. Generate and append Block 2 footnotes to the end of librodm.txt
   (done in review pass, after cross-references are resolved).
7. Run pptext and Spanish dictionary check; propose additions to
   `permitted words.txt` and `errors in 1920.txt` for editor review.
8. Update chapter_map.csv with the newly processed pages.

The editor reviews the four master files and proposed additions,
corrects any mistakes, and approves. No manual integration work.

---

## 9. Review Pass

After completing a page_NNN.txt file, perform the following steps
before integrating into the master files.

### Step 1 — Footnote Check

1. For each Block 1 entry, verify the reference is correctly read from
   the fn_zoom image (chapter, letter, text).
2. Confirm each cross-reference letter (e.g. "Véase c, Mosíah 29")
   matches what is printed. When ambiguous (i/l/1), consult the 1879
   page via chapter_map.csv, matching by target content (see Section 8,
   Ambiguity Resolution).
3. Confirm the `[N]` marker in the body text is placed immediately
   before the correct word and corresponds to the right Block 1 entry.

### Step 2 — Integrate Body Text and Block 1 Footnotes

4. Once footnotes are verified (Step 1 complete), insert the page's body
   text into librodm.txt immediately before the `Notas` line (scan
   backwards from end of file to locate it), preceded by a blank-line
   separator per the existing `Página N` block convention (see rule 10
   for the page-boundary word-split case).
5. Append the page's Block 1 entries to the end of librodm_foot.txt,
   normalized to one space after the colon (rule 16). No blank line
   between entries, except when a new book starts (an entry's chapter
   number is lower than the previous entry's): insert a blank line, the
   book name in caps with no trailing punctuation, and another blank
   line before the new entry. Take the book name from that page's own
   body text — the all-caps title line above its `CAPÍTULO 1.` heading
   (see rule 19 example).
6. Use `insert_body_text.py NNN [NNN ...]` to do both of these
   mechanically; it can take a run of several verified pages at once.
   Pass `--footnotes-only` to append just the Block 1 entries if body
   text was already inserted in an earlier run, or `--body-only` to
   insert just the body text and defer the Block 1 append. Block 2
   footnotes are NOT generated at this step — that is Step 3, next.

### Step 3 — Generate Block 2

7. Once footnotes and text are confirmed, generate Block 2 entries
   from Block 1, resolving cross-references to sequential numbers
   where the target is known. Resolution is book-aware: chapter+letter
   identifiers like "29c" are not unique across the whole document
   (several books have a chapter 29), so matching happens within the
   correct book section of librodm_foot.txt, not just the first line
   matching the chapter+letter pattern. Unknown targets keep the
   original letter form. Format: `number: Reference text.` — no
   brackets, ONE space after the colon (matches the actual convention
   already in librodm.txt's Notas section).
8. Append Block 2 footnotes to the end of librodm.txt.
   This runs BEFORE the orthography check (Step 4) deliberately: Block 1
   (the actual footnote reference wording) lives only in
   librodm_foot.txt, which pptext never scans — that text only becomes
   visible to pptext once it's resolved into Block 2 and appended into
   librodm.txt. Checking orthography first would mean scanning
   incomplete content and having to re-run pptext afterward anyway.
   Block 2 lines follow the same 72-character limit as body text (rule
   9), since this content lives in librodm.txt and IS what pptext scans
   (unlike Block 1/librodm_foot.txt — see rule 18). When a Block 2 entry
   needs to wrap, prefer breaking at a semicolon between whole
   references over splitting a single reference apart: e.g. for
   "...Helamán 14:12; Alma 38:37; ...", wrap so the semicolon after
   "14:12" is the last character on the line and "Alma 38:37" starts
   the next line whole — never split as "...Alma" / "38:37...".
9. Use `generate_block2.py NNN [NNN ...]` to do this mechanically — it
   builds a book-aware index from librodm_foot.txt, resolves `Véase
   <letter(s)>[, <Book> <Chapter>]` cross-references (including
   multi-letter forms like "p y q") to bare sequential numbers, and
   reports any that stay unresolved (target not yet transcribed).
   Run `generate_block2.py --fix-unresolved` to rescan every existing
   Block 2 entry in librodm.txt and re-resolve ones that couldn't be
   resolved when first generated — **run this once the entire Book of
   Mormon has been transcribed** as a final cleanup pass (can also be
   run earlier/periodically if useful).

### Step 4 — Orthography Check

**(Provisional — this decision process will be refined by working
through real examples together in an actual Session E run.)**

`permitted words.txt` and `errors in 1920.txt` are NOT alternative
destinations for a flagged word — one is a broad suppression list, the
other a narrow, separate log layered on top of it. A word can end up in
`permitted words.txt` alone, or in both files together, but never in
`errors in 1920.txt` alone.

9. Run the Python spell-check pre-pass on the new page text only
   (not the full librodm.txt):
   `python spellcheck_page.py page_NNN.txt`
   Words not in `permitted words.txt` and not passing Spanish
   spell-check are flagged. This (and the modern edition, Section 8)
   only signals "doesn't match current usage" — it says nothing about
   whether the word is archaic-valid, unique BoM vocabulary, or a
   genuine error.
10. Every flagged word, once reviewed, gets added to
    `permitted words.txt` (one word per line) — regardless of verdict.
    This is what stops it from being re-flagged on every future run;
    `permitted words.txt` is a noise-suppression list, not a certificate
    of correctness. This includes archaic forms, BoM-unique proper
    nouns/terms, accent variants, and even genuine documented errors
    (since the transcription still preserves them as-printed).
11. Decide whether the word ALSO needs an `errors in 1920.txt` entry:
    - **Not an error — skip the errors log**: the discrepancy is just a
      missing accent (1886 frequently omits accents too), or the word is
      unique to the Libro de Mormón (proper nouns, invented/theological
      terms) that generic spellcheck/modern-text comparison will always
      flag regardless of correctness.
    - **Possible genuine misspelling/typo**: for anything else, check
      for archaic-legitimacy evidence — compare against the 1886 page
      (via chapter_map.csv), check RAE DLE/DPD, and the editor's manual
      1946 check when available (Section 8, Additional Reference
      Resources).
      - Evidence of legitimate archaic/period usage found → NOT added
        to `errors in 1920.txt` (stays in `permitted words.txt` only).
      - No archaic evidence found → ALSO add to `errors in 1920.txt`,
        format: `Book Chapter:Verse error (correction) (evidence note)`.
        Logged on "no evidence found" rather than "proven wrong" — this
        is being judged for modern readers, so absence of archaic
        justification is enough, even if period-legitimacy can't be
        fully ruled out.
12. **Transcription error** is a separate, unrelated track: our own
    image-reading is wrong, independent of whether the word itself is
    valid. Correct directly in page_NNN.txt and log in Corrections — do
    not add the misread form to `permitted words.txt`.

---

### Planned Project Reorganization

Once the automation pipeline is in place:

- The rules MD file moves up one level to `libro_de_mormon_1920\`.
- `extracted pages\` remains as a workspace for intermediate files
  (page images and page_NNN.txt drafts).
- All product output (the four master files) stays at the
  `libro_de_mormon_1920\` level.
- Subfolders `pages_1920\`, `pages_1879\`, `pages_1886\` hold the
  pre-rasterized page images.
