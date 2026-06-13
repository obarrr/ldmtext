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

---

## 2. Body Text — Line Wrapping

5. Read every line ending directly from the image crop. NEVER approximate
   or guess line breaks from the OCR text or character-count estimation.
   Every line ending must be image-confirmed.
6. Reproduce the image line endings exactly, subject to rules 7 and 8.
7. Hyphenated word at end of line: remove the hyphen and rejoin the word.
   If the rejoined word appended to the first line is under 80 characters,
   keep it at the end of the first line. If 80 or more characters, move
   it to the start of the next line. Never preserve the hyphen split.
8. If a line as read from the image exceeds 79 characters in the output
   (e.g. due to added footnote markers), remove the last word and place
   it at the start of the next line. Repeat until the line is under 80
   characters. The removed words are prepended to the next image line.
9. Lines must be strictly less than 80 characters (i.e. 79 or fewer).

---

## 3. Footnote Markers in Body Text

10. Superscript letters in the original (a, b, c … z, 2a, 2b …) become
    `[N]` bracketed sequential numbers placed immediately before the word
    the superscript annotates — same position as in the original.
11. Footnote numbers run sequentially across the entire document and
    never restart.
12. Each chapter's footnotes restart at letter `a` in the original. If a
    new chapter begins mid-page, the letter sequence restarts at `a` for
    that chapter, but the global sequential number continues from where
    it left off.
13. NEVER trust the PDF OCR layer for superscript letters — it routinely
    misreads them. ALWAYS read superscript letters directly from the
    image (fn_zoom crop) before assigning footnote numbers.
14. Similarly, read inline superscripts from the body text image, not
    from the OCR text layer, to confirm which letter annotates which word.

---

## 4. Footnote Output — Two Blocks

Output TWO footnote blocks after the body text, separated by a blank line.

### Block 1 — Chapter+Letter Block

15. One entry per footnote, prefixed with chapter number and original
    letter, followed by the sequential number.
    Format: `[chapter][letter], [number]:  Reference.`
    Note: TWO spaces after the colon.
    When footnote letters extend past z into two-letter codes (2a, 2b,
    etc.), join the chapter number and letter code with a hyphen:
    `[chapter]-[2-letter code], [number]:  Reference.`
    Example: `3-2a, 3185:  Véase u, Alma 16.`
16. Cross-references use the original printed letters exactly.
17. Lines must be strictly less than 80 characters (79 or fewer).
    If a reference wraps, the continuation is flush left (no indent).
18. If a new book of the Book of Mormon begins within the block, insert
    the book name on its own line with a blank line above and below it.
19. If a chapter boundary falls mid-page, insert a blank line in the
    block between the last entry of the closing chapter and the first
    entry of the new chapter.

### Block 2 — Number Block

20. One entry per footnote using sequential numbers only.
    Format: `[number]: Reference.`
    Note: ONE space after the colon.
21. Cross-references resolved to sequential numbers where the target is
    known. If the target footnote is from a prior session and the number
    is unknown, keep the original letter for manual resolution.
22. Lines must be strictly less than 80 characters (79 or fewer).
    If a reference wraps, the continuation is flush left (no indent).
23. If a chapter boundary falls mid-page, insert a blank line in the
    block between the last entry of the closing chapter and the first
    entry of the new chapter.

### Footnote Reference Formatting (both blocks)

24. Semicolons between multiple references; period at end of entry.
25. No spaces around colons in references (e.g. `18:22` not `18 : 22`).
26. Sequential verse ranges use `-` (e.g. `3:6-19`).
27. Non-sequential verses use `,` (e.g. `3:12,19,24`).
28. Mixed: e.g. `4,17-18` means verse 4 and verses 17-18.

### Examples

Single chapter, no boundary:
```
3a, 3159:  Norte América.
3b, 3160:  Versículos 5, 9.

3159: Norte América.
3160: Versículos 5, 9.
```

New book beginning mid-block:
```
63p, 3137:  Estas numerosas copias de sagrados libros fueron
indudablemente copiadas directamente de ó comparadas con los
anales sobre las originales planchas de bronce.
63q, 3138:  Alma 37:27-32.

LIBRO DE HELAMÁN

1a, 3143:  Alma 50:40.
1b, 3144:  Véase c, Mosíah 29.

3137: Estas numerosas copias de sagrados libros fueron
indudablemente copiadas directamente de ó comparadas con los
anales sobre las originales planchas de bronce.
3138: Alma 37:27-32.
3143: Alma 50:40.
3144: Véase c, Mosíah 29.
```

Chapter boundary mid-page (chapter 2 closes, chapter 3 opens):
```
2a, 3158:  Véase f, I Nefi 1.

3a, 3159:  Véase 3166, Omni 1.
3b, 3160:  Norte América.

3158: Véase f, I Nefi 1.

3159: Véase 3166, Omni 1.
3160: Norte América.
```

---

## 5. Corrections Log

29. After the two footnote blocks, include a `Corrections` section
    listing every OCR error or typo corrected, in the format:
    `[verse or footnote ref] "original" → "corrected" — reason`

---

## 6. OCR Corrections

30. Rejoin hyphenated word splits from line breaks
    (e.g. "sepa-rados" → "separados"). See rule 7 for placement.
31. Fix name OCR errors: "Nef" / "Nefl" → "Nefi".
32. Fix word OCR errors as identified by visual inspection of the image
    (e.g. "fileles"→"fieles", "hahogó"→"ahogó", "coro"→"oro",
    "Covenios"→"Convenios").
33. Remove OCR-added spaces before punctuation
    (e.g. "dijo :" → "dijo:", "sí ," → "sí,").
34. Preserve 1920 Spanish spelling conventions exactly: á, vió, fué, etc.
    Do NOT modernize.
35. Remove "Digitized by Google" watermark text entirely.
36. Roman numeral "I" mis-read as digit "1" in book/chapter references
    should be corrected by context.

---

## 7. Session Workflow

1. Copy scripts to /home/claude/ from the project folder.
2. Run: `python3 process_page.py <pdf> <page_label> <first_fn_number>`
3. View fn_zoom image to read all footnote superscript letters.
4. View full page image to read all body text line endings and inline
   superscripts. Additional crops via crop_page.py only when needed.
5. Write output file: body text, then Block 1, then Block 2, then
   Corrections.
6. Run: `python3 check_lines.py page_NNN.txt` — fix any lines ≥ 80.
7. Copy to /mnt/user-data/outputs/ and call present_files.

**The starting footnote number for each session is provided by the
editor. Example: page 437 starts at footnote 3151.**

Scripts:
- **process_page.py** — rasterizes PDF at 400dpi, produces full page
  and section crops: top, mid, bot, fn, fn_zoom.
- **check_lines.py** — flags any lines ≥ 80 characters.
- **crop_page.py** — zooms into a specific region for closer inspection.
