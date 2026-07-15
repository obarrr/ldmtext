# Environment Setup — Libro de Mormón 1920 Project

For setting up this project's tooling on a new Windows machine. Covers
two independent pieces: the Windows-native Python toolchain used for
Sessions A, B, C, E (image-based transcription), and WSL/pptext used for
Session D (orthography spellcheck).

**Status:** Part 1 reflects the actual imports/hardcoded paths found in
the scripts already in this project as of 2026-07-10 but has not been
re-run start-to-finish on a clean machine. **Part 2 (WSL + pptext) has
been validated end-to-end on this machine (2026-07-11)** — built
successfully and confirmed working against a real test file (correctly
flagged missing accents and a nonsense word under `-a es`).

---

## Part 1 — Windows-native tools (Sessions A, B, C, E)

1. **Python 3** (provides the `py` launcher used by every script):
   `winget install Python.Python.3.13` (or the python.org installer —
   either way, must register the `py` launcher).
   Confirm: `py --version`

2. **Python packages**, confirmed as the actual imports used across
   every `.py` file at the project root (all other imports are standard
   library — no install needed):
   ```
   py -m pip install Pillow pytesseract pdfplumber
   ```
   - **Pillow** (`PIL.Image`) — image cropping, used by nearly every
     script (`process_page.py`, `crop_page.py`, `build_chapter_map.py`,
     `verify_fn.py`, `audit_spot_check.py`, `ocr_diag.py`, `ocr_page.py`).
   - **pytesseract** — Python wrapper around the Tesseract OCR engine
     (see item 4 below — the wrapper alone does nothing without it).
   - **pdfplumber** — PDF text extraction, used by `draft_page.py` for
     the "Google OCR conflict list" pass.

3. **Poppler** (provides `pdftoppm`, used by `split_pdfs.py` to do the
   one-time rasterization of all three source PDFs into
   `pages_1920\`/`pages_1879\`/`pages_1886\` at 400dpi). **Not required
   for routine Session A/B/C/E work** — `process_page.py` is always
   called against those pre-rasterized PNGs day to day, and that path
   never touches Poppler. Only install this if `split_pdfs.py` needs to
   be (re-)run (new source PDF, missing pages) or a specific page needs
   re-rasterizing above 400dpi (the source scans' native resolution is
   ~600dpi, confirmed by inspecting the embedded JBIG2 image dimensions
   via `pdfplumber` — worth doing as a targeted fallback if a superscript
   stays ambiguous even after the normal 400dpi + zoom crop):
   `winget install oschwartz10612.Poppler`
   `process_page.py` and `split_pdfs.py` both have this hardcoded
   fallback path (falls back to plain `pdftoppm` on `PATH` if not found
   there):
   ```
   C:\Users\<you>\AppData\Local\Microsoft\WinGet\Packages\
   oschwartz10612.Poppler_Microsoft.Winget.Source_8wekyb3d8bbwe\
   poppler-25.07.0\Library\bin\pdftoppm.exe
   ```
   This path is per-user (embeds the Windows account name), so it will
   never resolve on a machine where the project is accessed under a
   different Windows username than the one Poppler was installed under
   — confirmed 2026-07-13 on ROBERT-LAPTOP (account `rober`), where the
   hardcoded path still points at a `Robert O'Barr` account that doesn't
   exist on that machine, and Poppler was never installed there at all
   since the pre-rasterized PNGs made it unnecessary. If a future winget
   install lands at a different version/path, either update
   `PDFTOPPM_PATH` in both scripts or just ensure `pdftoppm.exe` is
   reachable via `PATH`.

4. **Tesseract OCR engine** (native binary — `pytesseract` is only a
   wrapper around it): install via the UB-Mannheim Windows build
   (https://github.com/UB-Mannheim/tesseract/wiki). **During install,
   add the Spanish language pack** in addition to the default English —
   the project OCRs both the 1920/1886 Spanish pages (`lang='spa'`) and
   the 1879 English pages (`lang='eng'`, used in `verify_fn.py` for
   cross-checking footnote superscripts).
   Scripts hardcode this path (`draft_page.py`, `build_chapter_map.py`):
   ```
   C:\Program Files\Tesseract-OCR\tesseract.exe
   ```
   Update those two lines if installed elsewhere.

5. **Git** — used for version control of the project folder generally;
   confirm with `git --version` (Git Bash also provides the Bash-tool
   shell used in Claude Code sessions on this project).

6. **Not yet built**: `libro_de_mormon_rules.md` and `CLAUDE.md`
   reference a `python spellcheck_page.py page_NNN.txt` pre-pass script
   that does not exist yet in the project. When it's written, it will
   likely need `pip install pyspellchecker` plus a Spanish word list —
   update this doc once that script exists.

---

## Part 2 — WSL + pptext (Session D)

Chosen over a native-Windows build specifically to match the pgdp.net
web tool's own environment (confirmed via its Dockerfile: Debian +
`apt install aspell aspell-es golang`), avoiding both a source patch
(native Windows needs one — see note at the end) and any Spanish
aspell-dictionary version drift between package ecosystems.

1. **Enable WSL** (one-time; requires admin elevation and likely a
   reboot on first setup):
   ```
   wsl --install
   ```
   Defaults to Ubuntu. This step **must be run from an elevated
   (Administrator) PowerShell/terminal** — a non-elevated `wsl --install`
   just prints the "not installed, run wsl --install" message in a loop
   without doing anything.
   **Gotcha encountered:** even after `wsl --install` completed and
   asked for a reboot, `wsl --status` afterward reported "WSL2 is unable
   to start since virtualization is not enabled on this machine" — the
   Windows-side feature was on, but hardware virtualization (Intel VT-x)
   was OFF in the laptop's BIOS/UEFI firmware (common Lenovo default).
   Fix: reboot into firmware settings (Windows 11: Shift+click Restart →
   Troubleshoot → Advanced options → UEFI Firmware Settings), enable
   "Intel (R) Virtualization Technology" (under Security/Configuration,
   varies by BIOS), save and exit. This is a manual, hands-on-keyboard
   step — nothing to automate here.
   **Second gotcha:** `wsl --install` alone enabled the feature but did
   NOT install a distro ("no installed distributions"). Install one
   explicitly:
   ```
   wsl --install Ubuntu
   ```
   Confirm afterward with `wsl --list --verbose`.
   **Third gotcha:** if the terminal's current working directory is a
   mapped network drive (like this project's `Z:`), `wsl` commands fail
   with `wsl: Failed to translate '<path>'` — WSL can't translate a
   mapped drive letter into a Linux path for the initial working
   directory. Work around it by passing `--cd ~` (or running from a
   local `C:\` path) on every `wsl` invocation, e.g.
   `wsl -d Ubuntu --cd ~ -- <command>`.
   **First launch** of the new distro needs an interactive
   username/password prompt (`Enter new UNIX username:` /
   `New password:`) — this has to happen in your own terminal window,
   not through an automated command (it hangs forever waiting on stdin
   otherwise). Same applies to every `sudo` call below the first time
   — `sudo -n true` fails with "interactive authentication is required"
   until you've typed the password once in that session.

2. **Inside the Ubuntu shell**, install build and runtime dependencies:
   ```
   sudo apt update
   sudo apt install -y golang aspell aspell-es aspell-en file git
   ```
   **Gotcha: `aspell-en` is required even for a Spanish-only project.**
   pptext has an internal word-qualification step (`asqual()`, called
   from three places in `pptext.go`) that runs `aspell` with no
   `--lang` argument at all, letting aspell fall back to its system
   default — which resolves to `en_US` regardless of the `-a` flag you
   pass on the command line. Without `aspell-en` installed, every run
   fails immediately with `Error: No word lists can be found for the
   language "en_US"`. This is presumably why pgdp.net's own Dockerfile
   installs a long list of aspell dictionaries (en, da, nl, fr, de, it,
   pt, es, ...) regardless of which languages a given book needs.

3. **Clone and build pptext** (no source patching needed on WSL — the
   hardcoded `/usr/bin/aspell` and `/usr/bin/file` paths the source
   uses are valid there, unlike on native Windows):
   ```
   git clone https://github.com/DistributedProofreaders/pptext.git ~/pptext
   cd ~/pptext
   go build pptext.go
   ```
   `scannos.txt` and `hebelist.txt` ship inside the repo already, next
   to `pptext.go` — no separate download needed. The binary finds them
   automatically via its own executable path at runtime.
   **Validated 2026-07-11**: build succeeded on the first try, no source
   changes needed.

4. **Running it against project files**: the project lives on a mapped
   network drive (`Z:`), which WSL cannot see directly. Stage the two
   small input files to a local Windows path first (WSL auto-mounts
   real local drives at `/mnt/c/...`), run pptext there, then copy the
   report back:
   ```bash
   # from WSL, after copying librodm.txt and "permitted words.txt"
   # to e.g. C:\Users\<you>\AppData\Local\Temp\pptext_run\
   ~/pptext/pptext \
     -i "/mnt/c/Users/<you>/AppData/Local/Temp/pptext_run/librodm.txt" \
     -g "/mnt/c/Users/<you>/AppData/Local/Temp/pptext_run/permitted words.txt" \
     -a es -v \
     -o "/mnt/c/Users/<you>/AppData/Local/Temp/pptext_run"
   ```
   Default flags to match the web form's "run all tests, Spanish only,
   verbose" state: omit `-t` entirely (its default value already means
   "run every test category"), `-a es` (Spanish only — confirmed correct
   for this Spanish-only project, not a mistake), `-v`.
   **Validated 2026-07-11** against a small test file containing
   "espanol", "aqui", and a nonsense word — `report.html` correctly
   flagged all three under "SPELLCHECK SUSPECT WORDS (es)".

5. **Full-project validation, 2026-07-11**: ran against the real
   `librodm.txt` (1.15MB) + `permitted words.txt` (~30s) and diffed the
   report byte-for-byte against a same-day web-interface run. Findings
   matched completely (same 2 spellcheck suspects, same long-lines
   entries). Two harmless difference sources to expect and ignore:
   - **Header metadata** (timestamp, version string, good-words
     filename) — cosmetic only. Our build shows a blank version string
     since we skip the Makefile's `-ldflags` git-hash/build-time
     embedding; the web server's build showed a Feb 2026 commit hash,
     confirming it isn't necessarily bleeding-edge master.
   - **Order within the "long lines check" section, among lines tied at
     the same character count**: `tcLongLines()` in `pptext.go` sorts
     with `sort.Slice` (explicitly documented as NOT stable) and no
     secondary tiebreaker, so tied-length entries can come out in a
     different relative order between builds (confirmed by checking
     source — every entry's line number/length/text matched exactly
     between the two reports, only the ordering among ties differed).
     This is an upstream code quirk, not a real discrepancy — no action
     needed.

### If native Windows is ever preferred instead of WSL

Not the current plan, but documented in case convenience later outweighs
the validation benefit of matching pgdp.net's exact environment: the
same repo needs a 2-line patch (`/usr/bin/aspell` → `aspell`,
`/usr/bin/file` → `file`, both in `pptext.go`, so Go's `exec.Command`
resolves them via `PATH`), plus Go (`winget install GoLang.Go`) and
MSYS2 (providing `aspell.exe`/`aspell-es`/`file.exe` on `PATH`) installed
natively. Audited the full ~4,450-line source — these two lines are the
*only* non-portable code in the file, so the patch is a safe, one-time,
well-isolated change if this route is ever taken.

---

## Notes on portability to a future machine

- Everything in Part 1 is a normal per-user or admin-level Windows
  install (`winget`, `pip`) — no reboot required.
- Part 2's `wsl --install` step is the only piece needing admin
  elevation and a likely reboot. On a laptop where virtualization is
  off by default in firmware (seen on this Lenovo), budget for an extra
  BIOS-settings reboot beyond the WSL-feature reboot — check
  `wsl --status` after the first reboot; if it complains about
  virtualization rather than about missing distributions, that's the
  firmware setting, not a WSL problem.
- Don't forget `aspell-en` alongside `aspell-es` even though this
  project only ever passes `-a es` — pptext needs it internally
  regardless (see gotcha above). Skipping it produces a confusing error
  that looks like a language-flag problem but isn't.
- All hardcoded paths called out above (Poppler, Tesseract) are
  winget/installer defaults — a fresh machine should reproduce them
  as-is unless a package version bump changes the folder name (Poppler
  embeds its version number in the install path).
