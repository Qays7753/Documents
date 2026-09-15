# Group 3 Delivery — Costing, Products, Orders, Delivery, Direct Sales, and Settlement

Program: Zman→Micro capability transfer (six groups) — Group 3.
Baseline: Micro `main @ 1207a5a` (Group 1 PR #149 + Group 2 PR #150 merged).
Delivery: Micro PR #151 merged → `main @ 67d4e41` (local == remote, clean tree, CI success).

## Contents
- `en/group-3-implementation-report-en.md` — baseline, completion gate, implementation, bug fixes, verification, Zman adopt/don't-copy, limitations
- `en/group-3-cost-product-order-contracts-en.md` — calculator/snapshot/product/order/delivery contracts (design contract A–G)
- `en/group-3-sale-deposit-settlement-contracts-en.md` — revenue-once, deposit truth, settlement-without-second-sale, reversal economics
- `en/group-3-ux-and-flow-review-en.md` — surfaces, guided questions, states, RTL/formatting compliance
- `en/group-3-test-evidence-en.md` — suites (domain 246/246, prototype 660/660), new test files, scenario coverage map
- `en/group-3-subagent-synthesis-en.md` — SA-1…SA-5 findings and consolidation
- `ar/group-3-implementation-report-ar.docx` — Arabic RTL Word report (real docx: RTL paragraphs, RTL tables, TOC field, 3-section numbering)

## Key facts
- Atomic delivery transaction (`commitOrderDelivery`): order + consumption movements + shortage rows + cash allocation in one IndexedDB transaction; idempotent by deterministic operation keys; self-healing on retry.
- Delivery reversal as documented correction: revenue neutralized to honest unknown, mirrored movement reversals, collected cash untouched, review unlock + resume path.
- Schema 33 / export 25; legacy 24/32 and 23/31 accepted with null-honest normalization.
- Gates: typecheck ×2, lint 0 errors / 37 baseline warnings, format, density (caps documented), design guards, domain 246/246 (21 files), prototype 660/660 (102 files), PWA build.
- SA-5 adversarial review: no blockers; REQUIRED/RECOMMEND findings fixed pre-merge.
