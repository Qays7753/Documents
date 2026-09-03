# Index of Deliverables

Master index of every report and generated document delivered to this repository. Current versions live in `reports/`; superseded versions live in `archive/` (date-prefixed) and are logged at the bottom. This file is updated in the same commit as every upload.

## Delivery 3 — 2026-09-03 — Micro Group 1 implementation package (guided financial entry)

Dated-folder delivery (`reports/2026/2026-09-03/micro-group-1-guided-financial-entry-001/`). First **implementation** delivery of the transfer program: Group 1 merged to Micro `main` via PR #149 (`761638b`) after green CI and adversarial review; gap-analysis TR-01/TR-02/TR-04 implemented, MIC-1/2/4/7/9 integrity foundation delivered read-only, schema 31 / export 23.

| # | Path | Deliverable | Language / format | Version | Date | Description | Provenance |
|---|---|---|---|---|---|---|---|
| 9 | `reports/2026/2026-09-03/micro-group-1-guided-financial-entry-001/en/group-1-implementation-report-en.md` | Group 1 Implementation Report | English · Markdown | v1.0 | 2026-09-03 | Complete implementation record: completion-state gate, scope §5.1–5.9, files, migration (30→31 / 22→23), 41 new tests, scenarios A–J, decisions register, defect fixes D-025 + guard fix, final merge verification | Micro `main` @ `761638b` (PR #149, feature `bc2e4c5`, baseline `4db6a5f`) |
| 10 | `reports/2026/2026-09-03/micro-group-1-guided-financial-entry-001/en/group-1-financial-contracts-en.md` | Group 1 Financial Contracts | English · Markdown | v1.0 | 2026-09-03 | Binding contracts: six-dimension concept separation, categoryLabel data contract, guided-journey contract, effect-preview derivation contract, allocation rules, canonical period-result designation, integrity registry (MIC-1..MIC-9 + reserved), test traceability | Mirrors in-repo contract 27 |
| 11 | `reports/2026/2026-09-03/micro-group-1-guided-financial-entry-001/en/group-1-ux-and-flow-review-en.md` | Group 1 UX & Flow Review | English · Markdown | v1.0 | 2026-09-03 | Two complete 18-field screen contracts (FinancialEventEditor, ToolsIntegrity), secondary-surface deltas, Arabic copy register decisions, state inventory, mobile/RTL compliance, live QA transcript (390×844, zero console errors) | Production build live session + jsdom suites |
| 12 | `reports/2026/2026-09-03/micro-group-1-guided-financial-entry-001/en/group-1-test-evidence-en.md` | Group 1 Test Evidence | English · Markdown | v1.0 | 2026-09-03 | Baseline vs final gates, full new-test inventory (41), migration/compatibility evidence, browser/device checks, SA-5 findings & dispositions, known limitations | CI logs + local runs at the stated commits |
| 13 | `reports/2026/2026-09-03/micro-group-1-guided-financial-entry-001/en/group-1-subagent-synthesis-en.md` | Group 1 Sub-Agent Synthesis | English · Markdown | v1.0 | 2026-09-03 | SA-1…SA-5 mandates and findings, adopted changes, conflict table with resolutions by authority order, independent verification layer | Five sub-agent reports consolidated |
| 14 | `reports/2026/2026-09-03/micro-group-1-guided-financial-entry-001/ar/group-1-implementation-report-ar.docx` | تقرير تنفيذ المجموعة الأولى | العربية · Word (.docx, RTL) | v1.0 | 2026-09-03 | Arabic RTL implementation report: 7 pages A4, dark cover with gold accents, TOC (Roman front matter / Arabic body numbering), RTL justified paragraphs and RTL tables, executive summary through final state | Generated from the finalized English report (deliverable #9) |
| 15 | `reports/2026/2026-09-03/micro-group-1-guided-financial-entry-001/supporting/` | Render preview (PDF) + live QA screenshots (2 PNG) | PDF / PNG | v1.0 | 2026-09-03 | LibreOffice render of deliverable #14 proving the .docx opens with RTL preserved; production-build browser evidence (integrity surface after run; payable effect preview) | Rendered / captured during verification |
| 16 | `reports/2026/2026-09-03/micro-group-1-guided-financial-entry-001/metadata.yml` | Delivery metadata | YAML | v1.0 | 2026-09-03 | Machine-readable manifest: SHA-256 checksums, repo states (Micro `761638b`), verification checklist (all pass incl. token-leak scan), scope implemented/deferred | Generated at delivery time |

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

Row numbers `1–3` belong to delivery 1 (flat `reports/` names, 2026-09-01); rows `4–8` belong to delivery 2 (dated folder, 2026-09-03); rows `9–16` belong to delivery 3 (dated folder, 2026-09-03). Numbers are append-only and never reused; a superseded file keeps its row and gains an archive-log entry.
