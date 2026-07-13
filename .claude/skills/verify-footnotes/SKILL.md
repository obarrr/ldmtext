---
name: verify-footnotes
description: Session B of the Libro de Mormón 1920 transcription workflow — verifies footnote superscripts in an already-transcribed page against the source image. Use when the user asks to "verify footnotes for page NNN."
---

# Session B — Verify footnote superscripts

Trigger: "Verify footnotes for page NNN."

1. Read `pages/page_NNN.txt`.
2. Read the fn_zoom image for that page.
3. For each Block 1 entry: confirm the reference text matches the image exactly.
4. Confirm each `[N]` marker is placed before the correct word in the body.
5. For every letter that is i, l, or 1 — in this page's own lettering or in a
   cross-reference target — the 1879 check is MANDATORY, not discretionary,
   regardless of how clear the 1920 reading looks: run `process_page.py` on
   the matching 1879 page (from pages_1879/, file_page from
   chapter_map.csv — note 1879's pagination doesn't track 1920's
   page-for-page, so check adjacent pages if needed), read its fn_zoom, and
   confirm the letter from the clearer 1879 printing. Re-reading the same
   1920 crop again does NOT satisfy this step — it must be the independent
   1879 source. You additionally have discretion to run this same check on
   any OTHER letter your judgment flags as possibly ambiguous, even outside
   i/l/1 — that discretion only ever adds scrutiny, never skips it for
   i/l/1. See `libro_de_mormon_rules.md` Section 8 for the full procedure,
   including a same-page glyph comparison step to run before 1879.
6. Edit `pages/page_NNN.txt` to fix any errors; add to Corrections section.

Output: `pages/page_NNN.txt` with verified footnotes.
