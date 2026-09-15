# Group 2 Recovery and Implementation Report — Catalog, Materials, Selective Inventory, Receiving, and Safe Inventory Automation

**Delivery ID:** micro-group-2-catalog-inventory-recovery-001
**Date:** 2026-09-04
**Program:** Group 2 of the six-group Zman→Micro transfer program (standalone resumption prompt; recovery-first execution)

| Field | Value |
|---|---|
| Micro repository | https://github.com/Qays7753/Micro |
| Baseline (before Group 2) | `761638b` — Group 1 merged via PR #149 |
| Recovery snapshot commit | `811e8ce` — preserved interrupted working tree (49 files, +5630/−411) |
| SA-5 completion commit | `e40da57` — repaired/added verification tests (+333/−35 within the same 2 files) |
| CI retrigger commit | `2e8dcab` — empty, transparent message (npm registry audit-endpoint outage) |
| Final Micro `main` commit | `1207a5adc460829322c9e33013e492d3cdb816bd` (merge of PR #150; merged tree `622716ae`) |
| Pull request | https://github.com/Qays7753/Micro/pull/150 |
| Net change on `main` | 49 files changed, +5928 insertions, −411 deletions |
| Zman reference (read-only) | https://github.com/Qays7753/zman-app (`main` @ `bdd63ab`; never modified) |
| Governing in-repo contract | `docs/contracts/28-selective-inventory-tracking-contract.md` |
| Schema / export version | 31 → 32 / 23 → 24 (legacy pair 23/31 accepted; unknown defaults to null, never zero) |
| Test status | **PASS** — full `pnpm check` green; domain 239/239 (20 files); prototype 643/643 (98 files); CI `success`; live browser QA 390×844 with 0 console errors |

---

## 1. Executive summary

Group 2 delivers an understandable, evidence-based catalog and inventory system inside Micro: the owner decides, per material, whether to track quantity or use the material only as a cost input; tracked materials hold a movement-derived position with distinct unknown / confirmed-zero / available / shortage states; purchases stay financial events until an explicit receipt; partial receipts reconcile by caps and state; waste is non-cash and outside the period result; untracking states its consequences and preserves history; and every coupled write is atomic and idempotent.

This delivery is a **recovery delivery**. A previous agent session was interrupted mid-implementation. The resumption agent did not restart: it verified the real repository state, preserved 49 files of valid uncommitted work as a recovery snapshot commit, re-ran every baseline gate before touching anything, completed the outstanding adversarial-review fixes, merged to remote `main` through PR #150 with green CI, and delivered this evidence package. Nothing was duplicated, nothing was discarded, and no claim in this report rests on the interrupted session's own progress messages — every gate was re-executed and re-verified during recovery.

## 2. The interrupted state (what recovery found)

The completion-state gate (recovery prompt §3) produced this recovery map before any edit:

```
Current remote main:            761638b (Group 1 merged via PR #149; no Group 2 commits)
Current local HEAD:             761638b on main, clean except 49 uncommitted files
Previous Group 2 branches:      none (remote agent/group2-financial-truth belongs to the PREVIOUS program)
Uncommitted files:              48 modified + 3 untracked (full phases 0–3 implementation)
Untracked files:                localTransferService.schema32.test.ts,
                                 group2InventorySurfaces.test.tsx,
                                 docs/contracts/28-selective-inventory-tracking-contract.md
Completed scope:                Phases 0–3 (design contract, domain, store/migration,
                                 application services, UI, docs) + SA-5 adversarial review returned
                                 "FIX REQUIRED" + most SA-5 source fixes already landed (F1/F2/F3/R7…)
Incomplete scope:               3 defective dom tests (failing), Finance waste-row dom test missing,
                                 F2 untracked-guard service test missing, Phase E (merge), Phase F (reports)
Broken tests:                   group2InventorySurfaces.test.tsx — 3 of 639 failing
Missing reports:                all six Group 2 deliverables
Next safe action:               safety snapshot → repair tests → re-run gates → merge → deliver
```

Key findings of the gate, each verified against the repository rather than trusted from the worklog:

1. **Group 1 was genuinely complete on remote `main`.** PR #149 was merged (`761638b`), so Group 2 could extend guided financial entry, integrity checks, and the canonical period reader without re-implementing any of it. Group 1 regression tests stayed green throughout.
2. **The interrupted work was real and nearly complete, but uncommitted.** The entire phases 0–3 output existed only as working-tree changes on local `main`. A sandbox crash would have destroyed it. Per recovery prompt §3.8 it was preserved first as commit `811e8ce` on branch `agent/group2-catalog-inventory` before any edit.
3. **The previous session's last verified state was not its last claimed state.** SA-5 (adversarial QA, worklog G2-7) had returned "FIX REQUIRED — 1 MAJOR + 6 MINOR". Most fixes were already implemented in source (marked `SA-5 (F1)`, `SA-5 (F2)`, `SA-5 (F3)` in code comments), but the verification tests written for them were defective and failing: the F1 test expected the wrong money-input format, the F6 test never imported the component it rendered, and the Scenario G test rendered the suggestion sheet without any suggestions. The 633/633 "green" claim in the interrupted worklog was already stale (639 tests, 3 failing) — exactly the class of unverifiable claim the recovery prompt forbids trusting.
4. **No secrets, no stashes, no other recovery branches.** A token scan of the working tree found nothing committable; the snapshot was clean to create.

## 3. What was recovered versus newly implemented

### 3.1 Recovered (preserved from the interrupted session, verified during recovery)

- **Domain layer**: `Material.tracking` and `Material.opening` optional fields; per-material tracked/untracked semantics with absent-field = legacy tracked (no backfill); `MovementCostKnowledge` with the value-zero ⟺ unknown rule; consumption requiring an order **or** a reason; `InventoryShortage` entity with resolution lifecycle; `positionCostKnowledge`; `materialIsTracked` / `materialQuantityKnowledge`; supplier-purchase `materialId` / `expectedQuantityMilli` with revision before-fields and `assertMaterialLink`.
- **Storage and migration**: schema 32 / export 24; new `inventory-shortages` store (contains-guarded upgrade); `commitInventoryWithShortage` three-store atomic commit; shortages carried in `readSnapshot` / `replaceSnapshot` / `emptySnapshot` (IndexedDB + MemoryLocalStore + resetAll); guided-opening import writes `material.opening`.
- **Import/export**: legacy pair 23/31; migration normalizations (tracking/opening null, costKnowledge known, shortages empty, purchase link null); extended `validMaterial` / `validInventoryMovement` / `validInventoryShortage`; import-time fold non-negativity; reversal cost-knowledge mirroring; shortage and purchase-material foreign keys; summary counts.
- **Application services**: guided `openMaterial` branches; `untrackMaterial` / `retrackMaterial` / `confirmMaterialOpening`; `receivePurchase` (tracked guard, material-link enforcement, cumulative value + quantity caps); `consume` (order or reason); `recordShortage` / `consumeWithShortage` (atomic) / `resolveShortage`; waste with unknown-cost; `extractRemainder` (pure-unknown support); `adjust` with zero-unknown increase; `reverse` mirroring costKnowledge; tracked-only `references` with positions; `purchaseReceiptStatus`; `readPeriodWaste`; `readOrderActualMaterialComparison` with cost knowledge; supplier-purchase edit guard versus received value/quantity.
- **Integrity**: MIC-8 «سلامة المخزون والمواد» — FAIL for structural breakage (fold negative, value-zero without unknown, double reversal, duplicate keys), WARN for open shortage or explicit unconfirmed opening, deep link to `/inventory`.
- **UI**: MaterialEditor guided journey with confirm mode (deep route `/inventory/material/:id/confirm`); InventoryMaterials sections, states, untrack dialog, shortage disclosure, «مرتدة موثقًا» marker; InventoryMovementEditor bridge prefill, received-status card, cost question, consume-target question, shortage panel, effect preview; SupplierPurchaseEditor material link, expected quantity, received card, bridge CTA; Finance period waste row; MaterialSheet suggestion chips wired through CostEditor; contract-26 `purchase`/`material` params; router/classifier updates; CSS additions.
- **Docs and tests**: contract 28 (governing); addenda to contracts 09/11/26/27; decision log D-027/028/029; current-state §24; todo and CHANGELOG entries; 7 new domain suites; service, schema-32, dom-surface and MIC-8 test files; text-density PAGES/CAPS entries; public-surface conscious additions.

### 3.2 Newly implemented during recovery (commit `e40da57`)

1. **F1 verification completed** — the bridge deep link now has a passing end-to-end dom test: quantity prefilled `6`, money prefilled `60.00` (the app's money-input convention is always two decimals; the interrupted test's `60` expectation was itself the defect). The prefill logic in `InventoryMovementEditor` (receipt-status effect filling remaining quantity/value once per purchase, never over owner edits) was already in the snapshot and is now proven.
2. **F6 bridge-card test repaired and completed** — the missing `SupplierPurchaseEditor` import was added; the zero-receipt-state assertion corrected from «استُلمت» (which only appears when fully received) to the honest «كمية مستلمة» line; a shared editor harness extracted.
3. **F6 fully-received state test added** — a purchase received in full states «استُلمت قيمة هذا الشراء كاملة.» and hides the bridge CTA: duplicate receipt prevention by state, not by copy.
4. **Scenario G test rewritten through the real surface** — the estimate-suggestions test now renders the real CostEditor over the real `InventoryMaterialService` (only `drafts.get`/`costs.preview` mocked, following the established U-01 harness pattern): chips derive from real overview+movements (last non-reversed receipt price), a chip tap fills name/unit/unit-price/confidence, saving adds the estimate row, and inventory movements and financial events remain untouched — an estimate never consumes stock and never creates cash.
5. **Finance period waste-row dom tests added** (the third promised S13 test): known-cost waste renders `2.50` with «— غير نقدي: لا يخرج كاش ولا يدخل نتيجة الفترة.» and zero financial events; unknown-cost waste renders «قيمة الهدر غير معروفة بعد» and never a confident `0.00`.
6. **SA-5 (F2) service test added** — `extractRemainder` refuses an untracked material («المادة غير متتبَّعة — فعّل متابعتها أولًا قبل إخراج الفاقد.») with zero movements created.
7. **Shortage repeat-safety test added** (closing an SA-5 note) — repeating `consumeWithShortage` with the same operation key returns `reused: true` with the same movement and the same single shortage record; no duplication on double submission or reload.

## 4. Implementation shape (what actually merged)

### 4.1 Domain and movement contracts

Six movement types remain the single source of inventory truth (`opening`, `purchase_receipt`, `consumption`, `waste`, `adjustment`, `reversal`), each carrying material, quantity, date, source type/id where applicable, value with cost-knowledge state, reason/note, and an idempotency `operationKey`. The deliberate domain rule changes are: consumption requires `orderId` **or** `reason`; `valueDeltaMinor === 0` is legal **iff** `costKnowledge === "unknown"` (quantity-zero stays forbidden); reversals mirror value and inherit cost knowledge. The entity chain is:

```
CatalogItem (reference) → SupplierPurchase (cash/payables only)
    → ReceiptMovement (explicit) → InventoryPosition (derived fold)
    → ConsumptionMovement / WasteMovement → Correction/Reversal
    → InventoryShortage (open → resolved) → Resolution
```

Nothing outside this chain writes movements. Greppable guarantee: `createInventoryMovement` / `commitInventory*` are called only from `inventoryMaterialService` and `guidedOpeningImportService`; zero new `createFinancialEvent` call sites exist — an estimate or selection cannot create cash or inventory effects.

### 4.2 Cost model

Micro's existing moving-average-within-material (`consumptionValueMinor`) is kept and documented against Zman's write-time weighted average: Micro stores the derived value on each outbound movement and shows position cost knowledge («معروفة» / «جزئيًا» / «غير معروفة») instead of inventing COGS or a confident zero. Pure-unknown positions consume at a marked zero (Decision-20 still rejects known-value zero consumption), and mixed known+unknown math is round-half-up, fold-conserving, and regression-tested.

### 4.3 Shortage policy (the negative-stock answer)

Micro does not copy Zman's "negative allowed at delivery". The deliberate policy: consumption above availability is **rejected** (the constitution's non-negative fold); the owner is offered either a plain shortage record (`recordShortage`) or the atomic «استهلك المتاح» (consume available + record the shortfall as an open shortage in one idempotent transaction); open shortages are disclosed inside the material row with a resolve action («سجّل الحل») carrying note and date; resolved records stay visible; MIC-8 reports open shortage as WARN (never an unexplained PASS); and reconciliation happens when the missing receipt arrives. The mapping from Zman's negative balance to Micro's shortage record is documented in contract 28 and D-027.

### 4.4 Waste and period reading

Waste is `هدر مخزون — بلا خروج نقد جديد`: a movement with material link, reason, and (where applicable) waste context; it updates the read model, appears as a period row «هدر مخزون هذه الفترة» in Finance's period view beside the period cost list, is excluded from the period result by design, and is correctable through the standard reversal path. Unknown-cost waste displays «قيمة الهدر غير معروفة بعد», never `0.00`.

### 4.5 Untracking with consequences

Disabling tracking opens a dialog stating: current quantity, cost state, that history is never deleted («لا يُحذف شيء»), that the material disappears from receipt/consumption/waste forms, and that re-activation returns the fold as «غير محدد بعد» until re-confirmed (the truth-corrected consequence line — Zman's "balance returns as-is" over-promise was deliberately not copied). Cancel is safe; confirmation is explicit; movements remain readable in history.

## 5. Schema, migration, and compatibility

- `SCHEMA_VERSION` 31 → 32, `EXPORT_VERSION` 23 → 24, bumped in exactly one place; the legacy pair 23/31 remains accepted.
- New `inventory-shortages` object store created with a contains-guarded upgrade (safe no-op on legacy databases).
- Snapshot enumeration (export/import/reset-all) carries shortages in IndexedDB `readSnapshot`/`replaceSnapshot`, `MemoryLocalStore`, and `LocalTransferService.emptySnapshot` — closing the "reset leaks stale shortage records" hole identified by SA-3 (R2).
- Migration normalizations: absent `tracking`/`opening`/`materialId`/`expectedQuantityMilli` → null (never zero, never invented); `costKnowledge` absent → known; shortages absent → empty; reversals inherit cost knowledge. Import validators enforce shortage and purchase-material foreign keys and the fold stays non-negative at import time.
- Round-trip and migration tests: schema-32 round trips for tracked/untracked, activation, receipts (full and partial), waste, corrections, unknown states, and shortage states; schema-31 legacy import tests updated for 24/32.

## 6. Merge and verification evidence

- Branch `agent/group2-catalog-inventory` pushed with a path-scoped credential store (tokens held outside the repositories, never in remote URLs, command text, logs, commits, or reports).
- PR #150 opened with the full scope/verification body.
- **CI run 1 failed at "Audit dependencies"** — the npm registry security-audit endpoint returned HTTP 500 then socket timeouts on GitHub's runner (transient infrastructure failure; no vulnerability existed: local `pnpm audit` reported "No known vulnerabilities found"; lint and check steps were skipped, never run). The token lacks `actions:write`, so re-run was impossible via API; a transparent empty commit `2e8dcab` retriggered the workflow.
- **CI run 2: `checks = success`, `Cloudflare Pages = success`.**
- PR #150 merged (`merge` method) → `main` at `1207a5adc460829322c9e33013e492d3cdb816bd`.
- Post-merge verification: local `main` == `origin/main` == `1207a5a` with a clean working tree; the merged tree `622716ae` is byte-identical to the CI-verified branch tree; domain 239/239 and prototype 643/643 re-run on merged `main`.

## 7. Acceptance scenarios

All fourteen scenarios (A–N) of the program prompt are covered by automated tests, and the load-bearing ones additionally by live browser evidence (§8 and the test-evidence report):

| # | Scenario | Coverage |
|---|---|---|
| A | Untracked material used for cost input without inventory | Service test «Scenario A» + Scenario G dom test (no movement, no event) |
| B | Tracked activation with known opening | Service test «Scenarios B & C» + MaterialEditor dom test + live browser (screenshot 03/04) |
| C | Unknown opening is not zero | Service test («unconfirmed», never zero) + dom test («غير محدد بعد») |
| D | Purchase without receipt leaves inventory unchanged | Service test «Scenario D & E & F» + bridge dom tests + live browser (05) |
| E | Full purchase received via source action → one linked receipt | Service tests + live browser (05→06→07) |
| F | Partial receipt, remaining quantity, safe second receipt | Service tests (caps, reversed excluded) + F1 dom test (remaining prefill 6 / 60.00) + live browser (07: 12.00 من 20.00 · 30 من 50) |
| G | Untracked/estimate material without movement | Scenario G dom test through real CostEditor + MaterialSheet chips |
| H | Deliberate tracked consumption, before/after position | Service test «Scenario H» (reason + idempotency) |
| I | Consumption above known quantity → shortage policy | Service test «Scenario I» (reject → atomic partial+shortage → resolve; repeat-safe) + dom test (shortage panel) |
| J | Waste: non-cash, no duplicate expense, correctable | Service test «Scenario J» + Finance dom tests + live browser (09/10: `2.00 — غير نقدي`) |
| K | Untrack with consequences, cancel, history preserved | Service test «Scenario K» + dom test (four consequences, safe cancel, «فعّل المتابعة») |
| L | Correction preserves original, net result correct | Domain + service reversal tests (cost-knowledge mirror, reversal-not-delete) |
| M | Repeat submission / reload without duplicates | Idempotency tests across consume / receive / waste / extract / consumeWithShortage (repeat returns `reused`) |
| N | Old exports/imports and new round trips | Schema-32 round-trip suite + schema-31 legacy import suite |

Group 1 regression: `group1Surfaces.test.tsx` and the full guided-entry/integrity/canonical-result suites remained green in every run (239 domain + 643 prototype include them).

## 8. Live browser evidence (390×844 RTL, dev build, 0 console errors)

Twelve screenshots in `supporting/` walk the real owner journey end to end: setup → inventory activation and empty state → the guided tracking question («أيوه، تابع الكمية / لا، للتكلفة فقط») → confirmed-branch entry → the saved tracked row → purchase creation with material link and expected quantity → the purchase-detail bridge card with CTA → **the deep-linked receipt editor fully prefilled (quantity 50, value 20.00, material, note, status card — the SA-5 F1 fix live)** → a partial receipt (30 of 50) returning safely to the purchase detail with «قيمة مستلمة: 12.00 من 20.00 د.أ · كمية مستلمة: 30 من 50» → the material position after receipt → the waste editor with its non-cash preview → the Finance period waste row reading exactly «هدر مخزون هذه الفترة | 2.00 — غير نقدي: لا يخرج كاش ولا يدخل نتيجة الفترة.» (weighted-average 24.00/60 m × 5 m = 2.00 JOD) → and the integrity surface after a run, where MIC-8 «سلامة المخزون والمواد» reports سليم («المراجع موصولة، والطيّ غير سالب، ولا نقص مفتوح»). The five-seat shell (`مشروعي الآن | العمل | سجّل | مالي | أدواتي`) is intact in every frame; no horizontal overflow or broken RTL appeared; `agent-browser errors` and console error scan returned empty.

## 9. Limitations and deliberate deferrals

- **Order-to-sale deduction workflow (Group 3)**: only the contract is in place — consumption-with-orderId is the documented deduction primitive; no delivery automation was built (per scope). 
- **Estimate→cost→order deep integration**: Scenario G covers the estimate row; richer estimate surfaces remain with later groups.
- **Known minor (documented, non-blocking)**: effect-preview sentences embed formatted money inside Arabic template literals (bidi-safe by digits, but not `MoneyValue` bdi nodes) — the cards and status surfaces all use `MoneyValue`; the deep-link fallback for an unknown purchase id silently falls back to the first purchase (guarded by the prefill-once rule).
- **CI flake record**: the first CI run failed on npm registry's audit endpoint outage; resolved by retrigger; no code change was involved (commit `2e8dcab` is empty and says so).
- **Snippets/notes library**: permanently out of scope for the whole program (owner decision; unchanged).

## 10. Conclusion

Group 2 is merged to remote `main` (`1207a5a` via PR #150), verified green locally and in CI, exercised in a real browser, and documented in-repo by contract 28 and its addenda. The recovery preserved one hundred percent of the interrupted implementation work, completed the outstanding adversarial-review verification, and added no duplicate features. The inventory system now honors every constitution invariant the program set out: purchases never silently create stock; unknown never silently becomes zero; waste never double-counts as cash; corrections preserve history; and every coupled write is atomic and idempotent.
