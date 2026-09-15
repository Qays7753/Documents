# 04 — Financial Workflow and Deferred Items

All items below are implemented in the merged PR #158 and verified by the green suites (285 domain + 835 prototype tests). None of the approved decisions was reopened or reinterpreted.

## 1. Deferred items — closed with evidence

### FC-06 / Conflict E — deposit settlement, source-wallet refund, mandatory preview (commit `c502b6b`)

| Requirement | Implementation | Evidence |
| --- | --- | --- |
| Refund follows the source wallet or current effective manual allocation, shown before confirmation | `retainedDepositService.ts` + `fulfillmentService.ts` refund path mirrors the wallet-allocation reversal atomically with the order update | `fulfillmentService.test.ts`: «refunds from the attributed wallet — the allocation is reversed by the refunded amount, atomically with the order» |
| Partial refund: remainder stays honestly pending; full refund closes the settlement | Domain `settleDeposit` — `depositSettlement`/`settlementStatus` only close when nothing remains pending | «refunds partially — partial allocation reversal, remainder pending, second refund completes»; craft-order domain tests (partial settlement describe) |
| Mandatory numeric impact preview (pending amount, documented cost, actually consumed = 0 pre-delivery, proposal, cash/profit/owner effects) | `OrderDetail.tsx` settlement panel `deposit-settlement-preview` with explicit dt/dd values | `G4RetainedDeposit.dom.test.tsx`: «shows the mandatory settlement impact preview and supports a partial refund that keeps the remainder pending» |
| Explicit classification as project income / owner money (not profit), never auto-classification | `classifyRetainedDeposit`/`reclassifyRetainedDeposit` with explicit amounts; mixed meaning surfaced | «classifies as revenue once: recognized in events, no new cash, no double count»; «reclassifies to owner money through a documented correction»; domain «partial classification and mixed meaning» |
| Retained proposal based on documented cost, adjustable with warning and reason | Cover proposal = `min(pending, documentedCost)` displayed; amount input adjustable | Preview test above; proposal fields verified |

### AV-07 / Conflict F — cancellation from needs_review (commit `c45c95c`)

| Requirement | Implementation | Evidence |
| --- | --- | --- |
| Cancellation available where it can complete safely, including needs_review when the state allows | `preDeliveryStatuses` gate extended; `nextAction` promise «ألغِ موثقًا» now backed by a real path | `G3.dom.test.tsx`: «offers cancellation from needs_review with a mandatory impact preview and completes safely» |
| Mandatory impact preview; honest block if a complete safe reversal is impossible; no silent partial cancel | Preview rendered before reason buttons; service-level guards unchanged | Same test + domain cancel guards |

### AV-08 / Conflict G — depreciation/disposal separation (commit `23972aa`)

| Requirement | Implementation | Evidence |
| --- | --- | --- |
| Depreciation to zero does not dispose/write off; asset stays owned, usable, book value zero | Asset lifecycle keeps status active; only disposal/archive freezes the ledger | `assetService.test.ts`: «proposes depreciation and records it as a non-cash event exactly once» |
| No depreciation/acquisition reversal after disposal/write-off (would resurrect a voided book value) | `assetService.ts` guards; `AssetDetail.tsx` hides the actions | «blocks depreciation reversal after disposal — archived book value stays frozen»; «rejects a no-change acquisition correction instead of churning history» |
| Documented pre-disposal error correction remains available while the asset is active | Guard scoped to archived/disposed assets only | «reverses a depreciation entry with a documented correction and no cash movement» |

### AV-09 / Conflict I — corrupted draft restoration (commit `7619f57`)

| Requirement | Implementation | Evidence |
| --- | --- | --- |
| Defensive coercion for `FinancialEventEditor` localStorage draft restoration; corrupted drafts must not break the form or produce unsafe values | Restoration path applies the same coercion discipline as the other editors | `FinancialEventEditor.guided.test.tsx`: «restores a corrupted draft through defensive coercion — form stays functional and safe»; «silently ignores a draft with nothing recoverable (garbage fields only)» |

### WF-04 / Conflict H — post-save expense classification correction (commit `9e6a340`)

| Requirement | Implementation | Evidence |
| --- | --- | --- |
| Classification corrected after save through the same user edit flow + internal atomic reverse-and-replace (reason, history, affected period, linked records) | «تعديل العملية» on expense events opens the classification form prefilled from the current context; the replacement carries the new classification while original + reversal keep the old one | `projectFinancialService.category.test.ts`: «replaces the classification on the atomic replacement while the original and reversal keep the old one»; «rejects classification correction on a non-expense event»; EventsLayer DOM tests |
| Affected-period information | FC-03 cross-month warning fires when the new date falls in a different month | `D005.dom.test.tsx` edit flow (period warning test from PR #156, still green) |

## 2. Approved conflicts — implementation summary

| Conflict | Behavior | Key code | Test evidence |
| --- | --- | --- | --- |
| **A / FC-02** — simple actions over the atomic engine | User sees «تعديل العملية»، «حذف العملية»، «إلغاء العملية»، «التراجع عن التصحيح»; internally only Atomic Reverse-and-Replace (original preserved, reversal+replacement linked and atomic, reason required, double-reversal prevented, plain-Arabic impact preview). **No second literal in-place mutation engine.** | `EventsLayer.tsx` actions + previews; `projectFinancialService.ts` `reverseEvent`/`editEvent`/`restoreEvent`; `IndexedDbLocalStore.commitFinancialEventCorrection` | `D005.dom.test.tsx` (edit/delete/restore flows + idempotent double-submit), `EventsLayer.familyGuard.dom.test.tsx`, `U001.dom.test.tsx` |
| **B** — optional party / order name | Optional order name (display label over the work item), optional free-text party name, optional saved party (repeated names), system order ID. One-time name stays local; repeated (2+ records) becomes a choosable party. Unnamed receivable allowed with a visible warning; naming is one-way from the order page. No blocking of cash orders/deposits/delivery. | `craft-order/policies.ts` (orderName/customerName), `OrderDetail.tsx` assign-party panel, `AgreementEditor.tsx`/`DraftEditor.tsx` fields, `partyLedgerService.ts` repeated-party lookup, `collectionService.ts` unnamed qualifier | `G3.dom.test.tsx` «names an unnamed order party once from the order page»; `agreementService.test.ts`; domain craft-order «optional party and one-way naming» |
| **C** — sale recognized at delivery only | Order creation, confirmation, deposit collection create no revenue. At delivery: full sale recognized exactly once, deposit applied once within it, remainder is receivable or collected; later collection is cash-only. | `craft-order` state machine (`recognizedRevenueMinor`), `deliveryReviewService.commitDelivery` | `deliveryReviewService.test.ts` «sale recognition at delivery only (Conflict C/D)» — the literal 100/20/80 contract example: one 100.00 sale, 20.00 deposit applied once, 80.00 remainder, later collection cash-only, zero revenue financial events |
| **D** — deposit meaning | Pre-delivery: liquidity linked to the order and selected wallet — not revenue, not profit, not a completed sale. Order linkage mandatory; party linkage optional. | Deposit fields on `CraftOrder`; wallet attribution at collection | Same Conflict C/D test (pre-delivery assertions: `recognizedRevenueMinor: 0`, `collectedMinor: 2000`); `fulfillmentService.test.ts` deposit guards («refuses a deposit beyond the agreed price and on delivered orders») |
| **E** — cancelled deposit choices | Never auto-classified; mandatory preview; full/partial refund, pending retention, actual-cost coverage, explicit project income, explicit owner money (not profit — no cash movement until an actual withdrawal); source wallet preserved; adjustable proposal with warning and reason | See FC-06 above | See FC-06 above |
| **F** — needs_review cancellation | See AV-07 above | See AV-07 | See AV-07 |
| **G** — depreciation | See AV-08 above | See AV-08 | See AV-08 |
| **H** — classification correction | See WF-04 above | See WF-04 | See WF-04 |
| **I** — draft restoration | See AV-09 above | See AV-09 | See AV-09 |

## 3. Previously approved behavior — regression-verified (not reimplemented)

The PR #156 baseline behavior was preserved and re-verified by the full suite: waste profit-impact choice (FC-01), tracked/untracked inventory behavior (contract 28), explicit negative-stock warning, unknown-not-zero rule («ما بعرف» states), loan-to-party linking, idempotency keys, backup integrity (AV-04 envelope + counts), local-first/offline PWA, Arabic RTL with English digits and `DD/MM/YYYY` numeric dates.

## 4. No second financial truth engine

Conflict A's prohibition was respected: all corrections flow through the single atomic engine. The Conflict C/D test additionally asserts **zero revenue-carrying financial events** after the full lifecycle (order-level `recognizedRevenueMinor` is the single revenue truth), closing the "second engine" risk explicitly.
