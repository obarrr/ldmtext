#!/usr/bin/env python3
"""
Session D: generate Block 2 (sequential-number footnotes) from Block 1
(chapter+letter footnotes in librodm_foot.txt) and append to librodm.txt.

Two modes:

1. Incremental (normal use, one or more already-integrated pages):
     python generate_block2.py 441 442 443 444 445 446
   For each page, pulls its Block 1 entries (by footnote-number range,
   read from the page file) from librodm_foot.txt, resolves any "Véase
   <letter(s)>[, <Book> <Chapter>]" cross-reference clauses to bare
   sequential numbers, and appends the resulting Block 2 entries to the
   end of librodm.txt. A cross-reference that can't be resolved against
   the CURRENT contents of librodm_foot.txt is left in its original
   letter form, unchanged -- this matches existing historical entries
   in librodm.txt (e.g. "Véase p, II Nefi 15." was never resolved
   because II Nefi hadn't been transcribed yet when that entry was
   originally generated).

2. Fix-unresolved (run once the full text is finished, or any time you
   want to sweep for newly-resolvable cross-references):
     python generate_block2.py --fix-unresolved
   Rescans every existing Block 2 entry already in librodm.txt's Notas
   section and re-attempts resolution for any that still contain a
   letter-form "Véase ..." clause. Rewrites librodm.txt in place with
   whatever now resolves; anything still unresolved is left as-is.

Cross-reference resolution is book-aware: chapter+letter identifiers
like "29c" are not unique across the whole document (multiple books
have a chapter 29), so resolution always happens within the book
section the reference names (or, for a bare "Véase <letter>." with no
book given, within the citing entry's own book+chapter).
"""
import io
import re
import sys
import unicodedata

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PAGES_DIR = "pages"
MASTER = "librodm.txt"
FOOT_MASTER = "librodm_foot.txt"

FN_LINE = re.compile(r'^(\S+),\s+(\d+):\s*(.*)$')
VEASE_CLAUSE = re.compile(r'Véase ([^.]+)\.')
STOPWORDS = {"LIBRO", "DE", "EL", "LOS", "LAS"}
ROMAN_PREFIX = [
    (re.compile(r'^IV\b'), "CUARTO"),
    (re.compile(r'^III\b'), "TERCER"),
    (re.compile(r'^II\b'), "SEGUNDO"),
    (re.compile(r'^I\b'), "PRIMER"),
]


def strip_accents(s):
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c))


def book_tokens(text):
    text = strip_accents(text).upper().strip()
    for pat, repl in ROMAN_PREFIX:
        text = pat.sub(repl, text, count=1)
    tokens = [t for t in re.split(r'\s+', text) if t and t not in STOPWORDS]
    return frozenset(tokens)


def parse_ident(ident):
    if "-" in ident:
        chap_str, code = ident.split("-", 1)
        return int(chap_str), code
    m = re.match(r'^(\d+)([a-zA-Z]+)$', ident)
    if not m:
        raise ValueError(f"cannot parse identifier: {ident!r}")
    return int(m.group(1)), m.group(2)


def is_header_line(s):
    letters = [c for c in s if c.isalpha()]
    return bool(letters) and all(c.isupper() for c in letters)


class FootIndex:
    """Book-aware index over librodm_foot.txt."""

    def __init__(self, path):
        with open(path, encoding="utf-8") as f:
            lines = [l.rstrip("\n") for l in f]

        self.by_book_chapter_code = {}   # (book_id, chapter, code) -> seqnum
        self.entry_context = {}          # seqnum -> (book_id, chapter)
        self.book_section_tokens = []    # [(book_id, tokenset, header_text)]
        self.entries_in_order = []       # [[seqnum, book_id, chapter, code, text], ...]

        book_id = -1
        last_entry = None
        for line in lines:
            s = line.strip()
            if not s:
                continue
            m = FN_LINE.match(line)
            if m:
                ident, seqnum, text = m.group(1), int(m.group(2)), m.group(3)
                chapter, code = parse_ident(ident)
                self.by_book_chapter_code[(book_id, chapter, code)] = seqnum
                self.entry_context[seqnum] = (book_id, chapter)
                entry = [seqnum, book_id, chapter, code, text]
                self.entries_in_order.append(entry)
                last_entry = entry
            elif is_header_line(s):
                book_id += 1
                self.book_section_tokens.append((book_id, book_tokens(s), s))
                last_entry = None
            elif last_entry is not None:
                # wrapped continuation line of the previous entry's reference text
                last_entry[4] += " " + s

    def find_book_id(self, book_text):
        target = book_tokens(book_text)
        for book_id, tokens, _header in self.book_section_tokens:
            if tokens == target:
                return book_id
        for book_id, tokens, _header in self.book_section_tokens:
            if target <= tokens or tokens <= target:
                return book_id
        return None

    def resolve(self, code, book_text, chapter, citing_book_id, citing_chapter):
        if book_text is not None:
            book_id = self.find_book_id(book_text)
            if book_id is None:
                return None
        else:
            book_id = citing_book_id
            chapter = citing_chapter
        return self.by_book_chapter_code.get((book_id, chapter, code))


LETTER_CODE = re.compile(r'^\d*[a-z]$')


def parse_letters(letters_expr):
    """Split a letters clause like "b, y, c" / "e, y g" / "g y j" / "p y q"
    / bare "y" into individual letter/code tokens. The word "y" ("and") is
    always a separator except when it is the ENTIRE clause (a literal
    reference to the footnote letter "y" itself, e.g. "Vease y.") -- real
    print copy uses every combination of comma and "y" inconsistently
    around the separator, so normalize by treating every standalone "y"
    as a comma before splitting, rather than assuming a fixed comma/"y"
    placement."""
    letters_expr = letters_expr.strip()
    if letters_expr == "y":
        return ["y"]
    normalized = re.sub(r'\by\b', ',', letters_expr)
    return [t.strip() for t in normalized.split(",") if t.strip()]


def resolve_text(text, citing_book_id, citing_chapter, index):
    def repl(m):
        inner = m.group(1)
        letters_expr, book_text, chapter = inner, None, None

        if "," in inner:
            # The letters clause and the book/chapter clause are always
            # separated by the LAST comma in the whole span (book names
            # never contain a comma) -- try that boundary first, and only
            # commit to it if the tail actually looks like "Book Chapter".
            # If it doesn't, there is no book/chapter present at all
            # (e.g. "f, y g.") and the commas belong to the letters list.
            candidate_letters, candidate_tail = inner.rsplit(",", 1)
            bcm = re.match(r'^(.*\S)\s+(\d+)(?::[\d,\s-]+)?$', candidate_tail.strip())
            if bcm:
                book_text, chapter = bcm.group(1), int(bcm.group(2))
                letters_expr = candidate_letters

        tokens = parse_letters(letters_expr)
        if not tokens or any(not LETTER_CODE.match(t) for t in tokens):
            return m.group(0)  # not a plain letter-code list, leave untouched

        resolved = []
        for tok in tokens:
            n = index.resolve(tok, book_text, chapter, citing_book_id, citing_chapter)
            if n is None:
                return m.group(0)  # any failure -> leave whole clause untouched
            resolved.append(str(n))
        return "Véase " + " y ".join(resolved) + "."

    return VEASE_CLAUSE.sub(repl, text)


def wrap_entry(seqnum, text, width=72):
    """Wrap a Block 2 entry at width, preferring to break at a semicolon
    between whole references (e.g. "...14:12; Alma 38:37...") rather than
    splitting a single reference apart (e.g. never "...Alma" / "38:37...").
    Falls back to word-level wrapping only for a segment that's too long
    to fit on a line by itself (or entries with no semicolons at all)."""
    segments = re.split(r'(?<=;)\s+', text)
    lines = []
    cur = f"{seqnum}: "
    is_first = True
    for seg in segments:
        candidate = cur if is_first else cur + " "
        candidate += seg
        if is_first or len(candidate) <= width:
            cur = candidate
            is_first = False
        else:
            lines.append(cur)
            cur = seg
    lines.append(cur)

    final = []
    for line in lines:
        if len(line) <= width:
            final.append(line)
            continue
        words = line.split(" ")
        c = ""
        for w in words:
            cand = (c + " " + w) if c else w
            if not c or len(cand) <= width:
                c = cand
            else:
                final.append(c)
                c = w
        if c:
            final.append(c)
    return final


def load_page_seqnums(page_num):
    path = f"{PAGES_DIR}/page_{page_num}.txt"
    with open(path, encoding="utf-8") as f:
        lines = [l.rstrip("\n") for l in f]
    seqnums = []
    for l in lines:
        m = FN_LINE.match(l)
        if m:
            seqnums.append(int(m.group(2)))
    return seqnums


def find_notas_index(lines):
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].strip() == "Notas":
            return i
    raise ValueError("Notas line not found in librodm.txt")


def last_book_id_in_master(lines, notas_idx, index):
    """Scan librodm.txt's existing Block 2 section to find which book
    section (by index.find_book_id) the last entry currently belongs to."""
    book_id = None
    for line in lines[notas_idx + 1:]:
        s = line.strip()
        if not s:
            continue
        if re.match(r'^\d+:', line):
            continue
        found = index.find_book_id(s)
        if found is not None:
            book_id = found
    return book_id


def incremental(page_nums):
    index = FootIndex(FOOT_MASTER)
    src_text_by_seqnum = {s: t for s, b, c, cd, t in index.entries_in_order}

    with open(MASTER, encoding="utf-8") as f:
        lines = [l.rstrip("\n") for l in f]
    notas_idx = find_notas_index(lines)

    last_book_id = last_book_id_in_master(lines, notas_idx, index)

    new_lines = []
    unresolved_report = []
    for num in page_nums:
        for seqnum in load_page_seqnums(num):
            book_id, chapter = index.entry_context[seqnum]

            if last_book_id is not None and book_id != last_book_id:
                header = index.book_section_tokens[book_id][2]
                new_lines.append("")
                new_lines.append(header)
                new_lines.append("")
            last_book_id = book_id

            resolved = resolve_text(src_text_by_seqnum[seqnum], book_id, chapter, index)
            new_lines.extend(wrap_entry(seqnum, resolved))
            if re.search(r'Véase [^.]*[a-zA-Z]', resolved):
                unresolved_report.append((seqnum, resolved))

    with open(MASTER, "a", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(new_lines) + "\n")

    print(f"Appended {sum(1 for l in new_lines if re.match(r'^\d+:', l))} "
          f"Block 2 entries to {MASTER}.")
    if unresolved_report:
        print(f"{len(unresolved_report)} entries still have an unresolved "
              f"cross-reference (left in letter form):")
        for seqnum, text in unresolved_report:
            print(f"  {seqnum}: {text}")


def fix_unresolved():
    index = FootIndex(FOOT_MASTER)

    with open(MASTER, encoding="utf-8") as f:
        lines = [l.rstrip("\n") for l in f]

    notas_idx = find_notas_index(lines)
    changed = 0
    for i in range(notas_idx + 1, len(lines)):
        line = lines[i]
        s = line.strip()
        if not s:
            continue
        m = re.match(r'^(\d+):\s*(.*)$', line)
        if not m:
            # header line or wrapped continuation of the previous entry --
            # either way, the citing entry's own book/chapter (below) comes
            # straight from librodm_foot.txt's index, so no book_id needs
            # to be tracked by scanning librodm.txt's own header lines here.
            continue
        seqnum, text = int(m.group(1)), m.group(2)
        if seqnum not in index.entry_context:
            continue
        book_id, chapter = index.entry_context[seqnum]
        new_text = resolve_text(text, book_id, chapter, index)
        if new_text != text:
            lines[i] = f"{seqnum}: {new_text}"
            changed += 1

    with open(MASTER, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Re-resolved {changed} previously-unresolved Block 2 entries.")


def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python generate_block2.py NNN [NNN ...]")
        print("       python generate_block2.py --fix-unresolved")
        sys.exit(1)

    if args[0] == "--fix-unresolved":
        fix_unresolved()
    else:
        incremental(args)


if __name__ == "__main__":
    main()
