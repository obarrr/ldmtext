---
name: integrate-page
description: Session C of the Libro de Mormón 1920 transcription workflow — inserts a verified page's body text into librodm.txt and appends its Block 1 footnotes to librodm_foot.txt. Use when the user asks to "integrate pages NNN-NNN into librodm.txt and librodm_foot.txt" or similar.
---

# Session C — Insert body text and append Block 1 footnotes

Trigger: "Integrate pages NNN-NNN into librodm.txt and librodm_foot.txt."
(can take a page range, e.g. "Integrate pages 441-446.")

1. Read `pages/page_NNN.txt` (must already be verified — Session B complete).
2. Insert the page's body text into `librodm.txt` immediately BEFORE the
   `Notas` line (scan backwards from end of file to locate it), preceded by
   a blank-line separator, matching the existing `Página N` block convention.
   For multiple pages in one run, insert them in order, each separated from
   the next by a blank line, per rule 10 of `libro_de_mormon_rules.md`.
3. Append the page's Block 1 footnote entries to the END of
   `librodm_foot.txt`, normalized to one space after the colon. No blank
   line is inserted between entries — including across a same-book chapter
   boundary (rule 20) — EXCEPT when a new book of the Book of Mormon
   starts (detected when an entry's chapter number is lower than the
   previous entry's), in which case a blank line, the book name in caps
   (no trailing punctuation), and another blank line are inserted before
   the new entry. The book name is read from that page's own body text
   (the all-caps title line above its `CAPÍTULO 1.` heading).

Use `insert_body_text.py NNN [NNN ...]` to do both of these mechanically
rather than by hand — it locates `Notas`, extracts each page's body text
and Block 1 entries, and writes the results back to both master files. Add
`--footnotes-only` to append just the Block 1 entries when body text was
already inserted in an earlier run, or `--body-only` to insert just the
body text and defer the Block 1 append to a later run.

Output: `librodm.txt` and `librodm_foot.txt` updated. Block 2 generation
(resolving cross-references to sequential numbers) happens next in
Session D, before Session E's orthography check.
