# Zman-to-Micro Capability Gap Analysis and Transfer Design

| | |
|---|---|
| **Report ID** | zaman-to-micro-gap-analysis-001 |
| **Date** | 2026-09-03 |
| **Analysis type** | One-way comparative discovery and transfer design (Zman → Micro) |
| **Source product (read-only)** | Zman — `github.com/Qays7753/zman-app` · `main` @ `bdd63ab` — app in `artifacts/zman-app` (Next.js 15, Drizzle/Postgres, Arabic RTL PWA) |
| **Target product (read-only)** | Micro — `github.com/Qays7753/Micro` · `main` @ `4db6a5f` — app in `apps/prototype-web/client` (Vite React PWA, offline-first, Arabic RTL), domain in `src/domain`, state: schema 30 / export 22 |
| **Analysts** | Five specialized read-only sub-agents (SA-1…SA-5) + parent consolidation; full sub-agent reports delivered alongside this report in `subagents/` |
| **Repositories modified** | **None.** Micro and Zman were strictly read-only. This report is delivered to the Documents repository only. |
| **Terminology note** | The product/repository name is **Zman** (`zman-app`). The task brief misspelled it as "Zaman"; the repository URLs are authoritative. The delivery folder name `zaman-to-micro-…` follows the task's prescribed path verbatim. |

---

## 0. Executive Summary

This analysis inspected both products at their current remote `main` states, reconstructed every Zman capability from its actual code (24 capabilities, ZC-01…ZC-24), classified the Micro equivalents (21 gap findings, MG-01…MG-21), designed the transfer of every serious candidate (17 final transfer findings, TR-01…TR-17), and rejected — with documented financial-truth reasons — everything that would violate Micro's product identity or financial rules.

**The headline results:**

1. **Micro is already stronger than Zman in 7 of the 18 compared capability areas** (cost calculation, catalog/units, orders lifecycle, wallets/cash continuity, opening balances, parties ledger, export/import). These are *reverse gaps*: a Zman owner moving to Micro gains capability. Any report that lists them as Micro gaps would be false — the false-gap register in §Output B exists to prevent exactly that.
2. **The real gaps are concentrated in "trust and share," not in bookkeeping mechanics.** Micro cannot (a) prove its own numbers to its owner with one tap (Zman's 16-check integrity suite, `فحص الآن`), (b) hand an accountant/family a period document (Zman's Markdown reports), (c) answer «شو صار على البنزين؟» with named expense groupings, or (d) answer «شو صار اليوم؟» in one place.
3. **The deepest transfer is architectural, not visual:** Zman's LOCKED-6 discipline — one canonical profit function plus a runtime cross-check that fails on drift — is the single highest-value pattern Micro can adopt (TR-01), and it *strengthens* Micro's bounded-profit boundary rather than weakening it.
4. **The most seductive Zman capabilities are precisely the ones that must be rejected.** Zman's auto-deducting selective inventory, order→sale conversion with deposit reclassification, and dual-entry write-off are genuinely excellent engineering — for Zman's server-side, single-ledger, revenue-as-sale model. Porting them into Micro's event-sourced, evidence-first, append-only model would create inventory effects from estimates, mutate past cash events, and convert unknowns into zeros. All three are rejected with evidence (TR-12, TR-13, and the mechanics half of TR-06/TR-17); only their *edges* — a purchase→receipt bridge, visibility rows, written laws — transfer.
5. **One capability was discovered that no Round-1/2 analyst registered:** Zman persists unsaved form input to localStorage and offers it back after a crash (DRAFT_KEYS). Micro has no editor-level draft persistence (verified by grep; only Setup keeps a draft). This becomes TR-11.

**Final ranked transfer set:** **P0** — TR-01 «قراءة الفترة الواحدة» (canonical period-result function + cross-surface check) and TR-02 «فحص سلامة مالي» (owner-facing integrity self-check). **P1** — TR-03 «شارك الكشف» (statement export artifact), TR-04 «تصنيفي للمصاريف» (free-tag expense classification, the only accepted schema change: 30→31 / export 22→23), TR-08 «قوانين الأثر والثبات» (written interaction laws). **P2** — TR-05 activity layer, TR-06 waste-visibility rows, TR-07 inventory edges, TR-09 undo-delete/paste helpers, TR-10 snippets (owner-gated), TR-11 editor draft persistence. **Reject** — TR-12…TR-17 with binding reasons.

Nothing in this task modified Micro or Zman. This is a design handoff only.

---

## 0.1 Methodology and Source-of-Truth Rules

- **Current remote state only.** Both repositories were cloned anonymously from their public URLs and analyzed at `main` (`zman-app` @ `bdd63ab`, `Micro` @ `4db6a5f`). No memory, prior bridges, or historical screenshots were used as evidence. Where a prior conversation's artifact (the Documents repo's 2026-09-01 Micro target-state design report) exists, it was *not* treated as implementation truth — only the live `main` trees are.
- **One-way comparison.** The direction is strictly Zman → Micro. Micro-only capabilities were catalogued only far enough to avoid false gap claims; they are neither redesign candidates nor transfer candidates. The seven reverse-gap areas are documented as warnings, not as work items.
- **Evidence-first.** Every material claim in this report cites an exact repository path (component, service, domain type, migration, or contract doc). Claims that could not be verified in code are labeled `INFERENCE` with the uncertainty stated. The five sub-agent reports (delivered in `subagents/`) carry the full evidence index for each layer: `01-zaman-capability-map.md`, `02-micro-gap-comparison.md`, `03-workflow-mobile-ux.md`, `04-financial-data-integrity.md`, `05-transfer-architecture-review.md`.
- **Contradiction resolution.** Round-1 rankings (source-side richness) conflicted with Round-2/3 financial and UX verdicts on four capabilities. SA-5 re-verified each contested claim directly in both codebases and issued binding resolutions, which the parent agent re-checked against the underlying evidence before adopting them here. The resolutions are recorded in §Output F and in `05-transfer-architecture-review.md` §1.5.
- **Effort allocation** followed the task brief: ~20% establishing the two baselines (§1), ~80% Zman extraction, gap identification, and transfer design (§Outputs C–H).
- **No external research was needed** for any binding decision; all decisions rest on repository evidence plus Micro's own documented rules. External best-practice material was deliberately not consulted, per the instruction that generic benchmarks must not override actual product behavior.

### 0.2 Non-negotiable Micro constraints used as transfer filters

Every transfer proposal in this report was tested against these constraints (verified implemented in Micro's code, not just documented):

1. Arabic RTL, mobile-first, **offline-first** (IndexedDB via `PrototypeLocalStore`; no cloud/auth/sync on `main`).
2. Five bottom-nav seats (`مشروعي الآن` / `سجّل` FAB / `العمل` / `مالي` / `أدواتي`), top bar for settings, centered recording FAB (`QuickActionSheet`).
3. JOD 2 decimals, English digits, `DD/MM/YYYY` dates (Group 6 item 5 — systemic across 17 routes).
4. Honest separation of physical cash, Amanah, receivables, owner money, period result, and unknown openings; **missing ≠ zero** (`resultStatus` / null-on-unknown discipline).
5. Estimates and cost calculations never create financial or inventory effects (CostEstimate is a "thinking tool"; `CostSnapshot` carries knowledge states).
6. Optional product selection during sale without forced inventory (`DirectSale.catalogItemId?` optional; inventory is opt-in with dated activation).
7. Traceable, atomic, idempotent corrections with before/after visibility (`CorrectionPreview`, 11-kind history, per-intent idempotency keys, `commit*` atomic transactions).
8. Bounded final profit: no "صافي الربح النهائي" when cost data is missing, stale, or changed.

---

## 1. Product Baselines (the 20%)

### 1.1 What Zman is

Zman is a single-owner (workshop/plant-nursery, "Zman Greens JO") Arabic-RTL financial + order-management PWA, used ~95% of the time on a 360–390px phone (`CLAUDE.md` §10). Its core promise, in the owner's words, is **"one profit number the owner can trust."**

- **Stack:** Next.js 15 App Router + React 19, Drizzle ORM + Postgres (Supabase), TanStack Query, react-hook-form + Zod. The deployed app uses Server Actions only — the repo's `artifacts/api-server` (Express) and `lib/api-*` packages are parallel artifacts *not used by the app* (verified: no imports). `artifacts/mockup-sandbox` is a shadcn preview gallery, not a product surface.
- **Financial model:** cash-basis ledger (`cash_movement` is the single source of cash truth, INV-1) plus exactly **three read-time non-cash adjustments**: COGS (from the inventory ledger), inventory write-off, and depreciation. Soft-delete is the only delete (INV-5); all aggregates filter `deleted_at IS NULL` (INV-6). The financial constitution is `artifacts/zman-app/docs/ACCOUNTING_RULES.md` (INV-1…INV-25), enforced at runtime by a 16-check integrity suite (IC-1…IC-16, `فحص الآن` on `/reports`).
- **Money:** integer fils (1 JOD = 1000 fils, 3 decimals, `formatFilsToJod`); `parseJodToFils` accepts Eastern-Arabic numerals and strips «د.أ»/«JOD»/«دينار» on paste.
- **Offline behavior:** server-backed, network-first. The only offline artifacts are in-form localStorage drafts and the 5-second undo-delete grace window. Offline submits are blocked with an Arabic toast (`assertOnline`).
- **Auth:** single shared passcode, 8h cookie, fail-closed middleware, 10-minute idle lock.
- **Data model (feature `db.ts` files + 29 migrations):** `purchase`, `expense`, `sale`, `account`, `cash_movement`, `owner_transaction`, `opening_balance`, `receivable(+payment)`, `order(+order_component)`, `catalog_component` (with `tracked` flag), `catalog_movement` (inventory ledger), `capital_asset`, `audit_log`, `snippet`, `message_template`, `idempotency_key`, plus two managed pick-list catalogs (`expense_category_catalog`, `purchase_item_catalog`).
- **Navigation:** 6-item desktop sidebar; mobile bottom bar = first 4 (الرئيسية/الطلبات/المالية/المخزون); everything else in a grouped "More" sheet (المتابعة والتحليل: التقارير، الملاحظات، الأصول، سجل النشاط · الإدارة المالية: الأرصدة الافتتاحية، الحسابات، أصناف الشراء · المراجعة والأمان: سجل التدقيق).

### 1.2 What Micro is (current `main`)

Micro is a delivery-final local-first financial and operating system for Jordanian home-based micro businesses, implemented as an Arabic RTL phone-first PWA (Vite + React + wouter), with a strict layering: React page → Application service → Domain (`src/domain`, 12 modules) → `PrototypeLocalStore` → IndexedDB (26 stores). No UI touches IndexedDB directly; collection flows pass the owning service then the single `distributeUnallocated` allocation path with operation keys.

- **State (verified `docs/operations/current-state.md`):** Groups 1–6 merged through PR #148; schema 30 / export 22; 42 routed page components; 16 domain test files + 533 prototype tests; full verified export/import with migration chain; PWA offline verified in live QA; device acceptance and human Pilot are the only next steps.
- **Financial events (exactly 8 types)** with declared five-delta effects `[cash, payable, ownerCapital, operatingExpense, amanah]`: owner investment/withdrawal, operating expense (cash/payable), payable settlement, amanah held/released, non-cash loss. **Amanah can never appear as profit by construction** — it lives in its own delta column.
- **Cash continuity:** multi-wallet (cash drawer / bank / digital / other), opening known/**unknown** («غير محدد بعد» — never zero), transfers, adjustments, cash count (future-effect-only settlement), unallocated-cash allocation/coverage with `sourceRef` links.
- **Orders:** 10 statuses + settlement statuses (incl. `needs_review` gating, `cancelled_pending/refunded/retained`), event log with `price_revised`/`collection_reversed`, deposits with explicit settlement decisions, agreement source + follow-up. Revenue is recognized **on the order** at `delivered`/`settled` (F-005); there is deliberately no convert-to-sale.
- **Corrections:** 11-kind unified history, `CorrectionPreview` before every correction, atomic replacement/restore, mandatory reasons, per-intent idempotency keys, live idempotency (triple-tap = one write).
- **Deliberately stopped on `main`** (from current-state.md §5 and `docs/decisions/remaining-capabilities-review-v1.md`): no new financial slices without an owner decision + contract; no Market/Delivery UI; no Activity Profiles; no POS/Auth/Sync/Cloud/CRM/WhatsApp/taxes/AI; assets & depreciation, loans, payroll, taxes, partial returns, forecasts are *deferred behind specialized contracts* («لا نخمن قواعدها»); never-build list includes full CRM, WhatsApp automation, general retail POS.

These baselines were established only as deeply as needed for accurate comparison; the remainder of this report is Zman extraction and transfer design.

---

## Output A — Zman Complete Capability Catalogue

Every meaningful Zman capability discovered, with where it is reachable, what it does, what it affects, and its evidence source. (Deep evidence per capability: `subagents/01-zaman-capability-map.md`.)

| ID | Capability (Arabic · English) | Where reachable | What it does & affects | Key evidence (`artifacts/zman-app/`) |
|---|---|---|---|---|
| ZC-01 | نموذج الإدخال المالي الموحّد · SmartFinanceForm | FAB on `/finance` payments tab; `?editExpense=`/`?editPurchase=` | One modal form, 4 modes (مصروف يومي/شراء مواد/أصل للورشة/دَين لشخص), each with a one-line **profit-impact hint before any field**; per-mode minimal field sets; derived unit cost (micro-fils); drafts in localStorage; double-submit lock; idempotency key; audit log | `src/features/finance/components/SmartFinanceForm.tsx` (1392 lines; hints 854–863) |
| ZC-02 | فئات المصاريف · Expense categories & 2-dimension classification | Category select in expense mode; «إدارة الفئات»; `?category=` filter | Flat name catalog with **lazy auto-enrollment** of hand-typed categories (trimmed, never blocks save), seed-on-read defaults, orphan-merge filter vocabulary; classification = `isCapitalAsset` × `costNature(fixed/variable)` × `isInventoryWriteoff`; category drives P&L distribution + filtering, zero money effect by itself | `finance/actions.ts` (678–783, 2560–2790), `finance/queries.ts:902`, `FinanceCatalogModal.tsx` |
| ZC-03 | مدفوعاتي · Unified payments feed | `/finance` «المدفوعات» tab | UNION ALL of expense/purchase/receivable with cursor `(createdAt,id)` pagination, kind chips, search, per-kind card second lines, 5s undo-delete, next-page-failure protection | `finance/queries.ts:getPayments` (80–505), `PaymentsTab.tsx` |
| ZC-04 | المبيعات اليدوية · Manual sales | `/finance` «المبيعات»; FAB «مبيعات جديدة» | Cash income not from orders; deposit-netting rule INV-4 (sale posts `max(0, amount − deposit)`); unique partial index prevents double conversion | `SalesTab.tsx`, `SaleForm.tsx`, `finance/actions.ts:1069+` |
| ZC-05 | سير عمل الطلبات · Order lifecycle | `/orders` (bottom seat); list/calendar tabs; card status dropdown | draft→sent→confirmed→delivered/cancelled; deposit as liability; live profit summary labeled «متوقّع/مرجعي»; pre-delivery insufficient-stock warning (never blocks); delivered orders lock component edits | `orders/actions.ts`, `OrderForm.tsx`, `OrderDetail.tsx` |
| ZC-06 | تحويل الطلب لمبيعة · Order→sale conversion + deposit transform + inverses | OrderDetail buttons | Atomic conversion: sale = full realized; **deposit cash movement reclassified** (not re-posted); remainder movement; `deductForDelivery` in-transaction; full inverse set (reverseSale, refund capped at remaining, forfeitDeposit without new cash, reverseDepositForfeiture); IC-3/4/9/16 guards | `finance/actions.ts` (1441–2440) |
| ZC-07 | المخزون الانتقائي · Selective per-item inventory | `/catalog` tracked toggle; `/inventory` seat; purchase linking | Per-item `tracked` flag (default **off**); tracked purchases capitalized as inventory (excluded from operating profit) with exact-value `in` movements; delivery auto-deducts with **immutable weighted-average COGS**; negative stock allowed with note; untrack-with-stock requires stated-consequences confirm + soft-deletes history; opening stock at zero cost (documented trade-off) | `catalog/db.ts`, `inventory/actions.ts` (196–368), `CatalogClient.tsx` (569–679), ACCOUNTING_RULES §9 |
| ZC-08 | مكوّنات الطلب وحساب التكلفة · Order components cost build-up | OrderForm «مكوّنات الطلب» | Component rows from catalog (cost prefills as snapshot) or free text; per-unit × order qty; order-level additional costs; live expected profit with neutral «متوقّع» styling; stock-aware picker with warnings; **no financial/inventory effect at save** | `ComponentsEditor.tsx`, `OrderForm.tsx` (246–680) |
| ZC-09 | الربح التشغيلي الموحّد · LOCKED-6 single profit function | all profit surfaces | ONE `computeOperatingPnl` (sales − opExpenses − opPurchases − COGS − write-offs − depreciation) used by dashboard, reports, monthly panel; **IC-13 runtime cross-check** (3 sources × 2 periods) fails on drift; third profit number forbidden (D3) | `finance/pnl.ts`, `integrityCheck.ts:1240+`, `CLAUDE.md` §2 |
| ZC-10 | الأصول والإهلاك · Capital assets + read-time depreciation | Asset mode → DepreciationPromptModal; `/assets`; ⋯ on asset cards | `capital_asset` register; monthly = floor(amount/life); **read-time computed, no cash ever**; retroactive start; last-month sweep; P&L deducts period depreciation; balance sheet stays cash-basis (dual profit labels by design); stop = soft delete | `depreciation/*`, ACCOUNTING_RULES §10 |
| ZC-11 | الذمم المدينة · Receivables (cash loans to people) | SmartFinanceForm «دَين لشخص»; PaymentsTab «ديون» | Loan = cash out + receivable row (**asset, never expense, never P&L**); payments = cash in; remaining computed read-time; IC-15 reconciliation; settled loans stay visible | `finance/db.ts`, `actions.ts:3710+`, `PROMPT_RECEIVABLES.md` |
| ZC-12 | الحسابات والصناديق · Accounts, transfers, owner draw/inject | `/finance/accounts` (hidden tab) | cash/bank accounts; default cash box auto-created; transfer = out+in pair (INV-2); archive refused with non-zero balance (INV-13); owner transactions never touch profit | `finance/actions.ts:2790–3460` |
| ZC-13 | الأرصدة الافتتاحية · Opening balance (lock once) | `/settings/opening-balance` | Single row (goLiveDate, cash, bank, capital); writes `opening` movements; `isLocked` freezes; IC-11 reconciles | `actions.ts:3463–3682`, `OpeningBalanceClient.tsx` |
| ZC-14 | لوحة المعلومات · Dashboard bundle | `/` | Period-filtered cards (net profit after depreciation, cash, capital additions); alerts bar; compare panel; liquidity flow; monthly profit trend with educational tooltips («شهر الشراء قد يظهر خسارة وهذا صحيح»); upcoming deliveries; drill-down details layer; global search | `features/dashboard/*`, `PERF_03_BUNDLE.md` |
| ZC-15 | التقارير · Reports + financial position + downloads | `/reports` | 6 report types (P&L, expenses by category, sales, orders, products, balance sheet); period ranges; as-of balance sheet: assets = cash+bank+inventory+receivables; **held deposits are the only liability**; equity with capitalAdditions; `equityDrift` must be 0; per-section **Markdown downloads with UTF-8 BOM** | `reports/page.tsx`, `reports/actions.ts` (90–943) |
| ZC-16 | فحص السلامة المالي · Integrity check suite | `/reports` → «فحص الآن» | Read-only suite of **16 checks (IC-1..IC-16)** in parallel; overall PASS/WARN/FAIL; per-check Arabic title/description/drift/count/offender IDs/suggested fix; production evidence: 14 PASS / 1 WARN / 0 FAIL | `finance/integrityCheck.ts` (1608 lines), `IntegrityCheckReportPanel.tsx` |
| ZC-17 | الكتالوج · Material catalog | `/catalog` | name/default cost/unit/notes + tracked toggle + opening stock on first activation; per-item movement history; hard delete only here (RESTRICT if referenced) | `catalog/actions.ts`, `CatalogClient.tsx` |
| ZC-18 | شطب المخزون · Non-cash inventory write-off | `/inventory` FAB → quick adjust (out, value>0) | One transaction: movement out (weighted-avg) + **shadow expense** (`isInventoryWriteoff=true`, no cash movement); P&L line; gray read-only card in payments; **no reverse** (known gap م-5) | `inventory/actions.ts:551–575`, ACCOUNTING_RULES INV-25 |
| ZC-19 | سجل التدقيق · Append-only audit log | `/settings/audit-log` | action/entity/snapshot logged after commit, outside transactions, never throws, never persists the passcode; infinite list with entity icons and verb labels | `audit/*`, migration 0026 |
| ZC-20 | الملاحظات · Snippets library | `/snippets` | title/body/category; copy-to-clipboard; grouped; confirm delete | `snippets/*` |
| ZC-21 | رسائل واتساب · WhatsApp templates | Orders toolbar | Template with variables ({customerName} etc.); Jordan phone normalization to +962; alt-phone fallback; button hidden without valid number | `lib/whatsapp.ts`, `WhatsAppTemplateEditor.tsx` |
| ZC-22 | المصادقة والقفل · Passcode auth + idle lock + PWA | `/login` | Single passcode, fail-closed middleware, 8h cookie, 10-min idle lock (visibilitychange), SW network-first with safe update prompt | `middleware.ts`, `auth/*`, `pwa/*` |
| ZC-23 | النسخ الاحتياطي · JSON backup export | Backup modal | Client-side JSON of accounts/catalog/opening/assets/recent-100 orders + summary counts; **no import/restore path exists** | `components/shared/BackupModal.tsx` |
| ZC-24 | أنماط التفاعل · Cross-cutting mobile RTL UX contracts | everywhere | 5s undo-delete (timer commits, pagehide best-effort, online-guard); MoneyInput discipline + Eastern-numeral parsing; header stability laws (one row, no conditional filters, body chips flex-wrap); Action Dock matrix (one primary per status, gated secondaries); teaching empty states (3 steps + action); effect-explaining copy before every financial commit; 48px targets; logical RTL properties only | `lib/undo-delete.ts`, `lib/money.ts`, `docs/DESIGN_SYSTEM_V2_1_CONTRACT.md`, `docs/HEADER_*_CONTRACT.md` |

**Zman's financial constitution (distilled from `ACCOUNTING_RULES.md`, binding for the transfer design):** cash-basis ledger as single cash truth; one movement per cash event; transfers as pairs; deposits are liabilities; soft-delete only; expected numbers never styled as actual; capital excluded from operating profit; tracked purchases capitalized; COGS at sale with immutable stored cost; write-off as non-cash expense; depreciation read-time and opt-in; equity drift must be zero; single profit function (LOCKED-6) with runtime cross-check.

---

## Output B — Zman-to-Micro Gap Register

Only capabilities that are **absent, weaker, hidden, incomplete, or materially different** in Micro are registered here, with classification, evidence, user impact, and confidence. Micro-stronger areas appear afterwards as false-gap warnings (they are not transfer candidates and must not be reported as gaps).

| ID | Capability | Classification | Zman evidence | Micro evidence | User impact (Jordanian micro-owner) | Transfer suitability | Confidence |
|---|---|---|---|---|---|---|---|
| MG-01 | Expense classification & tracking | **MICRO-DIFFERENT** | `expense.category` + catalog + lazy enrollment (`finance/actions.ts:678–2790`) | `OperatingExpenseContext` relationship/behavior/purpose/knowledge (`src/domain/financial-event/types.ts:30-36`); no named vocabulary anywhere | Cannot answer «شو صار على البنزين هذا الشهر؟» — Micro asks truth-context questions but keeps no named grouping; grouping is manual note-reading | adapt → **TR-04** | high |
| MG-02 | Selective inventory / tracked items | **MICRO-DIFFERENT** | `tracked` flag + auto-movements + capitalized purchases (`inventory/actions.ts:196-368`) | Opt-in dated activation; deliberate per-material movements; nothing auto-deducts on delivery (`inventory-material/policies.ts`, `SupplierPurchaseEditor.tsx:303`) | Micro's model is deliberate and stricter; the friction is only the missing purchase→receipt bridge and zero-stock visibility | reject core / adapt edges → **TR-07 / TR-12** | high |
| MG-07 | Period result / P&L | **MICRO-WEAKER** (export artifact only — see note) | `pnl.ts` LOCKED-6; `/reports` P&L + balance sheet + downloads | On-screen `readRecordedPeriodResult` + `/finance/statement` with source links; **no exportable artifact** (`pages/Statement.tsx` — no download logic, verified) | The owner cannot hand an accountant/lender/family a period document; bounded-profit and no-balance-sheet are **design boundaries, not gaps** | adapt → **TR-03 / TR-01** | high |
| MG-08 | Finance integrity check | **ZAMAN-ONLY** | IC-1..IC-16 + «فحص الآن» panel (`integrityCheck.ts`) | No user-facing integrity surface; structural enforcement only (unique indexes, atomic commits, import verifier) | When a number "looks off," the owner cannot verify Micro's boundaries with one tap — trust is design-implied, never demonstrated | adapt → **TR-02 (P0)** | high |
| MG-10 | Assets & depreciation | **ZAMAN-ONLY** (deliberately deferred in Micro) | `capital_asset` + read-time depreciation (`depreciation/*`) | Deferred behind specialized contract (`docs/decisions/remaining-capabilities-review-v1.md:32`); `loss_non_cash` is the only hook | Machine/oven purchases cannot spread cost over life; real but rare for the persona | reject now / gated future → **TR-14** | high |
| MG-11 | Audit log | **MICRO-DIFFERENT** | Append-only `audit_log` of every create/update/reverse (`audit/*`) | Corrections-only traceability: 11 kinds + reasons + previews; ordinary creates are not in one chronological stream | "What did I change last week?" is answered for corrections but not for all records; single-owner local app makes this an accepted trade | adapt (merged into activity layer) → **TR-05** | medium |
| MG-12 | Activities feed | **MICRO-INCOMPLETE** | `/activities` unified feed with deep links (`activities/page.tsx`) | Pieces across 4+ surfaces: Home «ما تغير مؤخرًا» (missing direct sales, corrections, wallet entries; events link generically), EventsLayer, corrections layer, orders list | «شو صار اليوم/هالأسبوع؟» requires visiting 4+ surfaces | adapt → **TR-05** | med-high |
| MG-13 | Reports (filters, summaries, period) | **MICRO-WEAKER** | 6 Markdown report downloads + BOM (`reports/actions.ts:90-433`) | On-screen only; export exists only as full JSON backup | No shareable period artifact for accountant/lender/family | adapt → **TR-03** | high |
| MG-14 | Snippets/notes | **ZAMAN-ONLY** | `snippet` library + copy (`snippets/*`) | No snippet store in `storage/local/types.ts`; free-text notes exist per record | Repeatedly typing the same specifications/follow-up text — low severity, real daily friction for repetitive crafts | adapt (gated on persona validation) → **TR-10** | high (class.) / medium (value) |
| MG-15 | Dashboard | **MICRO-DIFFERENT** (identity choice) | Analytical panels bundle (`features/dashboard/*`) | Decision-first Home «الأهم الآن» (deliberate; `docs/product/placement-principles-v1.md`) | Not a defect — an identity choice; analytics partially covered by Finance period layer | reject (identity conflict) → **TR-17** | high |
| MG-16 | Auth/login | **NOT-A-TRANSFER-CANDIDATE** | Passcode + middleware + idle lock | No auth by design (offline-first local; OwnerProfile future-linking-ready) | None — adding auth would break the offline-first promise | reject → **TR-17** | high |
| MG-19 | WhatsApp integration | **NOT-A-TRANSFER-CANDIDATE** | Templates + phone normalization (`lib/whatsapp.ts`) | Never-build list (`remaining-capabilities-review-v1.md:33`) | Owner shares info manually — accepted product boundary | reject → **TR-17** | high |
| MG-20 | Global search | **MICRO-WEAKER** (deferred by SA-5) | `GlobalSearch.tsx` | Per-surface search only (Parties) | Finding an old record requires knowing its surface; bounded at persona scale | defer — Pilot observation only → **TR-16** | medium |
| MG-21 | Idle auto-lock | **NOT-A-TRANSFER-CANDIDATE** | `IdleLock.tsx` | No lock; device-level protection assumed | None today; revisit only after Pilot shows shared-device usage | reject (this phase) | high |

**New gap discovered during review (not in Round 1):** **MG-22 (TR-11) — in-form draft persistence** — MICRO-INCOMPLETE: Zman persists unsaved form input per mode (`SmartFinanceForm.tsx:339-359`, DRAFT_KEYS) and offers restore after a crash; Micro's editors persist nothing (grep-verified: only Setup keeps `micro.setup-draft.v1`), so a phone-browser refresh mid-entry loses everything the UnsavedChangesGuard cannot save. Confidence: high (gap) / medium (value).

### False-gap warnings (do NOT report these as Micro gaps — Micro is stronger)

1. **Catalog units & conversions** — Zman's unit is free text; Micro has dimensioned units + exact conversions + templates (`src/domain/catalog/types.ts`). Reverse gap.
2. **Wallets/cash management** — Micro adds digital wallets, unknown-opening honesty, unallocated-cash allocation/coverage, cash count, per-wallet ledgers with source links. Reverse gap.
3. **Export/backup** — Micro's export is full, verified, restorable with migration chain; Zman's is partial with no restore path (`BackupModal.tsx`). Reverse gap.
4. **Cost calculation** — Micro's deep calculator + saved estimates + knowledge states + price floor + safety buffer strictly exceeds Zman's order-component costs. Reverse gap.
5. **Orders workflow depth** — Micro's 10 statuses + settlement statuses + event log + needs_review gating exceed Zman's 5 statuses + conversion. Reverse gap.
6. **Customer/supplier visibility** — Micro's per-party ledger with movements + net position exceeds Zman's scattered personName fields. Reverse gap.
7. **Corrections/undo** — Micro's reversal/replacement system with reasons, previews, atomic commits, and 11-kind history exceeds Zman's undo-delete + soft-delete reversals. Reverse gap.
8. **Inventory write-off mechanics** — Micro's reasoned, reversible waste movement with context is the compliant stronger design; Zman's is immutable with no reverse. Reverse gap.
9. **Opening balances** — Micro's known/unknown honesty + later completion + guided import exceeds Zman's single locked row. Reverse gap.
10. **"Final net profit" absence is a boundary, not a gap** — Micro deliberately refuses to show a final number when cost knowledge is missing; any transfer that "fixes" this violates the product's core rule.

*(Counts across the 22 register rows: MICRO-DIFFERENT 4 · MICRO-WEAKER 3 (+1 deferred) · ZAMAN-ONLY 3 · MICRO-INCOMPLETE 2 · NOT-A-TRANSFER-CANDIDATE 3 · MICRO-SUFFICIENT (reverse gaps, documented as warnings only) 7.)*

---

## Output C — Deep Capability and Workflow Dossiers

A-to-Z dossiers for the serious transfer candidates. Each dossier is complete enough to implement from without reopening Zman; deeper line-level evidence lives in the sub-agent reports.

### C.1 TR-04 — «تصنيفي للمصاريف» (expense classification)

**1. Zman's capability (how it works from A to Z).** Entry: FAB «تسجيل جديد» on `/finance` → SmartFinanceForm mode «مصروف يومي» → category Select (from `expense_category_catalog` + «أخرى (إدخال يدوي)» free-text option). Fields: date (default today), category (required ≤200), amount (MoneyInput, fils >0), note (optional ≤1000). On save: row in `expense` + `cash_movement(out)` + idempotency key + audit row; the category is trimmed and **auto-enrolled** into the catalog inside the same transaction (`ensureExpenseCategoryInCatalog` — failure never blocks the save). Vocabulary in the filter = catalog ∪ `SELECT DISTINCT category` (orphan-merge) so historical names stay filterable. Management: `FinanceCatalogModal` add/rename/delete (rename does **not** rewrite history — a documented drift). Classification semantics: `isCapitalAsset` (never in operating profit), `costNature` fixed/variable (filtering only; hidden `?nature=` filter, no UI — known gap م-2), `isInventoryWriteoff` (read-only gray card). P&L groups expenses by raw category text (donut). Corrections: `updateExpense` re-derives the cash movement and preserves classification; delete = soft delete + 5s undo.

**2. The exact Micro gap.** Micro's `OperatingExpenseContext` records relationship (project/shared), behavior (fixed/variable/mixed/unknown), purpose, knowledge, and shared-project share modes — a *decision-context* model, deliberately without named vocabulary. The statement splits project/shared/unallocated/legacy. There is no label the owner can group by, and no per-category summary anywhere. User problem: «شو صار على البنزين؟».

**3. The adapted Micro design.**
- **Micro name:** «تصنيفي للمصاريف» — a *tag*, never "account categories" (no accounting jargon).
- **Owner:** مالي → the existing `FinancialEventEditor` `/finance/new/operating_expense_*` secondary `<details>` layer («أضف سياقًا للمصروف», G22 pattern) — an optional single field «تصنيفك (اختياري)» with datalist suggestions from previously used tags. Surface type: inline field, not a new page, not a catalog modal.
- **Data contract:** `OperatingExpenseContext += { categoryLabel?: string | null }` — ≤80 chars, trimmed, internal whitespace collapsed; **frozen on the event like the note** (immutable per event; corrections go through documented replacement). Suggestions = derived DISTINCT list over active operating-expense events (derivation *replaces* Zman's lazy enrollment offline; orphan-merge is inherent). No managed catalog, no new write-path store in v1. **Zero effect on any of the five deltas, `sharedProjectShare`, or resultMinor.**
- **Where it pays off:** `/finance/statement` gains a collapsed-by-default «مصاريفي حسب تصنيفي» block (per-tag totals with source links, same `StatementLineRow` pattern); optional EventsLayer tag filter.
- **States:** empty («ما في تصنيفات بعد…»), offline (unchanged — all local), unsaved (existing UnsavedChangesGuard), edit (label change = documented replacement, only if the owner asks later), success (grouping appears next statement read).
- **Safe return:** no new route; `?from` unchanged. QuickActionSheet quick-expense stays field-free (verified: amount+note+wallet today — keep it minimal).
- **Migration:** schema **30→31**, export **22→23**; import defaults `categoryLabel→null` for older snapshots (precedent: `amanahDeltaMinor ?? 0`); no backfill — legacy null = «غير مصنّف», already surfaced honestly as `legacyUnclassifiedExpenseCount`.
- **Rejected Zman elements:** managed catalog + CRUD modal (a repair for a polluted seeded server system Micro doesn't have); rename/merge tools (silent history rewrite — only ever per-event documented replacement); any recurring/auto-write rules.

### C.2 TR-02 — «فحص سلامة مالي» (integrity self-check suite)

**1. Zman's capability.** Entry: `/reports` → IntegrityCheckReportPanel → «فحص الآن» (secondary button, loading state «جارٍ الفحص...»). 16 read-only checks run in parallel server-side. Result: overall banner (PASS/WARN/FAIL, `summaryAr`, as-of date, run timestamp) + toast + 16 result cards, each with status icon, Arabic title, status badge, description, drift line («الفارق: X»), violation count, collapsible offender IDs, and a suggested fix rendered as an italic action hint. The panel's InfoTooltip promises: «الفحص آمن ولا يُغيّر أي أرقام — يقرأ فقط». Production evidence: 14 PASS / 1 WARN / 0 FAIL. Fixes happen elsewhere — the check only points.

**2. The exact Micro gap.** Micro enforces integrity *structurally* (single write path, unique indexes, atomic `commit*` transactions, import-time relation validation) but has **no owner-facing surface**: nothing lets the owner press "check my numbers." Import/restore is already shipped and user-reachable (`localTransferService.ts:2144 replaceSnapshot` + Settings wiring), and local-first means only the app can catch corruption — this is why the suite is P0.

**3. The adapted Micro design.**
- **Micro name:** «فحص سلامة مالي». Copy contract borrowed verbatim: «يقرأ أرقامك ولا يغيّر شيئًا».
- **Owner:** **أدواتي** (primary) → new surface route `/tools/integrity` (route kind `surface` — a reader that keeps bottom nav, matching the seat's «احسب قبل أن تلتزم» thinking-tool identity and the Calculator's zero-effect precedent); **secondary doorway:** text-action in مالي's truth section next to عدّ الصندوق (where doubt is felt). Canonical fallback `/tools`.
- **Screen contract:** header (back + «فحص سلامة مالي» + one-line promise) → decision card (overall status + run timestamp + «افحص الآن») → check cards (Arabic title + status + explanation + drift where meaningful + **«وين المشكلة» per-record deep links** — stronger than Zman's raw IDs — + suggested next action as a text-action to the fixing surface). States: empty, loading, PASS, WARN, FAIL, re-run after fixes. **Zero writes; last-run persisted as a derived cache, not a store.**
- **The Micro invariant set (MIC-1..MIC-10, corrected by SA-5):**
  - MIC-1 period-result cross-surface consistency (requires TR-01; null is a value — all surfaces must agree on «غير متاح + أسباب»; drift > 0 → FAIL);
  - MIC-2′ cash structure: unallocated cash ≥ 0 read-back; per-wallet balance ≥ 0; every `transfer_out` has a matching `transfer_in`; every cash `reversal` references an existing, not-yet-reversed entry *(replaces SA-4's false MIC-2, which compared incomparable streams)*;
  - MIC-3 correction/reversal balance across all five families (events, cash, inventory, order collections, supplier payments) — every reversal references an existing active original; a reversal is never itself reversed;
  - MIC-4 allocation `sourceRef{Id,Kind,LineId}` integrity (reuse the import-verifier rules at runtime);
  - MIC-5′ order/sale collection consistency: `collectedMinor == Σ deposit_collected + Σ collection_recorded(not reversed) − Σ collection_reversed − Σ deposit_refunded`; direct-sale collected == its allocations *(corrected formula — SA-4's omitted deposit events/refunds)*;
  - MIC-6 pending deposit decisions: `cancelled_pending` + `needs_review` → WARN («قرار معلق، ليس خطأ»);
  - MIC-7 amanah ≥ 0 read-back (the write guard is application-layer; import/corruption can bypass it — exactly why the read-back exists);
  - MIC-8 inventory: positions ≥ 0; reversal refs valid + single-use; consumption/waste `orderId`/`purchaseId` exist;
  - MIC-9 knowledge honesty: final orders' `resultStatus` vs snapshot knowledgeGaps; direct sales with unknown cost (informational);
  - MIC-10 retained-deposit visibility (INFO): count + total of `cancelled_retained` — «قرار موثق، ليس إيرادًا بعد».
- **Excluded from v1:** waste-vs-`loss_non_cash` double-report warning (no linkage field → no reliable signal); archived-wallet check (no archive path exists — Zman's IC-5 analog is N/A).
- **IC-1..IC-16 mapping headline:** Micro structurally enforces 7/16 at write time; 7 map into the new runtime checks; 2 are N/A today (no archiving, no assets).

### C.3 TR-03 — «شارك الكشف» (statement export artifact)

**1. Zman's capability.** `/reports` → period toggle → per-section «تنزيل» buttons → server action returns Arabic Markdown → client wraps in a **Blob with UTF-8 BOM** → `report_<type>_<YYYY-MM-DD>.md` → toast. Six report types; the balance-sheet report renders the equation tables in Markdown.

**2. The exact Micro gap.** `pages/Statement.tsx` (verified) contains no download/share/export logic; the only export is the full-store JSON backup. The owner cannot hand anyone a period document.

**3. The adapted Micro design.**
- **Micro name:** «شارك الكشف» — an owner-language action, not "generate report."
- **Owner:** مالي → `/finance/statement` action group («حمّل الكشف نصًا») + a text-action in the Finance period-layer footer. No new route; no new page.
- **What it exports:** the **existing** `StatementReading` (the on-screen read model) rendered as Arabic **Markdown with UTF-8 BOM**, filename `micro-statement-<from>-<to>.md` (English digits, DD/MM/YYYY range), fully offline (local Blob; optional `navigator.share` text when the API exists).
- **Binding content rules (financial-truth):** every money line carries its knowledge state; `resultMinor` null exports as «غير متاح — بيانات ناقصة» **with reasons — never 0**; amanah wording preserved («كاش موجود، ليس مالك ولا ربحك»); corrections digest included; the truth lines («ما يعنيه هذا الكشف») are exported **verbatim** — Micro's honesty signature, which Zman lacks; header states generated-at + period + «قراءة من السجل المحلي»; **no «صافي الربح النهائي» wording; no balance-sheet equation claim** — a position *summary* may list components with the qualifier «قراءة مكوّنات، لا ميزانية محاسبية».
- **States:** loading (button disabled while reading), ready, success, failure + retry, offline (works — pure local read), empty (still yields an honest mostly-zero artifact with truth lines).
- **Not transferred:** Zman's dedicated reports page (Micro's statement + Finance layers are the reading surfaces); UNION-ALL feed pagination (server-scale); PDF (deferred to a documents pipeline if recipients reject Markdown).
- **Dependencies:** TR-01 (the export must reflect the canonical reading).

### C.4 TR-01 — «قراءة الفترة الواحدة» (canonical period-result function + cross-check)

**1. Zman's capability.** LOCKED-6: `computeOperatingPnl` is the only profit definition; all three display surfaces call it; **IC-13 re-derives the number from three independent display paths for two periods (current Amman month + all-time) and FAILs on any drift**; a third profit number is forbidden by the naming rule (exactly two declared: operating-after-depreciation and cash-retained-before-depreciation, difference shown as its own card).

**2. The exact Micro gap.** Micro has **two independent result-computing read paths** — `projectFinancialService.readRecordedPeriodResult` (Finance period view + insights) and `statementService` (statement result/cash lines) — plus Home position facts, with **no runtime cross-check** that they agree; drift is guarded only by tests.

**3. The adapted Micro design.**
- **Micro name:** «قراءة الفترة الواحدة» — an internal discipline, **no new screen**.
- **Designation:** `readRecordedPeriodResult` becomes THE canonical period-result function; every surface that shows a period number consumes it or cross-checks it; no page contains inline period arithmetic; a public-surface test locks the read API (pattern: `tests/domain/public-surface.test.ts`).
- **Cross-check:** recompute (a) canonical result from stores, (b) statement result line, (c) Finance period view values; drift > 0 JOD minor → WARN entry in the TR-02 integrity surface with both numbers (never auto-fix). **Null is itself a cross-checked value:** when `resultMinor` is null, all surfaces must show the same «غير متاح + أسباب» state (acceptance criterion).
- **What does NOT transfer:** Zman's formula (Micro's result is bounded, null-on-unknown, excludes nothing silently — the bounded-profit boundary is *strengthened*, never bypassed).
- **Schema impact:** zero. Priority: **P0** — the architecture is the precondition for MIC-1 and for a trustworthy TR-03 export.

### C.5 TR-07/TR-12 — المخزون الانتقائي (selective inventory: edges accepted, core rejected)

**1. Zman's capability.** Per-item `tracked` flag default OFF; enabling shows an opening-stock field (creates an `in` movement **at zero cost** — documented trade-off); tracked purchases auto-create `in` movements and are **capitalized** (excluded from operating profit); order delivery inside `convertOrderToSale` auto-deducts `out` movements with immutable weighted-average COGS; **negative stock allowed** with a warning note; untracking an item with stock requires a stated-consequences dialog («الرصيد الحالي N وحدة سيُعامَل كصفر… سيتم حذف سجل الحركات ناعمًا») and soft-deletes history. Safeguards: linking a purchase to a non-tracked item is rejected; capital+tracked combination rejected; delivered orders lock component edits.

**2. The exact Micro position.** Micro's inventory is opt-in *as a whole* (dated activation, القرار ٩), per-material, with deliberate consumption evidence (contracts 11/13), **non-negative positions enforced at write**, purchases affecting cash/payables only («لن يحوله Micro إلى تكلفة بيع أو مخزون حتى المرحلة التالية» — `SupplierPurchaseEditor.tsx:303`), and reversals-not-deletes. **The automation core is untransferable in principle** (four hard conflicts: inventory effects from estimates; explicit-evidence bypass; negative-stock tolerance; unknown→zero opening). Micro already implements the philosophy (optional selection, immutable written cost) *stricter*.

**3. What transfers (the edges).**
- **Purchase→receipt bridge:** text-action «استلم هذه المواد في المخزون» on the supplier-purchase record → `withFrom('/inventory/movement/receipt?purchase=<id>', '/suppliers/purchase/<id>')`; the receipt editor (which already takes a `purchaseId` select and already supports the `?order=` prefill pattern for consume) learns the `?purchase=` prefill. **A bridge, never automation** — the owner still records the receipt deliberately; prefill only, explicit save required. Add `?purchase` to the closed deep-link vocabulary + canonical fallback.
- **Zero-stock quiet strip** in `/inventory`: «مواد وصلت صفرًا: …» — a reading aid, never an alert system.
- **Stated-consequences dialog law** (Zman's untrack dialog as the template): reserved for any future Micro deactivation contract — name the current balance, name what future actions will see, name what happens to history. (Verified: Micro has no inventory deactivation flow at all today.)

### C.6 TR-05 — «آخر ما صار» / «سجل كل ما صار» (unified activity layer)

**1. Zman's capability.** `/activities`: one chronological feed (order/sale/expense/purchase) with type icon, bold title, timestamp, **signed amount (+/−/«—» for non-cash)**, and **every row deep-links to the record's editing surface with URL params** (`?view=`, `?editSale=`, `?editExpense=`…). Skeletons, error retry, empty state.

**2. The exact Micro gap.** Home's «ما تغير مؤخرًا» block (capped at 5) covers orders + drafts + financial events (linked *generically* to `/finance`) + schedules — **direct sales, corrections, and wallet entries are missing**, and event rows don't use the `?event=` focus parameter Finance already supports (verified `homeControlCenterService.ts:398-437`). No cross-record reader exists.

**3. The adapted Micro design (two tiers).**
- **Tier 1 (cheap, high confidence):** enrich the existing Home block's read model — add direct sales (recorded + revisions), corrections (labeled «تصحيح» with net effect shown honestly, dash-for-non-cash), wallet entries; make event rows link `withFrom('/finance?layer=events&event=<id>', '/')`. Keep the cap (5–7), same visual weight, below «مسارات مرتبطة فقط» — the decision-first principle is untouched.
- **Tier 2 (owner nod required):** «مزيد» text-action → full-screen read-only **«سجل كل ما صار»** reader at `/finance/activity` (route kind `surface`, مالي family — a reading task; canonical fallback `/finance`), built on one unified derived read service over existing stores (orders' events, directSales revisions, financialEvents, cashContinuityEntries, inventory movements, corrections), each row deep-linking to its focused record via existing params. Never a sixth seat, never a dashboard.
- **States:** empty (block hidden — current behavior), loading, per-row kind icons, honest amount semantics (dash for non-cash), source links. Zero writes; fixture-tested single service (read-model drift guard).

### C.7 TR-11 — «مسودة محفوظة» (in-form draft persistence) — NEW finding

**1. Zman's capability.** SmartFinanceForm writes per-mode drafts to localStorage on change (`zman_draft_{expense|purchase|asset|receivable}`) and offers restore via a banner on reopen (create-only; edit mode never offers a draft; discard/save clears the key).

**2. The exact Micro gap.** Grep-verified: no editor in Micro persists unsaved input — only Setup keeps `micro.setup-draft.v1` (removed on completion), proving Micro already knows the pattern. `UnsavedChangesGuard` warns on navigation; it cannot restore after a phone-browser refresh or crash.

**3. The adapted Micro design.** Per-editor localStorage draft keys written on change; restore banner on reopen (create mode only — Zman's rule); discard clears; save clears; **never auto-commits a record** (drafts are input, not records; not in schema/export). Rollout editor-by-editor (recommended first: the financial-event editor — longest form). Dual-state rule: drafts restore *input*; the guard governs *navigation* — no interaction between them.

### C.8 Supporting dossiers (compact)

- **TR-06 — «هدر مخزون — بلا خروج نقد» rows (P2):** Zman surfaces write-offs as gray read-only cards where money is read; Micro's waste lives only in `/inventory`'s movement log. Transfer = read-only rows in the EventsLayer/truth strip (amount + source link, dash convention, never styled as cash expense). Zero writes; rides TR-05's read model. **Micro's reversible waste mechanics stay untouched — Zman's immutable dual-entry is explicitly rejected.**
- **TR-08 — «قوانين الأثر والثبات» (P1, documentation):** codify as written review-gate laws: (1) effect-explaining copy before every financial commit, including the negative case («لا تُنشأ حركة نقدية جديدة…») and a loan-hint line on owner-withdrawal/expense editors («قرض شخصي؟ لا يسجل هنا»); (2) header anti-jitter law (no conditional rows above content; filters live in body chips, wrap never scroll); (3) OrderDetail status-driven action matrix documented as a contract table (one primary per state, gated secondaries, destructive separated); (4) teaching empty states (≤3 steps + direct action). Rejects: modal-over-page create/edit, fils/3-decimal display, ar-JO numerals, per-tab FAB labels.
- **TR-09 — helpers (P2):** 5-second undo-delete for **non-financial deletes only** (estimates today, snippets if built) — Micro's local writes make restore real, dropping Zman's online-guard complexity; **forbidden on financial records** (corrections path is stronger). Currency-label stripping («د.أ»/«JOD»/«دينار») in the paste path of `englishNumeric` (digit normalization already exists).
- **TR-10 — «ملاحظاتي المتكررة» (P2, owner-gated):** Zman's snippets as a local non-financial thinking-tool store (CostEstimate precedent) under أدواتي: title/body/category + copy-to-clipboard; optional «استخدم في» prefill for order specifications/agreement notes — **never prices** (binding guard). Build only after the owner validates the need; ideally bundle its store decision with TR-04's schema-31 bump.

*(Rejected dossiers — TR-12 selective-inventory automation core, TR-13 order→sale conversion + deposit reclassification + forfeit-as-revenue, TR-14 assets/depreciation now, TR-15 loan-out receivables now — carry full evidence-backed rejection rationale in Output F and in `subagents/05-transfer-architecture-review.md` §3.)*

---

## Output D — Screen, Navigation, and Information Architecture Transfer Map

Where each accepted capability lives in Micro, respecting the five-seat navigation, centered FAB, deep/surface route classification (contract 26), and safe return.

| Transfer | Micro name | Owning tab | Owning screen / surface | Surface pattern | Primary entry | Secondary entries | Safe return | Screen contract essentials |
|---|---|---|---|---|---|---|---|---|
| TR-01 | «قراءة الفترة الواحدة» | مالي | none — application layer | internal discipline | — | — | — | no screen; public-surface test + cross-check in TR-02 |
| TR-02 | «فحص سلامة مالي» | أدواتي | `/tools/integrity` (new) | **surface route** (reader keeps nav) | Tools module-states row «فحص سلامة مالي» | text-action in مالي truth section; auto-suggest after import/restore | `?from` + canonical fallback `/tools` | header + one-line promise «يقرأ ولا يغيّر» → overall verdict card → ≤10 check cards with per-record deep links and text-action fixes; states: empty/loading/PASS/WARN/FAIL |
| TR-03 | «شارك الكشف» | مالي | `/finance/statement` (existing) | **inline action group** | statement end «حمّل الكشف نصًا» | Finance period-layer footer action | n/a (no navigation) | export reflects on-screen reading line-for-line; truth lines verbatim; BOM; offline Blob |
| TR-04 | «تصنيفي للمصاريف» | مالي | `FinancialEventEditor` (existing) | **inline field in details layer** | «تصنيفك (اختياري)» field with suggestions | EventsLayer tag filter (optional) | existing editor `?from` | optional field; frozen per event; statement grouping block collapsed by default |
| TR-05 | «آخر ما صار» / «سجل كل ما صار» | مشروعي الآن + مالي | Home block (existing) + `/finance/activity` (new, tier 2) | **inline block + surface reader** | Home block | «مزيد» text-action; Finance truth-section text-action | reader `?from=/` with canonical fallback `/finance` | cap 5–7; per-kind icons; dash-for-non-cash; rows deep-link via existing `?event=` etc. |
| TR-06 | «هدر مخزون — بلا خروج نقد» | مالي | EventsLayer / truth strip | **read-model rows** | rows in events layer | Home recent block (via TR-05 tier 1) | `withFrom` to `/inventory` | amount + source link; never styled as cash |
| TR-07 | «استلم هذه المواد» + zero-stock strip | مالي | `/suppliers/purchase/:id` + `/inventory` | **contextual text-action + strip** | text-action on purchase record | zero-stock strip in inventory overview | receipt editor `?from` back to purchase | bridge hidden/honest when inventory inactive; prefill never auto-writes; `?purchase` joins closed vocabulary |
| TR-08 | «قوانين الأثر والثبات» | cross-cutting | docs/contracts + review gates | **documentation** | — | — | — | effect-copy rule, header law, action matrix, teaching empty states |
| TR-09 | «تراجع ٥ ثوانٍ» + paste helper | cross-cutting | components/forms + application/input | **component/helper** | estimate delete (and snippets if built) | — | — | non-financial deletes only; restore is real (local) |
| TR-10 | «ملاحظاتي المتكررة» | أدواتي | new module (if validated) | **module + deep editor** | Tools module-states row | «استخدم في» prefill (text only) | `?from` to `/tools` | copy-to-clipboard; never prefill prices |
| TR-11 | «مسودة محفوظة» | cross-cutting | deep editors | **restore banner** | editor reopen (create mode) | — | — | input only, never records; discard/save clears |

**Placement decisions resolved:** integrity suite → أدواتي primary + مالي doorway (thinking-tool identity; CashCount precedent); activity reader → `/finance/activity` in the مالي family (a reading task, not أدواتي's calculation identity); category tags → inline field inside the existing progressive-disclosure layer (90% quick-expense path untouched); statement export → action on the existing reader (no reports page). **New-route obligations:** TR-02 and TR-05-tier-2 register canonical-fallback rows; TR-07 adds `?purchase` to the closed deep-link vocabulary — all contract-26 changes in the same commits.

**What is NOT created:** no sixth seat, no "More" sheet, no dashboard panels on Home, no modal-over-page editors, no per-tab FAB labels — each would fragment Micro's finished navigation identity (evidence: `navigation.ts`, `BottomNav.tsx`, `routeClassifier.ts`, contract 26; Zman's alternatives documented in `subagents/03-workflow-mobile-ux.md` §5).

---

## Output E — Financial and Data Transfer Contracts

The proposed Micro behavior for records, relationships, event effects, corrections, idempotency, migrations, and auditability. All accepted contracts honor: single write path (page → application service → domain → store); atomic `commit*` for coupled writes; per-intent idempotency keys; import accepts older export versions; no silent history rewrite; estimates never create effects; missing never zero.

### E.1 Record contracts

| Contract | Record shape | Effects | Corrections | Idempotency | Migration |
|---|---|---|---|---|---|
| **TR-04 categoryLabel** | `OperatingExpenseContext += { categoryLabel?: string \| null }` — ≤80 chars, trimmed, whitespace collapsed; frozen on the event | **None** on cash/payable/ownerCapital/operatingExpense/amanah deltas, `sharedProjectShare`, or `resultMinor`. Grouping is a read-model concern | label immutable per event; future rename/merge only via per-event `commitFinancialEventReplacement` with reason (never a silent history tool) | inherits the event's idempotencyKey | schema 30→31 / export 22→23; import default null (precedent `amanahDeltaMinor ?? 0`); no backfill; lockstep: `normalizeExpenseContext` assertions, `validateSnapshot`, public-surface test, editor/statement tests |
| **TR-02 CheckResult** | `{ id: "MIC-*", titleAr, status: PASS\|WARN\|FAIL, detailAr, offendingIds?, deepLinks? }` — read-only; last-run = derived cache | **Zero writes** (store snapshot hash unchanged before/after run — an acceptance test) | n/a (fix actions deep-link to existing correction editors; **no auto-fix, ever**) | n/a | none (outside schema/export) |
| **TR-03 export artifact** | none (Blob) | pure read → local file; never re-imported as data | n/a | n/a | none; content rules binding (knowledge states, null wording, no final-profit, no equation) |
| **TR-05 activity rows** | derived row model over existing stores | zero writes; corrections rows labeled with honest net effect (dash for non-cash) | n/a | n/a | none |
| **TR-07 receipt bridge** | prefill parameter only (`?purchase=`) | **no auto-write** — inventory effect only on the owner's explicit movement record (purchase ≠ COGS preserved) | existing movement reversal path | existing editor keys | contract-26 vocabulary addition only |
| **TR-10 snippets** (gated) | local non-financial store (title/body/category) + copy action | zero financial/inventory effects | delete via undo-delete (non-financial) | unique indexes + operation keys on the new store | bundle with TR-04's schema-31 bump |
| **TR-11 drafts** | localStorage per editor key | none until explicit save — drafts are input, not records | n/a | n/a | none (outside store) |

### E.2 The retained-deposits open decision (surfaced, not solved)

Micro's retained deposit (`cancelled_retained`) is cash that is today **neither revenue, nor liability, nor amanah** — a documented decision with no accounting home. **No new event type is invented by this analysis.** The decision question formulated for the owner: «عند إلغاء طلب والاحتفاظ بعربونه: ماذا يعني لك هذا المبلغ؟ (١) مبلغ عاد إليك شخصيًا؟ (٢) إيراد مشروع عن فترة الإلغاء؟ (٣) حالة معلنة معلّقة؟» Until answered: interim wording rule «عربون محتفظ به — قرار موثق، ليس إيرادًا بعد» + MIC-10 INFO visibility. Any change requires a specialized contract (new event type or delta dimension) — an independent Micro decision, never a Zman transfer.

### E.3 Hard rejections preserving Micro's financial truth

1. **Auto-deduct inventory on delivery / auto-capitalization / negative stock / zero-cost opening stock / untrack-with-history-delete (ZC-07 core):** would create inventory effects from estimates; bypass consumption-evidence; break the non-negative invariant; convert unknowns to zero; suppress history. Micro's model is deliberately stricter.
2. **Order→sale conversion + deposit cash-event reclassification + auto forfeit-as-revenue (ZC-06):** a second revenue path vs F-005; mutation of past cash events vs append-only corrections; revenue from retained deposits vs collection≠profit and the no-guessing rule. Micro's three-option settlement + CorrectionPreview are the stronger UX and the compliant mechanics.
3. **Cash loan-out event type (ZC-11, now):** forcing loans through `owner_withdrawal` (corrupts owner capital) or `operating_expense` (corrupts profit) is the real hazard today — mitigated by wording only (TR-08 hint); the real fix needs a sixth delta dimension and its own contract.
4. **Immutable write-offs (ZC-18 mechanics):** no-reverse records violate traceable corrections; Micro's reversible waste stays.
5. **Anything that would let Amanah appear as profit, convert unknowns into zero, create duplicate events, force inventory, or bypass corrections:** none of the accepted contracts does (verified delta-by-delta above).

### E.4 Integrity invariants (MIC-1..MIC-10)

As specified in dossier C.2 — derived from Micro's own domain rules with SA-5's corrections (MIC-2′ structural cash checks replacing a false invariant; MIC-5′ full collection formula including deposit events and refunds; MIC-10 new retained-deposit INFO). Every check derives from a tested domain rule, never a heuristic; deliberate states render as WARN/INFO, not FAIL.

---

## Output F — Ranked Transfer Recommendations

### P0 — essential to professional completeness or financial safety

| ID | Micro name | Decision | Rationale (condensed table) | Depends on |
|---|---|---|---|---|
| **TR-01** | «قراءة الفترة الواحدة» | Designate `readRecordedPeriodResult` as THE canonical period-result function; all surfaces consume or cross-check it; null-on-unknown is a cross-checked value; public-surface test locks it | **User problem:** two independent read paths can drift; the owner could see different numbers on Finance vs Statement. **Evidence:** `projectFinancialService.ts:433-639` vs `statementService.ts` (independent). **Why this way:** architecture transfers, formula does not; strengthens bounded profit. **Trade-off:** cross-check scope must be like-for-like or it cries wolf. **Priority:** P0 — precondition for MIC-1 and trustworthy export. | — |
| **TR-02** | «فحص سلامة مالي» | Read-only surface `/tools/integrity` (أدواتي) + مالي doorway; MIC-1..MIC-10; per-record deep links; text-action fixes; auto-suggest after import/restore | **User problem:** no one-tap verification of Micro's boundaries — trust is design-implied, never demonstrated. **Evidence:** no integrity surface; import/restore shipped and user-reachable (`localTransferService.ts:2144`). **Why this way:** local-first means only the app can catch corruption; read-only = zero risk. **Trade-off:** false positives erode trust (mitigate: derive from tested rules; deliberate states = WARN/INFO). **Priority:** P0. | TR-01 |

### P1 — high-value workflow or discoverability improvement

| ID | Micro name | Decision | Rationale (condensed) | Depends on |
|---|---|---|---|---|
| **TR-03** | «شارك الكشف» | Markdown+BOM export of the existing `StatementReading` on `/finance/statement` (+ period-layer footer action); truth lines verbatim; no final-profit/equation claims | The one true MICRO-WEAKER gap: an artifact to hand an accountant/family. Zero writes, offline Blob, outside schema/export registries. Trade-off: Markdown readability (PDF later if recipients reject it). | TR-01 (sequence) |
| **TR-04** | «تصنيفي للمصاريف» | Optional `categoryLabel` + derived suggestions + statement grouping; free tags, no managed catalog in v1 | Answers «شو صار على البنزين؟» without touching a single delta or allocation boundary. The **only** accepted store change (schema 31 / export 23). Trade-off: label drift splitting totals (accepted, documented; Zman parity). | TR-03 for the statement-block surface (field itself independent) |
| **TR-08** | «قوانين الأثر والثبات» | Written laws: effect-copy (incl. «لا حركة نقدية» + loan hint), header anti-jitter, OrderDetail action matrix, teaching empty states | Nearly free; protects every future group from re-importing Zman's pre-contract mistakes (the exact failure mode Zman's own contract docs were written to stop). Trade-off: contract drift if review gates aren't enforced. | — |

### P2 — valuable, not required for the first implementation

| ID | Micro name | Decision (one line) | Depends on |
|---|---|---|---|
| **TR-05** | «آخر ما صار» + «سجل كل ما صار» | Tier 1 enrich Home's block (add direct sales, corrections, wallet entries; `?event=` focused links; cap 5–7); tier 2 `/finance/activity` reader (owner nod needed) | — (tier 2 needs owner nod + contract-26 fallback row) |
| **TR-06** | «هدر مخزون — بلا خروج نقد» | Read-only waste rows in EventsLayer/truth strip | rides TR-05's read model |
| **TR-07** | «استلم هذه المواد» + zero-stock strip | Purchase→receipt bridge (`?purchase=` prefill, explicit save) + quiet strip + reserved dialog law | contract-26 vocabulary addition |
| **TR-09** | «تراجع ٥ ثوانٍ» + paste helper | 5s undo-delete for non-financial deletes only; currency-label stripping | TR-08 (laws first) |
| **TR-10** | «ملاحظاتي المتكررة» | Snippets as a non-financial thinking-tool store — **owner-gated**; never prefill prices | owner validation; bundle store with TR-04's bump |
| **TR-11** | «مسودة محفوظة» | Per-editor localStorage drafts with restore banner (create-only) — the new finding | — |

### Reject — do not transfer (binding reasons)

| ID | Rejected capability | Reason (with evidence) |
|---|---|---|
| **TR-12** | Selective inventory automation core (auto-deduct, auto-capitalization, negative stock, zero-cost opening, untrack-with-delete) | Four hard Micro violations: estimates creating inventory effects; explicit-evidence bypass (contracts 11/13); non-negative invariant; missing≠zero. Micro already implements optional selection and immutable written cost stricter. Edges live in TR-07. |
| **TR-13** | Order→sale conversion + deposit reclassification + forfeit-as-revenue | Second revenue path vs F-005; cash-event mutation vs append-only corrections; auto forfeit-as-revenue vs collection≠profit. Micro's three-option settlement + CorrectionPreview are stronger. Laws preserved in TR-08. |
| **TR-14** | Assets & depreciation **now** | «مؤجل بعقد متخصص — لا نخمن قواعدها» (Micro's own decision doc). Pattern bank + gating condition preserved (read-time computation, sweep, two-step prompt, two-section visibility). The `loss_non_cash` hook is the only future entry point. |
| **TR-15** | Loan-out receivables **now** | Needs a sixth delta dimension + new event type = an independent Micro contract, not a transfer. Wording hint folded into TR-08. |
| **TR-16** | Global search (defer) + SmartFinanceForm-as-a-whole + unified feed/pagination | Search: bounded volumes + TR-05 covers recent-item finding — Pilot observation only. SmartForm pattern already present (QuickActionSheet modes + effect card); only draft persistence transfers (TR-11). Feed pagination is a server-scale solution with no local-scale value. |
| **TR-17** | Dashboard panels, auth/passcode/idle-lock, WhatsApp templates+automation, partial JSON backup, write-off dual-entry+immutability, fils/ar-JO numerals + modal-create | Identity conflict with decision-first Home; platform refusals (no auth/no cloud); never-build list; reverse gap (Micro's export/import is full+verified); Micro's reversible waste is compliant; numeric/deep-editor contracts are systemic rules. |

**Coherence check (passed):** nothing in P0 depends on an unaccepted P2; nothing rejected is silently depended on — ZC-07's edges → TR-07; ZC-06's laws → TR-08; ZC-18's visibility → TR-06; ZC-01's drafts → TR-11; ZC-03's feed ambition → TR-05; ZC-24's laws → TR-08/TR-09.

---

## Output G — Final Transfer Architecture

One coherent target design for adding the selected Zman capabilities to Micro later. Micro remains Micro: decision-first Home, bounded profit, five seats, offline-first.

### G.1 Reused from Micro as-is (zero modification)

- **The write path** (page → application service → domain → `PrototypeLocalStore` → IndexedDB) and its atomic `commit*` transactions — every accepted item either reads through it or adds a payload field through it; **none adds a second write path**.
- **The corrections system** (reversal/replacement records, reasons, CorrectionPreview, 11-kind history) — TR-04's label corrections, if ever requested, reuse `commitFinancialEventReplacement`.
- **`?from` navigation + contract 26** — every new surface registers a canonical fallback; TR-07 adds one deep-link vocabulary entry; nothing else changes.
- **Statement reading** (`statementService.read`) — TR-03 is a presentation function over it; TR-04's grouping block extends its read model.
- **QuickActionSheet** — untouched (5 actions, transitory philosophy, no tag field in the sheet).
- **Bounded-profit discipline** — TR-01 strengthens it (null becomes a cross-checked value); TR-03 exports it (truth lines verbatim); nothing ever claims a final number.

### G.2 The dependency graph (build order)

```
TR-01 (canonical function) ──► TR-02 (MIC-1 uses it) ──► TR-03 (export reflects the canonical reading)
                                                        │
TR-04 (tags: schema 31 / export 23) ◄── bundle decision with TR-10 (snippets store, if validated)
        └─ statement grouping block rides TR-03's surface
TR-08 (laws) ──► TR-09 (helpers follow the laws)
TR-05 (activity: tier 1 free-standing; tier 2 needs owner nod) ──► TR-06 (waste rows join the same read model)
TR-07 (inventory edges) — free-standing (contract-26 vocabulary addition)
TR-11 (draft persistence) — free-standing
```

Rationale for the spine: the canonical function must exist before the integrity check can cross-check it; the export must come before the statement grouping block so format conventions (BOM, truth lines, knowledge states) are fixed once.

### G.3 Migration and compatibility statement

- **Only TR-04 (and optionally TR-10) touch the store:** schema **30→31**, export **22→23**; import migration defaults `categoryLabel → null`; no backfill; lockstep updates: `normalizeExpenseContext`, `validateSnapshot`, public-surface test, new editor/statement tests.
- **Schema-free items:** TR-01, TR-02, TR-03, TR-05, TR-06, TR-09, TR-11 (TR-11 uses localStorage; TR-02's last-run is a derived cache). TR-02/TR-05 add routes → contract-26 canonical-fallback rows; TR-07 adds one deep-link vocabulary entry — contract-doc changes, not migrations.
- **Gated future majors:** assets/depreciation and loan-out each require an owner decision + specialized contract + major schema/export bump with import migration when approved.

### G.4 What remains separate from Zaman (and from this transfer)

- **Assets & depreciation** — reject-now, gated behind the owner-approved Micro contract; FI-06's mechanics sketch preserved verbatim as the pattern bank.
- **Loan-out receivables** — reject-now; future contract needs the sixth delta dimension.
- **Retained-deposits classification** — owner decision question formulated (§E.2); until answered: documented decision + MIC-10 INFO + statement wording rule.
- **Everything Micro-only** — untouched by design: this analysis never redesigns Micro-only capabilities; the seven reverse-gap areas are warnings, not work items.

### G.5 How the architecture preserves Micro's identity

- **Decision-first Home:** TR-05 enriches the existing bounded block (same visual weight, cap) and moves the full list to a separate reader; no panels, no analytics on Home.
- **Bounded profit:** «غير متاح» becomes a cross-checked first-class state (TR-01); the export carries the honesty instead of replacing it (TR-03); nothing prints «صافي الربح النهائي».
- **Five seats:** no new seat; TR-02 lives under أدواتي (thinking-tool identity), TR-05's reader under the مالي family; discoverability via the Tools module-states list and Finance text-actions — the roles these surfaces already own.
- **Offline-first:** every accepted item is pure local read/write — export is a local Blob, integrity checks read local stores, drafts are localStorage; zero network, zero cloud, zero auth.

---

## Output H — Implementation-Ready Handoff

Design handoff only — **no code was implemented in this task**. The sequence follows the dependency graph (§G.2); each item lists what "done" means and its acceptance test scenarios.

| # | Item | Done means | Acceptance criteria / test scenarios |
|---|---|---|---|
| 1 | **TR-01** | `readRecordedPeriodResult` is the only producer of period-result numbers; Finance period view, Statement, and Home facts consume or cross-check it; no page contains inline period arithmetic; public-surface test locks the API | (a) same fixture → identical result line on Finance/Statement/Home; (b) unknown-cost direct sale → all three surfaces render the same «غير متاح» + reasons (null never renders 0); (c) bounded-status flags unchanged (`recorded_only`/`incomplete`) |
| 2 | **TR-02** | Read-only service produces MIC-1..MIC-10; `/tools/integrity` renders PASS/WARN/FAIL cards with per-record deep links and text-action fixes; Tools row + Finance doorway; post-import auto-suggestion; zero new stores | (a) clean fixture → all PASS; (b) seeded corruption (orphan sourceRef, unbalanced reversal, negative amanah, drifting statement line) → correct WARN/FAIL with the right record link; (c) `cancelled_pending`/`needs_review` → WARN not FAIL; (d) `cancelled_retained` → INFO with totals; (e) run after import → suggested automatically; (f) **store snapshot hash unchanged before/after run** |
| 3 | **TR-03** | Statement action group downloads `micro-statement-<from>-<to>.md` (UTF-8 BOM) with all blocks, source labels, corrections digest, truth lines verbatim; optional `navigator.share`; works offline; empty data → honest artifact | (a) export of a known fixture matches the on-screen reading line-for-line; (b) null result → «غير متاح — بيانات ناقصة» + reasons, never 0; (c) **no balance-equation claim, no final-profit wording** (wording review gate); (d) BOM present; English-digit filename; DD/MM/YYYY range |
| 4 | **TR-04** (schema 31 / export 23) | Optional tag field in the details layer with derived suggestions (trim + collapse); tag on event rows; statement grouping block collapsed by default; optional EventsLayer filter; import migration defaults null | (a) tagged expense → deltas identical to untagged twin; (b) « بنزين » vs «بنزين» → one vocabulary entry; (c) export-22 import → labels null, legacy groups as «غير مصنّف»; (d) round-trip export 23 → labels preserved; (e) shared-expense with tag → share math unchanged |
| 5 | **TR-08** | Effect-copy rule (incl. loan hint + negative-cash case), header law, OrderDetail action matrix, teaching-empty-state rule written into docs and used as a review checklist | review-gate smoke: every money button on a new surface ships with a before-effect line |
| 6 | **TR-05** | Tier 1: Home block shows direct sales, corrections («تصحيح»), wallet entries; event rows link `/finance?layer=events&event=<id>`; cap 5–7. Tier 2: `/finance/activity` reader with per-kind rows, dash-for-non-cash, deep links, canonical fallback | (a) fixture with one record of each kind → correct row + link target; (b) correction row shows net effect without implying cash; (c) same list on Home and reader within cap (single service, fixture-tested) |
| 7 | **TR-06** | Waste movements appear in EventsLayer/truth strip as «هدر مخزون — بلا خروج نقد» with amount + link | waste fixture → row present, never counted in cash-in/out; reversal → row updates per active-movement rule |
| 8 | **TR-07** | «استلم هذه المواد في المخزون» text-action → receipt editor prefilled `?purchase=`; zero-stock strip; `?purchase` in the closed vocabulary + canonical fallback | (a) bridge hidden/disabled with honest copy when inventory inactive; (b) prefilled editor still requires explicit save; (c) strip lists only zero-quantity materials, quiet styling |
| 9 | **TR-09** | 5s undo-delete for estimate delete (and snippets if built) with true local restore; paste stripping in `englishNumeric` | delete → undo within 5s → record restored byte-identical; paste «12.50 د.أ» → 12.50; Arabic-Indic digits normalized |
| 10 | **TR-10** (owner-gated) | أدواتي module with list/copy/create/edit/delete (undo-delete); optional «استخدم في» prefill for order specifications text only | copy puts body on clipboard; **prefill fills text fields only — never price/cost fields**; unique indexes + operation keys on the new store |
| 11 | **TR-11** | Participating editors persist a draft on change and offer restore on reopen (create mode only); discard clears; save clears; never auto-save records | fill → reload → banner offers restore → values equal; save → key cleared; edit mode → no draft offered; no interaction with UnsavedChangesGuard |

**Migration concerns summary:** exactly one minor schema/export bump in this set (TR-04, optionally bundling TR-10); everything else is schema-free. The import path must continue to accept export 6..22 (existing chain) plus the new 23 with null-default labels. No backfill anywhere; legacy absence surfaces honestly («غير مصنّف»), consistent with the missing≠zero rule.

**Risks register (with mitigations):** integrity false positives (derive from tested rules only; deliberate states = WARN/INFO) · export wording drift (binding content rules + review gate) · tag drift splitting totals (accepted, documented; rename/merge deferred as documented corrections) · Home clutter (cap + same visual weight + separate reader + owner nod) · read-model drift across 6+ stores (single derived service + fixture tests) · bridge pressuring premature inventory use (text-action + honest copy) · undo-delete misapplied to financial records (forbidden by TR-08's law; review gate) · snippets built without validation (gated) · drafts doubling state (input vs navigation separation rule).

---

## Open Questions for the Owner (decision register)

1. **Retained deposits** — the formulated question (§E.2). Nothing changes until answered; MIC-10 keeps it visible.
2. **Category curation** — is derived-only vocabulary enough, or do you want rename/merge later (documented corrections)?
3. **Snippets** — do you reuse repetitive specification text enough to want «ملاحظاتي المتكررة»? (Gates TR-10.)
4. **Loan-out tracking** — do you lend project cash to people? (Pilot evidence; contract per §E.3 if yes.)
5. **Activity reader tier 2** — approve the `/finance/activity` reader, or keep Home-only enrichment?
6. **One-tap order closure** — a Zman-trained habit («أغلق الطلب») to monitor in Pilot; do not build preemptively.
7. **Export format acceptance** — will your accountant/lender actually read Markdown? (If not, a PDF follow-up via a documents pipeline — not a format change.)
8. **After device QA/import on real hardware:** recalibrate MIC severities on real data.
9. *(Observation only)* large one-off purchase visibility — would a reading-layer note suffice until the asset contract decision?

## References and Evidence Base

- **Sub-agent reports (delivered alongside, in `../subagents/`):** `01-zaman-capability-map.md` (ZC-01…ZC-24, full evidence index) · `02-micro-gap-comparison.md` (MG-01…MG-21, baseline, false-gap warnings) · `03-workflow-mobile-ux.md` (UX-01…UX-09, journey dossiers, UX rejection table) · `04-financial-data-integrity.md` (FI-01…FI-10, IC-1..IC-16 mapping, migration register) · `05-transfer-architecture-review.md` (critical review, contradiction resolutions, TR-01…TR-17, final architecture).
- **Primary repositories (read-only):** `Qays7753/zman-app` @ `bdd63ab` — `artifacts/zman-app/src/features/*`, `docs/ACCOUNTING_RULES.md`, `CLAUDE.md`, drizzle migrations 0000–0028. `Qays7753/Micro` @ `4db6a5f` — `apps/prototype-web/client/src/*`, `src/domain/*`, `docs/operations/current-state.md`, `docs/contracts/*`, `docs/decisions/*`.
- **No external sources were used for any binding decision** (repository evidence and Micro's own documented rules were sufficient and authoritative for every verdict), so no external reference list is applicable.

*End of report. Built from read-only inspection of both repositories; neither product repository was modified. The five specialized sub-agent reports and this report's evidence chain are preserved in the same delivery folder.*
