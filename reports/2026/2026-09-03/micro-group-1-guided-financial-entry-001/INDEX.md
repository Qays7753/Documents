# INDEX — Group 1 Delivery: Guided Financial Entry, Expense Classification, Allocation, and Financial Foundation

**Delivery ID:** micro-group-1-guided-financial-entry-001
**Date:** 2026-09-03
**Program:** Group 1 of the six-group Zman→Micro transfer program (standalone execution; completion-state gate verified before work — no prior implementation of this program existed)

| Field | Value |
|---|---|
| Micro repository | https://github.com/Qays7753/Micro |
| Final Micro `main` commit | `761638b` (merge of PR #149; feature commit `bc2e4c5`; baseline `4db6a5f`) |
| PR | https://github.com/Qays7753/Micro/pull/149 |
| Zman reference (read-only) | https://github.com/Qays7753/zman-app (`main` @ `bdd63ab`) |
| Report purpose | Implementation, financial contracts, UX/flow review, test evidence, and sub-agent synthesis for Group 1 (guided expense journey, `categoryLabel` classification, allocation review, effect preview derived from the committed intent, canonical period-result lock, read-only integrity foundation `/tools/integrity`) |
| Test status | **PASS** — `pnpm check` fully green (typecheck; lint 0 errors/37 warnings = baseline; format; text-density; design-guards; 231 domain + 607 prototype tests; PWA production build); GitHub Actions CI `completed success`; live browser QA on the production build (390×844 RTL, 0 console errors) |
| Governing contract (in-repo) | `docs/contracts/27-guided-financial-entry-contract.md` |
| Schema / export | 30→31 / 22→23 (legacy 22/30 accepted, labels default to null, no backfill) |
| Unresolved decisions | None blocking. Deferred (documented, deliberate): TR-03 statement export, TR-05 activity layer, TR-07 inventory bridge, TR-09, EventsLayer tag filter (needs `?tag` vocabulary), OwnerWithdrawalEditor loan hint (density cap), MIC-3/5/6/8/10 (registry reserved), density-counter truth-section blind-spot fix (D-026) |

## Files

| # | Path | Type | Purpose |
|---|---|---|---|
| 1 | [`en/group-1-implementation-report-en.md`](en/group-1-implementation-report-en.md) | English · Markdown | Complete implementation, decisions, files, migration, scenarios, final commit |
| 2 | [`en/group-1-financial-contracts-en.md`](en/group-1-financial-contracts-en.md) | English · Markdown | Category, nature, relationship, allocation, effect-preview, canonical-result, and integrity contracts |
| 3 | [`en/group-1-ux-and-flow-review-en.md`](en/group-1-ux-and-flow-review-en.md) | English · Markdown | Screen contracts (18 fields × 2 primary screens), journeys, Arabic copy decisions, states, mobile behavior, before/after |
| 4 | [`en/group-1-test-evidence-en.md`](en/group-1-test-evidence-en.md) | English · Markdown | Commands, results, migration checks, browser/device checks, SA-5 findings, known limitations |
| 5 | [`en/group-1-subagent-synthesis-en.md`](en/group-1-subagent-synthesis-en.md) | English · Markdown | SA-1…SA-5 findings, conflicts, and resolutions |
| 6 | [`ar/group-1-implementation-report-ar.docx`](ar/group-1-implementation-report-ar.docx) | العربية · Word (.docx, RTL) | Full Arabic implementation report: RTL cover, TOC (Roman front matter / Arabic body numbering), RTL paragraphs and tables, 7 pages A4 |
| 7 | [`supporting/ar-report-render-preview.pdf`](supporting/ar-report-render-preview.pdf) | العربية · PDF | LibreOffice render of deliverable #6 proving the .docx opens with RTL preserved (convenience preview, not a substitute) |
| 8 | [`supporting/group1-integrity-live.png`](supporting/group1-integrity-live.png) | Screenshot | Live browser QA: the integrity surface after a run (verdict + five checks, 390×844) |
| 9 | [`supporting/group1-payable-effect-live.png`](supporting/group1-payable-effect-live.png) | Screenshot | Live browser QA: the payable editor's derived effect preview |
| 10 | [`metadata.yml`](metadata.yml) | YAML | Machine-readable manifest (checksums, repo states, verification results) |

All facts above are verifiable from the linked repositories at the stated commits. No token or credential appears in any file of this delivery (scanned).
