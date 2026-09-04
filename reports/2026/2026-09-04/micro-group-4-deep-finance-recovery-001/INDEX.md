# Group 4 Delivery — Deep Finance: Assets, Depreciation, Loans, Retained Deposits, Inventory Automation (Recovery)

Program: Zman→Micro capability transfer (six groups) — Group 4, recovery session.
Baseline: Micro `main @ 67d4e41` (Groups 1–3, PRs #149–#151).
Delivery: PR #152 merged → `main @ 05669a9` (local == remote, clean tree, CI green — run 33867065062 + Cloudflare Pages).

## Contents
- `en/group-4-recovery-and-implementation-report-en.md` — recovery gate, preserved/corrected work, verification, Zman adopt/don't-copy, limitations
- `en/group-4-assets-depreciation-contracts-en.md` — asset event model, straight-line depreciation with last-month sweep, disposal/write-off, corrections
- `en/group-4-loans-deposit-contracts-en.md` — outgoing loans (never expense/withdrawal), retained-deposit three-outcome classification, hardened import integrity
- `en/group-4-inventory-automation-and-waste-en.md` — explicit single-atomic-commit automation contract, three-layer idempotency, shortage policy, MIC-13 rewrite
- `en/group-4-reconciliation-and-test-evidence-en.md` — MIC-10..13, 24-scenario coverage map, final gate table (277/277 + 717/717)
- `en/group-4-ci-investigation-report-en.md` — full failure matrix: source-format failure (fixed) + npm audit registry outage (classified, retried, green)
- `en/group-4-recovery-subagent-synthesis-en.md` — 4-a…4-e findings and dispositions
- `ar/group-4-recovery-and-implementation-report-ar.docx` — Arabic RTL Word report (bidi paragraphs, RTL tables, TOC field, 3-section numbering, render-verified)

## Key facts
- Recovery preserved the full prior implementation (f20f513, 74 files) — nothing reset, nothing rebuilt; the six REQUIRED-FIX findings of the adversarial review plus two later polish items were applied on top (dbd5f15, 632af0f).
- 9 new financial-event types, 3 optional delta columns (assets/loans/retained revenue), mandatory linked contexts; schema 34 / export 26 with honest 25/33 migration.
- CI matrix: 33861709388 source-format failure → fixed; 33866384883 npm-audit registry ERR_SOCKET_TIMEOUT ×3 → classified infrastructure (local audit clean), retried transparently; 33867065062 SUCCESS; merged 05669a9.
- Gates: typecheck ×2, lint 0/37 baseline, format, density (Statement 101 / AssetDetail 41 documented ratchets), domain 277/277 (23 files), prototype 717/717 (110 files), PWA build, audit clean.
