---
name: send-chapter
description: Session F of the Libro de Mormón 1920 transcription workflow — extracts one finished chapter from librodm.txt into chapters_emailed/<Book>_<N>.txt and emails it to the family recipients. Use when the user asks "what's the next chapter to send," "send chapter Book NN," or "send the next chapter."
---

# Session F — Email a finished chapter

Two separate triggers, both backed by `send_chapter.py`:

- **Query only**: "What's the next chapter to send?" →
  `py send_chapter.py --next` (no other flags). Reports the next
  book+chapter without extracting or sending anything. Relay the
  printed answer to the user; take no further action unless they then
  ask to send it.
- **Send**: "Send chapter <Book> <N>" or "Send the next chapter" →
  `py send_chapter.py <Book> <N>` (explicit) or
  `py send_chapter.py --next --send` (derives book+chapter from the
  log automatically). Both extract the chapter, write it to
  `chapters_emailed/`, email it, and log it — no confirmation step,
  since the user has chosen automatic sending (see below).

`<Book>` must match `chapter_map.csv`'s `book` column exactly, e.g.
`"1 Nephi"` `"2 Nephi"` `Jacob` `Enos` `Jarom` `Omni`
`"Words of Mormon"` `Mosiah` `Alma` `Helaman` `"3 Nephi"` `"4 Nephi"`
`Mormon` `Ether` `Moroni` (quote multi-word keys on the command line).

## What the script does

1. **Extracts** the chapter from `librodm.txt`: locates the `CAPÍTULO
   N.` heading within the correct book's body section (bounded by the
   next book header or the next chapter heading, whichever comes
   first), and copies everything in between verbatim — including any
   `Página NNN` markers that fall inside it.
2. **Pulls matching footnotes**: scans the chapter text for every
   `[NNNN]` citation, then extracts the corresponding `NNNN: text`
   entries (including multi-line wrapped entries) from the Notas/Block
   2 section at the end of `librodm.txt`.
3. **Writes** `chapters_emailed/<Book>_<N>.txt` — chapter text, blank
   line, footnote entries, in that order (matches the source document's
   own formatting exactly, since it's a straight extraction).
4. **Emails** it via direct SMTP (not Outlook — this machine only has
   the new Microsoft Store "Outlook for Windows," which does not
   expose the classic `Outlook.Application` COM automation interface;
   confirmed 2026-07-12, no classic desktop Outlook installed at all).
   Sends through `mail.theobarrs.com:465` (SSL), authenticated as
   `robert@theobarrs.com` using a password stored in Windows Credential
   Manager via the `keyring` package (service name
   `libro_de_mormon_smtp`) — entered once via
   `setup_email_credentials.py`, never re-typed, never stored in any
   project file. Recipients default to `claudia@theobarrs.com` and
   `obarrr@yahoo.com` (**not** `robert@theobarrs.com` — that address is
   only the sending/login account, a mix-up caught and fixed
   2026-07-12).
5. **Subject line**: `{Book display name} Capítulo {N}`, e.g. "Alma
   Capítulo 63", "Helamán Capítulo 1". Book display names use full
   modern Spanish accentuation regardless of how the document's own
   (inconsistent) all-caps headers print them — see `BOOK_ORDER` in
   `send_chapter.py` for the exact mapping (e.g. "Helamán" even though
   the in-document chapter-body header prints unaccented "HELAMAN").
6. **Logs** the send to `chapters_emailed/_log.txt` (`Book|Chapter|
   Date|note`, one line per chapter, append-only) — this is what
   `--next` reads to compute the next book/chapter, rolling over to the
   next book via `chapter_map.csv`'s max-chapter-per-book once the
   current book is exhausted.

## One-time setup (already done as of 2026-07-12, documented for a future machine)

```
py -m pip install pywin32 keyring
py setup_email_credentials.py
```
The credential prompt is a hidden `getpass` input — never echoed,
logged, or written to disk. `py setup_email_credentials.py --check`
confirms a credential is stored (prints only True/False, never the
password). `--remove` deletes it.

## Flags

- `--no-send`: extract and write the `.txt` file, but don't email or
  log — use this to sanity-check a chapter's extraction before sending
  for real, especially the first time through a new book (header regex
  patterns for books after Helaman haven't been exercised yet since
  transcription hasn't reached them).
- `--no-log`: send without appending to `_log.txt` — for one-off
  resends (e.g. fixing a wrong-recipient mistake) that shouldn't shift
  what `--next` reports.
- `--to=email1,email2`: override the default recipient list for one
  run — for one-off resends to a subset of the usual recipients.

## Known issue

Recipient inboxes may file these emails as spam (confirmed for
`obarrr@yahoo.com`, 2026-07-12 — delivered, but landed in the Spam
folder; `claudia@theobarrs.com`'s receipt unconfirmed as of that date).
Not yet addressed — if this keeps happening, consider adding SPF/DKIM
alignment checks on `mail.theobarrs.com`, or simply have recipients
whitelist the sending address.

## Verifying book-name/chapter extraction for a new book

The `BOOK_ORDER` header-regex table in `send_chapter.py` has only been
exercised end-to-end for Helamán so far. Before relying on `--next` to
carry a "send the next chapter" request across a book boundary (e.g.
Helamán 16 → III Nefi 1) for the first time, run with `--no-send` first
and eyeball the output — a body-header regex that doesn't match the
actual printed text (accented vs. unaccented, trailing period vs. not)
will raise `RuntimeError` rather than silently producing wrong output,
but it's still worth a visual check the first time through each book.

Output: `chapters_emailed/<Book>_<N>.txt` written; email sent (unless
`--no-send`); `chapters_emailed/_log.txt` updated (unless `--no-log`).
