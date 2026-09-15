# 02 — Actors, Permissions, and Entities

## Actors

### ACT-01 — Project owner / operator (مالك المشروع أو المشغّل المسؤول)

- **Kind:** primary local user
- **Status:** IMPLEMENTED
- **Description:** The single local user of the device. Holds every capability: sees all screens, creates and corrects every record, approves every financial effect. Micro has no accounts, roles, or multi-user access; the owner is the only human actor with system access.
- **Evidence:** apps/prototype-web/client/src/app/StartupGate.tsx:45-67 (single local profile boot); ARCHITECTURE.md (apps/prototype-web/ARCHITECTURE.md:14-15: no Auth, no SaaS, no multi-user)

### ACT-02 — Customer / reusable party (العميل أو الجهة القابلة لإعادة الاستخدام)

- **Kind:** external data subject (no system access)
- **Status:** IMPLEMENTED
- **Description:** Never logs in. Exists in Micro only as data: an optional customer name on drafts/orders, direct-sale customer names, and name-level aggregation in the people ledger. A name appearing in 2+ distinct source records becomes a selectable reusable party; a temporary unnamed receivable is allowed with a visible warning (Conflict B).
- **Evidence:** apps/prototype-web/client/src/application/parties/partyLedgerService.ts (name-level aggregation, repeatedOnly); src/domain/craft-order/policies.ts (party optional on order creation); docs/decisions/final-continuation-conflict-resolutions-v1.md (Conflict B)

### ACT-03 — Supplier (المورّد)

- **Kind:** external data subject (no system access)
- **Status:** PARTIALLY_IMPLEMENTED
- **Description:** No supplier portal or account exists. Suppliers appear as supplierName on purchase records, payables, and payments; controlled catalog offers are a future network concept (contract 20-N) and are NOT implemented. Publishing supplier offers is PLANNED_OR_CONCEPTUAL.
- **Evidence:** apps/prototype-web/client/src/application/suppliers/supplierPurchaseService.ts (purchase records only); docs/contracts/20-market-need-response-listing-moderation-contract.md (CONTRACT ONLY, expansion line)

### ACT-04 — Delivery company / courier (شركة التوصيل / المندوب)

- **Kind:** planned external actor
- **Status:** PLANNED_OR_CONCEPTUAL
- **Description:** Contract-only future actor (contract 21-N: request/quote/status/privacy). In current code 'delivery' means handing the order to the customer; no delivery-company assignment, dispatch, or courier data exists.
- **Evidence:** docs/contracts/21-delivery-request-quote-status-privacy-contract.md (CONTRACT ONLY); docs/expansion/historical-source/03-micro-delivery.md (historical plan); grep deliveryCompany over src/ and apps/: docs only

### ACT-05 — In-system assistant / guidance (المساعد داخل النظام)

- **Kind:** deterministic in-product guidance (no AI)
- **Status:** PARTIALLY_IMPLEMENTED
- **Description:** Today the 'assistant' is contract-governed, deterministic guidance: the guided financial-entry question sequence, impact previews, allocation review cards, derived suggestions (expense category chips, material suggestions, delivery consumption suggestions), the read-only integrity check, and pre-domain drafts. There is NO AI/LLM integration; deciding AI is explicitly rejected for this phase.
- **Evidence:** docs/product/guidance-interaction-policy-v1.md (governing policy); apps/prototype-web/client/src/pages/FinancialEventEditor.tsx (question sequence); apps/prototype-web/client/src/components/presentation/EventEffectPreview.tsx (impact preview); docs/product/deferred-capabilities-execution-plan-v1.md (AI that decides: rejected)

### ACT-06 — System / automation (النظام / الأتمتة المحلية)

- **Kind:** local automation
- **Status:** IMPLEMENTED
- **Description:** Local automation only: idle app-lock with visibility/heartbeat logic, PWA service-worker update gating (never reloads over dirty forms), cross-tab data-version broadcast (BroadcastChannel), idempotency/reentrancy guards, storage failure and blocked-database handling, auto settle at zero receivable.
- **Evidence:** apps/prototype-web/client/src/components/security/AppLockGate.tsx:33-100; apps/prototype-web/client/src/pwa/register.ts:51-59 (onNeedReload refuses auto-reload when dirty); apps/prototype-web/client/src/app/PrototypeServicesContext.tsx:121-141 (BroadcastChannel); apps/prototype-web/client/src/application/reentrancyGuards.test.ts

### ACT-07 — Employee / partner (موظف أو شريك)

- **Kind:** planned role (network line)
- **Status:** PLANNED_OR_CONCEPTUAL
- **Description:** Roles owner/supplier_member/courier_member/admin are defined only in network contract 18-N vocabulary with read/create/forbidden tables. No login, membership, invitation, or permission enforcement exists in the local product.
- **Evidence:** docs/contracts/18-network-identity-workspace-access-contract.md (CONTRACT ONLY)


## Permission matrix (flattened)

`yes` = allowed and implemented · `partial` = allowed under conditions · `no` = impossible by
design · `planned` = contract-only future capability.

| ID | Actor | Capability | Allowed | Evidence |
| --- | --- | --- | --- | --- |
| PRM-001 | ACT-01 | See all local data (orders, sales, money, inventory, parties, assets, loans, drafts) | yes | All 52 pages are owner-facing; e.g. apps/prototype-web/client/src/pages/Finance.tsx, Parties.tsx |
| PRM-002 | ACT-01 | Create every record type (order, sale, expense, purchase, wallet, movement, asset, loan, declaration, estimate, draft) | yes | QuickActionSheet 5 quick actions + deep editors (MicroRouter.tsx:86-157) |
| PRM-003 | ACT-01 | Edit / correct previous financial operations | yes | ProjectFinancialService.editEvent (atomic reverse-and-replace); pages/FinancialEventEditor.tsx; D005.dom.test.tsx |
| PRM-004 | ACT-01 | Approve impact previews before committing (corrections, cancellations, deliveries, classifications) | yes | EventEffectPreview.tsx, CorrectionPreview.tsx, DeliveryReview.tsx, G5DecisionPanel.tsx |
| PRM-005 | ACT-01 | Cancel / refund / reverse (orders with deposit, sales, collections, deliveries, payments, events, movements, repayments) | yes | fulfillmentService.refundDeposit/retainDeposit, directSaleService.cancel, collectionReversalService.reverse, deliveryReviewService.reverseDelivery, projectFinancialService.reverse |
| PRM-006 | ACT-01 | Export / import / reset local data | partial | Allowed only after PIN proof per session when lock enabled: pages/Settings.tsx:71-90, DataActionPinGate.tsx (SP-01/DP-04) |
| PRM-007 | ACT-01 | Bypass app lock on emergency routes | partial | /setup and /settings exempt from lock cover: AppLockGate.tsx:34, StartupGate.tsx:8 ('الطوارئ لا تُقفل') |
| PRM-008 | ACT-01 | Assign orders to an external delivery company | planned | No code; contract 21-N only |
| PRM-009 | ACT-01 | Use an AI assistant that changes financial truth | no | No AI integration; guidance-interaction-policy-v1.md; deferred-capabilities-execution-plan-v1.md rejects deciding AI |
| PRM-010 | ACT-02 | See any data inside Micro | no | No customer-facing surface exists; share texts are owner-edited before leaving the device (SharePreview.tsx) |
| PRM-011 | ACT-02 | Be recorded optionally on orders/sales; become a reusable party by repeat name | partial | partyLedgerService.ts (repeat names >=2 sources); Conflict B in final-continuation-conflict-resolutions-v1.md |
| PRM-012 | ACT-03 | Publish controlled catalog offers into the owner app | planned | Contract 20-N (CONTRACT ONLY); current catalog items are the owner's own references (P-002) |
| PRM-013 | ACT-03 | Receive orders / operational delivery data | planned | Contract 21-N disclosure matrix; nothing implemented |
| PRM-014 | ACT-04 | Receive only explicitly assigned orders and delivery data | planned | Contract 21-N: courier sees region/window/package only before quoting; not implemented |
| PRM-015 | ACT-05 | Explain, guide, prepare drafts (deterministic, local) | partial | FinancialEventEditor guided sequence; integrity check 'يقرأ أرقامك ولا يغيّر شيئاً'; draftService |
| PRM-016 | ACT-05 | Create or change financial truth silently | no | Previews derive from the same pure expansion used by save; drafts carry no financial effect (formDraftService header) |
| PRM-017 | ACT-06 | Lock the app after idle; auto-refresh activity on real input only | yes | AppLockGate.tsx:82-100 (30s heartbeat, pointerdown/keydown/wheel/touchstart) |
| PRM-018 | ACT-06 | Apply PWA update without owner approval | no | register.ts: skipWaiting:false, registerType prompt; update card waits for 'حدّث الآن' |
| PRM-019 | ACT-06 | Broadcast data change across tabs of the same device | yes | BroadcastChannel('micro-data-changed') in PrototypeServicesContext.tsx:121-141 |
| PRM-020 | ACT-07 | Any access to the local product | planned | Network roles are contract vocabulary only (18-N); no auth in app |

## Entity catalog

The repository persists 32 IndexedDB object stores (schema 35). The catalog below groups them
into 31 logical entities (plus the export envelope as a logical artifact). Derived read models
(party ledger, activity rows) are marked as not-stored.

| ID | Entity | Store | States | Financial effect | Inventory effect | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| ENT-PROFILE | ActivityProfile | activity-profile (singleton) | absent | present (single local profile) | none (identity only) | none | storage/local/types.ts:129-136; pages/Setup.tsx |
| ENT-OWNER-PROFILE | OwnerProfile | owner-profile (singleton) | absent | present | none | none | storage/local/types.ts:105-118; application/owner/ownerProfileService.ts |
| ENT-DRAFT | OrderDraft | order-drafts | new (created only on first real input) | saved | linked to order | deleted (only while unlinked) | none — a draft is explicitly not a CraftOrder | none | application/drafts/draftService.ts; pages/DraftEditor.tsx |
| ENT-CRAFT-ORDER | CraftOrder | craft-orders | draft → provisional_agreement → confirmed → in_progress → ready → delivered → settled; postponed, cancelled, needs_review (ALLOWED_TRANSITIONS); settlementStatus: unpaid|partially_paid|paid|debt|cancelled|cancelled_pending|cancelled_refunded|cancelled_retained | revenue recognized once at delivery; deposits are liquidity until then; cancellation zeroes receivable and nulls profit | delivery commits suggested consumption movements atomically | src/domain/craft-order/policies.ts:31-42 (ALLOWED_TRANSITIONS), 425-441 (recognition at delivery), 876-924 (cancelOrder); storage/local/types.ts:211-223 |
| ENT-DIRECT-SALE | DirectSale | direct-sales (unique idempotencyKey index) | active | cancelled; collectionStatus: collected_in_full | partial_debt | partial_needs_review | revenue recognized at sale date; unknown cost ⇒ profit null (never zero); cancel excludes revenue and mirror-reverses wallet allocations | optional consumption movement linked by saleId | src/domain/direct-sale/policies.ts; application/direct-sales/directSaleService.ts (reverseAllocationsForCancelledSale FT-02) |
| ENT-FINANCIAL-EVENT | FinancialEvent (general ledger record) | financial-events | active | reversed (via linked reversal event; original record never mutated) | DELTA_TABLE: 8 signed dimensions (cash, payable, ownerCapital, operatingExpense, amanah, asset, loan, retainedDepositRevenue) per type | loss_non_cash (waste with profit impact) is written together with inventory movement | src/domain/financial-event/types.ts:10-27; src/domain/financial-event/policies.ts:271-333 (DELTA_TABLE), 393-428 (reversal model) |
| ENT-SUPPLIER-PURCHASE | SupplierPurchase | supplier-purchases | unpaid | partially_paid | paid (effective paid = payments − documented reversals) | cash out and/or supplier payable — never an operating expense until consumption | optional material link; receipt bridge bounded by total/expected quantity | src/domain/supplier-purchase/policies.ts; application/suppliers/supplierPurchaseService.ts:95-97 (truth line) |
| ENT-CASH-WALLET | CashWallet | cash-wallets | opening known | opening unknown ('غير محدد', never zero) | tracks declared wallet balances only — never classifies revenue/expense/owner capital | none | src/domain/cash-continuity/types.ts:2-6; application/cash/cashContinuityService.ts |
| ENT-CASH-ENTRY | CashContinuityEntry | cash-continuity-entries | active | reversed (single-use reversal); transfers paired by transferId | moves cash between wallets and unallocated; allocation never changes total cash | none | src/domain/cash-continuity/policies.ts:83-108; application/cash/walletLedgerService.ts:100-102 (truth line) |
| ENT-MATERIAL | Material | materials | untracked (cost reference only) | tracked with unconfirmed opening | tracked with confirmed opening | opening unknown cost writes zero value flagged costKnowledge 'unknown' — never a declared amount | movements mutate quantity/value when tracked; untracked rejects movements | src/domain/inventory-material/types.ts; application/inventory/inventoryMaterialService.ts (untrack refuse paths 1060-1066) |
| ENT-INVENTORY-MOVEMENT | InventoryMovement | inventory-movements | active | reversed (mirror movement carries original costKnowledge) | wasteProfitImpact=true + known cost ⇒ linked loss_non_cash event in same atomic commit | quantity/value deltas; negative balance impossible (assertInventoryRemainsNonNegative) | src/domain/inventory-material/types.ts:34-68; application/inventory/inventoryMaterialService.ts:1285-1320 (waste profit choice) |
| ENT-SHORTAGE | InventoryShortage | inventory-shortages | open | resolved (explicit resolution) | none directly (honest disclosure) | replaces forbidden negative balance; surfaces as badge + MIC-8 WARN | src/domain/inventory-material/types.ts (InventoryShortage); contract 28 S6 / D-027 |
| ENT-CATALOG-ITEM | CatalogItem (product/service reference) | catalog-items | active | deactivated | none (P-002: defaults are optional suggestions) | none (template materialId is a planning reference only) | src/domain/catalog/types.ts:15-21 (proposal-only defaults); application/catalog/catalogService.ts |
| ENT-CATALOG-TEMPLATE | CatalogTemplate | catalog-templates | active | deactivated | superseded (immutable revisions) | none directly; autoConsumeOnDelivery only proposes consumption inside the atomic delivery confirmation — never deducts silently | proposes consumption rows at delivery review | src/domain/catalog/types.ts:131-135 (autoConsumeOnDelivery); application/deliveryReviewService.ts:308-549 |
| ENT-SCHEDULE-ENTRY | ScheduleEntry | schedule-entries | scheduled | completed (delivery reconciles idempotently) | cancelled (reason, stops future) | none — schedule never alters order money | none | application/scheduling/scheduleService.ts; contract 07 |
| ENT-ASSET | AssetRecord | assets | active (book value derived from events) | disposed | written_off; depreciation readiness: unknown_life | unknown_start | fully_depreciated | retired | ready | acquisition is capital (not expense); depreciation non-cash expense; disposal cash in + frozen book value; write-off non-cash loss | none | src/domain/asset/types.ts:10-13; src/domain/asset/policies.ts:180 (book value from events), 204-256 (proposal only) |
| ENT-LOAN | LoanRecord | loans | open | settled (outstanding derived from active repayments) | loan is neither expense nor owner draw; repayment is cash in, not income | none | src/domain/loan/policies.ts; application/loans/loanService.ts (commitLoanCorrection) |
| ENT-G5-DECLARATION | ShortCashDeclaration (expected record) | short-cash-declarations | declaration | reversed (documented, one per declaration) | never cash — feeds projectedCashMinor = recordedCash + declaredCollections − declaredCommitments | none | src/domain/g5/types.ts; application/g5/g5Service.ts (validateRelation caps) |
| ENT-ENTITLEMENT-POLICY | OwnerEntitlementPolicy | owner-entitlement-policies | active | ended (successor changes terms without rewriting predecessor) | entitlement calculation reads final orders / actual time / period result; never auto-paid | none | src/domain/owner-entitlement/policies.ts (successor series); application/finance/ownerEntitlementService.ts |
| ENT-OWNER-MOVEMENT | OwnerMovement (draw/return) | owner-movements | active | reversed (mirror) | draw lowers cash; return raises; owner capital delta only for new capital investment; always separate from project revenue/expense | none | src/domain/owner-entitlement/policies.ts (createOwnerMovement deltas); application/finance/ownerEntitlementService.ts (commitOwnerMovement) |
| ENT-ESTIMATE | CostEstimate | cost-estimates | saved (thinking tool only) | zero — saving never touches cash, balances, inventory, orders | none (reads material suggestions) | application/estimates/costEstimateService.ts; U004.dom.test.tsx (estimate→draft bridge, no financial movement) |
| ENT-ACTUAL-TIME | ActualTimeRecord | actual-time-records | active | reversed (negated delta) | feeds owner-entitlement evidence; never revenue | none | src/domain/actual-time/policies.ts; contract 16 |
| ENT-ALLOCATION-POLICY | AllocationPolicy (recurring-work loading) | allocation-policies | active | inactive | resultMinor = directMargin − amount; honest zero note | reads waste contexts | src/domain/recurring-margin/policies.ts:331; contract 14 |
| ENT-FORM-DRAFT | FormDraftEnvelope (transient text drafts) | form-drafts (excluded from snapshot/export by design) | saved | restored | discarded | ignored (version mismatch) | never becomes a financial event | none | application/drafts/formDraftService.ts (contract 36); storage/local/types.ts:47-57,568-573 |
| ENT-SECURITY | LocalSecurityRecord (app lock) | local-security (singleton; never exported, never in snapshot) | no lock | locked (idle window exceeded) | unlocked; backoff windows after failed attempts | none (protects from passing glance; not encryption) | none | application/security/localLockService.ts:52-66,229-266; storage/local/types.ts:58-78,568-573 |
| ENT-PREFERENCES | LocalPreferences | local-preferences (singleton) | present (defaults applied) | none — never carries financial meaning | none | storage/local/types.ts:138-152; application/preferences/preferenceService.ts |
| ENT-EXPORT-FILE | LocalExportFile (backup envelope) | (generated file, not a store) | parsed | rejected (11 documented rejection rules) | confirmed (atomic replace) | restore replaces the entire local financial state in one transaction | replaces all stores (except form-drafts/local-security) | application/transfers/localTransferService.ts:2453-2968 (API), 2496-2584 (rejection rules); storage/local/types.ts:331-342 |
| ENT-RECURRENCE | ScheduleRecurrence | schedule-recurrences | active | cancelled (stops future only) | occurrences are independent ScheduleEntries | never creates orders, agreements, reminders, or financial effects | none | application/scheduling/recurrenceService.ts; contract 19* G6-B |
| ENT-INVENTORY-ACTIVATION | InventoryActivation (snapshot at activation) | inventory-activations (singleton) | absent (module off) | present | past reports keep explicit gaps (not backfilled) | marks the boundary before which no movements exist | storage/local/types.ts (inventory-activations); docs/product/owner-decisions-v1.md (later inventory activation = snapshot at activation) |
| ENT-PARTY-LEDGER | PartyLedgerRow (derived, not stored) | (derived read over orders, sales, purchases, payable events) | single-use name (stays local to its record) | reusable party (>=2 distinct sources) | read-only aggregation | none | application/parties/partyLedgerService.ts (PA-010, no CRM entity) |
| ENT-ACTIVITY-ROW | ActivityRow (derived feed row) | (derived read over all stores) | derived per read | none (read-only) | none | application/activity/activityService.ts (contract 30) |

## Entity details

### ENT-PROFILE — ActivityProfile

- **Store:** activity-profile (singleton)
- **Fields (summary):** id, activityName, createdAt/updatedAt
- **States:** absent | present (single local profile)
- **Owner/editor actor:** ACT-01
- **Actions:** created in /setup wizard; edited in Settings/Profile; blocks boot to /setup until present
- **Financial effect:** none (identity only)
- **Inventory effect:** none
- **Related entities:** ENT-OWNER-PROFILE, ENT-PREFERENCES
- **Evidence:** storage/local/types.ts:129-136; pages/Setup.tsx; app/StartupGate.tsx:58

### ENT-OWNER-PROFILE — OwnerProfile

- **Store:** owner-profile (singleton)
- **Fields (summary):** ownerId (immutable), displayName, email?
- **States:** absent | present
- **Owner/editor actor:** ACT-01
- **Actions:** ensureLocal() at boot; edit in /profile
- **Financial effect:** none
- **Inventory effect:** none
- **Related entities:** ENT-PROFILE
- **Evidence:** storage/local/types.ts:105-118; application/owner/ownerProfileService.ts

### ENT-DRAFT — OrderDraft

- **Store:** order-drafts
- **Fields (summary):** id, intent (customer_order|planned_design), name?, customerName?, catalogItemId?, specifications, quantity, costSnapshots[], sourceEstimateId?, linkedOrderId?, updatedAt
- **States:** new (created only on first real input) | saved | linked to order | deleted (only while unlinked)
- **Owner/editor actor:** ACT-01
- **Actions:** create/edit/delete in DraftEditor; convert via AgreementEditor
- **Financial effect:** none — a draft is explicitly not a CraftOrder
- **Inventory effect:** none
- **Related entities:** ENT-CRAFT-ORDER, ENT-COST-ESTIMATE, ENT-CATALOG-ITEM
- **Evidence:** application/drafts/draftService.ts; pages/DraftEditor.tsx; owner decision 21 (drafts deletable without reason while unlinked)

### ENT-CRAFT-ORDER — CraftOrder

- **Store:** craft-orders
- **Fields (summary):** id, agreedPriceMinor, costSnapshot + costSnapshots[], status, settlementStatus, depositCollectedMinor, depositSettlement, retainedMeaning?, depositRetainedMinor?, collectedMinor, receivableMinor, recognizedRevenueMinor, recognizedCostMinor, profitIndicatorMinor, resultStatus, nextAction, events[] (+ agreement context fields: agreementSource, followUpSummary/date/reason, followUpEvents)
- **States:** draft → provisional_agreement → confirmed → in_progress → ready → delivered → settled; postponed, cancelled, needs_review (ALLOWED_TRANSITIONS); settlementStatus: unpaid|partially_paid|paid|debt|cancelled|cancelled_pending|cancelled_refunded|cancelled_retained
- **Owner/editor actor:** ACT-01
- **Actions:** create from draft, record agreement, start execution, deliver, collect, register debt, revise price, cancel, resume after review
- **Financial effect:** revenue recognized once at delivery; deposits are liquidity until then; cancellation zeroes receivable and nulls profit
- **Inventory effect:** delivery commits suggested consumption movements atomically
- **Related entities:** ENT-DRAFT, ENT-FINANCIAL-EVENT, ENT-CASH-CONTINUITY-ENTRY, ENT-MATERIAL, ENT-SCHEDULE-ENTRY
- **Evidence:** src/domain/craft-order/policies.ts:31-42 (ALLOWED_TRANSITIONS), 425-441 (recognition at delivery), 876-924 (cancelOrder); storage/local/types.ts:211-223

### ENT-DIRECT-SALE — DirectSale

- **Store:** direct-sales (unique idempotencyKey index)
- **Fields (summary):** id, itemLabel, revenueMinor, collectedMinor, customerName?, collectionStatus?, catalogItemId?, costMinor|null, profitMinor|null, occurredOn, status (active|cancelled), revisions[] (edit|cancel|price_cut with beforeRevenueMinor)
- **States:** active | cancelled; collectionStatus: collected_in_full | partial_debt | partial_needs_review
- **Owner/editor actor:** ACT-01
- **Actions:** record (cash/credit/price cut), edit, cancel
- **Financial effect:** revenue recognized at sale date; unknown cost ⇒ profit null (never zero); cancel excludes revenue and mirror-reverses wallet allocations
- **Inventory effect:** optional consumption movement linked by saleId
- **Related entities:** ENT-CASH-CONTINUITY-ENTRY, ENT-CATALOG-ITEM, ENT-INVENTORY-MOVEMENT
- **Evidence:** src/domain/direct-sale/policies.ts; application/direct-sales/directSaleService.ts (reverseAllocationsForCancelledSale FT-02)

### ENT-FINANCIAL-EVENT — FinancialEvent (general ledger record)

- **Store:** financial-events
- **Fields (summary):** id, type (17 types), amountMinor, occurredOn, recordedAt, note?, correctionType ('reverse'|null), correctionOfEventId?, correctionReason?, expenseContext?, assetContext?, loanContext?, depositContext?, idempotencyKey
- **States:** active | reversed (via linked reversal event; original record never mutated)
- **Owner/editor actor:** ACT-01
- **Actions:** record (guided editor / quick action), reverse (documented), edit (atomic reverse+replace), restore (Undo re-records as new event), delete (= documented reversal)
- **Financial effect:** DELTA_TABLE: 8 signed dimensions (cash, payable, ownerCapital, operatingExpense, amanah, asset, loan, retainedDepositRevenue) per type
- **Inventory effect:** loss_non_cash (waste with profit impact) is written together with inventory movement
- **Related entities:** ENT-ASSET, ENT-LOAN, ENT-CRAFT-ORDER (deposit classification), ENT-SUPPLIER-PURCHASE
- **Evidence:** src/domain/financial-event/types.ts:10-27; src/domain/financial-event/policies.ts:271-333 (DELTA_TABLE), 393-428 (reversal model)

### ENT-SUPPLIER-PURCHASE — SupplierPurchase

- **Store:** supplier-purchases
- **Fields (summary):** supplierName, purchasedOn, dueOn, totalMinor, paidMinor, payableMinor, status, payments[], paymentReversals?[], revisions?[] (edit with before-values), materialId?, expectedQuantityMilli?
- **States:** unpaid | partially_paid | paid (effective paid = payments − documented reversals)
- **Owner/editor actor:** ACT-01
- **Actions:** record purchase, record payment, reverse later payment, edit (documented, receipt-guarded)
- **Financial effect:** cash out and/or supplier payable — never an operating expense until consumption
- **Inventory effect:** optional material link; receipt bridge bounded by total/expected quantity
- **Related entities:** ENT-FINANCIAL-EVENT (payable settlements), ENT-MATERIAL, ENT-CASH-CONTINUITY-ENTRY
- **Evidence:** src/domain/supplier-purchase/policies.ts; application/suppliers/supplierPurchaseService.ts:95-97 (truth line)

### ENT-CASH-WALLET — CashWallet

- **Store:** cash-wallets
- **Fields (summary):** id, name, kind (cash_drawer|bank_account|digital_wallet|other), createdAt
- **States:** opening known | opening unknown ('غير محدد', never zero)
- **Owner/editor actor:** ACT-01
- **Actions:** create with opening balance (known/unknown/zero), complete opening later (documented)
- **Financial effect:** tracks declared wallet balances only — never classifies revenue/expense/owner capital
- **Inventory effect:** none
- **Related entities:** ENT-CASH-CONTINUITY-ENTRY
- **Evidence:** src/domain/cash-continuity/types.ts:2-6; application/cash/cashContinuityService.ts

### ENT-CASH-ENTRY — CashContinuityEntry

- **Store:** cash-continuity-entries
- **Fields (summary):** id, walletId, type (opening_balance|cash_adjustment|transfer_out|transfer_in|reversal|allocation), occurredOn, cashDeltaMinor, note, reason?, operationKey, transferId?, reversesEntryId?, sourceRefId/Kind/LineId?
- **States:** active | reversed (single-use reversal); transfers paired by transferId
- **Owner/editor actor:** ACT-01
- **Actions:** open, adjust (reason required), transfer (two legs), reverse (entry or both legs), allocate from/to unallocated
- **Financial effect:** moves cash between wallets and unallocated; allocation never changes total cash
- **Inventory effect:** none
- **Related entities:** ENT-CASH-WALLET, ENT-CRAFT-ORDER, ENT-DIRECT-SALE, ENT-FINANCIAL-EVENT
- **Evidence:** src/domain/cash-continuity/policies.ts:83-108; application/cash/walletLedgerService.ts:100-102 (truth line)

### ENT-MATERIAL — Material

- **Store:** materials
- **Fields (summary):** id, name, unit (piece|meter|kilogram|liter|other), tracking (tracked|untracked), opening {quantityState unconfirmed|confirmed, quantityMilli, costState known|unknown, valueMinor}
- **States:** untracked (cost reference only) | tracked with unconfirmed opening | tracked with confirmed opening
- **Owner/editor actor:** ACT-01
- **Actions:** create, activate tracking, stop tracking (4 announced consequences), confirm opening balance
- **Financial effect:** opening unknown cost writes zero value flagged costKnowledge 'unknown' — never a declared amount
- **Inventory effect:** movements mutate quantity/value when tracked; untracked rejects movements
- **Related entities:** ENT-INVENTORY-MOVEMENT, ENT-SUPPLIER-PURCHASE, ENT-CATALOG-TEMPLATE
- **Evidence:** src/domain/inventory-material/types.ts; application/inventory/inventoryMaterialService.ts (untrack refuse paths 1060-1066)

### ENT-INVENTORY-MOVEMENT — InventoryMovement

- **Store:** inventory-movements
- **Fields (summary):** id, materialId, type (opening|purchase_receipt|consumption|waste|adjustment|reversal), quantityDeltaMilli, valueDeltaMinor, occurredOn, reason, purchaseId?, orderId?, saleId?, reversesMovementId?, wasteContext?, costKnowledge?, wasteProfitImpact?
- **States:** active | reversed (mirror movement carries original costKnowledge)
- **Owner/editor actor:** ACT-01
- **Actions:** receipt, consume, waste (with/without profit impact), adjust, extract remainder, reverse
- **Financial effect:** wasteProfitImpact=true + known cost ⇒ linked loss_non_cash event in same atomic commit
- **Inventory effect:** quantity/value deltas; negative balance impossible (assertInventoryRemainsNonNegative)
- **Related entities:** ENT-MATERIAL, ENT-FINANCIAL-EVENT, ENT-SUPPLIER-PURCHASE, ENT-CRAFT-ORDER, ENT-DIRECT-SALE
- **Evidence:** src/domain/inventory-material/types.ts:34-68; application/inventory/inventoryMaterialService.ts:1285-1320 (waste profit choice)

### ENT-SHORTAGE — InventoryShortage

- **Store:** inventory-shortages
- **Fields (summary):** id, materialId, requestedQuantityMilli, availableQuantityMilli, shortageQuantityMilli, status (open|resolved), reason, operationKey
- **States:** open | resolved (explicit resolution)
- **Owner/editor actor:** ACT-01
- **Actions:** record shortage instead of negative balance; 'consume available + shortage' atomic path; resolve later
- **Financial effect:** none directly (honest disclosure)
- **Inventory effect:** replaces forbidden negative balance; surfaces as badge + MIC-8 WARN
- **Related entities:** ENT-MATERIAL, ENT-INVENTORY-MOVEMENT
- **Evidence:** src/domain/inventory-material/types.ts (InventoryShortage); contract 28 S6 / D-027

### ENT-CATALOG-ITEM — CatalogItem (product/service reference)

- **Store:** catalog-items
- **Fields (summary):** id, kind (product|service), name, unitLabel, unitId?, defaultPriceMinor?, defaultUnitCostMinor?, active
- **States:** active | deactivated
- **Owner/editor actor:** ACT-01
- **Actions:** create, update defaults (proposals only — never rewrites past sales), deactivate
- **Financial effect:** none (P-002: defaults are optional suggestions)
- **Inventory effect:** none (template materialId is a planning reference only)
- **Related entities:** ENT-CATALOG-TEMPLATE, ENT-DIRECT-SALE, ENT-DRAFT
- **Evidence:** src/domain/catalog/types.ts:15-21 (proposal-only defaults); application/catalog/catalogService.ts

### ENT-CATALOG-TEMPLATE — CatalogTemplate

- **Store:** catalog-templates
- **Fields (summary):** id, catalogItemId, components[] (quantityMilli, unitId, materialId?), yield, yieldReadiness, extras? (time/packaging/delivery/waste/safety), autoConsumeOnDelivery?: boolean|null, revision, sourceTemplateId, active
- **States:** active | deactivated | superseded (immutable revisions)
- **Owner/editor actor:** ACT-01
- **Actions:** create, revise (new revision), deactivate
- **Financial effect:** none directly; autoConsumeOnDelivery only proposes consumption inside the atomic delivery confirmation — never deducts silently
- **Inventory effect:** proposes consumption rows at delivery review
- **Related entities:** ENT-CATALOG-ITEM, ENT-MATERIAL
- **Evidence:** src/domain/catalog/types.ts:131-135 (autoConsumeOnDelivery); application/deliveryReviewService.ts:308-549

### ENT-SCHEDULE-ENTRY — ScheduleEntry

- **Store:** schedule-entries
- **Fields (summary):** id, orderId?, scheduledFor (local date), scheduledTime?+durationMinutes? (pair or neither), status, reason history (date change requires reason)
- **States:** scheduled | completed (delivery reconciles idempotently) | cancelled (reason, stops future)
- **Owner/editor actor:** ACT-01
- **Actions:** set/update timing, postpone, reconcile on delivery
- **Financial effect:** none — schedule never alters order money
- **Inventory effect:** none
- **Related entities:** ENT-CRAFT-ORDER, ENT-SCHEDULE-RECURRENCE
- **Evidence:** application/scheduling/scheduleService.ts; contract 07

### ENT-ASSET — AssetRecord

- **Store:** assets
- **Fields (summary):** id, name, categoryLabel, acquisitionAmountMinor, acquisitionKind (cash|payable), purchaseDate, lifeMonths|null, depreciationStartOn|null, status, acquisitionEventId, disposal?{on, proceedsMinor, bookValueMinor, eventId, reason}, writeOff?, contractRevisions[], operationKey
- **States:** active (book value derived from events) | disposed | written_off; depreciation readiness: unknown_life | unknown_start | fully_depreciated | retired | ready
- **Owner/editor actor:** ACT-01
- **Actions:** acquire, record depreciation (proposal → explicit event), revise contract (documented), correct acquisition (only while active), dispose, write off
- **Financial effect:** acquisition is capital (not expense); depreciation non-cash expense; disposal cash in + frozen book value; write-off non-cash loss
- **Inventory effect:** none
- **Related entities:** ENT-FINANCIAL-EVENT
- **Evidence:** src/domain/asset/types.ts:10-13; src/domain/asset/policies.ts:180 (book value from events), 204-256 (proposal only)

### ENT-LOAN — LoanRecord

- **Store:** loans
- **Fields (summary):** id, borrowerName, principalMinor, loanDate, purposeNote?, sourceWalletId, principalEventId, repayments[] {amountMinor, eventId, reversal?{reason, at, reversalEventId}}, corrections[]
- **States:** open | settled (outstanding derived from active repayments)
- **Owner/editor actor:** ACT-01
- **Actions:** create (cash out, loan asset up), record repayment, reverse repayment, correct principal/borrower (atomic reverse+replace)
- **Financial effect:** loan is neither expense nor owner draw; repayment is cash in, not income
- **Inventory effect:** none
- **Related entities:** ENT-FINANCIAL-EVENT, ENT-CASH-CONTINUITY-ENTRY
- **Evidence:** src/domain/loan/policies.ts; application/loans/loanService.ts (commitLoanCorrection)

### ENT-G5-DECLARATION — ShortCashDeclaration (expected record)

- **Store:** short-cash-declarations
- **Fields (summary):** id, kind (declaration|reversal), direction (collection|commitment), amountMinor, dueOn, source, knowledge (known|estimated|needs_review), note?, relatedOrderId?, relatedEventId?, idempotencyKey, reversalOfId?, createdAt
- **States:** declaration | reversed (documented, one per declaration)
- **Owner/editor actor:** ACT-01
- **Actions:** declare expected collection/commitment, reverse declaration
- **Financial effect:** never cash — feeds projectedCashMinor = recordedCash + declaredCollections − declaredCommitments
- **Inventory effect:** none
- **Related entities:** ENT-CRAFT-ORDER (registered debt link), ENT-FINANCIAL-EVENT (payable link)
- **Evidence:** src/domain/g5/types.ts; application/g5/g5Service.ts (validateRelation caps)

### ENT-ENTITLEMENT-POLICY — OwnerEntitlementPolicy

- **Store:** owner-entitlement-policies
- **Fields (summary):** id, seriesId, successorOfPolicyId?, version, family (time_period|fixed_amount|completed_work|profit_share|completed_sale_percentage|unit), kind (monthly/weekly/daily/hourly/fixed_period/fixed_shift/per_completed_work/profit_share/sale_percentage/per_unit), startsOn, endsOn?, status
- **States:** active | ended (successor changes terms without rewriting predecessor)
- **Owner/editor actor:** ACT-01
- **Actions:** create, create successor, calculate entitlement (evidence-based)
- **Financial effect:** entitlement calculation reads final orders / actual time / period result; never auto-paid
- **Inventory effect:** none
- **Related entities:** ENT-ENTITLEMENT-RECORD, ENT-OWNER-MOVEMENT
- **Evidence:** src/domain/owner-entitlement/policies.ts (successor series); application/finance/ownerEntitlementService.ts

### ENT-OWNER-MOVEMENT — OwnerMovement (draw/return)

- **Store:** owner-movements
- **Fields (summary):** id, kind (draw|return), reason (entitlement_settlement|opening_balance_settlement|pre_entitlement_draw|owner_draw|settlement_of_prior_draw|new_capital_investment), cashDeltaMinor, entitlementDeltaMinor, openingBalanceDeltaMinor, ownerCapitalDeltaMinor, walletId, occurredOn, idempotencyKey, reversalOfId?
- **States:** active | reversed (mirror)
- **Owner/editor actor:** ACT-01
- **Actions:** record movement (atomic with wallet cash entry), reverse movement
- **Financial effect:** draw lowers cash; return raises; owner capital delta only for new capital investment; always separate from project revenue/expense
- **Inventory effect:** none
- **Related entities:** ENT-CASH-CONTINUITY-ENTRY, ENT-ENTITLEMENT-POLICY
- **Evidence:** src/domain/owner-entitlement/policies.ts (createOwnerMovement deltas); application/finance/ownerEntitlementService.ts (commitOwnerMovement)

### ENT-ESTIMATE — CostEstimate

- **Store:** cost-estimates
- **Fields (summary):** id, inputs (materials, work minutes, extras), plannedCostMinor, unitCostMinor, priceFloorMinor, knowledgeState, createdAt/updatedAt
- **States:** saved (thinking tool only)
- **Owner/editor actor:** ACT-01
- **Actions:** preview live, save, edit, delete, start draft from estimate
- **Financial effect:** zero — saving never touches cash, balances, inventory, orders
- **Inventory effect:** none (reads material suggestions)
- **Related entities:** ENT-DRAFT, ENT-MATERIAL
- **Evidence:** application/estimates/costEstimateService.ts; U004.dom.test.tsx (estimate→draft bridge, no financial movement)

### ENT-ACTUAL-TIME — ActualTimeRecord

- **Store:** actual-time-records
- **Fields (summary):** id, orderId, minutesDelta, recordedOn, note?, operationKey, reversalOfId?, reversalReason?
- **States:** active | reversed (negated delta)
- **Owner/editor actor:** ACT-01
- **Actions:** record, reverse (reason)
- **Financial effect:** feeds owner-entitlement evidence; never revenue
- **Inventory effect:** none
- **Related entities:** ENT-CRAFT-ORDER, ENT-ENTITLEMENT-POLICY
- **Evidence:** src/domain/actual-time/policies.ts; contract 16

### ENT-ALLOCATION-POLICY — AllocationPolicy (recurring-work loading)

- **Store:** allocation-policies
- **Fields (summary):** id, seriesId, successorOfPolicyId?, version, catalogItemId, kind (manual_amount|per_output_unit|actual_time|completed_revenue_percentage), amountMinor/rates/percentageBps, unitId, periodFrom/To, status
- **States:** active | inactive
- **Owner/editor actor:** ACT-01
- **Actions:** create, successor, deactivate; calculate over evidence (final orders, output, actual time)
- **Financial effect:** resultMinor = directMargin − amount; honest zero note
- **Inventory effect:** reads waste contexts
- **Related entities:** ENT-CATALOG-ITEM, ENT-CRAFT-ORDER
- **Evidence:** src/domain/recurring-margin/policies.ts:331; contract 14

### ENT-FORM-DRAFT — FormDraftEnvelope (transient text drafts)

- **Store:** form-drafts (excluded from snapshot/export by design)
- **Fields (summary):** id 'formKind:scopeId', valuesVersion, values, updatedAt
- **States:** saved | restored | discarded | ignored (version mismatch)
- **Owner/editor actor:** ACT-01
- **Actions:** auto-save while typing, explicit restore prompt, delete after final save or dismissal
- **Financial effect:** never becomes a financial event
- **Inventory effect:** none
- **Related entities:** —
- **Evidence:** application/drafts/formDraftService.ts (contract 36); storage/local/types.ts:47-57,568-573

### ENT-SECURITY — LocalSecurityRecord (app lock)

- **Store:** local-security (singleton; never exported, never in snapshot)
- **Fields (summary):** pinHash (PBKDF2-SHA256 120k iterations + salt), salt, hashAlgo, autoLockMinutes, lastActiveAt, failedAttempts, lastFailedAt
- **States:** no lock | locked (idle window exceeded) | unlocked; backoff windows after failed attempts
- **Owner/editor actor:** ACT-01
- **Actions:** enable (PIN 4-8 English digits + idle choice), unlock, disable (correct PIN; record deleted)
- **Financial effect:** none (protects from passing glance; not encryption)
- **Inventory effect:** none
- **Related entities:** —
- **Evidence:** application/security/localLockService.ts:52-66,229-266; storage/local/types.ts:58-78,568-573

### ENT-PREFERENCES — LocalPreferences

- **Store:** local-preferences (singleton)
- **Fields (summary):** theme, capacity?, workMode?, actualTimeTrackingEnabled, installBannerDismissedAt, lastVerifiedExportAt, backupReminderEnabled
- **States:** present (defaults applied)
- **Owner/editor actor:** ACT-01
- **Actions:** save theme, operating mode, lock settings, banner dismissal, verified-export stamp
- **Financial effect:** none — never carries financial meaning
- **Inventory effect:** none
- **Related entities:** ENT-PROFILE
- **Evidence:** storage/local/types.ts:138-152; application/preferences/preferenceService.ts

### ENT-EXPORT-FILE — LocalExportFile (backup envelope)

- **Store:** (generated file, not a store)
- **Fields (summary):** format 'micro-prototype-local-export', version 27, schemaVersion 35, exportedAt, data (30-store snapshot), integrity {algorithm sha256, digest}, counts (13 counters), appVersion
- **States:** parsed | rejected (11 documented rejection rules) | confirmed (atomic replace)
- **Owner/editor actor:** ACT-01
- **Actions:** verified export (round-trip re-parse), prepareImport validation, confirmImport atomic replace, guided opening import
- **Financial effect:** restore replaces the entire local financial state in one transaction
- **Inventory effect:** replaces all stores (except form-drafts/local-security)
- **Related entities:** ENT-SECURITY (PIN gate for export/import/reset)
- **Evidence:** application/transfers/localTransferService.ts:2453-2968 (API), 2496-2584 (rejection rules); storage/local/types.ts:331-342

### ENT-RECURRENCE — ScheduleRecurrence

- **Store:** schedule-recurrences
- **Fields (summary):** id, sourceScheduleId, orderId?, pattern (weekly|monthly), occurrenceCount 1-12, status, createdAt, cancellation reason
- **States:** active | cancelled (stops future only) | occurrences are independent ScheduleEntries
- **Owner/editor actor:** ACT-01
- **Actions:** create from an existing entry, cancel with reason
- **Financial effect:** never creates orders, agreements, reminders, or financial effects
- **Inventory effect:** none
- **Related entities:** ENT-SCHEDULE-ENTRY
- **Evidence:** application/scheduling/recurrenceService.ts; contract 19* G6-B

### ENT-INVENTORY-ACTIVATION — InventoryActivation (snapshot at activation)

- **Store:** inventory-activations (singleton)
- **Fields (summary):** activation record with activation date
- **States:** absent (module off) | present
- **Owner/editor actor:** ACT-01
- **Actions:** activate inventory late = snapshot at activation day (owner decision)
- **Financial effect:** past reports keep explicit gaps (not backfilled)
- **Inventory effect:** marks the boundary before which no movements exist
- **Related entities:** ENT-MATERIAL
- **Evidence:** storage/local/types.ts (inventory-activations); docs/product/owner-decisions-v1.md (later inventory activation = snapshot at activation)

### ENT-PARTY-LEDGER — PartyLedgerRow (derived, not stored)

- **Store:** (derived read over orders, sales, purchases, payable events)
- **Fields (summary):** personName, receivableMinor, payableMinor, movements[] with deep links
- **States:** single-use name (stays local to its record) | reusable party (>=2 distinct sources)
- **Owner/editor actor:** ACT-01
- **Actions:** read (search, repeatedOnly filter); collect from row deep link
- **Financial effect:** read-only aggregation
- **Inventory effect:** none
- **Related entities:** ENT-CRAFT-ORDER, ENT-DIRECT-SALE, ENT-SUPPLIER-PURCHASE, ENT-FINANCIAL-EVENT
- **Evidence:** application/parties/partyLedgerService.ts (PA-010, no CRM entity)

### ENT-ACTIVITY-ROW — ActivityRow (derived feed row)

- **Store:** (derived read over all stores)
- **Fields (summary):** family (15 families), effect class (cash_in|cash_out|non_cash|payable|owner_money|trust|pending|informational), status (active|reversed|cancelled|pending), source deep link
- **States:** derived per read
- **Owner/editor actor:** ACT-01
- **Actions:** read with family/period filters; open source record
- **Financial effect:** none (read-only)
- **Inventory effect:** none
- **Related entities:** all record entities
- **Evidence:** application/activity/activityService.ts (contract 30)

