---
name: transcribe-page
description: Session A of the Libro de Mormón 1920 transcription workflow — transcribes one page of the source PDF into pages/page_NNN.txt. Use when the user asks to "transcribe page NNN" (optionally with "first footnote NNNN"), or otherwise asks to start transcribing a new page of the Libro de Mormón project.
---

# Session A — Transcribe the page

Trigger: "Transcribe page NNN[, first footnote NNNN]."

1. Read `libro_de_mormon_rules.md` (authoritative transcription rules).
2. Determine the first footnote number:
   - If the user supplied one, use it.
   - Otherwise, look for `pages/page_{NNN-1}.txt` (the previous page). If it
     exists and looks complete (has a well-formed Block 1 section), read its
     last Block 1 entry's sequential number and use last + 1 as the first
     footnote number for this page — no need to ask the user.
   - If the previous page file doesn't exist, doesn't look complete, or
     anything about the derivation is ambiguous, ask the user what the
     first footnote number should be rather than guessing.
3. Run `process_page.py` on the pre-rasterized PNG for this page (from
   `pages_1920\`, file_page = book_page + 22, e.g. `py process_page.py
   pages_1920\page_0475.png 453 3270`) to generate crops — never pass the
   raw PDF; Poppler is not part of the normal per-page workflow.
4. Read fn_zoom, top, mid, bot images. While reading, count the number
   of body-text print lines visible in each crop and note the total —
   this is the line count your raw transcript must match before any
   rule 7/8 adjustment.
5. **Raw line-by-line transcript first.** Transcribe each image line as
   its own output line, in order, straight off the images — this is a
   literal line-by-line copy, never composed as flowing prose and then
   wrapped or reflowed to a target width (rule 6). Confirm the raw line
   count matches what you counted in step 4 before moving on.
   (Confirmed failure mode 2026-07-19, page 475: the whole page was
   generated as continuous prose and rewrapped to ~72 chars, so no line
   boundary matched the image even though every line was under the
   length cap — see `libro_de_mormon_rules.md`'s rule 6 note.)
6. **Mechanical reconstruction pass — do this fully, for the whole page,
   before any investigative work in step 7.** Line by line, straight off
   the images: rejoin every hyphenated line-break split per rule 7
   (remove the hyphen, reattach any punctuation directly following the
   second half, recompute length, apply rule 8 rebalancing if the
   rejoined line hits 73+ chars), and clean up space-before-punctuation
   per rule 31. This is a no-judgment, rule-mechanical pass — don't mix
   it with the harder investigative work below. (Confirmed failure mode
   2026-07-14, Helamán 7 page 455: two hyphen rejoins were skipped
   because they got reconstructed from memory after several intervening
   typo/footnote-letter investigations rather than caught in a fresh,
   dedicated pass over the raw lines — the one rejoin that *did* survive
   only did because a footnote-marker insertion happened to force a
   character-count stop on that exact line. Sequencing the mechanical
   pass first, before anything competes for attention, is the fix — see
   `libro_de_mormon_rules.md`'s rule 7 note for the full incident.)
7. Now do the investigative work: for every superscript or
   cross-reference letter that is i, l, or 1, the 1879 mandatory check in
   `libro_de_mormon_rules.md` Section 8 applies now, at first transcription
   — do not defer it to Session B by default. Flag and zoom-verify any
   suspected misprints per rule 32 (preserve as printed, log in
   Corrections, never silently "correct").
8. Write `pages/page_NNN.txt` (body + Block 1 + Corrections).
9. Run `check_spaced_punctuation.py pages/page_NNN.txt` first — the
   mechanical backstop for rule 31 (flags any space before a comma,
   semicolon, colon, "!", or "?", whether from the original print or
   introduced during transcription; a hit inside the Corrections log
   itself may be a historical quote, not a live defect — check context).
   Then run `check_footnote_punctuation.py pages/page_NNN.txt` — the
   equivalent backstop for the page's own Block 1 entries (rules 22/23:
   flags a space before a comma/semicolon/colon or around a verse-range
   hyphen in a citation, e.g. "65 : 17" or "Alma 5 -10"). Fix anything
   either script flags in live text before moving on. (Added 2026-07-24
   after a run of pages — 470, 476, 495-502 — accumulated 91
   space-before-punctuation defects across `librodm.txt`,
   `librodm_foot.txt`, and three already-emailed chapter files before
   being caught; see the CLAUDE.md 2026-07-24/2026-07-24b entries.)
   Then run `check_lines.py pages/page_NNN.txt` — the mechanical
   backstop for line length (flags both overlength lines and any
   trailing hyphen a line-break split left behind), not a substitute for
   steps 5/6. Then run `check_line_wrap.py <book_page> pages/page_NNN.txt`
   — an advisory OCR-based cross-check that flags a body line count or
   length profile that looks reflowed rather than image-derived (see
   rule 6's note on the page 475 incident). A clean result from any of
   these scripts does not by itself prove the line breaks or punctuation
   are correct — only the per-line image read in step 5 does that.

Output: `pages/page_NNN.txt` ready for review.
