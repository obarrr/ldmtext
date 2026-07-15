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
4. Read fn_zoom, top, mid, bot images.
5. **Mechanical reconstruction pass — do this fully, for the whole page,
   before any investigative work in step 6.** Line by line, straight off
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
6. Now do the investigative work: for every superscript or
   cross-reference letter that is i, l, or 1, the 1879 mandatory check in
   `libro_de_mormon_rules.md` Section 8 applies now, at first transcription
   — do not defer it to Session B by default. Flag and zoom-verify any
   suspected misprints per rule 32 (preserve as printed, log in
   Corrections, never silently "correct").
7. Write `pages/page_NNN.txt` (body + Block 1 + Corrections).
8. Run `check_lines.py pages/page_NNN.txt` — this is the mechanical
   backstop (flags both overlength lines and any trailing hyphen a
   line-break split left behind), not a substitute for step 5.

Output: `pages/page_NNN.txt` ready for review.
