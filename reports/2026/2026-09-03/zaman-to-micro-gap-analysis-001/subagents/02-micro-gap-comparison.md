# SA-2 — Micro Baseline and Gap Comparison (Zman → Micro)

- **Task ID:** SA-2 (Micro Baseline and Gap Comparator, sub-agent)
- **Date:** 2026-09-03
- **Micro repo state:** `main` @ `4db6a5f` ("merge: Group 6 resume, regression recovery, and final closure (PR #148)") — read-only clone at `/home/z/my-project/repos/micro`. Local-first delivery-final state after Groups 1–6 (2026-09-02): schema `30`, export `22`, 42 page components (52 files in `pages/` including UI tests), 13 domain modules, 16 domain test files + 533 prototype tests, IndexedDB via `PrototypeLocalStore` (26 stores).
- **Zman repo state (comparison source, enumerated only):** `main` @ `bdd63ab`, clone at `/home/z/my-project/repos/zman`. Next.js + Drizzle/Postgres app under `artifacts/zman-app` with routes `/`, `/activities`, `/assets`, `/catalog`, `/finance`, `/finance/accounts`, `/inventory`, `/orders`, `/reports`, `/settings/audit-log`, `/settings/opening-balance`, `/snippets`, `/login`.
- **Methodology:** Evidence-first. Micro side read from the live source of truth `docs/operations/current-state.md` (§2, §3, §5, §16–§22), `AGENTS.md`, `README.md`, domain types/policies under `src/domain/`, the full route map in `apps/prototype-web/client/src/app/MicroRouter.tsx`, navigation contracts (`navigationContract.ts`, `routeClassifier.ts`, `navigation.ts`), storage contracts (`storage/local/types.ts`), and key pages/services. Zman side skimmed only to enumerate and verify capability areas (feature folders, `src/features/*/db.ts`, key components/pages). All file paths below are repo-relative. Inferences are labelled `INFERENCE`. Both repos untouched.

---

## 1. Micro current-state baseline

### 1.1 Product identity and constraints (verified in code)

- Arabic RTL, phone-first web PWA. JOD with 2 decimals, ASCII/English digits for money, `DD/MM/YYYY` local dates in Amman timezone (`src/domain/shared/currency.ts`, `apps/prototype-web/client/src/presentation/formatters.ts`; current-state.md §Group 6 item 5: "أرقام إنجليزية وDD/MM/YYYY نظاميًا" across 17 routes).
- Offline-first: all writes go through `PrototypeLocalStore` → IndexedDB (`apps/prototype-web/client/src/storage/local/IndexedDbLocalStore.ts`); PWA service worker registration with offline-ready/update states (`apps/prototype-web/client/src/pwa/register.ts`); locally hosted IBM Plex fonts, CSP, BroadcastChannel cross-tab updates (current-state.md §Group 5). **No cloud, no SaaS, no auth, no sync** (current-state.md §1 "نمط المنتج"; README.md "ما هذا المستودع الآن؟").
- Owner Profile: local-only record `OwnerProfile` with stable local `ownerId`, `provider: null`, `externalAccountId: null` — future account-linking-ready without Google/OAuth now (`apps/prototype-web/client/src/storage/local/types.ts:36-49`; `/profile` route).
- Honest separation enforced by domain invariants: collection ≠ profit, debt ≠ cash, purchase ≠ COGS, owner money ≠ sale/expense, Amanah ≠ own money, missing ≠ zero (current-state.md §4; `AGENTS.md` §6).
- Estimates/cost tools create zero financial or inventory effects: `CostEstimate` is a "thinking tool" record (`storage/local/types.ts:197-220`), Calculator is a deep route with declared "no financial effect" rule (`pages/CostCalculator.tsx`; current-state.md §Group 3).
- Optional product selection during sale: `DirectSale.catalogItemId?: string | null` optional binding (`src/domain/direct-sale/types.ts:19`); inventory never forced (current-state.md §Group 3: "لا استيراد مخزون تاريخي ولا مخزون إلزامي").
- Traceable corrections: every sensitive correction is a documented reversal/replacement with mandatory reason and `idempotencyKey`; originals preserved; unified `CorrectionPreview` before every correction (current-state.md §Group 2; `storage/local/types.ts` commit methods).

### 1.2 Navigation map (5 tabs + FAB + top bar)

**Shell:** one continuous Android-like shell `MicroAppShell` (`apps/prototype-web/client/src/components/layout/MicroAppShell.tsx`) with `AppHeader` + `BottomNav`. Bottom nav seats (from `apps/prototype-web/client/src/app/navigation.ts`):

```
مشروعي الآن (/)  |  العمل (/orders)  |  [سجّل FAB]  |  مالي (/finance)  |  أدواتي (/tools)
```

- **FAB (`سجّل`):** centered brown button in `BottomNav.tsx:29-32` opens `QuickActionSheet` (`components/layout/QuickActionSheet.tsx`) with five actions: تسجيل بيع (in-sheet quick sale form with cash-destination + receipt), تسجيل مصروف (in-sheet quick expense), طلب من عميل (new draft), مسودة تصميم (planned-design draft), عربون أو تحصيل (opens `/collect`). The sheet "never creates a financial effect" beyond its explicit forms; the quick sale/expense are transitory actions completed inside the sheet, full editors remain the correction/deep path.
- **Top bar (`AppHeader.tsx`):** brand lockup + contextual route label (`getNavigationLabel` in `navigation.ts`), settings gear (opens `/settings`), light/dark toggle. `/profile` reached from Home's owner block (`pages/Home.tsx:197`) and Settings (`pages/Settings.tsx:328`) — no sixth seat.
- **Route kinds (`routeClassifier.ts`):** `setup` (`/setup`), `surface` (keeps bottom nav + FAB, e.g. lists/details), `deep` (editors/tools hide bottom nav on purpose; back button returns to origin; `UnsavedChangesGuard` protects dirty forms with popstate/beforeunload — `components/forms/UnsavedChangesGuard.tsx`).
- **Safe return (contract 26, `navigationContract.ts`):** every deep route keeps `?from=<internal-path>` (validated: starts with `/`, ≤256 chars, no external scheme); unknown values silently ignored; `resolveReturnPath()` + `canonicalReturnFallbacks` map (e.g. `/tools/calculator` → `/tools`, `/collect` → `/`). Deep-link vocabulary is a closed enum: `?focus` (capacity|recurrence|guided-import|export|today|priority), `?layer` (corrections|events), `?mode` (cover), `?event`, `?to`. Cold start/refresh preserves intent via URL.
- **Startup gate (`app/StartupGate.tsx`):** routes `/setup` (first-run project setup) and `/foundation` (permanent front door "صفحة الأساس" reachable later, decision 7) before main shell.

**Tab → route reachability (from `MicroRouter.tsx` + page links):**

| Tab | Surfaces | Deep routes reached from it |
|---|---|---|
| مشروعي الآن (Home `/`) | Home control center: "الأهم الآن" priority block, financial facts (cash/receivables/payables/owner capital/unallocated with honest states), today list, follow-up, amanah qualifier, unallocated-cash card, owner profile block | `/collect`, `/profile`, `/finance/...`, `/orders/...`, `/cash`, statement, schedule |
| العمل (`/orders`) | Orders: "الأولوية الآن" always present, direct-sales rows, drafts, schedule sections | `/orders/new`, `/orders/draft/:id`, `/orders/draft/:id/cost`, `/orders/draft/:id/agreement`, `/orders/:id` (OrderDetail), `/direct-sales/new?product=…&from=/catalog` |
| مالي (`/finance`) | Finance split `?view=position|period` ("الوضع الآن" / "شو صار خلال الفترة"); layers: cash decision, period reading, G5, record (events), corrections history, deposits, owner summary | `/finance/new/:type` (8 event types), `/finance/withdraw`, `/finance/owner-entitlement`, `/finance/g5/declaration`, `/finance/statement`, `/parties`, `/suppliers`, `/suppliers/purchase/:id(/payment)`, `/cash` (+ wallet ledger/editors), `/collect`, `/inventory` (also from Foundation) |
| أدواتي (`/tools`) | Tools: saved estimates, module states (catalog/units/schedule/suppliers/parties with derived availability) | `/tools/calculator`, `/tools/estimate/:id`, `/catalog` |
| (top bar) Settings `/settings` | Settings: info, preferences (theme, work mode, actual time toggle), appearance, sensitive data (export/import/reset, guided opening import `?focus=guided-import`) | `/profile` |

### 1.3 Screen inventory (all routed pages, 42 components)

| Route | Page (file under `apps/prototype-web/client/src/pages/`) | What it does |
|---|---|---|
| `/` | `Home.tsx` | Control center: most-important-now block with concrete actions, financial fact cards with knowledge states ("غير محدد بعد" for unknown), today list, follow-up reminders, unallocated cash card, amanah qualifier, owner profile entry, honest empty state. |
| `/orders` | `Orders.tsx` | Work tab: "الأولوية الآن" (always, even if "nothing urgent"), brief direct-sale rows with CTA, drafts, schedule day/upcoming/overdue sections; every section appears only with real records. |
| `/orders/new`, `/orders/draft/:id` | `NewDraft.tsx`, `DraftEditor.tsx` | Order draft lifecycle with intent (customer_order / planned_design); draft created on first real input; catalog item optional; estimate source ref (sourceEstimateId). |
| `/orders/draft/:id/cost` | `CostEditor.tsx` | Cost snapshot editor for the draft: materials/time/packaging/delivery/waste/safety buffer, knowledge confidence, revision history (append-only snapshots). |
| `/orders/draft/:id/agreement` | `AgreementEditor.tsx` | Agreement + price + deposit: saves the agreement (price approval), agreement source (instagram/whatsapp/referral/walk_in), customer name, follow-up date; CTA for incomplete snapshots. |
| `/orders/:id` | `OrderDetail.tsx` | Order detail: status, settlement, snapshot truth, order event log (real labels), actual time/material panels (with `?order=` context link), corrections entry, "المصدر: تقدير" when from estimate. |
| `/direct-sales/new`, `/direct-sales/:id` | `DirectSaleEditor.tsx` | Direct sale (its own financial record): item, quantity, revenue, collected (X-06 partial debt / partial_needs_review), customerName (D-001), optional catalogItemId prefill (declared, editable), explicit cash destination (drawer default), realistic close screen (what sold / actual price / cash & debt effect / reference / open record / done). |
| `/schedule`, `/schedule/:id` | `Schedule.tsx`, `ScheduleEditor.tsx` | Local operational schedule: today/upcoming/overdue agenda, postpone with reason, capacity reading (bounded capacity G9), recurrence layer (weekly/monthly, G6-B), monthly view (G6-A). No financial effects. |
| `/finance` | `Finance.tsx` | Finance hub: split "الوضع الآن" (cash decision first) / "الفترة" (period reading `?view=period`); G5 decision panel; events layer ("السجل والأثر" — last 3 events, expandable full impact, `?event=` deep focus); corrections layer (all families); deposits layer; owner summary; supplier card; unallocated-cash difference explanation; corrections digest lines (all-time + in-period). |
| `/finance/new/:type` | `FinancialEventEditor.tsx` | One of 8 financial events with declared local effect: owner investment, owner withdrawal, operating expense paid, operating expense payable, payable settlement, amanah held, amanah released, non-cash loss. Expense context: relationship (project/shared), behavior (fixed/variable/mixed/unknown), purpose, knowledge; shared-project share modes (fixed/percentage/estimate/defer). G22 layered secondary details. |
| `/finance/withdraw` | `OwnerWithdrawalEditor.tsx` | Single entry "سحب من المشروع لنفسك؟" (X-05) writing to the correct owner path. |
| `/finance/owner-entitlement` | `OwnerEntitlement.tsx` | Owner entitlement (O1): summary first; layers for policy (dated, successor without rewriting history), records, opening balance (positive/negative), movements, ledger; `د.أ` wording (no "JOD minor" on surfaces). |
| `/finance/withdraw` editor + `OwnerWithdrawalEditor` | (same) | Owner draw/return/investment with documented reversals. |
| `/finance/g5/declaration` | `G5DeclarationEditor.tsx` | Dated short-cash declaration (collection/commitment) — reversible, never changes cash/receivable/profit (G5). |
| `/finance/statement` | `Statement.tsx` | Period statement (Group 2 §9.2): separates cash / result / amanah / receivables / payables / owner money; Sunday→Saturday week default, quick ranges + custom; every line links to its sources; restatement note; corrections line. |
| `/parties` | `Parties.tsx` | People's ledger (دفتر الناس): name-level aggregation over orders, sales, purchases, payables — read model, no CRM entity; search; collect entry with correct source (order/sale debt). |
| `/suppliers`, `/suppliers/purchase/:id(/payment)` | `Suppliers.tsx`, `SupplierPurchaseEditor.tsx` | Suppliers & purchases: card per purchase (total/paid/remaining + one payment CTA, M-24); purchase editor with payments, documented payment reversals and purchase revisions (before-values preserved). |
| `/cash` | `CashWallets.tsx` | Wallets: multi-wallet (cash_drawer/bank_account/digital_wallet/other), unallocated cash, allocation/coverage, count/transfer/distribute actions. |
| `/cash/wallet/:id` | `WalletLedger.tsx` | Wallet ledger: shallow read over wallet context; source links for allocations (sale/expense/collection/order). |
| `/cash/wallet/new` | `CashWalletEditor.tsx` | Create wallet; opening status known/unknown. |
| `/cash/wallet/:id/opening-later` | `CashOpeningLaterEditor.tsx` | Complete unknown opening balance later — documented additional event, no rewrite (D-004). |
| `/cash/wallet/:id/adjust` | `CashAdjustmentEditor.tsx` | Wallet adjustment with reason + idempotency. |
| `/cash/transfer` | `CashTransferEditor.tsx` | Transfer between wallets with direction validation. |
| `/cash/distribute` | `CashDistribution.tsx` | Distribute unallocated cash to wallets (allocation), or cover expenses (negative allocation). |
| `/cash/count` | `CashCount.tsx` | Cash count (عدّ الصندوق): count drawer vs recorded balance; difference recorded as documented adjustment — future effect only. |
| `/cash/entry/:id/reverse` | `CashReversalEditor.tsx` | Reverse a cash entry with reason. |
| `/inventory`, `/inventory/material/new` | `InventoryMaterials.tsx`, `MaterialEditor.tsx` | Materials & inventory: explicit dated activation; per-material position (quantity/value); movements: receipt, consume, waste (with wasteContext), adjust, reverse. |
| `/inventory/movement/:type`, `/inventory/movement/:id/reverse` | `InventoryMovementEditor.tsx`, `InventoryReversalEditor.tsx` | Record/reverse inventory movements with safe unknown-material path (G18). |
| `/catalog` | `Catalog.tsx` | Reference catalog: products/services, optional organized unit, default price/cost suggestions (proposals only, P-002), templates with components + yield (planning only), active toggle. |
| `/tools` | `Tools.tsx` | My Tools: calculator entry, saved estimates list (delete free), module states derived from real data (catalog/units/schedule/suppliers/parties). |
| `/tools/calculator` | `CostCalculator.tsx` | Deep cost calculator: materials/time/packaging/delivery/waste/safety/quantity, live result, declared uncertainty, dirty guard; save as estimate (same record — no duplicate estimates). |
| `/tools/estimate/:id` | `EstimateDetail.tsx` | Saved estimate: inputs, result, actions (bridge to draft / edit / delete), explicit qualifier "أداة تفكير بلا أثر مالي". |
| `/finance/new` etc. covered; `/review` | redirect → `/finance` | Weekly review merged as pulse inside Finance (F-003). |
| `/setup` | `Setup.tsx` | First-run setup: activity name, currency JOD, optional wallet with opening position question (skip path honest, F-002). |
| `/foundation` | `Foundation.tsx` | Permanent front door: setup state check, guided opening import entry, re-setup, direct links to first material recording. |
| `/settings` | `Settings.tsx` | Settings: info / preferences (theme, work mode, actual time) / appearance / sensitive data (verified export, import with validation, "ابدأ من جديد" reset gate behind verified export, guided opening import card, backup reminder prefs). |
| `/profile` | `Profile.tsx` | Owner profile: local identity, displayName, optional email, stable ownerId, quiet future-linking note; no login. |
| `*` | `NotFound.tsx` | 404. |

### 1.4 Domain model (12 modules, `src/domain/`)

| Module | Key entities / statuses | Financial write path |
|---|---|---|
| `craft-order` | `CraftOrder` (customerName, agreedPrice, costSnapshot + history, quantity), `OrderStatus`: draft → provisional_agreement → confirmed → in_progress → ready → delivered → settled / postponed / cancelled / needs_review; `SettlementStatus`: unpaid/partially_paid/paid/debt/cancelled(+pending/refunded/retained); `OrderEvent` log incl. price_revised, collection_reversed; `CostSnapshot` with knowledgeState + knowledgeGaps (mandatory/optional); ResultStatus final/estimated/incomplete/review_required | Orders never touch cash directly; collection goes through fulfillment/direct-sale owners, then cash allocation |
| `direct-sale` | `DirectSale` (revenue, collected, collectionStatus collected_in_full/partial_debt/partial_needs_review, customerName, catalogItemId optional, revisions edit/cancel/price_cut) | Own financial record; never inferred from order collections |
| `financial-event` | `FinancialEventType` (8): owner investment/withdrawal, operating expense cash/payable, payable settlement, amanah held/released, loss_non_cash; `OperatingExpenseContext` (relationship project/shared, behavior fixed/variable/mixed/unknown, purpose, knowledge); deltas per event: cashDelta, payableDelta, ownerCapitalDelta, operatingExpenseDelta, amanahDelta; corrections via reverse/replacement with reason + idempotency | Event write path with per-type declared effects |
| `cash-continuity` | `CashWallet` (kind cash_drawer/bank_account/digital_wallet/other, openingStatus known/unknown), `CashContinuityEntry` types: opening_balance / cash_adjustment / transfer_out/in / reversal / allocation; sourceRef (sale/expense/collection/order + lineId) linking allocations to their source records | Wallet ledger only; never classifies revenue/expense/capital |
| `inventory-material` | `Material` (unit piece/meter/kilogram/liter/other), `InventoryMovement` (opening/purchase_receipt/consumption/waste/adjustment/reversal) with quantityMilli, valueMinor, wasteContext, reversesMovementId | Purchase ≠ COGS; consumption evidence optional for G3 COGS |
| `owner-entitlement` | Policies (families time_period/fixed_amount/completed_work/profit_share/sale_percentage/unit; successor series without history rewrite), records, opening balances (±), owner movements (draw/return with reasons incl. pre_entitlement_draw, new_capital_investment) | Owner money separate from sales/expenses |
| `g5` | ShortCashDeclaration (collection/commitment, dated, knowledge, reversible), ContributionMargin/BreakEven from final orders + snapshot, ShortCash (recorded cash + declared + undated receivables/payables) | Declarations change nothing — read model |
| `catalog` | `CatalogItem` (product/service, unitId optional, defaultPrice/UnitCost suggestions), `MeasurementUnit` (dimension: count/mass/volume/time/distance/area), `DirectConversion` (exact rational, same dimension), `CatalogTemplate` (components + yield, planning only) | No financial or inventory effects ever |
| `actual-time` | `ActualTimeRecord` per order (minutesDelta, reversible), comparison planned vs actual | Time is not wage/cost/price (G4-B boundary) |
| `recurring-margin` | Allocation policies (manual_amount/per_output_unit/actual_time/completed_revenue_percentage) with successors, evidence-backed calculation | Loading is optional and declared, never silent |
| `supplier-purchase` | `SupplierPurchase` (total/paid/payable, status unpaid/partially_paid/paid, payments + paymentReversals + revisions with before-values) | Purchases affect cash/payables only |
| `shared` | JOD currency, MoneyMinor, roundHalfUp, quantityMilliExact, safe asserts | numeric safety helpers |

**Write path (enforced):** React page → Application service (`application/*`) → Domain (`src/domain`) → `PrototypeLocalStore` (`storage/local/*`) → IndexedDB. No direct UI→IndexedDB access (current-state.md §1). Single financial write source: collection passes the record's owning service (Fulfillment for orders, DirectSaleService for sales), then cash allocation via the single `distributeUnallocated` path with operation keys (current-state.md §Group 2 "مصدر الحقيقة الواحد"). Atomic transactions for coupled corrections (e.g. `commitOrderCollectionReversal` reverses order collection + its matching allocation in one transaction — `storage/local/types.ts:280-289`).

### 1.5 What Micro has TODAY per comparison topic

| Topic | Micro today (evidence) |
|---|---|
| Expense recording & classification | 8 typed financial events; quick expense sheet; expense context (project/shared, behavior, purpose, knowledge); shared-project share with 4 modes; period statement splits project vs shared vs unallocated; no user-defined named categories; no recurring expenses |
| Inventory/materials | Entirely optional + dated activation; per-material ledger with movements + reversals; per-order actual material panel; waste with context; positions feed optional COGS (recorded/partial/not_available) |
| Catalog | Product/service items, dimensioned units, exact same-dimension conversions, templates+yield planning, price/cost suggestions (P-002), catalog→direct-sale bridge |
| Cost calculation | Deep calculator + saved estimates + estimate→draft bridge; order cost snapshots with knowledge states; price floor; G4-B margin reading after optional loading |
| Orders | 10-status lifecycle + settlement statuses + event log + price revision/collection reversal corrections; deposits with settlement decisions; agreement source + follow-up |
| Statements/reports | On-screen period statement with source links; Finance period reading + insights (work-name profitability, cost composition, coverage, liquidity); corrections digest; **no exportable report files** |
| Corrections/reversals | Unified corrections history (11 kinds across events/sales/cash/purchases/orders), CorrectionPreview before every correction, atomic replacement, restore, mandatory reasons, idempotency keys, live idempotency (triple tap = one write) |
| Opening balances | Setup/foundation flow; wallet opening known/unknown ("غير محدد بعد" honest); opening-later completion; guided opening import (G82) with fixture validation; owner entitlement opening ± |
| Export/import | Full-store verified export (JSON, version 22) + atomic import with relation validation (incl. reversal stores, partial collections, price_cut), export preview counts, backup reminder, reset behind verified export; migration accepts older schema versions |
| PWA/offline | Service worker (prod-only, secure context), offline-ready, update flow, install banner with 30-day dismiss, runtime notice, offline reload verified in live QA (current-state.md §Group 4/5); device/Pilot acceptance still pending |

---

## 2. What is deliberately NOT implemented on main

From `docs/operations/current-state.md` (§5 "ما هو متوقف عمدًا" + §16–§22) and `docs/decisions/`:

1. **No new financial slices automatically** — the financial bundle G3→O1→G4-A→G4-B→G5 ended and merged via PR #115; any expansion needs an independent scope decision + contract + branch + PR (§5).
2. **No Market/Delivery** — E-00.14 is documentation-only (BottomNav market seat decided on paper; no UI/Domain/LocalStore/Auth/Cloud, §5 + §14).
3. **No Activity Profiles** — no food/services/agriculture/tourism/mixed schemas now (§5).
4. **Platform refusals:** no POS, no Auth, no Sync, no Cloud, no Banking, no CRM, no external calendar/reminders, no legal ledger, no taxes, no forecast, no AI (§5).
5. **Field acceptance pending:** Android/iOS device QA, standalone install acceptance, production offline, Cloudflare Pages production, human Pilot — all explicitly not accepted (§5; §Group 4/5/6 "حدود القبول").
6. **Deferred capabilities with contracts required:** assets/depreciation, loans, payroll, taxes, partial returns, forecasts — "مؤجل بعقد متخصص" (`docs/decisions/remaining-capabilities-review-v1.md:32`); "لا نخمن قواعدها" (no guessing their rules).
7. **Never-build list:** full CRM, WhatsApp automation, general retail POS, branches, MRP, AI-decides (`remaining-capabilities-review-v1.md:33`).
8. **Owner decisions deferred:** S2-04(a)-style UX refinements, Arabic-numeral normalization (tried and reverted), performance architecture items (S5-07/08/10/16) — documented deferrals, not gaps (§Group 5 "المؤجل الموثق").
9. **Next allowed step:** only the device-QA + human Pilot plan in `todo.md`; "لا مجموعة وظيفية جديدة قبل قرار مالك" (§Group 6 "الفعل التالي").

---

## 3. Gap classification map

Labels: `ZAMAN-ONLY` / `MICRO-WEAKER` / `MICRO-HIDDEN` / `MICRO-INCOMPLETE` / `MICRO-DIFFERENT` / `MICRO-SUFFICIENT` / `NOT-A-TRANSFER-CANDIDATE`.

```
finding_id: MG-01
capability_name: Expense classification & tracking (categories/types, recurring/personal/operating treatment)
comparison_classification: MICRO-DIFFERENT
zaman_evidence: artifacts/zman-app/src/features/finance/db.ts (expense table: category text + expenseCategoryCatalog pg-table 238-257, isCapitalAsset, costNature fixed/variable, isInventoryWriteoff); src/features/finance/components/PaymentsTab.tsx; drizzle/migrations/0005_finance_catalogs.sql, 0018_cost_classification.sql
micro_evidence: src/domain/financial-event/types.ts (OperatingExpenseContext relationship/behavior/purpose/knowledge + SharedProjectShare basis); apps/prototype-web/client/src/pages/FinancialEventEditor.tsx (shared modes fixed/percentage/estimate/defer); src/domain/g5/types.ts (G5ExpenseInput behavior/relationship); apps/prototype-web/client/src/application/finance/projectFinancialService.ts (period split project/shared/unallocated/legacy)
user_impact: A Zman-trained owner expects to pick a NAMED category ("بنزين"، "كراء"، "توصيل") and see per-category totals in a report. Micro instead asks decision-context questions (project vs shared, fixed/variable, purpose, knowledge) and shows behavior/shared splits in the period reading — powerful for truth, but there is no category vocabulary, no per-category summary, and no recurring-expense concept; grouping by "what kind of expense" is manual (notes only).
transfer_suitability: adapt
micro_destination: مالي (Finance) → FinancialEventEditor secondary layer (G22-style) + statement grouping: an OPTIONAL free-text/tag category list (local, non-financial) on OperatingExpenseContext; per-category statement lines derived read-only. Must NOT introduce auto-allocation or recurring writes.
confidence: high
open_questions: Should categories be a managed catalog (Zman-style) or free tags? Would per-category totals conflict with the "shared/unallocated" truth model? (Owner decision needed — G3 contract forbids hidden allocation.)
```

```
finding_id: MG-02
capability_name: Selective inventory & non-tracked items (per-item tracked/untracked choice)
comparison_classification: MICRO-DIFFERENT
zaman_evidence: artifacts/zman-app/src/features/catalog/db.ts (catalogComponent.tracked flag, migration 0019_catalog_tracked.sql); src/features/inventory/db.ts (catalog_movement in/out auto-created from purchase and order_delivery); src/app/(app)/catalog/CatalogClient.tsx (tracked toggle, untrack confirmation, stock display); src/features/finance/db.ts (purchase.isTrackedInventory capitalization, migration 0023)
micro_evidence: src/domain/inventory-material/types.ts (Material + movements: opening/purchase_receipt/consumption/waste/adjustment/reversal — nothing auto-fires on delivery); apps/prototype-web/client/src/storage/local/types.ts (InventoryActivation — explicit dated activation, decision 9); src/domain/direct-sale/types.ts (catalogItemId optional — sale never touches inventory); apps/prototype-web/client/src/components/order/ActualMaterialPanel.tsx + docs/decisions/actual-material-cost-per-order-g6-scope.md (per-order actual material)
user_impact: In Zman, flipping "tracked" on a catalog item makes purchases and deliveries move stock automatically and compute COGS on delivery. In Micro, inventory is opt-in as a whole (dated activation) and per-material; consumption is recorded deliberately (per order actual-material panel) and COGS only from consumption evidence — nothing auto-deducts at delivery. Owner used to Zman's automation must record consumption manually; owner who wants no inventory is actually better served by Micro.
transfer_suitability: reject
micro_destination: n/a (auto-deduct-on-delivery would violate Micro's explicit-evidence and purchase≠COGS boundaries; optional selection already exists at sale level)
confidence: high
open_questions: Could a per-material "auto-suggest consumption from the order's material list" (suggestion only, one tap, never silent) be a future adaptation? (Design decision, not a Zman transfer.)
```

```
finding_id: MG-03
capability_name: Cost calculation & pricing (materials/labor/overhead/waste/margin/estimate reuse)
comparison_classification: MICRO-SUFFICIENT
zaman_evidence: artifacts/zman-app/src/features/orders/components/ComponentsEditor.tsx + src/features/orders/db.ts (order components from catalog defaultCostCents + additional costs/profit migrations 0004/0013); no standalone calculator
micro_evidence: apps/prototype-web/client/src/pages/CostCalculator.tsx + /tools/estimate/:id (deep calculator, live result, uncertainty, dirty guard, save/edit/delete estimates); src/domain/craft-order/types.ts (CostSnapshot: materials/time/packaging/delivery/waste/safetyBuffer/quantity + knowledgeState + knowledgeGaps + priceFloor); storage/local/types.ts CostEstimate; Group 3 estimate→draft bridge (current-state.md §Group 3)
user_impact: None missing; Micro's calculator/estimate system is materially deeper than Zman's component-default-cost pricing (knowledge states, price floor, safety buffer, estimate reuse without duplication). Zman offers nothing here Micro lacks.
transfer_suitability: reject (nothing to transfer; reverse direction)
micro_destination: n/a
confidence: high
open_questions: none
```

```
finding_id: MG-04
capability_name: Catalog with units & conversions
comparison_classification: MICRO-SUFFICIENT
zaman_evidence: artifacts/zman-app/src/features/catalog/db.ts (unit is free text, default "قطعة"; no dimension model, no conversions, no templates); src/app/(app)/catalog/CatalogClient.tsx
micro_evidence: src/domain/catalog/types.ts (MeasurementUnit with dimension count/mass/volume/time/distance/area; DirectConversion exact rational within dimension; CatalogTemplate components+yield planning; contract 15 docs/contracts/15-catalog-reference-prototype-contract.md); apps/prototype-web/client/src/pages/Catalog.tsx
user_impact: Reverse gap — Zman units are free text with no conversion math; Micro has organized units, exact conversions, and templates. A Zman owner migrating to Micro gains capability.
transfer_suitability: reject (reverse gap)
micro_destination: n/a
confidence: high
open_questions: none
```

```
finding_id: MG-05
capability_name: Orders workflow (statuses, preparation, fulfillment, delivery/collection)
comparison_classification: MICRO-SUFFICIENT
zaman_evidence: artifacts/zman-app/src/features/orders/db.ts (status draft/sent/confirmed/delivered/cancelled); src/features/orders/components/OrderDetail.tsx (status ladder 290-299, deposit refund/retain/forfeit modals, convert-order-to-sale with revenue + stock out)
micro_evidence: src/domain/craft-order/types.ts (10 statuses incl. needs_review, in_progress, ready, settled, postponed; SettlementStatus unpaid/partially_paid/paid/debt/cancelled_*; OrderEvent log incl. price_revised & collection_reversed; DepositSettlementDecision incl. needs_review); pages/OrderDetail.tsx, AgreementEditor, fulfillment/collection flows
user_impact: Micro's lifecycle is richer and conceptually stricter (needs_review gating, collection≠profit). Zman's only unique affordance is the explicit "convert order to sale" revenue moment — Micro deliberately recognizes revenue without auto-cash. Not a gap for the target persona; INFERENCE: a Zman owner may look for a single "أغلق الطلب" action but Micro's settlement review serves it.
transfer_suitability: reject
micro_destination: n/a
confidence: high
open_questions: none
```

```
finding_id: MG-06
capability_name: Finance accounts/wallets & transfers
comparison_classification: MICRO-SUFFICIENT
zaman_evidence: artifacts/zman-app/src/features/finance/db.ts (account cash/bank, cash_movement with transfer sourceType, AccountsTab); src/app/(app)/finance/accounts/page.tsx
micro_evidence: src/domain/cash-continuity/types.ts (wallet kinds cash_drawer/bank_account/digital_wallet/other; entry types opening/adjustment/transfer_in-out/reversal/allocation with sourceRef links); pages/CashWallets.tsx, CashTransferEditor, CashDistribution, WalletLedger, CashCount; unallocated-cash concept
user_impact: Reverse gap — Micro adds digital wallets, unknown-opening honesty, unallocated cash with allocation/coverage, cash count reconciliation, and per-wallet ledgers with source links. Zman has plain accounts + transfers only.
transfer_suitability: reject (reverse gap)
micro_destination: n/a
confidence: high
open_questions: none
```

```
finding_id: MG-07
capability_name: Period result / P&L
comparison_classification: MICRO-WEAKER
zaman_evidence: artifacts/zman-app/src/features/finance/pnl.ts (computeOperatingPnl: sales, operating expenses/purchases, capital additions, depreciation, COGS, write-offs, operatingNet — LOCKED-6 single source); src/features/reports/actions.ts getFinancialPosition (balance sheet with assets/liabilities/equity + reconciliation); src/features/dashboard/components/MonthlyProfitPanel.tsx
micro_evidence: apps/prototype-web/client/src/application/finance/projectFinancialService.ts (RecordedPeriodResult with COGS status, shared splits, direct-sale revenue, result status recorded_only/incomplete/invalid); pages/Statement.tsx (period statement separating cash/result/amanah/receivables/payables/owner money with source links); current-state.md G3 limits: "ليست COGS كاملة/قانونية ولا صافي ربح نهائي أو ضريبي"
user_impact: The owner CAN see an honest recorded period result in-app, but (a) it is on-screen only — no exportable P&L artifact to share with an accountant/family; (b) no balance-sheet view (assets = liabilities + equity with reconciliation); (c) no cross-period retained-result view; (d) no depreciation/capital line (by design until contracts exist). A Zman owner "closing the month" gets a full P&L + balance sheet download; a Micro owner gets a truthful but narrower in-app reading.
transfer_suitability: adapt
micro_destination: مالي (Finance) → /finance/statement gains an export action (Markdown/text, same read model, zero new writes); later: balance-sheet-shaped reading layer (owner money + amanah + receivables/payables already exist as honest components)
confidence: high
open_questions: Export format (Markdown like Zman vs PDF vs clipboard text)? Any equity-reconciliation surface must respect "missing ≠ zero" and refuse "final net profit" wording — needs owner decision + contract before building.
```

```
finding_id: MG-08
capability_name: Finance integrity check
comparison_classification: ZAMAN-ONLY
zaman_evidence: artifacts/zman-app/src/features/finance/integrityCheck.ts (runFinancialIntegrityCheck, IC-1..IC-16 over INV-1..INV-17: equity drift, orphans, deposit consistency, unit consistency, P&L reconciliation, asset book value); src/features/reports/components/IntegrityCheckReportPanel.tsx; /reports page
micro_evidence: No user-facing integrity surface. Micro's equivalents are structural: single write path + idempotency, corrections digest (application/finance/correctionHistoryService.ts CorrectionDigest on 5 surfaces, Group 6 item 3), import verifier validating all relations (application/transfers/localTransferService.ts), domain tests incl. public-surface lock test. Nothing lets the OWNER press "check my numbers".
user_impact: When something feels wrong ("the cash number looks off"), the Micro owner has no one-tap self-audit that verifies the five boundaries, flags unallocated differences, unbalanced reversals, orphan references, or double-counted revenue. They must trust the design or call support.
transfer_suitability: adapt
micro_destination: أدواتي (Tools) → new read-only "فحص سلامة مالي" screen (or مالي deep layer) built ONLY from existing read models, mapping Micro's own invariants (collection≠profit checks on data, corrections digest, unallocated reconciliation, import-verifier rules reused at runtime) — no new writes, no new stores
confidence: high
open_questions: Which invariant set is meaningful for Micro (5 boundaries + reversal balance + sourceRef integrity + statement=position reconciliation per Group 5 S2/G5-S7 fixes)? Where does it live (أدواتي fits "thinking tool" identity; مالي fits money truth)?
```

```
finding_id: MG-09
capability_name: Opening balance setup
comparison_classification: MICRO-SUFFICIENT
zaman_evidence: artifacts/zman-app/src/features/finance/db.ts (openingBalance: go-live date, cash/bank/capital, isLocked); src/app/(app)/settings/opening-balance/OpeningBalanceClient.tsx
micro_evidence: pages/Setup.tsx + Foundation.tsx (permanent front door); CashWalletOpeningStatus known/unknown with "غير محدد بعد" honesty; CashOpeningLaterEditor (D-004 documented later completion); application/transfers/guidedOpeningImportService.ts + docs/contracts/21-guided-opening-import-prototype-contract.md + docs/fixtures/g82-guided-opening-import-fixtures.json; owner-entitlement opening ±
user_impact: Reverse gap — Micro's opening model is more honest and more recoverable (unknown ≠ zero, later completion, guided import with error report). Zman's lock flag is a simpler but cruder affordance. INFERENCE: Zman's "lock after go-live" concept could inspire a future Micro guard, but Micro already prevents opening rewrites by design (append-only events).
transfer_suitability: reject
micro_destination: n/a
confidence: high
open_questions: none
```

```
finding_id: MG-10
capability_name: Assets & depreciation
comparison_classification: ZAMAN-ONLY
zaman_evidence: artifacts/zman-app/src/features/depreciation/db.ts (capital_asset: usefulLifeMonths, monthlyDepreciationCents, startedAt=purchaseDate); actions.ts (addCapitalAsset); AssetsScreen.tsx; /assets page; pnl.ts depreciation in operating net; IC-14 book value
micro_evidence: None. Explicitly deferred: "أصول، إهلاك… مؤجل بعقد متخصص… لا نخمن قواعدها" (docs/decisions/remaining-capabilities-review-v1.md:32). Hook exists conceptually: loss_non_cash event type reduces period profit without cash (src/domain/financial-event/types.ts:69-74) — but no asset register, no depreciation schedule.
user_impact: An owner who buys a sewing machine or oven cannot spread its cost over its life; the purchase either sits as a plain purchase/expense or is invisible to the period result. Period result overstated for asset-heavy crafts. (For the current persona — home micro-businesses — low frequency, but real when it happens.)
transfer_suitability: adapt (LATER, gated)
micro_destination: مالي (Finance) deep editor, modeled as: asset register + monthly non-cash depreciation expressed through the existing loss/policy machinery; requires a Micro contract first (family, methods, Jordanian norms, disposal) — must not enter cash and must show as declared non-cash reduction
confidence: high
open_questions: Which depreciation conventions are honest for this persona (straight-line only)? Disposal/partial-year rules? This is exactly the "specialized contract" Micro's docs demand before code.
```

```
finding_id: MG-11
capability_name: Audit log
comparison_classification: MICRO-DIFFERENT
zaman_evidence: artifacts/zman-app/src/features/audit/db.ts (audit_log append-only: action, entityType, entityId, userId, changesSnapshot jsonb); actions.ts logAction outside transactions (swallows errors); /settings/audit-log page with pagination
micro_evidence: application/finance/correctionHistoryService.ts (11 correction kinds with recordedAt, occurredOn, signed amount effect, reason, original/replacement labels, deep links); components/finance/CorrectionsLayer.tsx (Finance layer); CorrectionPreview before every correction; originals never deleted (all reversal/revision types preserve before-values); INFERENCE: ordinary creates are not logged anywhere as a unified stream — they are visible in their own lists only.
user_impact: Micro records WHO-did-WHAT only for corrections (with reasons and previews — stronger than Zman there), but the owner cannot open one chronological log of every create/update across orders, sales, events, wallets to answer "what did I change last week?" (Zman's /settings/audit-log answers it for financial ops).
transfer_suitability: adapt
micro_destination: سجّل/مالي → a read-only unified "activity layer" derived from existing records (orders' events, sales' revisions, financial events' recordedAt, cash entries, corrections) — same pattern as partyLedger (read model, no new store, no userId needed since single-owner)
confidence: medium
open_questions: Is a full changes-snapshot audit (Zman's jsonb) ever needed in a single-owner local app, or is derived-read + corrections enough? Merges naturally with MG-12.
```

```
finding_id: MG-12
capability_name: Activities feed
comparison_classification: MICRO-INCOMPLETE
zaman_evidence: artifacts/zman-app/src/app/(app)/activities/page.tsx (unified feed of orders/sales/expenses/purchases with amounts, icons, deep links into the right tab+edit); src/features/dashboard/queries.ts useRecentActivities
micro_evidence: Pieces exist: Finance "السجل والأثر" events layer (last 3 + expandable full impact — pages/Finance.tsx imports EventsLayer), corrections layer, Orders list, Parties movements, wallet ledgers; Home "الأهم الآن" surfaces urgent items. No single cross-record recent-activity surface.
user_impact: "شو صار اليوم/هالأسبوع؟" across everything (order created, sale recorded, expense paid, payment reversed) requires visiting 4+ surfaces. Zman's /activities answers it in one list with one tap into each record.
transfer_suitability: adapt
micro_destination: مشروعي الآن (Home) → a "آخر ما صار" block (or a سجّل reading layer reachable from the FAB menu/home) — pure read model over existing stores (orders' events, directSales.recordedAt + revisions, financialEvents, cashContinuityEntries, corrections), no new writes
confidence: medium-high
open_questions: Home already resists dashboard-style clutter (decision-first principle); would a bounded "last N with مزيد" compromise the "الأهم الآن" priority? Needs UX decision; alternatively a deep reader page under مالي.
```

```
finding_id: MG-13
capability_name: Reports (filters, summaries, period views)
comparison_classification: MICRO-WEAKER
zaman_evidence: artifacts/zman-app/src/app/(app)/reports/page.tsx (6 report types: pnl, expenses, sales, orders, products, balance_sheet; date ranges all/month/30d; as-of for balance sheet; Markdown download with BOM); src/features/reports/actions.ts downloadReport/getAllReportData
micro_evidence: On-screen only: pages/Statement.tsx (week/last-week/month/custom ranges with source links); Finance period view + insights (work-name profitability, cost composition, coverage, liquidity — application/finance/projectFinancialService.ts FinancialInsights); NO downloadable report artifacts; export exists only as full-data JSON backup (localTransferService)
user_impact: The owner cannot hand an accountant/lender/family member a period report file. All Micro readings are on-screen and data-local; Zman produces six structured Markdown reports. Also no products-by-profitability export (Micro shows work-name profitability in-app only).
transfer_suitability: adapt
micro_destination: مالي (Finance) → /finance/statement export action (Markdown/text) reusing the existing StatementReading; optional second: work-name profitability export from FinancialInsights. Read-only, no schema/export changes (stays outside schema 30/export 22).
confidence: high
open_questions: Language/format (Arabic Markdown like Zman? PDF later via documents pipeline?); whether "تقرير المنتجات" needs catalog linkage depth Micro deliberately avoids (P-002 keeps catalog non-financial — work-name profitability is the honest equivalent).
```

```
finding_id: MG-14
capability_name: Snippets/notes (reusable text library)
comparison_classification: ZAMAN-ONLY
zaman_evidence: artifacts/zman-app/src/features/snippets/db.ts (snippet: title/body/category ≤5000 chars); /snippets page + SnippetsClient.tsx; used as reusable text (incl. WhatsApp template ecosystem — WhatsAppTemplateEditor.tsx in orders)
micro_evidence: Free-text notes exist on every record (note fields across domain types), and G22 made the note required-safe with Arabic messages; no reusable snippet library anywhere in storage/local/types.ts LocalStoreSnapshot
user_impact: An owner repeatedly typing the same order specifications, follow-up phrases, or product descriptions cannot save/reuse them. Low severity, but a real daily friction for repetitive crafts (e.g., standard specification text).
transfer_suitability: adapt
micro_destination: أدواتي (Tools) → "ملاحظاتي المتكررة" local store (non-financial, like CostEstimate precedent: a thinking tool with zero effects); optional one-tap "استخدم في" prefill for order specifications/agreement notes
confidence: high (classification); medium (transfer value — needs persona validation)
open_questions: Would snippet prefill silently weaken the "specifications are per-order truth" discipline? Must remain a copy-paste convenience, never a template that auto-fills prices.
```

```
finding_id: MG-15
capability_name: Dashboard
comparison_classification: MICRO-DIFFERENT
zaman_evidence: artifacts/zman-app/src/features/dashboard/components/DashboardClient.tsx (+MonthlyProfitPanel, SmartAlertsBar, UpcomingDeliveriesCard, FinanceComparePanel, LiquidityFlowPanel, GlobalSearch); / route
micro_evidence: pages/Home.tsx "الأهم الآن" decision-first control center (one most-urgent action, financial facts with knowledge states, today list, honest empty state); Finance position view; deliberately NOT a dashboard (docs/product/placement-principles-v1.md + home-navigation-proof-v1.md; BottomNav comment "no generic ERP chrome")
user_impact: A Zman owner sees analytical panels (monthly profit trend, comparison, liquidity flow). A Micro owner sees the single next action plus honest facts. Micro's model is a deliberate product identity choice, not a defect; the analytics Zman shows are partially covered by Finance period layer (insights/coverage/liquidity) but with no trend visualization.
transfer_suitability: reject (identity conflict: dashboard panels vs decision-first home); optional micro-adapt later: a simple month-over-month reading INSIDE Finance period layer (not Home) if Pilot asks
micro_destination: n/a (optional future: مالي → period layer trend line)
confidence: high
open_questions: none material
```

```
finding_id: MG-16
capability_name: Auth/login
comparison_classification: NOT-A-TRANSFER-CANDIDATE
zaman_evidence: artifacts/zman-app/src/middleware.ts (PASSCODE cookie gate, fail-closed); src/app/login/page.tsx + actions.ts; src/components/auth/IdleLock.tsx
micro_evidence: Explicit product constraint: local-first, no auth, no accounts, no cloud (README.md; current-state.md §1, §5; OwnerProfile provider/externalAccountId null by design; storage types.ts:42-46)
user_impact: None — Micro is single-owner local by definition; adding auth would break the offline-first promise and the current phase gates (MVP commercial later).
transfer_suitability: reject
micro_destination: n/a
confidence: high
open_questions: none (future account-linking is already reserved in OwnerProfile fields)
```

```
finding_id: MG-17
capability_name: Customer/supplier relationships
comparison_classification: MICRO-SUFFICIENT
zaman_evidence: artifacts/zman-app/src/features/orders/db.ts (customer name/phone on orders); src/features/finance/db.ts (purchase.supplier text; receivable.personName + receivablePayment); no CRM entities
micro_evidence: pages/Parties.tsx + application/parties/partyLedgerService.ts (name-level party ledger aggregating order debts/collections, sale debts/collections, purchase payables/payments, settlements; search; per-party net; collect entry with source); Suppliers.tsx cards; Collect.tsx single documented collection sheet with three entrances
user_impact: Reverse gap for reading (Micro's per-party ledger with movements + net is richer than Zman's scattered personName fields); both lack true relationship entities (addresses, history pages) — deliberately out of scope in both.
transfer_suitability: reject (reverse gap; CRM explicitly never-build in Micro)
micro_destination: n/a
confidence: high
open_questions: none
```

```
finding_id: MG-18
capability_name: Data export/import/backup
comparison_classification: MICRO-SUFFICIENT
zaman_evidence: artifacts/zman-app/src/components/shared/BackupModal.tsx (client-side JSON export of accounts/catalog/opening balance/assets/recent 100 orders only; NO import/restore path found)
micro_evidence: application/transfers/localTransferService.ts (full-store verified export version 22 + atomic replaceSnapshot import validating G3/O1/G4/G5 relations, template/unit/conversion, successor/reversal, actual-time, partial collections, price_cut); guidedOpeningImportService.ts; Settings reset gate behind verified export; backup reminder (O-001/P-01); migrations accept older versions
user_impact: Reverse gap — Zman's backup is partial and one-way (no restore); Micro's is full, verified, restorable, and migration-aware. Zman owner switching phones loses expenses/sales history in the backup; Micro owner does not.
transfer_suitability: reject (reverse gap)
micro_destination: n/a
confidence: high
open_questions: none
```

Additional capability areas found during comparison (not in the original list):

```
finding_id: MG-19
capability_name: WhatsApp messaging integration (templates, share)
comparison_classification: NOT-A-TRANSFER-CANDIDATE
zaman_evidence: artifacts/zman-app/src/lib/whatsapp.ts; src/features/orders/components/WhatsAppTemplateEditor.tsx; snippets used as message templates
micro_evidence: Micro's never-build list: "WhatsApp automation" خارج النطاق (docs/decisions/remaining-capabilities-review-v1.md:33); no messaging code anywhere
user_impact: Micro owner shares order/price info manually outside the app. Accepted product boundary.
transfer_suitability: reject (explicit never-build; also external dependency conflicts with local-first CSP posture)
micro_destination: n/a
confidence: high
open_questions: none
```

```
finding_id: MG-20
capability_name: Global search (cross-record)
comparison_classification: MICRO-WEAKER
zaman_evidence: artifacts/zman-app/src/features/dashboard/components/GlobalSearch.tsx (search across orders/customers from dashboard)
micro_evidence: Search exists only per-surface: Parties search (pages/Parties.tsx useState query); catalog browsing; no cross-record search over orders+sales+events+parties
user_impact: Finding "that order for أم محمد" or an old expense requires knowing which surface holds it. With local data volumes (hundreds of records) the friction is real but bounded.
transfer_suitability: adapt (low priority)
micro_destination: مشروعي الآن/العمل → a read-only search over existing stores (same read-model pattern as partyLedger); no index store needed at this scale
confidence: medium (gap real; priority low — INFERENCE from data volumes and persona)
open_questions: Worth building before Pilot? Device performance on low-end phones (Group 5 deferred performance items)?
```

```
finding_id: MG-21
capability_name: Idle auto-lock / privacy lock
comparison_classification: NOT-A-TRANSFER-CANDIDATE
zaman_evidence: artifacts/zman-app/src/components/auth/IdleLock.tsx
micro_evidence: No lock; no auth by design. (PWA install + local device lock are the assumed protections.)
user_impact: None today; if Pilot shows shared-device usage, revisit as an OS-level/device concern, not an app auth layer.
transfer_suitability: reject (for this phase)
micro_destination: n/a
confidence: high
open_questions: Revisit only with owner decision after Pilot evidence.
```

**Classification counts:** MICRO-SUFFICIENT 7 (MG-03, 04, 05, 06, 09, 17, 18) · MICRO-DIFFERENT 4 (MG-01, 02, 11, 15) · MICRO-WEAKER 3 (MG-07, 13, 20) · ZAMAN-ONLY 3 (MG-08, 10, 14) · MICRO-INCOMPLETE 1 (MG-12) · NOT-A-TRANSFER-CANDIDATE 3 (MG-16, 19, 21). Total 21 findings.

**Highest-value transfer candidates (adapt):** MG-13 report export → MG-08 integrity self-check → MG-12 unified activity layer (merges MG-11) → MG-01 optional category vocabulary → MG-14 snippets (lowest). **Gated/future:** MG-10 assets & depreciation (needs contract). **Reject:** automation-based inventory (MG-02), dashboard panels (MG-15), auth (MG-16), WhatsApp (MG-19).

---

## 4. False-gap warnings

Zman capabilities that LOOK missing in Micro but are actually present or stronger — do NOT report these as gaps:

1. **Catalog units & conversions (reverse gap).** Zman `catalogComponent.unit` is free text ("قطعة") with no conversions (`artifacts/zman-app/src/features/catalog/db.ts:10`). Micro has dimensioned `MeasurementUnit` + exact `DirectConversion` + templates/yield (`src/domain/catalog/types.ts`). Micro is strictly stronger.
2. **Multi-account cash management.** Zman: cash/bank accounts + transfers. Micro: 4 wallet kinds incl. digital_wallet, unknown-opening honesty, unallocated-cash allocation/coverage, per-wallet ledgers with source links, cash count reconciliation (`src/domain/cash-continuity/types.ts`, `pages/CashWallets.tsx`). Micro stronger.
3. **Opening balances.** Zman: one locked row (cash/bank/capital). Micro: known/unknown status ("غير محدد بعد" — never zero), later-completion editor (D-004), guided import with fixtures, owner-entitlement opening ±. Micro stronger and safer.
4. **Export/backup.** Zman `BackupModal.tsx` exports a partial JSON (no restore). Micro exports the full verified store with validated atomic import + migrations (`localTransferService.ts`). Micro stronger.
5. **Cost calculation.** Zman has only order components with default costs. Micro has a dedicated calculator, saved estimates with reuse bridge, snapshot knowledge states, price floor, safety buffer. Micro stronger.
6. **Orders workflow depth.** Zman: 5 statuses + convert-to-sale. Micro: 10 statuses + settlement statuses + event log + documented price/collection corrections + needs_review gating. Micro deeper (concepts differ — see MG-05).
7. **Customer/supplier visibility.** Zman personName is scattered; Micro's Parties read-model gives per-party net position + movements + collect entry (`partyLedgerService.ts`). Micro stronger for the reading task.
8. **Corrections/undo.** Zman: undo-delete + reverseSale soft-deletes. Micro: full reversal/replacement system with reasons, previews, atomic commits, restore, 11-kind unified corrections history. Micro stronger.
9. **Inventory write-off.** Zman: `isInventoryWriteoff` expenses from adjustStock. Micro: `loss_non_cash` financial event + waste movements with `wasteContext` (`src/domain/financial-event/types.ts`, `src/domain/inventory-material/types.ts`). Equivalent present.
10. **PWA/install.** Both have install affordances; Micro's is runtime-verified with offline reload in live QA (current-state.md §Group 4/5) — though device acceptance is still pending for both products' claims.

Inverse warning (for honesty): things that look like Micro gaps because Micro *chose* different words — "صافي الربح النهائي" (final net profit) absence is a boundary, not a missing feature (current-state.md §4); treat "P&L label" requests carefully before promising transfers that violate the boundary.

---

## 5. Evidence index

**Micro (repo `Micro` @ 4db6a5f):**
- Live state: `docs/operations/current-state.md` (§1 general, §2 published, §3 G3–G5 bundle, §5 stopped-on-purpose, §16–§22 Groups 1–6)
- Entry docs: `README.md`, `AGENTS.md`, `docs/00-document-index.md`, `docs/02-decision-log.md`
- Product: `docs/product/problem-statement-v4.md`, `docs/product/system-definition-v1.md`, `docs/product/user-operating-model-v1.md`, `docs/product/financial-operating-model-v1.md`, `docs/product/placement-principles-v1.md`, `docs/product/home-navigation-proof-v1.md`, `docs/product-source-of-truth.md`
- Contracts: `docs/contracts/05-financial-p0-policies.md`, `06-financial-event-prototype-contract.md`, `08-expense-classification-prototype-contract.md`, `10-cash-continuity-prototype-contract.md`, `11-inventory-material-consumption-prototype-contract.md`, `13-actual-material-per-order-prototype-contract.md`, `14-period-result-allocation-policy-prototype-contract.md`, `15-catalog-reference-prototype-contract.md`, `16-optional-operating-mode-and-actual-time-contract.md`, `17-contribution-break-even-short-cash-g5-contract.md`, `21-guided-opening-import-prototype-contract.md`, `26-navigation-referrer-and-deep-link-contract.md`
- Decisions/scope: `docs/decisions/remaining-capabilities-review-v1.md`, `docs/decisions/optional-capability-knowledge-model-v1.md`, `docs/decisions/actual-material-cost-per-order-g6-scope.md`
- Navigation/app: `apps/prototype-web/client/src/app/MicroRouter.tsx`, `navigation.ts`, `navigationContract.ts`, `routeClassifier.ts`, `useReturnNavigation.ts`, `StartupGate.tsx`; `components/layout/MicroAppShell.tsx`, `BottomNav.tsx`, `AppHeader.tsx`, `QuickActionSheet.tsx`
- Pages (42): `apps/prototype-web/client/src/pages/` — Home, Orders, OrderDetail, NewDraft, DraftEditor, CostEditor, AgreementEditor, DirectSaleEditor, Schedule, ScheduleEditor, Finance, FinancialEventEditor, OwnerEntitlement, OwnerWithdrawalEditor, G5DeclarationEditor, Statement, Parties, Suppliers, SupplierPurchaseEditor, CashWallets, CashWalletEditor, CashOpeningLaterEditor, CashAdjustmentEditor, CashTransferEditor, CashReversalEditor, CashDistribution, CashCount, WalletLedger, Collect, InventoryMaterials, MaterialEditor, InventoryMovementEditor, InventoryReversalEditor, Catalog, Tools, CostCalculator, EstimateDetail, Setup, Foundation, Settings, Profile, NotFound
- Domain: `src/domain/{craft-order,direct-sale,financial-event,cash-continuity,inventory-material,owner-entitlement,g5,catalog,actual-time,recurring-margin,supplier-purchase,shared}/{types,policies}.ts`
- Storage: `apps/prototype-web/client/src/storage/local/types.ts` (schema 30 / export 22, OwnerProfile, LocalStoreSnapshot, PrototypeLocalStore), `persistentStorage.ts`, `IndexedDbLocalStore.ts`
- Services: `application/finance/projectFinancialService.ts`, `statementService.ts`, `correctionHistoryService.ts`, `ownerEntitlementService.ts`; `application/transfers/localTransferService.ts`, `guidedOpeningImportService.ts`; `application/parties/partyLedgerService.ts`; `application/cash/cashContinuityService.ts`, `walletLedgerService.ts`; `application/collections/collectionService.ts`, `collectionReversalService.ts`; `application/home/homeControlCenterModel.ts`; `application/estimates/costEstimateService.ts`
- PWA: `apps/prototype-web/client/src/pwa/register.ts`, `install.ts`, `PwaInstallControl.tsx`, `PwaRuntimeNotice.tsx`
- Tests: `tests/domain/*.test.ts` (16 files incl. `public-surface.test.ts`, `amanah-loss.test.ts`, `cash-allocation.test.ts`), `apps/prototype-web/client/src/*.test.*` (U/G/D series), `pages/*.ui.test.*`

**Zman (repo `zman-app` @ bdd63ab, enumerated for comparison):**
- Routes: `artifacts/zman-app/src/app/(app)/{page,orders,finance,finance/accounts,catalog,inventory,reports,activities,assets,snippets,settings/audit-log,settings/opening-balance}` + `src/app/login/page.tsx` + `src/middleware.ts`
- Features: `src/features/finance/db.ts` (purchase/expense/sale/account/cashMovement/ownerTransaction/openingBalance/receivable/receivablePayment + purchaseItemCatalog/expenseCategoryCatalog), `finance/pnl.ts`, `finance/integrityCheck.ts`, `finance/components/{AccountsTab,PaymentsTab,SalesTab,OwnerTab,OpeningTab,SmartFinanceForm,ReceivablePaymentModal}.tsx`; `src/features/catalog/db.ts` (tracked flag); `src/features/inventory/db.ts` (catalog_movement); `src/features/orders/db.ts` + `orders/components/{OrderDetail,ComponentsEditor,OrderForm,StatusFilterSheet,OrderCalendar,WhatsAppTemplateEditor}.tsx`; `src/features/depreciation/{db,actions,AssetsScreen}.ts(x)`; `src/features/audit/db.ts`; `src/features/snippets/db.ts`; `src/features/reports/actions.ts` (downloadReport 6 types, getFinancialPosition); `src/features/dashboard/components/*`; `src/components/shared/BackupModal.tsx`; `src/lib/whatsapp.ts`; drizzle migrations 0000–0028 (esp. 0005 finance catalogs, 0018 cost classification, 0019 catalog tracked, 0022 capital assets, 0023 inventory capitalization, 0026 audit logs, 0027 receivables)
