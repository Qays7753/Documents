# Index of Deliverables

Master index of every report and generated document delivered to this repository. Current versions live in `reports/`; superseded versions live in `archive/` (date-prefixed) and are logged at the bottom. This file is updated in the same commit as every upload.

## Delivery 2 — 2026-09-03 — Zman-to-Micro gap analysis package

Dated-folder delivery (task-prescribed structure `reports/YYYY/YYYY-MM-DD/<delivery-id>/`), produced by five specialized read-only sub-agents plus parent consolidation. Both product repositories were strictly read-only.

| # | Path | Deliverable | Language / format | Version | Date | Description | Provenance |
|---|---|---|---|---|---|---|---|
| 4 | `reports/2026/2026-09-03/zaman-to-micro-gap-analysis-001/en/zaman-to-micro-gap-analysis-en.md` | Zman-to-Micro Capability Gap Analysis and Transfer Design | English · Markdown (canonical source) | v1.0 | 2026-09-03 | Full comparative analysis: Outputs A–H — 24-capability Zman catalogue (ZC-01..ZC-24), 22-row gap register + 10 false-gap warnings, 7 deep dossiers, transfer/navigation map, financial & data contracts (MIC-1..MIC-10), ranked set P0/P1/P2/Reject (TR-01..TR-17), final transfer architecture, implementation-ready handoff with acceptance criteria | Zman `main` @ `bdd63ab` + Micro `main` @ `4db6a5f` (both read-only, anonymous URL access) |
| 5 | `reports/2026/2026-09-03/zaman-to-micro-gap-analysis-001/ar/zaman-to-micro-gap-analysis-ar.docx` | تحليل فجوات القدرات من Zman إلى Micro وتصميم النقل | العربية · Word (.docx, RTL) | v1.0 | 2026-09-03 | Arabic RTL rendering of the complete analysis: 25 pages A4, right-to-left headings, paragraphs and tables, cover page, TOC (Roman front matter / Arabic body numbering), all Outputs أ–ح | Generated from the finalized English report (deliverable #4) |
| 6 | `reports/2026/2026-09-03/zaman-to-micro-gap-analysis-001/subagents/` | Five specialized sub-agent reports (01 Zman capability map · 02 Micro gap comparison · 03 workflow/mobile UX · 04 financial/data integrity · 05 transfer architecture & critical review) | English · Markdown | v1.0 | 2026-09-03 | Structured finding blocks (ZC/MG/UX/FI/TR series) with full evidence indexes from both repositories; SA-5 resolves cross-agent contradictions and issues corrections adopted by the final synthesis | Read-only inspection of both product repositories |
| 7 | `reports/2026/2026-09-03/zaman-to-micro-gap-analysis-001/supporting/ar-report-render-preview.pdf` | Arabic report — render verification preview | العربية · PDF | v1.0 | 2026-09-03 | LibreOffice A4 rendering of deliverable #5 proving the .docx opens correctly with RTL preserved; convenience preview, not a substitute for the .docx | Rendered from deliverable #5 |
| 8 | `reports/2026/2026-09-03/zaman-to-micro-gap-analysis-001/metadata.yml` | Delivery metadata (files, sizes, SHA-256, verification results, findings summary) | YAML | v1.0 | 2026-09-03 | Machine-readable manifest of the delivery: file checksums, repo states, verification checklist incl. token-leak scan (pass), ranked transfer set summary | Generated at delivery time |

## Delivery 1 — 2026-09-01 — Micro target-state design package

| # | Path | Deliverable | Language / format | Version | Date | Description | Provenance |
|---|---|---|---|---|---|---|---|
| 1 | `reports/Micro-Target-State-Design-Report.md` | Micro — Target Flow, Screen, Navigation & Gap-Discovery Design Report | English · Markdown (canonical source) | v1.0 | 2026-09-01 | Decision-ready target-state design package: 20% current-state discovery (verified flow map, screen-and-entry table, capability classification of 88 rows, major flow breaks) + 80% target-state design — Output A feature distribution & screen map, Output B screen hierarchies & textual wireframes, Output C core task flows (five mandatory + supporting), Output D missing-capabilities register (24 rows, 4×P0), Output E final target architecture with D1–D14 decision register and implementation roadmap; 43 external references with Jordanian context | Generated from Micro `main` @ `1b37c77c72f719a4b51be3aa5e243063c997df2e` (latest, clean tree) |
| 2 | `reports/Micro-Target-State-Design-AR.docx` | مايكرو — تصميم التدفق والشاشات والتنقل المستهدف | العربية · Word (.docx, RTL) | v1.0 | 2026-09-01 | Arabic RTL rendering of the complete report: 48 pages A4, right-to-left headings and tables preserved, executive summary, Part 1 current state, Outputs أ–هـ, the full missing-capabilities register (24 rows), decision cards, and references | Generated from the finalized English report (deliverable #1) |
| 3 | `reports/Micro-Target-State-Design-AR-preview.pdf` | Arabic report — read-only preview | العربية · PDF | v1.0 | 2026-09-01 | Convenience PDF rendering of the Arabic Word document (LibreOffice, A4) for quick review without Word; not a substitute for the .docx | Rendered from deliverable #2 |

## Archive log

| Path | Replaced on | Superseded by |
|---|---|---|
| — (empty — no superseded versions yet) | | |

## Numbering note

Row numbers `1–3` belong to delivery 1 (flat `reports/` names, 2026-09-01); rows `4–8` belong to delivery 2 (dated folder, 2026-09-03). Numbers are append-only and never reused; a superseded file keeps its row and gains an archive-log entry.
