# 03 — End-to-End User Journeys

Analysis baseline: Micro `main` @ `4af025d38f04dfb36ee645a4f9ca3345e362bf5b` (2026-09-06T13:21:03+03:00). 53 journeys, 192 documented steps. Every journey carries evidence (repository paths, line references, test names) and a status from the fixed vocabulary. Planned/conceptual journeys are marked and never presented as implemented.


## Group — A — Getting started


### FLW-001 — First entry and orientation (setup wizard)

> Arabic: الدخول الأول والتأسيس · Status: **IMPLEMENTED**

- **Journey name:** First entry and orientation (setup wizard) — الدخول الأول والتأسيس
- **Actor:** ACT-01
- **User intention:** Start using Micro on a new device with an honest, minimal first-run experience.
- **Entry points:** StartupGate redirect when no profile exists; Settings → ابدأ من جديد (reset)
- **Success outcome:** Activity profile + first wallet with declared or unknown opening saved; app enters Foundation/Home.
- **Primary path:** Boot → StartupGate redirects to /setup → 3-step wizard (activity name → wallet name + opening known/unknown/zero) → save → /foundation.
- **Alternative paths:** Skip wallet (F-002: never asks again, discards); staged setup draft restored from localStorage (micro.setup-draft.v1); emergency re-entry via /settings without lock.
- **Failure / exception paths:** IndexedDB unavailable → honest storage recovery screen with retry (StartupGate.tsx:53-89); second window open → storage_blocked message; wizard draft version mismatch → ignored safely.
- **Screens:** SCR-SETUP, SCR-FOUNDATION, SCR-STARTUP-GATE
- **Services:** SVC-PROFILE, SVC-CASH-CONTINUITY, SVC-OWNER-PROFILE
- **Entities:** ENT-PROFILE, ENT-CASH-WALLET, ENT-CASH-ENTRY, ENT-OWNER-PROFILE
- **Before state:** No profile, no stores; app locked out of surfaces by StartupGate.
- **After state:** Profile present; wallet with declared opening (or 'unknown' stamp, never zero); owner identity ensured (ensureLocal).
- **Financial effect:** Opening balance is a declared snapshot of cash — not sales, not owner capital classification.
- **Cashbox / wallet effect:** Wallet cash + openingMinor (or unknown).
- **Profit / cost effect:** None.
- **Inventory effect:** None.
- **Debt / deposit effect:** None.
- **Offline / sync behavior:** Fully local; no network required at any step.
- **Permissions / approval:** No lock exists yet on first run; /setup and /settings are lock-exempt 'emergency' routes forever.
- **History / audit behavior:** Opening entry written to wallet ledger with operation key; setup draft persisted locally only.
- **Exit & next action:** Foundation page proposes cash/owner/supplier/material entries or تخطَّ وأكمل لاحقًا → Home.
- **Evidence:** pages/Setup.tsx (3 steps, micro.setup-draft.v1); app/StartupGate.tsx:45-67; pages/Setup.ui.test.tsx (wallet-skip path F-002); app/StartupGate.recovery.test.ts
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | System action | ACT-06 | Boot check: no activity profile — فحص الملف المحلي | SCR-STARTUP-GATE | SVC-PROFILE | StartupGate loads profile once per session (S5-09); redirects replace→/setup unless on /setup or /settings. |
| 2 | User action | ACT-01 | Enter activity name — اكتب اسم نشاطك | SCR-SETUP | SVC-PROFILE | Draft saved to localStorage on first input; name is the only identity required. |
| 3 | User action | ACT-01 | Name wallet + choose opening: known / unknown / zero — سمِّ محفظتك واختر حالة الرصيد | SCR-SETUP | SVC-CASH-CONTINUITY | Unknown opening shows «غير محدد» — never silently zero. |
| 4 | Decision | ACT-01 | Opening knowledge decision — رصيد معروف أم غير محدد؟ | SCR-SETUP | SVC-CASH-CONTINUITY | Known → declared opening entry; unknown → stamp, completable later via /cash/wallet/:id/opening-later (PA-007). |
| 5 | Persistence write | ACT-06 | Persist profile + wallet atomically — حفظ الملف والمحفظة | — | SVC-CASH-CONTINUITY | IndexedDb stores activity-profile, cash-wallets, cash-continuity-entries. |
| 6 | System action | ACT-06 | Redirect to /foundation — توجيه إلى صفحة الأساس | SCR-FOUNDATION | — | Finish → /foundation (replace); Foundation offers cash/owner/supplier/material one-time entries. |


### FLW-002 — Foundation: declare what you have right now

> Arabic: صفحة الأساس — شو عندك هلق؟ · Status: **IMPLEMENTED**

- **Journey name:** Foundation: declare what you have right now — صفحة الأساس — شو عندك هلق؟
- **Actor:** ACT-01
- **User intention:** Record the true starting position (cash, owner investment, supplier debts, materials) or skip pieces explicitly.
- **Entry points:** /foundation after setup; Home → «مشروعي الآن» foundation link; Home financial fact card source
- **Success outcome:** Each foundation topic either has a recorded opening or an honest one-line state; entering the app leaves nothing silently zero.
- **Primary path:** /foundation → per-topic entries: محفظة ورصيد بداية / سجل استثمارًا نقديًا / رصيد سابق لحق المالك / سجل التزامًا لمورد / شراء مواد قائم → ادخل إلى مشروعي.
- **Alternative paths:** تخطَّ وأكمل لاحقًا (skip with honest state); guided opening import via /settings?focus=guided-import&from=/foundation.
- **Failure / exception paths:** Storage errors surface as inline Arabic notices with retry; every section is independently skippable.
- **Screens:** SCR-FOUNDATION
- **Services:** SVC-CASH-CONTINUITY, SVC-PROJECT-FINANCE, SVC-OWNER-ENTITLEMENT, SVC-SUPPLIER-PURCHASE, SVC-INVENTORY
- **Entities:** ENT-CASH-WALLET, ENT-FINANCIAL-EVENT, ENT-SUPPLIER-PURCHASE, ENT-MATERIAL
- **Before state:** Fresh or partially-declared project.
- **After state:** Optional declared opening facts; unknowns remain 'unavailable', never zero.
- **Financial effect:** Owner investment event (ownerCapital +cash) or supplier payable or wallet opening — each is its own money layer.
- **Cashbox / wallet effect:** Cash + for wallet opening / owner investment.
- **Profit / cost effect:** None (capital ≠ revenue).
- **Inventory effect:** Materials may be declared with opening knowledge.
- **Debt / deposit effect:** Supplier payable may be declared (payable +).
- **Offline / sync behavior:** Local only.
- **Permissions / approval:** None beyond owner.
- **History / audit behavior:** Events carry idempotency keys; foundation page is permanently reachable (owner decision: foundation permanently accessible).
- **Exit & next action:** ادخل إلى مشروعي → Home control center.
- **Evidence:** pages/Foundation.tsx (labels 108-240); pages/Foundation.ui.test.tsx (owner decisions 4-8: collapsible sections, honest one-line states)
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Open foundation page — افتح صفحة الأساس | SCR-FOUNDATION | — | Shows current foundation status per topic: cash/owner/suppliers/materials. |
| 2 | Decision | ACT-01 | Choose a topic to declare or skip — شو عندك هلق؟ | SCR-FOUNDATION | — | Each topic deep-links to its entry surface with ?from=/foundation. |
| 3 | User action | ACT-01 | Record cash / owner investment / supplier debt / materials — سجّل استثمارًا أو التزامًا أو مواد | — | SVC-PROJECT-FINANCE | Each entry writes its own money layer atomically. |
| 4 | User action | ACT-01 | Skip topics explicitly — تخطَّ وأكمل لاحقًا | SCR-FOUNDATION | — | Skipped topics keep honest 'unavailable' states in Home facts. |
| 5 | User action | ACT-01 | Enter the project — ادخل إلى مشروعي | SCR-HOME | — | Returns to Home; foundation stays reachable later. |


### FLW-003 — Understanding the current financial position

> Arabic: فهم الوضع المالي الحالي · Status: **IMPLEMENTED**

- **Journey name:** Understanding the current financial position — فهم الوضع المالي الحالي
- **Actor:** ACT-01
- **User intention:** Answer 'what do I own / owe / have in cash right now?' with sourced, knowledge-honest numbers.
- **Entry points:** Bottom tab «مشروعي الآن» (/); Bottom tab «مالي» (/finance); Finance → cards
- **Success outcome:** Four financial facts (recorded cash, customer receivables, supplier payables, owner capital) each with value + source + period + knowledge; unallocated cash visible separately.
- **Primary path:** Home → financial fact cards (cash/receivables/payables/owner capital/unallocated) → راجعها deep-links to the source record.
- **Alternative paths:** Finance hub → cash card + period result + G5 + owner money; /finance/activity for every record; statement for a period view.
- **Failure / exception paths:** Not-initialized modules show not_initialized state (not zero); storage failure → retry notice.
- **Screens:** SCR-HOME, SCR-FINANCE, SCR-FINANCE-ACTIVITY
- **Services:** SVC-HOME-CONTROL, SVC-PROJECT-FINANCE, SVC-FINANCIAL-PULSE, SVC-STATEMENT
- **Entities:** ENT-FINANCIAL-EVENT, ENT-CRAFT-ORDER, ENT-DIRECT-SALE, ENT-SUPPLIER-PURCHASE, ENT-CASH-WALLET, ENT-OWNER-MOVEMENT
- **Before state:** Any state with recorded history.
- **After state:** Read-only; no mutation.
- **Financial effect:** None (derived reading: readPosition).
- **Cashbox / wallet effect:** Reports recordedCash = unallocated + wallet cash.
- **Profit / cost effect:** None here (period result is a separate surface).
- **Inventory effect:** None.
- **Debt / deposit effect:** Reports registered debts + direct-sale debts and supplier payables.
- **Offline / sync behavior:** Local read; cross-tab freshness via BroadcastChannel dataVersion bump.
- **Permissions / approval:** Owner only.
- **History / audit behavior:** Every number links to its source (fact.source deep link).
- **Exit & next action:** Deep link into the record that produced the number.
- **Evidence:** application/finance/projectFinancialService.ts:340-442 (readPosition); application/home/homeControlCenterService.ts; docs/decisions/home-control-center-h01a-decision-v1.md (H01-A: exactly four facts)
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Open Home tab — افتح «مشروعي الآن» | SCR-HOME | SVC-HOME-CONTROL | Control center: activity name, local date, priority, four financial facts. |
| 2 | System action | ACT-06 | Compose position from all stores — اجمع الوضع من كل المخازن | — | SVC-PROJECT-FINANCE | readPosition: unallocated + wallet cash, receivables, payables, owner capital, amanah, assets, loans, pending retained deposits. |
| 3 | User action | ACT-01 | Tap a fact to open its source — راجعها | — | — | Each fact card carries source deep link + knowledge state (known/incomplete/not_initialized). |
| 4 | User action | ACT-01 | Open full activity feed — افتح السجل الكامل | SCR-FINANCE-ACTIVITY | SVC-ACTIVITY | Every registered record with effect word + source link, family/period filters. |


### FLW-004 — Guided opening import (G8.2)

> Arabic: الاستيراد الافتتاحي الموجّه · Status: **IMPLEMENTED**

- **Journey name:** Guided opening import (G8.2) — الاستيراد الافتتاحي الموجّه
- **Actor:** ACT-01
- **User intention:** Import an explicit opening-position JSON file (profile, wallets, materials) instead of typing first balances.
- **Entry points:** Foundation → الإعدادات with focus=guided-import; Settings → اختيار ملف البداية
- **Success outcome:** Preview → confirm → atomic snapshot replace; per-record idempotent re-import returns reused:true.
- **Primary path:** Choose file → prepare (validate) → preview with counts → confirm → single atomic replaceSnapshot.
- **Alternative paths:** Re-import same importId → per-record idempotency (createdOperationKey guided-opening:{importId}:{kind}:{id}).
- **Failure / exception paths:** non_empty_store rejection if local data exists (re-checked at confirm); wrong format/version/importId; zero-or-positive rule violations; rejected Excel/CSV/history files.
- **Screens:** SCR-SETTINGS, SCR-FOUNDATION
- **Services:** SVC-GUIDED-IMPORT
- **Entities:** ENT-EXPORT-FILE, ENT-CASH-WALLET, ENT-MATERIAL
- **Before state:** Empty local store.
- **After state:** Opening position recorded with knowledge grades; no orders, no revenue, no COGS created.
- **Financial effect:** Opening balances only; honest warning: import fixes an opening position, does not create sales/profit/history.
- **Cashbox / wallet effect:** Wallet opening entries with knowledge known|estimated.
- **Profit / cost effect:** None.
- **Inventory effect:** Materials with opening quantity/value knowledge.
- **Debt / deposit effect:** None (no unknown-source debts accepted).
- **Offline / sync behavior:** Local file; no network.
- **Permissions / approval:** Import confirmation is PIN-gated per session when lock enabled (DataActionPinGate).
- **History / audit behavior:** Idempotency keys per record; operation keys traceable.
- **Exit & next action:** Integrity check offered after import (deep link /tools/integrity).
- **Evidence:** application/transfers/guidedOpeningImportService.ts:209-358; docs/contracts/21-guided-opening-import-prototype-contract.md; docs/fixtures/g82-guided-opening-import-fixtures.json
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Choose opening file — اختر ملف البداية | SCR-SETTINGS | SVC-GUIDED-IMPORT | JSON only; format micro-guided-opening-import v1. |
| 2 | System action | ACT-06 | Validate + build preview — تحقق وابنِ المعاينة | — | SVC-GUIDED-IMPORT | Rejects non-empty store, bad ids, negative amounts; knowledge ladder per value. |
| 3 | User action | ACT-01 | Confirm import — أكّد الاستيراد | SCR-SETTINGS | SVC-GUIDED-IMPORT | Re-checks emptiness at confirm; single atomic replace. |
| 4 | Persistence write | ACT-06 | Atomic snapshot replace — استبدال ذري للمخزن | — | SVC-GUIDED-IMPORT | Domain factories create wallet/opening/material/movement records. |


## Group — B — Sales & orders


### FLW-005 — Quick direct cash sale (FAB)

> Arabic: تسجيل بيع مباشر سريع · Status: **IMPLEMENTED**

- **Journey name:** Quick direct cash sale (FAB) — تسجيل بيع مباشر سريع
- **Actor:** ACT-01
- **User intention:** Save a direct sale in seconds without creating an order.
- **Entry points:** FAB «سجّل» → تسجيل بيع (available on every surface route)
- **Success outcome:** Sale recorded; receipt («وصل التسجيل») with افتح السجل deep link; money attributed to a chosen wallet.
- **Primary path:** FAB → sale form in sheet (item, amount, qty, cost known toggle, wallet) → سجّل البيع → receipt.
- **Alternative paths:** Credit sale «بيع آجل» in the same sheet (collected < revenue → partial_debt or partial_needs_review); full editor /direct-sales/new for more fields; catalog product → sell button pre-fills.
- **Failure / exception paths:** Empty amount blocked; discard guard when numbers typed («في رقم مكتوب — تسجّله أو تتجاهله؟»); storage error → honest notice, nothing written; double tap → idempotent by key (reused).
- **Screens:** SCR-QUICK-ACTION
- **Services:** SVC-DIRECT-SALE, SVC-CASH-CONTINUITY
- **Entities:** ENT-DIRECT-SALE, ENT-CASH-ENTRY
- **Before state:** Any state.
- **After state:** Active direct sale; revenue recognized at sale date; wallet allocation (or unallocated if attribution fails — money never lost).
- **Financial effect:** Revenue at occurredOn; profit null if cost unknown (never fake); collected cash attribution.
- **Cashbox / wallet effect:** Cash + (allocation with sourceRefKind 'sale' or unallocated).
- **Profit / cost effect:** profitMinor = revenue − cost only when cost known.
- **Inventory effect:** Optional later consumption via /inventory/movement/consume?sale=<id>.
- **Debt / deposit effect:** Credit remainder becomes direct-sale debt (collectionStatus).
- **Offline / sync behavior:** Local write; works fully offline.
- **Permissions / approval:** Owner only.
- **History / audit behavior:** Idempotency key unique index in store; revisions recorded on later edits.
- **Exit & next action:** Receipt → افتح السجل (/direct-sales/:id) → سجّل استهلاك مواد لهذا البيع.
- **Evidence:** components/layout/QuickActionSheet.tsx:52-78, 315, 384; application/direct-sales/directSaleService.ts; application/reentrancyGuards.test.ts (duplicate record guard)
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Tap FAB سجّل — اضغط «سجّل» | SCR-QUICK-ACTION | — | 5 quick actions: sale, expense, order, estimate, collection (decision 23-b daily-repeat actions). |
| 2 | User action | ACT-01 | Fill in-sheet sale form — املأ البيع في الورقة | SCR-QUICK-ACTION | SVC-DIRECT-SALE | Item (default «بيع نقدي» if empty), amount, qty, cost known toggle, wallet choice, credit option. |
| 3 | Decision | ACT-01 | Cost known? (لا أعرف الآن) — أعرف التكلفة؟ | SCR-QUICK-ACTION | SVC-DIRECT-SALE | Unknown cost preserved as null — profit shows «غير متاح», never zero. |
| 4 | User action | ACT-01 | Record sale — سجّل البيع | SCR-QUICK-ACTION | SVC-DIRECT-SALE | Busy state «جارٍ التسجيل…»; idempotent write + wallet allocation. |
| 5 | System action | ACT-06 | Show receipt — أظهر وصل التسجيل | SCR-QUICK-ACTION | — | وصل التسجيل with افتح السجل + تم; links to /direct-sales/:id. |


### FLW-006 — Direct sale — full editor (credit, catalog prefill)

> Arabic: محرر البيع المباشر الكامل · Status: **IMPLEMENTED**

- **Journey name:** Direct sale — full editor (credit, catalog prefill) — محرر البيع المباشر الكامل
- **Actor:** ACT-01
- **User intention:** Record a richer direct sale: catalog product, quantity, partial collection now, or correct an existing one.
- **Entry points:** /direct-sales/new?product=<catalogId> (Catalog sell button); /direct-sales/:id (from receipt/activity)
- **Success outcome:** Sale saved with honest collection status; receipt flow returns to source.
- **Primary path:** Catalog → sell → /direct-sales/new?product=... prefilled suggestions → record → receipt → افتح السجل.
- **Alternative paths:** Open an existing sale → correct (edit revision with optimistic concurrency); price cut (X-06: خفّضتُ السعر); cancel.
- **Failure / exception paths:** Over-collection blocked (collected ≤ revenue); concurrent edit from another window → honest conflict message (expectedRevisionCount); unsaved-input guard on back.
- **Screens:** SCR-DIRECT-SALE-EDITOR, SCR-CATALOG
- **Services:** SVC-DIRECT-SALE, SVC-CATALOG, SVC-CASH-CONTINUITY
- **Entities:** ENT-DIRECT-SALE, ENT-CATALOG-ITEM, ENT-CASH-ENTRY
- **Before state:** Any.
- **After state:** Active/corrected sale with revisions history.
- **Financial effect:** Same as quick sale; corrections keep beforeRevenueMinor in revision record.
- **Cashbox / wallet effect:** Collection attribution at record and later collections.
- **Profit / cost effect:** Unknown cost → null profit; price cut drops revenue to collected.
- **Inventory effect:** Optional consumption link.
- **Debt / deposit effect:** partial_debt remainder collectable later.
- **Offline / sync behavior:** Local.
- **Permissions / approval:** Owner.
- **History / audit behavior:** Revisions array (edit/cancel/price_cut) with before-values.
- **Exit & next action:** Receipt → record consumption or return to referrer.
- **Evidence:** pages/DirectSaleEditor.tsx (labels 517-531); pages/DirectSaleEditor.ui.test.tsx; src/domain/direct-sale/policies.ts (X-06 price cut)
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Sell from catalog — اضغط «بِع» من الكتالوج | SCR-CATALOG | SVC-CATALOG | ?product prefill: defaults are proposals only (P-002). |
| 2 | User action | ACT-01 | Fill details + choose cash/credit — املأ التفاصيل | SCR-DIRECT-SALE-EDITOR | SVC-DIRECT-SALE | Credit sale: collected-now partial; difference is an explicit decision. |
| 3 | User action | ACT-01 | Record sale — سجّل البيع | SCR-DIRECT-SALE-EDITOR | SVC-DIRECT-SALE | Saves with idempotency; collection status resolved honestly. |
| 4 | System action | ACT-06 | Receipt with links — أظهر الوصل | — | — | افتح السجل → detail; consumption link available. |


### FLW-007 — Correcting a direct sale (edit / price cut / cancel)

> Arabic: تصحيح بيع مباشر · Status: **IMPLEMENTED**

- **Journey name:** Correcting a direct sale (edit / price cut / cancel) — تصحيح بيع مباشر
- **Actor:** ACT-01
- **User intention:** Fix a mistake in a recorded sale without silently rewriting history.
- **Entry points:** /direct-sales/:id → عدّل / تأكيد إلغاء البيع / خفّضتُ السعر
- **Success outcome:** Documented revision: edit (before-values kept), price cut (revenue = collected, original kept), cancel (excluded from revenue + mirror-reversed wallet allocations).
- **Primary path:** Open sale → choose correction → preview → confirm → revision recorded.
- **Alternative paths:** Cancel keeps history; revenue excluded; allocations reversed with deterministic keys sale-cancel:<saleId>:<entryId> (FT-02).
- **Failure / exception paths:** Concurrent edit conflict message; cancel of already-cancelled refused.
- **Screens:** SCR-DIRECT-SALE-EDITOR
- **Services:** SVC-DIRECT-SALE
- **Entities:** ENT-DIRECT-SALE, ENT-CASH-ENTRY
- **Before state:** Active sale.
- **After state:** Corrected sale with revision trail; cancelled sale excluded from revenue/cash/receivables.
- **Financial effect:** Signed effect in correction history: cancel → −revenue; price_cut → collected − beforeRevenue; edit → revenue − beforeRevenue.
- **Cashbox / wallet effect:** Cancel: wallet allocations mirror-reversed → value returns to unallocated.
- **Profit / cost effect:** Profit recomputed from new revenue; unknown cost still null.
- **Inventory effect:** Consumption movements unchanged (separate reversal flow).
- **Debt / deposit effect:** Cancelled credit sale removes its debt.
- **Offline / sync behavior:** Local.
- **Permissions / approval:** Owner.
- **History / audit behavior:** revisions[] preserved; correction history rows with signed effects (sale_edit/sale_cancel/sale_price_cut).
- **Exit & next action:** Return to referrer or open the reversed wallet ledger.
- **Evidence:** application/direct-sales/directSaleService.ts:217-273 (reverseAllocationsForCancelledSale); application/finance/correctionHistoryService.ts:246-281
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Open sale record — افتح سجل البيع | SCR-DIRECT-SALE-EDITOR | — | Detail shows revisions and status. |
| 2 | Decision | ACT-01 | Edit / price cut / cancel? — تعديل أم تخفيض أم إلغاء؟ | SCR-DIRECT-SALE-EDITOR | SVC-DIRECT-SALE | Three correction kinds, all documented (Conflict A simple verbs). |
| 3 | User action | ACT-01 | Confirm with preview — أكّد مع المعاينة | SCR-DIRECT-SALE-EDITOR | SVC-DIRECT-SALE | Before-values shown; original record never erased. |
| 4 | Persistence write | ACT-06 | Write revision — سجّل المراجعة | — | SVC-DIRECT-SALE | ExpectedRevisionCount optimistic concurrency on edit. |
| 5 | System action | ACT-06 | Mirror-reverse wallet allocations (on cancel) — اعكس تخصيصات المحفظة | — | SVC-CASH-CONTINUITY | Every allocation linked to the sale is reversed; wallet can't keep cancelled money. |


### FLW-008 — Creating an order without a saved customer

> Arabic: طلب بدون عميل محفوظ · Status: **IMPLEMENTED**

- **Journey name:** Creating an order without a saved customer — طلب بدون عميل محفوظ
- **Actor:** ACT-01
- **User intention:** Start a customer order when the customer is not (yet) saved — party is optional (Conflict B).
- **Entry points:** FAB → طلب من عميل → /orders/draft/new?intent=customer_order; Orders → بدء طلب; Schedule → بدء طلب (empty state)
- **Success outcome:** Draft created on first real input (no empty drafts), cost snapshot, agreement with price, delivery — all without a customer name.
- **Primary path:** FAB → DraftEditor (item, qty, specs — no customer required) → CostEditor snapshot → AgreementEditor price+deposit → OrderDetail → deliver.
- **Alternative paths:** Add customer name later from OrderDetail (سمِّ جهة هذا الطلب — one-way naming); unnamed receivable carries a visible warning when debt is registered.
- **Failure / exception paths:** Missing cost snapshot blocks agreement creation (missing_cost); unsaved-input guard protects typed values.
- **Screens:** SCR-DRAFT-EDITOR, SCR-COST-EDITOR, SCR-AGREEMENT-EDITOR, SCR-ORDER-DETAIL
- **Services:** SVC-DRAFT, SVC-COST, SVC-AGREEMENT
- **Entities:** ENT-DRAFT, ENT-CRAFT-ORDER
- **Before state:** No order.
- **After state:** Order without party; receivable honest when unnamed debt.
- **Financial effect:** Same as any order (deposit liquidity, revenue at delivery).
- **Cashbox / wallet effect:** None until deposit/collection.
- **Profit / cost effect:** Result only after delivery with final knowledge.
- **Inventory effect:** Consumption at delivery as usual.
- **Debt / deposit effect:** Unnamed debt allowed with warning (Conflict B).
- **Offline / sync behavior:** Local.
- **Permissions / approval:** Owner.
- **History / audit behavior:** Draft → linkedOrderId recorded; draft delete blocked once linked.
- **Exit & next action:** Name the party later or proceed to delivery.
- **Evidence:** pages/DraftEditor.tsx; pages/OrderDetail.tsx (سمِّ جهة هذا الطلب / احفظ اسم الجهة); docs/decisions/final-continuation-conflict-resolutions-v1.md (Conflict B)
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Start order draft — ابدأ مسودة طلب | SCR-DRAFT-EDITOR | SVC-DRAFT | Intent customer_order; created only on first real input (و٥ rule: exploration leaves no empty drafts). |
| 2 | User action | ACT-01 | Fill details without customer name — املأ التفاصيل بلا اسم عميل | SCR-DRAFT-EDITOR | SVC-DRAFT | Customer name optional field stays empty. |
| 3 | User action | ACT-01 | Cost snapshot + agreement — سجّل التكلفة والاتفاق | SCR-COST-EDITOR | SVC-COST | Agreement requires saved snapshot; price protected from cost when knowledge incomplete. |
| 4 | System action | ACT-06 | Create order from draft — أنشئ الطلب من المسودة | SCR-ORDER-DETAIL | SVC-AGREEMENT | commitOrderFromDraft atomic; provisional_agreement status; draft linked. |


### FLW-009 — Creating an order with an optional party/customer

> Arabic: طلب مع جهة اختيارية · Status: **IMPLEMENTED**

- **Journey name:** Creating an order with an optional party/customer — طلب مع جهة اختيارية
- **Actor:** ACT-01
- **User intention:** Attach a customer name and reuse it when the party repeats.
- **Entry points:** DraftEditor customer name field; OrderDetail → سمِّ جهة هذا الطلب
- **Success outcome:** Name stored on order; repeat names (≥2 distinct sources) surface as selectable parties in the people ledger; collection sheet picks the person up.
- **Primary path:** Type name in draft → order created with customerName → Parties page aggregates by name → جمع receivable rows deep link.
- **Alternative paths:** Name later from OrderDetail (one-way naming from order page); direct-sale customerName also feeds the ledger.
- **Failure / exception paths:** Duplicate similar names are not merged automatically (honest limitation — name-level, no CRM id).
- **Screens:** SCR-DRAFT-EDITOR, SCR-ORDER-DETAIL, SCR-PARTIES
- **Services:** SVC-DRAFT, SVC-PARTY-LEDGER
- **Entities:** ENT-DRAFT, ENT-CRAFT-ORDER, ENT-PARTY-LEDGER
- **Before state:** Party may or may not exist as repeated name.
- **After state:** Name-level party row with receivable/payable totals and movement links.
- **Financial effect:** None by itself.
- **Cashbox / wallet effect:** None.
- **Profit / cost effect:** None.
- **Inventory effect:** None.
- **Debt / deposit effect:** Receivables grouped per party name.
- **Offline / sync behavior:** Local derived read.
- **Permissions / approval:** Owner.
- **History / audit behavior:** Movements carry deep links to source records.
- **Exit & next action:** Collect from party row (ورقة التحصيل with source).
- **Evidence:** application/parties/partyLedgerService.ts (repeatedOnly, PA-010); pages/Parties.tsx:38-190
- **Status:** IMPLEMENTED
- **Open gaps:** GAP-06

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Enter party name — اكتب اسم الجهة | SCR-DRAFT-EDITOR | SVC-DRAFT | Optional; stored on the order. |
| 2 | System action | ACT-06 | Aggregate by name in people ledger — جمّع بالاسم في دفتر الناس | SCR-PARTIES | SVC-PARTY-LEDGER | ≥2 distinct sources → selectable reusable party (جهة). |
| 3 | User action | ACT-01 | Collect from party row — حصّل من الجهة | SCR-COLLECT | SVC-COLLECTION | Deep link /collect?source=order:<id>. |


### FLW-010 — Collecting a deposit (عربون)

> Arabic: قبض العربون · Status: **IMPLEMENTED**

- **Journey name:** Collecting a deposit (عربون) — قبض العربون
- **Actor:** ACT-01
- **User intention:** Take money before delivery and keep it as liquidity linked to the order — not revenue.
- **Entry points:** AgreementEditor at agreement recording; OrderDetail → سجّل العربون; Collect sheet → عربون أو تحصيل
- **Success outcome:** depositCollectedMinor increases; cash (with optional wallet attribution); depositSettlement stays null until cancellation; no revenue recognized.
- **Primary path:** OrderDetail → سجّل العربون → amount + wallet → deposit_collected event; allocation entry linked to order.
- **Alternative paths:** Deposit at agreement creation (createFromDraft initial deposit); deposit via collection sheet (money routed to owned service).
- **Failure / exception paths:** deposit + collected ≤ agreedPrice guard (Arabic numeric message); reversal via order collection reversal (double-reversal with allocation match).
- **Screens:** SCR-AGREEMENT-EDITOR, SCR-ORDER-DETAIL, SCR-COLLECT
- **Services:** SVC-AGREEMENT, SVC-FULFILLMENT, SVC-COLLECTION, SVC-CASH-CONTINUITY
- **Entities:** ENT-CRAFT-ORDER, ENT-CASH-ENTRY
- **Before state:** Order in pre-delivery status.
- **After state:** collectedMinor includes deposit; depositCollectedMinor set; cash in.
- **Financial effect:** Liquidity only — recognizedRevenue stays 0 until delivery (Conflict C/D).
- **Cashbox / wallet effect:** Cash + (allocation sourceRefKind 'order' or unallocated).
- **Profit / cost effect:** None (explicitly excluded from result).
- **Inventory effect:** None.
- **Debt / deposit effect:** Deposit reduces future receivable; on cancellation becomes refund/retain decision.
- **Offline / sync behavior:** Local.
- **Permissions / approval:** Owner.
- **History / audit behavior:** Order event deposit_collected; idempotency key; wallet ledger row with source link.
- **Exit & next action:** Deliver (deposit applied once inside the full sale) or collect more.
- **Evidence:** src/domain/craft-order/policies.ts:518 (collectDeposit guard); pages/OrderDetail.tsx:1009 (سجّل العربون); application/fulfillment/fulfillmentService.ts (collectDeposit)
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Record deposit — سجّل العربون | SCR-ORDER-DETAIL | SVC-FULFILLMENT | Amount + optional wallet destination. |
| 2 | System action | ACT-06 | Guard: deposit + collected ≤ price — تحقق من السقف | — | SVC-FULFILLMENT | Numeric Arabic message on violation. |
| 3 | Persistence write | ACT-06 | Write collection + allocation — اكتب القبضة والتخصيص | — | SVC-CASH-CONTINUITY | Cash in; allocation linked to order (sourceRefLineId for matching). |
| 4 | System action | ACT-06 | No revenue recognition yet — الإيراد لا يُعرف الآن | — | — | Deposit is liquidity tied to order + wallet (Conflict D). |


### FLW-011 — Delivering an order — full sale recognition

> Arabic: التسليم والاعتراف الكامل بالبيع · Status: **IMPLEMENTED**

- **Journey name:** Delivering an order — full sale recognition — التسليم والاعتراف الكامل بالبيع
- **Actor:** ACT-01
- **User intention:** Hand over the work and recognize the full sale exactly once, with deposit applied once inside it.
- **Entry points:** OrderDetail → راجع التسليم وسجّله (ready orders); /orders/:id/deliver
- **Success outcome:** One atomic transaction: status delivered, revenue = agreedPrice (once), consumption movements committed, optional collect-at-delivery into explicit wallet, schedule reconciled.
- **Primary path:** DeliveryReview builds full review (money lines, knowledge gaps, consumption rows with shortages, warnings) → optional price correction (reason) → consume checkboxes → wallet choice → single confirm → commitOrderDelivery.
- **Alternative paths:** Auto-consume proposal from template autoConsumeOnDelivery (never silent — inside the same confirmation); re-delivery after reversal gets a new attempt key (${id}:deliver-N).
- **Failure / exception paths:** Requires status ready; already-delivered → honest reuse; shortage rows offer 'record shortage' or 'consume available + shortage'; storage failure → nothing written (atomic).
- **Screens:** SCR-DELIVERY-REVIEW, SCR-ORDER-DETAIL
- **Services:** SVC-DELIVERY-REVIEW, SVC-FULFILLMENT, SVC-INVENTORY, SVC-CASH-CONTINUITY, SVC-SCHEDULE
- **Entities:** ENT-CRAFT-ORDER, ENT-INVENTORY-MOVEMENT, ENT-CASH-ENTRY, ENT-SCHEDULE-ENTRY
- **Before state:** Order ready; deposit may exist; receivable = price − collected.
- **After state:** delivered; recognizedRevenueMinor = agreedPrice; recognizedCostMinor; profit if final; receivable updated; auto settled if zero receivable.
- **Financial effect:** Revenue recognized ONCE here («التسليم: إيراد يُعرف مرة واحدة هنا»); deposit applied once within the sale value; collect-now is cash, not new revenue.
- **Cashbox / wallet effect:** Optional collection at delivery into explicit wallet (allocation with sourceRefLineId = delivery event id).
- **Profit / cost effect:** profitIndicatorMinor = price − planned cost when resultStatus final; consumption replaces snapshot material cost when cost-backed (COGS recorded).
- **Inventory effect:** Consumption movements per linked material (proportional value; unknown cost flagged; shortage recorded; one row per material).
- **Debt / deposit effect:** Remaining after delivery becomes collectable remainder or registered debt.
- **Offline / sync behavior:** Local atomic commit.
- **Permissions / approval:** Owner single confirm.
- **History / audit behavior:** status_changed delivered event + delivery_consumed note + delivery event id; reversal path documented.
- **Exit & next action:** Collect remaining (FLW-012) or register debt (FLW-014); order settles automatically when fully paid.
- **Evidence:** application/fulfillment/deliveryReviewService.ts:308-549 (commitDelivery atomic); src/domain/craft-order/policies.ts:425-441 (recognition); G3Delivery.dom.test.tsx (no hidden deduction, no duplicated revenue, no collection without destination)
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Open delivery review — راجع التسليم | SCR-DELIVERY-REVIEW | SVC-DELIVERY-REVIEW | Read-only review first: price, collected, deposit, remaining, cost, knowledge gaps. |
| 2 | Decision | ACT-01 | Confirm suggested material consumption — استهلاك المواد المقترح | SCR-DELIVERY-REVIEW | SVC-INVENTORY | Rows with planned vs available; suggestedAction per row; untracked materials never move. |
| 3 | Decision | ACT-01 | Collect at delivery? — قبض الآن أم لاحقًا؟ | SCR-DELIVERY-REVIEW | SVC-CASH-CONTINUITY | Optional amount into explicit wallet — cash only, never extra revenue. |
| 4 | User action | ACT-01 | Single atomic confirm — أكّد التسليم | SCR-DELIVERY-REVIEW | SVC-DELIVERY-REVIEW | commitOrderDelivery: transition + consumption + collection + schedule reconciliation in ONE transaction. |
| 5 | Persistence write | ACT-06 | Recognize revenue once — اعرف الإيراد مرة واحدة | — | — | recognizedRevenueMinor = agreedPrice; deposit counts inside it exactly once (Conflict C). |
| 6 | System action | ACT-06 | Auto-settle at zero receivable — سوّ تلقائيًا عند صفر متبقٍ | — | — | delivered + receivable 0 → settled with explicit events. |


### FLW-012 — Collecting the remaining amount after delivery

> Arabic: تحصيل المتبقي بعد التسليم · Status: **IMPLEMENTED**

- **Journey name:** Collecting the remaining amount after delivery — تحصيل المتبقي بعد التسليم
- **Actor:** ACT-01
- **User intention:** Collect the post-delivery remainder without re-recognizing revenue.
- **Entry points:** OrderDetail → حصّل المتبقي; Collect sheet → delivered remainder branch
- **Success outcome:** collectedMinor rises; cash attributed; auto settled at zero; revenue untouched.
- **Primary path:** OrderDetail/Collect → collectFullRemaining or collectFromSheet → wallet attribution → settled.
- **Alternative paths:** Partial collection (نصف المتبقي shortcut in sheet); register remainder as debt instead (FLW-014).
- **Failure / exception paths:** Requires delivered status («التحصيل يتطلب طلبًا مسلّمًا بمتبقٍ»); over-collection blocked with numeric message; attribution failure does not fail collection (money stays unallocated with notice).
- **Screens:** SCR-ORDER-DETAIL, SCR-COLLECT
- **Services:** SVC-FULFILLMENT, SVC-COLLECTION, SVC-CASH-CONTINUITY
- **Entities:** ENT-CRAFT-ORDER, ENT-CASH-ENTRY
- **Before state:** delivered with receivable > 0.
- **After state:** partially_paid → paid/settled; cash in.
- **Financial effect:** Cash only — collection is never revenue (five boundaries).
- **Cashbox / wallet effect:** Wallet allocation or unallocated.
- **Profit / cost effect:** None.
- **Inventory effect:** None.
- **Debt / deposit effect:** Receivable decreases.
- **Offline / sync behavior:** Local.
- **Permissions / approval:** Owner.
- **History / audit behavior:** collection_recorded event; reversal available as compound documented reversal (FLW-020).
- **Exit & next action:** Statement / next order.
- **Evidence:** src/domain/craft-order/policies.ts:551 (collectRemaining requires delivered); pages/Collect.tsx:145 (over-collection guard); application/collections/collectionService.ts
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Collect remaining — حصّل المتبقي | SCR-COLLECT | SVC-COLLECTION | Person + editable amount (نصف المتبقي shortcut) + explicit wallet. |
| 2 | System action | ACT-06 | Guard outstanding bounds — تحقق من حدود المتبقي | — | SVC-FULFILLMENT | Cap at remaining; honest Arabic numeric message. |
| 3 | Persistence write | ACT-06 | Write collection + allocation — سجّل القبضة والتخصيص | — | SVC-CASH-CONTINUITY | Deterministic attribution key; failure → unallocated + notice. |
| 4 | System action | ACT-06 | Auto-settle at zero — سوِّ عند الصفر | — | — | settlementStatus paid; status settled. |


## Group — C — Debt & parties


### FLW-013 — Selling on credit (receivable creation)

> Arabic: البيع بالأجل وإنشاء الدين · Status: **IMPLEMENTED**

- **Journey name:** Selling on credit (receivable creation) — البيع بالأجل وإنشاء الدين
- **Actor:** ACT-01
- **User intention:** Record a sale whose money is not received yet.
- **Entry points:** DirectSaleEditor → بيع آجل; QuickActionSheet sale form credit option
- **Success outcome:** Direct sale with collectionStatus partial_debt (explicit decision) and outstanding derived; or delivered order remainder later registered as debt.
- **Primary path:** Direct sale with collected < revenue → resolveCollection explicit decision (partial_debt or partial_needs_review) → debt appears in parties/collect sheet.
- **Alternative paths:** Order path: deliver without full collection → register debt explicitly (FLW-014); partial_needs_review honest state when undecided.
- **Failure / exception paths:** Ambiguity refused silently — difference must be an explicit decision; unknown remainder never auto-debt.
- **Screens:** SCR-DIRECT-SALE-EDITOR, SCR-QUICK-ACTION
- **Services:** SVC-DIRECT-SALE, SVC-COLLECTION
- **Entities:** ENT-DIRECT-SALE, ENT-CRAFT-ORDER, ENT-PARTY-LEDGER
- **Before state:** None / delivered order.
- **After state:** Receivable visible in position (customerReceivablesMinor) and collect sheet sources.
- **Financial effect:** Revenue recognized (at sale date for direct sales; at delivery for orders) — debt is not extra revenue.
- **Cashbox / wallet effect:** Only the collected part.
- **Profit / cost effect:** Profit computed on revenue regardless of collection.
- **Inventory effect:** None extra.
- **Debt / deposit effect:** Debt = revenue − collected, explicit.
- **Offline / sync behavior:** Local.
- **Permissions / approval:** Owner.
- **History / audit behavior:** collectionStatus recorded; revisions on later corrections.
- **Exit & next action:** Collect the debt later (FLW-015).
- **Evidence:** src/domain/direct-sale/policies.ts (resolveCollection); application/finance/projectFinancialService.ts:399-404 (receivables in position)
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Decision | ACT-01 | Choose credit sale — بيع آجل | SCR-DIRECT-SALE-EDITOR | SVC-DIRECT-SALE | Collected-now amount optional. |
| 2 | Decision | ACT-01 | Explicit decision on the difference — ماذا يمثل الفرق؟ | — | SVC-DIRECT-SALE | partial_debt vs partial_needs_review — never silent. |
| 3 | System action | ACT-06 | Debt appears in ledger sources — أظهر الدين في الدفتر | SCR-PARTIES | SVC-PARTY-LEDGER | Collect sheet finds receivable sources (registered debts + delivered remainders + sale debts). |


### FLW-014 — Registering order debt after delivery

> Arabic: تسجيل دين الطلب · Status: **IMPLEMENTED**

- **Journey name:** Registering order debt after delivery — تسجيل دين الطلب
- **Actor:** ACT-01
- **User intention:** Turn a delivered order's remainder into a registered, collectable debt.
- **Entry points:** OrderDetail → سجّل الدين; Collect sheet (debt branch)
- **Success outcome:** registerDebt on the order (debt exists only by explicit registration); debt appears as receivable source.
- **Primary path:** Delivered order → register debt (amount ≤ remaining) → settlementStatus debt → collect later.
- **Alternative paths:** Unnamed debt allowed with visible warning (Conflict B); later collections reduce debt and never re-open the order.
- **Failure / exception paths:** Debt before delivery refused; debt above remaining refused.
- **Screens:** SCR-ORDER-DETAIL, SCR-COLLECT
- **Services:** SVC-FULFILLMENT, SVC-COLLECTION
- **Entities:** ENT-CRAFT-ORDER, ENT-PARTY-LEDGER
- **Before state:** delivered, unpaid remainder.
- **After state:** debt registered; order not reopened by later collections.
- **Financial effect:** No new revenue (already recognized at delivery).
- **Cashbox / wallet effect:** None at registration.
- **Profit / cost effect:** None.
- **Inventory effect:** None.
- **Debt / deposit effect:** Debt registered; collectable from sheet; unnamed warning if no party.
- **Offline / sync behavior:** Local.
- **Permissions / approval:** Owner.
- **History / audit behavior:** debt_registered order event.
- **Exit & next action:** Collect from sheet; G5 declaration can link expected collection to this debt.
- **Evidence:** src/domain/craft-order/policies.ts:596-627 (registerDebt / collectRegisteredDebt); pages/OrderDetail.tsx:1596 (حصّل الدين من ورقة التحصيل)
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Register debt — سجّل الدين | SCR-ORDER-DETAIL | SVC-FULFILLMENT | Explicit registration — debt is never implied. |
| 2 | Decision | ACT-01 | Name party or leave unnamed (warning) — سمِّ الجهة أو اتركه | — | — | Conflict B: unnamed receivable represented honestly. |
| 3 | System action | ACT-06 | Add receivable source — أدرج مصدر التحصيل | SCR-COLLECT | SVC-COLLECTION | Debt branch of the collection sheet. |


### FLW-015 — Collecting a debt from the collection sheet

> Arabic: التحصيل من ورقة التحصيل · Status: **IMPLEMENTED**

- **Journey name:** Collecting a debt from the collection sheet — التحصيل من ورقة التحصيل
- **Actor:** ACT-01
- **User intention:** Collect money owed by any party (order debts, delivered remainders, sale debts) in one honest surface.
- **Entry points:** FAB → عربون أو تحصيل → /collect; Parties row → جمع; OrderDetail → حصّل الدين من ورقة التحصيل
- **Success outcome:** Collection recorded through the owned service (order/sale), cash attributed to explicit wallet, remainder reduced.
- **Primary path:** /collect → pick person → amount (نصف المتبقي shortcut) → explicit wallet destination → سجّل القبض → receipt with افتح السجل.
- **Alternative paths:** Pre-delivery money is routed as deposit (عربون) not collection; direct-sale path raises collectedMinor with revision reason «تحصيل دفعة من ورقة التحصيل» (FC-09).
- **Failure / exception paths:** Over-collection blocked (numeric message with remaining); attribution failure keeps money unallocated with notice; ambiguous sources resolved by explicit person selection.
- **Screens:** SCR-COLLECT, SCR-PARTIES
- **Services:** SVC-COLLECTION, SVC-FULFILLMENT, SVC-DIRECT-SALE, SVC-CASH-CONTINUITY
- **Entities:** ENT-CASH-ENTRY, ENT-CRAFT-ORDER, ENT-DIRECT-SALE
- **Before state:** Receivable sources exist.
- **After state:** Cash in; receivable down; order may settle; sale collectionStatus improves.
- **Financial effect:** Cash only — «التحصيل كاش ومتبقٍ فقط، لا إيراد جديد».
- **Cashbox / wallet effect:** Wallet allocation with source link (sourceRefLineId for double-reversal matching).
- **Profit / cost effect:** None.
- **Inventory effect:** None.
- **Debt / deposit effect:** Debt/remainder decreases.
- **Offline / sync behavior:** Local.
- **Permissions / approval:** Owner.
- **History / audit behavior:** Order collection events + sale revisions; wallet ledger row with source deep link.
- **Exit & next action:** Receipt → افتح السجل (source record).
- **Evidence:** pages/Collect.tsx:38-41, 205-298; application/collections/collectionService.ts (routing through owned services); G2.dom.test.tsx
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Pick person who owes — اختر الشخص | SCR-COLLECT | SVC-COLLECTION | Sources: registered order debts + delivered remainders + direct-sale partial debts. |
| 2 | User action | ACT-01 | Amount + explicit wallet — ادخل المبلغ والوجهة | SCR-COLLECT | SVC-CASH-CONTINUITY | Blocks over-collection; half-remaining shortcut. |
| 3 | User action | ACT-01 | Record collection — سجّل القبض | SCR-COLLECT | SVC-COLLECTION | Writes through the owned service, then attributes cash. |
| 4 | System action | ACT-06 | Receipt + source link — أظهر الوصل | — | — | افتح السجل → source record. |


### FLW-016 — Saving and reusing a recurring party

> Arabic: حفظ الجهة المتكررة وإعادة استخدامها · Status: **IMPLEMENTED**

- **Journey name:** Saving and reusing a recurring party — حفظ الجهة المتكررة وإعادة استخدامها
- **Actor:** ACT-01
- **User intention:** Deal with a repeat customer/supplier without managing contacts.
- **Entry points:** Parties page search; Collect person selection; Order/sale name fields
- **Success outcome:** Name-level party row (receivable + payable + movements); repeat names (≥2 distinct sources) become selectable; collect deep link per row.
- **Primary path:** Record orders/sales/purchases with the same name → Parties page aggregates → open row movements → collect.
- **Alternative paths:** repeatedOnly filter shows only reusable parties; single-use names stay local to their record.
- **Failure / exception paths:** No merge/dedup of similar names (honest name-level model, no CRM entity); legacy direct-sale customer names extracted from notes (عميل: X / لـ X).
- **Screens:** SCR-PARTIES
- **Services:** SVC-PARTY-LEDGER
- **Entities:** ENT-PARTY-LEDGER
- **Before state:** Names scattered across records.
- **After state:** Aggregated ledger per name.
- **Financial effect:** None (read-only aggregation).
- **Cashbox / wallet effect:** None.
- **Profit / cost effect:** None.
- **Inventory effect:** None.
- **Debt / deposit effect:** Receivable/payable totals per party visible.
- **Offline / sync behavior:** Local derived read.
- **Permissions / approval:** Owner.
- **History / audit behavior:** Movement deep links to each source record.
- **Exit & next action:** Collect or open supplier purchase.
- **Evidence:** application/parties/partyLedgerService.ts (PA-010; customerName legacy note extraction); application/parties/partyLedgerService.customerName.test.ts
- **Status:** IMPLEMENTED
- **Open gaps:** GAP-06

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | System action | ACT-06 | Aggregate movements by name — جمّع الحركات بالاسم | SCR-PARTIES | SVC-PARTY-LEDGER | Order debts/collections, sale debts, purchase payables/payments, payable events by counterparty. |
| 2 | User action | ACT-01 | Search / filter repeated — ابحث أو رشّح المتكرر | SCR-PARTIES | SVC-PARTY-LEDGER | repeatedOnly: ≥2 distinct sources → جهة. |
| 3 | User action | ACT-01 | Open movement or collect — افتح الحركة أو حصّل | — | SVC-COLLECTION | Every movement row deep-links to its source. |


## Group — D — Expenses & corrections


### FLW-017 — Recording an expense (guided entry)

> Arabic: تسجيل مصروف بالإدخال الموجّه · Status: **IMPLEMENTED**

- **Journey name:** Recording an expense (guided entry) — تسجيل مصروف بالإدخال الموجّه
- **Actor:** ACT-01
- **User intention:** Record what was paid, correctly classified, with honest context and effect preview.
- **Entry points:** FAB → تسجيل مصروف (quick form); /finance/new/operating_expense_cash | operating_expense_payable; Finance hub quick actions
- **Success outcome:** Event saved with expense context (relationship/behavior/purpose/knowledge, optional categoryLabel), effect preview matched by construction, optional wallet attribution.
- **Primary path:** Guided editor sequence: شو صار → قدّش → من وين طلع المبلغ؟ → date → party → context layer (category → behavior → relationship → share basis) → description → preview → save.
- **Alternative paths:** Quick path in sheet: amount + optional wallet + one-tap label; payable variant (التزام لمورد); amanah held/released; loss non-cash (هدر بلا خروج نقد).
- **Failure / exception paths:** Shared expense share must match computed amount (assertShareShape); unknown share → unallocated, excluded from result until declared (needs_review knowledge); draft restore is version-gated.
- **Screens:** SCR-FINANCIAL-EVENT-EDITOR, SCR-QUICK-ACTION
- **Services:** SVC-PROJECT-FINANCE, SVC-EXPENSE-INTENT, SVC-CATEGORY-SUGGESTIONS, SVC-CASH-CONTINUITY
- **Entities:** ENT-FINANCIAL-EVENT, ENT-CASH-ENTRY, ENT-FORM-DRAFT
- **Before state:** Any.
- **After state:** Event with signed deltas (cash − / payable + / expense +).
- **Financial effect:** operating_expense_cash: [−1,0,0,1,...]; unallocated shared expenses contribute 0 to result until share declared.
- **Cashbox / wallet effect:** Cash out (or payable); attribution to wallet after save (failure never touches the event).
- **Profit / cost effect:** Operating expense line in period result; category is a reading dimension only.
- **Inventory effect:** None (materials route to suppliers page — honest routing).
- **Debt / deposit effect:** Payable variant creates supplier payable to settle later.
- **Offline / sync behavior:** Local; form draft persisted (micro.finance-draft.<type>.v1).
- **Permissions / approval:** Owner.
- **History / audit behavior:** Idempotency; frozen categoryLabel with event; correction via reverse-and-replace only.
- **Exit & next action:** Saved event focus (/finance?event=<id>); suppliers link for payables.
- **Evidence:** pages/FinancialEventEditor.tsx (sequence + preview + line 867 category note); application/finance/expenseRecordIntent.ts (single expansion shared by preview and save); components/finance/AllocationReviewCard.tsx; pages/FinancialEventEditor.guided.test.tsx
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | What happened? (event type) — شو صار؟ | SCR-FINANCIAL-EVENT-EDITOR | SVC-PROJECT-FINANCE | 8 guided types; routing honesty: materials → suppliers, assets/loans → their pages. |
| 2 | User action | ACT-01 | How much and from where? — قدّش ومن وين؟ | SCR-FINANCIAL-EVENT-EDITOR | SVC-EXPENSE-INTENT | Amount + source wallet; safe-integer guards (AV-05). |
| 3 | Decision | ACT-01 | Project or shared (household)? — هل تخص المشروع أم البيت؟ | SCR-FINANCIAL-EVENT-EDITOR | SVC-EXPENSE-INTENT | Shared expenses record the project share only (contract 08); «غير متأكد» always offered. |
| 4 | User action | ACT-01 | Category label + behavior + purpose — أضف التصنيف والسياق | SCR-FINANCIAL-EVENT-EDITOR | SVC-CATEGORY-SUGGESTIONS | Free tag ≤80 chars + suggestion chips (owner's tags newest-first + Jordan seeds). |
| 5 | System action | ACT-05 | Impact preview before save — معاينة الأثر قبل الحفظ | SCR-FINANCIAL-EVENT-EDITOR | SVC-EXPENSE-INTENT | Derived from the same pure expansion consumed by save (no divergence possible). |
| 6 | User action | ACT-01 | Save — احفظ | SCR-FINANCIAL-EVENT-EDITOR | SVC-PROJECT-FINANCE | Idempotent write; optional wallet attribution after save. |


### FLW-018 — Correcting expense classification after saving

> Arabic: تصحيح تصنيف المصروف بعد الحفظ · Status: **IMPLEMENTED**

- **Journey name:** Correcting expense classification after saving — تصحيح تصنيف المصروف بعد الحفظ
- **Actor:** ACT-01
- **User intention:** Fix the classification of an already-saved expense (WF-04 / Conflict H) without altering the original record.
- **Entry points:** /finance events layer → event row → تعديل العملية (edit operation)
- **Success outcome:** Atomic reverse-and-replace: replacement event carries the new expenseContext; original keeps the old classification; correction history documents the pair.
- **Primary path:** Open event → edit operation → change classification fields → preview → confirm → commitFinancialEventReplacement (reversal + replacement, one transaction).
- **Alternative paths:** Restore (التراجع عن التصحيح) re-records original values as a new event (restore:<id> key).
- **Failure / exception paths:** Classification edit allowed only for expense events («التصنيف يُصحَّح لأحداث المصروف فقط»); family events (asset/loan/deposit) are corrected from their own surfaces.
- **Screens:** SCR-FINANCE, SCR-FINANCIAL-EVENT-EDITOR
- **Services:** SVC-PROJECT-FINANCE, SVC-CORRECTION-HISTORY
- **Entities:** ENT-FINANCIAL-EVENT
- **Before state:** Saved expense event with old context.
- **After state:** Reversal event (correctionType reverse) + replacement event with new context; reader uses replacement.
- **Financial effect:** Deltas unchanged in magnitude unless amount also corrected; category is zero-delta by construction (twin tests).
- **Cashbox / wallet effect:** None for classification-only change.
- **Profit / cost effect:** Reading dimension changes (statement groups by frozen label of the replacement).
- **Inventory effect:** None.
- **Debt / deposit effect:** None.
- **Offline / sync behavior:** Local atomic.
- **Permissions / approval:** Owner with preview.
- **History / audit behavior:** event_edit row with original/replacement labels; EDIT_REVERSAL_SUFFIX key pairing.
- **Exit & next action:** View corrected event; statement re-groups by new label.
- **Evidence:** application/finance/projectFinancialService.ts:1077-1103 (editEvent expenseContext-only); application/finance/projectFinancialService.category.test.ts (zero delta twins); docs/decisions/final-continuation-conflict-resolutions-v1.md (Conflict H/WF-04)
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Open the expense event row — افتح حدث المصروف | SCR-FINANCE | SVC-CORRECTION-HISTORY | Events layer with ?event=<id> focus. |
| 2 | User action | ACT-01 | Choose edit operation — اختر تعديل العملية | SCR-FINANCE | SVC-PROJECT-FINANCE | Conflict A: simple owner verb; engine = atomic reverse-and-replace. |
| 3 | User action | ACT-01 | Change classification — عدّل التصنيف | SCR-FINANCIAL-EVENT-EDITOR | SVC-EXPENSE-INTENT | Same guided context editor; replacement re-validated by normalizeExpenseContext. |
| 4 | Persistence write | ACT-06 | Atomic reversal + replacement — اكتب زوج التصحيح ذريًا | — | SVC-PROJECT-FINANCE | «كل شيء أو لا شيء»; original untouched. |
| 5 | System action | ACT-06 | Document in correction history — وثّق في السجل | — | SVC-CORRECTION-HISTORY | event_edit with amountEffectMinor = replacement − source. |


### FLW-019 — Editing a previous financial operation (general)

> Arabic: تعديل عملية مالية سابقة · Status: **IMPLEMENTED**

- **Journey name:** Editing a previous financial operation (general) — تعديل عملية مالية سابقة
- **Actor:** ACT-01
- **User intention:** Correct amount/date/context of any general financial event safely.
- **Entry points:** /finance events layer → row actions; U001 deep-linked row via ?event=
- **Success outcome:** Atomic reverse-and-replace pair; amount guards pass (payable settlement ≤ remaining; amanah release ≤ held).
- **Primary path:** Row → تعديل → edit form (amount, date, context) → preview → confirm → replacement pair.
- **Alternative paths:** Delete (حذف) = full documented reversal with reason «حذف»; Restore (Undo) = re-record original as new event; corrections of family events (asset/loan/deposit) route to their owner surfaces (FT-03).
- **Failure / exception paths:** No double reversal; no reversing a reversal; family guard rejects order-linked deposit events from general path (AV-03); amanah limit guard (F-006).
- **Screens:** SCR-FINANCE
- **Services:** SVC-PROJECT-FINANCE, SVC-CORRECTION-HISTORY
- **Entities:** ENT-FINANCIAL-EVENT
- **Before state:** Active event.
- **After state:** Reversal + replacement (edit) or reversal only (delete) or restored copy.
- **Financial effect:** Net effect = replacement − source for edits; −amount for delete; +original for restore.
- **Cashbox / wallet effect:** Follows delta table of the type.
- **Profit / cost effect:** Expense lines corrected at correction date (no restatement).
- **Inventory effect:** None (inventory has its own reversal flow).
- **Debt / deposit effect:** Payable guards keep settlements consistent.
- **Offline / sync behavior:** Local atomic.
- **Permissions / approval:** Owner with impact preview (D005).
- **History / audit behavior:** Three actions reachable from the row itself (D-005) with impact shown before confirm.
- **Exit & next action:** Corrected reading surfaces update.
- **Evidence:** application/finance/projectFinancialService.ts (reverse/editEvent/deleteEvent/restoreEvent); D005.dom.test.tsx; U001.dom.test.tsx; docs/contracts/23-general-financial-event-correction-boundary-proposal-v1.md (C1)
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Open register, pick operation — افتح السجل واختر العملية | SCR-FINANCE | SVC-CORRECTION-HISTORY | «السجل» shows every event; older events reachable via show-all. |
| 2 | Decision | ACT-01 | Edit / delete / undo? — تعديل أم حذف أم تراجع؟ | SCR-FINANCE | SVC-PROJECT-FINANCE | Three row actions with impact preview. |
| 3 | User action | ACT-01 | Confirm with reason — أكّد مع السبب | — | SVC-PROJECT-FINANCE | Reason mandatory for delete/reverse. |
| 4 | Persistence write | ACT-06 | Atomic commit — تنفيذ ذري | — | SVC-PROJECT-FINANCE | Reversal+replacement or reversal or restore event. |


### FLW-020 — Cancelling / reversing a collection (compound)

> Arabic: التراجع عن تحصيل مزدوج الأثر · Status: **IMPLEMENTED**

- **Journey name:** Cancelling / reversing a collection (compound) — التراجع عن تحصيل مزدوج الأثر
- **Actor:** ACT-01
- **User intention:** Reverse a collection together with its matching wallet allocation, honestly (S2-04ا).
- **Entry points:** OrderDetail → تراجع عن قبضة; WalletLedger row → تراجع; Correction layer
- **Success outcome:** Compound reversal: order collection reversed + mirror reversal cash entry; full match + full amount only; before/after preview numbers per dimension.
- **Primary path:** preview() → match statuses (full_match / no_allocation / ambiguous / amount_mismatch / allocation_already_reversed / partial_only) → confirm → commitOrderCollectionReversal.
- **Alternative paths:** Allocation attribute failure at collection time → collection reversal proceeds on order only (no allocation to reverse).
- **Failure / exception paths:** Ambiguous match refuses with message; partial reversal rejected; double reversal refused; wallet would go negative → safe rejection.
- **Screens:** SCR-ORDER-DETAIL, SCR-WALLET-LEDGER
- **Services:** SVC-COLLECTION-REVERSAL, SVC-CASH-CONTINUITY, SVC-CORRECTION-HISTORY
- **Entities:** ENT-CRAFT-ORDER, ENT-CASH-ENTRY
- **Before state:** Order collection + wallet allocation pair.
- **After state:** collection_reversed order event; reversal entry (reversesEntryId); cash out; receivable restored; revenue untouched.
- **Financial effect:** Cash returns to customer (cash-out); remainder re-becomes receivable; revenue never touched.
- **Cashbox / wallet effect:** Wallet balance down; unallocated adjusted; recorded cash down — all move together.
- **Profit / cost effect:** None («الإيراد لم يتغير»).
- **Inventory effect:** None.
- **Debt / deposit effect:** Receivable restored by reversed amount.
- **Offline / sync behavior:** Local atomic.
- **Permissions / approval:** Owner with honest preview.
- **History / audit behavior:** Order log carries documented reversal; correction history row collection_reversed (−amount).
- **Exit & next action:** Re-collect correctly or continue.
- **Evidence:** application/collections/collectionReversalService.ts (preview/reverse, match statuses); G6.dom.test.tsx (double reversal journey); application/collections/collectionReversalService.test.ts
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Request collection reversal — اطلب التراجع عن القبضة | SCR-ORDER-DETAIL | SVC-COLLECTION-REVERSAL | Pre-cancel warning for non-deposit collections (AV-06). |
| 2 | System action | ACT-06 | Find matching allocation — ابحث عن التخصيص المطابق | — | SVC-COLLECTION-REVERSAL | Primary: operation key; then sourceRefLineId; legacy amount-match with ambiguity refusal. |
| 3 | User action | ACT-01 | Review before/after preview — راجع الأرقام قبل وبعد | — | SVC-COLLECTION-REVERSAL | Wallet balance, unallocated, recorded cash per dimension. |
| 4 | Persistence write | ACT-06 | Atomic compound reversal — عكس مزدوج ذري | — | SVC-COLLECTION-REVERSAL | Full match + full amount only; one transaction. |


## Group — E — Order cancellation & deposits


### FLW-021 — Cancelling an order with a deposit (Conflict E)

> Arabic: إلغاء طلب فيه عربون · Status: **IMPLEMENTED**

- **Journey name:** Cancelling an order with a deposit (Conflict E) — إلغاء طلب فيه عربون
- **Actor:** ACT-01
- **User intention:** Cancel an order and decide honestly what happens to the deposit.
- **Entry points:** OrderDetail → ألغِ الطلب بهذا السبب (reason chips: خطأ في السعر / انسحب العميل / سبب آخر / تخطّى السبب وألغِ)
- **Success outcome:** Order cancelled; settlementStatus cancelled_pending; depositSettlement needs_review; impact preview shown; then refund/retain/partial split with classification.
- **Primary path:** Cancel with reason → cancelled_pending → decide: settleDepositRefund (cash back, allocations reversed up to refund) or settleDepositRetain → classify retained amount (owner vs revenue) → final cancelled_refunded / cancelled_retained.
- **Alternative paths:** Partial refund/partial retain (Conflict E: explicit amounts; remaining stays needs_review); skip reason via chip (تخطّى السبب وألغِ).
- **Failure / exception paths:** Cancel refused after delivered/settled/cancelled (Arabic status message); needs_review orders cancellable when it completes safely (AV-07) else honest block with reason; deposit > collected impossible by construction.
- **Screens:** SCR-ORDER-DETAIL
- **Services:** SVC-FULFILLMENT, SVC-RETAINED-DEPOSIT, SVC-CASH-CONTINUITY
- **Entities:** ENT-CRAFT-ORDER, ENT-CASH-ENTRY, ENT-FINANCIAL-EVENT
- **Before state:** Pre-delivery order with deposit; possibly needs_review.
- **After state:** cancelled (+ pending deposit settlement) → final refund/retain + classification events.
- **Financial effect:** Receivable zeroed; profit nulled (review_required); refund = cash out + allocation reversal; retained = cash stays + explicit meaning event (owner capital or revenue once).
- **Cashbox / wallet effect:** Refund: cash − and deposit wallet allocations reversed (full allocations fully, last partially, one reversal each); Retain: no cash movement.
- **Profit / cost effect:** Retained-as-revenue recognizes revenue ONCE (deposit_retained_revenue); never auto-classified.
- **Inventory effect:** Consumed materials (if any pre-delivery) reversed separately via inventory reversal.
- **Debt / deposit effect:** Deposit decision documented; pendingRetainedDepositsMinor visible in position until classified.
- **Offline / sync behavior:** Local atomic per stage.
- **Permissions / approval:** Owner with mandatory impact preview (Conflict E).
- **History / audit behavior:** cancelled event + deposit_refunded/deposit_retained/deposit_classified events; retainedMeaning recorded.
- **Exit & next action:** Deposits layer on Finance shows pending decisions; classification later correctable (FLW-023).
- **Evidence:** src/domain/craft-order/policies.ts:876-924 (cancelOrder), 1014-1087 (settle refund/retain); application/fulfillment/fulfillmentService.ts:414-483 (buildDepositAllocationReversals); pages/OrderDetail.tsx:933-1009; G4RetainedDeposit.dom.test.tsx
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Cancel with documented reason — ألغِ الطلب بسبب موثق | SCR-ORDER-DETAIL | SVC-FULFILLMENT | Reason chips; deposit>0 → cancelled_pending + needs_review. |
| 2 | System action | ACT-05 | Show full impact preview — اعرض معاينة الأثر الكاملة | SCR-ORDER-DETAIL | — | Deposit, cashbox source, inventory/cost, profit effect, retained/refunded/owner money (Conflict E mandate). |
| 3 | Decision | ACT-01 | Refund / retain / partial split? — رد أم احتفظ أم جزئي؟ | SCR-ORDER-DETAIL | SVC-FULFILLMENT | Explicit amounts; never auto full classification. |
| 4 | Persistence write | ACT-06 | Execute settlement — نفّذ التسوية | — | SVC-FULFILLMENT | Refund: commitDepositRefundSettlement (cash back + allocation reversals, atomic). Retain: settleDepositRetain. |
| 5 | Decision | ACT-01 | Classify retained amount — صنّف المحتفظ به | — | SVC-RETAINED-DEPOSIT | deposit_retained_owner (owner capital +) or deposit_retained_revenue (revenue once); default pending. |


### FLW-022 — Cancelling an order after cost or material consumption

> Arabic: إلغاء طلب بعد تكلفة أو استهلاك مواد · Status: **IMPLEMENTED**

- **Journey name:** Cancelling an order after cost or material consumption — إلغاء طلب بعد تكلفة أو استهلاك مواد
- **Actor:** ACT-01
- **User intention:** Cancel when work/materials were already spent — with honest boundaries.
- **Entry points:** OrderDetail cancel action (pre-delivery statuses incl. needs_review)
- **Success outcome:** Order cancelled; consumed material movements remain as facts (reversible separately via documented inventory reversal); needs_review resume path available instead of cancel.
- **Primary path:** Cancel (pre-delivery) → cancelled; inventory consumption movements (recorded earlier via /inventory/movement/consume?order=) stay; reverse them individually with reason if wrong.
- **Alternative paths:** After delivery: cancellation refused (honest block) → use reverseDelivery (FLW-039) to void the sale, then cancel if desired; resumeAfterReview path (needs_review → confirmed → in_progress).
- **Failure / exception paths:** «لا يمكن إلغاء الطلب وهو في حالة «تم التسليم»» — explicit Arabic refusal; cancellation from needs_review must complete safely else honest lock-with-reason (AV-07).
- **Screens:** SCR-ORDER-DETAIL, SCR-INVENTORY-REVERSAL
- **Services:** SVC-FULFILLMENT, SVC-INVENTORY
- **Entities:** ENT-CRAFT-ORDER, ENT-INVENTORY-MOVEMENT
- **Before state:** Pre-delivery order with recorded consumption or revised cost.
- **After state:** cancelled; movements intact (facts); resultStatus review_required.
- **Financial effect:** Profit nulled; cost facts remain in inventory value.
- **Cashbox / wallet effect:** Per deposit decision (FLW-021).
- **Profit / cost effect:** No sale recognition (was pre-delivery); consumption cost stays in inventory/period waste lines.
- **Inventory effect:** Consumption movements preserved; separate documented reversal if erroneous.
- **Debt / deposit effect:** Receivable zeroed.
- **Offline / sync behavior:** Local.
- **Permissions / approval:** Owner; AV-07 safe-completion check.
- **History / audit behavior:** cancelled + movement reversal records kept independently.
- **Exit & next action:** Reverse wrong consumption movements; record waste for lost materials (FLW-027/028).
- **Evidence:** src/domain/craft-order/policies.ts:876-884 (post-delivery refusal); pages/OrderDetail.tsx:1690 (consume link); application/inventory/inventoryMaterialService.ts (reverse)
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Decision | ACT-01 | Is order pre-delivery? — هل الطلب قبل التسليم؟ | SCR-ORDER-DETAIL | SVC-FULFILLMENT | Delivered/settled orders cannot be cancelled — honest refusal message. |
| 2 | User action | ACT-01 | Cancel order — ألغِ الطلب | SCR-ORDER-DETAIL | SVC-FULFILLMENT | Reason documented; deposit path as FLW-021. |
| 3 | System action | ACT-06 | Keep consumption movements as facts — حافظ على حركات الاستهلاك | — | SVC-INVENTORY | Movements not auto-reversed on order cancel. |
| 4 | User action | ACT-01 | Reverse wrong movement or record waste — اعكس حركة خاطئة أو سجّل هدرًا | SCR-INVENTORY-REVERSAL | SVC-INVENTORY | Separate documented actions with reasons. |


### FLW-023 — Retained deposit classification & reclassification

> Arabic: تصنيف العربون المحتفظ به وتصحيحه · Status: **IMPLEMENTED**

- **Journey name:** Retained deposit classification & reclassification — تصنيف العربون المحتفظ به وتصحيحه
- **Actor:** ACT-01
- **User intention:** Decide (and later correct) what a retained deposit means financially.
- **Entry points:** Finance → deposits layer; OrderDetail → احتفظ به رصيدًا → صحِّح التصنيف بقرار موثق
- **Success outcome:** deposit_retained_owner or deposit_retained_revenue event; partial amounts allowed; reclassification = atomic reverse+replace of the classification event.
- **Primary path:** listPending (cancelled + retain + meaning null) → classify(meaning, reason, amount?) → commitDepositClassification (order + event atomic).
- **Alternative paths:** Partial classification (explicit amount); mixed meaning derived from owner/revenue sums; reclassify finds last active classification event and replaces it.
- **Failure / exception paths:** Amount bounded by unclassified retained; events are truth (counters are mirror); family guard protects these events from general-path correction (FT-03).
- **Screens:** SCR-FINANCE, SCR-ORDER-DETAIL
- **Services:** SVC-RETAINED-DEPOSIT, SVC-CORRECTION-HISTORY
- **Entities:** ENT-CRAFT-ORDER, ENT-FINANCIAL-EVENT
- **Before state:** Retained deposit pending meaning.
- **After state:** Classified (owner capital or revenue-once) or reclassified with documented from/to.
- **Financial effect:** Owner path: ownerCapital +; Revenue path: retainedDepositRevenue + (counted once in period result).
- **Cashbox / wallet effect:** None — cash entered at collection; classification declares ownership only.
- **Profit / cost effect:** Revenue classification adds a separate declared line (never profit by itself; contract 29).
- **Inventory effect:** None.
- **Debt / deposit effect:** pendingRetainedDepositsMinor decreases.
- **Offline / sync behavior:** Local atomic.
- **Permissions / approval:** Owner with documented reason.
- **History / audit behavior:** deposit_classified / deposit_reclassification rows; correction keys -reversal:/-replacement:.
- **Exit & next action:** Statement shows the declared line; order deposit card updates.
- **Evidence:** application/finance/retainedDepositService.ts:40-119 (classify), 99-119 (events are truth); src/domain/craft-order/policies.ts:1088-1200 (classifyRetainedDeposit / reclassifyRetainedDeposit)
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Open pending deposit decisions — افتح قرارات العربون المعلّقة | SCR-FINANCE | SVC-RETAINED-DEPOSIT | Deposits layer lists pending with wallet + profit-effect label (FC-05). |
| 2 | Decision | ACT-01 | Owner money or project revenue? — مال مالك أم إيراد مشروع؟ | SCR-FINANCE | SVC-RETAINED-DEPOSIT | Explicit decision + optional partial amount. |
| 3 | Persistence write | ACT-06 | Atomic classification — صنّف ذريًا | — | SVC-RETAINED-DEPOSIT | commitDepositClassification: order + financial event. |
| 4 | User action | ACT-01 | Reclassify later — صحّح التصنيف لاحقًا | — | SVC-RETAINED-DEPOSIT | Reverse+replace of classification event with documented from/to meaning and amounts. |


## Group — F — Inventory & materials


### FLW-024 — Tracked material inventory flow

> Arabic: دورة المادة المتابَعة · Status: **IMPLEMENTED**

- **Journey name:** Tracked material inventory flow — دورة المادة المتابَعة
- **Actor:** ACT-01
- **User intention:** Track quantity and value of a material through receipts, consumption, waste, adjustments.
- **Entry points:** /inventory; Foundation → شراء مواد قائم; Supplier purchase → استلم المواد
- **Success outcome:** Material with tracking on; movements mutate quantity/value; balances honest; everything reversible documented.
- **Primary path:** MaterialEditor (name/unit/tracking/opening knowledge) → activate tracking → receive (linked to purchase) → consume (linked to order/sale) → waste/adjust → reverse when wrong.
- **Alternative paths:** Confirm-balance mode (/inventory/material/:id/confirm) for unconfirmed openings; late inventory activation = snapshot at activation day.
- **Failure / exception paths:** Negative balance impossible — shortage ledger instead; receipts bounded by purchase remaining; unknown cost stays flagged (zero value ⇔ costKnowledge unknown).
- **Screens:** SCR-INVENTORY, SCR-MATERIAL-EDITOR, SCR-INVENTORY-MOVEMENT-EDITOR
- **Services:** SVC-INVENTORY, SVC-SUPPLIER-PURCHASE, SVC-MATERIAL-SUGGESTIONS
- **Entities:** ENT-MATERIAL, ENT-INVENTORY-MOVEMENT, ENT-SHORTAGE, ENT-INVENTORY-ACTIVATION
- **Before state:** Material untracked or absent.
- **After state:** Tracked material with movement history and derived balance.
- **Financial effect:** Value deltas move material value; consumption into delivered orders enters COGS (derivePeriodCogs).
- **Cashbox / wallet effect:** None directly (cash moves at purchase payment).
- **Profit / cost effect:** Cost-backed consumption replaces snapshot material cost for final orders; unlinked consumption = unallocatedInventoryCostMinor.
- **Inventory effect:** Quantity/value movements; moving-average within material.
- **Debt / deposit effect:** None.
- **Offline / sync behavior:** Local atomic (commitInventoryWithEvents for waste+loss).
- **Permissions / approval:** Owner.
- **History / audit behavior:** Movement records with operation keys; mirror reversals keep original costKnowledge.
- **Exit & next action:** Delivery review proposes consumption; period waste reading available.
- **Evidence:** application/inventory/inventoryMaterialService.ts (overview/activate/receivePurchase/consume/waste/adjust/reverse); src/domain/inventory-material/policies.ts; group2InventorySurfaces.test.tsx
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Register material + activate tracking — سجّل المادة وفعّل المتابعة | SCR-MATERIAL-EDITOR | SVC-INVENTORY | Opening knowledge: unconfirmed/confirmed quantity; known/unknown cost. |
| 2 | User action | ACT-01 | Receive from purchase — استلم من شراء | SCR-INVENTORY-MOVEMENT-EDITOR | SVC-INVENTORY | Receipt bounded by purchase value/quantity; purchase link is a contract (S4). |
| 3 | User action | ACT-01 | Consume for order/sale — استهلك لطلب أو بيع | SCR-INVENTORY-MOVEMENT-EDITOR | SVC-INVENTORY | Consumption needs orderId/saleId or clear reason; proportional value out. |
| 4 | System action | ACT-06 | Balance via moving average — احسب الرصيد تقريبي المتوسط | — | — | Full consumption takes remaining value (Decision 20 supports extract remainder). |
| 5 | User action | ACT-01 | Reverse movement when wrong — تراجع عن حركة عند الخطأ | SCR-INVENTORY-REVERSAL | SVC-INVENTORY | Mirror movement; waste-with-profit reversal also reverses linked loss event. |


### FLW-025 — Untracked material flow (cost reference)

> Arabic: دورة المادة غير المتابَعة · Status: **IMPLEMENTED**

- **Journey name:** Untracked material flow (cost reference) — دورة المادة غير المتابَعة
- **Actor:** ACT-01
- **User intention:** Keep a material as a cost reference only, without quantity tracking.
- **Entry points:** /inventory → أوقف المتابعة (untrack dialog); MaterialEditor tracking off
- **Success outcome:** Material serves cost suggestions (last receipt price = known) but never moves quantity; movement attempts on untracked refuse honestly.
- **Primary path:** Untrack dialog announces 4 consequences → confirm → material becomes cost reference; suggestions still read last non-reversed receipt price.
- **Alternative paths:** Retrack later (retrackMaterial); existing movements remain as history.
- **Failure / exception paths:** waste/extract/adjust on untracked refused with honest message (lines 1060-1066, 1244-1250).
- **Screens:** SCR-INVENTORY, SCR-MATERIAL-EDITOR
- **Services:** SVC-INVENTORY, SVC-MATERIAL-SUGGESTIONS
- **Entities:** ENT-MATERIAL, ENT-INVENTORY-MOVEMENT
- **Before state:** Tracked material.
- **After state:** Untracked (cost reference only).
- **Financial effect:** None from untracking.
- **Cashbox / wallet effect:** None.
- **Profit / cost effect:** Cost suggestions remain available to cost editor/calculator.
- **Inventory effect:** No quantity movements accepted.
- **Debt / deposit effect:** None.
- **Offline / sync behavior:** Local.
- **Permissions / approval:** Owner with announced consequences (S7).
- **History / audit behavior:** Tracking state changes recorded.
- **Exit & next action:** Use suggestions in cost calculator; retrack when needed.
- **Evidence:** application/inventory/inventoryMaterialService.ts (untrack/retrack, refuse paths); application/inventory/materialSuggestions.ts; contract 28 S1/S7
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Stop tracking — أوقف المتابعة | SCR-INVENTORY | SVC-INVENTORY | Dialog announces 4 consequences before confirming. |
| 2 | System action | ACT-06 | Refuse later quantity movements — ارفض أي حركة كمية لاحقة | — | SVC-INVENTORY | Waste/extract/adjust refuse with honest Arabic message. |
| 3 | System action | ACT-05 | Keep last receipt price as suggestion — ابقِ سعر آخر استلام كمقترح | — | SVC-MATERIAL-SUGGESTIONS | Known price suggestion to cost editors; no receipt → name/unit only (estimated). |


### FLW-026 — Negative inventory warning and decision

> Arabic: تحذير المخزون السالب وقراره · Status: **IMPLEMENTED**

- **Journey name:** Negative inventory warning and decision — تحذير المخزون السالب وقراره
- **Actor:** ACT-01
- **User intention:** Consume more than available without ever storing a negative balance.
- **Entry points:** InventoryMovementEditor consume; DeliveryReview shortage rows
- **Success outcome:** Explicit choice: record shortage only, or consume available + shortage (atomic); shortage ledger tracks open items; MIC-8 surfaces WARN.
- **Primary path:** Consume request above available → guard rejects direct write → options presented → record shortage OR consume-available-plus-shortage → open shortage badge.
- **Alternative paths:** Skip consumption (suggestedAction 'skip' in delivery review); resolve shortage later explicitly.
- **Failure / exception paths:** assertInventoryRemainsNonNegative everywhere — negative balance is impossible by construction (D-027).
- **Screens:** SCR-INVENTORY-MOVEMENT-EDITOR, SCR-DELIVERY-REVIEW, SCR-INVENTORY
- **Services:** SVC-INVENTORY
- **Entities:** ENT-SHORTAGE, ENT-INVENTORY-MOVEMENT
- **Before state:** Available < requested.
- **After state:** Shortage record (open) + optional partial consumption; never a negative balance.
- **Financial effect:** None beyond consumed value.
- **Cashbox / wallet effect:** None.
- **Profit / cost effect:** None.
- **Inventory effect:** Honest zero floor; shortage quantity recorded explicitly.
- **Debt / deposit effect:** None.
- **Offline / sync behavior:** Local atomic.
- **Permissions / approval:** Owner decision with visible shortage numbers.
- **History / audit behavior:** Shortage records with status open/resolved; movement linked when consuming.
- **Exit & next action:** Resolve shortage (receive more, correct records) — badge on /inventory.
- **Evidence:** src/domain/inventory-material/policies.ts (assertInventoryRemainsNonNegative, createInventoryShortage); application/inventory/inventoryMaterialService.ts (consumeWithShortage, resolveShortage); contract 28 S6/D-027
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Request consumption above available — اطلب استهلاكًا أكبر من المتاح | SCR-INVENTORY-MOVEMENT-EDITOR | SVC-INVENTORY | Guard computes shortageQuantityMilli. |
| 2 | Decision | ACT-01 | Record shortage or consume-available + shortage? — سجّل نقصًا أم استهلك المتاح + نقص؟ | SCR-INVENTORY-MOVEMENT-EDITOR | SVC-INVENTORY | Explicit decision; skip also offered in delivery review. |
| 3 | Persistence write | ACT-06 | Write shortage; negative forbidden — اكتب النقص ولا تسمح بسالب | — | SVC-INVENTORY | Open shortage tracked; badge + MIC-8 WARN. |


### FLW-027 — Recording waste that affects profit

> Arabic: تسجيل هدر يمسّ الربح · Status: **IMPLEMENTED**

- **Journey name:** Recording waste that affects profit — تسجيل هدر يمسّ الربح
- **Actor:** ACT-01
- **User intention:** Record lost/spoiled material and have its cost hit the period result (non-cash loss).
- **Entry points:** /inventory → سجّل الحل (waste); /inventory/movement/waste
- **Success outcome:** Waste movement with wasteProfitImpact=true; when cost known, a linked loss_non_cash event is written in the same atomic commit.
- **Primary path:** Waste editor → choose context (order/catalog_item/catalog_template/general_project/unallocated) → profit impact = yes → movement + loss event atomically (key ${operationKey}:loss).
- **Alternative paths:** Extract remainder (Decision 20): whole remainder leaves at full value with notification; reversal of profit-impact waste reverses movement + loss event together.
- **Failure / exception paths:** Unknown cost keeps the choice without touching result (honest flag); untracked material refuses waste.
- **Screens:** SCR-INVENTORY-MOVEMENT-EDITOR, SCR-INVENTORY
- **Services:** SVC-INVENTORY
- **Entities:** ENT-INVENTORY-MOVEMENT, ENT-FINANCIAL-EVENT
- **Before state:** Tracked material with quantity/value.
- **After state:** Quantity/value down; loss_non_cash event (operatingExpense +) when cost known.
- **Financial effect:** Non-cash loss line in period result («هالك بلا خروج نقد»).
- **Cashbox / wallet effect:** None.
- **Profit / cost effect:** Operating expense + (loss) — owner's explicit choice.
- **Inventory effect:** Waste movement (must decrease quantity & value; reason mandatory).
- **Debt / deposit effect:** None.
- **Offline / sync behavior:** Local atomic commitInventoryWithEvents.
- **Permissions / approval:** Owner explicit choice.
- **History / audit behavior:** Movement carries wasteProfitImpact flag; linked event by key; reversal reverses both.
- **Exit & next action:** Period waste reading (readPeriodWaste) shows count/value/hasUnknownCost.
- **Evidence:** application/inventory/inventoryMaterialService.ts:1285-1320 (outbound with profit choice), 1195-1220 (atomic reversal); src/domain/inventory-material/types.ts:64-67; inventoryMaterialService.test.ts:1184-1299
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Record waste — سجّل الهدر | SCR-INVENTORY-MOVEMENT-EDITOR | SVC-INVENTORY | Context + reason mandatory. |
| 2 | Decision | ACT-01 | Affect profit? — هل يمسّ الربح؟ | SCR-INVENTORY-MOVEMENT-EDITOR | SVC-INVENTORY | wasteProfitImpact true/false/null stored on movement. |
| 3 | Persistence write | ACT-06 | Atomic movement + loss event — اكتب الحركة + حدث الخسارة ذريًا | — | SVC-INVENTORY | Only when cost known; idempotency key loss suffix. |


### FLW-028 — Recording waste without profit impact

> Arabic: تسجيل هدر بلا أثر على الربح · Status: **IMPLEMENTED**

- **Journey name:** Recording waste without profit impact — تسجيل هدر بلا أثر على الربح
- **Actor:** ACT-01
- **User intention:** Disclose quantity/value loss without touching the result.
- **Entry points:** /inventory/movement/waste
- **Success outcome:** Waste movement with wasteProfitImpact=false/absent — disclosure only; no financial event.
- **Primary path:** Waste editor → profit impact = no → movement only.
- **Alternative paths:** Same reversal semantics (movement mirror only, no event to reverse).
- **Failure / exception paths:** Same guards (tracked only, reason mandatory).
- **Screens:** SCR-INVENTORY-MOVEMENT-EDITOR
- **Services:** SVC-INVENTORY
- **Entities:** ENT-INVENTORY-MOVEMENT
- **Before state:** Tracked material.
- **After state:** Quantity/value down; result untouched.
- **Financial effect:** None.
- **Cashbox / wallet effect:** None.
- **Profit / cost effect:** None — general waste value visible as separate line (generalInventoryWasteMinor) not inside resultMinor.
- **Inventory effect:** Waste movement.
- **Debt / deposit effect:** None.
- **Offline / sync behavior:** Local.
- **Permissions / approval:** Owner explicit choice.
- **History / audit behavior:** Movement record only.
- **Exit & next action:** Period waste reading shows value with hasUnknownCost flag.
- **Evidence:** application/inventory/inventoryMaterialService.ts (outbound branches); application/finance/projectFinancialService.ts:314-316 (generalInventoryWasteMinor, reason «هدر عام»)
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Record waste without cash exit — سجّل الهدر بلا خروج نقد | SCR-INVENTORY-MOVEMENT-EDITOR | SVC-INVENTORY | Also reachable from Finance quick actions («سجل هدرًا بلا خروج نقد» = loss_non_cash guided type). |
| 2 | Persistence write | ACT-06 | Movement-only write — اكتب الحركة فقط | — | SVC-INVENTORY | No linked event; flag stored. |


## Group — G — Purchases & suppliers


### FLW-029 — Creating and receiving a supplier purchase

> Arabic: تسجيل شراء مورد واستلامه · Status: **IMPLEMENTED**

- **Journey name:** Creating and receiving a supplier purchase — تسجيل شراء مورد واستلامه
- **Actor:** ACT-01
- **User intention:** Buy materials: cash out and/or supplier payable, then receive into inventory.
- **Entry points:** /suppliers → سجل شراء مواد; Foundation → شراء مواد قائم
- **Success outcome:** Purchase record with payments; receipt bridge creates inventory movements bounded by the purchase; truth line explains it is not an expense yet.
- **Primary path:** SupplierPurchaseEditor (supplier, total, initial payment, optional material link + expected quantity) → save → استلم المواد → receipt editor pre-filled → inventory movements.
- **Alternative paths:** Credit purchase (unpaid → payable); later payments (دفعة إضافية) with reversal; partial receipts (cumulative ≤ total).
- **Failure / exception paths:** No zero/over-payment; edit cannot drop totals below documented receipts; material link cannot change with standing receipts (SA-5 F3); payment reversal only for later payments.
- **Screens:** SCR-SUPPLIERS, SCR-SUPPLIER-PURCHASE-EDITOR, SCR-INVENTORY-MOVEMENT-EDITOR
- **Services:** SVC-SUPPLIER-PURCHASE, SVC-INVENTORY
- **Entities:** ENT-SUPPLIER-PURCHASE, ENT-INVENTORY-MOVEMENT, ENT-MATERIAL
- **Before state:** No purchase.
- **After state:** Purchase (paid/partially_paid/unpaid) + received inventory value.
- **Financial effect:** Cash out (initial + later payments) and/or supplier payable — NOT an operating expense and NOT COGS until consumption.
- **Cashbox / wallet effect:** Cash − per payments (allocation source link).
- **Profit / cost effect:** None until consumption (contract 09 governing rule).
- **Inventory effect:** Receipt movements (value + quantity) bounded by purchase.
- **Debt / deposit effect:** Supplier payable tracked per supplier name in parties.
- **Offline / sync behavior:** Local.
- **Permissions / approval:** Owner.
- **History / audit behavior:** Payments ledger; documented revisions with before-values; payment reversals.
- **Exit & next action:** Consume materials into orders/sales; pay remaining via دفعة إضافية.
- **Evidence:** application/suppliers/supplierPurchaseService.ts:95-97 (truth line); pages/Suppliers.tsx:90-174; pages/SupplierPurchaseEditor.tsx:479-484 (receipt bridge, no silent write TR-07)
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Record material purchase — سجّل شراء مواد | SCR-SUPPLIER-PURCHASE-EDITOR | SVC-SUPPLIER-PURCHASE | Supplier name, total, initial payment optional, material link optional. |
| 2 | Persistence write | ACT-06 | Save purchase + payments — احفظ الشراء والدفعات | — | SVC-SUPPLIER-PURCHASE | Initial payment becomes payment id ${id}:initial; status derived. |
| 3 | User action | ACT-01 | Receive materials — استلم المواد | SCR-INVENTORY-MOVEMENT-EDITOR | SVC-INVENTORY | Bridge card opens pre-filled receipt editor — no silent write. |
| 4 | Persistence write | ACT-06 | Bounded receipt write — قيّد الاستلام داخل حدود الشراء | — | SVC-INVENTORY | Cumulative value ≤ total; quantity ≤ expected; link recorded on movement. |


### FLW-030 — Working with a supplier offer (controlled catalog)

> Arabic: التعامل مع عرض مورد · Status: **PLANNED_OR_CONCEPTUAL**

- **Journey name:** Working with a supplier offer (controlled catalog) — التعامل مع عرض مورد
- **Actor:** ACT-01
- **User intention:** Receive a supplier's published offer and decide whether to buy — without any automatic commitment.
- **Entry points:** (planned) Market module «السوق والتوصيل» — currently disabled in Tools grid (not_available)
- **Success outcome:** NOT IMPLEMENTED: no supplier offer, catalog publishing, or market surface exists in code.
- **Primary path:** None today. Contract 20-N defines need/response/listing/moderation state machines; contract 25-N requires amounts as announcements that are never expenses or commitments; transfer into Manage is a separate owner-reviewed entry.
- **Alternative paths:** Today the owner's own catalog items carry optional default price/cost as proposals only (P-002) — no supplier-authored content.
- **Failure / exception paths:** N/A (not implemented).
- **Screens:** —
- **Services:** —
- **Entities:** —
- **Before state:** N/A.
- **After state:** N/A.
- **Financial effect:** Planned rule: an offer is not automatically a purchase, expense, inventory movement, or financial commitment (approved product rule; to be verified at implementation time).
- **Cashbox / wallet effect:** None today.
- **Profit / cost effect:** None today.
- **Inventory effect:** None today.
- **Debt / deposit effect:** None today.
- **Offline / sync behavior:** N/A (network expansion is out of the local product).
- **Permissions / approval:** Planned: supplier_member role publishes after moderation (contract 20-N/22-N).
- **History / audit behavior:** Planned: network audit events (contract 22-N).
- **Exit & next action:** Future-state section of the atlas; E-00 expansion contracts 20-N/24-N/25-N.
- **Evidence:** docs/contracts/20-market-need-response-listing-moderation-contract.md (CONTRACT ONLY); docs/contracts/25-network-money-representation-contract.md (announced amounts rule); pages/Tools.tsx:133,337 («السوق والتوصيل» disabled placeholder)
- **Status:** PLANNED_OR_CONCEPTUAL
- **Open gaps:** GAP-02

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | System action | ACT-06 | No implemented path — لا يوجد مسار منفذ | — | — | Tools grid shows disabled placeholder; contracts define the future state only. |


### FLW-031 — Correcting a purchase / reversing a payment

> Arabic: تصحيح شراء أو عكس دفعة · Status: **IMPLEMENTED**

- **Journey name:** Correcting a purchase / reversing a payment — تصحيح شراء أو عكس دفعة
- **Actor:** ACT-01
- **User intention:** Fix purchase totals/supplier or undo a later payment, safely against receipts.
- **Entry points:** /suppliers/purchase/:id → عدّل هذا الشراء / سجّل دفعة إضافية / عكس دفعة
- **Success outcome:** Documented edit (before-values preserved, initial payment rebuilt) or payment reversal (restores payable + reverses cash effect).
- **Primary path:** Edit → guards (total ≥ received value; material link locked with standing receipts) → revisions recorded.
- **Alternative paths:** Reverse later payment only (initial corrected via edit); effective paid = payments − documented reversals (S2-01).
- **Failure / exception paths:** Paid-after-edit bounded by new total; one reversal per payment; reversal of initial refused.
- **Screens:** SCR-SUPPLIER-PURCHASE-EDITOR
- **Services:** SVC-SUPPLIER-PURCHASE, SVC-CASH-CONTINUITY
- **Entities:** ENT-SUPPLIER-PURCHASE, ENT-CASH-ENTRY
- **Before state:** Existing purchase.
- **After state:** Corrected purchase with revision trail.
- **Financial effect:** Cash/payable adjusted by difference; correction history row purchase_edit (beforeTotal − total).
- **Cashbox / wallet effect:** Payment reversal reverses its cash effect.
- **Profit / cost effect:** None (still not expense).
- **Inventory effect:** Receipts preserved; guards prevent inconsistency.
- **Debt / deposit effect:** Payable restored by reversal.
- **Offline / sync behavior:** Local.
- **Permissions / approval:** Owner.
- **History / audit behavior:** revisions[] with before-values; paymentReversals[].
- **Exit & next action:** Receive remaining or settle payable.
- **Evidence:** src/domain/supplier-purchase/policies.ts (updateSupplierPurchase, reverseSupplierPurchasePayment); tests/domain/supplier-purchase-corrections.test.ts
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Edit purchase — عدّل هذا الشراء | SCR-SUPPLIER-PURCHASE-EDITOR | SVC-SUPPLIER-PURCHASE | Before-values preserved in revision; initial payment rebuilt. |
| 2 | User action | ACT-01 | Reverse a later payment — عكس دفعة لاحقة | — | SVC-SUPPLIER-PURCHASE | One reversal per payment; initial corrected via edit. |
| 3 | Persistence write | ACT-06 | Rebuild state — أعد بناء الحالة | — | SVC-SUPPLIER-PURCHASE | Status derived from effective paid. |


## Group — H — Cost & pricing


### FLW-032 — Product/cost calculation flow (calculator → estimate → draft)

> Arabic: حساب التكلفة والسعر · Status: **IMPLEMENTED**

- **Journey name:** Product/cost calculation flow (calculator → estimate → draft) — حساب التكلفة والسعر
- **Actor:** ACT-01
- **User intention:** Think through cost and price before committing to any number.
- **Entry points:** /tools → حاسبة التكلفة والسعر; OrderDraft → CostEditor
- **Success outcome:** Live preview (plannedCost, unitCost, priceFloor, knowledgeState) with zero financial effect; estimate saved; optional draft started from estimate.
- **Primary path:** Calculator (materials from suggestions + time + extras) → save estimate → /tools/estimate/:id → ابدأ مسودة من هذا التقدير (values copied as editable proposals).
- **Alternative paths:** CostEditor per-draft snapshots (versioned); protection price as agreement start value only when knowledge not incomplete/partial.
- **Failure / exception paths:** Unknown prices stay unknown (incomplete blocks final result); unit cost ceil vector 100÷3=34 intentional (protective display).
- **Screens:** SCR-COST-CALCULATOR, SCR-ESTIMATE-DETAIL, SCR-COST-EDITOR
- **Services:** SVC-COST-ESTIMATE, SVC-COST, SVC-MATERIAL-SUGGESTIONS
- **Entities:** ENT-ESTIMATE, ENT-DRAFT
- **Before state:** Thinking phase.
- **After state:** Saved estimate (zero effect); optional draft with copied proposals.
- **Financial effect:** None — saving touches nothing (U004 evidence).
- **Cashbox / wallet effect:** None.
- **Profit / cost effect:** None until order snapshot exists.
- **Inventory effect:** None (reads suggestions only).
- **Debt / deposit effect:** None.
- **Offline / sync behavior:** Local.
- **Permissions / approval:** Owner.
- **History / audit behavior:** Estimate edit history; draft link sourceEstimateId.
- **Exit & next action:** Record agreement from draft (price owned by owner).
- **Evidence:** pages/CostCalculator.tsx; pages/EstimateDetail.tsx:204-220; application/estimates/costEstimateService.ts; U004.dom.test.tsx (no financial movement)
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Open calculator — افتح الحاسبة | SCR-COST-CALCULATOR | SVC-COST-ESTIMATE | Material suggestions with known price from last receipt; unknown stays unknown. |
| 2 | System action | ACT-06 | Live knowledge-honest preview — معاينة حية بالمعرفة | — | SVC-COST-ESTIMATE | knowledgeState derived (known/estimated/incomplete/stale/variable). |
| 3 | User action | ACT-01 | Save estimate + start draft — احفظ التقدير وابدأ مسودة | SCR-ESTIMATE-DETAIL | SVC-COST-ESTIMATE | Copied values are editable proposals; estimate unchanged. |


## Group — I — Assets & loans


### FLW-033 — Asset creation and depreciation

> Arabic: إنشاء الأصل والإهلاك · Status: **IMPLEMENTED**

- **Journey name:** Asset creation and depreciation — إنشاء الأصل والإهلاك
- **Actor:** ACT-01
- **User intention:** Buy a long-use item and charge its depreciation explicitly.
- **Entry points:** /assets → أضف أصلًا (also Finance → افتح سجل الأصول)
- **Success outcome:** Asset record + acquisition event (cash or payable); depreciation as proposal → explicit event(s); book value always derived from events.
- **Primary path:** AssetEditor (شراء للاستخدام الطويل: practical classification questions, دفعت نقدًا / على الذمم, عمر طويل؟) → save → /assets/:id → سجّل الإهلاك المستحق (proposal → confirm).
- **Alternative paths:** Immediate-expense choice (لا، يُستهلك فورًا); «لا يُسجَّل مصروفًا هذا الشهر» defers; contract revisions for life/start changes.
- **Failure / exception paths:** Unknown life/start ⇒ no schedule, no guessing (readiness states); depreciation recording only via explicit confirmation («المستحق جدولةً لا يدخل الربح إلا بتسجيل صريح»).
- **Screens:** SCR-ASSETS, SCR-ASSET-EDITOR, SCR-ASSET-DETAIL
- **Services:** SVC-ASSET
- **Entities:** ENT-ASSET, ENT-FINANCIAL-EVENT
- **Before state:** No asset.
- **After state:** Active asset; monthly schedule; recorded depreciation events.
- **Financial effect:** Acquisition = capital (cash − or payable +, asset +), NOT expense; depreciation = non-cash expense; never auto.
- **Cashbox / wallet effect:** Cash out at acquisition (cash kind).
- **Profit / cost effect:** asset_depreciation line in period result when recorded.
- **Inventory effect:** None.
- **Debt / deposit effect:** Payable variant creates supplier-style payable.
- **Offline / sync behavior:** Local atomic commitAssetRecord.
- **Permissions / approval:** Owner; every depreciation is an explicit decision.
- **History / audit behavior:** contractRevisions[] documented; corrections only while active (archived freeze).
- **Exit & next action:** Record next month depreciation; revise contract; dispose at end of life.
- **Evidence:** pages/AssetEditor.tsx (labels); application/assets/assetService.ts; src/domain/asset/policies.ts:133-256; G4Assets.dom.test.tsx
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Record asset purchase — سجّل شراء أصل | SCR-ASSET-EDITOR | SVC-ASSET | Long-use question + payment kind; effect preview before save. |
| 2 | Persistence write | ACT-06 | Atomic asset + acquisition event — أصل + حدث اقتناء ذريًا | — | SVC-ASSET | Capital, not operating expense (no hidden depreciation). |
| 3 | System action | ACT-05 | Propose depreciation schedule — اقترح جدول الإهلاك | SCR-ASSET-DETAIL | SVC-ASSET | Floor-rounded monthly; readiness honest (unknown_life/unknown_start). |
| 4 | User action | ACT-01 | Record due depreciation explicitly — سجّل الإهلاك المستحق | SCR-ASSET-DETAIL | SVC-ASSET | Proposal → event; schedule never auto-charges. |


### FLW-034 — Asset reaching zero while remaining in use

> Arabic: وصول الأصل للصفر مع بقائه مستخدمًا · Status: **IMPLEMENTED**

- **Journey name:** Asset reaching zero while remaining in use — وصول الأصل للصفر مع بقائه مستخدمًا
- **Actor:** ACT-01
- **User intention:** Continue owning/using an asset after its book value reaches zero.
- **Entry points:** /assets/:id after full schedule
- **Success outcome:** fully_depreciated readiness; asset remains active (status not changed); last month absorbs remainder; depreciation stops.
- **Primary path:** Schedule completes → scheduledAccumulated = acquisition → readiness fully_depreciated; note «استُهلك الجدول كاملًا — الدفتري صفر بمقتضى العقد.»; no more proposals.
- **Alternative paths:** Contract revision can extend life (documented revision — new schedule); disposal/write-off are separate events any time.
- **Failure / exception paths:** Reversing depreciation after disposal/write-off is rejected (AV-08 — prevents resurrecting voided value); recording more depreciation after disposal refused (retired).
- **Screens:** SCR-ASSET-DETAIL
- **Services:** SVC-ASSET
- **Entities:** ENT-ASSET, ENT-FINANCIAL-EVENT
- **Before state:** Active asset with remaining schedule.
- **After state:** Active asset, book value 0, owned and in use.
- **Financial effect:** No further expense lines.
- **Cashbox / wallet effect:** None.
- **Profit / cost effect:** Depreciation line only from recorded events.
- **Inventory effect:** None.
- **Debt / deposit effect:** None.
- **Offline / sync behavior:** Local.
- **Permissions / approval:** Owner.
- **History / audit behavior:** Schedule derived; revisions documented.
- **Exit & next action:** Dispose or write off when actually retired (separate events).
- **Evidence:** src/domain/asset/policies.ts:247 (fully depreciated note); docs/decisions/final-continuation-conflict-resolutions-v1.md (Conflict G/AV-08)
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | System action | ACT-06 | Complete schedule — أكمل الجدول | — | SVC-ASSET | Last month absorbs remainder; accumulated = acquisition. |
| 2 | System action | ACT-06 | Asset stays active at zero book value — الأصل يبقى نشطًا بقيمة صفر | SCR-ASSET-DETAIL | SVC-ASSET | Depreciation-to-zero ≠ disposal (Conflict G). |
| 3 | System action | ACT-06 | Refuse post-disposal depreciation reversal — ارفض إهلاكًا بعد التخلص | — | SVC-ASSET | AV-08 guard. |


### FLW-035 — Asset disposal and correction boundaries

> Arabic: التخلص من الأصل وحدود التصحيح · Status: **IMPLEMENTED**

- **Journey name:** Asset disposal and correction boundaries — التخلص من الأصل وحدود التصحيح
- **Actor:** ACT-01
- **User intention:** Sell or scrap the asset and understand what can still be corrected afterwards.
- **Entry points:** /assets/:id → تخلّص من الأصل أو اشطبه
- **Success outcome:** Disposal event: proceeds in, frozen book value, declared gain/loss; or write-off event (non-cash loss of remaining book value).
- **Primary path:** AssetDetail → dispose (proceeds amount, reason) → asset_disposal_cash event (cash + proceeds; assetDelta − bookValue) → status disposed.
- **Alternative paths:** Write-off (شطب) requires bookValue > 0 else refused («لا رصيد دفتري يُشطب»); acquisition correction allowed only while active (archived = frozen, AV-08).
- **Failure / exception paths:** Disposal requires active asset; post-disposal corrections locked with honest messages; depreciation reversal after disposal rejected.
- **Screens:** SCR-ASSET-DETAIL
- **Services:** SVC-ASSET, SVC-CORRECTION-HISTORY
- **Entities:** ENT-ASSET, ENT-FINANCIAL-EVENT
- **Before state:** Active asset.
- **After state:** disposed/written_off; frozen book value; correction boundaries locked.
- **Financial effect:** Disposal: cash + proceeds, declared result proceeds − bookValue; write-off: non-cash loss.
- **Cashbox / wallet effect:** Disposal proceeds in.
- **Profit / cost effect:** assetDisposalResultMinor / assetWriteOffLossMinor separate declared lines (never mixed into operating expenses).
- **Inventory effect:** None.
- **Debt / deposit effect:** None.
- **Offline / sync behavior:** Local.
- **Permissions / approval:** Owner with preview.
- **History / audit behavior:** Disposal/write-off records with events; asset_correction + asset_contract_revision rows in correction history.
- **Exit & next action:** Period result shows declared lines; assets list shows archived state.
- **Evidence:** src/domain/asset/policies.ts:261-330 (disposal/write-off); application/assets/assetService.ts:231-351 (active-only corrections)
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Dispose of asset — تخلّص من الأصل | SCR-ASSET-DETAIL | SVC-ASSET | Proceeds + reason; book value frozen at event moment. |
| 2 | Persistence write | ACT-06 | Disposal event — حدث التخلص | — | SVC-ASSET | Two declared amounts: proceeds (cash), book value (context). |
| 3 | User action | ACT-01 | Write off when scrap — اشطب عند اللزوم | SCR-ASSET-DETAIL | SVC-ASSET | Non-cash loss at remaining book value; requires > 0. |


### FLW-036 — Loan creation and repayment

> Arabic: إقراض مال واسترداده · Status: **IMPLEMENTED**

- **Journey name:** Loan creation and repayment — إقراض مال واسترداده
- **Actor:** ACT-01
- **User intention:** Record money lent to someone and its repayments.
- **Entry points:** /loans → أضف قرضًا (also Finance → افتح سجل القروض)
- **Success outcome:** Loan record + loan_outgoing_cash event (cash −, loan +); repayments with events; outstanding derived; settled state; full history preserved.
- **Primary path:** LoanEditor (أعطيت مالًا يُعاد: borrower, amount, date, source wallet) → save → /loans/:id → repay via bottom sheet (RepaymentSheet with impact preview + overpayment guard).
- **Alternative paths:** Correct loan (name/principal) = atomic reverse+replace of principal event; reverse a repayment (documented).
- **Failure / exception paths:** Repayment ≤ outstanding (no overpay); no payments after settled; concurrency guard rejects stale writes (loanCommitGuard, AV-02).
- **Screens:** SCR-LOANS, SCR-LOAN-EDITOR, SCR-LOAN-DETAIL
- **Services:** SVC-LOAN, SVC-CASH-CONTINUITY
- **Entities:** ENT-LOAN, ENT-FINANCIAL-EVENT
- **Before state:** No loan.
- **After state:** Open/settled loan; repayments history kept.
- **Financial effect:** «الدَّين ليس مصروفًا» — loan is neither expense nor owner draw; repayment is cash in, not income.
- **Cashbox / wallet effect:** Cash out at creation; cash in per repayment (source wallet).
- **Profit / cost effect:** None ever.
- **Inventory effect:** None.
- **Debt / deposit effect:** loansOutstandingMinor in position.
- **Offline / sync behavior:** Local atomic commitLoanRecord.
- **Permissions / approval:** Owner with impact preview.
- **History / audit behavior:** loan_correction rows; repayment reversals marked; outstanding always derived.
- **Exit & next action:** Repay more; correct data; view loans overview.
- **Evidence:** pages/LoanEditor.tsx; components/loans/RepaymentSheet.tsx; application/loans/loanService.ts; G4Loans.dom.test.tsx
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Record loan — سجّل القرض | SCR-LOAN-EDITOR | SVC-LOAN | Borrower, amount, date, source wallet; explicit preview (no profit/expense). |
| 2 | Persistence write | ACT-06 | Atomic loan + event — قرض + حدث ذري | — | SVC-LOAN | commitLoanRecord with loanCommitGuard. |
| 3 | User action | ACT-01 | Record repayment — سجّل سدادًا | SCR-LOAN-DETAIL | SVC-LOAN | Bottom sheet with impact preview; overpayment guarded. |
| 4 | User action | ACT-01 | Correct loan data — صحّح بيانات القرض | SCR-LOAN-DETAIL | SVC-LOAN | Atomic reverse+replace of principal event; principal ≥ active repayments. |


## Group — J — External delivery


### FLW-037 — Delivery company assignment (external)

> Arabic: إسناد التوصيل لشركة خارجية · Status: **PLANNED_OR_CONCEPTUAL**

- **Journey name:** Delivery company assignment (external) — إسناد التوصيل لشركة خارجية
- **Actor:** ACT-01
- **User intention:** Assign an order to a delivery company and share only the operational data it needs.
- **Entry points:** (planned) — no implemented entry point
- **Success outcome:** NOT IMPLEMENTED: no assignment, courier data, quote, or status surface exists.
- **Primary path:** None today. Contract 21-N defines draft→submitted_for_quote→courier_reviewing→quote_submitted→requester_accepted_quote→booked→source_ready→picked_up→in_transit→arrived_or_completed with exception states; disclosure matrix limits what the courier sees before quoting.
- **Alternative paths:** None implemented; current 'delivery' = customer order delivery (internal).
- **Failure / exception paths:** N/A.
- **Screens:** —
- **Services:** —
- **Entities:** —
- **Before state:** N/A.
- **After state:** N/A.
- **Financial effect:** Planned rule: delivery companies receive only explicitly assigned orders and operational delivery data (approved rule, verified as future state); quotes are announcements, never expenses.
- **Cashbox / wallet effect:** None today.
- **Profit / cost effect:** None today (deliveryMinor cost line exists on orders as a planned cost component).
- **Inventory effect:** None.
- **Debt / deposit effect:** None.
- **Offline / sync behavior:** N/A.
- **Permissions / approval:** Planned: courier_member role with delivery_scoped data classification (contract 24-N).
- **History / audit behavior:** Planned: immutable status events + audit events.
- **Exit & next action:** Future-state section; E-00 contracts.
- **Evidence:** docs/contracts/21-delivery-request-quote-status-privacy-contract.md (CONTRACT ONLY); grep deliveryCompany: docs only
- **Status:** PLANNED_OR_CONCEPTUAL
- **Open gaps:** GAP-03

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | System action | ACT-06 | No implemented path — لا يوجد مسار منفذ | — | — | Internal delivery (FLW-011) is the only delivery implemented. |


### FLW-038 — Delivery with collection (collect at delivery)

> Arabic: التسليم مع التحصيل · Status: **IMPLEMENTED**

- **Journey name:** Delivery with collection (collect at delivery) — التسليم مع التحصيل
- **Actor:** ACT-01
- **User intention:** Deliver and collect the money in the same trusted moment.
- **Entry points:** DeliveryReview → optional collect-now field
- **Success outcome:** Delivery transaction includes a cash collection into an explicit wallet — exactly one revenue recognition, cash recorded once.
- **Primary path:** DeliveryReview → choose wallet + amount ≤ remaining → single confirm → commitOrderDelivery writes transition + consumption + collection entry (allocation sourceRefLineId = delivery event).
- **Alternative paths:** Collect later via sheet; register remainder as debt.
- **Failure / exception paths:** No destination wallet → collection blocked (G3Delivery: «لا تحصيل بلا وجهة»); amount above remaining refused.
- **Screens:** SCR-DELIVERY-REVIEW
- **Services:** SVC-DELIVERY-REVIEW, SVC-CASH-CONTINUITY
- **Entities:** ENT-CRAFT-ORDER, ENT-CASH-ENTRY
- **Before state:** ready order.
- **After state:** delivered (+collected), possibly settled.
- **Financial effect:** Revenue once (delivery); collection is cash only.
- **Cashbox / wallet effect:** Cash in to chosen wallet with source link.
- **Profit / cost effect:** Profit from price − cost (once).
- **Inventory effect:** Consumption in same transaction.
- **Debt / deposit effect:** Deposit applied once; remainder tracked.
- **Offline / sync behavior:** Local atomic.
- **Permissions / approval:** Owner single confirm.
- **History / audit behavior:** Delivery event + allocation entry linked by id.
- **Exit & next action:** Order settles or remainder registered.
- **Evidence:** application/fulfillment/deliveryReviewService.ts:308-549; G3Delivery.dom.test.tsx (no collection without destination)
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Decision | ACT-01 | Collect at delivery? — قبض عند التسليم؟ | SCR-DELIVERY-REVIEW | SVC-DELIVERY-REVIEW | Optional; wallet choice mandatory if collecting. |
| 2 | Persistence write | ACT-06 | One atomic delivery + collection — تسليم + تحصيل ذري واحد | — | SVC-DELIVERY-REVIEW | Allocation linked to delivery event id. |


### FLW-039 — Delivery failure, dispute, or correction

> Arabic: فشل التسليم أو تصحيحه · Status: **IMPLEMENTED**

- **Journey name:** Delivery failure, dispute, or correction — فشل التسليم أو تصحيحه
- **Actor:** ACT-01
- **User intention:** Undo a wrong delivery record and redo it correctly.
- **Entry points:** OrderDetail after delivery → reverse delivery (documented reason)
- **Success outcome:** reverseDelivery: order → needs_review; recognized revenue/cost zeroed; consumption mirror-reversed; collected cash stays; then resume (needs_review → confirmed → in_progress) and re-deliver with NEW attempt key.
- **Primary path:** Reverse delivery (reason) → atomic commitOrderDeliveryReversal → review state → resumeAfterReview → work again → deliver-N (new idempotency key) → revenue re-recognized; period attribution follows last effective delivery (FT-01).
- **Alternative paths:** Cancel from needs_review when it completes safely (AV-07) with impact preview; otherwise honest lock-with-reason.
- **Failure / exception paths:** Reversal requires delivered/settled; double reversal refused; no delivery event found → honest error; cancel path blocked when unsafe.
- **Screens:** SCR-ORDER-DETAIL
- **Services:** SVC-DELIVERY-REVIEW, SVC-FULFILLMENT, SVC-INVENTORY
- **Entities:** ENT-CRAFT-ORDER, ENT-INVENTORY-MOVEMENT
- **Before state:** delivered/settled order.
- **After state:** needs_review → (resume or cancel); history preserved.
- **Financial effect:** Revenue/cost voided on reversal; re-recognized at re-delivery; cash collected stays (documented).
- **Cashbox / wallet effect:** None on reversal (cash fact kept).
- **Profit / cost effect:** resultStatus review_required, profit null until re-delivery.
- **Inventory effect:** Consumption movements mirror-reversed with original costKnowledge.
- **Debt / deposit effect:** Deposit card reflects non-delivered state.
- **Offline / sync behavior:** Local atomic.
- **Permissions / approval:** Owner with documented reason; AV-07 safe-completion rule for cancel.
- **History / audit behavior:** delivery_reversed event + correction history row (amountEffect null — revenue voided).
- **Exit & next action:** Resume → re-deliver (new key), or cancel with deposit path.
- **Evidence:** src/domain/craft-order/policies.ts:814+ (reverseDelivery requires delivered); application/fulfillment/deliveryReviewService.ts:553-637 (mirror reversals, atomic); application/finance/projectFinancialService.redelivery.test.ts (FT-01 attribution); G3.dom.test.tsx:647-660 (cancel-from-needs_review)
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Reverse delivery with reason — اعكس التسليم بسبب | SCR-ORDER-DETAIL | SVC-DELIVERY-REVIEW | Documented reason mandatory. |
| 2 | Persistence write | ACT-06 | Voided revenue + mirror-reversed consumption — إيراد مُحيَّد + حركات معكوسة مرآة | — | SVC-DELIVERY-REVIEW | «الإيراد يُحيَّد، حركات الاستهلاك تُعكس مرآةً، الكاش المقبوض يبقى». |
| 3 | User action | ACT-01 | Resume after review or cancel — استأنف أو ألغِ | SCR-ORDER-DETAIL | SVC-FULFILLMENT | needs_review → provisional_agreement/confirmed (resume) or safe cancel (AV-07). |
| 4 | User action | ACT-01 | Re-deliver with new attempt key — أعد التسليم بمفتاح جديد | SCR-DELIVERY-REVIEW | SVC-DELIVERY-REVIEW | ${id}:deliver-N; period reads last effective delivery. |


## Group — K — Data & resilience


### FLW-040 — Backup creation (verified export)

> Arabic: إنشاء نسخة احتياطية موثقة · Status: **IMPLEMENTED**

- **Journey name:** Backup creation (verified export) — إنشاء نسخة احتياطية موثقة
- **Actor:** ACT-01
- **User intention:** Get a trustworthy local backup file of the entire financial state.
- **Entry points:** Settings → بياناتي → verified export; Reset flow forces a verified export first
- **Success outcome:** File micro-local-YYYY-MM-DD.json downloaded; envelope v27 with sha256 digest + counts; round-trip re-parse verified before declaring success; lastVerifiedExportAt stamped.
- **Primary path:** Settings → export (PIN-gated once per session) → createVerifiedExport (full re-parse of the produced file) → Blob download → preference markVerifiedExport.
- **Alternative paths:** Reminder settings (backupReminderEnabled); honest 'no cloud in this version' copy.
- **Failure / exception paths:** Lock enabled but wrong PIN → backoff counter; export failure → honest notice, nothing claimed.
- **Screens:** SCR-SETTINGS
- **Services:** SVC-LOCAL-TRANSFER, SVC-PREFERENCE
- **Entities:** ENT-EXPORT-FILE, ENT-SECURITY
- **Before state:** Any local state.
- **After state:** Backup file on device; verified stamp recorded.
- **Financial effect:** None (read + serialize).
- **Cashbox / wallet effect:** None.
- **Profit / cost effect:** None.
- **Inventory effect:** None (snapshot included in file).
- **Debt / deposit effect:** None (snapshot included).
- **Offline / sync behavior:** Fully offline; SHA-256 computed synchronously (syncSha256) because import validation is sync.
- **Permissions / approval:** PIN proof per session when lock enabled (SP-01/DP-04).
- **History / audit behavior:** Digest over JSON of snapshot; counts embedded; app version recorded.
- **Exit & next action:** Keep file safe; import on another device/browser (FLW-041).
- **Evidence:** application/transfers/localTransferService.ts:2904 (createVerifiedExport); pages/Settings.tsx:196-229; localTransferService.envelope27.test.ts
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Request verified export — اطلب تصديرًا موثقًا | SCR-SETTINGS | SVC-LOCAL-TRANSFER | PIN gate first (once per session). |
| 2 | System action | ACT-06 | Create, digest, round-trip re-parse — أنشئ وحدّث وأعد التحليل | — | SVC-LOCAL-TRANSFER | File trustworthy only after re-parse succeeds. |
| 3 | User action | ACT-01 | Download file — نزّل الملف | SCR-SETTINGS | — | micro-local-YYYY-MM-DD.json; verified stamp saved. |


### FLW-041 — Restore: rejection and successful restore

> Arabic: الاستعادة: الرفض والنجاح · Status: **IMPLEMENTED**

- **Journey name:** Restore: rejection and successful restore — الاستعادة: الرفض والنجاح
- **Actor:** ACT-01
- **User intention:** Replace local data from a backup file, safely.
- **Entry points:** Settings → import file
- **Success outcome:** Preview (file summary + what will be replaced) → PIN-gated confirm → atomic replaceSnapshot → post-restore integrity check (PASS/WARN/FAIL) with deep link.
- **Primary path:** prepareImport (parse + version-pair allowlist + digest + counts + deep validateSnapshot incl. family orphans) → preview → confirmImport → integrityCheck.run().
- **Alternative paths:** Legacy envelopes accepted (18,27)…(26,34) with no-invented-history migrations; guided opening import separate flow (FLW-004).
- **Failure / exception paths:** 11 rejection rules leave device data untouched: bad JSON/format/version pair/exportedAt/data, malformed integrity, digest mismatch (tamper), missing integrity on current-version file (AV-04), missing counts, counts mismatch (DP-01), snapshot validation failure, family orphans (AI-01), storage error.
- **Screens:** SCR-SETTINGS, SCR-TOOLS-INTEGRITY
- **Services:** SVC-LOCAL-TRANSFER, SVC-INTEGRITY-CHECK
- **Entities:** ENT-EXPORT-FILE
- **Before state:** Any local state.
- **After state:** Replaced state (or untouched on rejection) + integrity report.
- **Financial effect:** Whole-state replacement in one readwrite transaction (form-drafts and local-security excluded by design).
- **Cashbox / wallet effect:** All wallets/entries replaced.
- **Profit / cost effect:** All events replaced.
- **Inventory effect:** All movements replaced.
- **Debt / deposit effect:** All orders/loans replaced.
- **Offline / sync behavior:** Offline; no network at any step.
- **Permissions / approval:** PIN-gated confirm; explicit preview of counts to be replaced.
- **History / audit behavior:** Envelope carries digest + counts; replace is atomic; nothing partially written.
- **Exit & next action:** Open /tools/integrity; continue working.
- **Evidence:** application/transfers/localTransferService.ts:2487-2584 (rejection rules), 1425-2410 (validateSnapshot); localTransferService.familyOrphan.test.ts (AI-01); localTransferService.schema34.test.ts
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Choose backup file — اختر ملف النسخة | SCR-SETTINGS | SVC-LOCAL-TRANSFER | Read via file input; parsed synchronously. |
| 2 | System action | ACT-06 | Validate fully or reject honestly — تحقق شامل أو ارفض | — | SVC-LOCAL-TRANSFER | Rejection leaves device data untouched with Arabic message. |
| 3 | User action | ACT-01 | Review replacement preview — راجع معاينة الاستبدال | SCR-SETTINGS | SVC-LOCAL-TRANSFER | File counts + current local counts («ما سيُستبدل»). |
| 4 | User action | ACT-01 | Confirm import (PIN-gated) — أكّد الاستيراد | SCR-SETTINGS | SVC-LOCAL-TRANSFER | Atomic replaceSnapshot in one transaction. |
| 5 | System action | ACT-06 | Run integrity check post-restore — افحص السلامة بعد الاستعادة | SCR-TOOLS-INTEGRITY | SVC-INTEGRITY-CHECK | PASS/WARN/FAIL note + deep link (Settings.tsx:332-339). |


### FLW-042 — Reset (start anew)

> Arabic: البدء من جديد · Status: **IMPLEMENTED**

- **Journey name:** Reset (start anew) — البدء من جديد
- **Actor:** ACT-01
- **User intention:** Wipe everything and start over — without losing the chance to keep a backup.
- **Entry points:** Settings → ابدأ من جديد
- **Success outcome:** Verified export forced first; name confirmation + PIN; atomic replace with empty snapshot; setup draft cleared; back to /setup.
- **Primary path:** resetFlow: export (mandatory) → name-typed confirmation → PIN gate → resetAll → navigate /setup.
- **Alternative paths:** إلغاء — بياناتي تبقى at any stage.
- **Failure / exception paths:** Wrong PIN → backoff; export failure blocks reset (honest).
- **Screens:** SCR-SETTINGS, SCR-SETUP
- **Services:** SVC-LOCAL-TRANSFER, SVC-PREFERENCE
- **Entities:** ENT-EXPORT-FILE
- **Before state:** Existing data.
- **After state:** Empty snapshot; setup wizard state.
- **Financial effect:** All local financial truth deleted (after backup chance).
- **Cashbox / wallet effect:** All wallets cleared.
- **Profit / cost effect:** All events cleared.
- **Inventory effect:** All materials/movements cleared.
- **Debt / deposit effect:** All debts cleared.
- **Offline / sync behavior:** Offline.
- **Permissions / approval:** PIN + typed name confirmation (double explicit).
- **History / audit behavior:** No partial resets (atomic).
- **Exit & next action:** Setup wizard (FLW-001).
- **Evidence:** pages/Settings.tsx:240-286, 548-598; application/transfers/localTransferService.ts:2958 (resetAll)
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Start anew — ابدأ من جديد | SCR-SETTINGS | SVC-LOCAL-TRANSFER | Forces verified export first. |
| 2 | User action | ACT-01 | Type name to confirm — اكتب الاسم للتأكيد | SCR-SETTINGS | — | Double explicit confirmation + PIN. |
| 3 | Persistence write | ACT-06 | Atomic empty replace — استبدال ذري بوضع فارغ | — | SVC-LOCAL-TRANSFER | Also removes localStorage setup draft; navigate /setup. |


### FLW-043 — Local-first / offline capture and honest status

> Arabic: العمل المحلي بلا اتصال وحالته الصادقة · Status: **IMPLEMENTED**

- **Journey name:** Local-first / offline capture and honest status — العمل المحلي بلا اتصال وحالته الصادقة
- **Actor:** ACT-01
- **User intention:** Keep working with no connectivity and know exactly what state the app is in.
- **Entry points:** Any surface while offline; PWA update card; Install banner
- **Success outcome:** All writes succeed offline; offline card states honestly: «لا مزامنة ولا نسخة سحابية في هذه النسخة» — Micro continues from local data; updates wait for approval.
- **Primary path:** Offline → runtime notice card (role=status) → keep recording (IndexedDB writes) → optionally install as PWA for offline app shell.
- **Alternative paths:** Update flow: onNeedRefresh → card; if dirty forms exist, reload refused (S2-11) until saved; applyPwaUpdate with card restore on failure.
- **Failure / exception paths:** SW registration failure → honest message (local app mode failed; continues from browser); storage unavailable → recovery screen.
- **Screens:** SCR-PWA-NOTICE
- **Services:** SVC-PWA
- **Entities:** ENT-PROFILE
- **Before state:** Any.
- **After state:** Working state unchanged; statuses honest.
- **Financial effect:** None (all writes already local-first).
- **Cashbox / wallet effect:** None.
- **Profit / cost effect:** None.
- **Inventory effect:** None.
- **Debt / deposit effect:** None.
- **Offline / sync behavior:** This IS the offline behavior: zero network calls in client src (verified by grep); no runtime caching routes; precache + SPA fallback only.
- **Permissions / approval:** Update application requires owner tap.
- **History / audit behavior:** Install banner dismissal persisted 30 days (preferences).
- **Exit & next action:** Continue work; approve update when ready.
- **Evidence:** apps/prototype-web/client/src/pwa/PwaRuntimeNotice.tsx:91-104; pwa/register.ts:51-59; vite.config.ts:221-254 (registerType prompt, no runtime caching); grep fetch/WebSocket/XMLHttpRequest over client src: zero matches
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | System action | ACT-06 | Monitor connectivity — راقب الاتصال | SCR-PWA-NOTICE | SVC-PWA | Offline card appears with honest copy (no sync, no cloud). |
| 2 | User action | ACT-01 | Keep recording offline — تابع التسجيل بلا اتصال | — | — | All writes are local IndexedDB transactions. |
| 3 | Decision | ACT-01 | Apply update now or later? — حدّث الآن أم لاحقًا؟ | SCR-PWA-NOTICE | SVC-PWA | Refuses reload over dirty forms; waits for approval. |


### FLW-044 — Assistant question and sourced answer (guidance)

> Arabic: سؤال للمساعد وإجابة موثقة · Status: **PARTIALLY_IMPLEMENTED**

- **Journey name:** Assistant question and sourced answer (guidance) — سؤال للمساعد وإجابة موثقة
- **Actor:** ACT-01
- **User intention:** Ask 'what's wrong with my numbers?' or 'what does this mean?' and get a deterministic, sourced answer.
- **Entry points:** /tools/integrity (فحص سلامة مالي); In-flow guidance panels (لماذا؟ disclosures); Event effect previews
- **Success outcome:** 16 read-only MIC checks with results and deep links to fix at the source; guidance messages follow event → effect → next action template; nothing is changed by the 'assistant'.
- **Primary path:** Finance → فحص سلامة مالي — اطمئن على أرقامك → run → PASS/WARN/FAIL per check → افتح السجل المعني deep link.
- **Alternative paths:** Guidance disclosures inside editors (لماذا؟ collapsed explanations); knowledge-gap cards on order surfaces; honest empty states naming the next step.
- **Failure / exception paths:** Checks never auto-fix; failing check states exactly which record to open.
- **Screens:** SCR-TOOLS-INTEGRITY, SCR-FINANCE
- **Services:** SVC-INTEGRITY-CHECK, SVC-PROJECT-FINANCE
- **Entities:** ENT-ACTIVITY-ROW
- **Before state:** Data possibly inconsistent.
- **After state:** Owner informed; fixes happen through their own flows.
- **Financial effect:** None (read-only: «يقرأ أرقامك ولا يغيّر شيئًا»).
- **Cashbox / wallet effect:** None.
- **Profit / cost effect:** None.
- **Inventory effect:** None.
- **Debt / deposit effect:** None.
- **Offline / sync behavior:** Local.
- **Permissions / approval:** Owner.
- **History / audit behavior:** MIC check ids stable (MIC-1..13); results derived each run.
- **Exit & next action:** Open the flagged record and correct through its own flow.
- **Evidence:** pages/ToolsIntegrity.tsx (16 checks, label); application/finance/integrityCheckService.ts; docs/product/guidance-interaction-policy-v1.md; ToolsIntegrity.ui.test.tsx
- **Status:** PARTIALLY_IMPLEMENTED
- **Open gaps:** GAP-01

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Open integrity check — افتح فحص السلامة | SCR-TOOLS-INTEGRITY | SVC-INTEGRITY-CHECK | Read-only audit across money/events/amanah/inventory/assets/loans/deposits. |
| 2 | System action | ACT-05 | Show sourced results — أظهر النتائج بمصادرها | SCR-TOOLS-INTEGRITY | SVC-INTEGRITY-CHECK | Every check has id, status, and fix-at-source deep link. |
| 3 | User action | ACT-01 | Open the relevant record — افتح السجل المعني | — | — | Corrections happen in the record's own flow — never here. |
| 4 | System action | ACT-06 | No conversational assistant exists — لا مساعد حواري | — | — | Guidance is deterministic and template-based; no AI integration (GAP-01). |


### FLW-045 — Draft requiring explicit confirmation

> Arabic: مسودة تتطلب تأكيدًا صريحًا · Status: **PARTIALLY_IMPLEMENTED**

- **Journey name:** Draft requiring explicit confirmation — مسودة تتطلب تأكيدًا صريحًا
- **Actor:** ACT-01
- **User intention:** Prepare work as a draft; nothing becomes financial truth without an explicit confirmation.
- **Entry points:** DraftEditor (orders); FormDraftRestoreBanner (long forms); CostEditor snapshots
- **Success outcome:** Drafts saved/restored with explicit restore prompt; conversion to real records only via explicit save actions; drafts never financial events.
- **Primary path:** Type → draft auto-saved → close → reopen → restore banner (explicit) → continue → explicit save converts (draft → order via agreement; form draft deleted after final save).
- **Alternative paths:** Version mismatch → draft silently ignored (safe); corrupted draft → defensive coercion / ignored (AV-09); conflict with finalized record → silent re-apply blocked.
- **Failure / exception paths:** Draft delete blocked once linked to an order; valuesVersion gate prevents wrong-shape restore.
- **Screens:** SCR-DRAFT-EDITOR, SCR-FORM-DRAFT-BANNER
- **Services:** SVC-DRAFT, SVC-FORM-DRAFT
- **Entities:** ENT-DRAFT, ENT-FORM-DRAFT
- **Before state:** Unsaved input at risk.
- **After state:** Draft preserved → converted or discarded explicitly.
- **Financial effect:** None until explicit save.
- **Cashbox / wallet effect:** None.
- **Profit / cost effect:** None.
- **Inventory effect:** None.
- **Debt / deposit effect:** None.
- **Offline / sync behavior:** Local; form drafts excluded from backups by design.
- **Permissions / approval:** Owner confirms every conversion.
- **History / audit behavior:** expectedUpdatedAt conflict guard; createdOperationKey traces.
- **Exit & next action:** Agreement recording (FLW-008/009) or discard.
- **Evidence:** application/drafts/draftService.ts; application/drafts/formDraftService.ts (contract 36, AV-09 defensive coercion); components/forms/FormDraftRestoreBanner.tsx; formDraftService.test.ts
- **Status:** PARTIALLY_IMPLEMENTED
- **Open gaps:** GAP-01

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Type in the form — اكتب في النموذج | — | SVC-FORM-DRAFT | Draft created only when user types. |
| 2 | System action | ACT-06 | Auto-save draft — احفظ المسودة تلقائيًا | — | SVC-FORM-DRAFT | Separate store; version-gated; never exported. |
| 3 | User action | ACT-01 | Explicitly restore — استرجع صراحةً | SCR-FORM-DRAFT-BANNER | SVC-FORM-DRAFT | Banner prompt; corrupted values replaced with safe ones (AV-09). |
| 4 | User action | ACT-01 | Final explicit save — احفظ نهائيًا | — | — | Draft deleted after final save or dismissal; record created. |


### FLW-046 — Error, retry, duplicate submission, uncertain result

> Arabic: الخطأ وإعادة المحاولة والتكرار والنتيجة غير المؤكدة · Status: **IMPLEMENTED**

- **Journey name:** Error, retry, duplicate submission, uncertain result — الخطأ وإعادة المحاولة والتكرار والنتيجة غير المؤكدة
- **Actor:** ACT-01
- **User intention:** Survive taps, failures, and concurrency without duplicated money.
- **Entry points:** Any save button; Any storage write
- **Success outcome:** Idempotent writes: same key → same record, reused:true; user sees one result; retries never duplicate.
- **Primary path:** Save → idempotency key → in-transaction duplicate check → single write → receipt/notice.
- **Alternative paths:** Concurrent window conflict → honest stale message («عُدّل من نافذة أخرى»); retry after storage error → same key reuses.
- **Failure / exception paths:** storage_unavailable/blocked/stale screens with retry; loan concurrency guard (AV-02) rejects stale relation; atomic commits roll back fully on failure.
- **Screens:** SCR-STARTUP-GATE
- **Services:** SVC-DIRECT-SALE, SVC-PROJECT-FINANCE, SVC-CASH-CONTINUITY
- **Entities:** ENT-FINANCIAL-EVENT, ENT-DIRECT-SALE, ENT-CASH-ENTRY
- **Before state:** Pending write.
- **After state:** Exactly one record (or honest failure with nothing written).
- **Financial effect:** Never duplicated.
- **Cashbox / wallet effect:** Never duplicated.
- **Profit / cost effect:** Never duplicated.
- **Inventory effect:** Atomic with events.
- **Debt / deposit effect:** Never duplicated.
- **Offline / sync behavior:** All local; no network uncertainty.
- **Permissions / approval:** Owner.
- **History / audit behavior:** reused flags; deterministic keys; loanCommitGuard.
- **Exit & next action:** Continue; verify via record surface.
- **Evidence:** application/reentrancyGuards.test.ts (P0); storage/local/IndexedDbLocalStore.ts:699-729 (writeOneIdempotent inside transaction); storage/local/loanCommitGuard.ts
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Double-tap save — اضغط حفظ مرتين | — | — | Busy state + idempotency key. |
| 2 | System action | ACT-06 | In-transaction duplicate check — تحقق داخل المعاملة | — | — | writeOneIdempotent; atomic commits return reused:true. |
| 3 | System action | ACT-06 | Honest failure notice — أخبر بصدق عند الفشل | — | — | Nothing written; retry safe; storage recovery screen if needed. |


## Group — L — Cross-cutting UX


### FLW-047 — Locking and unlocking (device lock)

> Arabic: قفل التطبيق وفتحه · Status: **IMPLEMENTED**

- **Journey name:** Locking and unlocking (device lock) — قفل التطبيق وفتحه
- **Actor:** ACT-01
- **User intention:** Protect the app from the passing glance on a shared device.
- **Entry points:** Idle timeout; Tab hidden / screen lock; Settings → lock settings
- **Success outcome:** Full-screen cover over live UI (forms survive under inert veil); unlock with PIN; data-leaving actions need PIN proof once per session.
- **Primary path:** Idle > autoLockMinutes (or visibility lost) → lock cover → enter PIN → unlock (PBKDF2 verify; legacy hash auto-upgrades).
- **Alternative paths:** Manual-only lock (null option); disable with PIN (record deleted permanently); emergency routes /setup & /settings never locked.
- **Failure / exception paths:** Wrong PIN → attempt count + escalating backoff (3s/10s/30s after 3/5/8 fails); no recovery without code (honest note; no cloud alternative).
- **Screens:** SCR-LOCK-COVER, SCR-SETTINGS
- **Services:** SVC-LOCAL-LOCK
- **Entities:** ENT-SECURITY
- **Before state:** Unlocked, possibly with dirty forms.
- **After state:** Locked/unlocked; UI state preserved underneath.
- **Financial effect:** None (not encryption).
- **Cashbox / wallet effect:** None.
- **Profit / cost effect:** None.
- **Inventory effect:** None.
- **Debt / deposit effect:** None.
- **Offline / sync behavior:** Local credential record; never exported.
- **Permissions / approval:** PIN required to unlock and for export/import/reset actions (once per session).
- **History / audit behavior:** Failed attempt counter; lastActiveAt.
- **Exit & next action:** Continue where left off.
- **Evidence:** components/security/AppLockGate.tsx:82-202; application/security/localLockService.ts:52-107, 179-266; Settings.lockGate.dom.test.tsx
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | System action | ACT-06 | Monitor idle + real input — راقب الخمول والمدخلات الحقيقية | — | SVC-LOCAL-LOCK | 30s heartbeat; usage = pointerdown/keydown/wheel/touchstart only. |
| 2 | System action | ACT-06 | Cover the app — غطِّ التطبيق | SCR-LOCK-COVER | SVC-LOCAL-LOCK | inert veil; forms survive; «بياناتك محلية كما هي». |
| 3 | User action | ACT-01 | Enter PIN — أدخل رمز القفل | SCR-LOCK-COVER | SVC-LOCAL-LOCK | 4-8 English digits; Arabic-Indic normalized; backoff on failures. |
| 4 | Decision | ACT-06 | Data-leaving action? (export/import/reset) — إجراء يُخرج البيانات؟ | SCR-SETTINGS | SVC-LOCAL-LOCK | One PIN proof per session (DataActionPinGate). |


### FLW-048 — Navigation back to source (?from contract)

> Arabic: الرجوع إلى مصدر التنقل · Status: **IMPLEMENTED**

- **Journey name:** Navigation back to source (?from contract) — الرجوع إلى مصدر التنقل
- **Actor:** ACT-01
- **User intention:** Open a deep record from anywhere and return exactly to where one started.
- **Entry points:** Every deep link built with withFrom(); Cold start with a URL containing ?from
- **Success outcome:** Return path preserved; loop-safe; canonical fallback when ?from missing/unsafe.
- **Primary path:** linkTo(target) → target?from=<current> → work → back → resolveReturnPath (valid, ≠ current) → return.
- **Alternative paths:** Canonical fallbacks table (e.g. /collect → /, /assets → /finance); deep-link params closed vocabulary with defensive parsing (unknown → null, no crash).
- **Failure / exception paths:** Unsafe ?from (protocol-relative, >256 chars, quotes) → silently ignored → fallback; ?from equals current → fallback (loop protection).
- **Screens:** —
- **Services:** SVC-NAV-CONTRACT
- **Entities:** —
- **Before state:** On a surface.
- **After state:** Back on the same surface.
- **Financial effect:** None.
- **Cashbox / wallet effect:** None.
- **Profit / cost effect:** None.
- **Inventory effect:** None.
- **Debt / deposit effect:** None.
- **Offline / sync behavior:** Local.
- **Permissions / approval:** None.
- **History / audit behavior:** Contract-tested invariants (navigationContract.test.ts).
- **Exit & next action:** Continue original task.
- **Evidence:** app/navigationContract.ts:5-198; app/useReturnNavigation.ts; app/navigationContract.test.ts; docs/contracts/26-navigation-referrer-and-deep-link-contract.md
- **Status:** IMPLEMENTED
- **Open gaps:** GAP-08

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Open deep record — افتح سجلًا عميقًا | — | SVC-NAV-CONTRACT | ?from carries the origin (single vessel). |
| 2 | User action | ACT-01 | Do the work — أنجز العمل | — | — | Editor or reader. |
| 3 | User action | ACT-01 | Go back — ارجع | — | SVC-NAV-CONTRACT | Valid ?from → return; else canonical fallback; loops prevented. |


### FLW-049 — Unsaved input protection

> Arabic: حماية المدخلات غير المحفوظة · Status: **IMPLEMENTED**

- **Journey name:** Unsaved input protection — حماية المدخلات غير المحفوظة
- **Actor:** ACT-01
- **User intention:** Never lose typed numbers and never save them silently.
- **Entry points:** Back button / browser back on deep editors; PWA update while dirty; Sheet discard with numbers typed
- **Success outcome:** 3-option dialog (stay / exit without saving) or 2-option quiet guard in sheets; PWA reload refused while dirty; form drafts preserve text.
- **Primary path:** Dirty form → back → guard dialog → choice honored; UnsavedChangesGuard bridges dirtiness to PWA layer (dirtyRegistry).
- **Alternative paths:** Sheet discard guard: «في رقم مكتوب — تسجّله أو تتجاهله؟» → سجّله الآن / تجاهل ما كتبت; form drafts auto-restore path (FLW-045).
- **Failure / exception paths:** beforeunload integration; popstate guard; no implicit save ever (decision v5).
- **Screens:** SCR-QUICK-ACTION
- **Services:** SVC-FORM-DRAFT
- **Entities:** ENT-FORM-DRAFT
- **Before state:** Dirty input.
- **After state:** Input saved, kept as draft, or discarded — by explicit choice.
- **Financial effect:** None (protection only).
- **Cashbox / wallet effect:** None.
- **Profit / cost effect:** None.
- **Inventory effect:** None.
- **Debt / deposit effect:** None.
- **Offline / sync behavior:** Local; SW update waits.
- **Permissions / approval:** Owner choice.
- **History / audit behavior:** Dirty snapshot stable symbol (D-026).
- **Exit & next action:** Proceed per choice.
- **Evidence:** components/forms/UnsavedChangesGuard.tsx (+4 test files); components/layout/QuickActionSheet.tsx:432-455 (discard guard); pwa/dirtyRegistry.ts; U005.dom.test.tsx
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Type then press back — اكتب ثم اضغط رجوع | — | — | Guard intercepts navigation. |
| 2 | Decision | ACT-01 | Stay or exit without saving? — ابقَ أو اخرج بلا حفظ؟ | — | — | 3-option dialog; no implicit save. |
| 3 | System action | ACT-06 | Block PWA reload over dirty forms — امنع تحديث PWA فوق بيانات متسخة | — | SVC-PWA | onNeedReload refuses auto-reload (S2-11). |


## Group — M — Cash management


### FLW-050 — Cash count and documented settlement

> Arabic: عدّ الصندوق وتسوية الفرق · Status: **IMPLEMENTED**

- **Journey name:** Cash count and documented settlement — عدّ الصندوق وتسوية الفرق
- **Actor:** ACT-01
- **User intention:** Match the drawer against the record and settle any difference honestly.
- **Entry points:** CashWallets → عدّ الصندوق; Finance → عدّ الصندوق — طابق الدرج مع السجل
- **Success outcome:** Counted vs recorded comparison; difference settled as a documented cash_adjustment (future effect, reason mandatory).
- **Primary path:** /cash/count → enter counted per wallet → سجّل التسوية → adjustment entry with reason.
- **Alternative paths:** Adjustment editor directly per wallet (اضبط أثرًا); reversal of a wrong adjustment documented.
- **Failure / exception paths:** Zero-delta settlement refused; reason required; reversal of reversal refused (record adjustment instead).
- **Screens:** SCR-CASH-COUNT, SCR-CASH-ADJUSTMENT, SCR-CASH-REVERSAL
- **Services:** SVC-CASH-CONTINUITY
- **Entities:** ENT-CASH-ENTRY
- **Before state:** Recorded wallet balance.
- **After state:** Balance adjusted to counted reality with documented reason.
- **Financial effect:** Cash continuity only — never classifies revenue/expense.
- **Cashbox / wallet effect:** ± difference per wallet.
- **Profit / cost effect:** None (by contract 10).
- **Inventory effect:** None.
- **Debt / deposit effect:** None.
- **Offline / sync behavior:** Local.
- **Permissions / approval:** Owner.
- **History / audit behavior:** Adjustment entry + optional reversal pair.
- **Exit & next action:** Wallet ledger shows settlement entry.
- **Evidence:** pages/CashCount.tsx:219 (سجّل التسوية); presentation/cashCountMessages.ts; application/cash/cashContinuityService.ts (adjust)
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Count the drawer — عدّ اللي في الدرج | SCR-CASH-COUNT | SVC-CASH-CONTINUITY | Counted vs recorded with difference shown. |
| 2 | User action | ACT-01 | Record settlement with reason — سجّل التسوية بسبب | SCR-CASH-COUNT | SVC-CASH-CONTINUITY | cash_adjustment entry; reason mandatory. |


### FLW-051 — Owner withdrawal and owner money separation

> Arabic: سحب المالك وفصل ماله · Status: **IMPLEMENTED**

- **Journey name:** Owner withdrawal and owner money separation — سحب المالك وفصل ماله
- **Actor:** ACT-01
- **User intention:** Take money for personal use without confusing it with expenses.
- **Entry points:** /finance/withdraw (سحب من المشروع لنفسك؟); Finance → سجل سحبًا شخصيًا; OwnerEntitlement surface
- **Success outcome:** Owner movement written (cash −, owner side per policy family); ledger movement or generic event depending on entitlement policy; wallet cash entry atomic.
- **Primary path:** Withdrawal editor → amount + wallet → recordMovement (owner_draw or settlement per policy) → atomic movement + cash entry.
- **Alternative paths:** Owner investment (owner_investment_cash); entitlement settlement ≤ remaining entitlement; opening balance settlement; returns (kind return).
- **Failure / exception paths:** Guards per reason (settlement ≤ remaining; settlement-of-prior-draw ≤ unreturned); withdrawal is never an expense (boundary).
- **Screens:** SCR-OWNER-WITHDRAWAL, SCR-OWNER-ENTITLEMENT, SCR-FINANCE
- **Services:** SVC-OWNER-ENTITLEMENT, SVC-PROJECT-FINANCE
- **Entities:** ENT-OWNER-MOVEMENT, ENT-FINANCIAL-EVENT, ENT-ENTITLEMENT-POLICY, ENT-CASH-ENTRY
- **Before state:** Owner capital/entitlement position.
- **After state:** Cash down; owner ledger movement; capital/entitlement deltas per kind.
- **Financial effect:** Owner money layer only — «سحبك ليس مصروفًا» (X-05 unified entry).
- **Cashbox / wallet effect:** Cash − (wallet entry).
- **Profit / cost effect:** None (never operating expense).
- **Inventory effect:** None.
- **Debt / deposit effect:** None.
- **Offline / sync behavior:** Local atomic (commitOwnerMovement).
- **Permissions / approval:** Owner.
- **History / audit behavior:** Movement + reversal pairs; readOwnerMoneyOverview unified view (S2-07).
- **Exit & next action:** Owner money overview; statement owner block.
- **Evidence:** pages/OwnerWithdrawalEditor.tsx; application/finance/ownerEntitlementService.ts; tests/owner-entitlement.test.ts; pages/OwnerWithdrawalEditor.ui.test.ts
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Record personal withdrawal — سجّل سحبًا شخصيًا | SCR-OWNER-WITHDRAWAL | SVC-OWNER-ENTITLEMENT | One unified entry picks the correct path (X-05). |
| 2 | Persistence write | ACT-06 | Atomic owner movement + wallet entry — حركة مالك + قيد محفظة ذري | — | SVC-OWNER-ENTITLEMENT | Deltas split per kind+reason; never expense. |


### FLW-052 — G5 declaration (expected collections/commitments)

> Arabic: تسجيل متوقعات السيولة القصيرة · Status: **IMPLEMENTED**

- **Journey name:** G5 declaration (expected collections/commitments) — تسجيل متوقعات السيولة القصيرة
- **Actor:** ACT-01
- **User intention:** Declare near-term expected money in/out to see projected short cash.
- **Entry points:** /finance/g5/declaration (تحصيل من عميل / التزام قريب)
- **Success outcome:** Declaration (direction, amount, dueOn, optional link to registered debt or payable event, knowledge grade) feeds projectedCashMinor; reversible documented.
- **Primary path:** G5DeclarationEditor → declare → appears in G5 decision card (projected cash) → reverse when obsolete.
- **Alternative paths:** Link validation caps (collections ≤ registered debt; commitments ≤ outstanding payable); no link to reversed events.
- **Failure / exception paths:** Undated receivables/payables block projection (incomplete, honest); declarations never become cash by themselves.
- **Screens:** SCR-G5-DECLARATION, SCR-FINANCE
- **Services:** SVC-G5
- **Entities:** ENT-G5-DECLARATION
- **Before state:** No declaration.
- **After state:** Declaration recorded (or reversed).
- **Financial effect:** None directly — reading layer: projectedCash = recordedCash + declaredCollections − declaredCommitments.
- **Cashbox / wallet effect:** None («متوقع» ≠ كاش).
- **Profit / cost effect:** None.
- **Inventory effect:** None.
- **Debt / deposit effect:** Links to existing debt/payable (bounded).
- **Offline / sync behavior:** Local.
- **Permissions / approval:** Owner.
- **History / audit behavior:** Reversal kind mirrors original exactly; one reversal per declaration.
- **Exit & next action:** G5 decision panel shows break-even + short cash ladders.
- **Evidence:** pages/G5DeclarationEditor.tsx; application/g5/g5Service.ts (validateRelation); src/domain/g5/policies.ts (calculateShortCash)
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Declare expected item — سجّل متوقعًا | SCR-G5-DECLARATION | SVC-G5 | Direction, amount, dueOn, knowledge, optional link. |
| 2 | System action | ACT-06 | Bound link validation — قيّد الروابط بحدودها | — | SVC-G5 | Order link only for collections ≤ debt; event link only for commitments ≤ payable. |
| 3 | User action | ACT-01 | Reverse when obsolete — اعكس عند التقادم | — | SVC-G5 | Documented reversal mirrors original exactly. |


### FLW-053 — Period statement generation and sharing

> Arabic: كشف الفترة ومشاركته · Status: **IMPLEMENTED**

- **Journey name:** Period statement generation and sharing — كشف الفترة ومشاركته
- **Actor:** ACT-01
- **User intention:** Get a plain-language separated period report and share it as text.
- **Entry points:** Finance → كشف الفترة — بسيط ومفصل بالعربية; /finance/statement
- **Success outcome:** Statement reading with separated blocks (cash in/out, corrections, owner, amanah, receivables/payables, deep finance, expense categories by frozen label); every line links to its source; Markdown export; share preview.
- **Primary path:** /finance/statement?from → choose period → read → ولّد ونزّل التقرير (Markdown) or share preview (editable text before leaving device).
- **Alternative paths:** Corrections shown once with net effect; unknown values rendered «غير متاح»; statement is a reading, never a financial event.
- **Failure / exception paths:** Invalid period range → inline error, no navigation; empty period → honest empty state.
- **Screens:** SCR-STATEMENT, SCR-SHARE-PREVIEW
- **Services:** SVC-STATEMENT, SVC-SHARE
- **Entities:** ENT-ACTIVITY-ROW, ENT-FINANCIAL-EVENT
- **Before state:** Period data.
- **After state:** Report generated/downloaded; optional shared text.
- **Financial effect:** None (read-only snapshot «نسخة قراءة لحظية… ليست حدثًا ماليًا»).
- **Cashbox / wallet effect:** None.
- **Profit / cost effect:** Reports recorded period result (canonical reader).
- **Inventory effect:** None (reports waste lines).
- **Debt / deposit effect:** Reports receivables/payables blocks.
- **Offline / sync behavior:** Local; share uses Web Share/copy of user-edited text.
- **Permissions / approval:** Owner; share text fully editable before leaving device.
- **History / audit behavior:** Statement built from canonical periodResult reader (periodResultCanonical.test.ts guard TR-01).
- **Exit & next action:** Open source records from lines; corrections layer for review.
- **Evidence:** pages/Statement.tsx:573 (ولّد ونزّل التقرير); application/finance/statementService.ts; application/finance/statementMarkdownService.ts; application/finance/periodResultCanonical.test.ts
- **Status:** IMPLEMENTED
- **Open gaps:** none recorded

#### Steps

| # | Kind | Actor | Action | Screen | Service | Detail |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | User action | ACT-01 | Open period statement — افتح كشف الفترة | SCR-STATEMENT | SVC-STATEMENT | Blocks separated by money layer; every line has source link. |
| 2 | User action | ACT-01 | Generate and download report — ولّد ونزّل التقرير | SCR-STATEMENT | SVC-STATEMENT | Arabic Markdown; unknown = «غير متاح»; no secrets. |
| 3 | User action | ACT-01 | Preview and edit share text — عاين المشاركة وعدّلها | SCR-SHARE-PREVIEW | SVC-SHARE | Full editable text before it leaves the device; no auto-send. |


## Journey status summary

| Flow | Name | Group | Status |
| --- | --- | --- | --- |
| FLW-001 | First entry and orientation (setup wizard) | A — Getting started | IMPLEMENTED |
| FLW-002 | Foundation: declare what you have right now | A — Getting started | IMPLEMENTED |
| FLW-003 | Understanding the current financial position | A — Getting started | IMPLEMENTED |
| FLW-004 | Guided opening import (G8.2) | A — Getting started | IMPLEMENTED |
| FLW-005 | Quick direct cash sale (FAB) | B — Sales & orders | IMPLEMENTED |
| FLW-006 | Direct sale — full editor (credit, catalog prefill) | B — Sales & orders | IMPLEMENTED |
| FLW-007 | Correcting a direct sale (edit / price cut / cancel) | B — Sales & orders | IMPLEMENTED |
| FLW-008 | Creating an order without a saved customer | B — Sales & orders | IMPLEMENTED |
| FLW-009 | Creating an order with an optional party/customer | B — Sales & orders | IMPLEMENTED |
| FLW-010 | Collecting a deposit (عربون) | B — Sales & orders | IMPLEMENTED |
| FLW-011 | Delivering an order — full sale recognition | B — Sales & orders | IMPLEMENTED |
| FLW-012 | Collecting the remaining amount after delivery | B — Sales & orders | IMPLEMENTED |
| FLW-013 | Selling on credit (receivable creation) | C — Debt & parties | IMPLEMENTED |
| FLW-014 | Registering order debt after delivery | C — Debt & parties | IMPLEMENTED |
| FLW-015 | Collecting a debt from the collection sheet | C — Debt & parties | IMPLEMENTED |
| FLW-016 | Saving and reusing a recurring party | C — Debt & parties | IMPLEMENTED |
| FLW-017 | Recording an expense (guided entry) | D — Expenses & corrections | IMPLEMENTED |
| FLW-018 | Correcting expense classification after saving | D — Expenses & corrections | IMPLEMENTED |
| FLW-019 | Editing a previous financial operation (general) | D — Expenses & corrections | IMPLEMENTED |
| FLW-020 | Cancelling / reversing a collection (compound) | D — Expenses & corrections | IMPLEMENTED |
| FLW-021 | Cancelling an order with a deposit (Conflict E) | E — Order cancellation & deposits | IMPLEMENTED |
| FLW-022 | Cancelling an order after cost or material consumption | E — Order cancellation & deposits | IMPLEMENTED |
| FLW-023 | Retained deposit classification & reclassification | E — Order cancellation & deposits | IMPLEMENTED |
| FLW-024 | Tracked material inventory flow | F — Inventory & materials | IMPLEMENTED |
| FLW-025 | Untracked material flow (cost reference) | F — Inventory & materials | IMPLEMENTED |
| FLW-026 | Negative inventory warning and decision | F — Inventory & materials | IMPLEMENTED |
| FLW-027 | Recording waste that affects profit | F — Inventory & materials | IMPLEMENTED |
| FLW-028 | Recording waste without profit impact | F — Inventory & materials | IMPLEMENTED |
| FLW-029 | Creating and receiving a supplier purchase | G — Purchases & suppliers | IMPLEMENTED |
| FLW-030 | Working with a supplier offer (controlled catalog) | G — Purchases & suppliers | PLANNED_OR_CONCEPTUAL |
| FLW-031 | Correcting a purchase / reversing a payment | G — Purchases & suppliers | IMPLEMENTED |
| FLW-032 | Product/cost calculation flow (calculator → estimate → draft) | H — Cost & pricing | IMPLEMENTED |
| FLW-033 | Asset creation and depreciation | I — Assets & loans | IMPLEMENTED |
| FLW-034 | Asset reaching zero while remaining in use | I — Assets & loans | IMPLEMENTED |
| FLW-035 | Asset disposal and correction boundaries | I — Assets & loans | IMPLEMENTED |
| FLW-036 | Loan creation and repayment | I — Assets & loans | IMPLEMENTED |
| FLW-037 | Delivery company assignment (external) | J — External delivery | PLANNED_OR_CONCEPTUAL |
| FLW-038 | Delivery with collection (collect at delivery) | J — External delivery | IMPLEMENTED |
| FLW-039 | Delivery failure, dispute, or correction | J — External delivery | IMPLEMENTED |
| FLW-040 | Backup creation (verified export) | K — Data & resilience | IMPLEMENTED |
| FLW-041 | Restore: rejection and successful restore | K — Data & resilience | IMPLEMENTED |
| FLW-042 | Reset (start anew) | K — Data & resilience | IMPLEMENTED |
| FLW-043 | Local-first / offline capture and honest status | K — Data & resilience | IMPLEMENTED |
| FLW-044 | Assistant question and sourced answer (guidance) | K — Data & resilience | PARTIALLY_IMPLEMENTED |
| FLW-045 | Draft requiring explicit confirmation | K — Data & resilience | PARTIALLY_IMPLEMENTED |
| FLW-046 | Error, retry, duplicate submission, uncertain result | K — Data & resilience | IMPLEMENTED |
| FLW-047 | Locking and unlocking (device lock) | L — Cross-cutting UX | IMPLEMENTED |
| FLW-048 | Navigation back to source (?from contract) | L — Cross-cutting UX | IMPLEMENTED |
| FLW-049 | Unsaved input protection | L — Cross-cutting UX | IMPLEMENTED |
| FLW-050 | Cash count and documented settlement | M — Cash management | IMPLEMENTED |
| FLW-051 | Owner withdrawal and owner money separation | M — Cash management | IMPLEMENTED |
| FLW-052 | G5 declaration (expected collections/commitments) | M — Cash management | IMPLEMENTED |
| FLW-053 | Period statement generation and sharing | M — Cash management | IMPLEMENTED |