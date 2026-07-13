---
name: generate-block2
description: Session D of the Libro de Mormón 1920 transcription workflow — resolves Block 1 cross-references to sequential numbers and appends Block 2 entries to librodm.txt. Use when the user asks to "generate Block 2 for page NNN" or to run the fix-unresolved cleanup pass.
---

# Session D — Generate Block 2 and append to librodm.txt

Trigger: "Generate Block 2 for page NNN." (can take a page range)

1. Read `pages/page_NNN.txt` (must be fully verified before this step; body
   text and Block 1 already integrated into the master files in Session C).
2. Generate Block 2 entries from Block 1:
   - Resolve cross-references to sequential numbers by searching `librodm_foot.txt`
     for the matching chapter+letter entry, matched within the correct BOOK
     section (chapter+letter identifiers like "29c" are not unique across
     the whole document — several books have a chapter 29).
   - Unresolved targets keep the original letter form.
   - Format: `number: Reference text.` (no brackets, ONE space after the
     colon — matches the actual convention already in librodm.txt's Notas
     section).
3. Append Block 2 entries to the END of `librodm.txt`.

Use `generate_block2.py NNN [NNN ...]` to do this mechanically — it builds
a book-aware index from `librodm_foot.txt`, resolves `Véase <letter(s)>[,
<Book> <Chapter>]` cross-references to bare sequential numbers (including
multi-letter forms like "p y q"), and reports any that stay unresolved.
Run `generate_block2.py --fix-unresolved` any time to rescan every
existing Block 2 entry in `librodm.txt` and re-resolve ones that couldn't
be resolved when first generated (their target hadn't been transcribed
yet) — this must be run once the entire Book of Mormon has been
transcribed, as a final cleanup pass; it can also be run earlier/
periodically if useful.

Output: `librodm.txt` updated; page NNN is fully integrated. This runs
BEFORE Session E's orthography check deliberately: Block 1 (the actual
footnote reference wording) lives only in `librodm_foot.txt`, which
pptext never scans — that text only becomes visible to pptext once it's
resolved into Block 2 and appended into `librodm.txt`. Running Session E
first would mean checking incomplete content and having to re-run pptext
afterward anyway.
