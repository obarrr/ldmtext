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
3. Run `process_page.py` to generate crops.
4. Read fn_zoom, top, mid, bot images. For every superscript or
   cross-reference letter that is i, l, or 1, the 1879 mandatory check in
   `libro_de_mormon_rules.md` Section 8 applies now, at first transcription
   — do not defer it to Session B by default.
5. Write `pages/page_NNN.txt` (body + Block 1 + Corrections).
6. Run `check_lines.py pages/page_NNN.txt`.

Output: `pages/page_NNN.txt` ready for review.
