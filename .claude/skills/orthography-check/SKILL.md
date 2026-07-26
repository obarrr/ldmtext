---
name: orthography-check
description: Session E of the Libro de Mormón 1920 transcription workflow — runs the orthography/spellcheck review for a page and decides on permitted-words vs. errors-in-1920 entries. Use when the user asks for an "orthography check for page NNN."
---

# Session E — Orthography check

Trigger: "Orthography check for page NNN."

1. Read `pages/page_NNN.txt` and `permitted words.txt`.
2. Identify unusual words (accents, archaic spellings, possible OCR errors).
3. For each flagged word: run `process_page.py` on the matching 1886 page
   (from pages_1886/, file_page from chapter_map.csv), read the relevant crop,
   note how the word appears in 1886. **Always additionally do independent
   research, even when the 1886 comparison seems to settle the question**
   — don't skip this because 1886 matched or because the call feels
   obvious. At minimum: (a) look up the word in RAE DLE via `WebSearch`
   (query: `dle.rae.es "<word>" definición`) — **not** `WebFetch`
   directly against `dle.rae.es`, which returns HTTP 403 every time
   (confirmed repeatedly, e.g. 2026-07-12; the site blocks the fetcher)
   — to confirm it's a real Spanish word (current or marked *desusado*)
   versus not a word at all, and (b) fetch the corresponding chapter of
   the modern Spanish Book of
   Mormon (`https://www.churchofjesuschrist.org/study/scriptures/bofm/
   {book}/{chapter}?lang=spa`) and check the same verse for a matching or
   analogous word, and (c) grep the flagged spelling (plus its
   dictionary-correct counterpart, plus a sanity-check common word)
   against the local reference corpora in `workspace/reference_corpora/`
   (Quijote, Reina-Valera 1909 NT, full Reina-Valera Bible — see
   `libro_de_mormon_rules.md` Section 8 for what each covers and why).
   See that same section for how to weigh all of these plus the 1946
   edition/DPD when available. A word absent from RAE entirely is a much
   stronger signal of a genuine error than a 1886-agreement alone — e.g.
   "seperado" (Helamán 5:35) appears identically in both 1920 and 1886,
   which looked at first like a settled period-spelling variant, but RAE
   DLE has no entry for "seperado" at all (only "separado"), and none of
   the three reference corpora contain "seperado" either (Reina-Valera's
   full Bible has one hit for "separado") — which is why this step is
   mandatory rather than conditional.
4. Propose decisions to the user for each flagged word:
   - Correct archaic/intentional 1920 form → add to `permitted words.txt`
   - Genuine 1920 error → add to `errors in 1920.txt`
     (format: `Book Chapter:Verse error (correction) (1886 note)`)
   - Transcription misread → correct in `pages/page_NNN.txt`, log in Corrections
5. User approves; Claude makes the edits.

Output: `permitted words.txt` and/or `errors in 1920.txt` updated.

**`errors in 1920.txt` new entries must be inserted in book/chapter/verse
order, never appended to the end of the file** (confirmed failure mode,
found and fixed 2026-07-14): the file is organized in canonical
Book-of-Mormon order (1 Nefi → 2 Nefi → Jacob → ... → Helamán → ...),
and every entry within a book runs in ascending chapter:verse order,
with chapter headings/footnote-only entries slotted near their
approximate verse position. For the entire history of this file, a
plain end-of-file append happened to *equal* correct sorted order,
because Session E only ever checked the page(s) currently being
transcribed, and pages are always transcribed in book order — so "new
finding" and "next in book order" were the same thing. That stopped
being true once whole-document sweeps were introduced (the "Mandatory
check" section above, and the pptext full-report walkthrough's
`errors in 1920.txt`-writing checks like "full stop followed by
unexpected sequence"): a single sweep can surface confirmed errors in
several different, already-transcribed books/chapters at once (e.g. one
2026-07-12 sweep found hits in Alma 13, 17, 43, 48, 49, 52, 57 *and*
Jacob 2 *and* Helamán, all in the same pass, while the page actively
being transcribed was in Helamán). Appending all of these to the end
of the file — instead of inserting each one at its own correct earlier
position — scattered Alma- and Jacob-book entries into the middle of
the Helamán section, and even shuffled the relative order of Helamán
entries found across two different sweep dates. This went unnoticed for
two commits before a user caught it by inspection. **Going forward:**
when a sweep or check finds confirmed errors outside the book/chapter
currently being transcribed, locate the correct insertion point for
each one individually (search the file for the nearest existing
Book/Chapter:Verse entry and insert immediately before/after it in
ascending verse order) rather than adding it wherever the file
currently ends. Plain append is still fine — and simplest — for the
common case where every new finding belongs to the page(s) just
transcribed, since that will always land at the true end of the file.

**Before proposing a `permitted words.txt` addition for a word noticed
by eye rather than sourced from an actual pptext flag, confirm pptext
actually flags it** (confirmed gap 2026-07-13): while auditing an older
page's Corrections log, "Jesu Cristo" (unaccented "Jesu") looked like a
natural spellcheck-suppression candidate — but a fresh pptext report
showed zero hits for "Jesu" anywhere in the ~1.15MB document despite 26
existing occurrences. aspell's Spanish dictionary already accepts it on
its own (almost certainly the old Spanish vocative/combining form of
"Jesús" used before another name, e.g. "Jesu Cristo," "Jesu Nazareno" —
the same pattern as "San" before "Pedro" instead of "Santo"), so it was
never being suppressed via the good-words list in the first place, and
adding it would have been a no-op. `permitted words.txt` only matters for
words aspell would otherwise flag — verify that's actually true (re-check
the current pptext report's Spellcheck Suspect Words section) before
adding anything discovered by manual reading rather than by the report
itself. This does not apply to words that already came from an actual
pptext flag (the normal case in step 3 above) — only to candidates
surfaced some other way, e.g. from a Corrections-log audit.

**A word can fail to appear in the Spellcheck Suspect Words section for
a reason unrelated to `permitted words.txt` entirely** (found
2026-07-17, pages 469-470): three brand-new, single-occurrence
misprints ("Poi", "dsesaría", "aninciado") were confirmed via direct
`aspell --list` piping (both standalone and embedded in their actual
sentence) to be flagged as misspelled, and a minimal 2-line
reproduction file run through the real `pptext` binary with the
project's actual `permitted words.txt` DID flag "Poi" correctly — but
the real full ~1.15MB `librodm.txt` run did not flag any of the three,
in ANY section of the report (confirmed by direct substring search
across the whole report, not just the spellcheck section). Line-number
citations elsewhere in the report were also found to be offset from
the true file by a regionally-varying amount (pptext appears to strip
blank lines or otherwise renumber internally), which makes any
line-range-based cross-referencing technique unreliable without first
confirming the offset in that specific region — prefer searching for
distinctive substrings from the page's own text directly against the
report instead of matching by line number. The root cause of the
full-document suppression was not tracked down (a likely suspect is the
"word occurs 5+ times anywhere in the document, in any case, and is
auto-accepted" rule in `aspellCheck()`, but the observed counts didn't
obviously reach 5 for these words — unconfirmed). Practical effect:
**the full pptext report is not proof a rare/new misprint won't be
flagged by aspell** — if 1886 comparison or independent research
already confirms a word is a genuine error, don't let a clean pptext
spellcheck section talk you out of logging it in `errors in 1920.txt`.
It only means no `permitted words.txt` entry is needed (matching the
"Jesu Cristo" no-op precedent above), not that the word is fine.

## Batch the narrow-space-vs-merge flags into this session's summary

Per `feedback_narrow_space_vs_merge`: when Session A defaults a tight
word-pair to two words (because 1886/grammar supports two words), it
notes this in the page's Corrections log at transcription time but does
NOT raise it to the editor mid-pipeline — Sessions A-D run straight
through without stopping on it. Session E is where these surface: sweep
the page's Corrections log for these notes and list them together in
this session's summary to the editor (book/chapter/verse, the two words
involved), so the editor can double-check against the actual image on
their own schedule. Don't re-litigate the call yourself — the two-word
transcription is already the committed default; this is purely a "you
may want to look at these" pointer, not a pending decision blocking
anything else in Session E.

## Mandatory check for any suspected error, in any section

This applies everywhere in Session E, not just the spellcheck/flagged-word
step above — every pptext section (dash, footnote, scanno, curly quote,
special situations, book/paragraph level, Jeebies), anything noticed by
eye while reading `librodm.txt` directly, **and every entry in the page's
own Corrections log** (`pages/page_NNN.txt`, the notes Sessions A/B/C
leave behind, e.g. "preserved as printed" / "apparent 1920 original
error" / "transcribed as printed"). That log is where a real error can
slip through undetected: it gets noted at transcription time but nothing
forces it to be checked against 1886 or promoted to `errors in 1920.txt`
— this happened with Helamán 3:32 "reinó las paz" (correctly flagged in
`page_441.txt`'s Corrections log back in Session A/B, but never checked
against 1886 or added to the master file until a reader found it later
in an emailed chapter). **Before finishing Session E for a page, read
that page's full Corrections log line by line and run every flagged
item through the same three-step check below**, exactly as if it had
just been noticed in `librodm.txt` — don't assume a note already being
in the Corrections log means it was resolved; the log records what was
*observed*, not what was *verified against 1886 or promoted*.

**Audit progress tracker**: this full-history sweep (every page's own
Corrections log, not just the current page's) was first run at scale on
2026-07-13, covering pages 437–452. It found and resolved 6
previously-undetected genuine 1920 errors (Helamán 4:5, 4:14, 5:10,
6:21 ×2, 6:22, 6:38 — see `errors in 1920.txt`) plus confirmed one
non-error ("Jesu Cristo," legitimate, matches 1886). It also caught a
transcription bug distinct from the missed-promotion pattern above: page
442's Corrections note for Helamán 4:5 correctly flagged a suspected
misprint, but the transcribed text itself had been silently changed to
the "expected" reading instead of preserving what was printed — see the
new note under rule 32 in `libro_de_mormon_rules.md` Section 6 for the
general rule this violated. **Going forward, a fresh page's Session E only needs to
sweep that page's own Corrections log** (the instruction two paragraphs
up) — pages 437–452 are now a clean baseline and don't need re-auditing
unless their transcriptions themselves change. One known gap surfaced
but not yet fixed as of 2026-07-13: `errors in 1920.txt`'s "Helamán 5:35
seperado" entry (logged 2026-07-11 or earlier) was never mirrored into
`permitted words.txt`, unlike every other preserved-as-printed error —
worth fixing whenever next touched, and worth spot-checking that new
`errors in 1920.txt` entries for preserved-as-printed words also get
their `permitted words.txt` counterpart (rule 10) at the time they're
added, not just eventually.

Whenever something looks like it might be a typographical or other error
in the 1920 print itself (as opposed to a pure transcription-accuracy
question):

1. **Check the matching 1886 image** at that exact location
   (`chapter_map.csv` for the file page, `process_page.py`/`crop_page.py`
   to read it). Matching the 1920 page image is **not sufficient** to
   clear a finding — that only confirms the transcription is accurate, it
   says nothing about whether the 1920 print deviates from 1886. See the
   "full stop followed by unexpected sequence" case in the Paragraph
   level checks notes below for the exact failure this causes: 6 hits
   were provisionally cleared against the 1920 image alone on
   2026-07-12, and all 6 turned out to be genuine 1920-only errors (1886
   had a comma every time) once actually compared to 1886.
2. **Check `errors in 1920.txt` for an existing entry** at that
   book/chapter/verse before concluding a finding is new — don't assume
   nothing is logged without checking, and don't create a duplicate
   entry.
3. **If 1886 differs from 1920 at that spot** (or independent
   research — RAE/modern edition/reference corpora, see step 3 above —
   establishes the 1920 form is simply wrong even where 1886 agrees),
   **add or update the entry in `errors in 1920.txt`**, in the existing
   format (`Book Chapter:Verse error (correction) (1886 note)`).
   Propose the addition to the user first, per step 5 above, same as any
   other flagged-word decision.

This is not limited to spellcheck suspects — apply all three steps to
anything flagged by any pptext section, and to anything noticed
independently while reading `librodm.txt`.

## Full pptext report walkthrough (beyond just spellcheck)

pptext produces many more sections than the spellcheck suspects list:
edit distance, hyphenation/spaced-pair consistency, adjacent/trailing
spaces, character checks, short/long lines, repeated words, duplicate
lines, ellipsis, dashes, footnote check, scanno check, curly quotes,
special situations, book/paragraph level checks. Session E should walk
through the FULL report, not just the spellcheck section.

**Step 0 — always regenerate the report first, every Session E run, no
staleness check.** Never reuse an existing `workspace/report_wsl_*.html`
without re-running pptext, even if it looks recent — the run only takes
about 30 seconds, so "always regenerate" is simpler and safer than
judging whether `librodm.txt`/`permitted words.txt` changed since the
last report (this is how Block 2 content for a just-integrated page
almost got reviewed against a pre-Session-D report earlier in this
project). From a Windows terminal:

```
1. Copy the two input files to a local staging folder (WSL can't see
   the Z: mapped drive):
   copy "librodm.txt" "C:\Users\<you>\AppData\Local\Temp\pptext_run\"
   copy "permitted words.txt" "C:\Users\<you>\AppData\Local\Temp\pptext_run\"

2. Run pptext from WSL (wrap in bash -lc so WSL's own shell expands
   `~`, not the outer Windows shell):
   wsl -d Ubuntu --cd '~' -- bash -lc '~/pptext/pptext \
     -i "/mnt/c/Users/<you>/AppData/Local/Temp/pptext_run/librodm.txt" \
     -g "/mnt/c/Users/<you>/AppData/Local/Temp/pptext_run/permitted words.txt" \
     -a es -v \
     -o "/mnt/c/Users/<you>/AppData/Local/Temp/pptext_run"'

3. Copy the result back into the project, named for today's date:
   copy "C:\Users\<you>\AppData\Local\Temp\pptext_run\report.html" ^
        "workspace\report_wsl_YYYYMMDD.html"
```

`-a es` (Spanish-only) and `-v` (verbose) and omitting `-t` (defaults to
every test category) match the pgdp.net web form's "run everything"
state — see `environment_setup.md` Part 2 for the full setup/validation
history and troubleshooting if the WSL/pptext install itself is broken.
Use the newly generated `workspace/report_wsl_*.html` for the rest of
this walkthrough.

**Do not wave a whole category through just because it's usually benign.**
Even when a pptext category (e.g. "these are all just accented capital
letters, a known period convention") seems very likely to be a non-issue
across the board, verify a meaningful sample of actual instances rather
than approving the category wholesale on the general pattern alone. A
mostly-legitimate category can still hide a real, specific exception —
this happened with the hyphenation/spaced-pair check: `Sumo-Sacerdotes`
vs `Sumo Sacerdotes` looked like an internal inconsistency question with
no clear answer, but checking each of the 5 instances against 1886
individually revealed 3 that matched 1886 (fine as printed) and 2 that
didn't (genuine 1920-specific errors, logged in `errors in 1920.txt`).
Bring findings to the user either way — even a confident "this looks
fine" conclusion is a proposal, not a unilateral decision; the user
always has final say and may weigh in differently.

**Not every check writes to `permitted words.txt` or `errors in
1920.txt`.** Some pptext checks (adjacent spaces, trailing spaces) flag
issues that are virtually always our own transcription artifacts, not
questions about the original 1920 print — fix those silently in the
page file's Corrections log, no research needed. Others (hyphenation/
spaced-pair consistency) don't consult `permitted words.txt` at all in
pptext's own implementation (it's a pure regex re-scan of the whole
document every run) — adding an entry there for a hyphenation finding
does nothing and should be skipped; only `errors in 1920.txt` applies
for a confirmed hyphenation-related error. Check what a given pptext
section actually does before assuming the standard permitted-words
workflow applies to it.

**Suppression via `permitted words.txt` is a blanket word-form match**
with no location awareness — once a word is added, aspell won't
re-flag ANY future occurrence of that exact word, even in a different
context where it might be a different situation. This is a deliberate
tradeoff to keep the page-by-page process manageable (re-litigating the
same archaic words on every single run isn't workable at full-book
scale), not an oversight. The mitigation: once the entire Book of
Mormon is transcribed, run pptext once more with `permitted words.txt`
emptied/renamed aside, and cross-reference every fresh flag against
`errors in 1920.txt` to catch any new-context exceptions that blanket
suppression would otherwise hide. Checks that don't use `permitted
words.txt` in the first place (hyphenation, edit distance, smart
quotes, jeebies, short/long lines, etc.) don't need this treatment —
they already re-scan fresh every run.

### Dash check

pptext's dash check has, in this project, exactly two buckets:
"adjacent dashes" (two or more dash characters run together, e.g.
`--`) and "hyphen-minus" (every other single hyphen not auto-approved
by pptext as a letter-hyphen-letter compound word). No en-dash,
figure-dash, or other Unicode dash character appears anywhere in the
document — the whole book uses plain ASCII hyphens only.

**Established convention (confirmed correct per Distributed
Proofreaders' own guidance — DPWiki Post-Processing FAQ and
Proofreading Guidelines, researched 2026-07-11):**
- Em-dash → `--` (two hyphens). DP's own wording: "for the plain text
  version, it is common to use hyphenated dashes rather than em
  dashes, though em dashes are acceptable" — `--` is DP's *expected*
  plain-text form, not a workaround. (Converting `--` to a real `—`
  character is the HTML-output step; not applicable to this project's
  plain-text deliverable.)
- Number/verse ranges → single hyphen, no spaces (`13:5-6`). Matches
  DP's documented "proofread as a single hyphen... usually no spaces
  in number ranges" convention.

No text changes resulted from this research — both conventions were
already in consistent use throughout `librodm.txt` and
`librodm_foot.txt`. This does not need to be re-researched in future
sessions; treat the convention above as settled.

**Going forward, per Session E run:**
1. "Adjacent dashes" bucket: skim only. pptext lists the first few
   `--` instances, then self-suppresses once it recognizes the book's
   convention (`book uses "--" as em-dash. not reporting further`).
   No research needed unless a listed instance ISN'T actually an
   em-dash use (three-or-more dashes run together, or `--` sitting
   where a plain range was clearly intended).
2. "Hyphen-minus" bucket: this is almost entirely legitimate
   number/verse ranges (`13:5-6`) and page-range table-of-contents
   entries; it does not need per-entry image/1886 verification. What
   IS worth a quick automated pass each time: confirm every hyphen in
   the bucket is directly flanked by a letter/digit on both sides
   (i.e. no floating `" - "` that could be a mistyped em-dash). A
   short script over the report's `hyphen-minus:` lines, checking the
   single character before/after each `-`, is enough — see the
   check performed on 2026-07-11 (938/938 clean).
3. **Blind spot pptext can't see**: pptext auto-approves any
   letter-hyphen-letter pattern as a compound word and never lists it
   in the report at all — so a single `-` mistakenly typed where `--`
   belonged (inside what looks like a compound word) would never
   surface in the report. Check for this independently of pptext by
   pulling every unique letter-hyphen-letter token straight out of
   `librodm.txt` (regex: a hyphen with a letter — including accented
   Spanish letters — on both sides) and eyeballing the distinct list.
   As of 2026-07-11, all ~79 unique forms are legitimate: Spanish
   compound ordinals (`décimo-nono`, `vigésimo-sexto`,
   `cuadragésimo-tercio`, etc.) or proper-noun/common-noun compounds
   (`Anti-Nefi-Lehi`, `Sumo-Sacerdotes`, `porta-estandarte`, etc.).
   `librodm_foot.txt` currently has zero such compounds. Re-run this
   scan periodically as new pages are added (each Session E is fine,
   or at minimum the final full-book pptext pass) rather than
   assuming it stays clean — this is the one part of dash check that
   isn't self-verifying from the pptext report alone.
4. This check never writes to `permitted words.txt` (pptext's dash
   check doesn't consult it, and never will regardless of blanket
   suppression). Any genuine dash error found would go straight to
   `errors in 1920.txt`.

### Footnote check

This is a newer pptext feature (not covered by earlier passes of this
project) that scans the whole document for the pattern `[NNN]` and
splits every match into two buckets purely by line position: a
"footnote anchor" is a `[NNN]` NOT at the start of a line (inline
call-out), a "footnote" is a `[NNN]`/`Footnote NNN:` that IS at the
start of a line (meant to catch definitions). **This distinction is
useless for our format**: our real footnote definitions in the Notas
section are plain `NNN: text` with no brackets, so pptext's
"footnote" bucket never matches any of them — what lands in it is
just inline anchors that happen to start a wrapped line by
coincidence. Don't read the two bucket labels/counts as meaningful;
what's useful is the union of every number in both buckets.

**How to actually use this check:** merge both buckets' numbers into
one set and diff against the full `1..<last footnote number>` range.
Three kinds of findings result, and each needs a different response:
1. **A number outside the valid range** (e.g. `[3890]` when the book
   only goes up to 3236) → almost certainly a digit-transposition typo
   for a nearby in-range number (check anchors immediately before/
   after it in the body for the correct neighborhood, then confirm
   the exact number via the Block 1 chapter+letter identifier and the
   page image). Fix directly in `librodm.txt`, no `errors in
   1920.txt` entry needed (our error, not the original's).
2. **A number used twice** → check both locations against Block 1's
   chapter+letter identifiers. Often one occurrence is legitimate and
   the other is a stray duplicate that actually belongs to a
   *different, nearby* number — this was the case for both `1445`/
   `1446` (Alma 2, should have been `1645`/`1646`) and is frequently
   linked to finding type 3 below (an off-by-one cascade makes a
   number get reused instead of skipped). Don't assume a duplicate is
   an isolated event — check the immediately surrounding anchors too.
3. **A number missing from the body entirely** → two distinct causes,
   and they require opposite responses, so don't assume either one:
   - **Genuine 1920 print defect**: the footnote text really is
     printed at the bottom of the page, but the printer never placed
     the corresponding superscript letter anywhere in the body. Only
     conclude this after checking *every word* of the relevant verse
     range at high zoom (both pages, if the passage spans a page
     break) and finding no candidate mark anywhere. When confirmed,
     make NO change to `librodm.txt` (we correctly transcribed what's
     printed) — instead log it in `errors in 1920.txt` in the
     existing "falta la nota X" style (see the `Mosiah 17:6`,
     `Mosiah 21:22`, `Alma 16:14`, `Alma 22:14` precedents), and if
     the 1879 Pratt English edition is available for that passage,
     check it too — English footnote letters often land on an
     unambiguous single word (e.g. Jacob 2:15 "glance"), which lets
     the errors-log entry name the exact intended word even though
     1920 never marked it. See the `Jacob 2:15`/footnote 812 entry
     added 2026-07-11 for the pattern.
   - **Mislabeled anchor, NOT actually missing**: what looks like one
     missing number is often really a *cascade* — the anchor that
     should carry number N was mistranscribed as N+1, which pushed
     the next real anchor to N+2, and so on, until the last one in
     the chain gets a genuinely duplicated number instead of its own.
     This happened at Mosiah 23:36–39 (`y`→`z`→`2a`, i.e. 1471→1472→
     1473, each transcribed one number too high, with the true 1474
     duplicated at the chapter-24 boundary). A "missing" number
     flanked by a "duplicated" number a few anchors later is the
     signature of this pattern — check it before concluding print
     omission. Diagnosing it reliably requires comparing actual glyph
     shapes, not guessing from context alone: crop the printed,
     labeled footnote-key letters from that same page's footnote
     block (e.g. the "y," "z," "2a," in "y, Véase b... z, Versículo
     38. 2a, Véase u.") as a shape reference, then crop each candidate
     body anchor at matching zoom and compare directly — content-only
     guessing (e.g. "this citation could plausibly attach to this
     word") is not reliable enough on its own to resolve which anchor
     goes where, but it's a decent first-pass hypothesis to narrow
     down which glyphs to compare. Use `ImageOps.invert(img).getbbox()`
     or a column-content scan (pixels darker than a threshold) to find
     precise crop coordinates instead of guessing pixel offsets by eye
     — much faster and more reliable than iterative manual cropping.

After any fix, re-scan the full document (`[re.findall(r'\[(\d+)\]',
body)` against `1..last`) to confirm zero duplicates, zero
out-of-range values, and that only genuine-print-defect numbers
remain missing — this is the way to know the cluster is fully
resolved rather than partially patched.

This check never writes to `permitted words.txt` (not a spelling
matter). Genuine print defects go to `errors in 1920.txt` with no
text change; transcription typos get fixed directly in `librodm.txt`
with no `errors in 1920.txt` entry.

### Scanno check

pptext flags any occurrence of a word from DP's *English* stealth-
scanno list (words like "modem"/"modern" that are common OCR
misreadings — see pgdp.net's `stealth_scannos_eng_common.txt`). This
is an English-language wordlist applied to a Spanish document, so
almost everything it could flag is irrelevant by construction. As of
2026-07-11 the only match in the entire book was the numeral `11`
(verse numbers, chapter headers, cross-references, footnote anchors —
464 legitimate hits, zero real errors), which has been added to
`permitted words.txt` and now suppresses cleanly (confirmed via
rerun: section now reads "no suspected scannos found in text.").
**Going forward:** if a NEW scanno word ever gets flagged (new pages
could coincidentally contain another English word from the list),
spot-check a sample of its hits the same way — confirm they're all
structural/numeric noise before adding to `permitted words.txt`,
since unlike `11` a flagged alphabetic word is somewhat more likely
to coincide with a genuine typo worth a closer look. This check DOES
honor `permitted words.txt` (unlike hyphenation/dash checks) — add
confirmed-benign scanno words there to keep future reports quiet.

### Curly quote check

pptext's curly-quote check only flags *misuse* of curly quotes that
are already present in the text (a curly quote floating alone between
spaces, or pointing the wrong direction for its context) — it does
NOT flag the mere presence of curly quotes, and it says nothing at
all if the document contains none. An empty/clean report from this
check is therefore not proof the document is quote-consistent; it
only proves no *already-curly* quote is obviously misused.

**Project convention (see rule 35 in `libro_de_mormon_rules.md`):**
always type plain straight ASCII quotes (`"` and `'`), never curly
(`“ ” ‘ ’`), during transcription — this matches DP's own
proofreading-stage guidance exactly (confirmed via DPWiki's
Proofreading Guidelines Explanation). Curly quotes are a deliberate
LATER, one-time conversion pass across the whole finished book (DP's
Post-Processing FAQ: curly is preferred in the final .txt AND .html
output, even when the original printed straight quotes) — not
something to hand-type per page.

**Going forward, per Session E run:** since pptext's own check can't
catch a stray curly quote sitting correctly-paired and correctly-
directed (which is exactly what slipped through undetected here), do
an independent scan every run: search both `librodm.txt` and
`librodm_foot.txt` directly for any of `“ ” ‘ ’` (e.g.
`text.count(ch)` for each character in Python, or `grep -n` for each
character) and fix any hit back to straight quotes immediately —
don't wait for pptext to notice, because for this specific problem it
won't. As of 2026-07-11, one instance was found and fixed (footnote
425, "la palabra 'no'", present in both Block 1 and Block 2 — likely
a text editor's autocorrect at transcription time) — it was the only
curly-quote pair in the ~1.15MB document, found only by direct
character search, not by the pptext report. This check never writes
to `permitted words.txt` (not a spelling matter, and the fix is a
direct text correction, not an `errors in 1920.txt` entry, since it's
purely a transcription-formatting slip with no bearing on what the
1920 original actually printed).

### Spaced punctuation check

**Do not confuse this with the "spacing pattern check" section** near the
top of the report (Text Analysis Report), which is a different, unrelated
check that has read 0 hits in every report seen so far. "Spaced
punctuation" is a separate section, much further down the report
(interleaved with the paragraph/book-level checks), that flags any comma,
semicolon, colon, exclamation mark, or question mark preceded by a space.
**This section was missing from the progress tracker below from
2026-07-11 through 2026-07-23** — it was never being walked as its own
section, which is exactly how a real, repeatable defect (a printed or
justification-added space before ";"/"!" ) went unnoticed and even got
misdiagnosed as an intentional "established recent-pages convention" on
pages 496-502 (see rule 31 in `libro_de_mormon_rules.md`, corrected
2026-07-24). Per rule 31, every hit in this section should be fixed by
removing the space — there is no legitimate case where 1920 intentionally
prints a space before one of these marks that should be preserved; this
check never writes to `permitted words.txt` (punctuation, not spelling)
and does not need an `errors in 1920.txt` entry either (it's a
transcription-normalization rule, not a question of what 1920 printed).

**Don't rely on pptext's report alone for this check — run the dedicated
scripts too, every Session E, across the WHOLE document, and fix
whatever they find regardless of whether it falls in the current page's
range** (2026-07-24 instruction, after 91 accumulated instances were
found spanning pages 470-502 plus `librodm_foot.txt`, none caught at the
time they were introduced): `check_spaced_punctuation.py librodm.txt`
(rule 31 — body/Block 2 text) and `check_footnote_punctuation.py
librodm_foot.txt` (rules 22/23 — Block 1 citation text: space before a
comma/semicolon/colon, or a spaced verse-range hyphen). Also run
`check_spaced_punctuation.py` against the current page's own file
(`pages/page_NNN.txt`) — a hit inside that file's Corrections log is
usually a historical quote of an already-fixed reading, not a live
defect, so check context before editing rather than reflexively "fixing"
the quote. Treat any live hit anywhere in the document as an
immediate fix, the same as the mandatory Corrections-log sweep above —
don't scope this to just the page(s) currently being transcribed.

### Verse indentation check

Run `check_verse_indent.py librodm.txt` every Session E, across the whole
document — flags any line where a verse number starting the line has
leading whitespace instead of starting at column 1 (see the
`libro_de_mormon_rules.md` Section 1 note). This defect went undetected
on page 493 for over a month because nothing mechanical checked for it
(only later pages were transcribed correctly going forward — page 493
itself, and `librodm.txt`'s copy of it, were left wrong until it
recurred independently on page 508 and both were finally fixed
2026-07-25). Also run it against the current page's own file
(`pages/page_NNN.txt`); as with the other two checker scripts, a hit
inside that file's Corrections log may be a prose paragraph that
happens to word-wrap onto a line starting with a quoted verse number —
check context before editing. Treat any live hit anywhere in the
document as an immediate fix, not scoped to just the current page(s).

### Special situations checks

A grab-bag of unrelated sub-checks, each a simple regex/inventory over
every line — none of them cross-reference Block 1/Block 2 structure or
scripture-citation format, so several fire constantly on patterns that
are completely normal for this project but rare in general English
prose. As of 2026-07-11, every sub-check that fired came back 100%
clean (verified individually, not waved through by category):
- **`standalone 1`**: fires on any bare "1" not matching pptext's
  (English-oriented) exception list — no exception for our
  colon-based `chapter:verse` citation format (`Mosíah 1:4`) or
  Block 2's `N: text` entry-number format, so this floods with
  legitimate hits. Verify with a quick categorization script (does
  the hit contain `\d+:\d+` or start with `N:`, is it a TOC page
  number, is it the `[1]` footnote anchor, is it `Página 1`) rather
  than reading every line by eye — 125/125 were one of those four
  categories on 2026-07-11, zero exceptions. Same root cause as the
  `11` scanno false-positive (see Scanno check above).
- **`paragraph ends in comma`**: fires when a physical line ends in a
  comma and the very next line is blank. Our page/chapter-break
  convention inserts a blank line before every `Página N`/
  `CAPÍTULO N.`/book-header line, so any verse that happens to wrap
  right at a page or chapter boundary — extremely common, since
  boundaries fall at arbitrary points in the text — trips this. Don't
  read individual hits; instead verify programmatically that line
  `n+1` is blank and line `n+2` is a `Página`/`CAPÍTULO`/all-caps
  header for every reported line number (34/34 confirmed 2026-07-11,
  zero exceptions) — that's sufficient to clear the whole category at
  once.
- **`punctuation error`** (flags `,.`/`.,`/`,,`/bare `..`): check each
  hit individually rather than assuming — it's a small list. As of
  2026-07-11 all 5 were the legitimate `etc.,`/`&c.,` combination
  (abbreviation period immediately followed by a sentence-continuing
  comma), not a real double-punctuation typo.
- **`abbreviation &c without period`**: small enough to always check
  against the page image individually. The one 2026-07-11 hit
  (`&c ;` with no period) turned out to be the 1920 print's own
  inconsistency — the same verse uses `&c.` with a period two
  sentences later. Transcribe exactly what's printed either way; this
  is not something to "fix" for consistency.
- **`ampersand character`**: NOT an error check — pptext's source
  just inventories every line containing `&` (relevant for HTML
  entity-escaping later, irrelevant to our current plain-text
  deliverable). No verification needed, just confirm each hit is a
  normal "&c." abbreviation and move on.
- **`mixed case within word`**: flags rare (used-once) words with an
  internal capital. Requires an image check per hit, since this is
  exactly the kind of check that can hide a real proper-noun typo
  among legitimate ones — don't wave the category through. Both
  2026-07-11 hits (`Ani-Anti`, a genuine Book of Mormon place name;
  `Anti-Nefi-Lehías`, confirmed against the page image as a real
  spelling variant used only at that one verse) checked out.
  **This is the one special-situations sub-check that honors
  `permitted words.txt`** (source explicitly checks
  `!inGoodWordList(word)`) — confirmed-correct hits go there, same as
  any other reviewed word.
- **`mixed letters and numbers in word`**: pptext's ordinal exception
  list only covers English forms (`1st`, `2nd`, `3rd`...). Spanish
  ordinal abbreviations (`3ra.`, `4to.`, etc.) will always false-
  positive here; confirm the word is a genuine Spanish ordinal
  abbreviation and move on, no image check needed for something this
  unambiguous.

None of these (except `mixed case within word`) write to `permitted
words.txt` — they're pure regex/structural scans with no word-list
consultation, so they'll keep re-flagging the same false positives on
every future run regardless. That's expected; re-verify quickly using
the category-specific shortcuts above rather than re-deriving them
from scratch each time.

## pptext report walkthrough progress tracker

Track section-by-section progress here across sessions so a fresh
session knows where to resume without re-reading the whole report.
Update this list as each section is completed. Sections, in report
order (see `workspace/report_wsl_*.html`):

**Covered** (as of the 2026-07-11 report):
- Smart Quote Scan
- Spellcheck Suspect Words
- Edit Distance Checks
- Text Analysis Report: hyphenation/non-hyphenated check
- Text Analysis Report: hyphenation and spaced-pair check
- Text Analysis Report: asterisk check
- Text Analysis Report: adjacent spaces check
- Text Analysis Report: trailing spaces check
- Text Analysis Report: character checks
- Text Analysis Report: spacing pattern check
- Text Analysis Report: main text headers check (confirmed 2026-07-12 —
  produces zero output in every report seen so far, no count/findings
  line at all between its header and the next section; same "not
  applicable to our format" pattern as book level checks, likely
  because pptext's heading heuristic expects a different chapter-
  marker convention than our `CAPÍTULO N.` style. Not previously
  tracked in this list even though it was always present in the
  report — re-confirm it stays empty on future full-book runs rather
  than assuming it always will.)
- Text Analysis Report: short lines check
- Text Analysis Report: long lines check
- Text Analysis Report: repeated word check
- Text Analysis Report: duplicate lines check
- Text Analysis Report: ellipsis check
- Text Analysis Report: dash check
- Footnote check
- Scanno check
- Curly quote check
- Spaced punctuation check (added to this tracker 2026-07-24 — was
  present in every report all along but never listed here, which is why
  it went unwalked; see the dedicated subsection above)
- Special situations checks
- Book level checks (as of 2026-07-12 report — all zero, clean)
- Paragraph level checks (as of 2026-07-12 report — see note below)
- Jeebies Report (as of 2026-07-12 report — "jeebies found no errors")

Note: this progress tracker reflects specific report runs
(`report_wsl_20260711.html`, `report_wsl_20260712.html`). A
regenerated report changes line numbers but not section order/names —
re-locate sections by name when parsing (note the two anchor styles:
`<span class='black'>-----` for most Text Analysis subsections, but
`<span class='(black|dim)'>-----` more generally, since a section with
zero findings renders `dim` instead of `black` — filtering on `black`
only will silently skip clean sections). Once the full report has been
walked end to end, treat this tracker as satisfied for that pass; a
later full-book pptext run (per the blanket-suppression mitigation
above) should get a fresh walkthrough since new content and the
emptied `permitted words.txt` can surface new findings even in
previously-clean sections.

**Efficient re-walkthrough technique** (used 2026-07-12): when only a
known page range is new since the last full walkthrough, it's not
necessary to re-read every section's full contents — instead extract
every `NNNNN: text` line-number citation from the whole report (across
all sections) and filter to just the line-number ranges covering the
new pages' body text and Block 2 notes in `librodm.txt` (find via
`grep -n "^Página NNN$"` and the first/last new footnote numbers). This
surfaces exactly what's new without re-vetting already-reviewed
content. Sections with no per-line citations (paragraph-level checks'
"paragraph starts with upper-case word" and "query: unexpected
paragraph end", which quote text without line numbers) need a manual
`grep` of the quoted snippet against `librodm.txt` to locate them
instead.

**Paragraph level checks — structural notes (2026-07-12, first
walkthrough of this section ever):**
- **"paragraph starts with upper-case word"** and **"query: unexpected
  paragraph end"**: structural false-positive categories for this
  project, same root cause as the short/long lines checks — pptext's
  paragraph-boundary heuristics assume DP's one-paragraph-per-line
  convention, but this project wraps each verse at ~72 chars across
  multiple lines (rule in `libro_de_mormon_rules.md`) rather than
  reflowing to one line per paragraph. Every entry seen is a TOC
  line, a `CAPÍTULO N.` heading, or an ordinary verse/page boundary —
  not a real signal. Don't work through these line by line; a spot
  check confirming the pattern is enough.
- **"full stop followed by unexpected sequence"** (period followed by
  a lowercase word): this check DOES catch real signal, and matching
  the 1920 page image is **not sufficient** to clear a hit — that only
  confirms our transcription is accurate, it says nothing about
  whether the period is a 1920-original error. A first pass on
  2026-07-12 checked all 6 then-known hits (5 pre-existing + 1 in
  pages 441-448) against the 1920 image only and wrongly concluded
  they were a shared, harmless printer idiosyncrasy; a follow-up
  1886-comparison the same day found **all 6 are actually 1920-only
  deviations** — 1886 has a plain comma at every one of these
  locations (Alma 43:9, 48:6, 49:3, 52:34, 57:6, Helamán 5:2), while
  1920 alone prints a period + lowercase continuation. All 6 are now
  logged in `errors in 1920.txt`. **Mandatory per hit, going
  forward:** check the 1886 image at the exact spot — don't stop at
  confirming the 1920 transcription is accurate. If 1886 has a comma
  (or otherwise doesn't reproduce the period), log it in `errors in
  1920.txt`; only treat it as house style if 1886 *also* prints a
  period there (no instance of that has been found yet, but don't
  assume it can't occur). This is a punctuation-placement question, so
  no RAE/corpus research is needed — just the 1886 comparison.
