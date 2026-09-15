# INDEX — Group 2 Delivery: Catalog, Materials, Selective Inventory, Receiving, and Safe Inventory Automation (Recovery)

**Delivery ID:** micro-group-2-catalog-inventory-recovery-001
**Date:** 2026-09-04
**Program:** Group 2 of the six-group Zman→Micro transfer program (standalone resumption prompt; recovery-first execution — a previous agent session was interrupted mid-implementation and 100% of its work was preserved, completed, merged, and delivered)

| Field | Value |
|---|---|
| Micro repository | https://github.com/Qays7753/Micro |
| Final Micro `main` commit | `1207a5adc460829322c9e33013e492d3cdb816bd` (merge of PR #150; merged tree `622716ae`; net 49 files, +5928/−411) |
| Recovery commits | `811e8ce` snapshot of the interrupted working tree (49 files, +5630/−411) · `e40da57` SA-5 verification completion · `2e8dcab` transparent CI retrigger (npm audit-endpoint outage) |
| Pull request | https://github.com/Qays7753/Micro/pull/150 |
| Zman reference (read-only) | https://github.com/Qays7753/zman-app (`main` @ `bdd63ab`; never modified) |
| Report purpose | Recovery narrative and implementation, inventory/financial contracts, catalog/UX review, test evidence, and sub-agent synthesis for Group 2 (per-material tracking, guided activation with known/unknown/confirmed-zero openings, purchase→receipt bridge with partial receipts, movement contracts, shortage policy, non-cash waste, untracking with consequences, schema 32/export 24 migration, MIC-8) |
| Test status | **PASS** — `pnpm check` exit 0 (typecheck ×2; lint 0 errors/37 warnings = baseline; format; text-density at caps; design-guards; 239 domain + 643 prototype tests; PWA build); GitHub Actions CI `success` (after a documented transient npm-registry audit outage); live browser QA 390×844 RTL with 12 screenshots and 0 console errors |
| Governing contract (in-repo) | `docs/contracts/28-selective-inventory-tracking-contract.md` (+ addenda to contracts 09/11/26/27; decisions D-027/028/029) |
| Schema / export | 31→32 / 23→24 (legacy 23/31 accepted; absent fields default to null — never zero; new `inventory-shortages` store; three-store atomic commits) |
| Security | No token or credential appears in any commit, diff, report, or file of this delivery (scanned; path-scoped credential store outside the repositories) |
| Unresolved limitations | None blocking. Documented: order-to-sale deduction deferred to Group 3 (contract in place); template-literal money in preview sentences (non-bidi nodes); unknown-id deep-link fallback guarded by prefill-once; CI flake record (npm registry outage — no code defect) |

## Files

| # | Path | Type | Purpose |
|---|---|---|---|
| 1 | [`en/group-2-recovery-and-implementation-report-en.md`](en/group-2-recovery-and-implementation-report-en.md) | English · Markdown | The interrupted state, recovery map and snapshot, recovered vs newly implemented work, implementation shape, migration, scenario matrix, merge evidence, limitations |
| 2 | [`en/group-2-inventory-financial-contracts-en.md`](en/group-2-inventory-financial-contracts-en.md) | English · Markdown | Normative contracts: entity chain and write boundaries, tracking/opening knowledge, movement rules, purchase→receipt bridge, cost model, shortage policy, waste, untracking, migration, Group 1 integration, Zman transfer map |
| 3 | [`en/group-2-catalog-and-ux-review-en.md`](en/group-2-catalog-and-ux-review-en.md) | English · Markdown | Material identity journeys, surface behaviors, seventeen required states, Arabic copy audit, density ledger, RTL/mobile rules, Zman UX dispositions, live QA verdict |
| 4 | [`en/group-2-test-evidence-en.md`](en/group-2-test-evidence-en.md) | English · Markdown | Gate matrix with re-executed commands, key test files, scenario coverage A–N, CI runs (incl. the outage record), SA-5 finding→resolution table, browser QA log, security checks |
| 5 | [`en/group-2-recovery-subagent-synthesis-en.md`](en/group-2-recovery-subagent-synthesis-en.md) | English · Markdown | SA-1…SA-5 findings and verdicts, R1–R8 required fixes and resolutions, parent reconciliation log, recovery verification |
| 6 | [`ar/group-2-recovery-and-implementation-report-ar.docx`](ar/group-2-recovery-and-implementation-report-ar.docx) | العربية · Word (.docx, RTL) | Full Arabic recovery & implementation report: RTL cover, TOC (Roman front matter / Arabic body numbering), RTL paragraphs and tables, 7 pages A4 |
| 7 | [`supporting/ar-report-render-preview.pdf`](supporting/ar-report-render-preview.pdf) | العربية · PDF | LibreOffice render of deliverable #6 proving the .docx opens with RTL preserved (convenience preview; VLM-verified pages: cover, TOC, body, tables) |
| 8 | [`supporting/00-setup-complete.png`](supporting/00-setup-complete.png) → [`supporting/04-material-saved-row.png`](supporting/04-material-saved-row.png) | Screenshots | Live browser QA (390×844 RTL): first-use setup, inventory activation and empty states, the guided tracking question, the confirmed-opening branch, the saved tracked row |
| 9 | [`supporting/05-purchase-detail-bridge-cta.png`](supporting/05-purchase-detail-bridge-cta.png) → [`supporting/07-purchase-partial-received-card.png`](supporting/07-purchase-partial-received-card.png) | Screenshots | Live bridge journey: purchase detail with received card + CTA, the deep-linked receipt editor fully prefilled (the SA-5 F1 fix live: quantity 50 / value 20.00), a partial receipt (30/50 · 12.00/20.00) with safe return |
| 10 | [`supporting/08-material-position-after-receipt.png`](supporting/08-material-position-after-receipt.png) → [`supporting/11-tools-integrity-mic8.png`](supporting/11-tools-integrity-mic8.png) | Screenshots | Live evidence: material position after receipt, the waste editor with non-cash preview, the Finance period waste row («هدر مخزون هذه الفترة \| 2.00 — غير نقدي»), and the integrity surface with MIC-8 «سلامة المخزون والمواد» سليم |
| 11 | [`metadata.yml`](metadata.yml) | YAML | Machine-readable manifest (checksums, repo states, verification results, scope) |

All facts above are verifiable from the linked repositories at the stated commits. No token or credential appears in any file of this delivery (scanned).
