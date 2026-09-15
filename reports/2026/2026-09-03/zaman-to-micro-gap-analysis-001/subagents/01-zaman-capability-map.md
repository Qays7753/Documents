# Zman Capability Map — Full Capability Catalogue (Source Product)

- **Task ID:** SA-1 (Zman Capability Mapper, sub-agent of Zman→Micro gap analysis)
- **Date:** 2026-09-03
- **Repo state analyzed:** local read-only clone `/home/z/my-project/repos/zman`, branch `main` @ `bdd63ab` (github.com/Qays7753/zman-app.git)
- **Methodology:** Every claim below was verified by reading actual files in the clone (code, schema, migrations, docs). File paths are cited per capability. Anything not directly verified is labeled `INFERENCE`. The Zman repo was NOT modified. Money throughout: fils (integer, 1 JOD = 1000 fils), formatted by `formatFilsToJod` (`artifacts/zman-app/src/lib/money.ts`).
- **Terminology note:** product name is "Zman" (repo `zman-app`). CLAUDE.md at repo root is the project's own status/rules document; `artifacts/zman-app/docs/ACCOUNTING_RULES.md` is the financial constitution (INV-1..INV-25, IC-1..IC-16 as implemented).

---

## 1. Product overview

**What Zman IS:** a single-user (workshop owner) Arabic RTL financial + order management PWA for a small plant/nursery workshop ("Zman Greens JO" per `src/app/manifest.ts`). The owner uses it ~95% of the time on a phone (360–390px) (`CLAUDE.md` §10). Its core promise, in the owner's words, is "one profit number the owner can trust" — cash-basis ledger with exactly three read-time non-cash adjustments (COGS, inventory write-off, depreciation).

- **Stack:** Next.js 15 App Router + React 19 + TypeScript, Tailwind (logical RTL properties only), react-hook-form + Zod, TanStack Query, Drizzle ORM + postgres.js, Sonner toasts, lucide icons. PWA via `public/sw.js` + `src/app/manifest.ts` + `src/components/pwa/*`.
- **Architecture:** pnpm monorepo. Deployable app: `artifacts/zman-app` (Vercel, Root Directory = `artifacts/zman-app`). Data layer: Server Actions (`src/features/*/actions.ts` with `"use server"`) calling Drizzle directly — **the app does NOT use the Express api-server** (verified: no import of `api-client-react`/`api-zod` anywhere in zman-app; `lib/api-spec/openapi.yaml` only defines `/healthz`). `artifacts/api-server` (Express + pino + auth middleware, routes for auth/catalog/dashboard/finance/orders/snippets) is a parallel/alternative artifact; `artifacts/mockup-sandbox` is a Vite component-preview sandbox for shadcn design mockups (gallery + `/preview/<Component>` routes, `mockup-sandbox/src/App.tsx`).
- **Data layer:** PostgreSQL on Supabase (Supavisor pooler, `src/lib/db/client.ts`: `connect_timeout 10`, `idle_timeout 30`, `prepare:false`). Table definitions live in feature `db.ts` files (`finance/db.ts`, `orders/db.ts`, `catalog/db.ts`, `inventory/db.ts`, `depreciation/db.ts`, `audit/db.ts`, `snippets/db.ts`) and are pushed via `drizzle-kit push --force` (migrations 0000–0028 exist but cannot build from an empty DB — ACCOUNTING_RULES §11.1; `CLAUDE.md` §6 documents manual application of 0017–0025 via Supabase SQL Editor).
- **Auth model:** single shared passcode. `src/app/login/actions.ts` sets `zman_session` cookie (httpOnly, `secure` conditional on NODE_ENV — was `true` always, fixed; `sameSite:strict`, 8h maxAge). `src/middleware.ts` protects every route (fail-closed if `PASSCODE` unset) and exempts `/api`, `/login`, static assets. `src/components/auth/IdleLock.tsx` locks the app after 10 minutes idle via `visibilitychange` + logoutAction. Audit `userId` is hardcoded `"owner"` (never reads the cookie, to avoid persisting the passcode — `src/features/audit/actions.ts`).
- **Key non-functional behaviors:** Amman-timezone dates (`getAmmanDate()` in `src/lib/utils.ts`); optimistic delete-with-undo pattern (`src/lib/undo-delete.ts`, 5s countdown + `pagehide` fire-and-forget commit); online assert before mutations (`src/lib/online.ts` `assertOnline()` → toast "لا يوجد اتصال — لم يُحفظ. أعد المحاولة."); rate limiting on write actions (`src/lib/ratelimit.ts` → "تجاوزت الحد المسموح للعمليات — حاول بعد دقيقة"); idempotency keys table for double-submit safety; `GET /api/health` warm-up route to prevent Supabase idling (scheduler not yet configured — `CLAUDE.md` §14).
- **Offline behavior (global truth):** server-backed, network-first. Service worker caches nothing (comment: "لا توجد قائمة precache؛ النظام network-first بطبيعته" — `public/sw.js`); all GETs bypass cache with `cache:"no-store"`. The ONLY offline artifacts are (a) in-form drafts in localStorage for the unified finance form (`SmartFinanceForm` DRAFT_KEYS `zman_draft_{expense|purchase|asset|receivable}`) and (b) delete-with-undo grace. Everything else fails with error states; old cached query data is shown with an alert bar instead of an error screen (performance round 2, `CLAUDE.md` §14).

---

## 2. Navigation & screen inventory

Nav config: `artifacts/zman-app/src/config/nav.ts`. Desktop sidebar = `navItems` (6). Mobile bottom bar = first 4 (`mainNavItems`). "More" sheet groups (`moreNavGroups`):

| Group | Items (label → href) |
|---|---|
| المتابعة والتحليل | التقارير `/reports` · الملاحظات `/snippets` · الأصول الرأسمالية `/assets` · سجل النشاط `/activities` |
| الإدارة المالية | الأرصدة الافتتاحية `/settings/opening-balance` · الحسابات والصناديق `/finance/accounts` · أصناف الشراء `/finance?manageCatalog=purchases` |
| المراجعة والأمان | سجل التدقيق `/settings/audit-log` |

Routes (all under `src/app/(app)/` route group, shell = `src/components/layout/AppShell.tsx` + `src/app/(app)/layout.tsx`):

| Route | Screen component(s) | Notes |
|---|---|---|
| `/` (dashboard) | `page.tsx` → `features/dashboard/components/DashboardClient.tsx` (+ SmartAlertsBar, FinanceComparePanel, LiquidityFlowPanel, MonthlyProfitPanel, UpcomingDeliveriesCard, FinancialAdvisor, DetailsLayer, GlobalSearch) | date filter (this month / 30d / all); single bundle query `getDashboardBundle` |
| `/orders` | `OrdersClient.tsx` → `features/orders/components/OrderList.tsx`, `OrderCard.tsx`, `OrderForm.tsx` (create/edit modal), `OrderDetail.tsx` (view=?id modal), `StatusFilterSheet.tsx`, `OrderCalendar.tsx`, `WhatsAppTemplateEditor.tsx`, `ComponentsEditor.tsx` | tabs: القائمة / التقويم; status counts; search |
| `/finance` | `FinanceClient.tsx` → `features/finance/components/PaymentsTab.tsx`, `SalesTab.tsx`, `AccountsTab.tsx`+`OwnerTab.tsx` (accounts tab), `SmartFinanceForm.tsx`, `SaleForm.tsx`, `FinanceCatalogModal.tsx`, `ReceivablePaymentModal.tsx` | 2 primary tabs «المدفوعات»/«المبيعات» + hidden tab `accounts` (redirects from legacy `?tab=expenses|purchases|owner|opening`) |
| `/finance/accounts` | `page.tsx` → FinanceClient with tab=accounts | header back-button to /finance |
| `/inventory` | `page.tsx` → `features/inventory/InventoryScreen.tsx` (+ `AddTrackedItemForm.tsx`, `QuickAdjustStockForm.tsx`) | tracked items only |
| `/catalog` | `page.tsx` → `CatalogClient.tsx` (all materials/components, tracked toggle, opening stock, manual adjust modal) | |
| `/reports` | `page.tsx` (large client page) + `features/reports/components/IntegrityCheckReportPanel.tsx` | tabs التقارير/الوضع المالي; period filter all/month/30d; per-section Markdown downloads; «فحص الآن» integrity check |
| `/assets` | `page.tsx` → `features/depreciation/AssetsScreen.tsx` (+ `DepreciationPromptModal.tsx`) | sections: أصول بلا إهلاك / تحت الإهلاك |
| `/activities` | `page.tsx` (recent activities feed, links into each entity) | |
| `/snippets` | `page.tsx` → `SnippetsClient.tsx` | notes library, copy-to-clipboard |
| `/settings/audit-log` | `page.tsx` → `AuditLogClient.tsx` | infinite scroll, entity icons, verb labels |
| `/settings/opening-balance` | `page.tsx` → `OpeningBalanceClient.tsx` (+ `features/finance/components/OpeningTab.tsx`) | lock-once flow |
| `/login` | `src/app/login/page.tsx` + `actions.ts` | passcode |
| `/api/health`, `/api/ping` | route handlers | warm-up/ping |

---

## 3. Data model inventory

All tables are defined in feature `db.ts` files (Drizzle, soft-delete `deleted_at` everywhere except `idempotency_key`, `message_template`, `audit_log`).

**Finance (`src/features/finance/db.ts`):**
- `purchase`: id, date, item (≤200), supplier (≤200, default ""), quantity (>0), unitCostCents (display), unitCostMicroCents (source of truth, millis-fils), totalCents **GENERATED ALWAYS** = round(micro×qty/1000), notes, isCapitalAsset (default false), costNature ∈ {fixed,variable} nullable, linkedCatalogComponentId FK→catalogComponent (RESTRICT), isTrackedInventory (auto-set), timestamps, deletedAt. CHECKs: lengths, quantity>0, classification check.
- `expense`: id, date, category (≤200, required), amountCents (>0), description (≤1000), isCapitalAsset, costNature, isInventoryWriteoff (default false), timestamps, deletedAt. Partial index on write-off rows.
- `sale`: id, date, source ∈ {manual, order} NOT NULL, orderId (unique partial index prevents double-conversion while active), amountCents, description, timestamps, deletedAt.
- `purchase_item_catalog`, `expense_category_catalog`: id, name (≤200), timestamps, deletedAt — managed pick-lists.
- `account`: id, name, type ∈ {cash, bank}, isArchived, timestamps, deletedAt. Unique partial index guarantees one default cash box «الصندوق الرئيسي». **No openingBalanceCents column** (dropped in migration 0011).
- `cash_movement` (the cash ledger): id, date, accountId FK, direction ∈ {in,out}, amountCents (>0), sourceType ∈ {sale, expense, purchase, deposit, owner_draw, owner_inject, opening, transfer, receivable, receivable_payment} (CHECK), sourceId, description, timestamps, deletedAt.
- `owner_transaction`: id, date, type ∈ {draw, inject}, amountCents (>0), accountId, reason, timestamps, deletedAt.
- `opening_balance`: id, goLiveDate, cashCents, bankCents, capitalCents (all ≥0), isLocked, timestamps, deletedAt. No accountId.
- `receivable`: id, date, personName (≤200), amountCents (>0), accountId (RESTRICT), notes, timestamps, deletedAt.
- `receivable_payment`: id, receivableId FK (RESTRICT), date, amountCents (>0), accountId, notes, timestamps, deletedAt.

**Orders (`src/features/orders/db.ts`):**
- `order`: id, customerName, customerPhone (NOT NULL but "" allowed = optional phone), customerPhoneAlt (nullable), productName, quantity, totalCostCents, additionalCostsCents, totalPriceCents, status ∈ {draft, sent, confirmed, delivered, cancelled} default draft, notes, deliveryDate (nullable), receivedDate (default today), depositCents (default 0), depositDate, deliveryPaidCents (documentation-only), additionalProfitCents (added once, not per-unit), timestamps, deletedAt.
- `order_component`: id, orderId FK (cascade), catalogComponentId FK (RESTRICT, nullable = free text), name, costCents, quantity, timestamps.
- `idempotency_key`: requestId PK, action, targetId, createdAt.
- `message_template`: key PK, template (≤5000), updatedAt.

**Catalog (`src/features/catalog/db.ts`):** `catalog_component`: id, name, defaultCostCents (≥0, default 0), unit (default "قطعة"), notes, **tracked** (boolean, default false), timestamps, deletedAt.

**Inventory (`src/features/inventory/db.ts`):** `catalog_movement` (inventory ledger): id, date, catalogComponentId FK (RESTRICT), direction ∈ {in,out}, quantity (>0), sourceType ∈ {purchase, order_delivery, opening, adjustment, manual_in, manual_out} (CHECK), sourceId (sale.id or purchase.id), orderComponentId FK (RESTRICT), unitCostCents (bigint, weighted-average at movement time), totalValueCents (exact integer value of movement), notes, timestamps, deletedAt.

**Depreciation (`src/features/depreciation/db.ts`):** `capital_asset`: id, sourceType ∈ {expense, purchase}, sourceId (no FK — historical link survives source deletion), name, purchaseDate, purchaseAmountCents, usefulLifeMonths (>0), monthlyDepreciationCents = floor(amount/life), startedAt (= purchaseDate), timestamps, deletedAt.

**Audit (`src/features/audit/db.ts`):** `audit_log` (append-only): id, action, entityType, entityId, userId (always "owner"), changesSnapshot jsonb, timestamp. Indexes on timestamp + entity.

**Snippets (`src/features/snippets/db.ts`):** `snippet`: id, title (≤200), body (≤5000), category (≤64, default "عام"), timestamps, deletedAt.

**Migrations (`artifacts/zman-app/drizzle/migrations/`):** 29 files 0000–0028 telling the model's evolution: 0000–0002 core order/expense/purchase/sale tables; 0003 catalog+snippets; 0004 order additional costs; 0005 finance catalogs; 0006 order dates; 0007 message template; 0008 alt phone; 0009 deposit; 0010 idempotent catalog seeding; 0011 drop account.opening_balance_cents; 0012 order delivery + component unit fix; 0013 additional profit; 0014 deposit transform & constraints; 0015 backfill remainder; 0016 high-precision unit cost; 0017 order_component→catalog FK; 0018 cost classification (is_capital_asset/cost_nature); 0019 catalog tracked flag; 0020 catalog_movement ledger; 0021 purchase↔catalog link; 0022 capital assets; 0023 inventory capitalization; 0024 total_value_cents; 0025 is_inventory_writeoff; 0026 audit logs; 0027 receivables; 0028 extra performance indexes.

**Relationships:** order 1—N order_component; order_component N—1 catalog_component (RESTRICT); purchase N—1 catalog_component (RESTRICT); cash_movement N—1 account; receivable 1—N receivable_payment (RESTRICT); catalog_movement N—1 catalog_component + N—1 order_component; sale 1—1 order (while active); capital_asset → (sourceType, sourceId) soft-link to expense/purchase.

`lib/db/src/schema/*` is a legacy minimal schema package (purchases/expenses/sales/orders/catalog_components/snippets) used by the api-server workspace — not used by the deployed app.

---

## 4. Capability catalogue

> 24 capabilities catalogued (ZC-01..ZC-24). Evidence paths are relative to `artifacts/zman-app/` unless a repo root path is given.

### ZC-01 — نموذج الإدخال المالي الموحّد «SmartFinanceForm» (Unified smart finance entry)

- **finding_id:** ZC-01
- **capability_name:** النموذج المالي الموحّد (SmartFinanceForm — one entry form, four modes)
- **zaman_evidence:** `src/features/finance/components/SmartFinanceForm.tsx` (1392 lines); `src/features/finance/hooks.ts`; `PROMPT_UNIFY_FINANCE.md`; `PROMPT_FINANCE_RESTRUCTURE.md`; `CLAUDE.md` §0/§10
- **user_problem:** Owner was "lost in finance — what's the difference between expenses and purchases? I want one interface" (owner quote in PROMPT_UNIFY_FINANCE). Three overlapping forms existed (SmartFinanceForm, dead ExpenseForm, legacy PurchaseForm used only for purchases-create).
- **entry_points:** FAB «تسجيل جديد» in /finance payments tab (label fixed text, not per-tab); edit paths via `?editExpense=`/`?editPurchase=` URL params from PaymentsTab cards; also FAB «مبيعات جديدة» opens the separate SaleForm (sales kept their own form deliberately).
- **screens_and_states:** ResponsiveModal containing: mode selector (4 icon buttons), dynamic explanatory line per mode, mode-specific field set, submit/cancel. Edit mode prefills from a flattened `SmartFinanceFormInitialData` interface. Draft offer banner when a localStorage draft exists (create-only). In-flight lock (double-submit guard `inFlight` ref). Offline toast on `assertOnline()` failure. Error toasts carry the server's Arabic message.
- **fields_inputs:**
  - Mode «مصروف يومي» (expense): date (default today), category (select from `expense_category_catalog` + "أخرى" free text, required ≤200), amount (MoneyInput, fils, required >0), note (optional ≤1000). On save → `createExpense(isCapitalAsset=false, costNature='variable')` — daily expenses are always operating-variable from this mode.
  - Mode «شراء مواد» (purchase): date, catalog picker (optgroup «أصناف المخزون المتتبعة» showing stock balances; optgroup «أصناف المشتريات العامة» from `purchase_item_catalog`; or free text item name), supplier (optional ≤200 — added after a bug silently erased suppliers on edit, PROMPT_UNIFY_FINANCE Phase 0), quantity (int >0, default 1), totalCents (MoneyInput >0 — unit cost is DERIVED: `unitCostMicroCents = round(totalCents×1000/qty)`), notes. Info line at picker: "ℹ️ شراء مباشر غير متتبَّع — سيُخصم المبلغ كاملاً من أرباح هذا الشهر." when untracked; tracked pick shows confirmation that cost deducts at sale.
  - Mode «أصل للورشة» (asset): date, name (placeholder "مثال: ثلاجة العرض، آلة الري..."), amount, description, `wantDepreciation` checkbox → after save opens DepreciationPromptModal (ZC-10). Saves as `createExpense(isCapitalAsset=true, costNature=null)`.
  - Mode «دَين لشخص» (receivable): date, personName, amount, accountId (select of active accounts, default first cash), notes.
  - Each mode shows a one-line profit-impact hint: expense → «يُخصم من ربح هذا الشهر كاملاً.»; purchase → «مادة تدخل منتجاتك. إن ربطتها بصنف متتبَّع، تُخصم تكلفتها عند البيع لا عند الشراء.»; asset → «لا يُخصم من ربح هذا الشهر. يُوزَّع إهلاكاً على عمره النافع.»; receivable → «لا يُخصم من ربحك — مالك ما زال لك، لكن عند غيرك.» (SmartFinanceForm.tsx:858-861).
- **calculations:** unit cost derived from total/quantity in micro-fils precision (guarantees unit×qty=total exactly — migration 0016 rationale).
- **data_effects:** mode→table mapping: expense/asset→`expense` (asset sets isCapitalAsset), purchase→`purchase` (+ optional `catalog_movement` in), receivable→`receivable` (+cash out). Every create also writes an `idempotency_key` row (requestId from `crypto.randomUUID()`), and an `audit_log` row after the transaction commits.
- **financial_effects:** each mode writes its matching `cash_movement` (see ZC-03/06/11/13). Asset mode deliberately does NOT hit profit; receivable mode does not touch profit at all.
- **corrections_reversals:** edit paths preserve original classification (`isCapitalAsset`/`costNature`/`linkedCatalogComponentId` passed through from initialData — the "Edit Trap" fix). Delete handled by parent tab with undo (ZC-03).
- **offline_behavior:** `assertOnline()` blocks submit with toast; per-mode drafts persist to localStorage (`zman_draft_*`) and are offered back on reopen (create-only, not edit).
- **workflow_summary:** Happy: open FAB → pick mode (hint line explains profit impact) → fill → save → toast «تم تسجيل المصروف/شراء المواد/...» → modal closes → list refetches. Edge: offline → toast, draft retained; double-tap submit → in-flight lock + idempotency key; editing a purchase preserves supplier and classification; asset + depreciation → second modal for useful life.
- **transfer_hint:** HIGH — this is Zman's flagship UX pattern: one form, explicit profit-impact wording per mode, derived unit cost, idempotency, drafts. Micro has separate editors per financial event; the "mode + impact hint" pattern transfers directly.
- **confidence:** high
- **open_questions:** none material.

### ZC-02 — تصنيف المصاريف والفئات (Expense categories & classification system) — MANDATORY DEEP AREA

- **finding_id:** ZC-02
- **capability_name:** فئات المصاريف وتصنيفها (Expense categories + two-dimensional classification)
- **zaman_evidence:** `src/features/finance/actions.ts` (createExpense:678, updateExpense:785, deleteExpense:953, seedDefaultExpenseCategories:2560, ensureExpenseCategoryInCatalog:2639, category CRUD 2667–2790); `src/features/finance/queries.ts` (getExpenseCategories:736, getDistinctExpenseCategories:902, getPayments:80); `src/features/finance/components/PaymentsTab.tsx` (filter chips, category dropdown); `src/features/finance/components/FinanceCatalogModal.tsx`; `src/features/finance/db.ts` (expense table + expense_category_catalog); `src/features/finance/schema.ts` (expenseInputSchema); `PROMPT_FIX_CATEGORIES.md`; `PROMPT_FINANCE_TABS_AUDIT.md`
- **user_problem:** Owner asked: "there are ready categories when adding an expense — can I control them, how and from where? Are they best practice?" Diagnosis (PROMPT_FIX_CATEGORIES): two conflicting sources (hardcoded `EXPENSE_CATEGORIES` in the filter vs DB catalog in the form), empty catalog in production, and free-typing producing 4 spelling variants of "owner salary".
- **who/when:** single owner, daily expense entry on phone.
- **entry_points:** category select inside SmartFinanceForm expense mode; «إدارة الفئات» button in PaymentsTab (expense chip active only) and nav-group link `/finance?manageCatalog=purchases` (items catalog); URL params `?category=` (server filter), `?nature=` (hidden — no UI button, known gap م-2).
- **screens_and_states:** FinanceCatalogModal (add/rename/delete category names); PaymentsTab second row: category dropdown «كل الفئات» + manage button; filter chips row (الكل · مصاريف · مشتريات · أصول · ديون); unified payment cards show category + classification badge + date.
- **category model (flat, not hierarchical):** categories are a flat name list. THREE sources unified:
  1. `expense_category_catalog` table (CRUD via FinanceCatalogModal; seed-on-read `seedDefaultExpenseCategories` — idempotent, non-destructive, seeds defaults for a plant workshop: رواتب · إيجار · كهرباء ومياه · نقل وتوصيل · تعبئة وتغليف · صيانة وأدوات · حوافز · أخرى + actually-used categories).
  2. Lazy auto-enrollment: `createExpense` calls `ensureExpenseCategoryInCatalog(trimmedCategory, tx)` — a hand-typed new category is added to the catalog automatically (trimmed; comparison trims whitespace; failure never blocks the expense save; ≤200 chars; no empty-string category).
  3. Orphan merge in the filter: `useExpenseFilterCategories` merges catalog names + `SELECT DISTINCT category FROM expense` so historical categories are always filterable (PROMPT_FIX_CATEGORIES §2 requirement).
- **fields per expense:** required: date (YYYY-MM-DD), category (≤200), amountCents (int >0). Optional: description (≤1000). System-set: isCapitalAsset (false from this mode), costNature ('variable'), isInventoryWriteoff (false — only adjustStock writes true).
- **classification dimensions (the "type" system):** Zman's answer to expense *types* is **not** a per-type enum but two orthogonal dimensions plus special flags, each with distinct accounting semantics:
  - **Capital vs operating** (`is_capital_asset`): capital NEVER enters operating profit; shown as separate balance-sheet line `capitalAdditionsCents`, subtracted from totalEquity to keep IC-1 balanced (INV-18/19). Default false. CHECK constraint on DB.
  - **Cost nature** (`cost_nature` ∈ fixed|variable, nullable): stored and filterable (`?nature=`), NULL allowed for capital rows and legacy rows; NULL ≡ implicitly variable. Default for new operating rows = 'variable' (set by SmartFinanceForm; PurchaseForm/ExpenseForm legacy exposed it; SmartFinanceForm hides it but preserves on edit).
  - **Inventory write-off flag** (`is_inventory_writeoff`): created ONLY by adjustStock out (ZC-07); non-cash loss, separate P&L line, read-only in the payments list (gray card, no ⋯ menu, no edit/delete).
  - **Receivable (دَين)**: NOT an expense at all — asset (ZC-11).
  - **Owner salary**: classified as `owner_transaction` draw, not expense (decision م-10: 7 misclassified rows worth 140.200 JOD await owner decision).
  - **Purchase vs expense**: purchases are materials tied to products (optionally tracked inventory); expenses are everything else. This concept split is exactly what SmartFinanceForm's mode hints teach.
- **how type changes tracking/reporting/period result:** operating expenses reduce `operatingNetCents` in their month (cash-basis); capital expenses do not reduce profit but reduce equity via capitalAdditions; write-offs reduce profit without cash; nature=fixed/variable only affects filtering/analytics (and the hidden `?nature=` filter); category drives the P&L expense distribution donut (`/reports` «توزيع المصاريف حسب الفئة») and list filtering.
- **how the type shows in lists and statements:** PaymentsTab unified card: line 1 name+amount; line 2 category + classification badge + date (expense), supplier+qty×unit + date (purchase), «رأس مال» badge (asset), gray «خسارة مخزون — بلا دفع» (write-off, read-only). P&L & balance sheet lines per ACCOUNTING_RULES.
- **corrections_reversals:** `updateExpense` re-validates (Zod), syncs the linked cash_movement (re-derive pattern), preserves classification passed from the form; write-off rows are guarded from edit/delete ("محروسة من التعديل والحذف" — CLAUDE.md §2/م-5; no reverse-writeoff feature). `deleteExpense` = soft delete + soft-delete of dependent cash_movement + audit log; UI delete has 5s undo. Editing is blocked from the UI for write-off rows (no ⋯ button).
- **data_effects:** expense row + cash_movement(out, expense) + category-catalog auto-add + audit_log; **no** inventory effect.
- **offline_behavior:** online-only; draft in localStorage.
- **workflow_summary:** Happy: FAB → expense mode → pick/typed category (new ones auto-cataloged) → amount → save → appears in «مدفوعاتي» filtered by chip and category, reduces this month's operating profit. Edge: category typed with trailing spaces → trimmed before compare/save (no duplicates); write-off rows visible but immutable; capital rows created via asset mode not expense mode.
- **transfer_hint:** HIGH — flat category catalog + lazy auto-enrollment + orphan-merge filtering + trim normalization solves exactly the free-text chaos Micro will face; the capital/operating × fixed/variable two-dimension classification is a simple model with strong accounting consequences.
- **confidence:** high
- **open_questions:** `?nature=` filter has no UI button and cannot distinguish NULL vs 'variable' (م-2, unresolved upstream); duplicated seeded categories («راتب المالك»/«راتب مالك»/«رواتب») require manual cleanup (م-11); proposed "merge categories" tool deferred.

### ZC-03 — قائمة «مدفوعاتي» الموحّدة (Unified payments list with chips & undo-delete)

- **finding_id:** ZC-03
- **capability_name:** مدفوعاتي (My payments — unified expense/purchase/asset/receivable feed)
- **zaman_evidence:** `src/features/finance/queries.ts:getPayments` (80–505, UNION ALL cursor pagination); `src/features/finance/components/PaymentsTab.tsx`; `src/lib/undo-delete.ts`; `PROMPT_FINANCE_RESTRUCTURE.md`
- **user_problem:** two tabs (مصاريفي/مشترياتي) with overlapping concepts; owner wanted one list ("واجهة واحدة").
- **entry_points:** /finance default tab «المدفوعات» (`?tab=payments`; legacy `?tab=expenses|purchases` redirect with proper filter chip).
- **screens_and_states:** header: 2-tab SegmentedControl + search (debounced 400ms → `?search=`); body: filter chips row; second row (expense chip only): category dropdown + «إدارة الفئات»; infinite scroll (cursor `(createdAt,id)`, `limit+1` nextCursor); skeletons; ErrorState with retry; EmptyState; unified card per kind with ⋯ CardActionSheet (edit/delete/…) — except write-off cards (read-only, gray).
- **fields_inputs (server filters):** `filter` ∈ all/expense/purchase/asset/receivable (chip semantics: الكل = both tables incl. assets+writeoffs; مصاريف = expense excluding capital; مشتريات = purchase excluding capital; أصول = both where isCapitalAsset; ديون = receivables); `search` (category/description for expenses; item/supplier for purchases); `category`; `nature` (hidden).
- **calculations:** none (pure feed).
- **data_effects:** reads only; deletes via mutations soft-delete rows + linked cash_movement + catalog_movement (purchase) + audit.
- **financial_effects:** deleting an expense/purchase reverses its cash movement (profit recomputed automatically since P&L reads live ledger).
- **corrections_reversals:** delete-with-undo: optimistic hide → 5s countdown («سيُحذف المصروف — لا تغلق الصفحة») → onCommit soft-delete; «تراجع» restores; pagehide fires best-effort commit; failure re-shows row + error toast. Edit reopens SmartFinanceForm prefilled.
- **offline_behavior:** network-first; stale cache shown with alert bar (query-provider behavior).
- **workflow_summary:** Happy: scroll unified chronological feed → chip filter → open edit → save. Edge: pagination across UNION ALL boundary — no dupes/missing (tested per prompt); write-off card has no actions; receivable cards open ReceivablePaymentModal.
- **transfer_hint:** HIGH — UNION ALL cursor pagination + kind-specific card second lines + undo-delete pattern are directly reusable for Micro's ledger feeds.
- **confidence:** high
- **open_questions:** none.

### ZC-04 — «مبيعاتي» والمبيعات اليدوية (Sales tab & manual sales)

- **finding_id:** ZC-04
- **capability_name:** المبيعات (Sales — manual sales + order conversions)
- **zaman_evidence:** `src/features/finance/components/SalesTab.tsx`; `src/features/finance/components/SaleForm.tsx`; `src/features/finance/actions.ts` (createSale:1069, updateSale:1175, deleteSale:1343)
- **user_problem:** record cash income that didn't come from a workshop order (walk-in sales).
- **entry_points:** /finance tab «المبيعات»; FAB «مبيعات جديدة»; `?newSale=true`/`?editSale=` URL params; activities page links.
- **fields_inputs:** date, amount (>0), description; source fixed 'manual' from SaleForm; Zod enforces orderId present iff source='order'.
- **data_effects/financial_effects:** sale row + cash_movement(in, sale). INV-4: createSale/updateSale with order source post `max(0, amount − order.deposit)` — never the full price; unique partial index blocks double conversion.
- **corrections_reversals:** updateSale re-derives cash; deleteSale soft-deletes + soft-deletes movements (order returns to re-convertable state per F-32).
- **workflow_summary:** Happy: FAB → amount → save → profit up. Edge: manual sale with source=order must reference an existing non-converted order.
- **transfer_hint:** MEDIUM — direct-sale concept exists in Micro; the deposit-netting rule (INV-4) is the key accounting idea to preserve.
- **confidence:** high
- **open_questions:** none.

### ZC-05 — سير عمل الطلبات (Order lifecycle: draft→sent→confirmed→delivered/cancelled)

- **finding_id:** ZC-05
- **capability_name:** الطلبات (Orders workflow)
- **zaman_evidence:** `src/features/orders/actions.ts` (createOrder:31, updateOrder:204, deleteOrder, updateOrderStatus); `src/features/orders/components/OrderForm.tsx`, `OrderCard.tsx`, `OrderDetail.tsx`, `StatusFilterSheet.tsx`, `OrderCalendar.tsx`, `OrderList.tsx`, `OrdersClient.tsx`; `src/features/orders/db.ts`; FEATURES_PLAN.md (features 3,5,6,7)
- **user_problem:** track customer orders from intake to delivery, with deposit, expected delivery date, and WhatsApp quote messages.
- **entry_points:** /orders (bottom nav); list/calendar tabs; status filter sheet with counts; FAB new order; card tap → detail modal (`?view=<id>`); status dropdown directly on card (Feature 5: `useUpdateOrderStatus` with stopPropagation).
- **screens_and_states:** OrderForm (create/edit): sections customer (name required, phone optional, alt phone optional), product (name, quantity), dates (expected delivery date optional, received date), components editor (ZC-08), additional costs (delivery/installation/fees — order-level not per-unit), delivery-paid + "record as additional profit" checkbox, pricing (agreed price, deposit + deposit date), notes; live summary card: العربون المستلم, صافي الربح (مرجعي/مُقدّر) = price − totalCost + additionalProfit, التوصيل — مرجعي (reference-only, never in profit math); a pre-save warning modal if a tracked component's stock is insufficient (negative balance allowed at delivery, documented). OrderDetail: status transitions via `nextStatuses` map (draft→sent→confirmed→delivered via conversion; any→cancelled), convert/reverse/refund/forfeit actions (ZC-06), WhatsApp send, consumed-stock list after delivery.
- **fields_inputs:** required: customerName, productName, quantity(>0); optional: phones, deliveryDate, deposit(+date), additionalCosts, deliveryPaid, additionalProfit, notes, components.
- **validations:** deposit ≤ price+additionalProfit (action + DB constraint from migration 0014); delivered orders cannot edit components (deducted quantities depend on delivery-time snapshot — error message: «استخدم reverseSale أولاً ثم عدّل ثم أعد التحويل»); delete+re-INSERT of components only if actually changed (D6 fix protecting catalog_movement FK).
- **data_effects:** createOrder inserts order + components + (if deposit>0) cash_movement(in, deposit) linked to order id (INV-3). Status changes are pure status updates EXCEPT delivered which is forced through convertOrderToSale.
- **financial_effects:** deposit enters cash but is deferred (liability) until conversion (ZC-06).
- **corrections_reversals:** updateOrder syncs deposit movement (re-derive; refuses deposit changes that break refund history), syncs sale movement if a converted order's price changed; deleteOrder soft-deletes order + components + deposit movement.
- **offline_behavior:** online-only; assertOnline in forms.
- **workflow_summary:** Happy: new order (draft) → send quote via WhatsApp → confirm → deliver (= convert to sale: revenue booked, remainder collected, stock deducted) → order locked. Edge paths: cancel + forfeit deposit (ZC-06); refund part of deposit (independent out movement); reverse delivery to fix price then re-deliver.
- **transfer_hint:** HIGH — status machine with finance bridge only at delivery, deposit-as-liability, and WhatsApp quote templates are core Micro-relevant patterns (Micro's craft-order domain).
- **confidence:** high
- **open_questions:** deliveryPaidCents is documentation-only by design; profit from delivery margin must be manually moved into additionalProfit (the checkbox automates it).

### ZC-06 — تحويل الطلب لمبيعة والتحويلات العكسية (Order→Sale conversion, deposit transform, reversal, refund, forfeiture)

- **finding_id:** ZC-06
- **capability_name:** تحويل إلى مبيعات (تسجيل إيراد) + عكس التسليم + رد العربون + احتجاز العربون (Convert / reverse / refund / forfeit)
- **zaman_evidence:** `src/features/finance/actions.ts` (convertOrderToSale:1441, reverseSale:1650, refundOrder:1787, forfeitDeposit:2020, reverseDepositForfeiture:2238); `src/features/orders/components/OrderDetail.tsx` (modals + toasts); migrations 0014, 0015; ACCOUNTING_RULES INV-3/4/9
- **user_problem:** book revenue exactly once at delivery, handle deposits without double-counting, and undo any of it cleanly.
- **entry_points:** OrderDetail buttons: «تحويل إلى مبيعات (تسجيل إيراد)» (confirmed status / "توصيل ✓" path), «عكس التسليم», refund modal, forfeit modal (+ reverse forfeiture when a forfeiture sale exists).
- **mechanics (verified):**
  - **convertOrderToSale:** transaction with row lock; guards: order exists, not deleted, price>0, not cancelled, deposit ≤ realized, no active sale for order. Sale row amount = FULL realized (price+additionalProfit); existing deposit cash_movement is **reclassified** (sourceType deposit→sale, sourceId→new sale — "محوَّل من عربون", not a new cash event); remainder movement inserted if >0 (computed from the *collected* deposit movement amount, not order.depositCents, to avoid re-booking refunded parts); `deductForDelivery` runs inside the same transaction BEFORE status→delivered; idempotency key `convert_to_sale`; audit logged.
  - **reverseSale:** reclassify the transformed movement back to deposit; soft-delete the remainder movement; soft-delete the sale; `restoreForReverse` soft-deletes all order_delivery catalog movements (COGS auto-reverses at read time); order → confirmed.
  - **refundOrder:** independent out movement (sourceType deposit, direction out) + reduces order.depositCents (the remaining refundable liability); refuses amount > remaining deposit; requires account + date.
  - **forfeitDeposit:** cancelled order's deposit becomes revenue WITHOUT a new cash movement — creates a sale (source order) via a settlement path and zeroes the deposit liability (no double cash); reversible by `reverseDepositForfeiture` (order → confirmed). IC-16 guards this.
- **fields_inputs:** refund: orderId, date, amount>0 ≤ remaining, accountId, notes; forfeit: orderId, date, notes.
- **data_effects:** sale, cash movements (reclassified/remainder/refund), catalog movements, order status, idempotency keys, audit rows.
- **financial_effects:** revenue = price+additionalProfit recognized at delivery; deposits held as liability until then; refunds reduce cash and liability; forfeiture converts liability to revenue without cash.
- **corrections_reversals:** each action has an explicit inverse (reverseSale / reverseDepositForfeiture); all soft-delete.
- **workflow_summary:** Happy: confirmed order → convert → status delivered, revenue booked, stock deducted, toasts. Edge: re-convert after deleteSale allowed (F-32); conversion of delivered order without active sale allowed; failed deduction rolls back everything (no sale, no status change).
- **transfer_hint:** HIGH — the deposit-transform (reclassify instead of double-post) + full inverse action set is the single most sophisticated financial-workflow pattern in Zman; Micro's craft-order + collect flows need exactly this.
- **confidence:** high
- **open_questions:** none (refund cap = remaining deposit verified in OrderDetail.tsx:136).

### ZC-07 — المخزون الانتقائي ودفتر catalog_movement (Selective inventory tracking) — MANDATORY DEEP AREA

- **finding_id:** ZC-07
- **capability_name:** تتبّع المخزون الانتقائي (Selective per-item inventory tracking + inventory ledger)
- **zaman_evidence:** `src/features/catalog/db.ts` (tracked flag); `src/features/inventory/db.ts` (catalog_movement); `src/features/inventory/actions.ts` (addCatalogMovement, deductForDelivery, restoreForReverse, adjustStock); `src/features/inventory/InventoryScreen.tsx`; `src/app/(app)/catalog/CatalogClient.tsx` (tracked toggle, opening stock, untrack warning); `src/features/inventory/components/AddTrackedItemForm.tsx`, `QuickAdjustStockForm.tsx`; `src/features/inventory/queries.ts`/`hooks.ts`; migrations 0019, 0020, 0021, 0023, 0024; ACCOUNTING_RULES §9 (INV-20/21/23/24), CLAUDE.md §2/§7
- **user_problem:** "profit swings and I never see my real number": (1) capital purchases destroyed the purchase month's profit; (2) no inventory — material purchases deducted immediately, sales didn't deduct anything (owner quote in CLAUDE.md §0).
- **participation model (the core answer):** inventory participation is **per catalog item, owner-chosen, default OFF**:
  - A catalog item is created in /catalog (name, default cost, unit, notes) — `tracked` defaults to false → **deliberately non-stock item**: purchases stay purely operational (deduct profit in purchase month, INV-1 original behavior), NO catalog_movement rows are ever created for it (silent skip in createPurchase and deductForDelivery — whitelist design), sales/orders never touch stock for it.
  - Owner enables tracking any time via a toggle **on the catalog card** («متتبَّع» / «تفعيل التتبع») or in the item form. First-time activation may enter an **opening stock** quantity (`openingStock` field appears only on first activation) → creates `catalog_movement(in, sourceType='opening')`. Entering via catalog costs **0** by design (its cost was already expensed at purchase — documented zero-cost inventory, CLAUDE.md §7).
  - Once tracked: linked purchases create `in` movements (unitCost = floor(total/qty), totalValueCents = purchase total — exact, no fils drift); order delivery creates `out` movements (qty = component quantity × order quantity) with weighted-average COGS stored immutably on the movement; manual adjustments via adjustStock.
  - **Changing the choice later:** untracking an item with stock > 0 requires an explicit confirmation dialog ( «ستفقد التتبّع. الرصيد الحالي N وحدة سيُعامَل كصفر للطلبات الجديدة. سيتم حذف سجل الحركات ناعماً. هل أنت متأكد؟») — account rule INV/SA1 NOTE-3; movements soft-deleted; new orders treat balance as zero. Re-enabling starts fresh with optional opening balance.
- **safeguards preventing accidental effects:**
  - createPurchase REJECTS linking to a non-tracked/missing catalog item («الصنف غير متتبَّع أو غير موجود» — card 3.F) and REJECTS combining isCapitalAsset=true + tracked link (double-counting guard, A-3 fix).
  - Purchases to tracked items are EXCLUDED from operating profit (capitalized as inventory asset; `is_tracked_inventory=true`; cash still leaves — INV-23).
  - Deduction allowed to go NEGATIVE (documented §6 scenario 1) — completion never blocked; warning recorded in movement notes ("⚠️ الرصيد قبل الخصم ... أقل من المطلوب").
  - Deduction happens ONLY inside convertOrderToSale's transaction (atomicity: failure rolls back sale+cash+status).
  - delivered orders cannot have components edited (delivery-time quantity snapshot).
  - FK RESTRICT on order_component and purchase links preserves history; D6 fix avoids orphaning movements.
- **screens:** InventoryScreen: low-stock alert banner («N أصناف نفد رصيدها» + names), stats cards (إجمالي الأصناف / القيمة الدفترية), sort (أبجدي/أقل رصيداً/أعلى قيمة), per-item cards (name, نفد badge, book value, balance+unit), `?filter=low-stock`, FAB «إجراءات المخزون» → AddTrackedItemForm / QuickAdjustStockForm / link to /catalog. Empty state with 3-step onboarding (go to catalog → enable tracking → set qty+price).
- **fields:** AddTrackedItemForm (name, unit, default cost, opening qty); QuickAdjustStockForm (select tracked item showing current balance, direction صرف/إضافة, qty, reason).
- **calculations:** balance = Σin − Σout (read-time, never stored); book value = Σ(in totalValue) − Σ(out totalValue) with coalesce fallback; weighted average = Σ(in qty × coalesce(unit_cost,0)) / Σ(in qty); A4 "last out sweeps residual book value" to avoid 1-fils residuals.
- **financial_effects:** tracked inventory value is a balance-sheet ASSET (`inventoryValueCents` in getFinancialPosition); COGS deducted from operating profit in the SALE month (INV-24); write-off (manual out with value>0) creates a non-cash expense (INV-25). Untracked items: NO financial effects beyond normal purchase/expense accounting.
- **corrections_reversals:** updatePurchase soft-deletes old movement and re-derives new (re-derive pattern); reverseSale soft-deletes delivery movements; NO reverse for manual write-off (م-5 known gap).
- **offline_behavior:** online-only.
- **workflow_summary:** Happy: create catalog item (untracked) → decide to track → toggle + opening qty → purchases linked → inventory screen shows balance/value → deliver order → stock deducted, COGS booked. Edge: negative stock allowed with note; untrack with stock → confirm dialog; purchase linked to untracked item → rejected; opening stock at zero cost (documented trade-off, balance sheet understates until old stock sold out).
- **transfer_hint:** **HIGHEST** — this is the exact "selective inventory + non-tracked items" capability Micro is designing (Micro's inventory-material + craft-order domains). The per-item `tracked` flag + separate movement ledger + capitalized purchases + weighted-average immutable COGS + negative-allowed philosophy + untrack confirmation is a complete, battle-tested design contract.
- **confidence:** high
- **open_questions:** opening stock at zero cost understates book value until legacy stock clears (accepted trade-off; full solution designed but NOT built — CLAUDE.md §7/§8 item 3); component badge in order list doesn't distinguish tracked vs untracked linked items (م-3, minor).

### ZC-08 — محرر مكوّنات الطلب وحساب التكلفة (Order components editor & cost build-up) — MANDATORY DEEP AREA (cost calculation)

- **finding_id:** ZC-08
- **capability_name:** مكوّنات الطلب وتكلفة المنتج (Order components / product cost build-up & pricing)
- **zaman_evidence:** `src/features/orders/components/ComponentsEditor.tsx`; `src/features/orders/components/OrderForm.tsx` (profit summary 246–680); `src/features/catalog/actions.ts`; `src/features/catalog/db.ts` (defaultCostCents, unit); `src/features/inventory/hooks.ts` (useComponentStock); `src/features/orders/db.ts` (order_component)
- **user_problem:** cost a made-to-order product from its materials (with or without catalog), decide price and see expected profit before saving.
- **entry_points:** inside OrderForm (create/edit): «مكوّنات الطلب» section; «إضافة مكوّن» opens catalog picker sheet «اختر من المكوّنات».
- **experience top-to-bottom (the cost calculator Zman actually has):**
  1. Component rows: name (from picker or free text), badge — «مربوط بصنف»+«متتبَّع» with live stock balance (picker item shows badge متتبَّع + current stock; zero-stock shows warning tooltip; NO blocking) or «نص حر · غير متتبَّع»; editable cost (MoneyInput, prefilled from `catalogComponent.defaultCostCents` snapshot); quantity (per-unit repetition, default 1); delete button; «تراجع» undo for just-removed rows.
  2. Catalog picker: debounced search, empty states («المكوّنات فارغة — أضف مكوّنات من صفحة المكوّنات»), tracked badge + stock per item (card 3.K).
  3. Additional costs section: order-level costs (توصيل، تركيب، رسوم) — «تكاليف تُدفع على الطلب بالكامل وليست مكوّناً».
  4. Delivery & extras: deliveryPaidCents (reference only) + checkbox «هل أدخله كإيراد وأرباح إضافية للمشروع عند التسليم؟» → copies value into additionalProfitCents.
  5. Pricing: agreed price (required for conversion), deposit + date.
  6. **Live calculations:** total cost = Σ(component cost × quantity)×order qty + additionalCosts; صافي الربح (مرجعي/مُقدّر) = totalPrice − totalCost + additionalProfit; التوصيل — مرجعي excluded by design; العربون المستلم shown. All labeled «متوقّع/تقديري» with neutral color (INV-8 — expected numbers never styled as actual).
- **inputs:** known values = component cost, qty, additional costs, price, deposit; **unknown/incomplete inputs**: cost may be 0 (allowed, ≥0), price 0 blocks conversion (not saving), stock below required triggers a pre-save warning modal («سيُسمح بحفظ الطلب، وقد يظهر رصيد سالب عند التسليم...») but never blocks.
- **saved estimates & reuse:** order_component rows persist name+cost snapshots (catalog link kept via catalogComponentId; snapshot survives catalog deletion — RESTRICT FK + snapshot design). Duplicating an order = manual re-entry (no duplicate-order feature found — INFERENCE from absence in orders actions/components).
- **relationship to product/sale:** cost estimates are order-scoped only (no product catalog pricing engine); realized revenue at delivery = price+additionalProfit; COGS comes from tracked inventory, not from the estimate (estimate is informational).
- **does any action create financial/inventory events?** saving the order: NO revenue, NO inventory movement (only deposit cash if entered); delivery conversion: revenue + stock deduction for tracked linked components.
- **data_effects:** order + order_component rows; nothing else.
- **financial_effects:** none at save (except deposit); estimates displayed as expected everywhere (dashboard «الربح المتوقّع بعد تسليم طلباتك», orders list expected profit).
- **corrections_reversals:** edit components blocked after delivery; delete component rows with undo within form; catalog item deletion RESTRICTed if referenced.
- **offline_behavior:** online-only.
- **workflow_summary:** Happy: pick components (cost prefills) → adjust qty/cost → add order-level costs → set price/deposit → save draft → WhatsApp quote → deliver. Edge: free-text components (no link, no stock effect); insufficient stock → warning only; cost=0 allowed (COGS then 0 for untracked).
- **transfer_hint:** HIGH — Micro has a full CostCalculator/Estimates domain; Zman's transferable elements: cost snapshotting vs live link distinction, per-unit vs per-order cost split, expected-vs-realized labeling discipline, pre-delivery stock warning, "delivery profit" checkbox pattern.
- **confidence:** high
- **open_questions:** no order duplication feature (INFERENCE — absence of evidence in orders/actions.ts); no margin/percentage pricing (price is entered, not derived — margin math is manual).

### ZC-09 — الربح التشغيلي الموحّد (LOCKED-6 single profit definition)

- **finding_id:** ZC-09
- **capability_name:** الربح التشغيلي — computeOperatingPnl (Single source of truth for profit)
- **zaman_evidence:** `src/features/finance/pnl.ts` (full file); `CLAUDE.md` §2 (LOCKED-6); ACCOUNTING_RULES INV-19a; `src/features/finance/integrityCheck.ts` (IC-13); `src/features/dashboard/queries.ts`; `src/features/reports/actions.ts:computeCashBasisPnl`
- **user_problem:** "my profit swings and I've never seen my real number" — multiple inline profit definitions previously disagreed across dashboard/reports/monthly.
- **mechanics:** `computeOperatingPnl({startDate?, endDate, tx})` is the ONLY profit definition; 6 parallel queries (sales in, expenses operating/capital, purchases operating/capital/tracked, depreciation for period, COGS, write-offs):
  `operatingNetCents = salesCents − operatingExpensesCents − operatingPurchasesCents − cogsCents − inventoryWriteOffCents − monthlyDepreciationCents`
  All three display entry points (dashboard.summary.netProfit, reports.pnl.netCents, dashboard.monthlyProfit[last].netProfitCents) call it; IC-13 enforces equality at runtime for two periods (current month + all-time) and FAILs on any drift.
- **two declared profit numbers (D3 rule):** «الربح التشغيلي (بعد الإهلاك)» (this function) vs «الربح النقدي المحتجز (قبل الإهلاك)» (balance sheet retainedProfitCents); the difference = period depreciation, displayed as its own dashboard card «إهلاك الفترة (غير نقدي)». Adding a third profit number is forbidden by the naming rule (D3 fix).
- **transfer_hint:** HIGHEST — a single compute function + runtime cross-check is the architecture Micro needs to avoid its own "two numbers" traps.
- **confidence:** high
- **open_questions:** none.

### ZC-10 — الأصول الرأسمالية والإهلاك (Capital assets & computed depreciation)

- **finding_id:** ZC-10
- **capability_name:** الأصول الرأسمالية والإهلاك الشهري المحسوب (Capital assets, read-time depreciation)
- **zaman_evidence:** `src/features/depreciation/db.ts`; `src/features/depreciation/actions.ts` (addCapitalAsset:59, deleteCapitalAsset:211, updateCapitalAsset:282); `src/features/depreciation/queries.ts` (getDepreciationForPeriodCents:83, getCapitalAssetValuation:160); `src/features/depreciation/assetsQueries.ts` (getUndepreciatedCapitalAssets:104); `src/features/depreciation/AssetsScreen.tsx`; `src/features/depreciation/components/DepreciationPromptModal.tsx`; migrations 0022, 0025; ACCOUNTING_RULES §10 (INV-22, IC-14)
- **user_problem:** a machine purchase shouldn't crater one month's profit; the owner wants "asset cost" matched over useful life.
- **entry_points:** asset mode in SmartFinanceForm → wantDepreciation → DepreciationPromptModal (useful life months); /assets screen (More menu); PaymentsTab ⋯ on asset cards (stop depreciation); AssetsScreen action sheet (تعديل / إيقاف الإهلاك).
- **mechanics:** `capital_asset` row per (sourceType, sourceId) — idempotent (existing row returned); validations: life 1–600 months, purchaseDate not future, amount integer ≥0; `monthlyDepreciationCents = floor(amount/life)`; `startedAt = purchaseDate` (retroactive for late entry, A-2 fix); depreciation counted from month AFTER start; stops at life months with "last month sweeps the remainder" (D13); months_elapsed uses `EXTRACT(YEAR)*12+EXTRACT(MONTH)` (never `date_part`, CRITICAL-NOTE-4); **no cash_movement ever** (non-cash); P&L deducts period depreciation (period-scaled, D2 fix); balance sheet stays pure cash-basis (retained profit excludes depreciation — intentional split); /assets shows two sections: «أصول بلا إهلاك» (capital rows without capital_asset — previously invisible, fixed by PROMPT_FINANCE_RESTRUCTURE Phase 1) and «تحت الإهلاك» (original value, depreciated to date, NBV, monthly amount).
- **corrections:** updateCapitalAsset (edit name/date/life — re-derives future depreciation); deleteCapitalAsset (stop depreciation — soft delete; the underlying expense/purchase row and cash movement remain); م-4 gap fixed by updateCapitalAsset (now exists — hooks `useUpdateCapitalAsset`, AssetsScreen «تعديل بيانات الأصل»).
- **transfer_hint:** HIGH — read-time computed depreciation with immutable monthly amount, sweep rule, and period scaling avoids COGS-style scheduled jobs entirely; Micro's financial-event domain can adopt this "computed at read" pattern.
- **confidence:** high
- **open_questions:** none material.

### ZC-11 — الذمم المدينة (Receivables — cash loans to people)

- **finding_id:** ZC-11
- **capability_name:** الذمم المدينة / الديون النقدية (Receivables: loans + free-amount payments)
- **zaman_evidence:** `src/features/finance/db.ts` (receivable, receivablePayment); `src/features/finance/actions.ts` (createReceivable:3710, deleteReceivable:3812, createReceivablePayment:3914, deleteReceivablePayment:4052); `src/features/finance/components/PaymentsTab.tsx` (ديون chip, cards); `src/features/finance/components/ReceivablePaymentModal.tsx`; `PROMPT_RECEIVABLES.md`; migration 0027; ACCOUNTING_RULES CLAUDE §2 (IC-15)
- **user_problem:** owner lends people cash; it must NOT be an expense ("هذول مستردّات") — he needs who/how much/when and remaining cash visibility.
- **mechanics:** loan = cash_movement(out, sourceType='receivable') + receivable row; payment = cash_movement(in, 'receivable_payment') + receivable_payment row; remaining = read-time `amount − Σpayments` (never stored); status قائم/مسدَّد derived; settled loans stay visible (owner constraint #4); payment exceeding remaining is rejected in-action; never enters computeOperatingPnl (separate tables); balance sheet asset (`receivablesCents` = Σ remaining); IC-15 reconciles ledger vs tables.
- **entry_points:** SmartFinanceForm mode «دَين لشخص» (hint: «لا يُخصم من ربحك — مالك ما زال لك، لكن عند غيرك.»); PaymentsTab chip «ديون»; «تسجيل دفعة» button on open loans → ReceivablePaymentModal (free amount ≤ remaining, date, account).
- **transfer_hint:** MEDIUM-HIGH — Micro has parties/collect flows; the "asset not expense" equation and read-time remaining balance are the key ideas.
- **confidence:** high
- **open_questions:** none.

### ZC-12 — الحسابات والصناديق والتحويلات (Accounts/wallets, transfers, owner draw/inject)

- **finding_id:** ZC-12
- **capability_name:** الحسابات والصناديق + سحب/حقن المالك + التحويلات (Cash boxes, bank accounts, owner transactions, transfers)
- **zaman_evidence:** `src/features/finance/actions.ts` (getOrCreateDefaultCashAccount:84, account CRUD+archive 2790–3040, getAccountBalances:3041, transferBetweenAccounts:3105, deleteTransfer:3207, owner transactions 3265–3460); `src/features/finance/components/AccountsTab.tsx`, `OwnerTab.tsx`; `CLAUDE.md` §10 (hidden tabs)
- **user_problem:** track cash box vs bank separately; owner personal money in/out must not distort profit; move money between boxes without double counting.
- **mechanics:** accounts typed cash/bank; default cash box auto-created «الصندوق الرئيسي» (unique partial index); transfer = pair of movements (out+in) with same sourceId (INV-2); archive refused with non-zero balance (INV-13, IC-5); balances read-time per account (as-of date support); owner draw/inject = owner_transaction + cash movement (sourceType owner_draw/owner_inject) — never profit; salaries recorded here since آب 2026 (م-10 policy).
- **screens:** /finance hidden `accounts` tab (AccountsTab + OwnerTab stacked, back-button header); opening-balance moved to /settings.
- **transfer_hint:** MEDIUM — Micro has CashWallets + wallet ledger; transfer-pair + archive-guard are the transferable invariants.
- **confidence:** high
- **open_questions:** none.

### ZC-13 — الأرصدة الافتتاحية (Opening balance setup)

- **finding_id:** ZC-13
- **capability_name:** الأرصدة الافتتاحية (Opening balance: cash, bank, capital — lock once)
- **zaman_evidence:** `src/features/finance/actions.ts` (getOpeningBalance:3463, saveOpeningBalance:3476, lockOpeningBalance:3682); `src/app/(app)/settings/opening-balance/OpeningBalanceClient.tsx`; `src/features/finance/components/OpeningTab.tsx`; ACCOUNTING_RULES INV-15
- **user_problem:** start the ledger with real-world starting cash/bank/capital without faking history.
- **mechanics:** single row (goLiveDate, cashCents, bankCents, capitalCents); saving writes opening cash_movements (sourceType 'opening') into cash+bank accounts (ledger is the only truth — no balance column on account, migration 0011); `isLocked` freezes the form (locked state shows read-only summary «هذه الأرقام مقفلة ومؤكدة تاريخياً»); IC-11 reconciles opening movements vs the row.
- **transfer_hint:** MEDIUM — Micro's setup/foundation flow needs the same "seed once, lock, ledger-only" contract.
- **confidence:** high
- **open_questions:** none.

### ZC-14 — لوحة المعلومات (Dashboard bundle)

- **finding_id:** ZC-14
- **capability_name:** الرئيسية (Dashboard: summary, alerts, compare, liquidity, monthly profit, upcoming deliveries, advisor, details layer, global search)
- **zaman_evidence:** `src/features/dashboard/components/*.tsx` (DashboardClient, SmartAlertsBar, FinanceComparePanel, LiquidityFlowPanel, MonthlyProfitPanel, UpcomingDeliveriesCard, FinancialAdvisor, DetailsLayer, GlobalSearch); `src/features/dashboard/queries.ts` (getFinancialSummary:90, getRecentActivities:275, getFinancialTrendData:399, getDashboardStats:488, getCashSummary:589, getAverageMonthlySpend:613, getMonthlyProfit:663, getDashboardBundle:740); PERF_03_BUNDLE.md
- **what the owner sees:** period-filtered (month/30d/all) cards: net profit (operating, after depreciation — LOCKED-6), cash, capital additions; SmartAlertsBar (auto-hiding warnings); FinanceComparePanel bars (مبيعات/تكلفة المبيعات/مصاريف تشغيلية/مشتريات تشغيلية/إهلاك) + operating profit + "صافي الربح بعد سحوبات المالك" + «الربح المتوقّع بعد تسليم طلباتك» (expected, neutral styling) + educational hint "هذا المبلغ لم يُطرَح من ربحك... أضيف لقيمة مخزونك أو أصولك"; LiquidityFlowPanel (cash composition); MonthlyProfitPanel (per-month net, independent of filter, tooltip: "شهر الشراء قد يظهر خسارة وهذا صحيح"); UpcomingDeliveriesCard (auto-hides when empty); FinancialAdvisor; DetailsLayer drill-down (health metrics, capital, profit-vs-liquidity decomposition with InfoTooltips); GlobalSearch (expenses link-outs).
- **performance:** getDashboardBundle = one round-trip (11→1), useDashboardBundle hook; staleTime 5min.
- **transfer_hint:** HIGH — the dual profit labeling + decomposition layer + expected-vs-realized discipline is exactly the financial-education pattern Micro's dashboard needs.
- **confidence:** high
- **open_questions:** FinancialAdvisor specifics not deep-read (low value for transfer).

### ZC-15 — التقارير (Reports: P&L, expense distribution, sales, orders, balance sheet, downloads)

- **finding_id:** ZC-15
- **capability_name:** التقارير والوضع المالي (Reports + financial position)
- **zaman_evidence:** `src/app/(app)/reports/page.tsx`; `src/features/reports/actions.ts` (computeCashBasisPnl:58, downloadReport:90, getAllReportData:457, getFinancialPosition:660)
- **screens:** tabs «التقارير»/«الوضع المالي»; period segmented control (كل الفترات/هذا الشهر/آخر 30 يوم); sections: ملخص الربح والخسارة (P&L), توزيع المصاريف حسب الفئة (donut), sales summary, order status distribution, balance sheet («ما تملك (الأصول)» cash+bank+inventory+receivables; «ما عليك (الالتزامات)» held deposits; equity), advanced reconciliation (1. تسوية توازن الأرباح المدورة), per-section Markdown download buttons (types pnl/expenses/sales/orders/products/balance_sheet → `downloadReport` returns MD text, downloaded as Blob with UTF-8 BOM).
- **getFinancialPosition equation (verified lines 660–880):** totalAssets = cash + bank + inventoryValue + receivables; totalLiabilities = active order deposits (not delivered/cancelled, deposit>0, date ≤ asOf); retainedProfit (cash-basis, excludes depreciation, includes COGS+write-offs to date); totalEquity = opening + injections − drawings + retained − capitalAdditions; `equityDriftCents = assets − liabilities − equity` must be 0.
- **transfer_hint:** HIGH — the balance-sheet composition with held deposits as the ONLY liability is a distinctive single-owner model worth porting; MD report download is a cheap win.
- **confidence:** high
- **open_questions:** none.

### ZC-16 — فحص السلامة المالي (Financial integrity check «فحص الآن»)

- **finding_id:** ZC-16
- **capability_name:** فحص السلامة (Run-time integrity checks IC-1..IC-16)
- **zaman_evidence:** `src/features/finance/integrityCheck.ts` (1608 lines); `src/features/reports/components/IntegrityCheckReportPanel.tsx`; `src/features/finance/actions.ts:runFinancialIntegrityCheckAction:4127`; ACCOUNTING_RULES header (enforcement)
- **mechanics:** read-only report, 16 checks in parallel: IC-1 equity drift (delegates to getFinancialPosition), IC-2 orphan cash movements, IC-3 deposit liability consistency, IC-4 no deposit double-count, IC-5 no archived account with balance, IC-6 P&L reconciles retained+deposits, IC-7 unit consistency, IC-8 source-ledger reconciliation (excludes write-offs), IC-9 sale amount = order realized, IC-10 owner tx matches movement, IC-11 opening balance matches, IC-12 inventory ledger (WARN on negative balances; FAIL on orphaned rows), IC-13 LOCKED-6 sources match (2 periods), IC-14 asset valuation (WARN fully depreciated), IC-15 receivables reconciliation, IC-16 deposit settlement. Overall PASS/WARN/FAIL + Arabic titles/descriptions/suggested fixes.
- **entry_points:** /reports → «فحص الآن» button.
- **transfer_hint:** HIGHEST — a runnable invariant suite is the mechanism that makes "one trusted number" credible; Micro should adopt the concept and the specific invariants.
- **confidence:** high
- **open_questions:** none.

### ZC-17 — الكتالوج (Catalog of materials/components)

- **finding_id:** ZC-17
- **capability_name:** كتالوج المكوّنات (Material catalog: name, default cost, unit, tracked)
- **zaman_evidence:** `src/features/catalog/actions.ts` (create/update/delete/getCatalogComponents); `src/app/(app)/catalog/CatalogClient.tsx`; `src/features/catalog/hooks.ts`
- **mechanics:** searchable list (debounced), create/edit modal (name, defaultCostCents, unit, notes, tracked + opening stock on first enable), tracked toggle on card with untrack confirmation, per-item stock display, movement history per item (labels: رصيد افتتاحي/صرف يدوي/...), delete = hard delete with ConfirmDialog «نعم، حذف نهائي» (catalog only; RESTRICTed if referenced by orders/purchases).
- **transfer_hint:** MEDIUM — Micro has its own catalog; transferable: default cost as prefill snapshot + RESTRICT-on-reference.
- **confidence:** high
- **open_questions:** catalog deletion is hard delete (verified comment in CatalogClient) unlike everything else.

### ZC-18 — شطب المخزون (Inventory write-off / waste)

- **finding_id:** ZC-18
- **capability_name:** هدر/تلف المخزون (Manual stock write-off as non-cash loss)
- **zaman_evidence:** `src/features/inventory/actions.ts:adjustStock` (write-off insert 551–575); ACCOUNTING_RULES INV-25; migration 0025; PaymentsTab gray read-only cards
- **mechanics:** adjustStock(direction='out', value>0) in ONE transaction: catalog_movement(out, weighted-avg cost, totalValue) + expense row (category «هدر/تلف مخزون», isInventoryWriteoff=true, variable, no cash_movement). P&L line inventoryWriteOffCents; balance sheet deducts from retained + inventory (IC-1 stays 0). A4 sweep applies. Guarded from edit/delete; no reverse feature (م-5).
- **transfer_hint:** HIGH — non-cash loss accounting is subtle; Micro's inventory reversal/write-off editors need this exact dual-entry (movement + shadow expense).
- **confidence:** high
- **open_questions:** no reverse-writeoff (documented gap م-5).

### ZC-19 — سجل التدقيق (Audit log)

- **finding_id:** ZC-19
- **capability_name:** سجل التدقيق (Append-only audit trail)
- **zaman_evidence:** `src/features/audit/db.ts`; `src/features/audit/actions.ts:logAction`; `src/features/audit/queries.ts:getAuditLogPage`; `src/app/(app)/settings/audit-log/AuditLogClient.tsx`; migration 0026
- **mechanics:** every create/update/delete/reverse on finance entities logs action+entity+snapshot AFTER the transaction (never inside; never throws — even if table missing); userId hardcoded "owner" (security: cookie contains the passcode — never persisted); UI: infinite list, entity icons, verb labels (إنشاء/تعديل/عكس/حذف), tableMissing EmptyState.
- **transfer_hint:** MEDIUM — defensive logging contract + "don't log secrets" rule.
- **confidence:** high
- **open_questions:** none.

### ZC-20 — الملاحظات (Snippets / notes library)

- **finding_id:** ZC-20
- **capability_name:** الملاحظات (Snippet library with categories + copy)
- **zaman_evidence:** `src/features/snippets/*`; `src/app/(app)/snippets/SnippetsClient.tsx`
- **mechanics:** title/body/category («عام» default), grouped by category, copy-to-clipboard («نسخ»→«✓ نُسخ»), CRUD modals, confirm delete.
- **transfer_hint:** LOW — utility feature.
- **confidence:** high
- **open_questions:** none.

### ZC-21 — رسائل واتساب (WhatsApp quote messages + editable template)

- **finding_id:** ZC-21
- **capability_name:** قالب رسالة واتساب (WhatsApp template with variables)
- **zaman_evidence:** `src/lib/whatsapp.ts` (cleanPhoneNumber/fillTemplate/hasWhatsAppNumber/buildOrderWhatsAppLink); `src/features/orders/components/WhatsAppTemplateEditor.tsx`; `message_template` table; FEATURES_PLAN.md Feature 4
- **mechanics:** template variables {customerName},{productName},{quantity},{totalPrice},{deliveryDate},{notes}; phone normalization to Jordan +962 (07…/00962/7…); fallback to alt phone; button hidden when no valid number; editor modal from orders toolbar.
- **transfer_hint:** MEDIUM — customer messaging around quotes/orders transfers well to Micro's agreement/quote flows.
- **confidence:** high
- **open_questions:** none.

### ZC-22 — المصادقة والقفل (Passcode auth + idle lock + PWA install)

- **finding_id:** ZC-22
- **capability_name:** تسجيل الدخول والقفل (Login, session, idle lock, PWA)
- **zaman_evidence:** `src/app/login/page.tsx` + `actions.ts`; `src/middleware.ts`; `src/components/auth/IdleLock.tsx`; `src/components/pwa/InstallButton.tsx`, `InstallFab.tsx`, `ServiceWorkerRegister.tsx`; `public/sw.js`; `src/app/manifest.ts`
- **mechanics:** single passcode env var; 8h cookie; fail-closed middleware; 10-min idle lock via visibilitychange (works in installed PWA); SW network-first with safe update prompt (SKIP_WAITING); install prompts.
- **transfer_hint:** MEDIUM — idle-lock and fail-closed patterns.
- **confidence:** high
- **open_questions:** none.

### ZC-23 — النسخ الاحتياطي والتصدير (JSON backup export)

- **finding_id:** ZC-23
- **capability_name:** تصدير نسخة احتياطية (Client-side JSON backup)
- **zaman_evidence:** `src/components/shared/BackupModal.tsx`
- **mechanics:** downloads `zman-backup-YYYY-MM-DD.json` containing accounts (incl. archived), catalog, openingBalance, capitalAssets, recent orders (limit 100) + summary counts. **No import/restore path exists** — export only (verified: no import code in app).
- **transfer_hint:** MEDIUM — partial-export honesty (summary counts) is a nice touch; Micro needs full export/import (a Zman gap to avoid copying).
- **confidence:** high
- **open_questions:** none.

### ZC-24 — أنماط تفاعل وحِرَفيات عامة (Cross-cutting UX craft)

- **finding_id:** ZC-24
- **capability_name:** أنماط مشتركة (Shared interaction patterns)
- **zaman_evidence:** `src/components/shared/*` (Button, MoneyInput with Arabic-numeral parsing, Select, SegmentedControl, FilterChip, CardActionSheet, ConfirmDialog, ResponsiveModal, EmptyState with steps, ErrorState, SkeletonList, InfoTooltip, FloatingActionButton, PageToolbar, BackupModal); `src/lib/undo-delete.ts`; `src/lib/ratelimit.ts`; `src/lib/online.ts`; `src/lib/money.ts` (parseJodToFils converts Eastern Arabic numerals ٠-٩, strips د.أ/JOD); docs/DESIGN_SYSTEM_V2_1_CONTRACT.md, HEADER_AND_HOME_V2_2_CONTRACT.md, HEADER_CONCEPT_V2_3_CONTRACT.md; PROMPT_FIX_TOOLBAR_STABILITY.md, PROMPT_CONSULT_BUTTONS_SYSTEM.md
- **craft rules:** header holds only tabs+search (no conditional filters — anti-jitter rule), filters live in body chips, flex-wrap not horizontal scroll, ≥44px touch targets, logical RTL properties only, fixed FAB label per tab, 5s undo-delete, optimistic-hidden rows, rate-limited writes with Arabic error messages, empty states with onboarding steps.
- **transfer_hint:** HIGH — these are battle-tested mobile-first RTL contracts Micro can adopt wholesale (Micro is also Arabic RTL mobile-first).
- **confidence:** high
- **open_questions:** none.

---

## 5. Financial rules (ACCOUNTING_RULES.md + implementation)

**Constitution:** `artifacts/zman-app/docs/ACCOUNTING_RULES.md` (read in full). Binding for any change to finance/orders/reports/dashboard/migrations; most rules enforced at runtime by `runFinancialIntegrityCheck` (IC-1..IC-16) via the «فحص الآن» button on /reports.

1. **Cash basis core (§0):** `cash_movement` is the single source of truth for cash (INV-1). Never convert to accrual. Deposits are liabilities; equity = opening + injections − drawings + retained profit.
2. **Ledger invariants (§1):** every cash event ↔ exactly one movement (INV-1); transfers = out+in pair with same sourceId (INV-2); deposit posts one `deposit` movement at order creation (INV-3); conversion books remainder only (INV-4); **soft-delete is the only delete** (INV-5); every aggregate filters `deleted_at IS NULL` (INV-6).
3. **Orders vs finance separation (§2):** order numbers are "متوقّع" (expected) — never summed into financial totals; only deposit bridges into finance; P&L revenue derives from cash movements, not sale rows (INV-10).
4. **Reconciliation (§3):** equity-from-ledger must equal equity-from-components (`equityDriftCents = 0`, INV-11); cash-basis net P&L = retained + deposits liability (INV-12).
5. **Money unit (§5):** integer fils; display ÷1000 (JOD, 3 decimals); one formatter `formatFilsToJod`; `*Cents` naming is historical; purchases store micro-fils precision and a GENERATED total.
6. **Two-dimension classification (§8, INV-18/19/19a):** every expense/purchase row classified capital? + nature(fixed/variable), defaults operating-variable; capital excluded from operating profit, shown separately, subtracted from equity; CHECK constraints; LOCKED-6 single profit via computeOperatingPnl.
7. **Selective inventory (§9, INV-20/21/23/24):** `catalog_movement` fully separate from cash ledger; untracked items create NO movements; tracked purchases capitalized as inventory (excluded from operating purchases), COGS deducted at sale via immutable weighted-average on the out movement; negative stock allowed with note; deduction only inside convertOrderToSale transaction; restore via soft-delete on reverseSale; IC-12 PASS/WARN/FAIL.
8. **Write-off (INV-25):** manual stock loss = non-cash expense row (is_inventory_writeoff), no cash movement, separate P&L line, keeps IC-1 balanced.
9. **Depreciation (§10, INV-22):** read-time computed, non-cash, monthly from month after start, correct months_elapsed formula, floor + sweep, never in balance sheet, explicit user opt-in (never automatic on capital save).
10. **Receivables (CLAUDE.md §2, IC-15):** asset not expense; never in P&L; balance-sheet asset; ledger reconciliation.
11. **Correction philosophy:** nothing is ever hard-deleted (except catalog items and idempotency keys); corrections = re-derive patterns (updatePurchase/updateSale re-derive dependent movements), reclassify-not-double-post (deposit transform), and explicit reverse actions (reverseSale, reverseDepositForfeiture). Historical data is protected by cut-over policy (§7 of CLAUDE.md): don't rewrite old months; only capital assets deserve retro-correction.
12. **Operations notes (§11.1):** migrations can't build from scratch (push --force is the bootstrap path); writes are rate-limited and idempotent; audit logs outside transactions and never fail the caller.
13. **Known unresolved items (CLAUDE.md §5/§15):** م-1 write-off verification query join, م-2 no "unclassified" UI filter, م-3 component badge doesn't show tracked state, م-5 no write-off reversal, م-10 7 misclassified owner-salary rows (140.200 JOD) awaiting owner decision, م-11 duplicate seeded categories.
14. **Verified production numbers (CLAUDE.md §0):** net profit 1,045,100 fils; cash 1,260,100; equityDriftCents 0; 14 PASS / 1 WARN (IC-12 negative stock) / 0 FAIL — the system's health is actively monitored.

---

## 6. Capabilities most relevant for Micro transfer (ranked shortlist)

| # | Capability | One-line rationale |
|---|---|---|
| 1 | ZC-07 Selective inventory + catalog_movement ledger | Exactly Micro's inventory-material design problem: per-item opt-in, capitalized purchases, immutable weighted-average COGS, untrack confirmations, negative-tolerant philosophy. |
| 2 | ZC-09 LOCKED-6 single profit function + IC-13 | One computeOperatingPnl + runtime cross-check = the architecture that guarantees "one trusted number" across all Micro screens. |
| 3 | ZC-16 Integrity check suite (IC-1..IC-16) | Copyable invariant catalog with Arabic titles/fix suggestions; makes financial correctness observable by a non-accountant owner. |
| 4 | ZC-06 Order→sale conversion + deposit transform + reversals | The most complete money-movement lifecycle (book-once, reclassify deposits, full inverses) for Micro's craft-order/collect flows. |
| 5 | ZC-01 SmartFinanceForm multi-mode entry with profit-impact hints | One form, four modes, explicit "what this does to your profit" wording — resolves Micro's many-editor confusion the same way it did Zman's. |
| 6 | ZC-02 Category catalog + lazy auto-enrollment + orphan merge | Solves free-text category chaos (Micro will face it day one) with trim normalization and never-block-the-save semantics. |
| 7 | ZC-08 Order components cost build-up + expected/realized labeling | Cost snapshot vs live link, per-unit vs per-order costs, stock warnings, "متوقّع" labeling discipline for Micro's estimates. |
| 8 | ZC-10 Read-time computed depreciation | Zero-scheduled-job asset cost spreading with sweep rule — portable to any capital purchase handling in Micro. |
| 9 | ZC-18 Non-cash inventory write-off | Dual-entry (movement + shadow expense, no cash) keeps the balance equation intact — subtle and battle-tested. |
| 10 | ZC-14/ZC-15 Dashboard + balance sheet with dual profit labels | Profit-after-depreciation vs cash-retained split with decomposition layer; held deposits as the only liability model. |
| 11 | ZC-24 Mobile RTL UX contracts (header rules, undo-delete, MoneyInput) | Battle-tested 360px Arabic-first interaction system Micro can adopt wholesale. |
| 12 | ZC-03 Unified payments feed (UNION ALL cursor pagination + kind cards) | Feed architecture + delete-with-undo for all of Micro's ledger screens. |

---

## 7. Evidence index (file path → capability)

All paths under `artifacts/zman-app/` unless prefixed `repos-root`.

| Path | Capability |
|---|---|
| `src/config/nav.ts` | navigation inventory (§2) |
| `src/app/(app)/finance/FinanceClient.tsx` | ZC-01, ZC-03, ZC-04, ZC-12 |
| `src/features/finance/components/SmartFinanceForm.tsx` | ZC-01, ZC-02, ZC-07 (picker), ZC-10, ZC-11 |
| `src/features/finance/components/PaymentsTab.tsx` | ZC-02, ZC-03, ZC-11, ZC-18 |
| `src/features/finance/components/SalesTab.tsx`, `SaleForm.tsx` | ZC-04 |
| `src/features/finance/components/AccountsTab.tsx`, `OwnerTab.tsx`, `OpeningTab.tsx` | ZC-12, ZC-13 |
| `src/features/finance/components/ReceivablePaymentModal.tsx` | ZC-11 |
| `src/features/finance/components/FinanceCatalogModal.tsx` | ZC-02 |
| `src/features/finance/db.ts` | data model (§3), ZC-02, ZC-11, ZC-12, ZC-13 |
| `src/features/finance/schema.ts` | ZC-01, ZC-02, ZC-04, ZC-06, ZC-11 input validation |
| `src/features/finance/actions.ts` | ZC-02, ZC-03, ZC-04, ZC-06, ZC-11, ZC-12, ZC-13, ZC-16 |
| `src/features/finance/queries.ts` | ZC-02, ZC-03, ZC-04, ZC-11 |
| `src/features/finance/pnl.ts` | ZC-09 |
| `src/features/finance/integrityCheck.ts` | ZC-16 (§5) |
| `src/features/inventory/db.ts` | ZC-07 (§3) |
| `src/features/inventory/actions.ts` | ZC-06 (deduct/restore), ZC-07, ZC-18 |
| `src/features/inventory/InventoryScreen.tsx` + `components/*` | ZC-07 |
| `src/app/(app)/catalog/CatalogClient.tsx` | ZC-07, ZC-17 |
| `src/features/catalog/db.ts`, `actions.ts`, `hooks.ts` | ZC-07, ZC-17 |
| `src/features/orders/db.ts` | ZC-05, ZC-08 (§3) |
| `src/features/orders/actions.ts` | ZC-05, ZC-06 (deposit posting) |
| `src/features/orders/components/OrderForm.tsx`, `ComponentsEditor.tsx` | ZC-05, ZC-08 |
| `src/features/orders/components/OrderDetail.tsx` | ZC-05, ZC-06, ZC-21 |
| `src/features/orders/components/OrderCard.tsx`, `OrderList.tsx`, `StatusFilterSheet.tsx`, `OrderCalendar.tsx`, `OrdersClient.tsx` | ZC-05 |
| `src/features/orders/components/WhatsAppTemplateEditor.tsx` + `src/lib/whatsapp.ts` | ZC-21 |
| `src/features/depreciation/*` (db, actions, queries, assetsQueries, AssetsScreen, DepreciationPromptModal) | ZC-10 |
| `src/features/audit/*` + `src/app/(app)/settings/audit-log/AuditLogClient.tsx` | ZC-19 |
| `src/features/snippets/*` + `src/app/(app)/snippets/SnippetsClient.tsx` | ZC-20 |
| `src/features/dashboard/*` | ZC-14 |
| `src/app/(app)/reports/page.tsx` + `src/features/reports/actions.ts`, `components/IntegrityCheckReportPanel.tsx` | ZC-15, ZC-16 |
| `src/app/(app)/activities/page.tsx` | activities screen (§2) |
| `src/app/(app)/settings/opening-balance/*` | ZC-13 |
| `src/app/login/*`, `src/middleware.ts`, `src/components/auth/IdleLock.tsx`, `src/components/pwa/*`, `public/sw.js`, `src/app/manifest.ts` | ZC-22 |
| `src/components/shared/BackupModal.tsx` | ZC-23 |
| `src/components/shared/*`, `src/lib/undo-delete.ts`, `src/lib/online.ts`, `src/lib/money.ts`, `src/lib/ratelimit.ts`, `src/lib/utils.ts` | ZC-24 (+ global behaviors §1) |
| `src/lib/db/client.ts`, `src/lib/db/errors.ts` | §1 data layer |
| `drizzle/migrations/0000–0028` | §3 model evolution |
| `repos-root:CLAUDE.md` | §1, §5, known issues, ops policy |
| `artifacts/zman-app/docs/ACCOUNTING_RULES.md` | §5 (read fully) |
| `repos-root:PROMPT_UNIFY_FINANCE.md`, `PROMPT_FINANCE_RESTRUCTURE.md`, `PROMPT_FIX_CATEGORIES.md`, `PROMPT_RECEIVABLES.md`, `PROMPT_FINANCE_TABS_AUDIT.md`, `PROMPT_CONSULT_FINANCE_UX.md`, `PROMPT_CONSULT_BUTTONS_SYSTEM.md`, `PROMPT_FIX_TOOLBAR_STABILITY.md` | intent & history for ZC-01/02/03/11/24 |
| `artifacts/zman-app/FEATURES_PLAN.md`, `docs/DESIGN_SYSTEM_V2_1_CONTRACT.md`, `docs/HEADER_*_CONTRACT.md` | ZC-05 (features 3–7), ZC-24 |
| `artifacts/api-server/src/**`, `lib/api-spec/openapi.yaml`, `lib/api-client-react/**`, `lib/api-zod/**`, `lib/db/src/schema/**` | §1 parallel artifacts (NOT used by deployed app) |
| `artifacts/mockup-sandbox/src/App.tsx` | §1 design sandbox (gallery + preview routes; no hidden product screens found) |

---

*End of SA-1 report. Built entirely from read-only inspection of zman-app @ bdd63ab.*
