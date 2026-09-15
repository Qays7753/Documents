# SA-3 — Transfer UX & Discoverability Audit (Zman → Micro)

- **Date:** 2026-09-05
- **Auditor:** Specialist Agent SA-3 (Task ID 5-a), Group 6 / Agent 2 transfer audit
- **Baseline:** Micro @ `1242aa62b3f81e8db263f4220bcefd3c8827d307` (verified via `git rev-parse HEAD`), app at `apps/prototype-web/client`
- **Method:** Static code analysis only — Grep/Read over the current tree (post Agent-1 changes: commit `0d45bb4` density guard + `c1ae93e`/`1242aa6` merge). The app was NOT executed; no repository file was modified. All citations are `file:line` against the baseline rev.
- **Scope:** Five-tab model conformance, discoverability of every routed surface, orphan detection, plain-Arabic labels, numeric/date normalization, one-handed/density, progressive disclosure, empty/unknown/offline states, consistency, and integration of every transferred record kind into core read surfaces, with harm classification (§9 categories).

---

## 1. Methodology

1. Read the navigation spine: `app/navigation.ts` (seats), `components/layout/MicroAppShell.tsx` (shell), `components/layout/BottomNav.tsx` (FAB seat), `components/layout/QuickActionSheet.tsx` (FAB actions), `app/MicroRouter.tsx` (all routes), `app/routeClassifier.ts` (deep vs surface), `app/navigationContract.ts` (`?from=` / deep-link vocabulary / canonical fallbacks).
2. Enumerated all 52 non-test page components under `src/pages/` and all 55 router patterns (incl. `/review` redirect and NotFound fallback).
3. For every route path literal, Grep'd the production tree (excluding `*.test.*`) for in-app navigation entries (`navigate(`, `requestNavigation(`, `withFrom(`, `href:`, `onOpen`, card CTAs, service-built `sourceHref`/`deepLink` values) and verified ≥1 entry point outside the route's own component.
4. Audited labels on all 14 transferred capability families listed in the brief; grepped for English UI leakage (`>[A-Z][a-z]+ …<`, `aria-label="[A-Za-z]"`), accounting jargon (`G5`, `تصريح`), required markers (`مطلوب`), optional markers (`اختياري`), unknown-state honesty (`غير معروف`), offline truth lines (`بلا إنترنت`, `محليًا على جهازك`).
5. Verified numeric input boundary (`application/input/englishNumeric.ts`, `EnglishNumberInput`/`EnglishQuantityInput` adoption across pages; zero `type="number"` matches) and date rendering (`presentation/formatters.ts` DD/MM/YYYY).
6. Verified touch-target and CTA placement rules in `index.css` (44/48px targets, `.micro-sticky-save` bottom dock, FAB 56px) and the §10.1 density guard (`scripts/text-density-count.py` — 52 pages measured; commit `0d45bb4`).
7. Cross-checked every transferred record kind against read surfaces (Home control center, Work, Finance layers, FinanceActivity, Statement, ToolsIntegrity, Tools module-states) for source links.

---

## 2. Tab model summary

Five-seat model confirmed exactly as specified (BottomNav.tsx:26-32; navigation.ts:13-18):

| Seat | Label | Route | Evidence |
|---|---|---|---|
| 1 | مشروعي الآن | `/` | navigation.ts:14; BottomNav items[0] |
| 2 | العمل | `/orders` | navigation.ts:15 |
| 3 (center) | **سجّل** (FAB, 56px) | opens QuickActionSheet | BottomNav.tsx:29-32; index.css:828-842 |
| 4 | مالي | `/finance` | navigation.ts:16 |
| 5 | أدواتي | `/tools` | navigation.ts:17 |

- FAB sheet actions (QuickActionSheet.tsx:52-78): تسجيل بيع (in-sheet), تسجيل مصروف (in-sheet), طلب من عميل → `/orders/draft/new?intent=customer_order`, مسودة تصميم → `/orders/draft/new?intent=planned_design`, عربون أو تحصيل → `/collect` (MicroAppShell.tsx:76-88).
- Settings = header gear (MicroAppShell.tsx:96; AppHeader.tsx:39-47) — no sixth seat. Profile = Home "ملف المالك" link (Home.tsx:197) + Settings:415.
- Route depth model (routeClassifier.ts:16-58): readers keep bottom nav ("surface"), editors hide it and guard unsaved changes ("deep") — one primary CTA per editor, back-to-source via `?from=`.

---

## 3. Master discoverability map (all routed surfaces)

Min taps counted from Home (`/`); FAB = 1 tap + 1 action selection. "Entry" = strongest in-app navigation evidence (non-exhaustive where many exist).

| Surface / Route | Entry point(s) (component:line) | Tab family | Min taps from Home | Orphan risk |
|---|---|---|---|---|
| `/` Home | BottomNav seat | Home | 0 | NONE |
| `/orders` Work | BottomNav seat; Home.tsx:243; homeControlCenterService.ts:98 | Work | 1 | NONE |
| `/orders/:id` OrderDetail | Orders.tsx:123; Finance.tsx:314,484; EventsLayer.tsx:100 | Work | 2 | NONE |
| `/orders/:id/deliver` DeliveryReview | OrderDetail.tsx:385 | Work | 3 | NONE |
| `/orders/draft/:id` DraftEditor | Orders.tsx:206; homeControlCenterService.ts:215; dailyFollowUpService.ts:80 | Work | 2 | NONE |
| `/orders/draft/new` (id="new") | FAB order/estimate (MicroAppShell.tsx:77,81); Orders.tsx:298; Schedule.tsx:261; Tools.tsx:257; CostCalculator.tsx:586; EstimateDetail.tsx:205 | Work+FAB | 2 | NONE |
| `/orders/draft/:id/agreement` | CostEditor.tsx:650; DraftEditor chain | Work | 3 | NONE |
| `/orders/draft/:id/cost` | DraftEditor.tsx:277; AgreementEditor.tsx:194,216 | Work | 3 | NONE |
| `/orders/new` NewDraft (redirect shim) | **none** — URL-only compat redirect (NewDraft.tsx:16, documented F-003) | Work | — | LOW (intentional shim) |
| `/direct-sales/new` | Orders.tsx:290,316; Catalog.tsx:1055 | Work | 2 | NONE |
| `/direct-sales/:id` | Orders.tsx:160; QuickActionSheet.tsx:304 (receipt); statementService.ts:365; activityService.ts:307,324; partyLedgerService.ts:123; collectionService.ts:109; walletLedgerService.ts:50; correctionHistoryService.ts:278 | Work | 2 | NONE |
| `/schedule` | homeControlCenterService.ts:387; Tools.tsx:114; Orders.tsx:282 | Home/Tools/Work | 2 | NONE |
| `/schedule/:id` | Schedule.tsx:216,229,238,247,280,296 | Work | 3 | NONE |
| `/finance` | BottomNav seat; Suppliers.tsx:52; Parties.tsx:84; CashWallets.tsx:84; InventoryMaterials.tsx:220 | Finance | 1 | NONE |
| `/finance/new/:type` (7 types) | Finance.tsx:1114-1163; Foundation.tsx:138,179; homeControlCenterService.ts:126-127; OwnerEntitlement.tsx:654 | Finance | 2 | NONE |
| `/finance/withdraw` | **single entry** OwnerEntitlement.tsx:662 (X-05 unified entry) | Finance | 3 | MED (deliberate single entry) |
| `/finance/owner-entitlement` | Finance.tsx:327,355,1130; Foundation.tsx:145; homeControlCenterService.ts:180; correctionHistoryService.ts:447 | Finance | 2 | NONE |
| `/finance/g5/declaration` | Finance.tsx:319,1012 | Finance | 2-3 | NONE |
| `/finance/statement` | Finance.tsx:462,1074; integrityCheckService.ts:221 | Finance | 2 | NONE |
| `/finance/activity` | Home.tsx:452 («افتح السجل الكامل»); Finance.tsx:1175 | Home/Finance | 2 | NONE |
| `/share/preview` | **single entry** OrderDetail.tsx:1158 («شارك رسالة مع الزبون») | Work | 3 | MED |
| `/collect` | FAB action (MicroAppShell.tsx:87); Parties.tsx:38,41; OrderDetail.tsx:1132,413 | FAB/Finance/Work | 2 | NONE |
| `/suppliers` | Finance.tsx:445,1100; Tools.tsx:119; FinancialEventEditor.tsx:695 | Finance/Tools | 2 | NONE |
| `/suppliers/purchase/new` (id="new") | Suppliers.tsx:90; Foundation.tsx:186 | Finance | 3 | NONE |
| `/suppliers/purchase/:id` | Suppliers.tsx:139,174; statementService.ts:251-273; activityService.ts:397,413; partyLedgerService.ts:139,152; correctionHistoryService.ts:312,326 | Finance | 3 | NONE |
| `/suppliers/purchase/:id/payment` | Suppliers.tsx:130; SupplierPurchaseEditor.tsx:588 | Finance | 3 | NONE |
| `/cash` CashWallets | Finance.tsx:1093 | Finance | 2 | NONE |
| `/cash/wallet/new` | CashWallets.tsx:156; Finance.tsx:424; Foundation.tsx:106; homeControlCenterService.ts:124; CashTransferEditor.tsx:77 | Finance | 2-3 | NONE |
| `/cash/wallet/:id` WalletLedger | CashWallets.tsx:242 | Finance | 3 | LOW (single natural list) |
| `/cash/wallet/:id/opening-later` | CashWallets.tsx:250 (unknown-balance wallets) | Finance | 3 | LOW |
| `/cash/wallet/:id/adjust` | CashWallets.tsx:258; CashOpeningLaterEditor.tsx:128 | Finance | 3-4 | LOW |
| `/cash/transfer` | **single entry** CashWallets.tsx:187 | Finance | 3 | LOW-MED |
| `/cash/distribute` | CashWallets.tsx:178; Finance.tsx:321,411 | Finance | 2-3 | NONE |
| `/cash/count` | CashWallets.tsx:164; Finance.tsx:453 | Finance | 2-3 | NONE |
| `/cash/entry/:id/reverse` | CashWallets.tsx:297; WalletLedger.tsx:171 | Finance | 3-4 | LOW |
| `/inventory` | Finance.tsx:1107; Tools.tsx:100; integrityCheckService.ts:651-675 | Finance/Tools | 2 | NONE |
| `/inventory/material/new` | InventoryMaterials.tsx:299; Foundation.tsx:213; InventoryMovementEditor.tsx:423 | Finance | 3 | NONE |
| `/inventory/material/:id/confirm` | InventoryMaterials.tsx:410 | Finance | 3 | NONE |
| `/inventory/movement/:type` (receipt/consume/waste) | InventoryMaterials.tsx:307,324,331; SupplierPurchaseEditor.tsx:484 (purchase→receipt bridge); OrderDetail.tsx:931,1229; DirectSaleEditor.tsx:507 | Finance/Work | 3 | NONE |
| `/inventory/movement/:id/reverse` | InventoryMaterials.tsx:705 | Finance | 3-4 | LOW |
| `/catalog` | Tools.tsx:109; homeControlCenterService.ts:375; DraftEditor.tsx:411 | Home/Tools | 2 | NONE |
| `/tools` | BottomNav seat | Tools | 1 | NONE |
| `/tools/calculator` | Tools.tsx:88,206; EstimateDetail.tsx:217 | Tools | 2 | NONE |
| `/tools/estimate/:id` | Tools.tsx:238; CostCalculator.tsx:576 | Tools | 2-3 | NONE |
| `/tools/integrity` | Tools.tsx:95; Settings.tsx:919; Finance.tsx:475 | Tools/Settings/Finance | 2-3 | NONE |
| `/assets` | Finance.tsx:507; integrityCheckService.ts:757,767 | Finance | 2 | NONE |
| `/assets/new` | Assets.tsx:81 | Finance | 3 | NONE |
| `/assets/:id` | Assets.tsx:71; statementService.ts:398,474; activityService.ts:116; EventsLayer.tsx:82; correctionHistoryService.ts:430 | Finance | 3 | NONE |
| `/loans` | Finance.tsx:538; integrityCheckService.ts:842 | Finance | 2 | NONE |
| `/loans/new` | Loans.tsx:88 | Finance | 3 | NONE |
| `/loans/:id` | Loans.tsx:77; statementService.ts:409,485; activityService.ts:117; EventsLayer.tsx:91; correctionHistoryService.ts:220 | Finance | 3 | NONE |
| `/parties` | Home.tsx:251; Tools.tsx:124; Finance.tsx:437 | Home/Tools/Finance | 2 | NONE |
| `/settings` | AppHeader gear (MicroAppShell.tsx:96); Home.tsx:261,271 | Global | 1 | NONE |
| `/profile` | Home.tsx:197; Settings.tsx:415 | Home | 1 | NONE |
| `/foundation` | Home.tsx:348; Setup.tsx:144 (post-setup replace) | Home | 2 | NONE |
| `/setup` | StartupGate.tsx:58 (auto-redirect when store empty); Settings.tsx:285,344 | Gated flow | n/a | NONE (first-run gate) |
| `/review` | **none** — legacy alias; `<Redirect to="/finance">` (MicroRouter.tsx:151-153) | Finance | — | LOW (intentional redirect, no 404) |
| NotFound fallback | escape to `/` (NotFound.tsx:12-14) | — | — | NONE |

**Totals:** 56 routed patterns mapped (55 Route entries + fallback); 52 page components; 53/55 reachable by ≥1 in-app navigation entry; 2 intentional URL-only shims (`/orders/new`, `/review`); 2 MED-risk single-entry routes (`/share/preview`, `/finance/withdraw`); no HIGH orphans.

---

## 4. Orphan detection findings

- **No HIGH orphans.** Every transferred capability has an in-app entry.
- `/review` (MicroRouter.tsx:151-153): correctly redirects to `/finance` (review merged into Finance pulse, comment §2.2) — legacy URL users are not dropped to 404. No in-app entry needed.
- `/foundation` (MicroRouter.tsx:88): reachable from Home "مالي → صفحة الأساس" (Home.tsx:348) and post-Setup redirect (Setup.tsx:144) — permanent front door honored (القرار ٧).
- `/orders/new`: zero in-app entries; NewDraft is a one-hop redirect shim preserving old links (NewDraft.tsx:14-16, documented decision F-003). All live flows use `/orders/draft/new?intent=…`. `canonicalReturnFallbacks` still lists `"/orders/new"` (navigationContract.ts:143) — vestigial but harmless.
- `/share/preview`: exactly one entry — OrderDetail.tsx:1158. See finding **UXD-01**.
- `/finance/withdraw`: exactly one entry — OwnerEntitlement.tsx:662 (deliberate X-05 "المدخل الواحد لسحب المالك", MicroRouter.tsx:32-33). See finding **UXD-02**.
- `/cash/transfer`: exactly one entry — CashWallets.tsx:187 (contextually correct: transfer lives inside wallet management); Finance quick-actions panel (Finance.tsx:1089-1167) has no transfer affordance. Noted as UXD-05 (P3).

---

## 5. Label / language findings (transferred surfaces)

**Verdict: PASS.** No English UI leakage, no accounting jargon, effect-explaining copy precedes every financial commit.

| Capability | Plain-Arabic label evidence | Effect copy before commit |
|---|---|---|
| Guided expense entry + classification | «سجل مصروفًا مدفوعًا» Finance.tsx:1116; editor heading + «ما الذي حدث؟ (مطلوب)» FinancialEventEditor.tsx:712-718; classification behind `<details>` «أضف سياقًا للمصروف» (661-668); dialect «على شو اندفعت المصاري؟» (820) | EventEffectPreview FinancialEventEditor.tsx:525; «افهم الأثر قبل الحفظ» (812) |
| Quick expense/sale sheet | «تسجيل بيع/تسجيل مصروف» QuickActionSheet.tsx:55,62; «مين عليه إلك وكم قبضت» (75) | Receipt + attribution notes (300-312, 362-369); «أدخل مبلغ … بالأرقام 0–9» errors (241,246,317) |
| Purchase → receipt bridge | «المادة المشتراة اختيارية — لربط الاستلام لاحقًا» SupplierPurchaseEditor.tsx:612; receipt bridge → `/inventory/movement/receipt?purchase=` (484) | Receipt guard copy (InventoryMovementEditor.tsx:535) |
| Waste / shortage | «تسجيل هدر» InventoryMaterials.tsx:331; «هدر مخزون» activityLabels.ts:27; shortage recorded atomically InventoryMovementEditor.tsx:353; «فرق نقص عند العدّ» cashCountMessages.ts:14 | «قيمة الاستلام غير معروفة — تُعرض «التكلفة غير معروفة» لا صفرًا» InventoryMovementEditor.tsx:446 |
| Calculator / estimates | «حاسبة التكلفة والسعر» Tools.tsx:200; «احسب قبل أن تلتزم» (163) | «هذا حساب تقديري. ما انحفظت أي حركة مالية ولا مخزون» Tools.tsx:190 |
| Orders / delivery | «راجع التسليم وسجّله» OrderDetail.tsx:389; «مراجعة التسليم» navigation.ts:32 | DeliveryReview full pre-commit surface (D5, MicroRouter.tsx:26-27) |
| Direct sale | «تسجيل بيع مباشر» Orders.tsx:292; editor «بيع مباشر» DirectSaleEditor.tsx:543 area | Loan-style decision cards; receipt (QuickActionSheet.tsx:304) |
| Deposits / settlement | «عربون أو تحصيل» FAB (QuickActionSheet.tsx:74); «سدد التزام مصروف» Finance.tsx:1140; «سجل أمانة قُبضت/سُلّمت» 1147-1157 | Collect outcome card Collect.tsx:198-217 |
| Assets | «الأصول — دفتري مشتق من الأحداث — لا مس شراءً للربح» Finance.tsx:490-491 | AssetEditor kind/long-use choices |
| Loans | «أعطيت مالًا يُعاد» LoanEditor.tsx:118; «يخرج X د.أ من الكاش… السداد يعيده لاحقًا» (184-185) | Decision card LoanEditor.tsx:180-187 |
| Activity | «آخر ما حدث — القارئ الكامل لكل النشاط» Finance.tsx:1177 | n/a (reader) |
| Statement | «كشف الفترة — بسيط ومفصول بالعربية» Finance.tsx:464 | «مشاركته إن شئت فعلٌ يدوي بيدك وحدك» Statement.tsx:565 |
| Integrity | «فحص سلامة مالي — اطمن على أرقامك» Finance.tsx:477 | n/a (reader) |
| Drafts | «مسودات قيد الإكمال» Orders.tsx:198; draft-on-first-input principle MicroAppShell.tsx:74-75 | «لم تُسجّل أي حركة مالية بعد» LoanEditor.tsx:131-133 |
| Backup / share | «حماية البيانات» Settings.tsx:432; «نسخة احتياطية» Home.tsx:258 | «المسح بعد نسخة احتياطية إلزامية» Settings.tsx:236 |

- **English leakage:** none. Only match is brand `aria-label="Micro"` (AppHeader.tsx:26), which is a brand name, and the wordmark «مايكرو» is Arabic (AppHeader.tsx:31-33).
- **Jargon:** "G5" never reaches the user — user-facing terms are «المتوقعات المحلية», «قبض/دفع متوقع» (G5DecisionPanel.tsx:212,224; Finance.tsx:1019,1043). Book value → «دفتري» (Finance.tsx:491,501). Loss → «هالك» (Finance.tsx:1165).
- **Label defect (minor):** header context label falls back to the brand word «مايكرو» and renders next to the wordmark «مايكرو» on `/collect`, `/catalog`, `/foundation`, `/direct-sales/*`, `/share/preview` (navigation.ts:36-40 has no entries for these prefixes; MicroAppShell.tsx:92-95 renders the fallback). → **UXD-03**.

---

## 6. Numeric / date findings

**Verdict: PASS.**

- Input normalization: `normalizeAsciiDigits` converts Arabic-Indic/Farsi digits to 0-9 at the input boundary only (englishNumeric.ts:8-19; no stored data rewrite). `EnglishNumberInput`/`EnglishQuantityInput` adopted in all 27 page files that take numbers + QuickActionSheet.tsx:490-544, EventsLayer.tsx:476, MaterialSheet.tsx, RepaymentSheet.tsx, ActualTimePanel.tsx (131 total occurrences across 35 files).
- Zero `type="number"` inputs in the whole client (grep: no matches) — no native spinner/keyboard bypass of the English-digit boundary.
- Dates: single formatter `formatLocalDate` → `DD/MM/YYYY` (formatters.ts:99-103); `formatLocalDateLong` is the same numeric output (formatters.ts:105-109, G6 §5 rule «لا أسماء شهور»); month label `MM/YYYY` (formatters.ts:120-123); datetime `DD/MM/YYYY HH:mm` (formatters.ts:111-118). All `occurredOn` render sites use `formatLocalDate`/`LocalDateValue`/`formatLocalDateLong` (verified across Home, Statement, FinanceActivity, OwnerEntitlement, LoanDetail, AssetDetail, WalletLedger, Parties, Tools, EstimateDetail…).
- Residual `slice(0, 10)` uses are internal date math or machine filenames, not display (Settings.tsx:218,253 — export filename `micro-local-YYYY-MM-DD.json`; Statement.tsx:95/FinanceActivity.tsx:47 date arithmetic). ISO leak fixes claimed by Group 6 closure are confirmed in user-visible rendering.
- Honesty fallback only: `formatLocalDate(...) ?? line.occurredOn` (Statement.tsx:78; ToolsIntegrity.tsx:94-95; FinanceActivity.tsx:108) — raw ISO shown only if a stored date is invalid; acceptable (UXD-08, P3, no material harm).

---

## 7. One-handed / density findings

**Verdict: PASS (with one P3 note).**

- Touch targets: `.micro-button` 48px (index.css:430-435); `.micro-text-action` 44/48px (536-538); `.micro-icon-button` 44×44 (263-265, 1388-1390, 3703-3711); suggestion chips 44px (6365-6371, UX-03 fix); activity rows 44px (6774-6775); checkboxes 44px (6442-6443); calendar cells 44px grid (3946-3949); FAB 56px (828-831). Bottom-nav grid: 5 columns (790-793).
- Primary CTA placement: editors use the bottom sticky dock `.micro-form-actions.micro-sticky-save` (index.css:1179-1190) in 14 editors (FinancialEventEditor.tsx:732, SupplierPurchaseEditor.tsx:871, InventoryMovementEditor.tsx:881, AgreementEditor.tsx:341, CostEditor.tsx:632, MaterialEditor.tsx:313/483, CashTransferEditor.tsx:149, CashAdjustmentEditor.tsx:149, CashReversalEditor.tsx:168, CashOpeningLaterEditor.tsx:188, OwnerWithdrawalEditor.tsx:232, G5DeclarationEditor.tsx:232, ScheduleEditor.tsx:247, CashWalletEditor.tsx:120). Remaining editors (LoanEditor.tsx:193-202, AssetEditor, Collect, CashCount, DirectSaleEditor.tsx:896) place the single primary button after all fields at form end — bottom-of-content, thumb-reachable.
- Quick entry = bottom sheet (vaul Drawer, direction="bottom", QuickActionSheet.tsx:374-375; RepaymentSheet; MaterialSheet); deep entry = full pages that hide bottom nav (routeClassifier.ts:16-58) — matches the brief's rule.
- Keyboard-open hides bottom nav so content is not covered (MicroAppShell.tsx:62-69; index.css:776-778).
- Density guard: `scripts/text-density-count.py` PAGES list covers all 52 page components incl. the 12 cash/collect/party/ledger pages (script lines 552-618; commit `0d45bb4` "density guard covers all 52 routed pages… 44px chip targets"). Agent-1's claim verified in current tree.
- 360×800 references exist (docs/quality/screenshots/g9-setup-360x800.png); `@media (max-width: 420px)` and landscape short-height adjustments present (index.css:3253+, 3274-3285).
- **UXD-06 (P3):** OrderDetail's contextual primary commit action («الخطوة التالية» card with ابدأ التنفيذ / الطلب جاهز للتسليم / راجع التسليم وسجّله, OrderDetail.tsx:353-429, 443-445) sits immediately after the page heading on a long scrolling page — no sticky dock on this surface, so on 360×800 the primary action can drift out of the thumb zone after scrolling. No material harm (status-conditional, page re-renders on state change).

---

## 8. Progressive disclosure counts (mandatory vs optional)

No Zman quick-flow became a mandatory-heavy slow form. Quick flows stay quick; full editors keep depth behind explicit optional markers/collapsed sections.

| Editor | Mandatory | Optional (markers/collapse) | Evidence |
|---|---|---|---|
| QuickActionSheet — sale | 1 (amount) | 5 (name «اختياري», cost-known select, credit toggle, customer, wallet) | QuickActionSheet.tsx:478-507, 388-390 («المبلغ هو الحقل الإلزامي الوحيد») |
| QuickActionSheet — expense | 1 (amount) | 3 (note, category chips, wallet) | 396-398, 109-112 |
| FinancialEventEditor (guided) | 2 (amount, note) | ~10 (counterparty «اختياري», wallet, whole classification layer behind `<details>`, category/behavior/purpose/knowledge/shared) | 652-698, 818-828 |
| SupplierPurchaseEditor | 3 (supplier, total, date) | material/quantity link «اختيارية», notes, payments, receipts | 612, 631, 767, 786 |
| InventoryMovementEditor (receipt/consume/waste) | 3 (material, quantity, date) | value-unknown toggle «لا، غير معروفة بعد», note «اختيارية», purchase/order links | 562-563, 715, 446 |
| DirectSaleEditor | 1-2 (amount [+customer if credit]) | name, quantity, cost, date, note | DirectSaleEditor guided test + EnglishNumberInput set |
| LoanEditor | 3 (borrower, amount, date) | wallet «اختياري — للعرض», note «اختياري» | LoanEditor.tsx:135-179, 160, 173 |
| AssetEditor | 3-4 (name, amount, date, kind/long-use choices) | category «تصنيف حر (اختياري)», start date «اختياري», note «اختياري» | AssetEditor.tsx:187, 265, 273 |
| Collect | 2 (source, amount) | note «اختيارية», wallet destination | Collect.tsx:380, 329 |
| CostCalculator | 0 (playground) | everything optional; save optional | Tools.tsx:163-164, 190-191 |
| CostEditor | per-gap markers | explicit «إلزامي/اختياري» gap badges | CostEditor.tsx:54, 378 |
| Draft editor | item + intent (draft-on-first-input) | customer name «اختياري في المسودة», work reference «اختياري» | DraftEditor.tsx:386, 418 |

Optional markers «اختياري» appear 70+ times across pages (grep §6 of methodology); collapsed `<details>` layers for classification (FinancialEventEditor.tsx:661), G5 link details (G5DeclarationEditor.tsx:178-219), Finance layers (Finance.tsx:487, 1081), catalog cost items (Catalog.tsx:1493).

---

## 9. Empty / unknown / offline findings

**Verdict: PASS.**

- **Teaching empty states** on every transferred list: Home «يومك مفتوح… سجّل أول بيع أو طلب من زر «سجّل» في الأسفل» (Home.tsx:304-307); Work «يومك مفتوح — سجّل أول بيع» (Orders.tsx:304-309); Assets (Assets.tsx:59), Loans (Loans.tsx:65), Parties «لسه ما في حدا عليه فلوس» (Parties.tsx:134), Tools «ما في تقديرات محفوظة بعد. احسب تكلفة منتج جديد وشوف كيف بتمشي» (Tools.tsx:223-226), Collect «ما في ديون قابلة للتحصيل الآن» (Collect.tsx:311), Statement (306, 317), FinanceActivity (270-272), OwnerEntitlement (705, 739, 1359), Schedule (251-256), WalletLedger (128), G5 panel «لن يفترض النظام مواعيد من تلقاء نفسه» (G5DecisionPanel.tsx:217).
- **Unknown-state honesty «غير معروف»**: pervasive — unknown cost blocks fake profit (projectFinancialService.ts:641; Finance.tsx:625,661,776; Statement.tsx:382; statementService.ts:587), unknown receipt value (InventoryMovementEditor.tsx:446,562-563), unknown opening balance (CashWallets.tsx:232; WalletLedger.tsx:106; Setup.tsx:128), unknown waste value (Finance.tsx:776), integrity checks enforce «المجهول يُصرَّح به ولا يُعرض صفرًا» (integrityCheckService.ts:203,528,555).
- **Offline indicators:** offline truth lines in 11 files (e.g. LoanEditor.tsx:203 «يعمل بلا إنترنت — يُحفظ محليًا على جهازك»; Collect.tsx:218-220; FinanceActivity, LoanDetail, AssetDetail, AssetEditor, SharePreview, ToolsIntegrity, RepaymentSheet, Home locality note Home.tsx:458-459; Settings.tsx:443 «لا توجد مزامنة سحابية»). Global PWA runtime notice + install control rendered in the shell above every route (MicroAppShell.tsx:99-100).

---

## 10. Consistency findings

**Verdict: PASS.**

- Five-tab model: no sixth seat anywhere; Profile/Settings/Market handled per documented decisions (navigation.ts:10-12; MicroRouter.tsx:16-17). FAB center seat labeled «سجّل» matches the approved structure verbatim (BottomNav.tsx:26-32).
- Duplicate/competing entries: none found. Sale appears in FAB sheet (transient, in-sheet) + Orders secondary CTA (Orders.tsx:287-293) + Catalog product bridge (Catalog.tsx:1055) — complementary contexts, quick-vs-full split is deliberate (م۳, QuickActionSheet.tsx:5-6, 72-73). Expense: FAB sheet (transient) vs Finance «سجل مصروفًا مدفوعًا» (full editor) — same deliberate split.
- One primary CTA per surface: editors have a single `micro-button-primary` save; OrderDetail derives exactly one contextual primary from status (OrderDetail.tsx:353-429); list pages carry one primary create button (Assets.tsx:79, Loans.tsx:86, Suppliers.tsx:88).
- Header/h1 duplication avoided via `CONTEXT_REPEATS_H1` (MicroAppShell.tsx:26-33) — except the fallback-duplication case UXD-03.
- `?from=` referrer discipline is uniform: every cross-surface link goes through `withFrom()`/`requestNavigation` with documented canonical fallbacks (navigationContract.ts:141-198) — no scattered hard-coded returns (single registry).

---

## 11. Integration findings (record kind → core read surfaces)

**Verdict: PASS — every transferred record kind is natively integrated with source links.**

| Record kind | Read surfaces + direct source link |
|---|---|
| Direct sale | Work list (Orders.tsx:160); Home recent (activityService.ts:307,324 `sourceHref`); FinanceActivity reader; Statement grouping with `href` (statementService.ts:365); Parties ledger (partyLedgerService.ts:123); Wallet ledger «بيع مباشر — السجل المصدر» (walletLedgerService.ts:50); corrections (correctionHistoryService.ts:278); FAB receipt link (QuickActionSheet.tsx:304) |
| Supplier purchase / payment / receipt | Suppliers list; Statement (statementService.ts:251-273); FinanceActivity (activityService.ts:397,413,541); Parties (partyLedgerService.ts:139,152); corrections (correctionHistoryService.ts:312,326) |
| Inventory movement / waste / shortage | FinanceActivity (activityService.ts:541-542); corrections (correctionHistoryService.ts:414); integrity deep links (integrityCheckService.ts:651-675); period waste read (Finance.tsx:776); shortage rows (InventoryMaterials.tsx:461) |
| Deposit (عربون) | DepositsLayer in Finance with `onOpenOrder` → `/orders/:id` (Finance.tsx:482-485); EventsLayer deposit links (EventsLayer.tsx:100) |
| Settlement / amanah / loss | Finance quick actions (Finance.tsx:1138-1166); position qualifiers (homeControlCenterService.ts:130-133); EventsLayer |
| Asset events | Finance assets layer (Finance.tsx:487-511); Statement hrefs (statementService.ts:398,474); FinanceActivity (activityService.ts:116); EventsLayer (EventsLayer.tsx:82); corrections (correctionHistoryService.ts:215,430) |
| Loan events / repayments | Finance loans layer (Finance.tsx:513-538); Statement (statementService.ts:409,485); FinanceActivity (activityService.ts:117); EventsLayer (EventsLayer.tsx:91); RepaymentSheet from Loans/LoanDetail |
| G5 expected records | Finance G5DecisionPanel + «سجل المتوقعات المسجلة» (Finance.tsx:1009-1043); period indicators (Finance.tsx:1345-1356) |
| Drafts | Home «اليوم» items (homeControlCenterService.ts:207-215); Work «مسودات قيد الإكمال» (Orders.tsx:192-222); daily follow-up (dailyFollowUpService.ts:80) |
| Owner capital / withdrawal | Home fact card source link (homeControlCenterService.ts:180); OwnerEntitlement unified ledger; corrections deep link (correctionHistoryService.ts:447) |
| Corrections (all kinds) | Finance `/finance?layer=corrections` (Finance.tsx:370,608); CorrectionsLayer `onOpenSource` with `withFrom` (CorrectionsLayer.tsx:259); RestatementNote (Finance.tsx:365-372) |
| Estimates | Tools «تقديراتي المحفوظة» (Tools.tsx:215-301); EstimateDetail; bridge to draft (Tools.tsx:250-265) |
| Integrity findings | ToolsIntegrity reader with `onOpen` deep links (ToolsIntegrity.tsx:139); deep links to `/finance`, `/cash`, `/inventory`, `/assets`, `/loans` (integrityCheckService.ts:321-1031) |
| Activity (all families) | FinanceActivity with per-row `sourceHref` + `?from` propagation (FinanceActivity.tsx:207) |

Deep-link vocabulary (`?event=`, `?from=`, `focus`, `layer`, `purchase`, `material`) is closed and defensively parsed (navigationContract.ts:41-102); FAB receipt uses `/finance?event=` (QuickActionSheet.tsx:366) and EventsLayer focuses that event (Finance.tsx:1185).

---

## 12. Prioritized findings (with §9 harm classification)

### P0 (financial / security / data-loss)
**None found.** No discoverability defect creates wrong money, data loss, or security exposure.

### P1 (missing capability / broken journey / data integrity)
**None found.** All 14 transferred capability families are reachable, labeled, and integrated; every route resolves (no 404 dead-ends in live flows; `/review` redirects; NotFound offers escape NotFound.tsx:12-14).

### P2 (UX / discoverability / performance / maintainability)

- **UXD-01 — `/share/preview` single deep entry (discoverability).** Only entry: OrderDetail.tsx:1158 («شارك رسالة مع الزبون»), 3 taps from Home, invisible from the Finance/Statement family even though its canonical fallback is `/finance` (navigationContract.ts:164). Sharing patterns also diverge: orders get an editable preview page (contract 33), Statement shares directly via the system sheet/clipboard without preview (Statement.tsx:236-241, textDelivery). Harm: **discoverability** (owner may never find customer-message sharing from financial surfaces; statement share has no pre-send editing). Suggested: add a «شارك» entry on Statement/Finance that routes through `/share/preview`, or document the single-context intent in the contract.
- **UXD-02 — Owner withdrawal discoverability (discoverability / cognitive-load).** The only entry to `/finance/withdraw` is inside the unified owner ledger (OwnerEntitlement.tsx:662): Home → مالي (1) → مال المالك (2) → سحب (3). The Finance quick-actions panel (Finance.tsx:1089-1167) and the top position card (Finance.tsx:351-363, «رأس مالك · افتح الدفتر الموحد») do not mention withdrawal, so an owner looking for "خذ فلوسي من الدرج" must know the unified-ledger concept. This is a documented deliberate single-entry design (X-05, MicroRouter.tsx:32-33: «يسأل سحب من المشروع لنفسك؟») — flagged as a discoverability tradeoff, not a defect of intent. Harm: **discoverability / cognitive-load**, no material harm (the entry that exists writes to the correct path and previews the effect). Suggested: label the Finance owner card or add a quick action «اسحب لنفسك» that routes to the same unified editor.

### P3 (enhancement / no material harm)

- **UXD-03 — Header context label duplicates the brand wordmark (cognitive-load, cosmetic).** `getNavigationLabel` has no entries for `/collect`, `/catalog`, `/foundation`, `/direct-sales/*`, `/share/preview`, so the header renders context «مايكرو» beside the wordmark «مايكرو» (navigation.ts:36-40 fallback; MicroAppShell.tsx:92-95; AppHeader.tsx:31-34). Harm: **no material harm** (visual duplication only). Suggested: add contextual labels («ورقة التحصيل», «الكتالوج», «صفحة الأساس», «بيع مباشر», «مشاركة الرسالة») or suppress the context span on the fallback.
- **UXD-04 — Finance quick-actions hub is collapsed mid-page (discoverability, mitigated).** The densest entry hub («تسجيل حركة أو فتح مصدر», Finance.tsx:1081-1167) opens from a collapsed `<details>` below the position section; mitigated by always-visible fact-road links higher up (Finance.tsx:433-479). Harm: **cognitive-load** (progressive disclosure is deliberate; 360×800 first-screen holds pulse + position cards before the hub). No action required; consider promoting the top-3 actions.
- **UXD-05 — `/cash/transfer` single entry (discoverability, minor).** Only from the wallets surface (CashWallets.tsx:187); no affordance in the Finance actions panel (which has محافظ/موردون/مخزون/مصروف… but not تحويل). Harm: **discoverability**, no material harm (transfer is contextually a wallet-list action; 3 taps). Suggested: optional quick action in the Finance hub.
- **UXD-06 — OrderDetail primary CTA not docked (one-handed, minor).** Status-conditional primary commit actions render in the «الخطوة التالية» decision card right after the heading (OrderDetail.tsx:353-429, 443-445) without the sticky dock editors use; on long order pages at 360×800 the action can sit above the thumb zone. Harm: **no material harm** (single primary per status preserved; page is a reader that keeps bottom nav).
- **UXD-07 — `/orders/new` vestigial route + fallback entry (maintainability, trivial).** URL-only compat shim (NewDraft.tsx:14-16) and a `canonicalReturnFallbacks["/orders/new"]` entry that no live flow targets (navigationContract.ts:143). Harm: **maintainability** (two "new order" spellings to keep in mind; behavior is correct). Suggested: comment or remove the fallback entry when the shim is retired.
- **UXD-08 — ISO fallback in date render (misleading-state, theoretical).** `formatLocalDate(...) ?? raw` fallbacks (Statement.tsx:78; ToolsIntegrity.tsx:94-95; Home.tsx:431; FinanceActivity.tsx:108) would show `YYYY-MM-DD` only for a stored invalid date. Harm: **no material harm** (honesty fallback; unreachable with valid domain dates).

### Verified clean (no defect)
Tab model, FAB actions, orphan coverage (no HIGH), labels/jargon/English leakage, effect-explaining copy, English-digit normalization, DD/MM/YYYY rendering, 44/48px targets, sticky bottom saves, bottom-sheet quick entry vs full-page deep entry, keyboard-open chrome handling, progressive-disclosure counts, empty/unknown/offline states, one-primary-CTA discipline, `?from=` referrer contract, and record-kind→read-surface integration with source links.

---

## 13. Next actions (for Agent 2 synthesis)

1. Decide UXD-01: either add a second `/share/preview` entry from the statement/finance family (preferred: statement «شارك» → preview page for pre-send editing parity) or record single-context intent in docs/contracts/33.
2. Decide UXD-02: keep X-05 single entry (acceptable) or surface a labeled «اسحب لنفسك» affordance in the Finance hub/owner card.
3. Cheap polish batch (UXD-03/05/07): contextual header labels for the 5 fallback paths, optional transfer quick action, retire `/orders/new` fallback entry.
4. No blocking issues for the transfer verdict: every transferred capability is discoverable, correctly placed in the five-tab model, plainly labeled in Arabic, mobile-RTL-friendly, and natively integrated with source links.
