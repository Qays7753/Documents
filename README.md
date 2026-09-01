# Documents — Permanent Delivery Repository

This repository is the **permanent delivery location** for reports and generated documents produced during work on the **Micro** project ([github.com/Qays7753/Micro](https://github.com/Qays7753/Micro)) and related tasks. It holds deliverables only — no source code, no secrets, no credentials.

## Structure

| Path | Purpose |
|---|---|
| `reports/` | Current, authoritative deliverables — every new upload lands here |
| `archive/` | Superseded versions of deliverables — replaced files move here, never deleted |
| `INDEX.md` | Master index of every deliverable ever uploaded, with version history |
| `UPLOAD_GUIDE.md` | Binding rules and procedure for adding new deliverables (incl. token security) |

## Current deliverables

See `INDEX.md` for the authoritative list. As of 2026-09-02 the repository carries the **Micro target-state design package**:

1. `reports/Micro-Target-State-Design-Report.md` — English canonical report (Markdown): 20% current-state discovery + 80% target-state design, Outputs A–E, five mandatory core task flows, 24-row missing-capabilities register, D1–D14 decision register, 43 external references.
2. `reports/Micro-Target-State-Design-AR.docx` — Arabic RTL Word document rendered from the finalized English report (48 pages A4, RTL headings and tables preserved).
3. `reports/Micro-Target-State-Design-AR-preview.pdf` — read-only PDF rendering of the Arabic Word document, for quick review without Word.

## Binding rules

- **Deliverables only.** Reports and generated documents; nothing else.
- **No silent replacement.** When a deliverable is superseded, the previous file moves to `archive/` (date-prefixed) and `INDEX.md` records both versions.
- **Index discipline.** Every upload updates `INDEX.md` in the same commit.
- **No secrets, ever.** No tokens, keys, or credentials in any file, commit message, log, or URL — see `UPLOAD_GUIDE.md` for the token-handling rules that govern access to this repository.
