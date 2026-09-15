# SA-3 — Zman→Micro Workflow, Screen, and Mobile UX Transfer Analysis

- **Task ID:** SA-3 (Workflow, Screen, and Mobile UX Analyst, sub-agent)
- **Date:** 2026-09-03
- **Repos analyzed (both read-only, untouched):**
  - Zman: `/home/z/my-project/repos/zman` — `main` @ `bdd63ab` — app under `artifacts/zman-app` (Next.js 15 App Router, Arabic RTL, PWA)
  - Micro: `/home/z/my-project/repos/micro` — `main` @ `4db6a5f` — app under `apps/prototype-web/client` (Vite React PWA, wouter router)
- **Methodology:** journey reconstruction by direct code reading of screen components, navigation config, design contracts, and shared interaction libraries in both repos; every screen/flow claim cites an exact file path; anything not directly verified is labeled `INFERENCE`. Round-1 reports (SA-1 `01-zaman-capability-map.md`, SA-2 `02-micro-gap-comparison.md`) provided the candidate list and MG classifications; all UX claims were re-verified in source. Product name is "Zman" (repo `zman-app`).
- **Convention:** Zman money = fils (1 JOD = 1000 fils, 3 decimals, `formatFilsToJod`); Micro money = minor (1 JOD = 100 minor, 2 decimals, English digits, `formatMoneyMinor`). Zman dates = `en-CA` ISO input + `ar-JO` display; Micro dates = DD/MM/YYYY English digits in Asia/Amman.

---

## 1. Zman UX system summary

Zman is a **phone-first (360–430px) Arabic RTL single-owner app** whose UX law is written down in three binding contracts under `artifacts/zman-app/docs/`:

### 1.1 Design System v2.1 (`docs/DESIGN_SYSTEM_V2_1_CONTRACT.md`)
- **Hierarchy by place/size/weight before color; color never carries meaning alone** (§3.3) — every status pairs text + icon.
- **The financial-action rule (§3.5): "الفعل ذو الأثر المالي يشرح أثره قبل التنفيذ وبعده"** — a financially meaningful action must explain its effect *before* execution and *after* it. This is the deepest UX contract in Zman and the source of the mode-hint lines, COGS preview boxes, and reverse-confirmation bullet lists.
- Touch targets **48×48 px** internal standard (§5), buttons `lg=52 / md=48 / sm=40` with real 48px hit areas in card rows (§8).
- **Destructive financial actions stack vertically on phone: cancel first, destructive action after a clear gap; never merge two reverses** (§8 buttons) — visible in OrderDetail's reverse modals.
- Primary button text must describe the act («حفظ الطلب», «تأكيد رد العربون»), never generic «موافق» (§8).
- Bottom sheets: independent scroll, safe-area, focus trap, 85vh ceiling not target; error toasts must not stay stuck over content (§8).
- Bottom bar keeps labels under font scaling; FAB never covers the last card; conditional bottom safe area only when bar/FAB present (§8).
- Money: `bdi dir="ltr"` around amounts, «د.أ» suffix, `tabular-nums` (§6). Logical RTL properties only; directional arrows mirror, status icons don't; product names/numbers/phone wrapped in `bdi` (§12).
- Component "done" definition includes states, contrast, 48px, focus-visible, RTL, 320/360/390/430px, zoom 100/130/200%, reduced motion (§14).
- **Action Dock matrix (§9):** one primary action per order status (`draft`→إرسال للعميل, `sent`→بدء التنفيذ, `confirmed`→تم التسليم, `delivered`/`cancelled`→no forward transition), with conditional secondary actions gated on real data (WhatsApp ⇐ valid phone; reverse forfeiture ⇐ `forfeitureSale` exists; refund ⇐ `depositCents > 0`). No UI transition may exist without state-machine + server guard + financial scenario tests.

### 1.2 Header & Home v2.2 (`docs/HEADER_AND_HOME_V2_2_CONTRACT.md`) + Header Concept v2.3 (`docs/HEADER_CONCEPT_V2_3_CONTRACT.md`)
- **One single header row** inside `AppShell` (56px phone / 64px desktop) — no second toolbar, no ContextBar; header height may never grow from feature work.
- **Anti-jitter rule:** conditional filters live in the *body* (chips, flex-wrap — never horizontal scroll), never in the header; the header holds only page title + one primary contextual action + a unified «أدوات الصفحة» button when secondary actions multiply.
- **RTL visual order fixed by v2.3:** `عنوان الصفحة → تبويب/سياق → بحث → فلتر → أدوات الصفحة` — "where am I" → "what context" → "how do I narrow".
- Title takes full width when the page has no actions (the `max-w-[32%]` clamp is forbidden in that case).
- Tabs (المدفوعات/المبيعات) sit *in* the header row, nearest the title, as compact `tab`-pattern buttons — they never become a second bar.
- Home ordering inside content: «يحتاج انتباهك» → «ملخصك الآن» → «الوصول السريع» → «التحليل المالي» → collapsible details; the period selector lives in the one header, never duplicated in the body.

### 1.3 Navigation model (`src/config/nav.ts`, `src/components/layout/AppShell.tsx`)
- Desktop sidebar 6 items; mobile bottom bar = first 4 (الرئيسية / الطلبات / المالية / المخزون). Everything else lives in a **grouped "More" sheet** with three labeled groups: المتابعة والتحليل (التقارير، الملاحظات، الأصول الرأسمالية، سجل النشاط) · الإدارة المالية (الأرصدة الافتتاحية، الحسابات والصناديق، أصناف الشراء) · المراجعة والأمان (سجل التدقيق). Each item carries a one-line Arabic description.
- Screens are full pages under `src/app/(app)/`; create/edit are `ResponsiveModal` sheets over the page (not routes), with edit state encoded in URL params (`?editExpense=`, `?newPayment=`) so refresh/back keeps intent.

### 1.4 Mobile interaction craft (ZC-24 evidence)
- **5-second undo-delete** (`src/lib/undo-delete.ts`): sonner toast with «تراجع» button; the timer, not the toast dismissal, commits the delete; `committed` flag prevents double-fire; `pagehide` (not `beforeunload` — unreliable on the owner's phone browsers) fires a best-effort commit **only when `navigator.onLine`** (offline ⇒ row stays visible and uncommitted — never lie to the user); past tense «تم الحذف» only after server success. Message uses future tense: «سيُحذف المصروف — لا تغلق الصفحة».
- **MoneyInput** (`src/components/shared/MoneyInput.tsx`): `inputMode="decimal"`, single decimal point enforced, leading-zero cleanup, display not reset while focused, 3-decimal freeze on blur, explicit "0" clears on blur; currency symbol pinned to the logical end (`inset-e-4`). **`parseJodToFils`** (`src/lib/money.ts`) converts Eastern-Arabic numerals ٠–٩ and strips «د.أ»/«JOD»/«دينار» before parsing — paste-tolerant money entry.
- **Empty states teach** (`EmptyState.tsx`): title + description + up to 3 numbered onboarding steps + a direct action button (e.g. payments empty state walks to the FAB → mode → save).
- Skeletons, `ErrorState` with retry, `CardActionSheet` (⋯ per card), `ConfirmDialog`, `InfoTooltip` for just-in-time terminology («شرح التصنيفات»), `FloatingActionButton` with fixed per-tab label, `PageToolbar`/`HeaderIconButton` unified families.
- **List feed pagination** (`PaymentsTab.tsx` + `queries.ts:getPayments`): UNION ALL across expense/purchase/receivable with cursor `(createdAt,id)` and `limit+1` next-cursor; «تحميل المزيد» button with a dedicated *next-page-failure* error block that refuses to drop already-loaded rows («تعذر تحميل الحركات التالية دون فقدان الحركات الحالية»).

### 1.5 Five-second orientation summary (what a Zman screen feels like)
Header (title + context actions) → body (filter chips row → info strip → cards with per-kind second lines) → FAB (fixed label) → modal/sheet for create/edit with a one-line profit-impact hint before the submit button. Every money action names its profit effect before you commit it.

---

## 2. Micro navigation & surface model summary

### 2.1 The five seats + centered recording FAB
- `apps/prototype-web/client/src/app/navigation.ts`: `primaryNavigation` = **مشروعي الآن `/` · العمل `/orders` · مالي `/finance` · أدواتي `/tools`**.
- `components/layout/BottomNav.tsx`: items 1–2, then the centered brown **`سجّل` FAB** (`micro-fab`, aria-label «سجّل»), then items 3–4. The FAB is the primary recording entry (F-003), and its label matches the approved structure verbatim.
- `components/layout/AppHeader.tsx`: brand lockup + contextual route label (`getNavigationLabel`), settings gear → `/settings`, day/night toggle. No sixth seat; `/profile` is reached from Home and Settings.
- `components/layout/MicroAppShell.tsx`: one continuous Android-like shell; `data-route-kind` on root; global chrome hidden while the keyboard is open (visualViewport); `CONTEXT_REPEATS_H1` set suppresses the header label where the page's own `h1` already says it (finance/schedule/settings/inventory/suppliers/cash).
- **QuickActionSheet (`components/layout/QuickActionSheet.tsx`, lazy-loaded + idle-prefetched):** menu of 5 actions — **تسجيل بيع** (in-sheet transitory sale form: name, amount, known-cost select with «لا أعرف الآن — الربح غير متاح لا صفر», credit toggle with customer name + collected-now, wallet destination, receipt mode with record link), **تسجيل مصروف** (in-sheet quick expense), **طلب من عميل** (→ `/orders/draft/new?intent=customer_order`), **مسودة تصميم** (→ `?intent=planned_design`), **عربون أو تحصيل** (→ `/collect` with `?from`). Rule: «البيع والمصروف فعلان عابران — يتمان داخل الورقة… والنموذج الكامل يبقى باب التصحيح والعمق» — the sheet never creates an effect beyond its explicit forms; sale/expense are minimum-viable transitory actions, deep editors remain the correction path.

### 2.2 Route kinds — reader is a surface, editor is depth
`app/routeClassifier.ts` is the single classification point: `setup` (`/setup`), `surface` (keeps bottom nav + FAB: lists, details, readers), `deep` (editors and thinking tools hide nav on purpose; regex list in `deepFlowPatterns` covers `/finance/new/:type`, `/collect`, `/cash/*` editors, `/inventory/material/new`, `/inventory/movement/:id(/reverse)`, `/tools/calculator`, `/tools/estimate/:id`, etc.). U-005 rule: «القارئ سطح، والمحرر عمق» — OrderDetail keeps nav; DirectSaleEditor hides it.

### 2.3 Safe return — contract 26
`app/navigationContract.ts` + `docs/contracts/26-navigation-referrer-and-deep-link-contract.md`:
- `?from=<internal-path>` is the **only** source container; validated by `isSafeInternalPath` (starts `/`, ≤256 chars, no whitespace/quotes/`//`); invalid values silently ignored → `canonicalReturnFor()` documented fallback (e.g. `/tools/calculator`→`/tools`, `/collect`→`/`, `/finance/statement`→`/finance`, `/catalog`→`/tools`); self-referencing `from` ignored (no loops).
- Closed deep-link vocabulary: `?focus` (capacity|recurrence|guided-import|export|today|priority), `?layer` (corrections|events), `?mode` (cover), `?event` (id, `/^[A-Za-z0-9_-]{1,64}$/), `?from`, `?to`. Unknown values → null, no explosions. Cold start/refresh preserves intent in the URL.
- Deep links open *the section or action*, not the generic page (`/finance?layer=corrections` opens the corrections layer; `?event=` focuses a specific event row).

### 2.4 Unsaved-input guard
`components/forms/UnsavedChangesGuard.tsx`: registered guards (`isDirty` + `onSave`); in-app navigation intercepted into a 3-choice RTL dialog («ابقَ في الصفحة» primary/first-focus, «احفظ واستمر» text action, «اخرج دون حفظ» danger last, separated by 16px gap); browser back is caught by a `microGuard` sentinel history entry so the form stays mounted; `beforeunload` armed while dirty; Esc = stay (least destructive). Focus is trapped and restored to the trigger.

### 2.5 Micro's own money/date/RTL contracts
- `presentation/formatters.ts`: **English digits 0–9 and numeric DD/MM/YYYY everywhere** (Group 6 item 5 systemic rule); money 2-decimal with thousands grouping + «د.أ» suffix from one central formatter; Arabic plural rules (`formatArabicPlural`) so never «1 طلبات».
- `components/forms/EnglishNumberInput.tsx`: `lang="en" dir="ltr"` isolated input, `inputMode` per kind, pattern-checked, **`normalizeAsciiDigits` converts Arabic-Indic/Persian digits to English on every change** (Group 6 item 5) — the numeric meaning never changes. Empty-allowed mode, focus clears default zero, blur re-formats.
- Honest-state language discipline: «غير متاح» not 0 for unknown profit; «يحتاج مراجعة»; RestatementNote strip whenever corrections exist; every reading states what it includes/excludes.

### 2.6 Screen inventory relevant to the dossiers
- **Home `/`** (`pages/Home.tsx` + `application/home/homeControlCenterService.ts`): «الأهم الآن» single priority block → «اليوم» action list → honest facts → مالي summary → catalog block → optional paths → **«ما تغير مؤخرًا» recent block capped at 5** (orders/drafts/financial events/schedules, each linking to its record; events link generically to `/finance`) → locality note.
- **Finance `/finance`** (`pages/Finance.tsx`): first decision = «الوضع الآن» / «شو صار خلال الفترة» (defensive `?view=`); position view = cash decision card, position cards, RestatementNote, truth section with text-action links (دفتر الناس، الموردون، عدّ الصندوق، كشف الفترة، قراءة الفترة الكاملة), DepositsLayer; period view = collapsible «قراءة الفترة» layer with month range, status, inclusion/exclusion notes, insights; **«تسجيل حركة أو فتح مصدر» collapsible actions layer** (8 event-type buttons + محافظ/موردون/مواد/مال المالك, all `withFrom`); EventsLayer («السجل والأثر», `?layer=events`, `?event=` focus); CorrectionsLayer (`?layer=corrections`).
- **FinancialEventEditor `/finance/new/:type`** (`pages/FinancialEventEditor.tsx`): deep editor; «الأثر المعروف» decision card first; money + date + counterparty + required note «ما الذي حدث؟ (مطلوب)»; **progressive-disclosure `<details>` «أضف سياقًا للمصروف»** containing `ExpenseClassification` (relationship project/shared, behavior fixed/variable/mixed/unknown, purpose, knowledge, shared-basis modes fixed/percentage/estimate/defer with helper copy per mode); sticky save button; UnsavedChangesGuard.
- **Statement `/finance/statement`** (`pages/Statement.tsx`): quick ranges (this/last week — Sunday→Saturday — this month, custom); blocks: cash-in/cash-out lines with expandable per-line **sources deep links**, corrections block, period result card, amanah card, receivables/payables now; «ما يعنيه هذا الكشف» truth lines; return via `?from`.
- **Tools `/tools`** (`pages/Tools.tsx`): «احسب قبل أن تلتزم» — calculator deep route, saved estimates (open/«ابدأ مسودة من هذا التقدير» bridge/two-step destructive delete), **module states list** (المخزون/الكتالوج/المواعيد/الموردون/دفتر الناس/السوق) with derived availability states and «افتح» actions — the natural home for read-only thinking/verification tools.
- **Inventory `/inventory`** (`pages/InventoryMaterials.tsx` + `MaterialEditor.tsx` + `InventoryMovementEditor.tsx` + `InventoryReversalEditor.tsx`): whole-inventory **opt-in activation dated today** (القرار ٩) with an honest pre-activation explainer; per-material cards (quantity + value + movement count); «أخرِج المتبقي» full-write-off panel with mandatory reason (القرار ۲۰); movement log «سجل لا يحذف بصمت» (first 8) with per-movement «تراجع موثق» links; movement editor supports receipt/consume/waste/adjust with **mandatory reason for waste/adjust**, wasteContext (order/catalog/template/general/unallocated), `?order=` prefill for consume, purchaseId select for receipt.
- **OrderDetail `/orders/:id`** (`pages/OrderDetail.tsx`): readiness → «الطلب جاهز للتسليم» → «تم التسليم» (revenue recognized at delivery, *no conversion action*); price edit via CorrectionPreview (before/after + unchanged list); cancellation with 3 reasons + skip (القرار ١٩); **cancelled-order deposit settlement = three options** (ردّ العربون / احتفظ به / اتركه «يحتاج مراجعة») with reason field; per-collection reversal with cumulative-cap validation («التراجع التراكمي لا يتجاوز مبلغ القبضة»).
- **CashCount `/cash/count`** (`pages/CashCount.tsx`): count-the-drawer compare → recorded difference becomes a *documented adjustment dated today* — Micro's existing reconciliation-thinking-tool precedent.
- **DirectSaleEditor** (`pages/DirectSaleEditor.tsx`): post-save returns to `?from` source; revisions trail (price_cut/cancel) preserved; cancellation with reason + idempotency key.

### 2.7 What Micro's model means for transfer design
Every accepted capability must pick one of five surface types: **(1) a seat-surface page** (keeps nav), **(2) a deep editor** (hides nav, UnsavedChangesGuard, `?from` return), **(3) an in-sheet transitory action** (QuickActionSheet), **(4) a collapsible layer inside an existing surface** (Finance layers), or **(5) a contextual text-action/inline field**. New deep routes must be added to `deepFlowPatterns` + `canonicalReturnFallbacks` in the same commit (contract 26).

---

## 3. Journey dossiers

> Each dossier: **A** = Zman's actual UX (verified in code) → **B** = proposed Micro appearance → structured finding block.

---

### 3.1 UX-01 — Expense classification + unified smart entry (ZC-02 + ZC-01; MG-01 MICRO-DIFFERENT)

#### A. Zman's actual workflow

**Entry points:** FAB «تسجيل جديد» on `/finance` payments tab (label fixed per tab, `PaymentsTab.tsx:669-684` opens `ResponsiveModal` titled «تسجيل جديد» hosting `SmartFinanceForm`); edit paths via URL params `?editExpense=` / `?editPurchase=` from payment cards; nav link `/finance?manageCatalog=purchases` for the items catalog; «إدارة الفئات» button inside the payments filter modal (expense chip only).

**Screen anatomy — SmartFinanceForm (`src/features/finance/components/SmartFinanceForm.tsx`, 1392 lines):**
1. (Create-only) **draft offer banner** when a localStorage draft exists («مسودة محفوظة» + استعادة/تجاهل).
2. **Mode selector**: 2×2 grid on phone (`grid-cols-2 sm:grid-cols-4`, `role="tablist"` «نوع العملية») — مصروف يومي / شراء مواد / أصل للورشة / دَين لشخص, each icon + label, min-h-12.
3. **One-line profit-impact hint** (lines 854–863), shown *before any field*: expense → «يُخصم من ربح هذا الشهر كاملاً.» · purchase → «مادة تدخل منتجاتك. إن ربطتها بصنف متتبَّع، تُخصم تكلفتها عند البيع لا عند الشراء.» · asset → «لا يُخصم من ربح هذا الشهر. يُوزَّع إهلاكاً على عمره النافع.» · receivable → «لا يُخصم من ربحك — مالك ما زال لك، لكن عند غيرك.»
4. Mode-specific field set (each ≤5 fields, 48px-high inputs, inline Arabic Zod errors):
   - **مصروف يومي**: date (default today) · **category: Select from catalog + «أخرى (إدخال يدوي)...» option that flips to free text with «اختر من القائمة» toggle-back link** (lines 883–936) · amount (MoneyInput) · optional note. Submit «تسجيل المصروف».
   - **شراء مواد**: date · item Select with two optgroups — «أصناف المخزون المتتبعة» (with stock) and «أصناف المشتريات العامة» — or free text; **live impact preview box** when a tracked item is selected: green card «📦 سيُضاف N وحدة إلى المخزون · الرصيد الحالي: X» + «✓ لن تُخصم التكلفة من ربح هذا الشهر — تُضاف لقيمة أصول المخزون وتُخصم كتكلفة بضاعة مباعة (COGS) عند بيع وتسليم المنتجات» (lines 1080–1095), and a neutral ℹ️ box for untracked: «شراء مباشر غير متتبَّع — سيُخصم المبلغ كاملاً من أرباح هذا الشهر» · supplier (optional) · quantity × total (MoneyInput) · **derived unit price preview** «سعر الوحدة: X» (lines 1160–1172) · notes. Submit «تسجيل الشراء».
   - **أصل للورشة**: date · name (placeholder examples) · amount · description · **«توزيع الإهلاك شهرياً» checkbox with worked example** «ثلاجة بـ 600 دينار / 24 شهر = 25 دينار تُخصم من ربحك شهرياً» (lines 1253–1270) → after save, `DepreciationPromptModal` asks useful life. Submit «تسجيل الأصل».
   - **دَين لشخص**: date · person name · amount · account Select («دُفع من صندوق / حساب») · notes.
5. Sticky full-width submit (min-h-12), double-submit `inFlight` lock, offline `assertOnline()` toast, error toasts carry the server's Arabic message.

**Category system (ZC-02):** flat name catalog `expense_category_catalog` with three unified sources — (1) seed-on-read defaults (رواتب، إيجار، كهرباء ومياه…) idempotent and non-destructive; (2) **lazy auto-enrollment** — `createExpense` calls `ensureExpenseCategoryInCatalog(trimmedCategory, tx)`: a hand-typed category joins the catalog automatically, trimmed, failure never blocks the save; (3) **orphan merge in the filter** — `useExpenseFilterCategories` merges catalog names + `SELECT DISTINCT category FROM expense` so historical categories stay filterable. Management modal `FinanceCatalogModal` (add/rename/delete) reachable from the filter modal's «إدارة فئات المصروفات» button.

**Filtering/listing UX (`PaymentsTab.tsx`):** one filter button (compact) opening a «تصفية المدفوعات» modal with a 2×2 grid of kind chips (الكل/مصاريف/مشتريات/أصول/ديون — 5 chips), category dropdown (expense chip only), manage-categories button, «مسح» clear chip in the row, result count strip + «شرح التصنيفات» InfoTooltip, kind-specific card second lines (category pill + «مصروف أصل» tag; supplier + «N وحدات × unit»; «رأس مال» badge; gray read-only «تسوية مخزون تلقائية» for write-offs).

**Happy path:** `Open /finance → tap FAB «تسجيل جديد» → mode «مصروف يومي» (hint line explains profit impact) → pick «كهرباء ومياه» from Select → MoneyInput 12.500 → «تسجيل المصروف» → toast → modal closes → list refetches → card shows category pill + relative date → this month's operating profit drops by 12.500`.
**Edge paths:** hand-typed category → auto-enrolled next time; offline submit → toast, draft retained in localStorage; edit a purchase → supplier + classification preserved (Edit-Trap fix); delete → 5s undo; write-off card → no ⋯ menu, edit attempt answers «هذا مصروف تلقائي… صحِّح المخزون من شاشة الكتالوج».

**Mobile/RTL/return:** modal-over-page (no route change) so the list context is never lost; 48px targets; MoneyInput LTR-isolated; return = modal close. Desktop = side sheet.

#### B. Proposed Micro appearance

- **Capability name (owner language):** «تصنيفي للمصاريف» (my own expense grouping) — a *tag vocabulary*, never "account categories"; the accounting dimensions (relationship/behavior/purpose/knowledge) stay exactly as Micro defines them.
- **Owning tab:** **مالي**. Owning screen: the existing `/finance/new/operating_expense_*` deep editors — the classification `ExpenseClassification` `<details>` layer is the natural host.
- **Surface type:** **inline field inside the existing progressive-disclosure layer** (surface type 5) — *not* a new page, *not* a managed-catalog modal. A single optional field «تصنيفك (اختياري)»: a text input with datalist-style suggestions from previously used tags + «+ تصنيف جديد» — exactly Zman's Select-then-custom pattern without the catalog modal.
- **Why:** Micro's classification is *context questions*, not names (MG-01). A named tag is additive metadata that never changes amounts, never allocates, never enters the shared/unallocated truth model — it only feeds grouping. Putting it inside the existing details layer keeps the happy path (amount → date → note → save) untouched for the 90% quick-expense case, matching Micro's transitory-action philosophy.
- **Lazy auto-enrollment + trim normalization:** adopt Zman's exact three-source merge (used tags + typed tags, trimmed compare) — but store as a **derived read list** (like `partyLedger`), not a new write-path table, unless the owner needs rename/merge (defer).
- **Where it pays off:** `Statement.tsx` gains a collapsed «مصاريفي حسب تصنيفي» block (per-tag totals with source links, same `StatementLineRow` pattern) and `EventsLayer` gains an optional tag filter. Read-only derivation; zero new financial semantics.
- **Screen contract:** states — empty («ما في تصنيفات بعد؛ اكتب أول تصنيف وقت تسجيل المصروف»), offline (all local, no change), error (none — optional field), unsaved (already guarded by UnsavedChangesGuard), edit (tag editable via documented correction), success (grouping appears next statement read).
- **Safe return:** no new route ⇒ `?from` unchanged; statement block links use `withFrom('/finance/…', '/finance/statement')` like existing source links.
- **Discoverability:** secondary/contextual (field inside editor + reading block in statement). Not a seat, not a Tools module.
- **MVP vs complete:** MVP = optional free-text tag with suggestions + statement grouping block. Complete = rename/merge tag management sheet («إدارة التصنيفات») opened from the statement block, mirroring Zman's FinanceCatalogModal placement (in a filter/reading context, not the editor), plus per-tag period trend.
- **RTL/digits:** tags are Arabic free text (RTL natural); amounts keep English digits + «د.أ» from the central formatter; dates DD/MM/YYYY.

```
finding_id: UX-01
capability_name: تصنيف المصاريف (tags) + نمط الإدخال الموحد متعدد الأوضاع
comparison_classification: MICRO-DIFFERENT (MG-01)
zaman_evidence: artifacts/zman-app/src/features/finance/components/SmartFinanceForm.tsx (MODES 49-54; hints 854-863; category select/custom 883-936; tracked preview 1080-1102; unit-price preview 1160-1172; depreciation example 1253-1270); src/features/finance/components/PaymentsTab.tsx (filter modal 271-359, category dropdown 304-345); src/features/finance/actions.ts (seedDefaultExpenseCategories:2560, ensureExpenseCategoryInCatalog:2639); src/features/finance/queries.ts (getExpenseCategories:736, getDistinctExpenseCategories:902); src/features/finance/components/FinanceCatalogModal.tsx
micro_evidence: apps/prototype-web/client/src/pages/FinancialEventEditor.tsx (details layer 353-377; ExpenseClassification 448-569); src/domain/financial-event/types.ts (OperatingExpenseContext); apps/prototype-web/client/src/pages/Statement.tsx (line rows + sources 37-82); apps/prototype-web/client/src/pages/Finance.tsx (EventsLayer 955-965)
user_problem: the owner cannot answer "شو صار على البنزين هذا الشهر؟" — Micro asks truth-context questions but keeps no named vocabulary, so grouping is manual note-reading
workflow_summary: Zman: FAB → 4-mode selector → per-mode profit-impact hint → minimal fields → save → auto-enrolled category appears in filter + P&L donut. Micro: deep editor → context questions in a details layer → required note → save → no grouping anywhere
screen_and_navigation_summary: Zman = one modal form + filter modal + catalog modal; Micro = deep editors per event type + reading layers
micro_proposal: optional «تصنيفك» free-text-with-suggestions field inside the existing ExpenseClassification details layer (lazy auto-enrollment, trim normalization, derived read list) + per-tag grouping block in /finance/statement + optional EventsLayer tag filter. No managed catalog in MVP; no accounting jargon; no allocation semantics
transfer_recommendation: adapt — the mode-hint and lazy-category patterns transfer as pure UX; Micro's context model stays the source of truth
micro_destination: مالي → /finance/new/operating_expense_* (inline field) + /finance/statement (grouping block)
priority: P1
confidence: high
risks: tag vocabulary drifting into fake accounting (mitigate: copy that says tags don't change amounts); free-typing chaos (mitigate: trim + suggestions + orphan merge, Zman-proven); statement clutter (keep block collapsed by default)
open_questions: managed catalog vs free tags (owner decision, flagged by SA-2); should QuickActionSheet's quick-expense get the tag field too (recommend: no — keep transitory action minimal)
```

---

### 3.2 UX-02 — Selective per-item inventory (ZC-07; MG-02 MICRO-DIFFERENT)

#### A. Zman's actual workflow

**Entry points:** bottom-nav seat `/inventory` (المخزون is a first-class seat); `/catalog` for the master list; purchase mode in SmartFinanceForm for linking; FAB «إجراءات المخزون» on the inventory screen.

**Screens:**
- **`/catalog` item form (`src/app/(app)/catalog/CatalogClient.tsx`)**: name/default cost/unit/notes + a boxed **«متتبَّع» checkbox** (lines 569–602) with `InfoTooltip`: «عند تفعيل التتبع: الشراء لهذا الصنف يُسجَّل كمخزون (لا يخفض الربح في شهر الشراء)، وعند البيع تُخصم تكلفة البضاعة المباعة من الربح. الأصناف غير المتتبَّعة تُعالَج كمصروف تشغيلي مباشر.» The **«الرصيد الافتتاحي» field appears only on first activation** («يُضاف مرة واحدة عند التفعيل») with the note that it creates an `in` movement at cost 0 (documented trade-off). Catalog cards carry a per-card tracked toggle («متتبَّع»/«تفعيل التتبع», line 389).
- **Untrack confirmation** (lines 626–635 inline warning + 673–679 ConfirmDialog): «ستفقد التتبّع. الرصيد الحالي N وحدة سيُعامَل كصفر للطلبات الجديدة. سيتم حذف سجل الحركات ناعماً. هل أنت متأكد؟» — consequences stated with the actual number; confirm button labeled «نعم، ألغِ التتبّع».
- **`/inventory` (`src/features/inventory/InventoryScreen.tsx`)**: header (title + sort modal via PageToolbar) → **low-stock warning banner** («N أصناف نفد رصيدها» + names joined) → two stats cards (إجمالي الأصناف / القيمة الدفترية) → per-item cards (name + «نفد» badge + book value + big balance number + unit, warn-tinted when low) → **FAB «إجراءات المخزون» opens an action sheet** with three rows (إضافة صنف مُتابَع / تعديل سريع للمخزون — صرف أو إضافة / إدارة الكتالوج الكامل) → empty state with 3-step onboarding (اذهب إلى الكتالوج → فعّل التتبع → حدد الكمية والسعر) + «الانتقال إلى الكتالوج» button.
- **`QuickAdjustStockForm`**: select tracked item (showing current balance inline), direction صرف/إضافة, qty, reason. `AddTrackedItemForm`: name/unit/default cost/opening qty.
- **Auto-coupling (the part Micro rejects):** a purchase linked to a tracked item automatically creates an `in` movement (capitalized, profit untouched); order delivery inside `convertOrderToSale` automatically deducts `out` movements with weighted-average COGS; negative balances allowed with a recorded warning note.

**Happy path:** `فتح الكتالوج → صنف جديد → تفعيل «متتبَّع» → ظهور حقل الرصيد الافتتاحي → حفظ → الشراء اللاحق يظهر في /inventory → التسليم يخصم الرصيد ويحسب COGS في شهر البيع`.
**Edge paths:** untrack with stock>0 → confirmation dialog → movements soft-deleted; purchase linked to untracked item → rejected with Arabic error; negative stock → allowed + note «⚠️ الرصيد قبل الخصم أقل من المطلوب».

#### B. Proposed Micro appearance

**Verdict: REJECT the automation core; ADAPT three interaction contracts.** Micro's inventory is opt-in *as a whole* (dated activation, القرار ٩) and consumption is deliberate per-order evidence (`docs/contracts/11`, `13`); auto-deduct-on-delivery is an explicit boundary violation (MG-02, SA-2). `SupplierPurchaseEditor` says it out loud: «لن يحوله Micro إلى تكلفة بيع أو مخزون حتى المرحلة التالية» (line 303).

What still transfers as UX:
1. **Stated-consequences confirmation pattern for state-changing inventory decisions.** Micro has activation but **no deactivation/disable flow at all** (INFERENCE — no UI or contract found for turning inventory off; Zman's untrack dialog is the proven template if Micro ever needs one: name the current balance, say what future orders will see, say what happens to history).
2. **Stock-aware purchase→receipt bridge.** Zman's purchase form shows current stock next to the tracked item; Micro keeps purchase and receipt separate (receipt movement editor takes a `purchaseId` dropdown, `InventoryMovementEditor.tsx:307`). Proposal: a contextual text-action on the supplier-purchase record — «استلم هذه المواد في المخزون» → `withFrom('/inventory/movement/receipt?purchase=<id>', '/suppliers/purchase/<id>')` + teach the receipt editor the `?purchase=` prefill (the consume editor already proves the pattern with `?order=`). This is a *bridge*, not automation: the owner still records the receipt deliberately.
3. **Low-stock visibility.** Zman's banner (count + names) is a cheap, honest reading aid; Micro's inventory overview shows quantities but no «نفد/منخفض» cue. A quiet strip in `/inventory` («مواد وصلت صفرًا: …») fits Micro's «الأهم الآن» honesty without creating an alert system.

- **Capability name:** no new capability — enhancements to «المواد والمخزون».
- **Owning tab/screen:** مالي → `/inventory` (bridge from `/suppliers/purchase/:id`).
- **Surface type:** inline contextual actions + one text-action bridge; zero new routes except the `?purchase=` param on an existing deep route.
- **States:** bridge button hidden when inventory not activated (or shown with honest copy «فعّل المخزون أولًا»); receipt editor prefilled + guard unchanged.
- **Safe return:** receipt editor returns to the purchase record via `?from`; add `/inventory/movement/receipt?purchase=` to the existing canonical family (already `/inventory`).
- **MVP vs complete:** MVP = receipt bridge + `?purchase=` prefill + zero-stock strip. Complete = stated-consequences deactivation dialog (only if a contract for disabling inventory is ever written).
- **RTL:** nothing new; quantities already English digits.

```
finding_id: UX-02
capability_name: المخزون الانتقائي لكل صنف (tracked flag + حركة تلقائية)
comparison_classification: MICRO-DIFFERENT (MG-02)
zaman_evidence: src/app/(app)/catalog/CatalogClient.tsx (tracked toggle + tooltip 569-602; openingStock 604-624; untrack warning 626-635 + ConfirmDialog 673-679); src/features/inventory/InventoryScreen.tsx (banner 104-119, stats 121-135, FAB sheet 223-276); src/features/inventory/components/QuickAdjustStockForm.tsx; SmartFinanceForm.tsx (tracked optgroup + stock preview 1022-1095)
micro_evidence: apps/prototype-web/client/src/pages/InventoryMaterials.tsx (activation 173-203; أخرج المتبقي 316-366; movement log 367-395); src/pages/InventoryMovementEditor.tsx (receipt purchaseId 307, consume ?order prefill 28, reason mandatory 157); src/pages/SupplierPurchaseEditor.tsx (line 303: «لن يحوله Micro إلى … مخزون حتى المرحلة التالية»); src/domain/inventory-material/types.ts (movement types + WasteContext); docs/contracts/11-inventory-material-consumption-prototype-contract.md
user_problem: none today in Micro's own model (explicit evidence is the design); the friction is the missing bridge between a recorded purchase and the deliberate receipt, and zero-stock visibility
workflow_summary: Zman: toggle tracking per item → purchases/deliveries move stock automatically with weighted-average COGS. Micro: activate inventory once (dated) → record receipt/consumption/waste movements deliberately per order
screen_and_navigation_summary: Zman = catalog form checkbox + inventory seat + FAB action sheet; Micro = finance-owned inventory surface + deep movement editors with ?from
micro_proposal: keep Micro's explicit-evidence model; add (1) «استلم هذه المواد في المخزون» bridge text-action on the purchase record → receipt editor prefilled ?purchase=, (2) zero-stock quiet strip in /inventory, (3) Zman's stated-consequences dialog pattern reserved for any future deactivation contract. REJECT auto-deduct and auto-capitalization
transfer_recommendation: reject (core) + adapt (three interaction contracts) — automation contradicts Micro's purchase≠COGS and explicit-evidence boundaries
micro_destination: مالي → /inventory + /suppliers/purchase/:id (bridge)
priority: P2
confidence: high (rejection); medium (bridge — needs owner validation that the extra link helps rather than pressures)
risks: bridge could pressure owners into premature inventory use (mitigate: honest copy on the button, keep it a text-action not a primary button); zero-stock strip must not become an alert system
open_questions: does Micro ever need inventory deactivation? (no contract today); should the purchase summary show «لم يُستلم بعد» state? (needs supplier-purchase domain check — INFERENCE: no received flag seen in editor UI)
```

---

### 3.3 UX-03 — Finance integrity check suite (ZC-16; MG-08 ZAMAN-ONLY)

#### A. Zman's actual workflow

**Entry point:** `/reports` page → IntegrityCheckReportPanel card. (Secondary: it is the only place; the More menu leads to /reports.)

**Screen anatomy — `src/features/reports/components/IntegrityCheckReportPanel.tsx` (187 lines):**
1. Card header: ShieldCheck icon + «الفحص المالي الدوري» + `InfoTooltip` (added in Round 4 B-5) explaining the three states: «سليم» (green: balanced, no action), «تحذير» (yellow: minor drift, review when free), «خطأ» (red: broken accounting balance, usually a missing/duplicated movement, needs fixing) + the safety promise «الفحص آمن ولا يُغيّر أي أرقام — يقرأ فقط».
2. Secondary-size «فحص الآن» button (isLoading «جارٍ الفحص...»).
3. On result: **overall summary banner** (status-colored border/bg, `summaryAr`, as-of date + run timestamp in ar-JO) + toast mirroring the overall status.
4. **16 result cards (IC-1..IC-16)**, each: status icon (CheckCircle2/AlertTriangle/XCircle) + `titleAr` bold + status badge («سليم/تحذير/خطأ») + `descriptionAr` + drift amount line («الفارق: X (سالب/موجب)» — with IC-12/IC-14 re-labeled as book-value readings) + count line («عدد المخالفات: N») + collapsible `<details>` of offending record IDs + **`suggestedFixAr` rendered as an italic action hint prefixed «↩»**.
5. Read-only: zero writes; runs all checks in parallel server-side.

**Happy path:** `فتح التقارير → «فحص الآن» → انتظار ثانيتين → بانر أخضر «كل الحسابات سليمة» + توست نجاح → تصفح الفحوصات الستة عشر كلها «سليم»`.
**Edge paths:** any FAIL → red banner + toast «توجد مشاكل تحتاج إصلاح» → open the failing card → read description + suggested fix → (fix happens elsewhere: e.g. IC-5 archived account with balance → go fix the account); WARN → yellow, review later; empty data → checks pass trivially.

**Return to context:** stays on /reports; panel result persists in local state until rerun.

#### B. Proposed Micro appearance

- **Capability name:** **«فحص سلامة مالي»** — one-tap self-audit, read-only. Copy contract borrowed directly from Zman: «فحص آمن — يقرأ أرقامك ولا يغيّر شيئًا».
- **Owning tab:** **أدواتي** (primary) — it is a thinking/verification tool, matching the seat's identity «احسب قبل أن تلتزم» and the Calculator's zero-effect precedent; **secondary entry: a text-action in مالي's truth section** («فحص سلامة مالي» next to عدّ الصندوق) because that is where doubt is felt. (SA-2 left أدواتي vs مالي open; this resolves it: primary home أدواتي, contextual doorway مالي.)
- **Surface type:** **full-screen read-only surface page** (route kind `surface`, keeps bottom nav — it's a reader, not an editor): `/tools/integrity` with `?from`. No UnsavedChangesGuard (nothing to save); no new deep-link params needed.
- **Screen contract (hierarchy):**
  - Header: back button (`?from` → `/tools`) + `micro-page-heading` «فحص سلامة مالي» + one-line promise «يقرأ كل سجلاتك محليًا ويتحقق من توازنها — لا يكتب ولا يصحح».
  - Decision card: overall status (سليم/تحذير/خطأ) + run timestamp + «افحص الآن» primary button.
  - Body: check cards — Arabic title + status + one-line explanation + drift/δ where meaningful + **«وين المشكلة»** source links (Micro has record-level hrefs — stronger than Zman's raw IDs) + suggested next action as a *text-action to the fixing surface* (e.g. unallocated-cash difference → «افتح توزيع الكاش»).
  - States: empty (no data yet — «سجّل أول حدث ثم افحص»), loading, PASS, WARN, FAIL, re-run after fixes.
- **Invariant set (mapped to Micro's own rules, NOT Zman's):** (a) cash continuity: wallet balances = Σ entries per wallet (cash-continuity module); (b) every correction has its reversal pair and net effect ≤ original (corrections digest); (c) statement = position reconciliation (S2/G5-S7: period reading components tie to position cards); (d) sourceRef integrity — every event/movement points at an existing record (reuse import-verifier rules at runtime); (e) collection≠profit boundaries — no collection event changes period result; (f) order debt = price − collected − documented settlements; (g) inventory: Σ movements per material = displayed balance; waste ≤ remaining. Build ONLY from existing read models — no new stores, no new writes.
- **Safe return:** `withFrom('/tools/integrity', source)` from both Tools and Finance; canonical fallback `/tools`.
- **Discoverability:** Tools module-states list gains a row «فحص سلامة مالي» (state: enabled once any data exists, else «سجّل بيانات أولًا») + Finance truth-section text-action.
- **MVP vs complete:** MVP = overall verdict + 5–7 core invariants with links. Complete = full card set with per-record links, last-run persistence, and a «فحص بعد الاستيراد» auto-suggestion after import/restore (the highest-risk moments).
- **RTL/digits:** amounts English digits + «د.أ»; status words Arabic with icon (never color alone — Zman rule that Micro already follows).

```
finding_id: UX-03
capability_name: فحص السلامة المالي (one-tap self-audit)
comparison_classification: ZAMAN-ONLY (MG-08)
zaman_evidence: src/features/reports/components/IntegrityCheckReportPanel.tsx (full panel; InfoTooltip 68-70; runCheck 38-59; per-check cards 106-181); src/features/finance/integrityCheck.ts (IC-1..IC-16, 1608 lines); src/features/finance/actions.ts (runFinancialIntegrityCheckAction:4127)
micro_evidence: no user-facing integrity surface; structural equivalents: apps/prototype-web/client/src/application/finance/correctionHistoryService.ts (CorrectionDigest on 5 surfaces); application/transfers/localTransferService.ts (import verifier); pages/CashCount.tsx (count→adjustment reconciliation precedent); pages/Tools.tsx (thinking-tool identity + module states 75-111)
user_problem: when the cash number "looks off" the owner has no one-tap verification of Micro's five boundaries, reversal balance, or source integrity — trust is design-implied, never demonstrated
workflow_summary: Zman: /reports → «فحص الآن» → overall banner + 16 Arabic check cards with drift, counts, IDs, suggested fixes; read-only
screen_and_navigation_summary: one panel embedded in the reports page; entry = single button; states = loading/PASS/WARN/FAIL
micro_proposal: full-screen read-only surface «فحص سلامة مالي» under أدواتي (primary) + contextual text-action in مالي truth section; Micro-specific invariants only; per-record source links (stronger than Zman's IDs); suggested fix = text-action to the fixing surface; auto-suggest after import/restore
transfer_recommendation: adapt — the interaction pattern and honesty copy transfer wholesale; the invariant set must be re-derived from Micro's own domain rules
micro_destination: أدواتي → /tools/integrity (new surface route) + مالي doorway
priority: P1 (becomes P0 the moment import/restore is heavily used — post-import verification)
confidence: high
risks: false positives eroding trust (every check must be derived from a tested domain rule, not a heuristic); scope creep into auto-fix (forbid — read-only, fixes happen in their own surfaces); check count inflation (keep ≤10 owner-legible checks)
open_questions: exact invariant list needs a domain pass (correctionHistoryService + cash-continuity + statement reconciliation rules); does the check surface persist last-run results locally (recommend: yes, as a derived cache, not a store)
```

---

### 3.4 UX-04 — Reports & period artifacts + unified payments feed (ZC-15 + ZC-03; MG-13/MG-07 MICRO-WEAKER)

#### A. Zman's actual workflow

**`/reports` page (`src/app/(app)/reports/page.tsx`, 862 lines):**
- Header: title «التقارير» + refresh HeaderIconButton + in-header `SegmentedControl` (underline tone) switching «التقارير» / «الوضع المالي».
- Body: period `SegmentedControl` (كل الفترات / هذا الشهر / آخر 30 يوم); for the balance-sheet section an `asOfDate` date input.
- Sections: P&L summary (net with profit/loss color + lines), **توزيع المصاريف حسب الفئة donut chart** (with legend + values), sales summary, order status distribution, balance sheet (ما تملك: cash+bank+inventory+receivables · ما عليك: held deposits · حقوق الملكية with opening/injections/drawings/retained/capitalAdditions), advanced reconciliation block; `IntegrityCheckReportPanel` embedded.
- **Per-section Markdown download buttons**: `handleDownload` (lines 170–202) → `downloadReport(type, range)` server action returns Arabic Markdown (e.g. balance-sheet MD at `reports/actions.ts:116-157` with tables) → client wraps in **Blob with UTF-8 BOM** → `report_<type>_<YYYY-MM-DD>.md` → toast «تم تحميل <title> بنجاح».

**Payments feed (ZC-03, `PaymentsTab.tsx` + `queries.ts:getPayments` 80–505):** UNION ALL of expense/purchase/receivable, cursor `(createdAt,id)` pagination with `limit+1`, debounced search (400ms → `?search=`), 5-chip kind filter + category dropdown, kind-specific card second lines, ⋯ CardActionSheet, 5s undo-delete, «تحميل المزيد» with next-page-failure protection.

**Happy path (report):** `فتح التقارير (More → التقارير) → اختر «هذا الشهر» → اقرأ الملخص → «تنزيل تقرير الأرباح» → ملف MD عربي في التنزيلات → شاركه واتساب/إيميل`.
**Happy path (feed):** `فتح المالية → تصفية «مصاريف» → فئة «كهرباء» → مراجعة البطاقات → تعديل واحدة عبر ⋯`.

#### B. Proposed Micro appearance

- **Capability name:** **«شارك الكشف»** (share the statement) — export as an owner-language action, not "generate report".
- **Owning tab:** **مالي**. Owning screen: `/finance/statement` (already a cross-context reader opened from Finance and Home). Secondary: an export text-action inside the Finance period layer.
- **Surface type:** **inline action group on the existing statement surface** (surface type 5) — no new page. Two actions in `micro-finance-actions` at the statement's end: «حمّل الكشف نصًا» (Markdown) and later «حمّل نتيجة الفترة». Optionally a share-target via `navigator.share` when available (PWA).
- **Why:** MG-13's core gap is *no downloadable artifact to hand an accountant/lender/family*. Micro already has the exact read model (`statementService.read(from,to)` → `StatementReading` with blocks, sources, truth lines) — the export is a pure presentation function over it: zero new writes, zero schema/export-registry changes (stays outside schema 30/export 22), fully offline (Blob).
- **Format:** Arabic Markdown mirroring the on-screen structure: heading with range (DD/MM/YYYY), cash-in/cash-out blocks with per-line amounts + source labels, corrections with reasons and net effect, period result with its formula sentence, amanah, receivables/payables, and **the truth lines verbatim** («ما يعنيه هذا الكشف» honesty block must be part of the artifact — a Micro signature Zman lacks). UTF-8 BOM + `statement_<from>_<to>.md` naming à la Zman.
- **Screen contract:** states — loading (button disabled while reading), ready, export success («تم تحميل الكشف»), export failure (message + retry), offline (works — pure local read), empty statement (button still yields an honest mostly-zero artifact with truth lines).
- **Safe return:** no navigation; the statement keeps its existing `?from` behavior.
- **Discoverability:** secondary action on a level-2 reading surface; also add a text-action «حمّل نسخة للكشف» in Finance period layer's footer.
- **MVP vs complete:** MVP = statement Markdown export (one function, one button pair). Complete = (a) work-name profitability export from `projectFinancialService` insights (SA-2's optional second), (b) `navigator.share` integration, (c) a "report pack" (statement + period result + integrity verdict in one MD) — only after Pilot demand.
- **Feed pagination: SKIP.** Micro is offline-local with hundreds of records; UNION ALL cursor pagination is a server-scale solution. Micro's collapsible layers (EventsLayer «السجل كاملًا (N حدثًا)») already handle volume honestly. No transfer.

```
finding_id: UX-04
capability_name: تقارير قابلة للمشاركة (statement export artifact) + قائمة مدفوعات موحدة
comparison_classification: MICRO-WEAKER (MG-13/MG-07)
zaman_evidence: src/app/(app)/reports/page.tsx (sections + segmented controls 226-268; handleDownload + BOM Blob 170-202); src/features/reports/actions.ts (downloadReport 90-433; balance-sheet MD 116-157); src/features/finance/components/PaymentsTab.tsx (feed, chips, undo); src/features/finance/queries.ts (getPayments UNION ALL 80-505)
micro_evidence: apps/prototype-web/client/src/pages/Statement.tsx (whole reader; sources 56-79; truth lines 345-353); src/application/finance/statementService.ts (StatementReading read model); src/application/finance/projectFinancialService.ts (insights); application/transfers/localTransferService.ts (JSON backup only — no readable artifact)
user_problem: the owner cannot hand an accountant/lender/family a period document — every Micro reading is on-screen and data-local
workflow_summary: Zman: /reports → period toggle → per-section MD downloads with BOM + dated filenames. Micro: /finance/statement → read on screen → (no export)
screen_and_navigation_summary: Zman = dedicated reports page with two tabs + embedded integrity panel; Micro = statement reader + finance layers, no reports page needed
micro_proposal: «شارك الكشف» action group on /finance/statement (Markdown with BOM, offline Blob, DD/MM/YYYY range, truth lines included verbatim) + later work-name profitability export; skip feed pagination entirely (local scale)
transfer_recommendation: adapt — export-the-read-model is a cheap, boundary-respecting win; reports *page* and pagination do not transfer
micro_destination: مالي → /finance/statement (export action) + period layer footer action
priority: P1
confidence: high
risks: Markdown readability for non-technical recipients (mitigate: table layout like Zman's; PDF later via documents pipeline); truth lines make the artifact longer (keep — they are the product's honesty signature); filename/i18n conventions must follow the English-digits rule
open_questions: format decision (MD vs TXT vs both — flagged by SA-2); does the QuickActionSheet need a «شارك» action (recommend: no — reading, not recording)
```

---

### 3.5 UX-05 — Assets & depreciation (ZC-10; MG-10 ZAMAN-ONLY, gated)

#### A. Zman's actual workflow

**Entry points:** (1) SmartFinanceForm mode «أصل للورشة» + `wantDepreciation` checkbox → `DepreciationPromptModal` immediately after save (useful-life months with worked example); (2) More menu → `/assets`; (3) PaymentsTab ⋯ on asset cards → «إيقاف الإهلاك» confirm.

**Screens:**
- **`DepreciationPromptModal`** (`src/features/depreciation/components/DepreciationPromptModal.tsx`): asks useful life (1–600 months) right after the asset is saved — progressive disclosure at the moment of highest relevance, with the monthly-amount arithmetic shown.
- **`/assets` (`src/features/depreciation/AssetsScreen.tsx`, 662 lines):** header «الأصول الرأسمالية» → two sections: **«أصول بلا إهلاك»** (capital expenses without a `capital_asset` — previously invisible, made visible by PROMPT_FINANCE_RESTRUCTURE Phase 1) and **«تحت الإهلاك»** (per-asset card: original value, depreciated-to-date, NBV, monthly amount) → per-card ⋯ bottom action sheet: «تعديل بيانات الأصل» (name/date/life — re-derives future depreciation) and «إيقاف الإهلاك» (confirm dialog; soft-deletes the capital_asset; the expense row and its cash movement remain) → empty state.
- **Mechanics (UX-visible consequences):** read-time computed depreciation (no scheduled jobs); started retroactively at purchase date; last month sweeps the remainder; P&L deducts period depreciation while the balance sheet stays pure cash-basis — and the FinanceComparePanel educates: «شهر الشراء قد يظهر خسارة وهذا صحيح».

**Happy path:** `FAB → «أصل للورشة» → اسم + قيمة → فعّل «توزيع الإهلاك شهريًا» (مثال محسوب) → حفظ → مودال الإهلاك: 24 شهرًا → الأصل يظهر في /assets تحت الإهلاك، وخصم شهري في الربح التشغيلي`.
**Edge paths:** late entry → retroactive depreciation from purchase month; stop depreciation → confirm → future P&L unaffected, history intact; fully depreciated → IC-14 WARN with remaining book value.

#### B. Proposed Micro appearance

**Verdict: REJECT for now — deliberately gated.** `docs/decisions/remaining-capabilities-review-v1.md` lists «أصول، إهلاك، قروض، أجور، ضرائب…» as «مؤجل بعقد متخصص… لا؛ لا نخمن قواعدها». The only Micro hook is `loss_non_cash` (period-profit reduction without cash — `src/domain/financial-event/types.ts`). Building an asset register on Zman's rules would *guess the contract Micro explicitly refuses to guess* (family/methods/Jordanian norms/disposal).

**When the contract exists, the transfer design is ready (design-time transfer only):**
- **Capability name:** «أدوات وأجهزة المشروع» (project tools & equipment) — never "fixed assets".
- **Owning tab:** مالي; surface: **deep editor family** `/finance/new/asset` + a **reading surface** `/finance/assets` (surface kind, keeps nav) listing «معدات بلا توزيع» / «موزّعة على عمرها» — mirroring Zman's two-section honesty (the "untracked/un-depreciated capital spend" visibility fix is the single most important Zman lesson here: never let big purchases become invisible).
- **Entry UX to preserve:** the two-step progressive disclosure (record purchase → *then* offer «وزّع تكلفته على عمره؟» with a worked example «فرن بـ 360 د.أ / 36 شهر = 10 د.أ شهريًا») — Zman's DepreciationPromptModal is the best-in-class pattern for this persona; a first-screen form asking useful-life upfront would be worse.
- **States:** edit (re-derive future), stop (confirm with stated consequences «لن يُخصم من الفترات القادمة؛ التاريخ محفوظ»), read-time computation, fully-depreciated honest state.
- **MVP vs complete:** MVP (post-contract) = straight-line monthly, retroactive start, sweep remainder, stop-with-reason. Complete = disposal/partial-year/IC-14-style valuation check.
- **Priority:** P2 (gated; low frequency for home micro-businesses — MG-10).

```
finding_id: UX-05
capability_name: الأصول والإهلاك (asset register + read-time depreciation)
comparison_classification: ZAMAN-ONLY (MG-10, deliberately deferred)
zaman_evidence: src/features/depreciation/AssetsScreen.tsx (sections 141-163; edit modal 256-260; stop confirm 274-321; per-card action sheet 328-350); src/features/depreciation/components/DepreciationPromptModal.tsx; src/features/depreciation/actions.ts (addCapitalAsset:59, updateCapitalAsset:282); SmartFinanceForm.tsx (wantDepreciation + example 1253-1270); docs/ACCOUNTING_RULES.md §10
micro_evidence: docs/decisions/remaining-capabilities-review-v1.md (مؤجل بعقد متخصص); src/domain/financial-event/types.ts (loss_non_cash 69-74); no asset register anywhere in storage/local/types.ts
user_problem: a sewing machine or oven purchase cannot be spread over its life; the period result is overstated for asset-heavy crafts (real but rare for the persona)
workflow_summary: Zman: asset mode → depreciation prompt (useful life) → /assets two sections → edit/stop with confirms; depreciation computed at read time, monthly amount immutable, last month sweeps
screen_and_navigation_summary: modal chain + dedicated screen + per-card action sheet; entry from unified form and More menu
micro_proposal: REJECT now (contract-gated). When built: مالي deep editor /finance/new/asset + reading surface /finance/assets with the two-section honesty pattern and the two-step «وزّع تكلفته على عمره؟» prompt with worked example; straight-line + sweep; stop-with-reason; loss expressed through loss_non_cash
transfer_recommendation: reject (now) + design-time adapt (pattern bank) — Micro's own contract must define the rules first
micro_destination: (future) مالي → /finance/assets + /finance/new/asset
priority: P2
confidence: high
risks: guessing Jordanian norms (the exact thing Micro forbids); persona mismatch (low frequency); if built without contract it would corrupt period-result honesty
open_questions: the specialized contract itself (family, straight-line?, disposal, partial months) — outside UX scope; whether «أصول بلا إهلاك»-style visibility of big purchases could be served TODAY by a reading-layer note (INFERENCE: period layer could flag large one-off costs without any asset semantics — candidate for Pilot observation)
```

---

### 3.6 UX-06 — Unified activities feed (ZC-14/activities route; MG-12 MICRO-INCOMPLETE, MG-11 adjacent)

#### A. Zman's actual workflow

**Entry point:** More sheet → group «المتابعة والتحليل» → «سجل النشاط — تصفح الحركات بترتيبها الزمني» → `/activities`.

**Screen — `src/app/(app)/activities/page.tsx` (94 lines):** header «كل الحركات المالية» → one chronological list (order/sale/expense/purchase) where each row = type icon in tinted square + bold title + `yyyy-MM-dd HH:mm` timestamp + **signed amount (+ green for order/sale, − warn for expense/purchase, «—» when no cash impact)** + trailing arrow. **Every row deep-links to the record's editing surface with URL params**: order → `/orders?view=<id>`, sale → `/finance?tab=sales&editSale=<id>`, expense → `/finance?tab=payments&editExpense=<id>`, purchase → `…editPurchase=<id>`. Skeleton ×8, error state with retry, empty state with a starting hint. Feed from `getRecentActivities` (dashboard queries).

**Happy path:** `المزيد → سجل النشاط → تصفح آخر الحركات → «مصروف كهرباء −12.500» → نقرة → يفتح المالية بوضع التعديل لهذا المصروف مباشرة`.
**Edge paths:** no cash impact (write-off/receivable) → «—» dash; error → retry.

#### B. Proposed Micro appearance

- **Capability name:** **«آخر ما صار»** (what happened lately) for the Home block; **«سجل كل ما صار»** for the full reader.
- **Owning tab:** **مشروعي الآن** (Home) — but strictly as an *extension of the existing block*, respecting the decision-first principle that made SA-2 hesitate.
- **Current Micro state (verified):** Home already renders «ما تغير مؤخرًا» capped at **5** rows from `homeControlCenterService.ts:398-423` (orders + drafts + financial events + schedules), each row = date + title + optional detail + deep link — but: **direct sales are missing** (they appear only in the away-section's last-activity math, lines 431–437), **corrections are missing**, **cash entries are missing**, and financial events link *generically to `/finance`* rather than to the focused event row (the `?event=` focus param that Finance already supports!). EventsLayer on Finance shows the full events list («السجل كاملًا (N حدثًا)») but only financial events.
- **Proposal — two tiers:**
  1. **Minimum (high confidence):** enrich the existing Home read model — add direct sales (recorded + revisions), corrections, and wallet entries; make the financial-event rows link `withFrom('/finance?layer=events&event=<id>', '/')` so one tap focuses the exact row in the events layer (the deep-link vocabulary already exists); keep the cap (5–7) and keep the block below «مسارات مرتبطة فقط». No new surface, no new store, no clutter.
  2. **Complete (needs UX decision):** a «مزيد» text-action at the block's end → a full-screen read-only **«سجل كل ما صار»** reader (surface kind, keeps nav) at an `/activities`-equivalent (suggest `/finance/activity` with `?from=/`), built on the same unified read model (orders' events, directSales revisions, financialEvents, cashContinuityEntries, inventory movements, corrections), each row deep-linking to its focused record via existing params (`?event=`, `/orders/:id`, `/cash/wallet/:id`, `/inventory/movement/:id`). This answers Zman's /activities question «شو صار اليوم/هالأسبوع؟» in one list — the MG-12 gap — without adding a seat or a dashboard.
- **Surface type:** tier 1 = inline block (existing); tier 2 = full-screen reader.
- **States:** empty (block hidden — already the behavior), loading, per-row kind icon + honest amount semantics (+in/−out or «—» for non-cash like corrections/reversals — Micro's honesty demands the dash, not a fake number), source links preserved.
- **Safe return:** reader uses `?from=/` (or its opener); rows use `withFrom` to return to the reader.
- **Discoverability:** primary = Home block (bounded); secondary = the reader's link from Finance's truth section («سجل كل ما صار») — matching how «كشف الفترة» is doorway-linked today.
- **RTL/digits:** rows are RTL text with LTR-isolated dates/amounts; relative day labels in Arabic.

```
finding_id: UX-06
capability_name: طبقة النشاط الموحدة (unified recent-activity layer)
comparison_classification: MICRO-INCOMPLETE (MG-12; MG-11 adjacent)
zaman_evidence: src/app/(app)/activities/page.tsx (feed rows 49-89; deep links 53-57; states 24-47); src/features/dashboard/queries.ts (getRecentActivities:275); src/config/nav.ts (More group 86-90)
micro_evidence: apps/prototype-web/client/src/pages/Home.tsx (ما تغير مؤخرًا 412-440); src/application/home/homeControlCenterService.ts (recentChanges 398-423; missing directSales/corrections; events → /finance generic); src/components/finance/EventsLayer.tsx (full events list + ?event focus); src/pages/Finance.tsx (layer=events 961); docs/contracts/26 (focus/event vocabulary)
user_problem: "شو صار اليوم/هالأسبوع؟" across orders, sales, expenses, payments requires visiting 4+ surfaces; Home's block covers only 4 record kinds and links events generically
workflow_summary: Zman: More → /activities → one chronological list → one tap opens the exact record in edit mode. Micro: Home block (5 rows, partial kinds) + separate layers per domain
screen_and_navigation_summary: one list page with per-kind icons, signed amounts, deep links; skeleton/error/empty
micro_proposal: tier 1 = enrich Home's existing block (add direct sales, corrections, wallet entries; event rows link with ?event= focus) keeping cap 5-7; tier 2 = «مزيد» → full-screen read-only «سجل كل ما صار» reader over existing stores (read model, no new writes), rows deep-link to focused records
transfer_recommendation: adapt — the question transfers, the surface does not; Micro answers it with a bounded Home block + one reader, never a seat or dashboard
micro_destination: مشروعي الآن → Home block (+ reader route /finance/activity if tier 2 approved)
priority: P2 (tier 1 could ride any Home iteration cheaply)
confidence: high (tier 1); medium (tier 2 — Home clutter tension flagged by SA-2)
risks: Home clutter vs decision-first principle (mitigate: cap + same visual weight as today + «مزيد» not inline expansion); read-model drift across 6+ stores (derive in one service like homeControlCenterService, test with fixtures)
open_questions: tier-2 route placement (/finance/activity vs /tools — recommend finance family); should corrections appear as rows (recommend: yes, labeled «تصحيح» with net-effect dash/amount)
```

---

### 3.7 UX-07 — Mobile RTL UX contracts (ZC-24)

#### A. Zman's actual contracts (see §1.4 for evidence paths)

The transferable contract set: (1) **5-second undo-delete** with timer-commits-not-toast, pagehide best-effort, online-guard, past-tense-after-server; (2) **MoneyInput** discipline (single dot, leading zeros, focus/blur formatting, currency suffix pinned, Eastern-Arabic + currency-label stripping in `parseJodToFils`); (3) **header stability** (one row, fixed height, no conditional header filters, body chips flex-wrap, RTL order title→context→search→filter→tools); (4) **Action Dock** status matrix (one primary per state, data-gated secondaries, destructive separated); (5) **empty states that teach** (3 steps + direct action); (6) **financial actions explain effect before and after**; (7) per-kind second lines in list cards; (8) pagination that never drops loaded rows.

#### B. What Micro already has (verified) — and what to import

Micro already equals or beats Zman on: RTL logical properties + `dir="rtl"` shell; 48px targets; English digits + DD/MM/YYYY (a *different*, deliberate numeric contract — do NOT import Zman's ar-JO numerals); Arabic plurals; UnsavedChangesGuard (3-choice, focus-trapped, sentinel history — stronger than Zman's modals for editor exits); CorrectionPreview with before/after (stronger than Zman's confirmations for financial corrections); deep-link vocabulary and safe return (Zman has nothing equivalent — its modals-over-page approach is *weaker* for intent preservation).

**Import list (pattern-level, no code):**
1. **Undo-delete for non-financial destructive actions (P2):** Micro's destructive pattern today is two-step inline confirm (Tools estimate delete «احذف «X» نهائيًا؟ لا يمكن التراجع» + احذفه/تراجع). For *financial* records Micro's correction/reversal model is stronger and must stay. For **non-financial, recoverable-by-recreation records** (estimates, drafts already guarded differently, future snippets if ever), Zman's 5s undo is a lighter, friendlier pattern: tap delete → row optimistically hidden → toast «سيُحذف… — تراجع» → commit. Adapt Micro-offline: since writes are local and instant, the undo window can *actually restore* (no server race) — simpler than Zman's online-guarded version.
2. **Header anti-jitter rule as written law (P1 documentation):** Micro's AppHeader is already stable (brand + one context label + 2 icon buttons). Codify in the design contract: "no conditional rows above content; filters live in body chips, wrap never scroll" — this prevents future groups from re-introducing Zman's pre-v2.2 problem (PR #35 revert).
3. **MoneyInput paste-tolerance (P2):** Micro's `EnglishNumberInput` normalizes Arabic-Indic digits on change (already Zman-parity for the digit problem). Missing: Zman's stripping of «د.أ»/«JOD»/«دينار» when pasting a formatted amount. One helper in `application/input/englishNumeric.ts` closes it.
4. **Effect-explaining copy discipline (P1):** Micro already does this («لا يغيّر هذا الحدث نتيجة طلب قائم…», «الدفع يخفض ما بقي… ولا يسجل مصروفًا مرة ثانية») — formalize Zman's rule wording in the Micro design contract so every new financial button ships with its before-effect line.
5. **Teaching empty states (P2):** Micro's empty copies are honest but rarely instructional; Zman's 3-step pattern (go here → do this → then that + button) is cheap and proven for first-run surfaces.
6. **Status-driven action matrix (P1 documentation):** write Micro's own Action Dock equivalent for OrderDetail (readiness → deliver → settle) as a contract table like Zman §9, gating secondaries on real data — Micro's OrderDetail already behaves this way; writing it down protects it.

**Reject:** Zman's ResponsiveModal-over-page create/edit model (Micro's deep-editor + `?from` + UnsavedChangesGuard is strictly better for intent preservation and offline PWA); Zman's 3-decimal fils display (Micro's 2-decimal JOD is its own systemic rule); Zman's ar-JO digit formatting in `Intl` (Micro mandates English digits).

```
finding_id: UX-07
capability_name: عقود تجربة الهاتف RTL (undo-delete، إدخال المال، ثبات الرأس، مصفوفة الأفعال)
comparison_classification: MICRO-SUFFICIENT (pattern-level) — no MG entry; ZC-24 source
zaman_evidence: src/lib/undo-delete.ts (5s pattern); src/components/shared/MoneyInput.tsx + src/lib/money.ts (parseJodToFils 25-57); docs/HEADER_AND_HOME_V2_2_CONTRACT.md + docs/HEADER_CONCEPT_V2_3_CONTRACT.md; docs/DESIGN_SYSTEM_V2_1_CONTRACT.md (§3.5, §8, §9); src/components/shared/EmptyState.tsx
micro_evidence: apps/prototype-web/client/src/components/forms/EnglishNumberInput.tsx (normalizeAsciiDigits on change 76-78); src/application/input/englishNumeric.ts; src/components/forms/UnsavedChangesGuard.tsx (3-choice + sentinel); src/components/finance/CorrectionPreview.tsx; src/components/layout/MicroAppShell.tsx (stable AppHeader); src/presentation/formatters.ts (English digits + DD/MM/YYYY rule)
user_problem: none open today; the risk is regression — future capability groups re-introducing modal-create, conditional headers, or paste-hostile money fields
workflow_summary: Zman codified its phone-RTL craft in three binding contracts + a lib (undo-delete) + a component (MoneyInput); Micro has equivalent-or-stronger primitives but fewer written laws
screen_and_navigation_summary: cross-cutting; not a screen
micro_proposal: import as written law + small helpers: (1) 5s undo-delete for non-financial deletes only; (2) header anti-jitter rule in the design contract; (3) currency-label stripping in englishNumeric paste path; (4) effect-before-action copy rule; (5) 3-step teaching empty states; (6) status-driven action matrix documented for OrderDetail. Reject Zman's modal-create model, fils display, ar-JO digits
transfer_recommendation: adapt (pattern bank + contract wording; almost no code)
micro_destination: cross-cutting — components/forms + docs/design-system + docs/contracts
priority: P1 (documentation rules) / P2 (undo-delete + paste helper)
confidence: high
risks: undo-delete misapplied to financial records (forbid — corrections path is stronger); contract drift if rules are not enforced in review (same PR-gate ritual Zman uses)
open_questions: whether Micro wants a written design-system contract file mirroring Zman's three (recommend: fold into docs/product/design-system-v1.md update)
```

---

### 3.8 UX-08 — Order→sale conversion + deposit reclassification (ZC-06; MG-05 MICRO-SUFFICIENT, reject)

#### A. Zman's actual workflow

**Entry point:** OrderDetail's **sticky Action Dock** (`OrderDetail.tsx:596-680`): status-driven primary button («تم التسليم» for confirmed) + conditional secondaries (رد أموال العربون when deposit>0; «تسجيل إيراد مباشرة» for draft/sent; «عكس التسليم» for delivered; «عكس احتجاز العربون» for cancelled-with-forfeitureSale).

**Conversion — «تأكيد تحويل الطلب إلى مبيعات» modal (696–724):** copy enumerates the full effect *before* commit: «سيتم ترحيل كامل المبلغ المتبقي (X) إلى الصندوق كإيراد مبيعات (يشمل الأرباح الإضافية)، وتحويل العربون المحصَّل إلى إيراد، وتحديث حالة الطلب إلى تم التسليم» + إلغاء/«تأكيد التحويل». Server: atomic transaction — reclassify deposit movement (sourceType deposit→sale «محوَّل من عربون»), insert remainder movement, `deductForDelivery` stock movements, status→delivered, idempotency key, audit.
**Reverse — «تأكيد عكس التسليم» modal (887–924):** numbered list of 4 effects (reclassify back, delete remainder, delete sale, status→confirmed) + the reassurance note «النقد الفعلي في الصندوق لا يتأثر — العربون كان محفوظاً كنقد منذ بدايته» + warn-colored confirm.
**Refund modal:** date + amount (validated ≤ remaining deposit) + account + notes — an independent out-movement that reduces the refundable liability.
**Forfeit — «تأكيد الاحتفاظ والإلغاء» (833–885):** explains «سيتم احتجاز المتبقي كإيراد تسوية، وتسجيل القرار على الطلب، ثم نقله إلى «ملغى». لا تُنشأ حركة نقدية جديدة لأن المال دخل الصندوق سابقاً» — revenue without a new cash movement; reversible via «عكس احتجاز العربون» (1066–1070) which reclassifies back and soft-deletes the forfeiture sale.

#### B. Micro proposal

**Verdict: REJECT the mechanics; Micro already covers the *UX contracts* the flow was invented to deliver.**
- Micro's revenue moment is the status transition «تم التسليم» (OrderDetail) — no conversion button, no sale record, no reclassification; collection events are independent cash facts. This is deliberate (contract 02 order lifecycle; MG-05): the deposit reclassification dance exists *only because* Zman books revenue as a sale row; Micro's event-sourced model doesn't need it.
- Micro's equivalents (all verified stronger or equal at UX level): deposit settlement on cancelled orders = **three documented options with reason** (ردّ/احتفظ/يحتاج مراجعة — OrderDetail 770–831) vs Zman's refund/forfeit pair; per-collection reversal with **cumulative-cap validation and CorrectionPreview before/after** (547–703) vs Zman's plain confirm; price correction with unchanged-list (388–407).
- **The two things worth keeping as law:** (1) *every financial action must name its cash effect explicitly in the confirm copy* — including the negative case («لا تُنشأ حركة نقدية جديدة…») which Micro already writes; (2) *every financial action needs its documented inverse* — Micro has reversal for collections, movements, supplier payments, cash entries, and inventory waste (`deepFlowPatterns` covers all). Zman's discipline of shipping reverse-actions from day one is the law to keep, not the reclassification machinery.

```
finding_id: UX-08
capability_name: تحويل الطلب لمبيعة + إعادة تصنيف العربون + العكس الكامل
comparison_classification: MICRO-SUFFICIENT (MG-05) — reject
zaman_evidence: src/features/orders/components/OrderDetail.tsx (Action Dock 596-680; convert modal 696-724; reverse modal 887-924; forfeit 833-885 + reverse-forfeit 1066-1070; refund cap); src/features/finance/actions.ts (convertOrderToSale:1441, reverseSale:1650, refundOrder:1787, forfeitDeposit:2020, reverseDepositForfeiture:2238); docs/DESIGN_SYSTEM_V2_1_CONTRACT.md §9 (dock matrix)
micro_evidence: apps/prototype-web/client/src/pages/OrderDetail.tsx (تم التسليم 290-302; deposit settlement 3 options 769-831; collection reversal + CorrectionPreview 547-703; price correction 388-407); docs/contracts/02-order-lifecycle-contract.md; src/pages/Finance.tsx (DepositsLayer 395)
user_problem: none for Micro's model — the Zman flow solves a bookkeeping problem (revenue-as-sale double-counting) Micro doesn't have
workflow_summary: Zman: confirmed order → «تم التسليم» → convert modal enumerating reclassifications → atomic sale+cash+stock; delivered → reverse modal with 4-effect list; cancelled → forfeit/reverse-forfeit without cash. Micro: readiness → «تم التسليم» (revenue recognized) → settlements/corrections as documented events with previews
screen_and_navigation_summary: Zman = status-driven Action Dock + 4 modals; Micro = status-driven buttons + CorrectionPreview sheets
micro_proposal: reject the conversion/reclassification machinery; adopt (already present, keep as law): explicit cash-effect copy in every confirm (incl. «لا حركة نقدية») and documented inverse for every financial action; Micro's three-option deposit settlement is the stronger UX — keep it
transfer_recommendation: reject — contradicts collection≠profit and explicit-evidence boundaries; Micro's settlement review + corrections discipline already deliver the UX goals
micro_destination: n/a
priority: P2 (documentation-level keep: inverse-action law + cash-effect copy rule)
confidence: high
risks: a Zman-trained owner may look for «أغلق الطلب» one-tap closure (INFERENCE, MG-05) — monitor in Pilot, do not build
open_questions: none material
```

---

### 3.9 UX-09 — Non-cash inventory write-off (ZC-18)

#### A. Zman's actual workflow

**Entry point:** `/inventory` FAB → «تعديل سريع للمخزون» → `QuickAdjustStockForm` (direction صرف, value>0) — write-off is a *flavor* of manual adjustment, not a separate flow.

**Mechanics (UX-visible):** one transaction writes a `catalog_movement(out)` with weighted-average cost + a **shadow expense row** (category «هدر/تلف مخزون», `isInventoryWriteoff=true`, no cash movement). In the payments feed the write-off appears as a **gray, read-only card** («تسوية مخزون تلقائية», no ⋯ menu, no edit/delete — «محروسة من التعديل والحذف»); attempting to open it in edit mode produces the honest answer: «هذا مصروف تلقائي… لا يمكن تعديله أو حذفه من هنا — صحِّح المخزون من شاشة الكتالوج» (PaymentsTab 696–711). P&L carries `inventoryWriteOffCents` as its own line; **no reverse-writeoff exists** (م-5 known gap).

**Happy path:** `المخزون → إجراءات المخزون → تعديل سريع → صنف «تربة» صرف 3 وحدات بسبب → حفظ → الرصيد ينقص، القيمة الدفترية تنقص، الربح الشهري ينقص بلا خروج نقدي، بطاقة رمادية في المدفوعات`.
**Edge paths:** edit/delete attempts → blocked with redirect-to-source copy; reversal → impossible (gap).

#### B. Micro proposal

**Verdict: Micro's write-off is already a first-class, *reversible*, reasoned movement — stronger than Zman's.** Verified: `InventoryMovementEditor` supports `waste` with **mandatory reason** and `wasteContext` (order/catalog/template/general/unallocated); `InventoryMaterials` offers the full-remaining shortcut «أخرِج المتبقي» (القرار ۲۰) with the honest panel copy «سيُسجَّل هدر… لا حذف ولا شطبًا بلا أثر. يصير مخزون المادة بعدها صفرًا صادقًا والقيمة تظهر في الهدر»; every movement row offers «تراجع موثق» (`InventoryReversalEditor`); waste feeds insights (`projectFinancialService.ts:276`) — the Zman "dual-entry" accounting effect is achieved with a *single* movement type plus read-time effects, which is architecturally cleaner and fully reversible.

**The one real UX gap worth closing:** **waste is invisible in the مالي events layer.** Zman surfaces the loss where the owner reads money (gray read-only card in the payments feed); Micro's waste lives only in `/inventory`'s movement log and period insights — an owner scanning «السجل والأثر» never sees that 20 د.أ of material evaporated. Proposal: EventsLayer (or the Finance truth strip) gains read-only rows for inventory waste movements: «هدر مخزون — بلا خروج نقد» with amount and a `withFrom` link to `/inventory` (or the movement row). Clearly labeled non-cash (Micro's dash convention, not a fake expense row); no new writes; pure read model join.

```
finding_id: UX-09
capability_name: شطب المخزون غير النقدي (dual-entry movement + shadow expense)
comparison_classification: MICRO-SUFFICIENT at mechanics level (MG-02-adjacent; SA-1 ZC-18 flagged the dual-entry as transferable — this analysis finds Micro's single-movement model stronger)
zaman_evidence: src/features/inventory/actions.ts (adjustStock write-off insert 551-575); src/features/finance/components/PaymentsTab.tsx (gray read-only card 410-427; auto-expense guard 696-711); CLAUDE.md §2/م-5 (no reverse-writeoff gap)
micro_evidence: apps/prototype-web/client/src/pages/InventoryMaterials.tsx (أخرِج المتبقي panel 316-366); src/pages/InventoryMovementEditor.tsx (waste + mandatory reason 157; wasteContext fields 40-46); src/pages/InventoryReversalEditor.tsx; src/domain/inventory-material/types.ts (waste type + WasteContext); src/application/finance/projectFinancialService.ts (waste filter 276)
user_problem: (Micro today) the owner reading مالي does not see material losses — waste is only visible in the inventory movement log; (Zman's problem is solved in Micro by reason+reversal)
workflow_summary: Zman: quick adjust out → shadow expense + gray immutable card in payments; no reverse. Micro: waste movement with mandatory reason + context (partial or full) → reversible via documented reversal → feeds period insights
screen_and_navigation_summary: Zman = one form + read-only card; Micro = movement editor + extract-remaining panel + reversal editor
micro_proposal: keep Micro's model entirely; add read-only «هدر مخزون — بلا خروج نقد» rows (amount + source link) surfaced in مالي's events layer/truth strip so losses are visible where money is read; no shadow records, no immutability guards needed (movements are append-only with reversals)
transfer_recommendation: reject (mechanics) + adapt (visibility row) — Micro's reasoned, reversible waste movement is the stronger design
micro_destination: مالي → EventsLayer read-model extension (source: /inventory)
priority: P2
confidence: high
risks: read-model join across inventory + financial events must stay cheap (local stores, trivial); labeling must never imply cash left (dash + «بلا خروج نقد»)
open_questions: should the waste row also appear in the Home recent block (tier-1 of UX-06) — recommend: yes via the same enrichment
```

---

## 4. Cross-capability UX patterns worth importing

Ranked by value-to-effort for Micro:

1. **«يقرأ فقط — لا يغيّر شيئًا» verification tools (from ZC-16's check panel):** the read-only self-audit posture with PASS/WARN/FAIL + Arabic titles + suggested next action. The single highest-trust pattern Zman owns; Micro has the read models and the precedent (CashCount) but no surface. → UX-03.
2. **Effect-explaining copy before every financial commit** (Zman design system §3.5; SmartFinanceForm hint lines; convert/reverse modal effect lists; forfeit's «لا تُنشأ حركة نقدية جديدة»): Micro already writes this in places (SupplierPurchaseEditor lines 300–303, FinancialEventEditor effect card) — make it a review-gate rule for every new money button. Nearly free, prevents the classic microbusiness error of pressing the wrong kind of record.
3. **Shareable reading artifacts (BOM + dated filename + truth lines):** export-the-read-model, not build-a-report-page. → UX-04.
4. **Lazy vocabulary enrollment + trim + orphan-merge (ZC-02):** the proven antidote to free-text chaos for any future owner vocabularies (expense tags now; agreement templates or work names later).
5. **5-second undo-delete (timer commits, not dismissal; online-guard) — restricted to non-financial deletes:** estimates today, snippets if ever built. Micro's offline-local writes make the undo *actually* restore, removing Zman's server-race complexity. Financial deletes keep Micro's correction/reversal discipline.
6. **Teaching empty states (title + description + ≤3 steps + direct action):** cheap first-run onboarding for /inventory, statement, and the future integrity screen.
7. **Stated-consequences confirmation dialogs for participation/state changes** (Zman's untrack dialog): the template for any future Micro flow that switches a record family off (inventory deactivation, wallet archival) — name the number, name what future actions will see, name what happens to history.
8. **Status-driven action matrix as documented contract** (Zman design system §9): one primary action per state, secondaries gated on real data, destructive actions separated. Micro's OrderDetail already implements it; writing it down protects it from future groups.
9. **Header stability law + body-chips filtering:** anti-jitter rules to fold into Micro's design docs before more surfaces exist.
10. **Kind-specific card second lines + dash-for-non-cash convention:** from ZC-03's unified feed — Micro's EventsLayer and the future activity reader should show per-kind second lines (source, reason, context) rather than uniform rows.

Explicitly *not* imported despite being excellent in Zman: UNION-ALL cursor pagination (server-scale problem), modal-over-page create/edit (inferior to Micro's deep editors + guard), More-sheet navigation (Micro has a cleaner 5-seat + tools model), dashboard analytics panels (identity conflict, MG-15).

---

## 5. What should NOT transfer on UX grounds

| Zman pattern | Why rejected for Micro | Evidence |
|---|---|---|
| **Six-item sidebar + 4-seat bottom bar + grouped "More" sheet** | Micro's five seats + أدواتي + settings-in-header is a finished, tested navigation identity; a More sheet would re-fragment it (Micro's module states list in Tools already plays the "everything else" role honestly) | `zman src/config/nav.ts` vs `micro navigation.ts` + `Tools.tsx` |
| **Dashboard panels (monthly profit trend, compare bars, liquidity flow, advisor)** | Direct identity conflict with Home's decision-first principle (MG-15); Micro's Finance period layer owns reading, and the product forbids "final net profit" wording Zman's panels imply | `zman features/dashboard/components/*` vs `micro pages/Home.tsx` «الأهم الآن» |
| **Modal-over-page create/edit (`ResponsiveModal` + URL params)** | Loses UnsavedChangesGuard protection, deep-link intent, and offline refresh-safety; Micro's route-based deep editors with `?from` are strictly stronger for a PWA | `zman SmartFinanceForm` in modal vs `micro routeClassifier.ts` + `UnsavedChangesGuard.tsx` |
| **Revenue-as-sale conversion button + deposit reclassification modals** | Solves a double-counting problem Micro doesn't have (event-sourced collections); the reclassify-in-place + soft-delete machinery contradicts append-only corrections with reasons | UX-08 dossier |
| **Auto-deduct inventory on delivery + auto-capitalization of tracked purchases** | Violates Micro's explicit-evidence and purchase≠COGS boundaries (MG-02; contracts 11/13); the *purchase→receipt bridge* is the honest version | UX-02 dossier |
| **ar-JO numerals + 3-decimal fils display** | Micro's systemic rule is English digits + 2-decimal JOD (Group 6 item 5); importing display conventions would break 17 routes' formatting consistency | `zman lib/money.ts` vs `micro presentation/formatters.ts` |
| **Login/passcode + idle lock + WhatsApp automation + partial JSON backup** | Rejected in Round 1 (MG-16/19/18/21); no UX argument changes those verdicts (offline-first, local-only, CSP posture; Micro's backup is full+verified+restorable) | SA-2 §4 |
| **Zman's own known UX debt** | Do not import: no-UI `?nature=` filter (م-2), no reverse-writeoff (م-5), duplicated seeded categories (م-11) — Micro's designs already avoid each | SA-1 open questions; CLAUDE.md known issues |
| **Per-tab fixed-label FAB** | Micro's centered `سجّل` FAB with the 5-action sheet is a stricter and better contract (one recording door, transitory actions, deep editors for correction) | `zman FloatingActionButton` per-tab labels vs `micro QuickActionSheet.tsx` |

---

## 6. Evidence index

### Zman (repo `zman`, `artifacts/zman-app/`)
| Path | Used for |
|---|---|
| `docs/DESIGN_SYSTEM_V2_1_CONTRACT.md` | 48px targets, effect-before-action rule, destructive stacking, bottom-sheet/FAB rules, Action Dock matrix, RTL/zoom laws |
| `docs/HEADER_AND_HOME_V2_2_CONTRACT.md` | one-header-row law, anti-jitter, home ordering |
| `docs/HEADER_CONCEPT_V2_3_CONTRACT.md` | RTL header order, title full-width rule |
| `src/config/nav.ts` | 6 sidebar / 4 bottom / 3 More groups with descriptions |
| `src/components/layout/AppShell.tsx` | shell + header slot |
| `src/lib/undo-delete.ts` | 5s undo-delete full contract |
| `src/lib/money.ts` | parseJodToFils Eastern numerals + currency stripping; formatFilsToJod |
| `src/components/shared/MoneyInput.tsx` | input discipline, RTL currency suffix |
| `src/components/shared/EmptyState.tsx`, `ErrorState.tsx`, `CardActionSheet.tsx`, `ConfirmDialog.tsx`, `InfoTooltip.tsx` | shared states |
| `src/features/finance/components/SmartFinanceForm.tsx` | 4-mode selector, hints, category select/custom, tracked preview, unit-price preview, depreciation checkbox |
| `src/features/finance/components/PaymentsTab.tsx` | filter modal + chips, undo-delete wiring, gray write-off cards, auto-expense guard, load-more failure guard |
| `src/features/finance/components/FinanceCatalogModal.tsx` | category CRUD |
| `src/features/finance/actions.ts` | createExpense/ensureExpenseCategoryInCatalog/seed; convertOrderToSale/reverseSale/refundOrder/forfeitDeposit/reverseDepositForfeiture; runFinancialIntegrityCheckAction |
| `src/features/finance/queries.ts` | getPayments UNION ALL; getExpenseCategories/getDistinctExpenseCategories |
| `src/features/finance/integrityCheck.ts` | IC-1..IC-16 |
| `src/features/inventory/InventoryScreen.tsx` | low-stock banner, stats, FAB action sheet, empty onboarding |
| `src/features/inventory/components/AddTrackedItemForm.tsx`, `QuickAdjustStockForm.tsx` | quick forms |
| `src/features/inventory/actions.ts` | adjustStock dual-entry write-off |
| `src/app/(app)/catalog/CatalogClient.tsx` | tracked toggle, openingStock, untrack confirm |
| `src/features/reports/components/IntegrityCheckReportPanel.tsx` | فحص الآن panel |
| `src/app/(app)/reports/page.tsx` | tabs/periods/sections; BOM Blob download |
| `src/features/reports/actions.ts` | downloadReport MD; balance-sheet MD |
| `src/app/(app)/activities/page.tsx` | activities feed + deep links |
| `src/features/depreciation/AssetsScreen.tsx` | two sections, edit/stop modals |
| `src/features/depreciation/components/DepreciationPromptModal.tsx` | useful-life prompt |
| `src/features/orders/components/OrderDetail.tsx` | Action Dock, convert/reverse/refund/forfeit modals |
| `src/features/dashboard/queries.ts` | getRecentActivities |

### Micro (repo `micro`)
| Path | Used for |
|---|---|
| `apps/prototype-web/client/src/app/navigation.ts` | five seats |
| `apps/prototype-web/client/src/components/layout/BottomNav.tsx` | centered `سجّل` FAB |
| `apps/prototype-web/client/src/components/layout/AppHeader.tsx` | brand + context + settings + theme |
| `apps/prototype-web/client/src/components/layout/MicroAppShell.tsx` | route kinds, keyboard chrome, CONTEXT_REPEATS_H1 |
| `apps/prototype-web/client/src/components/layout/QuickActionSheet.tsx` | 5 actions, in-sheet sale/expense, receipt mode |
| `apps/prototype-web/client/src/app/routeClassifier.ts` | deep patterns, reader/editor rule |
| `apps/prototype-web/client/src/app/navigationContract.ts` | `?from`, closed deep-link vocabulary, canonical fallbacks |
| `apps/prototype-web/client/src/app/useReturnNavigation.ts` | return resolution |
| `docs/contracts/26-navigation-referrer-and-deep-link-contract.md` | binding navigation rules |
| `apps/prototype-web/client/src/components/forms/UnsavedChangesGuard.tsx` | 3-choice guard, sentinel, focus trap |
| `apps/prototype-web/client/src/components/forms/EnglishNumberInput.tsx` | digit normalization, LTR isolation |
| `apps/prototype-web/client/src/application/input/englishNumeric.ts` | parse/format helpers (INFERENCE: detailed behavior inferred from component usage) |
| `apps/prototype-web/client/src/presentation/formatters.ts` | English digits + DD/MM/YYYY rule, money/plural helpers |
| `apps/prototype-web/client/src/pages/Home.tsx` | priority/today/recent blocks |
| `apps/prototype-web/client/src/application/home/homeControlCenterService.ts` | recentChanges model + gaps |
| `apps/prototype-web/client/src/pages/Finance.tsx` | view split, layers, actions layer, EventsLayer, CorrectionsLayer, DepositsLayer |
| `apps/prototype-web/client/src/pages/FinancialEventEditor.tsx` | effect card, ExpenseClassification details layer |
| `apps/prototype-web/client/src/components/finance/EventsLayer.tsx` | events layer, CorrectionPreview usage |
| `apps/prototype-web/client/src/pages/Statement.tsx` | ranges, blocks, sources, truth lines |
| `apps/prototype-web/client/src/pages/Tools.tsx` | thinking-tool identity, module states |
| `apps/prototype-web/client/src/pages/InventoryMaterials.tsx` | activation, materials, أخرِج المتبقي, movement log |
| `apps/prototype-web/client/src/pages/InventoryMovementEditor.tsx` | receipt/consume/waste/adjust, reason mandatory, ?order prefill, purchaseId select |
| `apps/prototype-web/client/src/pages/InventoryReversalEditor.tsx` | movement reversal |
| `apps/prototype-web/client/src/pages/OrderDetail.tsx` | delivery/settlement, 3-option deposit settlement, collection reversal previews |
| `apps/prototype-web/client/src/pages/SupplierPurchaseEditor.tsx` | purchase truth card, «لن يحوله إلى مخزون», payment reversal |
| `apps/prototype-web/client/src/pages/CashCount.tsx` | reconciliation tool precedent |
| `apps/prototype-web/client/src/pages/DirectSaleEditor.tsx` | save-then-return, revisions, cancellation |
| `apps/prototype-web/client/src/pages/Settings.tsx` | export/import home (adjacent to UX-04) |
| `src/domain/inventory-material/types.ts` | movement types, WasteContext |
| `apps/prototype-web/client/src/domain/financial-event/types.ts` | OperatingExpenseContext, loss_non_cash |
| `apps/prototype-web/client/src/domain/shared/currency.ts` | JOD/minor model |
| `apps/prototype-web/client/src/application/finance/projectFinancialService.ts` | period/insights/waste reading |
| `apps/prototype-web/client/src/application/finance/statementService.ts` | StatementReading model |
| `apps/prototype-web/client/src/application/finance/correctionHistoryService.ts` | corrections digest |
| `apps/prototype-web/client/src/application/transfers/localTransferService.ts` | import verifier (integrity rules source) |
| `docs/decisions/remaining-capabilities-review-v1.md` | gated/rejected capabilities (assets, POS, CRM…) |

---

*End of SA-3 report. Both repositories were read strictly read-only; no file inside either repo was modified.*
