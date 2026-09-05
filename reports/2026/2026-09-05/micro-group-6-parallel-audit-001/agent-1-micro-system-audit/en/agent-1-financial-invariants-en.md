# Agent 1 — Financial Invariants Verification

The audit probed the ten product invariants against actual code and adversarial scenarios on `main @ ad9fc13`, then re-verified the affected ones on the audit branch after the fixes. Money terms in the copy are Arabic; evidence cites files and lines at the baseline.

---

## Invariant verification table

| # | Invariant | Verdict | Key evidence |
|---|---|---|---|
| 1 | cash, result, owner money, Amanah, receivables, payables, inventory, assets, loans, deposits, estimates, corrections, reversals, and non-cash effects are distinct | **HOLDS** | 8-column delta table `financial-event/policies.ts:271-302` (e.g. `amanah_held_cash [1,0,0,0,1,0,0,0]`, `asset_depreciation [0,0,0,0,0,-1,0,0]`, `loan_outgoing_cash [-1,0,0,0,0,0,1,0]`); order fields separate deposit/collected/receivable/revenue/cost (`craft-order/types.ts:153-161`); cash-continuity never classifies (`cash-continuity/types.ts:1`); owner movements carry 4 independent deltas (`owner-entitlement/types.ts:116-119`); post-hoc MIC-16 (`integrityCheckService.ts:1049-1081`) |
| 2 | unknown ≠ zero | **HOLDS** | material opening «unconfirmed» preserved (`inventory-material/policies.ts:59-63, 76-79`); wallet «unknown» shows «غير محدد» (`cash-continuity/types.ts:18-19`); direct-sale `costMinor null ⇒ profitMinor null` (`direct-sale/policies.ts:78`); final profit blocked without known cost (`craft-order/policies.ts:426-437`); G5 declares gaps (`g5/policies.ts:405-409`); MIC-9 enforces result-null ⇔ unknown-cost (`integrityCheckService.ts:526-539`) |
| 3 | estimates create zero actual events | **HOLDS** | `costEstimateService.ts:2-3, 90-118` — writes only the estimate store; header contract states it verbatim |
| 4 | drafts create zero financial events | **HOLDS** | draft orders carry no cash/revenue effect (`craft-order/policies.ts:352-375`); deposit collected only at agreement recording (`agreementService.ts:133-134`); form drafts live in a separate store excluded from snapshot; revenue recognized exactly once at delivery (`craft-order/policies.ts:423-439`) |
| 5 | reversal negates, never doubles | **HOLDS at the ledger; attribution was P1 (fixed)** | every delta negated (`financial-event/policies.ts:412-419`); double-reversal rejected at domain (`:395-396`), app (`projectFinancialService.ts:906-912`), and storage (`IndexedDbLocalStore.ts:1294-1312`); inventory mirrors single-shot (`inventoryMaterialService.ts:1155-1196`); MIC-2 verifies mirror equality (`integrityCheckService.ts:290-300`). Attribution defect FT-01 fixed: revenue re-recognition now lands in the re-delivery period |
| 6 | deposit is not revenue without explicit classification | **HOLDS** | `deposit_retained_*` rows carry no cash and only owner-capital/revenue layers (`financial-event/policies.ts:298-301`); retention leaves decision pending (`craft-order/policies.ts:874-884`); classification requires an explicit documented decision (`:987-1016` + `retainedDepositService.ts:84-122`); pending deposits surfaced (`projectFinancialService.ts:410-417`); MIC-12 cross-checks (`integrityCheckService.ts:862-877`) |
| 7 | inventory movement: one source, one idempotency identity | **HOLDS (hardening gap documented)** | every writer checks `operationKey` first (`inventoryMaterialService.ts:730, 820, 1045, 1096, 1159`); receipts require `purchaseId` (`inventory-material/policies.ts:137-138`); MIC-8 flags duplicate keys/dangling refs (`integrityCheckService.ts:604-650`). Multi-source exclusivity not structurally enforced (FT-10, P3) |
| 8 | partial receipt cannot exceed ordered quantity | **HOLDS** | quantity cap vs `expectedQuantityMilli` and value cap vs `totalMinor`, both computed from **active** receipts (`inventoryMaterialService.ts:757-786`); same on edit (`supplierPurchaseService.ts:210-236`); parallel caps for payments, loan repayments, payable settlements, order collections |
| 9 | wallet deltas reconcile with cash movement | **HOLDS after FT-02 fix** | `recordedCashMinor = unallocated + wallet` by construction (`projectFinancialService.ts:385-421`); expense-with-wallet writes a matching negative allocation; owner movements commit movement + cash entry atomically (`ownerEntitlementService.ts:865-877` + `commitOwnerMovement:2215`); compound collection reversal reverses the matching allocation atomically (`collectionReversalService.ts:300-345`). Fixed: direct-sale cancel now mirrors allocation reversals |
| 10 | asset and loan contexts survive edit, restore, reversal, import | **HOLDS at event level; record level was P1 (fixed)** | editEvent/restoreEvent carry contexts (`projectFinancialService.ts:1089-1093, 1173-1176`); domain reversal copies contexts (`financial-event/policies.ts:420-422`); import requires contexts for family types and re-derives delta columns (`localTransferService.ts:534-605`). Fixed: family events corrected only via owner records (FT-03); MIC-11 recognizes loan restores |

---

## Adversarial scenarios executed (fresh data, on the audit branch)

| Scenario | Method | Result |
|---|---|---|
| Double submit (same idempotency key) | service-level reruns (`directSaleService`, lock enable) + existing 277-test suite incl. duplicate-write prevention | reused honestly; no double effect |
| Double reversal | domain + app + storage guards; import rejects reverse-of-reverse | rejected at every layer |
| Reversal after re-delivery | new `projectFinancialService.redelivery.test.ts` | revenue attributed to the effective (second) delivery period — FT-01 regression |
| Cancel after wallet attribution | new `directSaleService` tests | mirror reversal written; wallet sum returns to zero; repeated cancel idempotent — FT-02 regression |
| Family-event general correction | new `EventsLayer.familyGuard.dom.test.tsx` | owner deep-link shown; general reverse/edit/delete absent — FT-03 regression |
| Wrong PIN brute force (rapid retries) | new lock-service tests | enforced backoff window; counter not inflated by in-window retries |
| Legacy lock record (old hash format) | new lock-service test | unlocks via legacy path, transparently upgrades to PBKDF2 — no lockout |
| Arabic-Indic PIN entry | new dom test | ٤١٧٩ ⇒ "4179", unlocks |
| Locked device → `/settings` export | new dom tests | PIN gate blocks export until proof; session proof holds; disabled lock ⇒ no gate |
| Tampered backup (digest mismatch) | existing envelope27 suite | rejected, store untouched |
| Hand-merged backup (counts mismatch, digest still valid) | new envelope27 test | rejected — DP-01 regression |
| Corrupted integrity block (unknown algorithm) | new envelope27 test | rejected — DP-09 regression |
| Malformed values (NaN/∞/negative/overflow/>2dp) | `shared` numeric guards + import validators (existing suite) | rejected at construction; import re-validates types |
| Invalid IDs / dangling links | existing schema32/34 + integrity tests | rejected with store untouched |
| Interrupted saves (partial writes) | IDB atomic transactions + orphan-free failure tests (existing) | no partial state; migration cursor-error aborts upgrade without partial writes |
| Duplicate import (same file twice) | replace-semantics + duplicate-key validation (existing) | idempotent |
| Boundary quantities (partial receipt == / > ordered) | existing A-02 quota tests + guards | over-receipt rejected; caps from active receipts only |
| Concurrent reversal attempts | existing `Promise.all` test | single reversal wins, second rejected |
| Future-dated events | not guarded (AR-08, P3 documented) | accepted by design today — documented |

## Product shell invariant (five seats)

Verified structurally and by the navigation test: exactly one bottom bar with five seats (مشروعي الآن | العمل | سجّل FAB | مالي | أدواتي), one FAB (the middle seat), no sixth seat, no competing bar (`BottomNav.tsx`, `app/navigation.ts:13-18`, `navigation.test.ts:7-12`; route classifier hides chrome on deep editors by design). JOD amounts render with two decimals through a single formatter; dates are numeric DD/MM/YYYY; formatters are guard-tested.

## Two product-decision findings (owner must decide; not defects)

- **FT-04 cross-period reversal policy:** operating expenses are period-attributed (reversal credits its own month), while group-4 events (depreciation/write-off/disposal/deposit revenue) vanish from both periods once reversed, and G5 never credits the reversal window — the same month can read differently across surfaces for cross-period reversals. Unifying changes reported numbers.
- **FT-05 known waste:** disclosed in the period reader but never expensed in `resultMinor` (while write-offs are). Either subtract waste or prompt an explicit `loss_non_cash` record — asymmetry documented.
