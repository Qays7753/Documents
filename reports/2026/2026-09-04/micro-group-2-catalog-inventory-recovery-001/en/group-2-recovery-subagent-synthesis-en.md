# Group 2 Recovery Sub-Agent Synthesis — SA-1…SA-5 Findings, Conflicts, and Parent Resolutions

**Delivery:** micro-group-2-catalog-inventory-recovery-001 · **Date:** 2026-09-04
**Context:** Five specialized sub-agents served the Group 2 cycle (SA-1 Micro investigator, SA-2 Zman journey analyst, SA-3 financial/inventory truth reviewer, SA-4 Arabic RTL mobile UX reviewer, SA-5 adversarial QA), followed by this recovery session's parent verification. The parent remained responsible for reconciliation and final correctness; sub-agents never pushed conflicting work (all reviews were read-only; implementation was parent-only).

---

## 1. SA-1 — Micro inventory/storage investigator

**What it mapped:** the complete live inventory surface before Group 2 — six movement types, moving-average `consumptionValueMinor`, the non-negative fold, `commitInventory` atomicity, catalog/units/conversions, supplier-purchase semantics (payments, revisions, no cash events — read-time aggregation only), the transfer/import version-pair machinery, guided opening import, the integrity registry, and the unmeasured deep editors in the density counter.

**Key findings adopted:** no tracked/untracked flag existed anywhere; no purchase→receipt bridge; the migration precedent to follow was Group 1's `categoryLabel` (single-file version bump, null defaults, legacy pair acceptance, contains-guarded IDB upgrade); lint ceiling 37; next free contract number 28. **Pre-existing defects it surfaced** (all addressed or documented): WasteContext duplication across two domains (drift risk — documented); «تراجع» rendering on already-reversed movements (fixed in Group 2 with «مرتدة موثقًا»); contract 11's unimplemented "awaiting receipt" promise (superseded by contract 28's received card); supplier payments bypassing cash wallets (documented, out of Group 2 scope).

## 2. SA-2 — Zman journey analyst

**What it reconstructed (read-only, with file:line citations):** the real app root and live schema; `catalog_component.tracked` per item; the movement ledger with six source types; purchase→immediate stock-in with linked component; weighted-average COGS at write time (floor, immutable on out, residual sweep); the untrack soft-delete of **all** movements with no equity compensation; no receipt step and no partial receipt anywhere; delivery deduction atomic with negative stock allowed (warning only); waste as a manual adjustment producing a non-cash write-off expense row; opening stock only on first activation.

**Value to Group 2:** the journey shapes (question order, tracking toggle placement, movement history modal, zero-cost honesty) transferred directly; the mechanics were filtered — Micro kept its stronger financial-truth rules wherever Zman's shortcuts (silent zeros, soft-delete reversals, untracked silent skip, untrack equity collapse) conflicted. SA-2's anti-copy list is reproduced in the contracts report §12.

## 3. SA-3 — financial/inventory truth reviewer

**Verdict:** the design contract was financially truthful in its core (waste never enters the period result; purchases cash/payables-only; non-negative fold unchanged; shortage mapping honest), with **8 required fixes before implementation**:

| # | Finding | Resolution in implementation |
|---|---|---|
| R1 | Import validator lockstep gap (consumption-requires-orderId vs new order-or-reason; value-zero-iff-unknown) | Both rules encoded in `validInventoryMovement` |
| R2 | Snapshot enumeration must carry shortages (IDB read/replace, memory, `emptySnapshot`, guided import) — else export/import drops them and reset-all leaks | All five paths carry shortages; tested |
| R3 | Unknown→zero read surfaces (order comparison; waste rows) | `readOrderActualMaterialComparison` carries cost knowledge; waste rows show «غير معروفة بعد» |
| R4 | Untrack dialog copy contradicted retrack semantics | Truth-corrected («غير محدد بعد» until re-confirmed) |
| R5 | Movement editor listed ALL materials (promise: tracked-only) | References serve tracked-only; purchase editor keeps all + hint |
| R6 | `confirmMaterialOpening` increase-with-unknown vs adjust() rule conflict | `adjust` accepts zero-unknown increases; service rule updated + tested |
| R7 | Purchase edit below received value/quantity; link swapping | Both guards added; before-fields in revisions; tested |
| R8 | MIC-8/`quantityKnowledge` must treat ABSENT opening as known (legacy false positives) | Explicit predicates; tested |

Nice-to-haves it proposed and the parent adopted: import-time fold non-negativity; `extractRemainder` pure-unknown support; guided import writing `material.opening`; public-surface conscious additions; contract-27 MIC-8 reservation note.

## 4. SA-4 — Arabic RTL mobile UX reviewer

**Verdict:** implementable on a 360px one-handed device with **14 mandated UX fixes**, all adopted: «أيوه» correction; date/source gated to confirmed branches; dynamic save labels; fixed-min-height effect previews (116px law) as the last block above the sticky save; the untrack dialog without a reason field (keyboard law) and with the truth-fixed consequence line; bridge CTA shortened to 23 chars; received card placed after the decision card and before payments; fully-received/unknown-expected states; the shortage panel at the end of the form (typing-jitter law) with a live one-line warning; cost question on receipt/adjust-increase; Finance waste row in the period view with word-order fix; MaterialSheet chips capped at 6, top-of-sheet, `MoneyValue` inside chips, no autoFocus with suggestions; the confirm-opening deep route instead of a dialog; and the density ledger (new PAGES entries; Finance 182; the `wasteSummary`→`periodWaste` rename to dodge the counter's "Summary" heuristic — the final count matched its prediction exactly).

Its 12-verdict Arabic copy audit (colloquial questions / MSA truth copy, no jargon in owner labels) and the 7 REQUIRED state additions (fully-received, unknown expected quantity, unconfirmed-with-movements, legacy absent-opening ⇒ known, bridge untracked hint, reversed-row marker, resolved-shortage visibility) are all present in the merged code.

## 5. SA-5 — adversarial QA reviewer

**Process:** reviewed the complete 45-file diff file-by-file; ran all gates read-only (239/239 domain, 633/633 prototype at that time); executed the adversarial checklist end-to-end (duplicate movements and idempotency including the `${key}:shortage` interplay and double-tap; hidden automation greps — `createInventoryMovement`/`commitInventory` confined to the two legitimate services, zero new `createFinancialEvent` sites; no direct store access from pages; source references and deep links; untracked guards; negative stock; history preservation; `notifyDataChanged` propagation; migration and reset-all; Group 1 regressions; RTL/date/money formatting; density-counter heuristics; contract/doc accuracy; 14 named edge cases).

**Verdict: FIX REQUIRED** — 1 MAJOR (bridge deep-link prefill never fires) + 6 MINOR + notes. Constitution invariants verified intact. Every REQUIRED finding was resolved (see the test-evidence report §5 for the finding→resolution table); the interruption happened between the source fixes and their verification tests, which the recovery session completed, verified, and merged.

## 6. Parent reconciliation log (decision order: prompt > live code > reviews)

1. **Selective-inventory automation** — the prior program's "rejected" label is void (the program prompt voids it); Group 2 implemented the safe subset: explicit receipts, shortage records, stated-consequence untracking. Silent auto-deduct and hidden negative stock remain rejected.
2. **Weighted average** — kept Micro's moving average (documented mapping) rather than rewriting the cost engine for Zman parity; cost-knowledge states carry the honesty burden.
3. **Untrack semantics** — SA-3 R4 and SA-4 agreed against Zman's copy; history preservation won over both Zman's soft-delete and any balance-collapse shortcut.
4. **Shortage vs negative** — SA-2 documented Zman's negative-allowed behavior; SA-3's truth review and the constitution forced the shortage-record policy; the mapping is documented for the owner (contract 28, D-027).
5. **Density vs honesty** — the counter heuristic collision (`wasteSummary`) was resolved by renaming the reading, not by special-casing the counter (D-029).
6. **Recovery-specific reconciliation** — the interrupted session's own claims (633/633 green) were falsified by re-execution (639, 3 failing); the three failures were diagnosed as test defects (wrong money format; missing import; missing suggestions wiring), not implementation gaps, and were repaired rather than re-implemented — preserving 100% of the interrupted work.

## 7. Recovery verification (the parent's own final pass)

The recovery parent re-ran the entire gate chain on the snapshot, after the fixes, and on merged `main` (three full executions), re-verified the tree identity between the CI-verified branch and the merge commit (`622716ae`), confirmed local == remote at `1207a5a` with a clean tree, performed the live browser QA (12 screenshots, 0 console errors), scanned the final diff and the delivery package for secrets, and authored this delivery. No sub-agent claim — including the interrupted session's — was merged on trust alone.
