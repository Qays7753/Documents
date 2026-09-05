# SA-1 — Zman Capability Archaeology (Complete Code-Verified Capability Catalogue)

- **Task ID:** 4-a / SA-1 "Zman Capability Archaeologist" (Group 6, Agent 2 — Zman→Micro transfer audit)
- **Date:** 2026-09-05
- **Zman revision analyzed:** `bdd63abb861d6ef41f5c151ddf0d68df158df225` (merge of PR #39 `feat/orders-dashboard-mobile-redesign-v24`, 2026-08-21) — verified via `git rev-parse HEAD` in `/home/z/my-project/repos/zman-app`.
- **READ-ONLY STATEMENT:** The Zman repository was **not modified in any way** during this task. Only two files were written by this agent, both outside the repo: this report (`/home/z/my-project/specialists/01-zman-capability-archaeology.md`) and an append to `/home/z/my-project/worklog.md`.
- **Methodology:** Every capability record below was rebuilt **from code only** (Grep/ripgrep + Read of `artifacts/zman-app/src/**`, `drizzle/migrations/**`, root docs). Prior reports (including the 2026-09-03 capability map) were read **after** primary code inspection and used only as a comparison baseline (§6). Every claim carries a `file:line` citation. Money is integer fils (1 JOD = 1000 fils), the only formatter being `formatFilsToJod` (`src/lib/money.ts:15-20`). Arabic labels are quoted verbatim from the UI code.
- **Corrections to the task brief, verified by enumeration:** the Drizzle migration chain contains **29 migration files** (`drizzle/migrations/0000…0028`, confirmed by `git ls-files | grep '\.sql$'` and `meta/_journal.json` = 29 entries), not 44. Two additional SQL files exist outside the chain: `src/lib/db/triggers.sql` (unreferenced by any code — see ZC-30) and a repo-root ops script `FIX_DELIVERED_ORDERS_WITHOUT_SALES.sql`.

---

## 0. Executive verdict

| Metric | Count |
|---|---|
| Prior-map capabilities re-verified from code (ZC-01…ZC-24) | 24 |
| — CONFIRMED exactly as described | 21 |
| — CONFIRMED-WITH-DIFFERENCES (see §6 for the deltas) | 3 (ZC-06, ZC-17, ZC-01 minor comment drift) |
| — NOT-FOUND-AS-DESCRIBED | 0 |
| New discoveries (ZC-25…ZC-30) | 6 (4 capability promotions + 2 code-artifact findings) |
| **Audit-brief question: "project relationship & shared expense allocation"** | **DOES NOT EXIST in Zman — code-verified negative (§1)** |

Status vocabulary: `CONFIRMED` = code matches the prior map; `CONFIRMED-WITH-DIFFERENCES` = capability exists but a documented detail differs; `NEW-DISCOVERY` = not catalogued as a standalone record before.

---

## 1. Special investigation — does Zman have "project relationship and shared expense allocation by amount/percentage/estimate/deferment"?

**Code-verified answer: NO. Zman has no project entity and no shared-expense allocation capability of any kind.**

Evidence (exhaustive searches over `artifacts/zman-app/src/**` and `drizzle/migrations/**`):

1. **No project table/column/field.** The complete data model is 16 tables: `purchase, expense, sale, purchase_item_catalog, expense_category_catalog, account, cash_movement, owner_transaction, opening_balance, receivable, receivable_payment` (`src/features/finance/db.ts:22–488`), `order, order_component, idempotency_key, message_template` (`src/features/orders/db.ts:14–156`), `catalog_component` (`src/features/catalog/db.ts:4–31`), `catalog_movement` (`src/features/inventory/db.ts:37–100`), `capital_asset` (`src/features/depreciation/db.ts:54–102`), `snippet` (`src/features/snippets/db.ts:4–21`), `audit_log` (`src/features/audit/db.ts:18–33`). None has a `project_id` or allocation fields; no migration (0000–0028) creates any project/allocation structure (`rg -i "project|allocat|share|split" drizzle/migrations` → 0 matches).
2. **All 27 occurrences of `project|مشروع` in `src/**` are generic copy** meaning "the (whole) business" — e.g. "صافي ما يملكه المشروع" (`src/app/(app)/reports/page.tsx:745,751`), "الأرصدة الافتتاحية للمشروع" (`src/features/finance/db.ts:385`), "بداية المشروع" empty-state text (`src/features/dashboard/components/FinancialAdvisor.tsx:46–48`). None is an entity, link, or filter.
3. **All 16 occurrences of `allocation|allocate|توزيع` are one of three unrelated concepts:**
   - **Monthly depreciation spread** of a *single* asset's cost over its life — "توزيع شهري (إهلاك)" (`src/features/depreciation/components/DepreciationPromptModal.tsx:17,150,176`; `src/features/depreciation/actions.ts:22`). Temporal spreading, not cross-entity sharing.
   - **Read-only analytics distribution charts**: "توزيع المصاريف حسب الفئة" donut and "توزيع الطلبات حسب الحالة" (`src/app/(app)/reports/page.tsx:388,404,520`) — percentages *of totals* in report tables (`src/features/reports/actions.ts:250,308,358`), not allocation inputs.
   - UI copy for the FinanceComparePanel bar proportions ("طول الشريط = نسبة من أكبر قيمة", `FinanceComparePanel.tsx:117`).
4. **No allocation UI.** No input anywhere accepts an allocation percentage/amount *between* two or more cost objects. `rg -i "مشترك|شارك"` in `src/**` matches only "shared React components" and "shared filters" (`src/components/layout/AppShell.tsx:294`, `src/features/orders/components/OrderList.tsx:34`, `dashboard/queries.ts:731`). `تقدير/تقديري` matches are *expected/estimated order values* ("أرقام تقديرية — لا تُمثّل نقداً مُحصَّلاً", `reports/page.tsx:513`; estimated profit in `OrderDetail.tsx:261`) — estimation of a single order's numbers, never allocation-by-estimate. `deferment|مؤجّل` matches are held deposits ("عربونات مؤجلة", `reports/actions.ts:139`) and the PWA `beforeinstallprompt` event (`InstallButton.tsx:32`) — a liability classification and a browser API, not deferment allocation.
5. **The closest real concept — and it is NOT shared allocation:** order-level `additionalCostsCents` (`src/features/orders/db.ts:28`) attaches a delivery/installation fee to *one* order; there is no mechanism to split one expense across multiple orders, projects, or periods. The only *temporal* cost-spreading is `capital_asset` depreciation (ZC-10); the only *category* aggregation is the expense-category system (ZC-02).

**Statement for the audit:** any Micro-side requirement for "project relationship and shared expense allocation by amount/percentage/estimate/deferment" transfers to a **green-field build** — Zman contributes no schema, no action, no UI, and no invariant for it. Its closest transferable *ingredients* are (a) the two-dimension classification (`is_capital_asset` × `cost_nature`, ZC-02), (b) read-time non-cash adjustments (COGS/depreciation/write-off, ZC-09), and (c) the report-side "distribution of totals" analytics — none of which is allocation.

---

## 2. Complete capability catalog

Status column = this code review vs the prior map (`repos/Documents/reports/2026/2026-09-03/zaman-to-micro-gap-analysis-001/subagents/01-zaman-capability-map.md`). Paths relative to `artifacts/zman-app/` unless `root:` (repo root).

| ID | Capability (AR + EN) | Route / surface | Key files:lines | Financial effect | Status |
|---|---|---|---|---|---|
| ZC-01 | نموذج الإدخال المالي الموحّد — SmartFinanceForm guided entry (4 modes) | `/finance` FAB «تسجيل جديد»; edit via `?editExpense=`/`?editPurchase=` | `src/features/finance/components/SmartFinanceForm.tsx:47-54,58-115,338-459` | Per mode: expense → cash out + profit down; purchase → cash out (capitalized if tracked); asset → cash out, profit untouched; receivable → cash out, profit untouched | CONFIRMED (comment drift, §6.3) |
| ZC-02 | فئات المصاريف والتصنيف — expense categories + 2-dim classification | SmartFinanceForm expense mode; PaymentsTab «إدارة الفئات» | `src/features/finance/actions.ts:678-783,2560-2790`; `src/features/finance/db.ts:108-171,238-260` | Operating expense hits month profit; capital excluded (equity line); write-off flag = non-cash loss | CONFIRMED |
| ZC-03 | مدفوعاتي — unified payments feed (expenses+ purchases+ assets+ receivables) | `/finance` tab «المدفوعات» | `src/features/finance/queries.ts:80-505`; `PaymentsTab.tsx:42-47` | Read-only feed; deletes reverse cash via soft-delete | CONFIRMED |
| ZC-04 | المبيعات اليدوية — manual sales | `/finance` tab «المبيعات»; FAB «مبيعات جديدة» | `src/features/finance/actions.ts:1069-1173`; `SaleForm.tsx:79-149` | cash in (sale); order-source posts remainder only | CONFIRMED |
| ZC-05 | دورة حياة الطلب — order lifecycle | `/orders` (list/calendar tabs, detail `?id=`) | `src/features/orders/actions.ts:31-1022`; `orders/db.ts:14-92` | Deposit-in only until conversion; estimates never in totals | CONFIRMED |
| ZC-06 | تحويل الطلب لمبيعة + تسويات العربون — order→sale conversion + deposit transform/reverses | OrderDetail buttons | `finance/actions.ts:1441-2440` | Revenue booked once at delivery; deposit reclassified; refund = cash out; forfeiture = liability→revenue w/o cash | CONFIRMED-WITH-DIFFERENCES (forfeit sale `source='manual'`, §6.1) |
| ZC-07 | المخزون الانتقائي — selective inventory + catalog_movement ledger | `/catalog` toggle; `/inventory` | `inventory/actions.ts:79-608`; `catalog/db.ts:15` | Tracked purchases capitalized; COGS at sale; untracked = pure expense | CONFIRMED |
| ZC-08 | مكوّنات الطلب وحساب التكلفة — order components cost build-up | OrderForm «مكوّنات الطلب» | `orders/actions.ts:106-171`; `orders/schema.ts:23-41` | None at save (estimate); drives stock deduction at delivery | CONFIRMED |
| ZC-09 | الربح الموحّد — LOCKED-6 single profit function | all money surfaces | `src/features/finance/pnl.ts:122-290` | `operatingNetCents = sales − opExp − opPurch − COGS − writeoff − depreciation` | CONFIRMED |
| ZC-10 | الأصول والإهلاك — capital assets + read-time depreciation | asset mode → DepreciationPromptModal; `/assets` | `depreciation/actions.ts:59-391`; `depreciation/queries.ts:83-127,160-219` | Non-cash monthly depreciation hits profit; balance sheet cash-basis | CONFIRMED |
| ZC-11 | الذمم المدينة — receivables/loans-out | SmartFinanceForm «دَين لشخص»; PaymentsTab chip «ديون» | `finance/db.ts:414-491`; `finance/actions.ts:3710-4125` | Asset not expense; cash ↔ receivable swap; profit never moves | CONFIRMED |
| ZC-12 | الحسابات والتحويلات وسحب المالك — accounts/transfers/owner draw | `/finance?tab=accounts`, `/finance/accounts` | `finance/actions.ts:2790-3265,3265-3460` | Transfer = paired out+in (net zero); draw/inject affect equity not profit | CONFIRMED |
| ZC-13 | الأرصدة الافتتاحية — opening balances | `/settings/opening-balance` | `finance/actions.ts:3463-3704` | Seeds `opening` cash movements; lock-once | CONFIRMED |
| ZC-14 | لوحة المعلومات — dashboard bundle | `/` | `dashboard/queries.ts:90-793`; `dashboard/components/*` | Display-only; one bundle round-trip | CONFIRMED |
| ZC-15 | التقارير والتنزيلات — reports + downloads | `/reports` | `reports/actions.ts:58-460,660-1087` | Read-only; 6 MD downloads; balance-sheet equation | CONFIRMED |
| ZC-16 | فحص السلامة — integrity checks IC-1..IC-16 | `/reports` → «فحص الآن» | `finance/integrityCheck.ts:65-1609` | Read-only audit; PASS/WARN/FAIL | CONFIRMED |
| ZC-17 | الكتالوج — material catalog | `/catalog` | `catalog/actions.ts:38-199`; `CatalogClient.tsx` | default cost = prefill snapshot only | CONFIRMED-WITH-DIFFERENCES (delete is soft, §6.2) |
| ZC-18 | شطب المخزون — inventory write-off | `/catalog` «صرف يدوي»; `/inventory` quick adjust | `inventory/actions.ts:431-583` | Non-cash loss; movement + shadow expense; IC-1 stays 0 | CONFIRMED |
| ZC-19 | سجل التدقيق — append-only audit log | `/settings/audit-log` | `audit/actions.ts:39-58`; `audit/queries.ts:36-88` | None (logging only) | CONFIRMED |
| ZC-20 | الملاحظات — snippets library | `/snippets` | `snippets/actions.ts:27-139`; `snippets/db.ts:4-21` | None | CONFIRMED |
| ZC-21 | قوالب واتساب — WhatsApp templates | Orders toolbar editor; OrderDetail «إرسال تفاصيل العرض» | `src/lib/whatsapp.ts:6-96`; `orders/actions.ts:1028-1089` | None (external messaging) | CONFIRMED |
| ZC-22 | الدخول والقفل وPWA — passcode auth + idle lock + PWA | `/login`; app-wide | `middleware.ts:4-45`; `login/actions.ts:5-33`; `IdleLock.tsx:18-86`; `public/sw.js` | None | CONFIRMED |
| ZC-23 | النسخ الاحتياطي — JSON backup export | AppShell «حفظ نسخة من بيانات المشروع» | `src/components/shared/BackupModal.tsx:28-134` | None (export-only, not restorable) | CONFIRMED |
| ZC-24 | عقود UX للموبايل RTL — mobile RTL UX contracts | app-wide | `src/components/shared/*`; `root:CLAUDE.md §10:397-399` | n/a | CONFIRMED |
| ZC-25 | الحذف مع تراجع — delete-with-undo (5s toast + pagehide) | payments/orders/sales lists | `src/lib/undo-delete.ts:49-111` | Soft-delete committed after 5s; undo cancels | NEW-DISCOVERY (promoted) |
| ZC-26 | تحديد المعدل — server rate limiting (30/60s) | all mutating server actions | `src/lib/ratelimit.ts:17-27`; `finance/actions.ts:75-78` | Blocks duplicate/flood writes | NEW-DISCOVERY (promoted) |
| ZC-27 | كاش العميل والمثابرة — TanStack localStorage persistence + stale-cache alert | app-wide data queries | `src/providers/query-provider.tsx:43-70` | None (read cache) | NEW-DISCOVERY (promoted) |
| ZC-28 | مسارات الإحماء — `/api/health` + `/api/ping` warm-up | ops | `src/app/api/health/route.ts`; `src/app/api/ping/route.ts` | None | NEW-DISCOVERY (promoted) |
| ZC-29 | مسودات النماذج — localStorage drafts (Issue #7) | Order/Sale/SmartFinance forms | `OrderForm.tsx:170-212`; `SmartFinanceForm.tsx:338-459`; `SaleForm.tsx:79-124` | None until submit | NEW-DISCOVERY (promoted) |
| ZC-30 | بقايا SQL ميتة — unreferenced `triggers.sql` + root ops script | code artifacts | `src/lib/db/triggers.sql` (0 references); `root:FIX_DELIVERED_ORDERS_WITHOUT_SALES.sql` | None (not executed by app) | NEW-DISCOVERY (artifact) |

---

## 3. Per-capability dossiers

Compact format. Fields per the mission brief: problem · entry/journey · mandatory vs optional inputs · validation/errors · storage · derived · financial effect · unknown/zero behavior · correction/reversal · offline/reload · exit/cancel · completion state · discoverability.

### ZC-01 — SmartFinanceForm guided entry (نموذج الإدخال الذكي)
- **Problem:** the Jordanian owner was lost among expense/purchase/asset forms; one guided entry with explicit profit impact per mode ("إدخال واحد لكل المداخل").
- **Entry/journey:** `/finance` → FAB «تسجيل جديد» → ResponsiveModal → mode selector icons (`SmartFinanceForm.tsx:49-54`: مصروف يومي/شراء مواد/أصل للورشة/دَين لشخص) → mode-specific fields → hint line per mode (`:858-861` profit-impact wording) → save → toast + list refetch.
- **Mandatory/optional:** expense: date, category (select + free text), amount>0; note optional. purchase: date, item (catalog picker or free text), quantity>0, total>0; supplier/notes optional. asset: date, name, amount>0; description + `wantDepreciation` optional. receivable: date, personName, amount>0, accountId; notes optional (`:58-115`).
- **Validation/errors:** Zod per mode (`:58-115`); `assertOnline()` throws "offline" toast (`src/lib/online.ts:10-14`); in-flight double-submit guard; server errors surfaced as Arabic toasts.
- **Storage:** mode→table mapping: expense/asset→`expense` (asset sets `isCapitalAsset=true, costNature=null`); purchase→`purchase` (+ `catalog_movement in` if tracked link); receivable→`receivable` + cash out.
- **Derived:** purchase unit cost derived `unitCostMicroCents = round(total×1000/qty)` (micro-fils, exact `unit×qty=total`); `purchase.totalCents` is GENERATED (`finance/db.ts:38-42`).
- **Financial effect:** expense → cash out + operating profit −; purchase → cash out, profit − only if untracked; asset → cash out, profit unchanged (capital line); receivable → cash out, profit unchanged (asset swap).
- **Unknown/zero:** amount 0 rejected (positive); qty 0 rejected; unpriced asset not possible (amount mandatory).
- **Correction/reversal:** edit reopens prefilled form preserving classification ("Edit Trap" fix, `:129-150`); delete via parent list with undo (ZC-25).
- **Offline/reload:** per-mode localStorage drafts offered back on reopen (create-only, `:338-459`); offline submit blocked.
- **Exit/cancel:** modal X/back → draft persists silently.
- **Completion:** toast «تم تسجيل…», draft key removed (`:517,540,592,618,675,700,752`).
- **Discoverability:** fixed FAB label «تسجيل جديد» in every payments view; mode icons.
- **Note:** file header comment says «ثلاثة أوضاع» (three modes) while `MODES` has four — stale comment (§6.3).

### ZC-02 — Expense categories + classification
- **Problem:** free-text categories produced 4 spelling variants of "owner salary"; two conflicting category sources.
- **Entry/journey:** expense mode category select (catalog + "أخرى"); PaymentsTab second row «[▾ كل الفئات] [إدارة الفئات]» (expense chip only); FinanceCatalogModal CRUD.
- **Mandatory/optional:** category required ≤200 chars; classification dimensions are system/advanced-set: `isCapitalAsset` bool, `costNature ∈ {fixed,variable}` nullable (`finance/schema.ts:63-65`); DB CHECK enforces logic (`finance/db.ts:149-153`).
- **Validation:** Zod `expenseInputSchema` (`schema.ts:46-66`); trimmed category; empty category rejected.
- **Storage:** `expense` row + `expense_category_catalog` lazy auto-enroll via `ensureExpenseCategoryInCatalog` (`actions.ts:2639`) + seed defaults `seedDefaultExpenseCategories` (`actions.ts:2560`); filter merge includes `SELECT DISTINCT category` orphans.
- **Derived/financial:** operating rows reduce `operatingExpensesCents` in their month; capital rows → `capitalAdditionsCents` (balance-sheet line, excluded from profit); `is_inventory_writeoff=true` rows are non-cash loss (read directly from `expense` by `pnl.ts:224-237`).
- **Unknown/zero:** `costNature` NULL ≡ variable; **cannot distinguish NULL vs 'variable' in filters** (known gap م-2; `?nature=` filter exists server-side with no UI button, `queries.ts:103-111`).
- **Correction:** updateExpense re-derives cash movement and re-feeds catalog; **write-off rows guarded** from edit/delete (`actions.ts:819-828`); delete = soft + audit + 5s undo.
- **Completion:** toast; new category appears in select and catalog.
- **Discoverability:** chips row + «إدارة الفئات» button visible only on expense chip (deliberate progressive disclosure).

### ZC-03 — Unified payments feed («مدفوعاتي»)
- **Problem:** two overlapping tabs (expenses/purchases) → one list the owner asked for.
- **Entry/journey:** `/finance` default tab; SegmentedControl 2 tabs «المدفوعات»/«المبيعات» (`FinanceClient.tsx:55-58`); chips الكل·مصاريف·مشتريات·أصول·ديون (`PaymentsTab.tsx:42-47`); search debounced 400ms → `?search=`; infinite scroll cursor pagination over UNION ALL of expense/purchase/receivable (`finance/queries.ts:80-505`).
- **Inputs:** server filters `filter/category/search/nature`; legacy `?tab=expenses|purchases` auto-redirect with chip (CLAUDE.md §10:416).
- **Validation:** chip semantics enforced server-side (e.g. asset chip = `isCapitalAsset=true` both tables, `queries.ts:112-116`).
- **Storage:** read-only; mutations soft-delete row + linked `cash_movement` (+ `catalog_movement` for purchases) + audit.
- **Financial effect of delete:** reverses cash movement; profit recomputed live.
- **Unknown/zero:** write-off cards render gray, read-only (no ⋯ menu); zero-amount expense impossible (amount>0).
- **Correction/reversal:** edit → SmartFinanceForm prefilled; delete → 5s undo (ZC-25).
- **Offline/reload:** network-first; stale cache + alert bar (ZC-27); ErrorState only when no cache.
- **Completion state:** infinite scroll end (nextCursor undefined).
- **Discoverability:** chips + category row + FAB; empty-state with onboarding steps.

### ZC-04 — Manual sales («مبيعاتي»)
- **Problem:** record walk-in cash income not tied to an order.
- **Entry/journey:** `/finance` → tab «المبيعات» → FAB «مبيعات جديدة» → SaleForm (date, amount, description) → save.
- **Mandatory/optional:** date, amount>0 required; description optional; `source` fixed 'manual' from SaleForm; Zod refine: `orderId` required iff `source='order'` (`finance/schema.ts:89-100`).
- **Storage:** `sale` row + `cash_movement(in,'sale')`.
- **Derived/financial:** profit up by amount; **order-source posts `max(0, amount − order.depositCents)`** to avoid double-counting the deposit (INV-4; `actions.ts:1123-1132`); unique partial index blocks double conversion while a sale is active (`finance/db.ts:201-203`).
- **Correction:** updateSale re-derives cash; deleteSale soft-deletes sale+movement and re-opens the order for re-conversion (F-32).
- **Offline:** draft localStorage (`SaleForm.tsx:79-124`); `assertOnline`.
- **Completion:** toast; SalesTab list refetch; activities feed entry.
- **Discoverability:** tab + FAB label differs per tab («مبيعات جديدة»).

### ZC-05 — Order lifecycle
- **Problem:** run made-to-order jobs from quote → delivery without corrupting the books.
- **Entry/journey:** `/orders` (tabs القائمة/التقويم, `OrdersClient.tsx:58,137-148`; status filter sheet; search) → FAB → OrderForm → create as `draft` → status buttons (`sent`/`confirmed`/`cancelled`) → OrderDetail `?id=` for convert/refund/forfeit/WhatsApp.
- **Mandatory/optional:** customerName, productName, quantity>0, requestId (UUID) mandatory; **both phones optional** (stored `""` to satisfy NOT NULL without migration, `orders/schema.ts:15-21`, `orders/db.ts:20-23`); components array; price ≥0; deposit ≤ price+additionalProfit (refine `schema.ts:89-92`); deliveryDate/receivedDate/notes/deliveryPaid/additionalProfit optional.
- **Validation/errors:** Zod; optimistic concurrency (`updatedAt` compare) on update/status; rate limit.
- **Lifecycle guards (all in `updateOrderStatus`, orders/actions.ts:789-1022):** cannot set `delivered` directly («لتأكيد التوصيل، استخدم زر «تحويل إلى مبيعات»», `:809-814`); cannot reopen cancelled (`:833-838`); cannot cancel delivered (`:843-849`); cannot cancel with unsettled deposit (`:855-890`); cannot leave delivered via raw status change (`:894-900`); self-heal check blocks status change while an active sale exists (`:904-917`).
- **Storage:** `order` + `order_component` rows; deposit posting at creation (INV-3): one `cash_movement(in,'deposit')` if `depositCents>0` (`orders/actions.ts:144-157`).
- **Derived:** `totalCostCents = Σ(cost×qty per unit) × orderQty + additionalCosts` (`orders/actions.ts:106-114`); expected profit shown as «تقديري/متوقّع» only.
- **Financial effect:** none beyond deposit cash-in until conversion; estimates never enter totals.
- **Unknown/zero:** price 0 allowed at save but blocks conversion («لا يمكن تحويل طلب بسعر صفر», `finance/actions.ts:1487-1489`).
- **Correction:** updateOrder full edit (re-derives deposit movement); deleteOrder soft; cancel cleans linked sale/deposit movements with historical-refund preservation (`orders/actions.ts:934-1003`).
- **Offline/reload:** create-mode localStorage draft (`OrderForm.tsx:170-212`).
- **Completion:** status badge colors (`src/lib/status-colors.ts`); delivered shows sale link; calendar shows delivery dates.

### ZC-06 — Order→sale conversion + deposit transform + settlement inverses
- **Problem:** book revenue exactly once at delivery; handle deposits without double-counting; undo everything cleanly.
- **Entry/journey (OrderDetail):** «تحويل إلى مبيعات (تسجيل إيراد)» → «عكس البيع» → «رد أموال العربون» → «احتجاز العربون» / «عكس احتجاز العربون» (`OrderDetail.tsx:653,677,681-688,920,1056,1068-1070`).
- **convertOrderToSale** (`finance/actions.ts:1441-1638`) — transaction + row lock + idempotency key `convert_to_sale`: guards (exists, not deleted, price>0, not cancelled, deposit ≤ realized, no active sale `:1481-1517`); sale row `amountCents = totalPrice + additionalProfit` (FULL realized, `:1528-1541`); **deposit transform**: existing `deposit/in` movement *reclassified* in place to `sale/in` pointed at the new sale («محوَّل من عربون» — no new cash event, `:1549-1576`); remainder movement inserted only if `realized − collectedDeposit > 0` computed from the **collected movement amount** not `order.depositCents` so refunded parts are never re-booked (`:1578-1595`); `deductForDelivery` runs in the same transaction BEFORE status→delivered (`:1597-1616`); audit after commit (`:1622-1630`).
- **reverseSale** (`:1650-1778`): finds the «محوَّل من عربون» movement by description and reclassifies back to `deposit` (`:1710-1724`); soft-deletes the remainder movement; `restoreForReverse` soft-deletes all `order_delivery` movements (COGS auto-reverses at read, `inventory/actions.ts:385-414`); soft-deletes the sale; order → `confirmed` with liability intact (`:1740-1756`).
- **refundOrder** (`:1787-2020`): independent `deposit/out` movement on a chosen account; guards: not delivered/cancelled, amount ≤ remaining deposit, total refunds ≤ original collection (`:1855-1912`); reduces `order.depositCents` (`:1952-1960`).
- **forfeitDeposit** (`:2020-2232`): cancelled-order settlement — requires exactly one unrefunded collection matching the remaining liability (`:2097-2136`); creates a **`sale` row with `source='manual'`** for the forfeited remainder (`:2150-2161`) [prior map says 'order' — see §6.1]; reclassifies the collection movement to `sale` (no new cash, `:2167-2175`); order → `cancelled`, `depositCents=0` (`:2177-2186`).
- **reverseDepositForfeiture** (`:2238-2440`): reclassifies back to `deposit`, soft-deletes the forfeiture sale, order → `confirmed` — mirror of root `ACCOUNTING_RULES.md` rule 8.
- **Financial effect:** revenue recognized once at delivery; deposit held as liability until then (reports `getFinancialPosition:780-793`); refund = cash out + liability down; forfeiture = liability→revenue without cash.
- **Unknown/zero:** zero-price order blocked; forfeiture of fully-refunded deposit blocked (forfeited ≤ 0).
- **Offline/idempotency:** all four settlement actions carry `requestId` idempotency keys; row-level `FOR UPDATE` locks.
- **Completion:** toasts per action; IC-3/IC-4/IC-9/IC-16 guard the lifecycle at runtime.

### ZC-07 — Selective inventory + catalog_movement ledger
- **Problem:** profit swung because material purchases hit profit immediately and sales deducted nothing.
- **Participation model:** per catalog item `tracked` flag, default **false** (deliberately non-stock) (`catalog/db.ts:15`). Untracked items never create movements (silent skip in `createPurchase` and `deductForDelivery`, `inventory/actions.ts:237,258`). First-time activation may enter opening stock → `catalog_movement(in,'opening')` at **zero cost by design** (cost was expensed at purchase; CLAUDE.md §7:351-363).
- **Entry/journey:** `/catalog` → toggle «تفعيل التتبع» + opening qty → purchases linked → `/inventory` screen (low-stock banner `:111-112`, stats «إجمالي الأصناف/القيمة الدفترية» `:125-129`, per-item cards with «نفد» badge `:192-197`, FAB «إجراءات المخزون» `:226` → AddTrackedItemForm/QuickAdjustStockForm, `?filter=low-stock`).
- **Mechanics:** purchase→`in` movement (unitCost=floor(total/qty), `totalValueCents=purchase.totalCents` exact); delivery→`out` movement qty = component qty × order qty (`inventory/actions.ts:260-262`) with **weighted-average COGS stored immutably on the movement** (`:294-311`); negative balance **allowed**, warning recorded in movement notes (`:267-270`); A4 "last out sweeps residual book value" avoids 1-fils ghosts (`:313-336`); untracking soft-deletes all movements after explicit confirm dialog (CatalogClient `:328-338`).
- **Validation:** createPurchase rejects linking to non-tracked/missing item and rejects `isCapitalAsset=true` + tracked link (double-count guard).
- **Financial effect:** tracked purchase excluded from operating profit (`is_tracked_inventory=true`, `pnl.ts:185-200`), appears as balance-sheet asset `inventoryValueCents` (`reports/actions.ts:733-749`); COGS deducted in the sale month (`pnl.ts:209-222`).
- **Correction:** updatePurchase soft-deletes and re-derives movements; reverseSale restores; no reverse for manual write-off (م-5).
- **IC-12:** FAIL on orphaned `order_component_id`, WARN on any negative per-item balance, else PASS (`integrityCheck.ts:1165-1183`).

### ZC-08 — Order components cost build-up
- **Problem:** cost a made-to-order product and see expected profit before saving.
- **Entry/journey:** OrderForm → «مكوّنات الطلب» → «إضافة مكوّن» → catalog picker (tracked badge + live stock) or free text → rows with cost (prefilled from `catalog_component.defaultCostCents` snapshot) + per-unit repetition qty → «تكاليف إضافية» order-level costs → price/deposit → live summary.
- **Inputs:** component cost ≥0 (0 allowed); quantity (per-unit repetition) >0; `catalogComponentId` optional (free text = null); `unit` field deliberately removed from persisted schema (D12 fix, `orders/schema.ts:36-41`).
- **Derived:** `unitComponentsCost = Σ(cost×repetition)`; total = ×orderQty + additionalCosts (`orders/actions.ts:106-114`); expected profit `= totalPrice − totalCost + additionalProfit` shown neutral «تقديري» (`OrderDetail.tsx:261,556-578`).
- **Storage:** `order_component` (name+cost **snapshots**; RESTRICT FK keeps history if catalog item later deleted).
- **Financial effect:** none at save (except deposit); COGS at delivery comes from inventory ledger, not the estimate.
- **Unknown/zero:** stock below requirement → pre-save warning modal, never blocks; cost 0 allowed.
- **Correction:** component rows editable until delivery (blocked after); delete row has in-form undo; no order duplication feature (verified absent in orders/actions.ts).
- **Completion:** order saved with components; badge «مربوط بصنف»/«نص حر» (tracked distinction missing in list badge — م-3).

### ZC-09 — LOCKED-6 single profit function
- **Problem:** "ربحي يتأرجح ولم أرَ رقمي الحقيقي أبداً" — multiple inline profit definitions disagreed.
- **Mechanics:** `computeOperatingPnl({startDate?, endDate, tx})` is the only profit definition (`pnl.ts:122-290`); 6 parallel queries (Promise.all `:242-256`): sales-in, expenses (operating/capital conditional), purchases (operating/capital/tracked), period depreciation, COGS, write-offs. Result:
  `operatingNetCents = salesCents − operatingExpensesCents − operatingPurchasesCents − cogsCents − inventoryWriteOffCents − monthlyDepreciationCents` (`:272-278`).
- **Callers (LOCKED-6):** `dashboard.getFinancialSummary`, `reports.computeCashBasisPnl` (`reports/actions.ts:58-88` — thin wrapper, `netCents: pnl.operatingNetCents`), `dashboard.getMonthlyProfit` — no inline profit anywhere; IC-13 cross-checks all three entry points for two periods and FAILs on drift (`integrityCheck.ts:1240-1312`, title at `:1315`).
- **Financial effect:** defines profit for every surface; non-cash adjustments (COGS/write-off/depreciation) subtract here and only here.
- **Unknown/zero:** no movements → all zeros (legit new-business state; FinancialAdvisor handles the empty case).
- **Discoverability:** dashboard card «صافي الربح», P&L report, monthly panel — all labeled from the same function.

### ZC-10 — Capital assets + read-time depreciation
- **Problem:** a machine purchase shouldn't crater one month's profit.
- **Entry/journey:** SmartFinanceForm asset mode + `wantDepreciation` → DepreciationPromptModal (useful life months, "توزيع شهري (إهلاك)" `SmartFinanceForm.tsx:1262`); `/assets` screen (More menu) with two sections «أصول بلا إهلاك»/«تحت الإهلاك»; PaymentsTab ⋯ → «إيقاف الإهلاك».
- **Validation:** life 1–600 months; purchaseDate not future (`depreciation/actions.ts:84-119`); name ≤200; amount integer ≥0; idempotent per `(sourceType, sourceId)` (`:122-135`).
- **Storage:** `capital_asset` (no FK to source by design — history survives source deletion); `monthlyDepreciationCents = floor(amount/life)` (`:141-143`); `startedAt = purchaseDate` (A-2 fix, retroactive, `:166`).
- **Derived (read-time):** period depreciation via EXTRACT year×12+month formula, capped at life, zero before start / after full life (`depreciation/queries.ts:83-127`); valuation with D13 "last month charges the remainder" so NBV hits exactly 0 (`:160-219`, `:195-199`).
- **Financial effect:** non-cash; P&L −period depreciation; balance sheet stays cash-basis (retained excludes depreciation by design — the two declared profit numbers D3 rule).
- **Correction:** `updateCapitalAsset` edits name/date/life only — **`purchaseAmountCents` immutable** (taken from DB row, `:327-349`); `deleteCapitalAsset` stops depreciation (soft); both re-derive at read time.
- **Completion:** /assets shows original/depreciated/NBV/monthly; IC-14 informational.

### ZC-11 — Receivables (loans-out)
- **Problem:** owner lends people cash; it is an asset, not an expense («هذول مستردّات»).
- **Entry/journey:** SmartFinanceForm «دَين لشخص» (hint: «لا يُخصم من ربحك — مالك ما زال لك، لكن عند غيرك.») → PaymentsTab chip «ديون» → open loan card → «تسجيل دفعة» → ReceivablePaymentModal.
- **Inputs:** loan: personName, amount>0, accountId, date, notes optional (`finance/schema.ts:189-207`); payment: receivableId, amount>0, accountId, date, notes (`:210-225`).
- **Storage:** `receivable` + `receivable_payment`; cash movements `receivable/out` + `receivable_payment/in` (`finance/actions.ts:3710-4125`).
- **Derived:** remaining = `amount − Σpayments` **computed at read, never stored**; status قائم/مسدَّد derived; settled loans stay visible.
- **Financial effect:** cash ↔ asset swap; **never enters computeOperatingPnl** (separate tables); balance-sheet asset `receivablesCents` (`reports/actions.ts:752-776`); IC-15 reconciles (`integrityCheck.ts:1420-1489`).
- **Correction:** deleteReceivable/deleteReceivablePayment soft-delete + reverse cash; payment exceeding remaining rejected in-action.
- **Completion:** card flips to مسدَّد; equityDrift stays 0.

### ZC-12 — Accounts, transfers, owner draw/inject
- **Problem:** cash box vs bank; personal money must not distort profit; move money without double counting.
- **Entry/journey:** hidden `/finance?tab=accounts` (AccountsTab+OwnerTab stacked, back-button header; legacy `?tab=owner|opening` redirects, `FinanceClient.tsx:69-97`); `/finance/accounts` standalone; More-sheet link.
- **Mechanics:** accounts `cash|bank`, archive refused with non-zero balance (INV-13); **transfer = pair of movements with a shared generated `transferId`** (`finance/actions.ts:3153-3175`) — net zero on the books; `deleteTransfer` soft-deletes both (F-23, `:3207`); owner draw/inject = `owner_transaction` + cash movement, equity-side only; salaries belong here since آب 2026 (م-10 policy, CLAUDE.md §15:530).
- **Validation:** transfer same-account and ≤0 rejected (`:3118-3124`); account name required; unique default cash box «الصندوق الرئيسي» (`finance/db.ts:285-287`).
- **Financial effect:** none on profit; balance sheet per-account balances read-time (`getAccountBalances:3041`).

### ZC-13 — Opening balances
- **Problem:** start the ledger from real starting cash/bank/capital.
- **Entry/journey:** More sheet → `/settings/opening-balance` → form (goLiveDate, cashCents, bankCents, capitalCents) → save → «قفل» → locked read-only summary.
- **Mechanics:** single `opening_balance` row; saving writes/updates **`opening` cash movements into cash+bank accounts** (ledger is the only truth — no balance column on `account`, dropped in migration 0011) (`finance/actions.ts:3476-3680`); lock guard `:3495-3503`; IC-11 reconciles (`integrityCheck.ts:986-1026`).
- **Financial effect:** seeds assets and `openingCashInEquityCents`; capital is reference-only.
- **Correction:** editable until locked; locked = frozen (only fix = manual DB ops).

### ZC-14 — Dashboard bundle
- **Problem:** one home screen with the trusted number + education.
- **Entry/journey:** `/` → period filter (month/30d/all) → cards + panels; single `getDashboardBundle` query (11→1 round-trip, `dashboard/queries.ts:740`; CLAUDE.md §14:497).
- **Surfaces:** net profit, cash, capital additions, `monthlyDepreciationCents`, `inventoryValueCents`, `cogsCents` (interface `:16-77`); SmartAlertsBar; FinanceComparePanel (bars مبيعات/تكلفة المبيعات/مصاريف تشغيلية/مشتريات تشغيلية/إهلاك); LiquidityFlowPanel; MonthlyProfitPanel («شهر الشراء قد يظهر خسارة وهذا صحيح» tooltip); UpcomingDeliveriesCard (auto-hide); FinancialAdvisor (Arabic sentences); DetailsLayer drill-down (localStorage expanded/collapsed, `DetailsLayer.tsx:86-100`); GlobalSearch.
- **Financial effect:** none (display); all numbers from LOCKED-6 path.
- **Discoverability:** bottom-nav «الرئيسية»; «أكمل الإعداد الأولي للمشروع» completion CTA (`DashboardClient.tsx:281`).

### ZC-15 — Reports + downloads
- **Problem:** owner-readable statements + shareable files.
- **Entry/journey:** `/reports` → tabs «التقارير»/«الوضع المالي» → period segmented control → sections (P&L summary, expense-by-category donut, sales summary, order-status distribution, top products, balance sheet, advanced reconciliation) → per-section `DownloadBtn` (types pnl/expenses/sales/orders/products/balance_sheet, `reports/page.tsx:329-576`) → Markdown blob download.
- **Mechanics:** `downloadReport` builds Arabic Markdown with tables (`reports/actions.ts:90-460`); balance-sheet equation (§7).
- **Financial effect:** read-only.
- **Completion:** file `report_<name>_<date>.md` saved; toast.

### ZC-16 — Integrity checks IC-1…IC-16
- **Problem:** make correctness observable by a non-accountant.
- **Entry/journey:** `/reports` → «فحص الآن» (IntegrityCheckReportPanel) → 16 checks in parallel → overall PASS/WARN/FAIL + Arabic titles/descriptions/suggested fixes.
- **Inventory of checks (file:line of result):** IC-1 balance (`:270`), IC-2 orphans (`:428`), IC-3 deposit liability (`:535`), IC-4 no double count (`:602`), IC-5 archived w/ balance (`:647`), IC-6 P&L↔retained (`:718`), IC-7 unit consistency (`:753`), IC-8 ledger↔source tables (`:864`), IC-9 sale=order revenue (`:908`), IC-10 owner tx↔movement (`:970`), IC-11 opening↔movements (`:998,1029`), IC-12 inventory ledger (`:1191`), IC-13 LOCKED-6 sources, month+all (`:1315`), IC-14 asset valuation (`:1394`), IC-15 receivables↔ledger (`:1492`), IC-16 deposit settlement (`:1598`). Runner `:65-122`.
- **Financial effect:** none (read-only); FAIL is a stop-the-line signal (CLAUDE.md §6:337).
- **Completion:** report persisted in UI with runAt; drill into offending IDs.

### ZC-17 — Catalog
- **Problem:** reusable materials list with default costs.
- **Entry/journey:** `/catalog` → search (debounced 400ms → `?q=`) → create/edit modal (name, defaultCostCents, unit default «قطعة», notes, tracked + openingStock on first activation) → per-card ⋯ sheet (تعديل/حذف) → movement history sheet.
- **Storage:** `catalog_component` (soft-delete column present).
- **Note (§6.2):** server `deleteCatalogComponent` performs a **soft delete** (`catalog/actions.ts:173-176`) even though the UI ConfirmDialog says «حذف نهائي … لا يمكن التراجع» (`CatalogClient.tsx:303-326`) and a code comment claims hard delete (`:270-271`). No undo affordance exists.
- **Financial effect:** `defaultCostCents` is a prefill snapshot only.
- **Validation:** name ≤200 required; cost ≥0; FK RESTRICT protects referenced items.

### ZC-18 — Inventory write-off
- **Problem:** damaged/stolen stock must reduce profit without faking a cash payment.
- **Entry/journey:** `/catalog` «صرف يدوي» modal or `/inventory` quick-adjust (direction out, qty, reason).
- **Mechanics:** ONE transaction (`inventory/actions.ts:451-578`): weighted-avg cost + totalValue (`:496-536`), `catalog_movement(out,'manual_out')`, and if value>0 a shadow `expense` row (`category='هدر/تلف مخزون'`, `isInventoryWriteoff=true`, `costNature='variable'`, **no cash movement**, `:557-575`).
- **Financial effect:** P&L line `inventoryWriteOffCents` (`pnl.ts:224-237`); balance sheet: inventory asset down + retained down by same amount → IC-1 = 0 (`reports/actions.ts:902-918`).
- **Correction:** **guarded from edit/delete** in updateExpense/deleteExpense (`actions.ts:819-828` + delete path); no reverse feature (م-5); gray read-only card in PaymentsTab.
- **Completion:** toast; item balance/value drop; audit row (via adjustStock → no direct logAction — movements logged by catalog hooks; expense insert has no audit row: noted as minor inconsistency).

### ZC-19 — Audit log
- **Problem:** "who did what when" without multi-user complexity.
- **Mechanics:** `logAction` called AFTER every successful transaction, swallows ALL errors including missing table (`audit/actions.ts:39-58`); `userId` hardcoded `"owner"` because the session cookie stores the passcode itself and must never be persisted (`:29-37`); UI `/settings/audit-log` infinite scroll (PAGE_SIZE 50, `audit/queries.ts:23`), `tableMissing` EmptyState (`:20`).
- **Coverage:** all finance create/update/delete + convert/reverse/refund/forfeit + capital-asset actions + order status changes (call sites throughout `finance/actions.ts`, `orders/actions.ts`, `depreciation/actions.ts`).
- **Financial effect:** none; append-only.

### ZC-20 — Snippets
- **Problem:** reusable workshop notes/answers.
- **Entry/journey:** `/snippets` → grouped by category → «نسخ» → «✓ نُسخ» → CRUD modals.
- **Fields:** title ≤200, body ≤5000, category ≤64 default «عام» (`snippets/db.ts:16-18`); optimistic concurrency on update.
- **Financial effect:** none.

### ZC-21 — WhatsApp templates
- **Problem:** send a professional Arabic quote message from the order.
- **Entry/journey:** OrderDetail «إرسال تفاصيل العرض عبر واتساب» (`OrderDetail.tsx:681-688`); template editor from orders toolbar (message_template row, `orders/actions.ts:1028-1089`).
- **Mechanics:** variables `{customerName}/{productName}/{quantity}/{totalPrice}/{deliveryDate}/{notes}` (`src/lib/whatsapp.ts:24-45`); Jordan phone normalization 07…→962…, 00962, bare 7… (`:6-22`); fallback to alt phone; button hidden when no valid number (`:51-59`).
- **Financial effect:** none (external).

### ZC-22 — Passcode auth + idle lock + PWA
- **Mechanics:** env `PASSCODE`; cookie `zman_session` 8h httpOnly sameSite=strict, **`secure` conditional on production** (fixed; CLAUDE.md §4 documents the old bug, `login/actions.ts:12-22`); middleware fail-closed if PASSCODE unset (`middleware.ts:26-29`); 10-minute idle lock via visibilitychange + localStorage timestamp shared across tabs, works inside installed PWA (`IdleLock.tsx:8-86`); SW network-first, no precache, safe SKIP_WAITING update prompt (`public/sw.js:1-34`); manifest "Zman Greens JO" standalone (`src/app/manifest.ts:7-11`); install button/FAB with iOS/Android hints.
- **Offline:** SW deliberately does NOT serve stale data; mutation blocked by `assertOnline`.
- **Discoverability:** lock happens silently (redirect to /login).

### ZC-23 — JSON backup export
- **Mechanics:** AppShell → «حفظ نسخة من بيانات المشروع» → BackupModal → downloads `zman-backup-YYYY-MM-DD.json` with accounts (incl. archived), catalog, openingBalance, capitalAssets, **last 100 orders only** (`BackupModal.tsx:28-70`); explicit honesty warning: «ليست نسخة استرجاع كاملة … لا يمكن استيرادها» (`:101-108`).
- **Financial effect:** none; no import path anywhere in the app.

### ZC-24 — Mobile RTL UX contracts
- **Contracts (root CLAUDE.md §10:397-417):** logical CSS properties only (`ps-/pe-/ms-/me-/text-start`), no `pl-/pr-/left-/right-`; 360/390px first; ≥44px touch targets; header carries tabs+search only (anti-jitter); filters are body chips; `flex-wrap` not horizontal scroll; fixed FAB label per tab; no function leaves its tab.
- **Shared kit:** Button, MoneyInput (Arabic-Indic numeral parsing ٠-٩ + currency-label stripping, `src/lib/money.ts:32-48`), Select, SegmentedControl, FilterChip, CardActionSheet, ConfirmDialog, ResponsiveModal, EmptyState (with onboarding steps), ErrorState, SkeletonList, InfoTooltip, FAB, PageToolbar, AmountText, DateText, Sparkline, StatusBadge.
- **Design contracts on disk:** `docs/DESIGN_SYSTEM_V2_1_CONTRACT.md`, `docs/HEADER_AND_HOME_V2_2_CONTRACT.md`, `docs/HEADER_CONCEPT_V2_3_CONTRACT.md`.

### ZC-25 — Delete-with-undo (NEW, promoted)
- `scheduleDeleteWithUndo` (`src/lib/undo-delete.ts:49-111`): optimistic hide → 5s countdown toast with «تراجع» → commit (server soft-delete) → only then past-tense confirmation «تم الحذف» (Issue #17 honesty rule `:29-37`); `pagehide` fire-and-forget last attempt **guarded by `navigator.onLine`** (Issue #6, `:58-66`); per-call closures prevent interleaving; dismiss (X) does not commit (`:108-110`). Used by PaymentsTab/SalesTab/Orders lists.

### ZC-26 — Server rate limiting (NEW, promoted)
- Upstash sliding window **30 requests/60s** per IP with a no-op fallback when env vars absent (`src/lib/ratelimit.ts:17-27`); uniform guard `checkRateLimit()` at the top of every mutating action (`finance/actions.ts:74-78`); Arabic error «تجاوزت الحد المسموح للعمليات — حاول بعد دقيقة».

### ZC-27 — Client query cache + persistence (NEW, promoted)
- TanStack Query `createSyncStoragePersister` to localStorage with cache-key removal on failure (`src/providers/query-provider.tsx:43-70`); staleTime 5 min (perf round 2); stale cache is shown behind an alert bar instead of ErrorState; single `getDashboardBundle` aggregation.

### ZC-28 — Health/ping warm-up routes (NEW, promoted)
- `GET /api/health` returns `{status:"ok"}` only, catch-without-params, excluded from middleware via `/api` mask (CLAUDE.md §14:506); `GET /api/ping` companion; purpose: prevent Supabase cold-sleep; no scheduler configured yet.

### ZC-29 — Form drafts (NEW, promoted)
- Issue #7 pattern: create-mode forms persist values to localStorage (`zman_draft_*`), offer restore banner on reopen, clear on successful submit; edit mode never persists. Evidence: `OrderForm.tsx:170-212,277`, `SmartFinanceForm.tsx:338-459`, `SaleForm.tsx:79-124`. Survives reload and PWA restart; not synced across devices.

### ZC-30 — Dead/ops SQL artifacts (NEW, artifact finding)
- `src/lib/db/triggers.sql` defines `set_updated_at()` triggers for 5 tables but is **referenced by zero code** (`rg "triggers.sql" src` → no matches) — `updated_at` is maintained by application code; the file is dead weight or a manual ops script.
- Root `FIX_DELIVERED_ORDERS_WITHOUT_SALES.sql` is a one-off ops repair script outside the migration chain.
- Neither affects runtime behavior; both are repo-hygiene notes for the transfer audit.

---

## 4. New discoveries (ZC-25…ZC-30) — summary

1. **ZC-25 Delete-with-undo** promoted to a standalone capability: the honest-toast ("no past tense until server confirms"), pagehide best-effort with online guard, and dismiss-doesn't-commit rules are distinct, transferable contracts.
2. **ZC-26 Rate limiting** (30/60s sliding window + no-op fallback) — previously a one-line mention inside ZC-24 craft rules.
3. **ZC-27 Query persistence** (localStorage persister + stale-cache alert bar + 5-min staleTime + bundle aggregation) — previously a footnote inside ZC-03.
4. **ZC-28 `/api/health` + `/api/ping`** warm-up ops capability (cited only in the nav inventory before).
5. **ZC-29 Draft persistence** as a cross-cutting capability (previously embedded in ZC-01).
6. **ZC-30 Dead SQL artifacts** (`triggers.sql` unreferenced; root ops script) — never catalogued.
7. **CLAUDE.md staleness findings (documentation vs code):** (a) §4's login `secure: true` bug is **already fixed** in code (`login/actions.ts:18` — conditional on NODE_ENV); (b) §5 م-4 "cannot edit useful life" is **already fixed** by `updateCapitalAsset` (`depreciation/actions.ts:282-391` + `SmartFinanceForm.tsx:201,664`); CLAUDE.md documents both as open. The prior map already noted (b); (a) is a new observation.
8. **Write-off expense rows skip the audit log** (adjustStock inserts the shadow expense directly with no `logAction` call, `inventory/actions.ts:565-574`) — a minor coverage gap in the otherwise blanket audit trail.

---

## 5. Audit-brief focus areas — consolidated code-verified statements

- **Project/shared allocation:** DOES NOT EXIST (§1) — no entity, no field, no UI, no invariant; nothing to transfer except generic ingredients.
- **Drafts/offline:** localStorage drafts (create-mode only) + assertOnline mutation guard + network-first SW with no data cache + persisted read cache with alert bar. The app is deliberately **not** offline-first for writes.
- **Unknown/zero behaviors (catalogued):** zero-price order blocks conversion; zero-amount expense/purchase/receivable rejected (positive); `costNature` NULL ≡ variable (indistinguishable in filters); zero-deposit orders skipped in liability sum (`reports/actions.ts:788`); no-in-movement manual out → COGS 0 (`inventory/actions.ts:481-483`); zero-opening stock → movement not created; depreciation 0 in start month; IC-12 WARN (not FAIL) on negative stock.
- **Correction/reversal map (inverse functions):** convertOrderToSale ↔ reverseSale; forfeitDeposit ↔ reverseDepositForfeiture; create/update → re-derive dependent movements; delete → soft-delete + linked movements; refundOrder (liability-only, one-way, capped); updateCapitalAsset/deleteCapitalAsset (read-time re-derivation); NO inverse for manual write-off (م-5).
- **Exit/back/cancel:** modals are ResponsiveModal (dismiss = cancel, draft retained); destructive actions use ConfirmDialog with explicit consequence text; orders tab back via header; cancel-vs-final-cancel distinction in OrderDetail (`:981,1056`).

---

## 6. Disagreements with the prior capability map (verified sample)

The 2026-09-03 map (`repos/Documents/reports/2026/2026-09-03/.../01-zaman-capability-map.md`) was re-verified item-by-item. It is overwhelmingly accurate (24/24 capabilities exist; the data-model inventory, routes, migration list 0000–0028, IC inventory, and financial-rule summary all match the code). Differences found:

1. **ZC-06 — forfeiture sale `source` value (prior map WRONG):** the map states forfeitDeposit "creates a sale **(source order)** via a settlement path". Code inserts `source: "manual"` (`finance/actions.ts:2154`). The repo-root `ACCOUNTING_RULES.md` rule 4 also specifies `source='manual'`. Impact: low (unique partial index semantics are the same), but any transfer spec copying "forfeiture sale source='order'" would be wrong.
2. **ZC-17 — catalog delete semantics (prior map WRONG at implementation level):** the map claims "delete = hard delete with ConfirmDialog … (catalog only)" and repeats it as an open question. The server action is a **soft delete** (`catalog/actions.ts:173-176` sets `deleted_at`), even though the UI comment (`CatalogClient.tsx:270-271`) and ConfirmDialog (`:303-326`) say «حذف نهائي / لا يمكن التراجع». The truth: soft-deleted in DB, presented as permanent, no undo. The prior map trusted the UI comment; the code disagrees with the comment.
3. **ZC-01 — stale header comment (minor):** the map describes four modes correctly; the file's own header still says «ثلاثة أوضاع» (`SmartFinanceForm.tsx:6-9` vs `:47-54`). Documentation-level nit only.
4. **Migration count (task brief, not the map):** the brief said "44 migrations"; actual = **29** (journal-verified). The prior map's "29 files 0000–0028" is correct.
5. **Confirmed matches worth noting (sample re-verified):** deposit-transform reclassification (`finance/actions.ts:1549-1576`), INV-4 remainder posting (`:1123-1132`), write-off guards (`:819-828`), IC-12 FAIL/WARN semantics (`integrityCheck.ts:1165-1183`), transfer pair (`:3153-3175`), audit userId="owner" security rationale (`audit/actions.ts:29-37`), backup non-restorable warning (`BackupModal.tsx:101-108`) — all exactly as the map describes.

---

## 7. Zman's financial constitution as implemented (evidence-backed)

1. **Cash-basis core — `cash_movement` is the single source of cash truth (INV-1).** Every event writes exactly one movement: expense (`actions.ts:744-754`), purchase, sale (`:1134-1144`), deposit (`orders/actions.ts:144-157`), owner draw/inject, opening (`:3596-3671`), receivable/payments, transfer pair. Aggregates always filter `deleted_at IS NULL` (partial indexes throughout `finance/db.ts`).
2. **One movement per cash event; transfers are a pair (INV-2).** Shared generated `transferId` on out+in (`finance/actions.ts:3153-3175`); net-zero by construction; IC-8 reconciles ledger vs source tables.
3. **Deposit is a liability, not revenue (INV-3/4).** Held on the balance sheet for undelivered orders (`reports/actions.ts:780-793`); converted at delivery by **reclassification** not double-posting (`finance/actions.ts:1549-1576`); refunds capped at the original collection (`:1895-1912`); forfeiture books only the unrefunded remainder as a `manual` sale with **no new cash movement** (`:2150-2175`); settlement lifecycle guarded by IC-3/4/16.
4. **LOCKED-6 — exactly one profit definition.** `computeOperatingPnl` (`pnl.ts:122-290`) with formula `sales − operatingExpenses − operatingPurchases − COGS − writeOff − depreciation` (`:272-278`); three display entry points call it; IC-13 cross-checks two periods and FAILs on drift (`integrityCheck.ts:1240-1315`); `computeCashBasisPnl` is a thin wrapper (`reports/actions.ts:58-88`). The repo carries an explicit rejected-branch warning against injected mock financials (CLAUDE.md §1:108-122).
5. **Exactly three read-time non-cash adjustments** (all inside `computeOperatingPnl`): COGS from `catalog_movement` outs (`pnl.ts:209-222`), inventory write-off from flagged expense rows (`:224-237`), period depreciation from `capital_asset` (`depreciation/queries.ts:83-127`). Nothing else touches profit outside cash movements + these three.
6. **Soft-delete is the only delete (INV-5).** Every table (except `idempotency_key`, `message_template`, `audit_log` append-only) has `deleted_at`; even catalog "permanent" delete is soft in the action (§6.2). Corrections = re-derive + reclassify + explicit inverse actions, never history rewrites; cut-over policy protects old months (CLAUDE.md §7).
7. **Equity equation and drift discipline.** `totalEquity = openingCashInEquity + injections − drawings + retainedProfit − capitalAdditions` (`reports/actions.ts:923`); `retainedProfit = salesCashIn − deposits − operatingCashOut − COGS-to-date − writeOff-to-date` (`:913-918`); `equityDriftCents = (assets − liabilities) − equity` must be 0 (`:927-929`); assets include inventory value (`:733-749`) and receivables (`:752-776`); the only liability is held deposits (`:793`). IC-1 shares the exact drift definition (`integrityCheck.ts:128-136`).
8. **Integer fils money (INV-16).** Storage in fils; micro-fils purchase precision with a `GENERATED ALWAYS` total that is never hand-written (`finance/db.ts:34-42`); `formatFilsToJod` the only formatter (`money.ts:15-20`); IC-7 guards unit consistency.
9. **Two declared profit numbers (D3 rule):** operating profit (after depreciation) vs cash-retained profit (before depreciation); a third number is forbidden; the difference is displayed as its own card.
10. **Selective inventory as an explicit INV-1 exception (INV-23/24).** Tracked purchases capitalized (excluded from `operatingPurchasesCents`, `pnl.ts:185-200`), COGS at sale; untracked items purely operational; negative stock allowed with documented warning.
11. **Write-off as non-cash dual entry (INV-25).** Movement + shadow expense, no cash movement, keeps IC-1 = 0; rows guarded immutable.
12. **Depreciation non-cash, read-time (INV-22).** Never in `cash_movement`; floor + last-month sweep; `startedAt = purchaseDate`; amount immutable after creation.
13. **Receivables never touch P&L.** Separate tables; balance-sheet asset; IC-15.
14. **Operational guardrails:** rate-limited + idempotent writes (`idempotency_key` + `requestId` on every mutation), row locks (`FOR UPDATE`), optimistic concurrency (`updatedAt`), audit outside transactions that never fails the caller, Amman-timezone dates (`getAmmanDate`, `src/lib/utils.ts`) to avoid UTC month-boundary drift, fail-closed auth, and a runnable 16-check invariant suite as the enforcement mechanism of the whole constitution (`runFinancialIntegrityCheck`, integrityCheck.ts:65-122).

---

## 8. Transfer-readiness note for the Group 6 audit

For every ZC above, the inverse-function map (§5) and the financial constitution (§7) are the two artifacts Micro cannot re-derive from UI inspection alone. The specific audit-brief capability (project/shared allocation) is **absent by design** in Zman — Zman's model allocates *time* (depreciation) and *category* (classification), never *cost objects*, so Micro's allocation requirements must be designed fresh against the Zman constitution (single profit function, one-movement-per-event, soft-delete, drift discipline).

*End of SA-1 report. Built entirely from read-only inspection of zman-app @ bdd63ab.*
