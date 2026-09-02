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

See `INDEX.md` for the authoritative list. As of 2026-09-03 the repository carries two packages:

**Zman-to-Micro gap analysis package (2026-09-03)** — `reports/2026/2026-09-03/zaman-to-micro-gap-analysis-001/`:

1. `en/zaman-to-micro-gap-analysis-en.md` — English canonical report (Markdown): one-way comparative discovery Zman → Micro with Outputs A–H — 24-capability Zman catalogue, 22-row gap register plus 10 false-gap warnings, deep dossiers, transfer/navigation map, financial & data contracts, ranked transfer set P0/P1/P2/Reject (TR-01..TR-17), final transfer architecture, implementation-ready handoff.
2. `ar/zaman-to-micro-gap-analysis-ar.docx` — Arabic RTL Word rendering of the complete analysis (25 pages A4, TOC, all Outputs).
3. `subagents/` — the five specialized sub-agent reports (Zman capability map, Micro gap comparison, workflow/mobile UX, financial/data integrity, transfer architecture & critical review) with full evidence indexes.
4. `supporting/` + `metadata.yml` — render-verification preview of the Arabic report and machine-readable delivery manifest (checksums, verification results, findings summary).
5. Both product repositories (Zman `zman-app` @ `bdd63ab`, Micro @ `4db6a5f`) were inspected strictly read-only.

**Micro target-state design package (2026-09-01)** — flat files under `reports/`:

1. `reports/Micro-Target-State-Design-Report.md` — English canonical report (Markdown): 20% current-state discovery + 80% target-state design, Outputs A–E, five mandatory core task flows, 24-row missing-capabilities register, D1–D14 decision register, 43 external references.
2. `reports/Micro-Target-State-Design-AR.docx` — Arabic RTL Word document rendered from the finalized English report (48 pages A4, RTL headings and tables preserved).
3. `reports/Micro-Target-State-Design-AR-preview.pdf` — read-only PDF rendering of the Arabic Word document, for quick review without Word.

## Binding rules

- **Deliverables only.** Reports and generated documents; nothing else.
- **No silent replacement.** When a deliverable is superseded, the previous file moves to `archive/` (date-prefixed) and `INDEX.md` records both versions.
- **Index discipline.** Every upload updates `INDEX.md` in the same commit.
- **No secrets, ever.** No tokens, keys, or credentials in any file, commit message, log, or URL — see `UPLOAD_GUIDE.md` for the token-handling rules that govern access to this repository.
