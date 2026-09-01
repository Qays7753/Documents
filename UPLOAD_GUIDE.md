# Upload Guide

Binding rules and procedure for adding deliverables to this repository. This guide governs every upload, current and future.

## 1. Access and token security (binding rules)

1. Access to this repository is granted by a **fine-grained GitHub access token** provided by the repository owner **through a secure channel, separately from any prompt or document**.
2. The token is used **only** for this repository (`https://github.com/Qays7753/Documents.git`) and **only** for uploading the requested deliverables. It is never used for any other repository, purpose, or operation.
3. The token must **never** appear:
   - in any prompt or instruction text,
   - in any file (including scripts, logs, worklogs, reports, and this repository's contents),
   - in any commit message,
   - in any log or command output,
   - in any URL — including git remote URLs.
4. The token is used **transiently**: it is supplied to `git` as a process-environment credential (`GH_DOCS_TOKEN`) consumed by an in-memory credential helper for the duration of one authenticated operation. It is never written to disk, never saved to `.git/config`, never stored in a credential file or credential store, and never cached.
5. If the token is revoked, expires, or is unavailable, uploads stop and the exact reason is reported. Uploads never fall back to embedding credentials anywhere.
6. The reference procedure lives in the assistant workspace as `scripts/push-documents-repo.sh`; it reads `GH_DOCS_TOKEN` from the environment and persists nothing.

## 2. Where files go

| Situation | Action |
|---|---|
| New deliverable | Add the file under `reports/` |
| Updated deliverable | Old file moves to `archive/` with a date prefix (e.g. `2026-09-01_Micro-Target-State-Design-Report.md`); new file takes the stable name in `reports/` |
| Every upload | Update `INDEX.md` in the same commit (new row + archive log entry if applicable) |

## 3. Naming convention

Stable names, no dates in current filenames (dates live in `INDEX.md` and archive prefixes):

```
<Project>-<Deliverable>[-<Language>].<ext>
Micro-Target-State-Design-Report.md          English canonical, Markdown
Micro-Target-State-Design-AR.docx            Arabic, Word (.docx), RTL
Micro-Target-State-Design-AR-preview.pdf     read-only preview of the Arabic document
```

## 4. Upload procedure

1. Stage the deliverable under `reports/` (moving any superseded file to `archive/` with a date prefix).
2. Update `INDEX.md`: one row per file — path, deliverable title, language/format, version, date, description, provenance.
3. Commit with a plain, secret-free message: `docs(reports): add <deliverable> — <one-line reason>`.
4. Push using the transient-credential procedure (§1) — token via `GH_DOCS_TOKEN`, never persisted.
5. Verify (§5) and report the resulting repository links.

## 5. Verification checklist (after every upload)

- [ ] `git ls-remote` shows the pushed commit on the target branch.
- [ ] The file exists at its path in the repository with the correct name and extension.
- [ ] File size is non-zero; the Markdown contains the complete report (spot-check start/end and required sections); the Word file opens and is not corrupted.
- [ ] For Arabic deliverables: RTL direction, headings, tables, and text are preserved.
- [ ] `INDEX.md` reflects the uploaded state and was committed together with the files.
- [ ] No token or secret appears in any file, commit message, or log (grep the diff before pushing).
