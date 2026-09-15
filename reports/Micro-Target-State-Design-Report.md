# Micro — Target Flow, Screen, Navigation & Gap-Discovery Design Report

**Product:** Micro — Arabic RTL, phone-first, offline-first financial & operating system for one Jordanian home-based / micro-business owner
**Repository analyzed:** https://github.com/Qays7753/Micro — branch `main` @ `1b37c77c72f719a4b51be3aa5e243063c997df2e` (latest, clean tree, verified)
**Report type:** Discovery, gap analysis, and target-state design (design only — no code was modified, no data changed, no commits created)
**Date:** 1 September 2026

---

## 0. Executive Summary

This report answers five questions the owner asked, in this order:

1. **Where does every feature live** across `مشروعي الآن | سجّل | العمل | مالي | أدواتي`? → **Output A** (§3)
2. **What does the user see** from the top of each major screen to the bottom, and what is the primary action? → **Output B** (§4)
3. **What are the exact step-by-step flows** for the owner's daily tasks? → **Output C** (§5)
4. **What is missing** completely or partially, and what must be added? → **Output D** (§6)
5. **What is the single preferred target architecture** connecting features, screens, transitions, results, and safe returns? → **Output E** (§7)

**Method.** The full current `main` was treated as the only truth: all 36 page components (16,172 lines of page code), the router, navigation model, route classifier, app shell, 13 domain units, the application-service layer, the 26-store IndexedDB layer, the tests, and the governing docs (`docs/product-source-of-truth.md`, `docs/operations/current-state.md`, `docs/08-glossary.md`) were inspected directly. Four specialist sub-agents worked in parallel (current-state mapping; target navigation architecture; screen contracts & wireframes; benchmarks & missing capabilities) and a fifth review pass integrated the results. Every "missing" claim in this report was verified against the code before being classified; every capability claimed to exist was also verified. External research produced 43 cited sources; assumptions are labeled.

**Headline verdict.** The financial engine is genuinely strong. Atomic documented corrections, revision conflict guards, `unknown ≠ zero` discipline, honest empty states, and idempotent writes are all real and better than consumer-app norms. **The gaps are concentrated in navigation placement, discoverability, and two correction voids — not in money logic:**

- **Two record families have no correction path at all**: supplier purchases/payments (the service exposes only record/list/summary), and post-agreement order prices (a price change today requires cancelling the whole order and re-doing deposit settlement).
- **The #1 daily money-in action — "قبضت من خالد" (collecting a debt) — costs 3–4 taps** through a full editor and a difference dialog, while the FAB collection shortcut lands on an unfiltered Orders list.
- **Cash tools are orphaned from their own hub**: `/cash/count` and `/cash/distribute` are linked only from Finance, never from `/cash` — the page both tools exit to. The `cover_payment` resolution for negative unallocated cash is reachable only by typing a URL.
- **The quick-sale sheet's wallet default ("بلا نسبة الآن — كاش غير موزع") silently manufactures the unallocated-cash backlog** the owner must later resolve.
- **Real capabilities are invisible**: actual time/material recording, recurrence/capacity, and guided opening import are buried in collapsed layers.
- **`كيف كان أسبوعي؟` (how was my week?) has no screen** — the period reading hides inside a collapsed Finance layer.
- **A money-truth gap on the morning screen**: Home's cash figure silently includes Amanah cash with no qualifier, and shows neither unallocated cash nor unknown-opening signals.

The target design keeps the approved five-destination shell (`مشروعي الآن | العمل | سجّل | مالي | أدواتي`), fixes the placement and loop gaps with **6 new routes + 1 optional + 1 retarget**, introduces **new interaction surfaces** — ورقة التحصيل CollectionSheet, كشف الأسبوع StatementView, معاينة الأثر CorrectionPreview contract, كشف المحفظة WalletLedger, the two P0 correction editors (order price, purchase correction), an optional صفحة شخص PartyDetail — and registers **24 missing capabilities** (4 P0, 10 P1, 10 P2) — each tied to a real user task, a code-verified failure, and a concrete target solution.

**The 20% / 80% split.** Part 1 (§1–2) is the concise current state. Part 2 (§3–7) is the target-state design and missing-capability discovery, which is the main body of this report.

---

# PART 1 — CURRENT STATE (≈20%)

## 1. Verified system facts

All facts below were verified in code on `main` @ `1b37c77`, not taken from docs. Where docs and code conflict, code wins (conflicts listed in §2.4).

| Fact | Verified value | Evidence |
|---|---|---|
| Route declarations | 39 explicit routes + NotFound catch-all (=40), incl. `/review` → redirect `/finance` and `/orders/new` → redirect `/orders/draft/new` | `MicroRouter.tsx` |
| Page components | 36 `.tsx` page files (2 non-visual: `NewDraft`, `NotFound`) | `pages/` |
| Bottom navigation | `مشروعي الآن` `/` · `العمل` `/orders` · **center FAB `سجّل`** (opens QuickActionSheet) · `مالي` `/finance` · `أدواتي` `/tools`; settings gear in header | `navigation.ts`, `BottomNav.tsx` |
| Chrome suppression | `deep` routes (19 regex patterns) hide BottomNav + FAB; `surface` keeps them; `/setup` special | `routeClassifier.ts` |
| IndexedDB stores | 26 (incl. `cost-estimates`); schema 29 / export 21, legacy files accepted & migrated | `IndexedDbLocalStore.ts`, `localTransferService.ts` |
| Entry pipeline | UI → Application Service → Domain → `PrototypeLocalStore` → IndexedDB (no direct UI→IndexedDB anywhere) | services layer |
| Corrections model | `commitFinancialEventReplacement` (reverse + replacement in one atomic transaction), documented delete/restore; direct sales use `revisions[]` + `expectedRevisionCount` conflict guard | `EventsLayer.tsx`, `DirectSaleEditor.tsx` |
| Unsaved-changes guard | 3-choice drawer (ابقَ / احفظ ثم اخرج / اخرج بلا حفظ) + browser-back sentinel on all deep editors | `UnsavedChangesGuard.tsx` |
| Offline behavior | No sync. Live offline banner (`navigator.onLine`) + SW update card; all reads/writes local; boot storage failures get dedicated recovery screen with 4 codes | `PwaRuntimeNotice.tsx`, `StartupGate.tsx` |
| Financial event types | 8: 5 originals + `amanah_held_cash` + `amanah_released_cash` + `loss_non_cash`; impact computed from single `DELTA_TABLE` | `financial-event/policies.ts` |

The six financial non-negotiables hold in the engine: **collection ≠ profit; debt ≠ cash; purchase ≠ COGS; owner money ≠ revenue; Amanah is real cash but not business-owned; unknown ≠ zero.**

## 2.1 Simplified current-state flow map

```
Boot → StartupGate ──(no profile)──→ /setup (3 steps: name → wallet «الدرج» (skippable) → opening known/unknown/zero)
                                     └→ /foundation (optional: cash, capital, debts, materials, import) → /

SURFACE (BottomNav + FAB)                        FAB «سجّل» → QuickActionSheet
/ Home        today rows → /orders/:id, /drafts, /schedule/:id      ├ تسجيل بيع      (IN-SHEET: amount only → receipt)
              facts roads → wallet/new, /orders, expense, invest     ├ تسجيل مصروف    (IN-SHEET)
              away card → /parties, /settings                        ├ طلب من عميل   → /orders/draft/new
/orders العمل  sales → /direct-sales/:id; orders → /orders/:id      ├ مسودة تصميم   → /orders/draft/new
              drafts → /orders/draft/:id; مواعيد → /schedule        └ عربون/تحصيل   → /orders (plain list ⚠)
/finance مالي  G5 declare, unallocated strip (only if >0) → /cash/distribute
              position cards → /cash /parties /suppliers
              layers: period, coverage, actions(11 buttons), deposits, events(+corrections)
/tools أدواتي  calculator → save estimate → «ابدأ مسودة من هذا التقدير» → /orders/draft/new?estimate=
              module status → /inventory /catalog /schedule /suppliers /parties

HUBS (surface)                     READERS (surface+back)                DEEP EDITORS (chrome hidden, guarded)
/cash wallets                      /orders/:id OrderDetail               /orders/draft/:id, /cost, /agreement
/parties دفتر الناس                (lifecycle + collect + cancel)        /direct-sales/:id (revisions, X-06)
/suppliers purchases               /schedule/:id                          /finance/new/:type (8), /withdraw,
/inventory materials                                                      /owner-entitlement, /g5/declaration
/catalog (1,859-line page)                                                /cash/* (wallet/transfer/adjust/distribute/
/foundation, /settings                                                    count/opening-later/reverse), /inventory/*
```

## 2.2 Screen-and-entry table (condensed)

Full 40-row inventory with per-row actions exists in the analysis artifacts; the table below condenses it to the surfaces that matter for the redesign.

| Destination / hub | Route | Shows (top→bottom today) | Primary entry points out | Notable asymmetry |
|---|---|---|---|---|
| مشروعي الآن | `/` | away card (7d) → truth line → «اليوم» (9 row kinds) → 4 fact cards + roads → «مالي» unit (primary button) → «منتجاتي وخدماتي» unit (primary button) → optional modules → recent changes (5) → scope line | rows → sources; facts → roads; units → `/finance`, `/catalog` | Two in-page primary buttons compete with the FAB; cash fact includes Amanah silently |
| العمل | `/orders` | «مبيعاتي» (always first) → DecisionPanel (only when orders exist) → «طلباتي» → drafts → مواعيد preview (5) → «إنشاء مسودة أخرى» | rows → detail editors | Priority panel below the sales list; sale rows 6–9 lines; no create-sale CTA anywhere |
| سجّل (FAB) | sheet | 5 items: بيع / مصروف (in-sheet) / طلب / مسودة / عربون-تحصيل | in-sheet writes; deep routes | Collection lands on plain `/orders`; default wallet = unallocated |
| مالي | `/finance` | back-to-Home button → ReviewPulse → CashDecision → OwnerDecision card → 4 position cards → «ما نعرفه الآن» (dense text + unallocated strip) → ~7 collapsed layers | declare; distribute; cards → hubs; 11 action buttons; events/corrections layers | Reading (ReviewPulse) before decision; «أعلن…» wording violates glossary |
| أدواتي | `/tools` | rule card → calculator (result card AFTER all inputs) → save primary → saved estimates → module status | estimate→draft bridge; module rows | Result not visible while typing; calculator input unguarded |
| محافظ الكاش | `/cash` | decision card → totals → wallet list → transfer/adjust/opening-later → last 8 entries | wallet editors; entry reversal | **No count/distribute buttons** (Finance-only entries); history capped at 8 |
| دفتر الناس | `/parties` | totals → search → party rows (accordion) → «حصّل من X» → source records | source editors | Collect shortcut opens full editor, not a collect step |
| الموردون | `/suppliers` | payables card → «سجل شراء» → open purchases → settled (4) | purchase/payment editors | Opening a purchase id shows the payment form; **no corrections exist** |
| المواد والمخزون | `/inventory` | activation state → material form → movement buttons → material list → last 8 movements | material/movement/reversal editors | Consume doesn't preselect the originating order |
| منتجاتي وخدماتي | `/catalog` | 1,859-line single page: creation form, list, units, conversions, templates, policies, readings | draft/sale reference selects | Back always `/orders`, even when entered from Home |

## 2.3 Capability classification (88 rows → headline)

| Class | Count | Items |
|---|---|---|
| 1 Present and usable | 71 | quick cash/credit sale, quick expense, wallet attribution, order full cycle, direct-sale corrections + revisions, events 8 types, expenses + classification, wallets + opening + transfer + adjust + reversal, parties ledger, owner entitlement/withdrawal, inventory + movements + reversal, catalog, schedule, G5, estimates save + draft bridge, export/import/reset, PWA, return-after-absence, setup, foundation, storage recovery (three of these carry noted caveats: thin entry, glossary language conflict, page structure) |
| 2 Present but hidden | 5 | actual-time recording, actual-material + consume shortcut, recurrence templates, daily capacity, guided opening import |
| 3 Present but incomplete | 3 | negative-unallocated alert routing (review only, no resolution), saved estimate detail/edit (service `update()` exists, no UI), FAB collection shortcut (unfiltered list) |
| 4 Present but misplaced | 2 | cash distribution (Finance-only entry; cover mode unreachable), cash counting (Finance text-link only) |
| 5 Missing state/transition | 1 | CostEditor linked-draft guard (bookmark can append snapshot to a converted draft) |
| 6 Missing capability | 2 | post-agreement order price revision; supplier purchase/payment correction (incl. purchase detail view) |
| 7 Optional/future | 2 | orders search/filter; Market/Delivery/CRM/Auth/Cloud (E-00.14) |
| 8 Not a real gap | 2 | "notification bell" (rejected by E-00.14 decision — attention lives in source screens); "transfers need ≥2 wallets is a bug" (intentional truth-first conditional) |

## 2.4 Major flow breaks (the redesign's justification)

1. **Cash tools orphaned from their hub** — `/cash/count` and `/cash/distribute` are linked only from Finance (grep-verified: only `Finance.tsx:272/302`); `/cash`, the page both tools exit to, never links to them. When unallocated < 0, the alert's «راجع مصدر الفرق» goes to `/cash` for review — the documented `cover_payment` resolution becomes URL-only.
2. **No correction paths for supplier purchases/payments** — `SupplierPurchaseService` exposes only `recordPurchase/recordPayment/list/readSummary`; a mistyped purchase total or payment is uncorrectable in-app. Opening a purchase id renders the payment form, not a purchase view.
3. **No post-agreement order price revision** — `AgreementService` has only `list/get/createFromDraft/startExecution`; a price change means cancel + deposit settlement + restart. Direct sales have `price_cut`; orders have nothing.
4. **FAB collection shortcut lands on the unfiltered Orders list** — no filter, no receivable picker, no collection step.
5. **Saved estimates have no view/edit** — rows show title/floor/date only; delete + re-enter is the only correction, even though `costEstimateService.update()` exists unused.
6. **Hidden capabilities** — actual time/material (collapsed OrderDetail drawer), recurrence/capacity (collapsed Schedule layer), guided opening import (collapsed Settings layer).
7. **Guard net has five holes** — QuickActionSheet's typed amount, CashCount's counted value, CashDistribution's amount, Schedule capacity inputs, and the Tools calculator all silently lose typed money; CostEditor additionally lacks the linked-draft guard its sibling editors have.
8. **Success closure missing after money actions** — OrderDetail collect/deposit actions save with no feedback and no cash delta; DirectSale/Agreement editors navigate away silently.
9. **Home money-truth omissions** — unallocated cash, unknown-opening flag, and the Amanah qualifier are absent from the morning screen; the Home cash card includes Amanah cash without saying so.
10. **Docs ↔ code conflicts (code wins)**: SoT says the distribute strip lives "في مالي/المحافظ" (code: Finance only); glossary binds «متوقع» and forbids «أعلن» (code: Finance CTA reads «أعلن تحصيلًا أو التزامًا قريبًا»); route count is 39, not 38; SoT's exit map for count/distribute assumes a `/cash` linkage that was never built.

**Compacted current/hidden/incomplete/misplaced/absent distinction.** Current = the 71 usable rows. Hidden = the 5 collapsed-layer capabilities. Incomplete = negative-unallocated routing, estimate edit, FAB collection. Misplaced = count/distribute entries. Absent = supplier corrections, order price revision, statement screen, collection sheet, wallet ledger, correction-preview contract, and the states/guards listed in Output D.

*Where the full detail lives (kept out of this report deliberately, to preserve the 20% budget):* the complete 40-row route/screen inventory with per-row actions and return paths, the full 88-row capability catalog with evidence, the complete 12-state audit per screen, the full wireframe set for every secondary screen (Schedule, Suppliers, Settings, OwnerEntitlement, Inventory, Catalog), the full benchmark dossiers (10 patterns × who/problem/evidence/transfers/does-not-transfer), and the raw scenario walkthroughs A–H with per-step code citations are preserved in the four working artifacts: `01-current-state.md` (current state), `02-target-navigation.md` (navigation), `03-screen-contracts-wireframes.md` (screens), `04-research-missing-capabilities.md` (research), plus `05-critical-review.md` (the independent review pass). This Part 1 is the condensed, verified view of those artifacts; the target-state design in Part 2 is the report's own main body.

---

# PART 2 — TARGET STATE (≈80%)

# 3. OUTPUT A — Feature Distribution & Screen Map

## 3.1 Target navigation model

The five-destination shell is **kept** (decision D1, §7.1): `مشروعي الآن | العمل | سجّل (FAB) | مالي | أدواتي`. Each destination answers exactly one owner question:

| Destination | Route | Owner question | Role | Must never contain |
|---|---|---|---|---|
| **مشروعي الآن** (Home) | `/` | «ماذا عليّ اليوم؟ وما هو مسجل؟» | Orientation + priority surface; read-only; every row deep-links to its source | Editors; in-page primary buttons competing with the FAB |
| **العمل** (Orders) | `/orders` | «وين وصلت الطلبات والمسودات؟ وإيش الأولوية؟» | Work pipeline hub: priority panel, orders, direct sales, drafts, schedule preview | Financial readings (period result, wallet math) |
| **سجّل** (FAB → sheet) | no route | «سجّل شيئًا الآن — بلس من ١٠ ثواني» | **The recording hub**: transient ≤3-field writes (sale/expense/collection) + routers to deeper intents; closes over the standing screen, never navigates for its fast paths | Structured workspaces (order creation, classification, corrections) |
| **مالي** (Finance) | `/finance` | «وين الكاش؟ وإيش الوضع والقرار المالي؟» | Money reading + decision surface; canonical parent of cash/people/suppliers/owner-money hubs | Work-pipeline status steps |
| **أدواتي** (Tools) | `/tools` | «احسب قبل أن تلتزم» | Thinking tools: calculator, saved estimates, module status; zero financial writes by contract | Any financial write |

**Four navigation levels** formalize the existing `routeClassifier` rule («القارئ سطح، والمحرر عمق»):

1. **Level 1 — tabs + FAB** (chrome always visible).
2. **Level 2 — domain hubs** (surface, BottomNav kept, canonical parent): `/cash`, `/parties`, `/suppliers` under مالي; `/catalog`, `/schedule` under العمل (schedule fallback changes `/`→`/orders`); `/inventory` under مالي (materials are money-bearing).
3. **Level 3 — stack readers** (nav kept, explicit back-to-origin): `/orders/:id`, `/cash/wallet/:id` [NEW], `/parties/:name` [NEW, optional], `/suppliers/purchase/:id` [RETARGET to purchase detail], `/statement` [NEW], `/foundation`.
4. **Level 4 — deep editors** (chrome hidden, 3-choice unsaved guard): the existing 19 deep patterns plus `/orders/:id/price`, `/suppliers/purchase/:id/edit`, `/suppliers/purchase/:id/payment/:paymentId/reverse`, `/tools/estimates/:id` [all NEW].

## 3.2 FAB «سجّل» — the recording hub (behavior contract)

| Menu item | Behavior | Change |
|---|---|---|
| **تسجيل بيع** | In-sheet fast form: المبلغ (only mandatory) + محفظة القبض **default «الدرج»** + «خيارات أكثر» disclosure (item, cost known/unknown, آجل → customer + collected-now). Receipt with closure numbers + «افتح السجل» deep link. | Fix default wallet (today `""` = unallocated — manufactures backlog); receipt deep link; discard confirm |
| **تسجيل مصروف** | In-sheet: المبلغ + البند (optional) + محفظة الصرف default «الدرج». | Default wallet fix |
| **طلب من عميل** | Deep route `/orders/draft/new?intent=customer_order` (no record until first real input). | Keep |
| **مسودة تصميم** | Deep route `/orders/draft/new?intent=planned_design`. | Keep |
| **تحصيل أو عربون** | **[RETARGET]** Opens a **collection picker sheet** (top receivable parties, e.g. «خالد — 20.00 د.أ») → tap opens **ورقة التحصيل CollectionSheet** prefocused; footer «افتح دفتر الناس» → `/parties?focus=receivable`. | Today lands on plain `/orders` |

Sheet-level rules: closing with a typed amount asks «في رقم مكتوب — تسجّله أو تتجاهله؟» (today `reset()` wipes silently); receipts never navigate on success — they close over the standing screen; FAB hides on deep routes and when the keyboard opens.

## 3.3 Deep-link route vocabulary (alerts → sources)

Query-param vocabulary on existing routes (extends the existing `?event=`, `?intent=`, `?estimate=` precedent):

| Param | Values | Meaning |
|---|---|---|
| `?focus=` | `collect · receivable · overdue · unallocated · export · unknown-opening` | pre-focus a row/panel on landing |
| `?layer=` | `events · corrections · period · capacity · recurrence` | auto-expand a collapsed layer |
| `?mode=cover` | on `/cash/distribute` | pre-select «غطِّ صرفًا خرج من محفظة» (negative-unallocated resolution) |
| `?from=`/`?to=` | on `/statement` | period range |

**Rule: no alert ever routes to an unfiltered list.** Key re-points: Home `due_amount` → `/orders/:id?focus=collect` (collect panel open, المتبقي prefilled); Home receivables road → `/parties` (was `/orders`); away card overdue → `/parties?focus=overdue`; backup age → `/settings?focus=export`; capacity warning → `/schedule?layer=capacity`; Finance negative-unallocated alert → `/cash/distribute?mode=cover` (was `/cash` review-only); FAB collection → picker → CollectionSheet; quick-sale receipt → `/direct-sales/:id`.

## 3.4 Feature distribution map (Output A table)

Legend — Current: catalog class from §2.3. Pattern: FS full-screen deep editor · SR stack reader · BS bottom sheet · DL dialog · IN inline. Decision vocabulary: **keep · move · merge · make-secondary · add · retarget · defer · remove**. One authoritative owner per capability; secondary links never own the write. (Rows condensed where the catalog's 88 rows share a screen; every capability is covered.)

### A. Home («مشروعي الآن»)

| Feature | Current | Target owner | Why | Primary entry | Secondary links | Pattern | After action | Safe return | Decision |
|---|---|---|---|---|---|---|---|---|---|
| Today list (9 kinds, action labels) | present | Home `/` | the opening question | tab 1, cold start | Orders preview | rows→deep links | n/a (read) | n/a | keep; cap 5 rows + «و X أخرى» |
| Fact roads (cash/receivables/payables/owner) | present | Home 2×2 chips | unknown ≠ zero needs a road | same | — | chips | n/a | n/a | keep; receivable road → `/parties` |
| Home truth lines (locality, backup age, Amanah qualifier, unallocated, unknown-opening) | partial/missing | Home | money truth on the morning screen | auto-conditional | Settings | one-row lines | n/a | n/a | **add** (MC-14, MC-24) |
| «مالي» / «منتجاتي وخدماتي» in-page units | present, misplaced | demoted to one quiet links row | two primary buttons compete with FAB + duplicate tabs | — | tabs | quiet links | n/a | n/a | **make-secondary** |
| Scope line «فتح مالي» | present | removed, replaced by locality line | duplicates the مالي tab | — | — | text line | n/a | n/a | **remove** |
| Away card (return after absence) | present | Home | guilt-free recovery | auto ≥7 idle days | — | conditional card | n/a | n/a | keep; add focus deep links |
| Statement teaser «عرض تفاصيل الأسبوع» | missing | Home On-Demand row | weekly-review entry | auto | Finance period layer | link row | n/a | n/a | **add** (D8) |

### B. Quick record actions (FAB «سجّل»)

| Feature | Current | Target owner | Why | Primary entry | Secondary | Pattern | After action | Safe return | Decision |
|---|---|---|---|---|---|---|---|---|---|
| Quick cash sale | present | QuickActionSheet (sale) | 10-second path: 1 mandatory input + default wallet | FAB | — | BS | receipt closes over standing screen | discard confirm | keep; default wallet «الدرج» |
| Quick credit sale (`partial_debt`) | present | QuickActionSheet (آجل disclosure) | debt ≠ cash | FAB | — | BS (progressive) | receipt | same | keep |
| Quick expense | present | QuickActionSheet (expense) | daily cash-out | FAB | — | BS | receipt | same | keep |
| Wallet attribution at quick entry | present, harmful default | QuickActionSheet selector | default «الدرج» stops manufacturing unallocated | FAB | — | selector | allocation recorded with event | — | **retarget default** (MC-11) |
| Collection picker (تحصيل أو عربون) | incomplete | QuickActionSheet 2nd-level sheet | landing on plain `/orders` breaks the loop | FAB menu | Home due row, Parties | BS → CollectionSheet | receipt | discard confirm | **retarget** (D6/D7) |
| Receipt → open/undo just-created record | missing (text only) | receipt buttons «افتح السجل» / «تراجع» | corrections one tap from the record | receipt | — | buttons → `/direct-sales/:id` | editor | guarded | **add** (MC-18) |

### C. Orders + drafts («العمل» + order stack)

| Feature | Current | Target owner | Why | Primary entry | Secondary | Pattern | After action | Safe return | Decision |
|---|---|---|---|---|---|---|---|---|---|
| Orders landing + «الأولوية الآن» | present, misordered | Orders `/orders` | priority must precede lists | tab 2 | — | hub reader | n/a | n/a | keep; **reorder panel first, always rendered** |
| Direct-sales list (مبيعاتي) | present, dense | Orders section | rows ≤3 lines, detail deferred | Orders | Parties links | hub section | n/a | n/a | keep; compress rows; add create-sale CTA |
| Draft editor (lazy materialization) | present | `/orders/draft/:id` | story + quantity before money | FAB, Orders, Tools bridge | — | FS deep | «احسب التكلفة» → cost | guard + delete 2-step | keep |
| Cost editor + snapshots | present | `/orders/draft/:id/cost` | protection price before commitment | draft primary | — | FS deep | save → stays; «تسجيل الاتفاق» when snapshot exists | guard | keep |
| Cost linked-draft guard | missing state | CostEditor redirect | sibling editors guard converted drafts | direct URL | — | redirect | → `/orders/:id` | — | **add** (MC-12) |
| Agreement editor (floor + deposit) | present | `/orders/draft/:id/agreement` | the commitment moment | cost editor | — | FS deep | creates order → `/orders/:id` + closure | guard | keep |
| OrderDetail reader | present | `/orders/:id` | status + الخطوة التالية + lifecycle | Orders, Home, Finance, Parties | — | SR | contextual actions inline | back-to-origin | keep; sticky contextual CTA |
| Order lifecycle (start→ready→deliver) | present | OrderDetail | one screen owns the cycle | OrderDetail | — | sticky bar + closure sentence | closure | — | keep |
| Collect full / register debt at delivery | present | OrderDetail | collection ≠ profit; debt ≠ cash | OrderDetail | — | inline panel | closure sentence | — | keep; add closure (MC-06) |
| Partial debt collection (orders) | present | OrderDetail panel | focused single-field collect | OrderDetail; Home `?focus=collect` | Parties | inline panel | closure | — | keep; deep-link focus |
| Order cancel + 3-way deposit settlement | present | OrderDetail cancel panel | deposit truth preserved | OrderDetail | — | inline + DL | documented receipt | — | keep |
| **Order price revision post-agreement** | **missing** | **`/orders/:id/price` [NEW]** | today price change = cancel + restart; direct sales have price_cut, orders don't | OrderDetail «صحّح السعر المتفق» | — | FS deep + CorrectionPreview | receivable delta preview → documented revision in event log | guard | **add** (D10, MC-02) |
| Actual-time recording per order | hidden | OrderDetail «شو صار فعليًا» section (promoted when status ≥ execution) | real time feeds honest results | OrderDetail | — | inline card | save inline | — | **move up** (MC-16) |
| Actual material comparison + consume shortcut | hidden | OrderDetail same section | plus consume form must preselect the originating order | OrderDetail «سجل الاستهلاك» → `/inventory/movement/consume?order=:id` | — | inline card → FS | movement saved → back to order | guard | **move up + preselect** (MC-17) |
| Order event log / agreement context memory | present | OrderDetail details drawer | read-only audit + memory without CRM | OrderDetail | — | collapsed drawer | n/a | n/a | keep |

### D. Direct sales

| Feature | Current | Target owner | Why | Primary entry | Secondary | Pattern | After action | Safe return | Decision |
|---|---|---|---|---|---|---|---|---|---|
| Direct sale create (full editor) | present, entry thin | `/direct-sales/new` | rare complex cases; quick path is the sheet | **Orders section CTA «تسجيل بيع مباشر»** (add) | Parties | FS deep | → `/orders` + closure | guard | keep; **add list CTA** (MC-20) |
| Direct sale correction + revisions + conflict guard | present | `/direct-sales/:id` | already strong | Orders rows, receipt «افتح السجل», Parties | — | FS deep | → origin list | guard | keep |
| Price cut (X-06 3-way difference) | present | DirectSaleEditor difference panel | documented returns | on save when collected < agreed | — | inline panel | → `/orders` | guard | keep |
| Sale cancellation (reason) | present | DirectSaleEditor danger zone | record survives | editor | — | DL/inline zone | documented receipt | — | keep |
| **Credit-sale collection** | present, multi-hop | **CollectionSheet [NEW]** over the source | collection today = full editor + difference dialog; sheet = 2 fields | Parties «حصّل من خالد», FAB picker, Home due row | DirectSaleEditor | BS | receipt closure «تم تسجيل التحصيل — الكاش زاد 20.00 — المتبقي على خالد 0» | discard confirm | **add** (D7, MC-03) |

### E. Expenses + financial events

| Feature | Current | Target owner | Why | Primary entry | Secondary | Pattern | After action | Safe return | Decision |
|---|---|---|---|---|---|---|---|---|---|
| Quick expense | present | QuickActionSheet | 10-second rule | FAB | — | BS | receipt | discard confirm | keep |
| Full expense editor (classification) | present | `/finance/new/operating_expense_cash/_payable` | structured classification is optional depth | Finance actions layer | Foundation | FS deep | → `/finance` + closure | guard | keep |
| Expense classification drawer | present | FinancialEventEditor details drawer | progressive disclosure done right | editor | — | drawer | inline | guard | keep |
| Expense/event correction (reverse/atomic edit/delete/restore) | present | EventsLayer inline forms (Finance) | D-005 discipline | `/finance?layer=events`; Home recent rows | — | inline + CorrectionPreview | documented receipt | — | keep; add CorrectionPreview contract (MC-08) |
| Payable recording + settlement with guard | present | FinancialEventEditor (payable types) | عليّ للموردين truth | Finance actions; Home payables road | — | FS deep | → `/finance` | guard | keep |

### F. Cash: wallets, allocations, counting

| Feature | Current | Target owner | Why | Primary entry | Secondary | Pattern | After action | Safe return | Decision |
|---|---|---|---|---|---|---|---|---|---|
| Wallets hub (read) | present | `/cash` | «وين الكاش عندي فعليًا؟» | Finance cards; Home cash road | Tools module | hub reader | n/a | back-to-origin (fallback `/finance`) | keep |
| Wallet creation (4 kinds) | present | `/cash/wallet/new` | declared places | `/cash` primary; Setup (default) | Finance no-wallet road, Foundation | FS deep | → `/cash` | guard | keep |
| Opening known/unknown/zero | present | Setup + wallet editor | unknown ≠ zero at the door | Setup step 3 | — | radio cards (Setup) | — | — | keep; radio cards not `<select>` |
| Opening-later completion (D-004) | present | `/cash/wallet/:id/opening-later` | documented later knowledge | `/cash` unknown rows | — | FS deep | → `/cash` | guard | keep |
| Cash transfer / adjustment / entry reversal | present | `/cash/transfer`, `/cash/wallet/:id/adjust`, `/cash/entry/:id/reverse` | documented movements | `/cash` rows; WalletLedger | — | FS deep + CorrectionPreview | → `/cash` | guard | keep |
| **Cash counting (عدّ الصندوق)** | present, **misplaced entry** | `/cash/count` — **entry moves to `/cash`** | the hub it exits to never links to it; counting happens standing at the drawer | **`/cash` primary button** (thumb zone) | Finance quick links; WalletLedger | FS deep | done screen → `/cash` | **add typed-count guard** | **move entry** (D9, MC-05) |
| **Cash distribution (allocation ±)** | present, **misplaced entry** | `/cash/distribute` — **entry moves to `/cash`** (strip/button when unallocated ≠ 0) | same asymmetry; SoT says «في مالي/المحافظ», code has Finance only | `/cash` strip + button | Finance strip (kept) | FS deep + impact preview | inline success, stays for repeat | **add typed-amount guard** | **move entry** (D9, MC-05) |
| Negative-unallocated alert → resolution | incomplete | alert button → `/cash/distribute?mode=cover` | `cover_payment` is the documented resolution but is UI-unreachable when negative | Finance CashDecisionSurface | — | deep link | distribute | guard | **retarget** (MC-04) |
| **WalletLedger (كشف المحفظة)** | missing | **`/cash/wallet/:id` [NEW]** | «شو صار بدرجي؟» — global log capped at 8 | `/cash` wallet row | Finance | SR | n/a | back to `/cash` | **add** (MC-13) |
| Per-entry reversal from ledger | present (global log only) | WalletLedger rows | reversal belongs next to the movement | ledger rows | — | row action → CorrectionPreview | → ledger | — | **add** (extends existing) |

### G. Amanah + non-cash loss

| Feature | Current | Target owner | Why | Primary entry | Secondary | Pattern | After action | Safe return | Decision |
|---|---|---|---|---|---|---|---|---|---|
| Amanah held / released (balance guard) | present | `/finance/new/amanah_held_cash`, `/finance/new/amanah_released_cash` | real cash, not owned | Finance actions layer | — | FS deep | → `/finance` + closure | guard | keep |
| Amanah dual-truth line | present (Finance) | Finance chip + Statement line + **Home qualifier** | honest dual truth on every cash reading | Finance, `/statement`, Home (when > 0) | — | chip/line | n/a | n/a | keep; promote when > 0 (MC-14) |
| `loss_non_cash` (هالك بلا خروج نقد) | present | `/finance/new/loss_non_cash` | expense without cash | Finance actions | — | FS deep | → `/finance` | guard | keep |

### H. Parties / debts / collections (دفتر الناس)

| Feature | Current | Target owner | Why | Primary entry | Secondary | Pattern | After action | Safe return | Decision |
|---|---|---|---|---|---|---|---|---|---|
| Parties ledger (لك/عليك by name) | present | `/parties` | read-only aggregated book; parent مالي (money, not work status) | Finance quick links; Home away card; FAB picker footer | Tools module | hub reader | n/a | back-to-origin (fallback `/finance`) | keep |
| Name search | present | `/parties` | find-the-person speed | in-page | — | inline | n/a | n/a | keep |
| Party movement links to sources | present | `/parties` expanded rows | the book routes to documents | party rows | — | expandable rows | n/a | n/a | keep |
| **PartyDetail** | missing (accordion acceptable) | **`/parties/:name` [NEW, optional P2]** | many-movement names need a stack screen; keeps list rows one-line | party row (when movements > ~3) | — | SR | n/a | back to `/parties` | **add (optional)** |
| Parties «حصّل من {name}» shortcut | present, hops to source | **CollectionSheet attached** over `/parties` | the shortcut should collect, not just navigate | party row action | — | BS | receipt | discard confirm | **retarget** (D7) |
| Overdue badge «فات متابعته» | partial | `/parties` rows + `?focus=overdue` | calm badge (no red shame); deep link sorts them first | away card, weekly review | — | badge | n/a | n/a | **add focus mode** (MC-15) |
| Direct-sale debts as Home-today items | missing | Home today `due_amount` | daily collections prompt covers the dominant sale type | Home (auto) | — | today row | n/a | n/a | **add** (MC-22) |

### I. Owner money

| Feature | Current | Target owner | Why | Primary entry | Secondary | Pattern | After action | Safe return | Decision |
|---|---|---|---|---|---|---|---|---|---|
| Owner investment | present | `/finance/new/owner_investment_cash` | owner money ≠ revenue | Finance actions; Foundation; Home owner-fact road | — | FS deep | → `/finance` | guard | keep |
| Unified withdrawal (X-05 dual-path) | present | `/finance/withdraw` | one door, dual-path invisible to owner | Finance actions layer | OwnerEntitlement | FS deep | → `/finance` + closure | guard | keep |
| Owner entitlement ledger | present | `/finance/owner-entitlement` | «ما حقي المسجل؟» | Finance link row (demoted card) | Foundation | SR/deep hybrid | → `/finance` | guard | keep; demote card weight |

### J. Suppliers + purchases

| Feature | Current | Target owner | Why | Primary entry | Secondary | Pattern | After action | Safe return | Decision |
|---|---|---|---|---|---|---|---|---|---|
| Suppliers hub + payables card | present | `/suppliers` | «عليّ للموردين كم؟» | Finance link row; Tools module | — | hub reader | n/a | back-to-origin | keep; empty state gets CTA (MC-20) |
| Purchase record | present | `/suppliers/purchase/new` | purchase ≠ COGS (truth card) | Suppliers CTA; Foundation | — | FS deep | → `/suppliers` | guard | keep |
| **Purchase detail view** | **missing (route shows payment form)** | **`/suppliers/purchase/:id` [RETARGET]** | opening a purchase must show the purchase | Suppliers rows; Parties movement links | — | SR | n/a | back to `/suppliers` | **retarget** (D11, MC-01) |
| Supplier payment | present | `/suppliers/purchase/:id/payment` | payment ≤ remaining (guard) | purchase detail button; Suppliers rows | — | FS deep | → `/suppliers` + closure | guard | keep |
| **Purchase correction** | **missing** | **`/suppliers/purchase/:id/edit` [NEW]** | the only record family without a correction path | purchase detail «صحّح الشراء» | — | FS deep + CorrectionPreview | payables delta preview → documented receipt | guard | **add** (D11, MC-01) |
| **Payment reversal** | **missing** | **`/suppliers/purchase/:id/payment/:paymentId/reverse` [NEW]** | documented تراجع موثق for payments | purchase detail payment rows | — | FS deep + CorrectionPreview | → purchase detail | guard | **add** (D11, MC-01) |
| Supplier-name autocomplete | missing (P2, later) | SupplierPurchaseEditor datalist | prevent split ledgers from typos | purchase editor | — | input assist | consistent grouping | — | **add (later)** (MC-23) |

### K. Materials / inventory · L. Catalog · M. Schedule · N. G5

| Feature | Current | Target owner | Why | Primary entry | Secondary | Pattern | After action | Safe return | Decision |
|---|---|---|---|---|---|---|---|---|---|
| Inventory activation (dated, today-only) | present | `/inventory` | late activation never rewrites history | activation card | Tools module status | hub reader | inline | n/a | keep |
| Material + opening balance; receipt/consume/waste/adjust; reversal; extract-remainder | present | `/inventory` + movement editors | typed single-purpose editors | `/inventory` buttons (conditional + «لاحقًا» explainers) | OrderDetail consume shortcut (**preselect order** [add]) | FS deep | → `/inventory` (consume → back to order when deep-linked) | guard | keep; **preselect order** (MC-17) |
| Catalog hub | present (1,859-line page) | `/catalog` | reference library under العمل | Home quiet link; Tools module | draft/sale reference selects | hub (multi-step in-page editor) | inline saves | **contextual back** (today always `/orders`) | keep; add contextual back; long-term step-split (P2) |
| Catalog «سجّل بيع هذا المنتج» shortcut | missing | Catalog reference row | product's knowledge must travel to the sale | Catalog rows | — | action → `/direct-sales/new?item=:id` (reference preselected) | sale editor prefilled | back to Catalog | **add** (MC-19) |
| Schedule agenda + timing edit + postpone | present | `/schedule`, `/schedule/:id` | «وين مواعيدي ومنو متأخر؟» | Orders preview; Home today rows; Tools module | — | hub + FS deep | → `/schedule` | guard | keep; fallback changes `/`→`/orders` |
| Recurrence templates + daily capacity | **hidden** | `/schedule` «التكرار والسعة» — **promoted to a visible section** | recurring work is a real capability buried in a settings-like layer | schedule page | Home capacity deep link `?layer=capacity` | section | inline | **add guard** | **move up** (MC-16) |
| G5 declaration create + reversal; coverage/break-even reading | present | `/finance/g5/declaration`; Finance layers | قبض/دفع متوقع | Finance CashDecision **«سجّل قبضًا أو دفعًا متوقعًا»** (rename from «أعلن…») | — | FS deep + layer | → `/finance` | guard | keep; **rename** (MC-21) |

### O. Finance readings + سجل · P. Tools · Q. Onboarding · R. Settings · S. Offline

| Feature | Current | Target owner | Why | Primary entry | Secondary | Pattern | After action | Safe return | Decision |
|---|---|---|---|---|---|---|---|---|---|
| Finance landing order | present, misordered | `/finance` — decision blocks first, then position, then layers | decision before reading | tab 3 | — | hub reader | n/a | n/a | keep; **reorder**; remove back-to-Home button |
| Position 4 cards; period result + insights; coverage; deposits; events; corrections layers | present | Finance layers | deep reading is on-demand | Finance | `/statement` (plain view) | collapsed layers | n/a | n/a | keep; ReviewPulse demotes into «صورة الطلبات» layer |
| Actions layer (11 buttons) | present | Finance «سجّل حركة أو افتح مصدر» — **grouped** (قبض/صرف · مالك · أمانات وهالك · تسديد) | rare writes grouped by intent | Finance layer | Foundation CTAs | grouped buttons | → editors | guards | keep; **group** |
| **StatementView (كشف الأسبوع)** | **missing** | **`/statement` [NEW]** | the owner question «كيف كان أسبوعي؟» has no home | Home «عرض تفاصيل الأسبوع»; Finance period layer «كشف بسيط» | receipts | SR | n/a | back-to-origin | **add** (D8, MC-09) |
| Cost calculator (live result) | present | `/tools` | zero-effect thinking tool; the result is the product | tab 4 | — | workspace + **sticky result bar** | n/a | **add soft guard** | keep |
| Saved estimates list + estimate→draft bridge | present | `/tools` | reviewable thinking | Tools | — | section | inline delete; bridge → prefilled draft | guard | keep |
| **Estimate detail / edit** | **incomplete** | **`/tools/estimates/:id` [NEW]** | service `update()` exists unused; delete+re-enter is the only correction | estimate row | — | FS deep | → `/tools` | guard | **add** (MC-07) |
| Module status matrix | present | `/tools` | optional-capability honesty | Tools | — | section rows | n/a | n/a | keep |
| Setup wizard (3 steps, draft persistence, skip-wallet) | present | `/setup` | minimum friction first-use | StartupGate | Settings reset exit | setup | → `/foundation` | localStorage draft | keep; radio cards for step 3 |
| Foundation (always-open front door) | present | `/foundation` | skipped items become roads, never zeros | post-setup; Home quiet link | — | hub | exits → `/` | n/a | keep; single primary exit |
| Guided opening import | **hidden** | Settings **visible row** + Foundation row | a real recovery path buried in a collapsed layer | Settings; Foundation «عندي ملف موقف جاهز» | — | row → preview | import flow | — | **move up** (MC-16) |
| Settings hub; verified export; import with preview; reset; preferences | present | `/settings` | protection + preferences | header gear | Home away card `?focus=export` | hub rows | inline; `lastVerifiedExportAt` recorded | — | keep; add staleness line |
| Offline banner + truthful local privacy; PWA install/update; storage failure recovery; 404 | present | shell + StartupGate + NotFound | local-first needs honest failure UX | auto | — | banner/cards/full-screen | reload | — | keep; add last-export staleness to locality lines |

**Decision tally (approximate — compound rows can be read several ways):** keep ~90 · move/move-up 7 · retarget 5 · add ~14 · make-secondary 2 · remove 1 · defer 1 ("merge" is available in the decision vocabulary but no capability required it — the closest case, Home's optional modules merging into the links row, is filed under make-secondary). New routes: 6 + 1 optional; retarget: 1. New query params: `?focus=`, `?layer=`, `?mode=cover`, `?from&to`.

## 3.5 Target screen map

```
AppHeader (all screens): «مايكرو» + contextual label · gear → /settings · theme
StartupGate (boot): no profile → /setup · storage failure → recovery (public: /setup, /settings)

══════════ LEVEL 1 — BOTTOM NAV (surface) ══════════

مشروعي الآن  /                                        سجّل  (FAB — center, all surface screens)
├─ away card ──→ /parties?focus=overdue                ├─ تسجيل بيع      (in-sheet: المبلغ + محفظة «الدرج»)
├─ truth lines ──→ /settings?focus=export              ├─ تسجيل مصروف    (in-sheet)
├─ today rows ──→ /orders/:id?focus=collect            ├─ طلب من عميل   ──→ /orders/draft/new?intent=customer_order
│                 /orders/draft/:id · /schedule/:id    ├─ مسودة تصميم   ──→ /orders/draft/new?intent=planned_design
├─ facts (2×2) ──→ /cash · /parties · /finance/new/*  └─ تحصيل أو عربون ──→ collection picker [RETARGET]
├─ عرض السجل ────→ /finance?layer=events                    ├─ party rows ──→ CollectionSheet [NEW sheet]
└─ عرض تفاصيل الأسبوع → /statement [NEW]                    └─ footer ─────→ /parties?focus=receivable

العمل  /orders                                        مالي  /finance
├─ «الأولوية الآن» (first, always)                    ├─ قرار الكاش (first) ──→ /finance/g5/declaration
├─ مبيعاتي rows ──→ /direct-sales/:id                 ├─ unallocated strip ──→ /cash/distribute (+ ?mode=cover)
├─ طلباتي rows ──→ /orders/:id                        ├─ position cards 2×2 → /cash · /parties · /suppliers
├─ مسودات rows ──→ /orders/draft/:id                  ├─ أمانات line (when > 0)
├─ المواعيد preview → /schedule                       ├─ quick links: دفتر الناس · الموردون · عدّ الصندوق · دفتر حق المالك
└─ إنشاء مسودة أخرى / تسجيل بيع مباشر [add]           └─ layers: قراءة الفترة → /statement · صورة الطلبات ·
                                                          التغطية والتعادل · سجّل حركة (grouped) · عربونات ·
                                                          السجل (?event=) · تصحيحاتي الموثقة

أدواتي  /tools
├─ calculator (sticky live result — zero writes)
├─ تقديراتي rows ──→ /tools/estimates/:id [NEW] ── «ابدأ مسودة» → /orders/draft/new?intent=planned_design&estimate=:id
└─ حالة الوحدات rows → /inventory · /catalog · /schedule · /suppliers · /parties

══════════ LEVEL 2 — DOMAIN HUBS (surface) ══════════

/cash (parent مالي)                    /parties (parent مالي)           /suppliers (parent مالي)
├─ wallet rows ──→ /cash/wallet/:id    ├─ party rows (expand |           ├─ open purchases ──→ /suppliers/purchase/:id
│    [NEW] WalletLedger                │   >3 movs → /parties/:name      │   [RETARGET] PurchaseDetail
│    └ «عدّ الصندوق» → /cash/count     │   [NEW, optional])              ├─ «سجل شراء مواد» → /suppliers/purchase/new
├─ «محفظة ورصيد بداية» → /cash/wallet/new ├─ «حصّل من X» → CollectionSheet └─ «سجل دفعة» → …/payment
├─ تحويل → /cash/transfer              └─ movement rows → sources       /inventory (parent مالي)
├─ unallocated strip → /cash/distribute [MOVED ENTRY]                    ├─ activate (dated, today-only)
└─ «عدّ الصندوق» → /cash/count [MOVED ENTRY]  /catalog (parent العمل)   ├─ material rows; movements; reversals
                                            └─ steps: reference → template └─ receipt/consume/waste/adjust editors
/schedule (parent العمل — fallback changed /→/orders)
├─ متأخر / اليوم / قادم → /schedule/:id
└─ التكرار والسعة (promoted section, ?layer=capacity)

══════════ LEVEL 3 — STACK READERS (surface + back→origin) ══════════

/orders/:id (OrderDetail)             /cash/wallet/:id [NEW]            /parties/:name [NEW, optional]
├─ sticky contextual CTA              ├─ full entry ledger              ├─ balance header
├─ debt panel (?focus=collect)        └─ «عدّ الصندوق» → /cash/count    └─ «حصّل» → CollectionSheet
├─ «صحّح السعر المتفق» → /orders/:id/price [NEW]
└─ «شو صار فعليًا»: actual time/material (promoted) → /inventory/movement/consume?order=:id

/suppliers/purchase/:id [RETARGET]    /statement [NEW]                  /foundation (surface)
├─ remaining + payments               ├─ period switcher (?from&to)     └─ sections → each editor
├─ «سجل دفعة» → /payment             └─ rows → sources
├─ «صحّح الشراء» → /edit [NEW]
└─ payment rows → …/payment/:pid/reverse [NEW]

══════════ LEVEL 4 — DEEP EDITORS (chrome hidden, UnsavedChangesGuard) ══════════

/orders/draft/new · /orders/draft/:id (lazy, ?intent=, ?estimate=)
/orders/draft/:id/cost (+ linked-draft guard) · /orders/draft/:id/agreement
/direct-sales/new · /direct-sales/:id (revisions, X-06 difference, cancel)
/finance/new/:type (8 types) · /finance/withdraw · /finance/owner-entitlement · /finance/g5/declaration
/suppliers/purchase/new · /edit [NEW] · /payment · /payment/:pid/reverse [NEW]
/cash/wallet/new · /transfer · /distribute (?mode=cover) · /count · /wallet/:id/adjust
/cash/wallet/:id/opening-later · /cash/entry/:id/reverse
/inventory/material/new · /movement/:type (?order=) · /movement/:id/reverse
/orders/:id/price [NEW] · /tools/estimates/:id [NEW] · /schedule/:id

══════════ SYSTEM ══════════
/setup (chrome-less wizard → /foundation) · /settings (gear) · /review → /finance · * → NotFound → /
```

**Sheet layer (no route, overlays any surface screen):** QuickActionSheet (menu/sale/expense/receipt) · collection picker · **CollectionSheet [NEW]** · MaterialSheet (cost editor) · expense-context drawer · **CorrectionPreview dialog [NEW]** («ما سيتغير / ما لن يتغيّر») · delete/reset confirm dialogs.

---

# 4. OUTPUT B — Screen Hierarchy & Textual Wireframes

## 4.0 Global conventions (apply to every screen)

**Thumb-zone model (one-handed, small portrait phone, 360×640 reference):**

| Zone | Content | Rule |
|---|---|---|
| Top ~25% (hard to reach) | Orientation only: screen question, date, status chips | No inputs, no primary buttons |
| Middle | Scan cards: facts, list rows, previews | Read-only; each row = one tap target |
| Bottom ~33% (thumb zone) | Primary CTA + numeric inputs of the fast path | Sticky action bar on deep editors; FAB «سجّل» on surfaces |

Documented exceptions (kept deliberately): Setup / CashCount / CashDistribution / AgreementEditor / CostEditor / FinancialEventEditor place the primary button at the bottom of a short form card (bottom of scroll — acceptable because the form is short; becomes sticky when the form exceeds one screen). Tools has no mandatory action — the live result bar occupies the thumb zone and save is secondary. Settings is a utility screen where every row owns its action.

**JOD & RTL number rules (binding):**
1. Unit after the number: `20.00 د.أ` — never `د.أ 20.00`, never a `(د.أ)` prefix inside labels (both exist today: `Orders.tsx:28` «دين مسجل (د.أ): 20.00» vs `CashCount` messages «… 20.00 د.أ»).
2. ASCII digits, `en-US` grouping, isolated with `bdi dir="ltr"` (pattern already used in `Home.tsx:98`).
3. Never mix «دينار» with «د.أ» (`DirectSaleEditor.tsx:507-508` says «الفرق 2.00 دينار»).
4. Signed deltas isolated LTR: `+5.00 د.أ` / `−5.00 د.أ`.
5. Unknown ≠ zero: «—» mark + a road («سجّله»), or «غير محدد بعد» for unknown wallet opening, «غير متاح» for unusable readings.
6. Dates `dd/MM/yyyy` LTR-isolated for compact rows; Arabic long date for headers; numeric keypads (`inputmode`) with ASCII-only money fields.

**The 12 states vocabulary:** `empty · loading · saving/busy · success · error · offline · unknown-value · partial-data · unsaved-input · cancel · back · correction`. Success = non-blocking + closure sentence + Undo only where safely reversible (undo always routes through the explicit correction flow with preview). Offline = truthful local privacy line, only when actually offline or export is stale. Correction = always preview → confirm → documented receipt («تراجع موثق»), never silent.

**Wording baseline (glossary-bound owner language):** «حدث مالي», «دين», «لي عند العملاء», «عليّ للموردين», «حق المالك», «سعر الحماية», «نسخة التكلفة», «المتوقع/قبض متوقع/دفع متوقع» (never «أعلن» — violated today in `Finance.tsx:1025`), «توزيع/موزّع/غير موزّع», «تراجع موثق», «د.أ بعد الرقم», «الخطوة التالية».

## 4.1 «مشروعي الآن» — Home (`/`)

**Screen Contract**

| Field | Value |
|---|---|
| Goal | «ماذا عليّ اليوم؟ وما هو مسجل؟» |
| Entry points | Bottom-nav tab 1; cold start; back from Finance/Schedule |
| Exit(s) | Any today-item → its source; facts → their owners; tabs; FAB |
| Primary action | FAB «سجّل» (global, thumb zone) — no in-page primary competes |
| Source-of-truth owner | None (read model: homeControlCenterService) |
| Acceptance criteria | 1) First today item is the single priority, fully visible without scrolling. 2) Unknown facts show «—»/road, never 0.00. 3) ≤8 top-level blocks before «ما تغير مؤخرًا». 4) Away card appears only after 7 idle days and includes a guilt-free «ابدأ من اليوم» action |

**Target content hierarchy**

- **Header**: «مشروعي الآن» overline + activity name + long date (orientation only).
- **Body (top→bottom)**: ① away card (conditional) ② truth lines (backup age, locality — conditional, one row each) ③ «اليوم» list — max 5 rows, action-specific labels ④ «ما هو مسجل حتى الآن؟» — 4 fact chips 2×2, tappable ⑤ «ما تغير مؤخرًا» — 3 rows + «عرض السجل».
- **Primary CTA**: FAB «سجّل». The «مالي»/«منتجاتي وخدماتي» units demote to one quiet links row (the tabs already carry them).
- **On-Demand details**: each today row's date/time inline; facts' source/period/helper behind tap; full recent-changes behind «عرض السجل»; upcoming count behind «قادمة: …».
- **Special states**: empty («لا متابعات اليوم — يومك مفتوح. سجّل أول شي يصير.»), loading ✅ exists, error ✅ (keep reload), offline («شغال بدون إنترنت — كل شي محفوظ على جهازك» when `navigator.onLine === false`), unknown («—» + road), partial (away digest describes last recorded day only).

**Textual wireframe**

```
[Screen: مشروعي الآن  /]
Header: "مشروعي الآن" · «مشغل ليان» · الخميس 12 أيلول 2026
(conditional) Away card: "أثناء غيابك — آخر تسجيل قبل 9 أيام"
  · "آخر يوم تسجيل (3 أيلول): بيع 2 بـ 45.00 د.أ · مصروف 1 بـ 6.50 د.أ"
  · "2 دين فات موعد متابعته — راجع دفتر الناس" [tap → /parties?focus=overdue]
  · "ما في نسخة احتياطية معتمدة بعد — انسخ الآن" [tap → /settings?focus=export]
  · quiet: "ابدأ من اليوم — التاريخ ما بيفرق" [tap → FAB sheet]
(conditional) truth line: "بياناتك على هذا الجهاز فقط — آخر نسخة مصدّرة 12/09/2026" [الإعدادات]
Body 1 "اليوم" (قراءة الصباح):
  "تسليم غدًا — صندوق خشبي · سارة"  [سلّم ← → OrderDetail]
  "تحصيل مستحق — خالد · 20.00 د.أ"   [حصّل ← → CollectionSheet/OrderDetail?focus=collect]
  "أكمل تكلفة — طلب ريم"             [أكمل ← → OrderDetail]
  (empty: "لا متابعات اليوم — يومك مفتوح. سجّل أول شي يصير.")
  "قادمة: 15 أيلول — افتح أقربها" [tap → /schedule]
Body 2 "ما هو مسجل حتى الآن؟" (2×2 chips, each tappable):
  الكاش المسجل 145.00 د.أ (منها أمانات 10.00 د.أ) | لي عند العملاء 20.00 د.أ
  عليّ للموردين 0.00 د.أ  | مال المالك المسجل — سجّله (نقرة)
  (unknown fact → "—" ; not_initialized → «سجّله (نقرة)» road;
   when unallocated ≠ 0: line under cash chip "غير موزع: 35.00 د.أ — وزّعه [→ /cash/distribute]")
Body 3 "ما تغير مؤخرًا":
  "11 أيلول · بيع مباشر — كوب قهوة · 3.00 د.أ" [tap → DirectSaleEditor]
  "11 أيلول · مصروف — أكياس تغليف · 2.50 د.أ" [tap → /finance?event=…]
  "عرض السجل" [tap → /finance?layer=events]
Quiet links row: "صفحة الأساس · مالي · منتجاتي وخدماتي · أدواتي" (text actions, no primary buttons)
Offline: "شغال بدون إنترنت — بياناتك محفوظة على هذا الجهاز"
Primary CTA: [FAB «سجّل» — bottom center, thumb zone → QuickActionSheet]
```

## 4.2 «العمل» — Orders (`/orders`)

**Screen Contract**

| Field | Value |
|---|---|
| Goal | «وين وصلت الطلبات والمسودات؟ وإيش الأولوية؟» |
| Entry points | Bottom-nav tab 2; OrderDetail back; QuickActionSheet deep intents |
| Exit(s) | Rows → OrderDetail / DirectSaleEditor / DraftEditor; مواعيد row → ScheduleEditor; FAB |
| Primary action | First actionable row (contextual). Page-level secondary: «إنشاء مسودة أخرى» + «تسجيل بيع مباشر» [NEW] |
| Source-of-truth owner | Read model over orders/drafts/directSales/schedules |
| Acceptance criteria | 1) «الأولوية الآن» is the first body block (before any list) and always rendered. 2) Direct-sale row ≤3 text lines; revisions/canned next-steps deferred to detail. 3) Empty state offers «سجّل أول بيع». 4) Every money value renders `د.أ` after the number |

**Textual wireframe**

```
[Screen: العمل  /orders]
Header: "العمل" — الطلبات والمسودات ودورتها
Body 1 "الأولوية الآن" (DecisionPanel, accent — first, always rendered):
  truth: "دين مستحق بعد التسليم: 20.00 د.أ" · nextAction: "حصّل المتبقي أو سجّله دينًا"
Body 2 "طلباتي" (سجل محفوظ):
  [صندوق خشبي] اتفاق مؤقت · موعد التسليم 13 أيلول
    المتبقي: 20.00 د.أ   الخطوة التالية: سجّل العربون أو ابدأ التنفيذ  [→ OrderDetail]
Body 3 "مبيعاتي":
  [كوب قهوة] 11 أيلول · قبض 3.00 من 3.00 د.أ — كامل       [→ DirectSaleEditor]
  [كيكة شوكولا] 10 أيلول · قبض 8.00 من 10.00 · الباقي 2.00 د.أ دَين على خالد  [→ DirectSaleEditor]
  (row ≤ 3 lines; الربح والتخفيضات خلف التفاصيل)
  + "تسجيل بيع مباشر" [NEW secondary CTA → /direct-sales/new]
Body 4 "مسودات قيد الإكمال": [طلب ريم] طلب من عميل · الخطوة التالية: أكمل ما تعرفه الآن [→ DraftEditor]
Body 5 "المواعيد": "متأخر · 12 أيلول — تسليم صندوق سارة" (+2) — "افتح جدول المواعيد"
Secondary: "إنشاء مسودة أخرى"
(empty-all): "لا توجد سجلات عمل بعد — ابدأ من الفعل الذي تحتاجه اليوم" + [سجّل أول بيع → QuickActionSheet]
Primary CTA: [FAB «سجّل» + first row tap]
Offline: "شغال بدون إنترنت — سجلاتك محفوظة على هذا الجهاز"
```

## 4.3 «سجّل» — QuickActionSheet (FAB bottom sheet)

**Screen Contract**

| Field | Value |
|---|---|
| Goal | «سجّل شيئًا الآن في أقل من 10 ثواني» — quick sale/expense in-sheet; deeper intents routed |
| Entry points | FAB «سجّل» (all surfaces) |
| Exit(s) | Receipt «تم» closes over standing screen; deep intents → DraftEditor; collection → picker |
| Primary action | «سجّل البيع» / «سجّل المصروف» inside the sheet |
| Source-of-truth owner | directSales + projectFinance (idempotency keys); wallet attribution via allocation |
| Acceptance criteria | 1) Cash sale = 1 mandatory input (المبلغ) + default wallet «الدرج»; all else progressive behind «خيارات أكثر». 2) From Home ≤2 taps to submit. 3) Receipt shows closure numbers + «تراجع» opening the documented cancel flow. 4) Closing with a typed amount asks before discarding |

**Textual wireframe**

```
[Sheet: سجّل — Menu]
Title: "ماذا تريد أن تسجّل؟"
  [تسجيل بيع]   احفظ بيعًا مباشرًا من دون إنشاء طلب.        (in-sheet)
  [تسجيل مصروف] سجّل مصروفًا مدفوعًا في لحظته.              (in-sheet)
  [طلب من عميل] ابدأ مسودة طلب واتفاق أولي.                 (→ DraftEditor)
  [مسودة تصميم] ابدأ مسودة قبل الاتفاق.                     (→ DraftEditor)
  [تحصيل أو عربون] حصّل دينًا قائمًا باسم صاحبه.            (→ collection picker [RETARGET])

[Sheet: سجّل بيعًا الآن]
المبلغ المحصل (د.أ)   [   20.00  ]        ← first, huge, keypad
[ سجّل البيع ]                          ← primary, directly under
▾ خيارات أكثر
   ما الذي بعته؟ (اختياري) [كوب قهوة]
   هل تعرف تكلفته؟ (لا أعرف الآن — الربح «غير متاح» لا صفر / نعم → التكلفة)
   هل بقي شيء عليه؟ (قُبض المبلغ كاملًا / آجل → اسم الزبون + المحصل الآن)
   محفظة القبض: ● الدرج (افتراضي) / اتركه غير موزّع / محفظة أخرى
Receipt: "سُجّل بيع 20.00 د.أ — الكاش زاد 20.00 وصار 165.00 د.أ"
          [افتح السجل → /direct-sales/:id]  [تراجع → تصحيح موثق بمعاينة]  [تم]
(credit case adds: "الباقي 2.00 د.أ دَين على خالد — حصّله من دفتر الناس")
```
(Expense form mirrors: المبلغ first, البند optional, محفظة الصرف default «الدرج».)

## 4.4 «مالي» — Finance (`/finance`)

**Screen Contract**

| Field | Value |
|---|---|
| Goal | «وين الكاش؟ وإيش الوضع المالي والقرار اللي عليّ؟» |
| Entry points | Bottom-nav tab 3; deep links `?event=`; back from cash/parties/suppliers |
| Exit(s) | Cash decision → G5 editor; unallocated strip → distribute; cards → hubs; layers expand in place |
| Primary action | Contextual: «وزّع على محفظة» when unallocated > 0, else «سجّل قبضًا أو دفعًا متوقعًا» (renamed from «أعلن…») |
| Source-of-truth owner | Read model over position/period/insights/G5/owner/pulse/deposits + events & corrections layers |
| Acceptance criteria | 1) Decision blocks before reading blocks. 2) Amanah line visible whenever > 0 with the dual-truth sentence. 3) ≤5 body blocks visible before the first collapsed layer. 4) No «أعلن» wording anywhere |

**Textual wireframe**

```
[Screen: مالي  /finance]
Header: "مالي" — قراءة مالية مسجلة          (back-to-Home button REMOVED — it is a tab)
Body 1 "قرار الكاش · 1 → 31 أيلول":
   الكاش المسجل الآن 145.00 د.أ | قبض متوقع قريب 20.00 د.أ
   دفع متوقع قريب 15.00 د.أ    | الكاش المتوقع 150.00 د.أ
   الحالة: مسجل · الخطوة التالية: راجع دفعًا متوقعًا قريبًا
   [سجّل قبضًا أو دفعًا متوقعًا]        ← renamed primary
Body 2 (if >0) "كاش غير موزع: 35.00 د.أ — وزّعه على محفظة الآن، أو اتركه حتى تعرف وجهته"
   [وزّع على محفظة → /cash/distribute]
Body 3 "الوضع المسجل" (2×2):
   الكاش المسجل 145.00 (محافظ معلنة + غير موزع) [→ /cash]
   لي عند العملاء 20.00 (دين مسجل بعد التسليم)  [→ /parties]
   عليّ للموردين 0.00 (مصروفات أو مشتريات مستحقة) [→ /suppliers]
   مال المالك المسجل — غير مسجل، سجّله (نقرة)     [→ /finance/owner-entitlement]
Body 4 (if >0): "أمانات بحوزتك 10.00 د.أ — كاش حقيقي في الدرج لكنه ليس لك ولا يدخل الربح."
Body 5 quick links: دفتر الناس · الموردون · عدّ الصندوق · دفتر حق المالك
Layers (details): ▸ قراءة الفترة (نتيجة الفترة المسجلة + المؤشرات) → «كشف بسيط» → /statement [NEW]
                  ▸ صورة الطلبات: قبض ودين ونتائج (ReviewPulse demoted here) + استبعادات
                  ▸ التغطية والتعادل + سجل المتوقعات
                  ▸ سجّل حركة أو افتح مصدر (أزرار مجمّعة: قبض/صرف · مالك · أمانات وهالك · تسديد)
                  ▸ عربونات · السجل (?event=) · تصحيحاتي الموثقة
Offline: "شغال بدون إنترنت — كل الأرقام من هذا الجهاز"
Primary CTA: [FAB «سجّل» + contextual قرارات أعلى الصفحة]
```

## 4.5 «أدواتي» — Tools (`/tools`)

**Screen Contract**

| Field | Value |
|---|---|
| Goal | «احسب قبل أن تلتزم» — pricing decision before commitment; zero financial effect |
| Entry points | Bottom-nav tab 4; bridge back-link from draft editor |
| Exit(s) | Estimate row → detail [NEW] / draft bridge; module rows → hubs; tab away |
| Primary action | None mandatory — **the live result is the product**; «احفظ التقدير» is secondary |
| Source-of-truth owner | costEstimates store — zero cash/balance/inventory impact, always tagged «تقديري» |
| Acceptance criteria | 1) «سعر الحماية» visible at all times while typing (sticky bar in thumb zone). 2) The disclaimer appears exactly once. 3) Incomplete knowledge → «—» + reason, never a number. 4) Leaving with typed input asks before discarding |

**Textual wireframe**

```
[Screen: أدواتي  /tools]
Header: "أدواتي" — احسب قبل أن تلتزم
Rule line (once): "هذا حساب تقديري. ما انحفظت أي حركة مالية ولا مخزون."
عنوان التقدير (اختياري) [كيكة مناسبة صغيرة]
المادة 1: [دقيق] [2 كيلو] [سعر الوحدة 1.750 د.أ]
   + أضف مادة أخرى
هل تحسب وقت عمل؟ (بلا وقت الآن / نعم → دقائق + أجر الساعة)
عدد القطع الناتجة [4]
▸ بنود أخرى وحماية السعر (تغليف/توصيل/هدر/هامش)
────────────── sticky bar (thumb zone) ──────────────
سعر الحماية: 12.50 د.أ للقطعة   [حالة المعرفة: معروفة ▾]
(المزيد: تكلفة القطعة 10.00 · الإجمالي المتوقع 40.00)
[احفظ التقدير لمراجعته لاحقًا]  (secondary)
"تقديراتي المحفوظة":
  كيكة مناسبة صغيرة · تقديري · سعر الحماية 12.50 د.أ · 12 أيلول
    [افتح التقدير → /tools/estimates/:id NEW] · [ابدأ مسودة من هذا التقدير] · [🗑]
"حالة الوحدات": حاسبة التكلفة مفعّلة · المخزون متاح — غير مفعّل · …
```

## 4.6 OrderDetail (`/orders/:id`)

**Screen Contract**

| Field | Value |
|---|---|
| Goal | «شو حالة هذا الطلب وإيش الخطوة التالية؟» |
| Entry points | Orders rows; Home today items; Finance exclusion links; Parties debt links |
| Exit(s) | Back → origin; contextual action consumes the step; cancel documented; details in place |
| Primary action | Status-contextual: «ابدأ التنفيذ» → «الطلب جاهز للتسليم» → «تم التسليم» → «تحصيل المتبقي الآن»/«تسجيله دينًا» |
| Source-of-truth owner | agreements/fulfillment services (CraftOrder + order events) |
| Acceptance criteria | 1) Contextual primary in a **sticky bottom bar** (today mid-page after 3 cards, `OrderDetail.tsx:250`). 2) Every status transition ends with a closure sentence. 3) Cancel is a quiet action with reason choices + deposit impact preview. 4) Debt-collection panel prefilled with المتبقي (exists ✅) |

**Textual wireframe**

```
[Screen: طلب — صندوق خشبي  /orders/abc]
Header: "اتفاق مؤقت" · صندوق خشبي · سارة · الكمية: 2
Body 1 "الخطوة التالية": سجّل العربون أو ابدأ التنفيذ · موعد التسليم: 13 أيلول
Body 2 chips: السعر المتفق 35.00 د.أ | المتبقي 20.00 د.أ | عربون محصل 15.00 د.أ (كاش مرتبط بالطلب)
quiet: [صحّح السعر المتفق → /orders/:id/price NEW]
Body 3 (settled+debt) "تحصيل الدين المسجل": قبضت الآن من الدين (د.أ) [20.00] → [سجّل القبض]
   success: "تم تسجيل التحصيل — الكاش زاد 20.00 د.أ — المتبقي على سارة 0 د.أ"
Body 4 (delivered/settled) result: "نتيجة الطلب معروفة · 12.00 د.أ — عند التسليم: السعر 35.00 · التكلفة 23.00"
"شو صار فعليًا" [NEW promoted section when status ≥ execution]:
   وقت فعلي [سجل الوقت] · مواد فعلية [سجل الاستهلاك → /inventory/movement/consume?order=:id]
quiet: [إلغاء الطلب] → panel: سبب بنقرة (غلط في السعر/انسحب العميل/سبب آخر/تخطٍّ) + عربون impact:
   "يوجد عربون محصل 15.00 د.أ — يبقى «يحتاج مراجعة» حتى تردّه أو تحتفظ به."
▸ تفاصيل إضافية (الاتفاق، سجل الطلب)
────────── sticky bar (thumb zone) ──────────
[ ابدأ التنفيذ ]        ← contextual primary
```

## 4.7 Draft / Cost / Agreement editors (order-creation chain)

**DraftEditor** (`/orders/draft/:id`) — Goal «سجّل قصة الطلب قبل التكلفة»; ≤3 visible fields on open (وصف، اسم الزبون، الكمية); catalog reference deferred to «خيارات متقدمة»; unsaved guard ✅; estimate-bridge notice ✅; delete 2-step ✅; primary «احسب التكلفة».

```
[Screen: مسودة — طلب من عميل]
Header: "مسودة محلية — طلب من عميل" · نسجل القصة والكمية الآن.
(bridge) "بدأت هذه المسودة من تقديرك «كيكة مناسبة صغيرة» — القيم مقترحات قابلة للتعديل."
وصف القطعة (مطلوب قبل الانتقال للتكلفة) [صندوق خشبي مخصص]
اسم الزبون (اختياري) [سارة]
الكمية (0–9) [2]
ملاحظات التخصيص [لون بني، حفر اسم…]
▸ خيارات متقدمة: مرجع العمل (منتجاتي وخدماتي)
[حفظ مسودة]  [احسب التكلفة]   ← primary
(quiet) احذف المسودة → "الحذف نهائي بلا أثر مالي — المسودة لم تصبح طلبًا." [تراجع]
```

**CostEditor** (`/orders/draft/:id/cost`) — Goal «قَدّر تكلفة هذا الطلب قبل ما تلتزم بسعر»; live result card sticky; knowledge gaps listed with إلزامي/اختياري chips; MaterialSheet drawer ✅; incomplete-save allowed with «لا تدخل صفرًا بدل المجهول» guidance; **[NEW] linked-draft guard** (redirect to `/orders/:id` like its siblings).

```
[Screen: تكلفة — صندوق خشبي]
"سعر الحماية لكل قطعة: 17.50 د.أ" [تقديرية] (sticky while editing)
  gaps: [إلزامي] وقت العمل ناقص · [اختياري] تغليف غير مضاف
المواد: [خشب 2 قطعة · تكلفة الوحدة 6.00 · مؤكد] [🗑] + [＋]
وقت العمل: [اترك الوقت غير مكتمل / إضافة وقت → دقائق 90 · سعر الساعة 5.00]
▸ بنود أخرى وحماية السعر: [+ تغليف] [+ توصيل] [+ هدر] [+ هامش الحماية]
(ناقصة): "يمكنك حفظ ما تعرفه الآن كمسودة ناقصة… لا تدخل صفرًا بدل المجهول."
[حفظ مسودة تكلفة ناقصة / حفظ نسخة التكلفة]  [تسجيل الاتفاق]
```

**AgreementEditor** (`/orders/draft/:id/agreement`) — Goal «سجّل الاتفاق: السعر وموعد التسليم والعربون»; price field first with «استخدم سعر الحماية كبداية» chip; below-floor acknowledgment; deposit optional + truth line; primary «تسجيل الاتفاق» → OrderDetail + closure «انسجّل الاتفاق — الطلب محفوظ بموعد تسليم 13 أيلول».

```
[Screen: سجّل ما اتفقت عليه]
"سعر الحماية المشتق من نسخة التكلفة: 17.50 د.أ × 2 = 35.00 د.أ (تقديرية)"
السعر المتفق عليه (د.أ) [35.00]  [استخدم سعر الحماية كبداية]
(إذا أقل): ☑ "السعر أقل من سعر الحماية. راجعت السبب وأريد التسجيل كما هو."
موعد التسليم [13/09/2026]
العربون المحصل الآن (د.أ) [15.00] (اختياري؛ اتركه فارغًا إذا لم تقبض)
  "العربون كاش محصل مرتبط بالطلب، وليس ربحًا نهائيًا."
▸ كيف تم الاتفاق؟ (WhatsApp / إحالة / زيارة مباشرة…)
[تسجيل الاتفاق]  → OrderDetail + closure
```

## 4.8 DirectSaleEditor (`/direct-sales/:id`)

**Screen Contract**

| Field | Value |
|---|---|
| Goal | Full workspace for one direct sale: create (rare) / **correct / settle difference / cancel** |
| Entry points | Orders «مبيعاتي» rows; receipt «افتح السجل» [NEW]; Parties debt links |
| Exit(s) | Save → `/orders` (+ closure); cancel documented → `/orders`; back guarded |
| Primary action | «حفظ البيع المباشر» / «حفظ تصحيح البيع» / «أكمل الحفظ بالقرار المختار» |
| Source-of-truth owner | directSales store (revisions preserve originals) |
| Acceptance criteria | 1) السعر immediately after الاسم; الكمية deferred. 2) X-06 difference prompt stays: 3 choices incl. «يحتاج مراجعة». 3) Cancel requires reason + states the record survives. 4) Revision history card shows originals |

```
[Screen: تصحيح بيع مباشر — كيكة شوكولا]
"حد الحقيقة: التحصيل ليس ربحًا." (cost unknown → الربح «غير متاح» لا صفر)
(revisions) "الأصل يبقى في السجل: خفّضتُ السعر — الأصلي 12.00 د.أ · سبب: خصم"
ما الذي بعته؟ (اختياري) [كيكة شوكولا]
السعر المتفق عليه (د.أ) [10.00]
ما قبضت الآن (اتركه فارغًا إذا قبضت كامل السعر) [8.00]
   → difference panel: "اتفقيتَ على 10.00 وقبضتَ 8.00 — الفرق 2.00 د.أ. اختر ما حدث فعلًا:"
     ○ خفّضتُ السعر (يصير 8.00، لا دَين) ○ الباقي عليه (2.00 د.أ في «لي عند العملاء») ○ يحتاج مراجعة
▸ تفاصيل أكثر: الكمية · التكلفة · رابط مرجع · التاريخ · بيان
(اسم الزبون يظهر عند وجود دين/زبون ✅)
[أكمل الحفظ بالقرار المختار / حفظ تصحيح البيع]
danger zone: [إظهار تأكيد الإلغاء] → سبب (مطلوب) + "سيبقى البيع ظاهرًا بحالة ملغى، ولن يُحذف بصمت."
```

## 4.9 FinancialEventEditor (`/finance/new/:type`) — 8 types

**Contract:** effect preview card top (exists ✅) strengthened into a «ما سيتغير / ما لن يتغيّر» pair; amount + note = only required fields; amanah-release shows held-balance guard ✅; payable settlement shows remaining preview ✅; unsaved guard ✅.

```
[Screen: حدث مالي — سجل أمانة قُبضت]
"الأثر المعروف: الكاش + · أمانات + · لا مصروف ولا ربح."
  ما سيتغير: الكاش 10.00 د.أ ↑ · أمانات بحوزتك 10.00 ↑
  ما لن يتغيّر: الربح · المصروف · مال المالك
المبلغ بالدينار الأردني [10.00]
تاريخ الحدث [12/09/2026]
ما الذي حدث؟ (مطلوب) [أمانة جارة — أم رامي]
الجهة (اختياري) [أم رامي]
[حفظ الحدث] → /finance + "سُجّل الحدث — الكاش صار 155.00 د.أ · الأمانات 10.00 د.أ."
(amanah_released) "رصيد الأمانات بحوزتك الآن: 10.00 د.أ — لا يمكنك تسليم أكثر منه."
```

## 4.10 Cash screens: CashWallets · CashCount · CashDistribution

**CashWallets** (`/cash`) — Goal «وين الكاش عندي فعليًا؟»; header replaces jargon overline «استمرارية السجل» with «وين الكاش عندك؟»; wallet rows above the global history; totals chips include non-distributed with «وزّع» action; unknown opening wording unified to «رصيد الافتتاح غير محدد بعد — سجّله»; history capped at 8 → full ledger behind tap [NEW WalletLedger]; **[NEW] «عدّ الصندوق» primary button and unallocated strip** (moved entries).

```
[Screen: محافظ الكاش]
chips: كاش المحافظ 145.00 د.أ · غير الموزع 35.00 د.أ [وزّع → /cash/distribute]
"1 محفظة": [الدرج] "درج · 6 آثار · رصيد الافتتاح غير محدد بعد"  110.00 د.أ
             [سجّل رصيدًا موثقًا لاحقًا] [افتح كشف المحفظة → NEW WalletLedger]
        [حساب بنكي «الكِي»] "حساب بنكي · 4 آثار"  35.00 د.أ  [ضبط بسبب]
[عدّ الصندوق → /cash/count]  ← NEW primary (thumb zone)
[محفظة ورصيد بداية]  ·  [تحويل بين المحافظ] / "لاحقًا: أضف محفظة ثانية أولًا"
```

**CashCount** (`/cash/count`) — Goal «طابق الدرج مع السجل»; selected wallet's recorded balance visible as a card; live difference card with calm likely-cause wording; settle = today-only `cash_adjustment`; done screen closure; **[NEW] typed-count guard**.

```
[Screen: عدّ الصندوق]
"الدرج — المسجل: 150.00 د.أ"  (المحفظة التي تعدّها [الدرج ▾])
كم وجدت فعلًا؟ (د.أ) [155.00]
الفرق عن المسجل: +5.00 د.أ
  "غالبًا قبضات ما انسجّلت — رح تُسجَّل الفرق زيادة بتاريخ اليوم، وما رح يتغير أي رقم قديم."
[سجّل التسوية] → done: "انسجّلت التسوية — الصندوق صار 155.00 د.أ. ولا رقم قديم تغيّر."
```

**CashDistribution** (`/cash/distribute`) — Goal «قرار توزيع صريح»; available card top; plain direction labels; **[NEW] impact preview before submit**; success stays in place for repeat; supports `?mode=cover` (negative-unallocated resolution).

```
[Screen: وزّع الكاش غير الموزّع]
"الكاش غير الموزع المتاح: 35.00 د.أ — التوزيع ينقل بينهما ولا يغيّر الإجمالي."
الاتجاه: ● ادخل كاشًا إلى محفظة (من غير الموزّع) ○ غطِّ صرفًا خرج من محفظة
المحفظة [الدرج — الرصيد 110.00 د.أ]  المبلغ (د.أ) [20.00]  ملاحظة (اختياري)
معاينة: "الدرج: 110.00 → 130.00 د.أ · غير الموزع: 35.00 → 15.00 · الإجمالي 145.00 د.أ لا يتغير."
[سجّل التوزيع] → "انخصص الكاش — الإجمالي المسجل لم يتغير."
```

## 4.11 Parties · Setup · Foundation

**Parties** (`/parties`) — Goal «مين عليه إلَي، وعليّ لمين؟»; «لك» parties ordered before «عليك» when both exist; overdue badge «فات متابعته» (calm); search live ✅; read-only truth line stays; **[RETARGET] «حصّل من X» opens CollectionSheet** instead of the source editor.

```
[Screen: دفتر الناس]
chips: لك عند الناس 22.00 د.أ | عليك للناس 0.00 د.أ
ابحث بالاسم [خالد]
  خالد — لك 20.00 د.أ · 3 حركة [فات متابعته]   ▸
     ▸ expand: [حصّل من خالد ← CollectionSheet NEW] · دين طلب 15/08 · تحصيل طلب 01/09 · دين بيع مباشر 10/08
  سارة — لك 2.00 د.أ · 1 حركة ▸
"هذا الدفتر قراءة مجمّعة من سجلاتك الحالية — ما يُسجَّل منه شيء جديد."
```

**Setup** (`/setup`) — 3-step wizard; only the activity name is mandatory; setup draft persisted (U-003); skip-wallet path honest (F-002 ✅); **step 3 becomes three large radio cards** (replacing `<select>`, `Setup.tsx:288-311`).

```
[Screen: الإعداد — الخطوة 3/3]
"شو وضع الدرج هلق؟ — ثلاثة أجوبة صادقة."
 ○ أعرف الرقم        → كم في الدرج الآن؟ (د.أ) [150.00]
 ◐ ما بعرف الآن — يُحدَّد لاحقًا  ("ستبقى «غير محدد بعد» — لا تُعرض صفرًا أبدًا.")
 ● بدأت من الصفر       ("صفر موثق = بداية نظيفة معلنة.")
"كل ما تدخله هنا يُحفظ على هذا الجهاز فقط في هذا الإصدار."
[خطوة سابقة] [احفظ وافتح صفحة الأساس]
```

**Foundation** (`/foundation`) — Goal «شو عندك هلق؟»; cash + رأس مالك sections open; ديون/مواد collapsed; single primary exit «ادخل إلى مشروعي»; «تخطَّ وأكمل لاحقً» quiet text action (today two same-target buttons).

```
[Screen: صفحة الأساس]
"سجل ما تعرفه الآن فقط. ما تخطّاه يظهر لاحقًا كطريق، لا كصفر."
▸ الكاش (open): "لم تسجل محفظة بعد" [ابدأ من هنا → /cash/wallet/new]
▸ رأس مالك (open): "لم يسجل رأس مال بعد — اختياري بالكامل" [سجل استثمارًا نقديًا] [رصيد سابق لحق المالك]
▸ ديون قائمة (collapsed) · ▸ مواد متوفرة (collapsed)
"عندي ملف موقف جاهز → فتح الاستيراد" (→ /settings — NEW visible row)
[تخطَّ وأكمل لاحقًا (quiet)]  [ادخل إلى مشروعي]  ← single primary
```

## 4.12 NEW screens (proposed — none of these exists in code today)

### N1. ورقة التحصيل — CollectionSheet (NEW bottom sheet) — P0

**Why new:** collecting a debt today requires navigating to the source record (OrderDetail panel or DirectSaleEditor + X-06 dialog) — 3–4 taps from Home, and the Parties shortcut lands on a full editor. A transient sheet (≤3 fields) serves the dominant daily action «قبضت من خالد».

| Field | Value |
|---|---|
| Goal | «قبضت الآن من دين قائم — سجّله بلمسة» |
| Entry points | Home today «تحصيل مستحق»; Parties «حصّل من …»; FAB collection picker |
| Exit(s) | Receipt «تم» closes over standing screen; «افتح السجل المصدر» → source editor |
| Primary action | «سجّل القبض» |
| Source-of-truth owner | **None of its own** — calls the same services the source records use (fulfillment.collectDebt / directSales collection update); keeps partyLedger read-only purity |
| Acceptance criteria | 1) Amount prefilled with المتبقي; over-collection blocked by guard. 2) محفظة القبض defaults «الدرج». 3) Receipt closure with numbers. 4) Everything else optional |

```
[Sheet: حصّل من خالد]
من دين: طلب صندوق خشبي (15/08) — المتبقي 20.00 د.أ
قبضت الآن (د.أ) [20.00]     ← prefilled
محفظة القبض: ● الدرج
ملاحظة (اختيارية) [ — ]
[سجّل القبض]
Receipt: "تم تسجيل التحصيل — الكاش زاد 20.00 د.أ — المتبقي على خالد 0 د.أ"
          [افتح السجل المصدر] [تم]
```
States: empty amount → guard «أدخل المبلغ بالأرقام 0–9»; saving; error; unsaved confirm on close; correction → «افتح السجل المصدر» (explicit flow with preview).

### N2. كشف الأسبوع — StatementView (NEW full screen `/statement`) — P1

**Why new:** the owner question «كيف كان أسبوعي؟» has no single screen: period result hides inside a collapsed Finance layer; cash movement is scattered. A plain statement full-screen assembles existing read models only (no new stores).

| Field | Value |
|---|---|
| Goal | «شو صار هالأسبوع؟» — one honest page |
| Entry points | Home «عرض تفاصيل الأسبوع»; Finance period layer «كشف بسيط» |
| Exit(s) | Back to origin; row taps → source records |
| Primary action | None (reading); period switcher |
| Source-of-truth owner | Read model: projectFinance period/insights + events + position |
| Acceptance criteria | 1) Six plain lines max on first paint. 2) Every number carries its honesty qualifier («مسجل», «تقديري», «غير متاح»). 3) Amanah + unknowns declared. 4) Cash start/end reconciles to position |

```
[Screen: كشف الأسبوع — 6 إلى 12 أيلول  (◀ ▶)]
بعت (محتسب عند التسليم):        105.00 د.أ  (3 طلبات + 5 بيع مباشر)
قبضت فعليًا:                    85.00 د.أ
صرفت:                           22.50 د.أ  (مصروف 5 · مشتريات 1)
نتيجة الفترة المسجلة:           27.50 د.أ  (تقديرية — تكلفة بيعين غير معروفة)
الكاش: بداية الأسبوع 110.00 د.أ → نهايته 145.00 د.أ
أمانات بحوزتك: 10.00 د.أ — كاش في الدرج، ليست لك ولا ربحًا.
ديون جديدة عليّ للناس: +12.00 · حصّلت من ديون قائمة: 20.00
(«غير متاح» بدل أي رقم مجهول · كل سطر [tap → مصدره])
Offline: "قراءة محلية من هذا الجهاز — آخر تصدير 12/09/2026"
```

### N3. معاينة الأثر — CorrectionPreview (NEW shared dialog contract) — P1

**Why new:** impact previews exist ad-hoc (EventsLayer before/after dl, cash reversal preview, cancel-panel text) but no single contract guarantees «ما سيتغير / ما لن يتغيّر» before *every* edit/delete/reverse. This is a pattern applied by EventsLayer edit/delete, cash reversal, inventory reversal, supplier corrections [NEW], direct-sale cancel.

| Field | Value |
|---|---|
| Goal | «قبل التصحيح — شوف شو بيتغير وشو لا» |
| Entry points | Any «تراجع / تصحيح / حذف» action on a financial record |
| Exit(s) | «تراجع موثق» / «حفظ التصحيح» → receipt; «إلغاء» returns |
| Primary action | The destructive confirm, disabled until the reason rule passes |
| Acceptance criteria | 1) Two non-empty lists: ما سيتغير / ما لن يتغيّر. 2) Reason optional by default («تعديل موثق»), required for delete-type corrections. 3) Receipt with numbers + «الأصل محفوظ في السجل». 4) Never color-alone: icons + labels |

```
[Dialog: قبل التصحيح — بيع مباشر «كيكة شوكولا»]
ما سيتغير:  الربح المعروض لهذا البيع · الباقي على خالد (20.00 → 2.00 د.أ)
ما لن يتغيّر: الكاش المسجل · الأصل في السجل · طلبات أخرى
سبب التصحيح (اختياري): [خصم متفق]
[إلغاء]  [احفظ التصحيح] → "انسجّل التصحيح — الأصل محفوظ · الباقي على خالد 2.00 د.أ"
```

### N4. كشف المحفظة — WalletLedger (NEW `/cash/wallet/:id`) — P1

**Why new:** CashWallets caps history at 8 global entries (`CashWallets.tsx:217-221`); «شو صار بدرجي؟» needs a full per-wallet ledger. Pure navigation-stack read screen.

```
[Screen: الدرج — كشف المحفظة]
الرصيد الآن: 110.00 د.أ · رصيد الافتتاح: غير محدد بعد [سجّل رصيدًا موثقًا]
12 أيلول: تخصيص من غير الموزع +20.00 · قبض بيع (تصحيح؟) +3.00
11 أيلول: ضبط كاش (عدّ الصندوق) +5.00 · تحويل صادر −10.00 …
[عدّ الصندوق] · كل صف: [تراجع → CorrectionPreview]
```

### N5. صفحة شخص — PartyDetail (NEW `/parties/:name`, optional P2)

Replaces the accordion for names with many movements: balance header (لك/عليك), «حصّل من …» CollectionSheet shortcut, movement list → source records. Keeps the Parties list to one-line rows. Optional: the accordion is acceptable for ≤3 movements.

### N6. تصحيح السعر المتفق — OrderPriceEditor (NEW `/orders/:id/price`) — P0 deep editor (MC-02)

**Contract:** Goal «صحّح السعر المتفق بعد الاتفاق دون إلغاء الطلب» · Entry: OrderDetail quiet action · Exit: receipt → OrderDetail · Primary: «احفظ السعر المصحّح» · Owner: agreements (documented revision in the order event log — mirrors direct-sales `price_cut`) · Acceptance: ① protection-price comparison shown ② receivable delta preview before confirm ③ deposit truth explicitly unchanged ④ revision preserved in event log.

```
[Screen: صحّح السعر المتفق — صندوق خشبي]
السعر المتفق الحالي: 35.00 د.أ · سعر الحماية المرجعي: 17.50 د.أ للقطعة (تقديرية)
السعر الجديد (د.أ) [40.00]
معاينة (CorrectionPreview):
  ما سيتغير:  المتبقي على سارة (20.00 → 25.00 د.أ) · نتيجة الطلب عند الحساب
  ما لن يتغيّر: العربون المحصل 15.00 د.أ · الكاش المسجل · التسليمات والسجل القديم
سبب التصحيح (اختياري): [الزبون زاد الطلب]
[إلغاء]  [احفظ السعر المصحّح] → "انسجّل السعر الجديد 40.00 — الأصل محفوظ · المتبقي على سارة 25.00 د.أ"
```

### N7. صحّح الشراء — PurchaseCorrectionEditor (NEW `/suppliers/purchase/:id/edit`) — P0 deep editor (MC-01)

**Contract:** Goal «صحّح شراءً مسجلًا مع معاينة أثره على المتبقي» · Entry: purchase detail quiet action · Exit: receipt → purchase detail · Primary: «احفظ التصحيح» · Owner: supplierPurchases (correction APIs to be added at the service layer) · Acceptance: ① payables delta preview before confirm ② payments untouched unless corrected separately ③ documented revision (original preserved) ④ payment reversal via `/payment/:paymentId/reverse` uses the same CorrectionPreview contract.

```
[Screen: صحّح الشراء — شراء مواد من أبو خالد]
الإجمالي الحالي: 120.00 د.أ · المدفوع: 30.00 · المتبقي: 90.00 د.أ
الإجمالي الصحيح (د.أ) [110.00]
معاينة (CorrectionPreview):
  ما سيتغير:  المتبقي لأبي خالد (90.00 → 80.00 د.أ) · «عليّ للموردين»
  ما لن يتغيّر: الدفعات المسجلة (30.00 د.أ) · الكاش المسجل · السجل الأصلي
سبب التصحيح (اختياري): [غلط كتابة في الفاتورة]
[إلغاء]  [احفظ التصحيح] → "انسجّل التصحيح — الأصل محفوظ · المتبقي لأبي خالد 80.00 د.أ"
```

## 4.13 Density & order critique (current → target, the five destinations)

*Note on self-containment:* the full Output-B hierarchy-and-wireframe set for the six secondary screens (Schedule, Suppliers, Settings, OwnerEntitlement, Inventory, Catalog) — with screen contracts and states — exists in the working artifact `03-screen-contracts-wireframes.md` (§1.18–§1.22 there); their Output A rows in §3.4 carry the placement decisions. The wireframes above cover the five destinations, the core flow screens, and all NEW screens including both P0 editors (N6/N7).

**مشروعي الآن (Home).** Current order: heading → away card → truth line → «اليوم» → 4 fact cards → «مالي» unit with **primary** button → «منتجاتي وخدماتي» unit with **primary** button → optional modules → recent changes (5) → scope line. Target: the two in-page primary units demote to one quiet links row (tabs already carry them); optional modules merge into the links row; recent changes trim to 3 + «عرض السجل»; scope line «فتح مالي» is removed (duplicates the tab) and replaced by the locality/offline line. Scroll ownership (360×640): heading + away/truth (conditional) + first 2–3 today rows + start of facts; FAB always visible.

**العمل (Orders).** Current: «مبيعاتي» always first; DecisionPanel second and hidden when no orders; sale rows 6–9 `<small>` lines; canned «الخطوة التالية: راجع أو صحح البيع عند الحاجة» noise. Target: DecisionPanel first and always rendered (quiet when nothing due); sale rows ≤3 lines; canned next-step removed; empty state gains a «سجّل أول بيع» CTA; مواعيد preview trims to 3 rows. JOD fixes: «دين مسجل (د.أ): 20.00» → «الدين: 20.00 د.أ»; raw `(revenueMinor/100).toFixed(2)` renders → MoneyValue.

**مالي (Finance).** Current ~13 top-level blocks; ReviewPulse (reading) first; CashDecision second; OwnerDecision card with primary; dense «ما نعرفه الآن» text block; back-to-Home button. Target: back button removed; CashDecision + unallocated strip first; position cards 2×2; Amanah chip when > 0; ReviewPulse demotes into «صورة الطلبات» layer; OwnerDecision demotes to a tappable position card; «ما نعرفه الآن» defers to a «تفاصيل الأرقام» layer; the 10 action buttons group by intent. Wording: «أعلن تحصيلًا أو التزامًا قريبًا» → «سجّل قبضًا أو دفعًا متوقعًا» (glossary violation, `Finance.tsx:1025`); «الصورة العامة · المبالغ (د.أ)» → «قراءة مالية مسجلة».

**أدواتي (Tools).** Current: rule card + result disclaimer duplicated; result card sits after all inputs (off-screen while typing); save button primary weight. Target: one rule line; **sticky live result bar** in the thumb zone; materials row compressed (name + unit price prominent, quantity/unit compact); save demoted to secondary. Unsaved calculator input gets a soft guard.

**Key before→after wording upgrades (selected):**

| Before (code) | After (target) | Reason |
|---|---|---|
| QuickActionSheet default «بلا نسبة الآن — كاش غير موزع» | default «الدرج» + explicit «اتركه غير موزّع» option | fast path needs a destination; current default manufactures the backlog |
| Home service actionLabel «افتح» (all 9 today kinds) | action-specific «حصّل / سلّم / أكمل / راجع» | actionable wording |
| Orders.tsx:120 «الفرق دَين على العميل — يظهر في «لي عند العملاء».» | «الباقي 2.00 د.أ دَين على خالد — حصّله من دفتر الناس» | plain + name + action |
| CashWallets.tsx:89 «استمرارية السجل» | «وين الكاش عندك؟» | jargon → owner language |
| CashWallets.tsx:180 «رصيد الافتتاح غير معروف» | «رصيد الافتتاح غير محدد بعد — سجّله» | mandated unknown wording + road |
| DirectSaleEditor.tsx:507 «الفرق 2.00 دينار» | «الفرق 2.00 د.أ» | unit consistency |
| Finance.tsx:1025 «أعلن تحصيلًا أو التزامًا قريبًا» | «سجّل قبضًا أو دفعًا متوقعًا» | glossary binds «متوقع» |

## 4.14 State coverage matrix (12 states × major screens)

Legend: ✅ handled (code evidence) · ⚠️ partial · ❌ missing · — n/a.

| Screen | empty | loading | saving | success | error | offline | unknown | partial | unsaved | cancel | back | correction |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Home | ✅ | ✅ | — | — | ✅ | ❌ | ✅ facts | ⚠️ away only | — | — | — | — |
| Orders | ✅ + inline | ✅ | — | — | ✅ | ❌ | ⚠️ profit only | ✅ | — | — | ✅ | ✅ via editors |
| OrderDetail | — | ✅ | ✅ | ⚠️ full-collection note only; ❌ collect closure | ✅ | ❌ | ✅ result «—» | ✅ | — | ✅ | ✅ | ✅ cancel documented |
| Finance | ✅ wallet road | ✅ | — | — | ✅ | ❌ | ✅ «غير متاح» | ✅ exclusions | ⚠️ | — | ✅ (remove) | ✅ CorrectionsLayer |
| Tools | ✅ | ⚠️ | ✅ | ✅ | ✅ | — | ✅ «—» | ✅ | ❌ calculator lost | ⚠️ | ✅ | ✅ free delete |
| QuickActionSheet | — | — | ✅ | ⚠️ receipt total; ❌ remaining/undo | ✅ | — | ✅ cost option | ✅ | ❌ close wipes input | ✅ | ✅ | ✅ via editors |
| DraftEditor | — | ✅ | ✅ | ✅ | ✅ conflict | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ snapshots |
| CostEditor | ✅ inline | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ versions |
| AgreementEditor | — | ✅ | ✅ | ⚠️ navigates only | ✅ | — | ✅ | ✅ | ✅ | — | ✅ | ✅ |
| DirectSaleEditor | — | ✅ | ✅ | ⚠️ navigates only | ✅ conflict | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ revisions |
| FinancialEventEditor | — | ⚠️ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | — | ✅ | ✅ |
| CashWallets | ✅ | ✅ | — | — | ✅ | ❌ | ✅ D-004 | ✅ | — | — | ✅ | ✅ reverse |
| CashCount | ✅ | ✅ | ✅ | ✅ done | ✅ | — | — | ✅ | ❌ counted lost | ⚠️ | ✅ | ✅ future-only |
| CashDistribution | ✅ | ✅ | ✅ | ✅ inline | ✅ guards | — | — | — | ❌ | — | ✅ | ✅ allocation reversal |
| Parties | ✅ + no-result | ✅ | — | — | ✅ | ❌ | — | ⚠️ | — | — | ✅ | ✅ read-only note |
| Setup | — | — | ✅ | ✅ → Foundation | ✅ | — | ✅ | — | ✅ draft | ✅ | ✅ | — |
| Schedule | ✅ | ✅ | — | — | ✅ | ❌ | ✅ | ✅ | ❌ capacity | — | ✅ | ✅ postpone |
| Settings | — | ⚠️ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ | — | ✅ | ✅ | ✅ reset gate |

**Missing states → target wording (priority order):**
1. **Success closure after money actions** (OrderDetail collect, DirectSale save, Agreement create): «تم تسجيل التحصيل — الكاش زاد 20.00 د.أ — المتبقي على خالد 0 د.أ» / «انسجّل التصحيح — الأصل محفوظ».
2. **Offline/locality** (Home, Finance, Orders, Parties, CashWallets): «شغال بدون إنترنت — بياناتك محفوظة على هذا الجهاز» (only when offline) + staleness «آخر نسخة مصدّرة: 12/09/2026».
3. **Unsaved in transient surfaces**: sheet close with typed amount → «في رقم مكتوب — تسجّله أو تتجاهله؟»; CashCount back with counted value; Tools calculator navigation.
4. **Tools loading** for estimates list: «جارٍ قراءة تقديراتك…» skeleton row.
5. **Empty upgrades**: Orders global empty gets a CTA; Home today-empty stays honest («يومك مفتوح»).
6. **Unknown wallet opening unified wording**: «رصيد الافتتاح غير محدد بعد» everywhere — never «غير معروف» or bare «—» on a balance.

---

# 5. OUTPUT C — Core Task Flows

Each step shows: **[screen] → user action → system response → destination → data state → safe return**. Happy path plus the important failure, cancellation, empty, unknown, offline, and correction paths. Offline note applies globally: all writes are local (idempotency-keyed) and succeed identically without a connection; the offline banner appears when `navigator.onLine === false` and never blocks a write.

## 5.1 Mandatory Flow 1 — Product-to-Sale

### 5.1a With an existing product (catalog reference)

1. **[Home]** → tap **سجّل** (FAB) → QuickActionSheet opens → no data yet.
2. **[QuickActionSheet]** → tap **تسجيل بيع** → in-sheet sale form: المبلغ first, keypad, «سجّل البيع» directly beneath; «خيارات أكثر» disclosure.
3. **[Sale form]** → open **خيارات أكثر** → tap **ما الذي بعته؟** → the field now offers **catalog suggestions** (P-002 pattern extended to the sheet [NEW]) — typing «كيكة» shows «كيكة شوكولة — السعر المقترح 10.00 د.أ، التكلفة: معروفة تقديريًا». Tap a suggestion → name + suggested price fill as **editable suggestions, never enforced**. If the owner ignores suggestions entirely, nothing blocks the save.
4. **[Sale form]** → enter actual amount **10.00** (editable — the recorded price is always the actual price; catalog price is a starting point only) → quantity is documentation-only and deferred to «تفاصيل أكثر» in the full editor → choose **محفظة القبض: الدرج** (default).
5. **[Sale form]** → tap **سجّل البيع** → write `directSales.record` + wallet `allocation` (idempotency keys) → **receipt replaces the form**: «سُجّل بيع 10.00 د.أ — الكاش زاد 10.00 وصار 155.00 د.أ» + **[افتح السجل]** + **[تراجع]** + **[تم]** → data saved atomically; nothing else changes; no navigation.
6. **[Receipt]** → tap **افتح السجل** → `/direct-sales/:id` correction editor (revisions, X-06 difference, cancel zone) → guarded back → returns to the list/origin. **Or** tap **تم** → sheet closes over Home. **Safe return everywhere.**

Failure paths: empty amount → inline «أدخل مبلغ البيع بالأرقام 0–9» (no dialog); amount typed then sheet closed → NEW discard confirm «في رقم مكتوب — تسجّله أو تتجاهله؟»; credit case → «آجل» discloses اسم الزبون + المحصل الآن; if collected < total, the sheet records `partial_debt` and the receipt states «الباقي 2.00 د.أ دَين على خالد — حصّله من دفتر الناس». Cost unknown → the sheet offers «لا أعرف الآن» and the profit reads «غير متاح» — never zero.

### 5.1b Full editor path (rare detail / correction)

1. **[Orders]** → **مبيعاتي** section → [NEW] **«تسجيل بيع مباشر»** CTA → `/direct-sales/new` → guarded editor.
2. **[DirectSaleEditor]** → field order: الاسم → السعر المتفق → ما قبضت الآن → «تفاصيل أكثر» (الكمية، التكلفة، رابط مرجع مع اقتراحات P-002، التاريخ، بيان). Reference suggestions declared + editable; copy explains «عدّله ليصير السعر الفعلي لهذا البيع»; quantity is honest documentation and price is the **total** (qty > 1 → no auto-fill; copy says «اضرب بنفسك وأدخل الإجمالي الفعلي»).
3. **[DirectSaleEditor]** → save → if collected < agreed → **X-06 difference panel**: «اتفقيتَ على 10.00 وقبضتَ 8.00 — الفرق 2.00 د.أ. اختر ما حدث فعلًا: خفّضتُ السعر / الباقي عليه / يحتاج مراجعة» → confirm → navigate to `/orders` + closure sentence «انسجّل التصحيح — الباقي على خالد صار 2.00 د.أ».
4. No inventory is forced anywhere: catalog is an optional module; nothing blocks a save for lack of stock/product. **[Catalog]** → [NEW] reference row action **«سجّل بيع هذا المنتج»** → `/direct-sales/new?item=:id` with the reference preselected (product knowledge travels to the sale).

Cancellation: back with typed input → 3-choice drawer (ابقَ / احفظ ثم اخرج / اخرج بلا حفظ). Correction: from the Orders row or receipt → editor with revision history; originals preserved.

### 5.1c The order path (product made to order)

Draft (وصف + زبون + كمية، lazy materialization — no record until first real input) → **احسب التكلفة** → CostEditor (snapshot; incomplete allowed as declared «ناقصة»; never type zero for unknown) → **تسجيل الاتفاق** (suggested = protection price; below-floor acknowledgment; optional deposit recorded as cash linked to the order, not profit) → OrderDetail (sticky contextual CTA drives the cycle: ابدأ التنفيذ → جاهز للتسليم → تم التسليم → تحصيل المتبقي/تسجيله دينًا) → collection closes the loop with the closure sentence. At any pre-delivery point: cancel with reason + 3-way deposit settlement (refund / keep / needs_review — a valid resting state). Post-agreement price change: [NEW] `/orders/:id/price` documented revision (see §5.5).

## 5.2 Mandatory Flow 2 — مشروعي الآن (alerts open their source in one tap)

1. **[Home]** morning open → Header orients (name + date). Body 1 «اليوم» shows at most 5 rows with **action-specific labels**:
   - «تسليم غدًا — صندوق خشبي · سارة» [سلّم] → tap → **OrderDetail** scrolled to the step card.
   - «تحصيل مستحق — خالد · 20.00 د.أ» [حصّل] → tap → **CollectionSheet** (N1) prefilled from the order debt [NEW deep link `/orders/:id?focus=collect` opens OrderDetail with the collect panel open + المتبقي prefilled when the sheet route is not wanted].
   - «أكمل تكلفة — طلب ريم» [أكمل] → tap → **OrderDetail/DraftEditor** at the cost step.
   - capacity warning → `/schedule?layer=capacity` [NEW].
   - [NEW] direct-sale debts also appear as `due_amount` rows (today order-only) — MC-22.
2. Each row is one tap to the **source document, never a generic list**. Back returns to Home (referrer-aware; BottomNav always present).
3. Fact chips (2×2) answer «what is recorded»: cash (with [NEW] Amanah qualifier «منها أمانات 10.00 د.أ» + unallocated line when ≠ 0), receivables (road → `/parties`), payables (road → payable editor), owner capital (road → investment). Unknown → «—» + «سجّله» road; never 0.00.
4. Away card (≥7 idle days): last-recorded-day digest (honest — nothing changes during absence), overdue debts → `/parties?focus=overdue`, backup age → `/settings?focus=export`, quiet «ابدأ من اليوم — التاريخ ما بيفرق» → FAB sheet. **No shaming, no backlog language, no red counters.**
5. «ما تغير مؤخرًا» rows → source records; «عرض السجل» → `/finance?layer=events` [NEW deep link].

Empty: «لا متابعات اليوم — يومك مفتوح. سجّل أول شي يصير.» Error: retry block. Offline: locality line only when actually offline or export stale.

## 5.3 Mandatory Flow 3 — مالي (cash, Amanah, debts, position, period result — separated and explained)

1. **[Finance]** open → decision first: **قرار الكاش** (recorded cash now, قبض متوقع, دفع متوقع, expected cash; status + الخطوة التالية; primary **«سجّل قبضًا أو دفعًا متوقعًا»** — renamed from «أعلن…»).
2. **Unallocated strip** (when > 0): «كاش غير موزع: 35.00 د.أ — وزّعه على محفظة الآن، أو اتركه حتى تعرف وجهته» → `/cash/distribute`. When **negative**: the alert button re-points [NEW] to `/cash/distribute?mode=cover` — the documented `cover_payment` resolution (today unreachable).
3. **الوضع المسجل 2×2**: الكاش المسجل (declared wallets + unallocated) → `/cash`; لي عند العملاء (registered post-delivery debt) → `/parties`; عليّ للموردين → `/suppliers`; مال المالك المسجل → `/finance/owner-entitlement`. Each card's number is a **registered** fact with its qualifier; unknowns read «غير متاح», never 0.00.
4. **Amanah line (when > 0)**: «أمانات بحوزتك 10.00 د.أ — كاش حقيقي في الدرج لكنه ليس لك ولا يدخل الربح.» Both truths at once: physically present (counts in cash) / not owned (excluded from profit, result, owner equity). Actions: «سجل أمانة سُلّمت» appears when held > 0.
5. Layers (on-demand): «قراءة الفترة» (registered period result with statuses, COGS sources, exclusions, insights) → [NEW] «كشف بسيط» → `/statement`; «صورة الطلبات» (ReviewPulse demoted here); «التغطية والتعادل» (G5); «سجّل حركة أو افتح مصدر» (grouped write buttons); عربونات; السجل (`?event=` focus) with inline corrections; تصحيحاتي الموثقة.
6. **/statement [NEW]** answers «كيف كان أسبوعي؟» in six honest lines (بعت / قبضت فعليًا / صرفت / نتيجة with qualifier / كاش بداية→نهاية / أمانات dual-truth), every row tappable to its source.

Financial-truth guarantees in this flow: collection ≠ profit (receipts separate from result); debt ≠ cash (receivable card is not cash); Amanah ≠ profit (dual-truth line + DELTA_TABLE isolation); owner money ≠ revenue; unknown ≠ zero («غير متاح» + road). Period result carries its honesty qualifiers («تقديرية — تكلفة بيعين غير معروفة»); exclusions list links to the excluded orders.

## 5.4 Mandatory Flow 4 — أدواتي / Cost Calculator (estimate freely, zero commitment)

1. **[Tools]** tab 4 → «احسب قبل أن تلتزم». One rule line: «هذا حساب تقديري. ما انحفظت أي حركة مالية ولا مخزون.» No order, no product, no inventory, no sale is required or created — the calculator is fully independent.
2. Type freely: عنوان التقدير (optional), مواد rows (name + unit price prominent, quantity/unit compact), وقت العمل toggle, عدد القطع, «بنود أخرى وحماية السعر» (packaging/delivery/waste/margin) behind a disclosure.
3. **Sticky live result bar** [NEW]: «سعر الحماية: 12.50 د.أ للقطعة» + knowledge chip, always visible while typing; expand for تكلفة القطعة/الإجمالي. Incomplete knowledge → «—» + reason — never a number, never zero.
4. **احفظ التقدير** (secondary weight) → stored in `cost-estimates` (schema 29) with **zero effect** on cash, balances, inventory, orders — always tagged «تقديري». In-place message: «حُفظ التقدير للمراجعة لاحقًا — لم تُنشأ أي حركة مالية أو مخزون.» Deleting an estimate is free (a thinking tool, not a financial record).
5. **LATER — reuse**: **[Tools]** «تقديراتي المحفوظة» → row actions: [NEW] **«افتح التقدير»** → `/tools/estimates/:id` edit mode (service `update()` exists unused; today delete + re-enter is the only correction) → **«ابدأ مسودة من هذا التقدير»** → `/orders/draft/new?intent=planned_design&estimate=:id` → DraftEditor prefilled **once** with a proposal notice: «بدأت هذه المسودة من تقديرك — القيم مقترحات قابلة للتعديل» → the conversion is an explicit owner decision, and the estimate survives (its numbers are copied as editable suggestions).
6. Safe return: leaving with typed calculator input → [NEW] soft guard «الرقم غير محفوظ — احفظه تقديرًا أو تجاهله» (today typed input is silently lost).

## 5.5 Mandatory Flow 5 — Safe correction (edit, delete, reverse, restore — with impact preview and safe return)

**Principle (already the engine's discipline; the target extends it universally):** every correction = **preview → confirm → documented receipt**; originals preserved; never a silent delete; never a between-state. Undo on a receipt routes through the same explicit flow.

1. **From any record list** (Finance السجل `?event=` focus, Orders مبيعاتي row, wallet ledger row [NEW], purchase detail [NEW]) → tap «تراجع / تصحيح».
2. **[CorrectionPreview dialog — NEW shared contract]** → two non-empty lists:
   - «ما سيتغير»: e.g. الباقي على خالد (20.00 → 2.00 د.أ)، الربح المعروض لهذا البيع.
   - «ما لن يتغيّر»: الكاش المسجل، الأصل في السجل، طلبات أخرى.
   - Reason: optional for edits («تعديل موثق» default), required for delete-type corrections. Confirm disabled until the rule passes. Icons + labels (never color alone).
3. **Confirm** → atomic write (financial events: `commitFinancialEventReplacement` = reverse + replacement in one IndexedDB transaction; direct sales: revisions + conflict guard; cash: documented reversal; inventory: documented reversal) → receipt: «انسجّل التصحيح — الأصل محفوظ · الباقي على خالد 2.00 د.أ».
4. **Safe return** to the list that launched the correction; conflict (another edit landed first) → reload preserving typed input.

Family coverage today vs target: events ✅ (reverse/atomic edit/documented delete/restore with before→after dl); direct sales ✅ (revisions, conflict guard, price_cut, cancel); cash entries ✅ (reversal with preview); inventory ✅ (reversal). **Missing → target adds:** supplier purchases/payments (`/suppliers/purchase/:id/edit` + `/payment/:pid/reverse` — MC-01 P0); post-agreement order prices (`/orders/:id/price` with receivable delta preview, deposits untouched — MC-02 P0); the CorrectionPreview contract itself applied uniformly (MC-08 P1).

Special cases: wrong wallet attribution → allocation reversal via `/cash/distribute` (documented); counting mistake → a new count (adjustments are future-only — historical numbers never change); order price after agreement → documented revision in the event log (mirrors direct-sales `price_cut`); cancel with deposit → 3-way settlement, «needs_review» is a valid resting state until resolved.

## 5.6 Onboarding flow (first opening → first useful result)

1. Boot → StartupGate (no profile → `/setup`; storage failure → recovery screen with reload CTA; `/setup` & `/settings` are public recovery routes).
2. **[Setup]** — only the activity name is mandatory. «وين تحط فلوسك؟» → default wallet «الدرج» (skippable — skipping skips the question entirely, F-002 fixed; no question is ever asked and then ignored). «شو وضع الدرج هلق؟» → **three radio cards** [NEW]: أعرف الرقم (amount) / «ما بعرف الآن» (stays «غير محدد بعد», never 0.00, road appears later on `/cash`) / بدأت من الصفر (documented zero). Setup draft persists in localStorage with restore notice; interrupted setup resumes.
3. **[Foundation]** «شو عندك هلق؟» — optional: cash, رأس مالك, ديون, مواد; [NEW] visible «عندي ملف موقف جاهز» import row (today the guided import hides in a collapsed Settings layer). «تخطَّ وأكمل لاحقً» quiet; **ادخل إلى مشروعي** single primary → `/`.
4. **First useful action ≤60s from Home**: FAB → تسجيل بيع → amount → receipt. The owner has value on the device before understanding anything else. Truth line at the door: «كل ما تدخله هنا يُحفظ على هذا الجهاز فقط في هذا الإصدار.»

Skipped items surface later as roads (Home facts «سجّله» / `/cash` unknown opening) — never as zeros.

## 5.7 Supporting flows (condensed, integrated with Outputs A–B)

- **Quick expense**: FAB → sheet → المبلغ + optional بند + محفظة الصرف default «الدرج» → receipt with cash delta. Classification (relationship/behavior/purpose/knowledge, shared fixed/%/estimate/defer) lives behind the full editor's drawer — depth when wanted, never in the fast path.
- **Debt collection**: three doors → CollectionSheet (N1): Home due row, Parties «حصّل من X», FAB picker. Amount prefilled = المتبقي; over-collection blocked; wallet default «الدرج»; receipt closure «تم تسجيل التحصيل — الكاش زاد 20.00 د.أ — المتبقي على خالد 0 د.أ» + «افتح السجل المصدر». The sheet owns no data (same service writes as the source records).
- **Cash counting (قفل اليوم)**: `/cash` [NEW primary button] → `/cash/count` → wallet card shows recorded balance → counted amount → live difference with calm cause explanation → «سجّل التسوية» → today-only `cash_adjustment` → done screen closure → `/cash`. Historical numbers never change; a counting mistake is corrected by a new count.
- **Amanah held/released**: Finance actions → FinancialEventEditor → «ما سيتغير/ما لن يتغيّر» pair → save → closure with the new held balance. Release ≤ held balance (guard).
- **Orders cycle & schedule**: as §5.1c; schedule rows deep-link; recurrence/capacity [NEW] visible section; postpone-1-day quick action.
- **Export/backup habit**: Settings → verified export (full re-parse before readiness; `lastVerifiedExportAt` recorded) → truthful local privacy line with staleness; Home truth line + away card nudge at 7 days. Reset: mandatory verified export → typed «ابدأ من جديد» → atomic `resetAll` → `/setup`; any failure halts everything.
- **Import/restore**: preview (file date + contents + what will be replaced) → atomic replace → summary. Guided opening import [NEW visible row in Foundation + Settings].
- **Return after absence**: §5.2 step 4 — honest digest of the last recorded day; no invented history; guilt-free continuation.
- **Offline recovery**: offline banner when offline; all writes local and identical; boot storage failures → dedicated recovery screen (4 codes); 404 boundary → «العودة إلى مشروعي الآن».

## 5.8 Target user journey (staged narrative)

**Stage 0 — first opening (≤3 min):** Setup (name only mandatory → default wallet → honest opening position) → Foundation (optional) → Home.
**Stage 1 — first useful action (≤60 s):** FAB → تسجيل بيع → amount → receipt with cash total.
**Stage 2 — daily rhythm:** morning Home review (today list, one tap to sources) → recording bursts through the FAB sheet (sale/expense/collection, ≤2 mandatory inputs, receipts never navigate) → closing: `/cash` → عدّ الصندوق → done → optionally `/statement`.
**Stage 3 — weekly review:** Home «عرض تفاصيل الأسبوع» → `/statement` six honest lines → rows to sources → `/parties?focus=overdue` follow-ups.
**Stage 4 — return after absence (guilt-free):** away card digest → overdue debts → backup age → «ابدأ من اليوم».
**Stage 5 — correction/recovery:** any record → CorrectionPreview → documented receipt (§5.5).
**Stage 6 — backup habit:** verified export; staleness lines on Home/Settings; reset gated.

---

# 6. OUTPUT D — Missing Capabilities Required for a Complete Target Experience

> **Status convention:** every row below is a **PROPOSAL for an absent capability**. Nothing in this register is described as existing; each "why the current system fails" column was verified against the code on `main` @ `1b37c77` before the row was admitted. Priorities: **P0** = blocks task completion / financial trust / recovery · **P1** = significant friction or trust risk · **P2** = discoverability / polish. "Now" = current prototype scope; "Later" = post-prototype (deferred families per E-00.14).
>
> **Scenario key** (each register row is grounded in one of these walkthroughs; the flows in §5 cover them all): **A** — first opening / onboarding (§5.6) · **B** — daily review from «مشروعي الآن» (§5.2) · **C** — product to sale (§5.1) · **D** — cost before sale (§5.4) · **E** — cash, debt, Amanah (§5.3) · **F** — correction after a mistake (§5.5) · **G** — return after absence (§5.2 step 4) · **H** — empty states and offline (§4.1/§4.14).

| ID | Missing item | Type | Scenario | Why current system fails (code-verified) | Target solution (screen + behavior) | Target owner screen | Entry point | Result & next step | Priority | Now/later | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MC-01 | Supplier purchase & payment correction (edit / reverse / documented delete) + purchase detail view | feature + recovery path + screen | F | `SupplierPurchaseService` exposes only `recordPurchase/recordPayment/list/readSummary` — no reversal/edit/delete API; `/suppliers/purchase/:id` renders the *payment form* for any id (no purchase detail screen) | [NEW] `/suppliers/purchase/:id` detail (story, payments, remaining) + [NEW] `/edit` correction with payables impact preview + [NEW] `/payment/:paymentId/reverse` documented reversal | Suppliers hub | purchase row | «انسجّل التصحيح — الأصل محفوظ» receipt → back to Suppliers | **P0** | Now | High |
| MC-02 | Post-agreement order price revision | feature + screen | F | `AgreementService` = `list/get/createFromDraft/startExecution` only; price change = cancel whole order (3-way deposit settlement) + restart; direct sales have `price_cut`, orders have nothing | [NEW] `/orders/:id/price`: old→new price, receivable delta preview («ما سيتغير/ما لن يتغيّر»), reason optional; documented revision in the order event log; deposits untouched | OrderDetail | «صحّح السعر المتفق» (quiet action) | Receipt with new receivable → OrderDetail | **P0** | Now | High |
| MC-03 | Lightweight collection sheet + FAB collection picker | screen + action | B, E | Debt collection for direct sales = full `DirectSaleEditor` + X-06 3-way dialog (Parties «حصّل من» lands there); FAB «عربون أو تحصيل» navigates to plain `/orders` with no filter | [NEW] transient CollectionSheet over the source record (amount prefilled, wallet default «الدرج», optional note; writes through existing services — owns no data); FAB item becomes a 2nd-level receivable picker | Parties / Home / QuickActionSheet | Parties «حصّل من {name}»; Home due row; FAB | Receipt «تم تسجيل التحصيل — الكاش زاد X — المتبقي على {name} Y» closes over standing screen | **P0** | Now | High |
| MC-04 | Negative-unallocated resolution path (`cover_payment` reachability) | state + deep-link + recovery | B, E, F | Finance strip renders only when `unallocated > 0`; when negative, the alert's button → `/cash` (review only); `cover_payment` direction reachable only by typing the URL | Retarget alert → `/cash/distribute?mode=cover` preselecting «غطِّ صرفًا خرج من محفظة»; param parsed on cold start | Finance CashDecisionSurface | negative-unallocated alert | Distribution in cover mode → record → back to `/cash` | **P0** | Now | High |
| MC-05 | Cash count + distribute entries on the `/cash` hub | deep-link + action | E (daily closing) | grep: `/cash/count` & `/cash/distribute` appear only in `Finance.tsx`; `CashWallets.tsx` has 0 references — the tools exit to `/cash` but are unreachable from it | Two primary buttons on `/cash`: «عدّ الصندوق» and (when unallocated ≠ 0) «وزّع الكاش غير الموزع»; Finance links become secondary | `/cash` (wallets hub) | `/cash` page | Existing loops unchanged (count → done → `/cash`) | **P1** | Now | High |
| MC-06 | Success-closure feedback after money actions | feedback + content | B, F | `OrderDetail.run()` refreshes after `collectDebt`/deposit with **no success message and no cash delta**; DirectSale/Agreement editors navigate away silently; QuickActionSheet receipt is the one good example | Closure sentence after every money write: «تم تسجيل التحصيل — الكاش زاد 20.00 د.أ — المتبقي على خالد 0 د.أ» (inline notice) before/instead of silent navigation | Each owning editor/screen | all money writes | Number that changed + safe return visible | **P1** | Now | High |
| MC-07 | Saved-estimate view/edit | screen + route | D | Estimate rows show title + floor + date only; `costEstimateService.update()` **exists but no UI calls it**; delete + re-enter is the only correction | [NEW] `/tools/estimates/:id` deep editor (calculator form in edit mode; save = `update()`); guard wired; draft bridge unchanged | Tools | estimate row (row becomes tappable) | Estimate updated in place; bridge unchanged | **P1** | Now | High |
| MC-08 | Uniform CorrectionPreview contract («ما سيتغير / ما لن يتغيّر») | pattern + dialog | F | Impact previews exist ad hoc (EventsLayer before/after dl, cash reversal, cancel panel) but inventory reversal, sale cancel, and (future) supplier corrections have no guaranteed two-list preview | Shared dialog contract before every edit/delete/reverse of a financial record: two non-empty lists, reason rule, receipt with numbers, icons + labels | Shared (dialog layer) | every «تراجع/تصحيح/حذف» | «تراجع موثق» receipt; original preserved | **P1** | Now | Med-high |
| MC-09 | Plain statement one-pager («كشف الأسبوع») | screen + route | B (weekly), G | Period result + insights exist only inside Finance's collapsed layer; no single screen answers «شو صار هالأسبوع؟» with cash start→end, sold/collected/spent, result with qualifiers | [NEW] `/statement` stack reader: six plain lines max, every number carries its honesty qualifier, Amanah dual-truth line, cash start→end reconciles, rows tap to sources, period switcher | Statement (new) | Home On-Demand row; Finance period layer CTA | Reading → rows to sources; back to origin | **P1** | Now | High |
| MC-10 | Unsaved-input guard net closure (sheet, count, distribute, schedule, tools) | state + guard | B, D, H, F | QuickActionSheet close silently `reset()`s a typed amount; CashCount counted value lost on back; CashDistribution amount lost; Schedule capacity/reason unguarded; Tools calculator lost | Extend the existing 3-choice guard: quiet variant for transient surfaces («في رقم مكتوب — تسجّله أو تتجاهله؟»), full variant for count/distribute/schedule, soft variant for Tools | Shared (guard layer) | back/nav while dirty | Choice drawer; nothing typed is silently lost | **P1** | Now | High |
| MC-11 | Quick-sale wallet default = «الدرج» | behavior fix | B, E | `saleWalletId`/`expenseWalletId` initialize `""` and the empty option is «بلا نسبة الآن — كاش غير موزع» — every quick sale defaults to manufacturing unallocated cash | Default the selector to the drawer-kind wallet when one exists; keep «اتركه غير موزّع» explicit; no new data | QuickActionSheet | FAB sale/expense forms | Allocation recorded with the event; backlog stops growing by default | **P1** | Now | High |
| MC-12 | CostEditor linked-draft guard | state + guard | F | CostEditor has **0** references to `linkedOrderId` while DraftEditor and AgreementEditor guard converted drafts — a bookmarked URL can append a snapshot to a converted draft | On load, if `draft.linkedOrderId != null` → redirect to `/orders/:id` with a notice | CostEditor | direct URL / stale navigation | Redirect; no snapshot appended to converted drafts | **P1** | Now | High |
| MC-13 | Per-wallet full ledger (WalletLedger) | screen + route | E | `/cash` caps history at 8 global entries; no `/cash/wallet/:id` route exists | [NEW] `/cash/wallet/:id` stack reader: sticky balance header, full grouped-by-day entries with deltas, per-entry reversal (via MC-08), «عدّ الصندوق» primary for drawer wallets | Wallets hub | `/cash` wallet row | Full ledger; back to `/cash` | **P1** | Now | Med |
| MC-14 | Home money-truth surfacing: unallocated, unknown-opening flag, Amanah qualifier | content + state | B, E | Home facts = 4 fixed cards; no unallocated, no unknown-opening signal, and `recordedCashMinor` **includes** Amanah cash with no qualifier — the Home cash card overstates spendable money | (a) line under cash fact when unallocated ≠ 0 → resolution; (b) unknown-opening badge → opening-later road; (c) qualifier «منها أمانات X د.أ» when > 0 | Home facts block | Home (auto, conditional) | Truth visible on the morning screen; deep links to resolution | **P1** | Now | Med |
| MC-15 | Action-specific today labels + focus deep links | content + deep-link | B, G | Every Home today item's action label is the generic «افتح» (all 9 kinds); away-card actions land unfiltered | Verb labels («حصّل/سلّم/أكمل/راجع»); `?focus=`/`?layer=` params on landing | Home | Home today rows / away card | One tap from alert to the *action*, not just the page | **P2** | Now | High |
| MC-16 | Surface hidden capabilities (actual time/material; recurrence/capacity; guided opening import) | placement | A, B, F | ActualTime/ActualMaterial inside OrderDetail's collapsed drawer; recurrence+capacity inside Schedule's collapsed layer; guided opening import inside Settings' collapsed layer | Promote actual-panels to an OrderDetail section «شو صار فعليًا» when status ≥ execution; promote capacity to Schedule top; guided-import row into Foundation | OrderDetail / Schedule / Foundation | same | Visible without unfolding | **P2** | Now | High |
| MC-17 | Consume movement preselects originating order | deep-link | C, F | OrderDetail's panel navigates `/inventory/movement/consume` **without an order param** and the movement editor's `orderId` starts empty — the user re-picks the order they came from | Pass `?order=:id`; editor preselects; after save, back returns to the order | InventoryMovementEditor | OrderDetail «سجل الاستهلاك» | Movement recorded against the right order first time | **P2** | Now | High |
| MC-18 | Receipt → open/undo the just-created record | action + deep-link | A, B, F | Quick-sale receipt shows only text «صحّح من «العمل» أو «مالي» عند الحاجة» — no link to `/direct-sales/:id` | Receipt buttons: «افتح السجل» → `/direct-sales/:id`; optional «تراجع» through the documented flow | QuickActionSheet receipt | receipt | One-tap correction from the moment of record | **P2** | Now | High |
| MC-19 | Catalog back-context + product→sale shortcut | navigation + deep-link | C | Catalog's back is hardcoded `/orders` even when entered from Home; no «سجّل بيع هذا المنتج» anywhere in Catalog | Referrer-aware back (fallback `/orders`); reference row action «سجّل بيع» → `/direct-sales/new?item=:id` (reference preselected) | Catalog | Catalog rows | Sale editor prefilled from the reference; back returns to Catalog | **P2** | Now | High |
| MC-20 | Empty/CTA polish: Suppliers empty CTA; Orders create-sale CTA | content + action | C, H | Suppliers open-list empty is a warning sentence with no CTA in the slot; Orders list has no `/direct-sales/new` CTA — the full sale editor is unreachable from its own list | Suppliers empty: CTA + teaching line; Orders: secondary «تسجيل بيع مباشر» CTA near «مبيعاتي» | Suppliers / Orders | empty states / list header | Creation one tap from the list that owns the records | **P2** | Now | High |
| MC-21 | G5 wording: «أعلن» → glossary-compliant «سجّل … متوقعًا» | content | B | Finance CTA reads «أعلن تحصيلًا أو التزامًا قريبًا»; the glossary binds «متوقع» and forbids «إعلان» | Rename CTA to «سجّل قبضًا أو دفعًا متوقعًا»; align editor copy | Finance / G5DeclarationEditor | same | Terminology consistency (trust through language) | **P2** | Now | High |
| MC-22 | Direct-sale debts as Home-today items | content + state | B | Home `due_amount` items are built from **orders only**; direct sales with `partial_debt` appear nowhere on Home | Add `due_amount` items for aged direct-sale debts (e.g. > 3 days or follow-up set), capped by the 5-row budget | Home today | Home (auto) | Daily collections prompt covers the dominant sale type | **P2** | Now | Med |
| MC-23 | Supplier-name autocomplete (prevent split ledgers) | feature | C, F | `supplierName` is bare free-text; parties ledger groups by exact string — a typo silently creates a second "person" (customer free-text is by design; suppliers are repeated counterparties) | Datalist of existing supplier names on the purchase editor (no person-management screens) | SupplierPurchaseEditor | purchase editor | Consistent ledger grouping; no new stores | **P2** | Later | Med |
| MC-24 | Home locality/offline line (replace scope line) | content + explanation | B, H | Home renders «فتح مالي» scope line duplicating the tab; the honest locality sentence appears only in Settings/offline banner | Replace scope line with locality line «شغال بدون إنترنت — بياناتك على هذا الجهاز» (+ last export date when stale) | Home | Home (auto) | Offline-first trust visible daily, not only in Settings | **P2** | Now | Med |

**Register totals: 24 rows — 4×P0, 10×P1, 10×P2.**

## 6.1 Verified as NOT missing (rejected candidates — evidence)

These were candidate gaps; each was checked in code and found present. They must not be re-proposed:

| Candidate | Verdict | Evidence (code) |
|---|---|---|
| Saved-estimate → editable-draft continuation | **Rejected — exists** | `Tools.tsx` L523 → `/orders/draft/new?intent=planned_design&estimate=:id`; `DraftEditor.tsx` L46–86 (`prefillFromEstimate`, proposal notice, copied-once semantics); CostEditor estimate prefill |
| Home alert deep-linking | **Rejected — exists** | `TodayItemRow` navigates `item.href` to source records; away-card actions → `/parties`, `/settings`, `/orders`; recent-changes rows → sources (polish only → MC-15) |
| Offline indicators | **Rejected — exists** | `PwaRuntimeNotice.tsx` offline banner with honest local-first copy; SW update card; boot storage-failure recovery (4 codes) |
| Opening-balance later route | **Rejected — exists** | `/cash/wallet/:id/opening-later` (D-004) with `already-known` guard; entry on `/cash` per unknown wallet |
| Export reminder cadence | **Rejected — exists** | 7-day cadence (`homeControlCenterService` `daysSinceLastExport >= 7` or null → truth line), O-001 toggle respected; away-card backup age; `lastVerifiedExportAt` recorded |
| Undo / reversal behavior | **Rejected — exists** (events, sales, cash, inventory) | EventsLayer reverse/atomic edit/documented delete/restore + previews + reasons + idempotency messages; `CashReversalEditor`; `InventoryReversalEditor`; direct-sale revisions + conflict guard. Missing **only** for suppliers/orders → MC-01/MC-02 |
| Statement/period *data* | **Rejected — exists** (reading) | Finance «قراءة الفترة» layer: range, statuses, COGS sources, exclusions, insights. What's missing is a standalone one-page statement **screen** → MC-09 (placement, not data) |
| Empty-state guidance (broad) | **Rejected — exists** | Rich empties: Orders (CTA), Schedule («بدء طلب»), Tools estimates, Parties (+no-result state), CashWallets, count/distribute no-wallet states. Thin spots only → MC-20 |
| PWA / offline first-run explanation | **Rejected — exists** | Setup truth line; Settings local-truth card + export warning; PwaInstallControl (30-day dismissal) |
| Back-navigation with unsaved input | **Rejected — exists** (deep editors) | `UnsavedChangesGuard` + `useFormDirty` on all deep editors. The 4–5 unguarded surfaces are the real, narrow gap → MC-10 |
| Unit status explanation | **Rejected — exists** | Tools «حالة الوحدات» module matrix, data-derived states |
| Search across records | **Rejected — deferred by design** | Parties has name search; Orders/global search is not promised (E-00.14) — do not raise without owner decision |
| Error recovery wording | **Rejected — exists** | StartupGate storage failures with dedicated codes + reload CTA; public recovery routes; per-screen error states with retry |
| Person creation while recording | **Rejected — by design** | Free-text customer (D-001) and supplier names feed the parties ledger — no person entity; typo risk for suppliers noted as MC-23 |

---

# 7. OUTPUT E — Final Target Architecture

## 7.1 Decision register (D1–D14)

Each major decision uses: Problem / Decision / Why this fits the owner + evidence / Main trade-off / Priority.

**D1 — Keep the five-destination split.**
- Problem: does a 5-slot bottom bar (4 tabs + FAB) still serve one owner, one hand, one phone?
- Decision: keep `مشروعي الآن | العمل | سجّل | مالي | أدواتي` exactly.
- Why: each tab answers one owner question (source-of-truth §3); the FAB carries the one verb that crosses all domains («سجّل»). The 88-row catalog shows no capability that lacks a natural parent among the four. Tabs are load-bearing after the 2026-08-31 redesign. Benchmark P1 (Material/Android/Smashing: ≤5 destinations, bottom nav + central action) confirms the shell.
- Trade-off: finance-adjacent hubs (cash/parties/suppliers/inventory) are two taps deep from مالي. Accepted: مالي links them all; Home facts deep-link directly.
- Priority: P0 (stability — no code).

**D2 — FAB «سجّل» is the recording hub; sheets close over the standing screen.**
- Problem: daily records must be ≤10 seconds and must not cost the owner their place.
- Decision: 5-item menu; sale/expense stay in-sheet (receipt, no navigation); deep intents route out; «عربون أو تحصيل» becomes the collection picker (D6). Receipt gains «افتح السجل».
- Why: QuickActionSheet already implements in-sheet writes with idempotency keys; the breaks are the collection target (MC-03) and the missing receipt link (MC-18). Principle 3: transient ≤3 fields = sheet.
- Trade-off: rare complex sales go to the full editor — accepted (progressive disclosure).
- Priority: P0.

**D3 — Tools stays a separate destination.**
- Problem: could the calculator be a step inside order creation, freeing a tab?
- Decision: keep `/tools` as tab 4.
- Why: the calculator is a pre-commitment thinking tool with zero financial effect (source-of-truth §10); embedding it in the order flow would blur «تقديري» vs committed numbers and break the explicit conversion bridge. The module-status matrix also needs a neutral home.
- Trade-off: a tab slot spent on an occasional tool. Mitigated: 5th position; doubles as the honest "what exists" surface.
- Priority: keep (no change).

**D4 — Parties ledger stays under مالي, not العمل, not a tab.**
- Problem: parties touch both work (customers) and money (debts).
- Decision: `/parties` canonical parent = مالي; entries from Home away card, FAB picker footer, Tools modules; back = origin with `/finance` fallback.
- Why: the ledger's content is money owed («مين عليه إلَي، وعليّ لمين؟»), its service is a pure read model over debts, and its primary action is collection (money-in). Benchmark P3 (khata apps): the per-customer balance is a *money* surface. Not a tab: it is consulted, not inhabited.
- Trade-off: a customer-centric owner must accept the money-first framing; the Work side keeps customer names on orders/sales rows.
- Priority: keep; the collection shortcut upgrade is P0 (D7).

**D5 — Quick sale is a bottom sheet with default wallet «الدرج».**
- Problem: the most frequent write must fit the ≤2-mandatory-inputs rule.
- Decision: in-sheet form: المبلغ (only mandatory) + محفظة القبض defaulting to «الدرج» + «خيارات أكثر» disclosure.
- Why: today's sheet works in ≤3 touches but defaults the wallet to «بلا نسبة الآن» (`QuickActionSheet.tsx:404`), silently manufacturing the unallocated backlog the owner must later resolve. Benchmark P6 (YNAB "give every dollar a job"): a default of "no job" is a design bug, not neutrality.
- Trade-off: attribution mistakes (paid into another wallet) — recoverable via documented allocation, visible in the wallet ledger.
- Priority: register MC-11 (P1, owner-impact) — sequenced in Wave 0 because the default fix is cheap wiring; sheet re-ordering same wave.

**D6 — Deep-link vocabulary: every alert routes to its source document.**
- Problem: several alerts land on generic lists (FAB collection → plain `/orders`; negative-unallocated → `/cash` review; Home receivables road → `/orders`).
- Decision: standardize `?focus=` / `?layer=` / `?mode=cover` / `?from&to` on existing routes; rule: no alert routes to an unfiltered list.
- Why: one-tap-from-alert-to-resolution is the difference between «النظام بيجيبلي» and «بيدور بنفسي». Params keep routes flat, survive cold starts, and match the existing `?event=` precedent.
- Trade-off: landing pages must parse params defensively (unknown values fall back silently).
- Priority: P0 (re-pointing), P1 (hardening).

**D7 — Collections live in a dedicated CollectionSheet, fed by three doors.**
- Problem: collecting a debt = Parties → source record → full editor → difference dialog (sales) — asymmetric and multi-hop for the single most common money-in event.
- Decision: ورقة التحصيل CollectionSheet (amount prefilled, wallet «الدرج», receipt closure). Doors: Home due row, Parties «حصّل من X», FAB picker. The sheet owns no data.
- Why: benchmark P3: khata apps' most-loved features are all about getting money back; in Micro «قبضت من خالد» costs 3–4 taps today. The 10-second rule applies.
- Trade-off: a second write surface per source type must reuse the exact service guards (over-collection, wallet balance) — the sheet is a view, not a new path.
- Priority: P0.

**D8 — The period statement lives on its own stack screen `/statement`.**
- Problem: «كيف كان أسبوعي؟» has no home: period result is a collapsed Finance layer with 15-row density.
- Decision: `/statement` [NEW]: six plain lines, honesty qualifiers on every number, period switcher. Entries: Home + Finance period layer. Finance keeps analytical depth.
- Why: statements are a full-screen reading pattern (principle 3); Home is the weekly-review entry point; Finance must not grow another top-level block (already ~13).
- Trade-off: two period-related surfaces — differentiated: plain story vs analytical depth.
- Priority: P1.

**D9 — Cash tools (count + distribute) move their primary entry to `/cash`.**
- Problem: both tools are reachable only from Finance; both exit to `/cash`; the hub never links back; `cover_payment` is unreachable when negative.
- Decision: `/cash` gains the unallocated strip + «وزّع» button (any sign) + «عدّ الصندوق» primary button + ledger rows. Finance keeps secondary links. The negative alert deep-links `?mode=cover`.
- Why: counting is performed standing at the drawer — the wallets page is that drawer's representation. The source-of-truth's own exit map already treats المحافظ as the tools' home; the code just never linked back.
- Trade-off: Finance loses some "everything money is here" completeness — mitigated by quick links.
- Priority: register MC-05 (P1, owner-impact) — entry buttons sequenced in Wave 0 as cheap wiring; ledger screen (MC-13, P1) in Wave 2.

**D10 — Order price revision becomes a documented deep edit `/orders/:id/price`.**
- Problem: changing an agreed price today means cancel + deposit settlement + restart; direct sales have `price_cut`, orders have nothing.
- Decision: [NEW] editor: current → new price, protection-price comparison, impact preview (receivable delta, deposit truth unchanged, no cash effect unless collected), reason, revision preserved in the order event log.
- Why: price changes are a normal micro-business event («الزبون زاد الطلب»); forcing cancel destroys order history. Benchmark P4: every professional system (Xero/Sage/QuickBooks) allows correcting posted transactions with preserved history.
- Trade-off: more state in the order domain (revision list + receivable recompute) — bounded, consistent with the direct-sale precedent.
- Priority: register MC-02 (P0, owner-impact — the current alternative destroys the order and its deposit settlement); sequenced in Wave 2 because it needs service-layer work first.

**D11 — Supplier purchases get a detail screen + correction paths.**
- Problem: opening `/suppliers/purchase/:id` shows the payment form; the purchase/payment family has no edit/reverse/delete at all — the only record family outside the correction discipline.
- Decision: retarget to PurchaseDetail; add `/edit` (impact preview) and `/payment/:paymentId/reverse` (documented).
- Why: parity with events/sales/cash/inventory corrections («سجل لا يحذف بصمت» must be universally true); benchmark P4.
- Trade-off: service-layer work first (correction APIs needed) — navigation defines the destination.
- Priority: register MC-01 (P0, owner-impact — the only record family with zero correction paths); sequenced: detail retarget in Wave 2, corrections in Wave 2/3 because the service layer needs correction APIs first.

**D12 — Back-stack and unsaved-input rules become uniform.**
- Problem: back targets are hard-coded and inconsistent (catalog always `/orders`; schedule `/`); five transient surfaces lose typed input silently (quick-sheet amount, counted drawer value, distribution amount, schedule capacity, calculator); CostEditor misses the linked-draft guard.
- Decision: referrer-aware back with canonical fallbacks; extend the guard to the four unguarded pages + sheet discard confirm; add the CostEditor guard; deep editors keep step-back.
- Why: the guard component and history sentinel already exist — this is wiring, not invention. Losing a counted drawer amount is exactly the distrust Micro must avoid.
- Trade-off: more dialogs — kept quiet (2-choice for non-financial surfaces).
- Priority: register MC-10/MC-12 (P1, owner-impact) — guards and the CostEditor fix sequenced in Wave 0 as cheap wiring; contextual back (D12) in Wave 2.

**D13 — Hidden layers surface where their question is asked.**
- Problem: real capabilities are invisible (actual time/material, recurrence/capacity, guided import).
- Decision: OrderDetail gains a visible «شو صار فعليًا» section when status ≥ execution (consume preselects the order); Schedule's «التكرار والسعة» becomes a visible section; guided import becomes a Settings + Foundation row.
- Why: these answer questions the owner is already standing on. Benchmark P7 failure mode: progressive disclosure must not hide *primary* actions.
- Trade-off: density increases on OrderDetail/Schedule — mitigated by the demotions in Output B.
- Priority: P1.

**D14 — Catalog stays one hub under العمل with contextual back.**
- Problem: `/catalog` is a 1,859-line page; its back always goes to `/orders` even from Home.
- Decision: keep route + العمل parent; add referrer-aware back; internal step-split is a screen-level refinement (P2).
- Why: catalog is a reference library consulted from work contexts, not a daily destination; a tab would waste the slot.
- Trade-off: occasional scroll-length until the step-split lands.
- Priority: P2.

## 7.2 The complete target architecture (one coherent journey)

**Shell.** Five destinations (D1) + header gear + theme. Level-2 domain hubs (cash, parties, suppliers, inventory under مالي; catalog, schedule under العمل) — Level-3 stack readers — Level-4 deep editors with chrome hidden and 3-choice guards. The sheet layer overlays any surface: QuickActionSheet (sale/expense fast paths), collection picker, CollectionSheet, MaterialSheet, expense-context drawer, CorrectionPreview dialog.

**The owner's day in the target system.** Morning: Home shows the single priority with an action verb; one tap opens the source document or the prefocused collection sheet; the fact chips carry the money truth (Amanah qualifier, unallocated line, unknown roads). During the day: every record is a sheet away — sale (amount + default drawer), expense, collection — receipts close over the standing screen and offer «افتح السجل». Closing: `/cash` → عدّ الصندوق (first-class on the hub) → done screen → optionally `/statement` for «شو صار اليوم؟». Weekly: `/statement` six honest lines → rows to sources → `/parties?focus=overdue`. Absence: away card digest, guilt-free. Mistake: any record → CorrectionPreview («ما سيتغير / ما لن يتغيّر») → documented receipt — including supplier purchases and order prices, which today have no path at all. Protection: verified export with staleness lines; reset gated behind it.

**Invariants preserved in every change** (must hold in implementation):
1. Unknown ≠ zero — «غير محدد بعد» / «غير متاح» + road, never 0.00.
2. Every correction = preview → confirm → documented receipt; originals preserved; no silent deletes; no between-states.
3. One authoritative owner per write; shortcuts never own the write.
4. Sheets never navigate on success; alerts never land on unfiltered lists.
5. The six financial non-negotiables: collection ≠ profit; debt ≠ cash; purchase ≠ COGS; owner money ≠ revenue; Amanah = real cash but not business-owned; unknown ≠ zero.
6. Glossary wording (متوقع not أعلن؛ د.أ after the number; تراجع موثق؛ الخطوة التالية).
7. Zero financial effect from Tools (calculator/estimates) by contract.

## 7.3 Implementation roadmap (for a later, separate implementation prompt — nothing implemented in this task)

**Wave 0 — cheap wiring (no new stores, no schema change):** re-point FAB collection → picker/`/parties?focus=receivable`; `/cash` action buttons (count/distribute) + negative alert `?mode=cover`; receipt «افتح السجل»; guards (sheet/count/distribute/schedule/tools) + CostEditor linked-draft guard; rename «أعلن…» CTA; default wallet «الدرج»; action-verb today labels; Home truth lines (MC-14/24).

*Priority reconciliation:* register priorities (§6) rank **owner impact**; waves rank **implementation order** (cheap wiring first). Where a wave label differs from a register priority, the register governs impact and the wave governs sequence — e.g. MC-01/MC-02 are impact-P0 but sequenced in Wave 2 because they need service-layer work first; MC-05/MC-10/MC-11/MC-12 are impact-P1 but land in Wave 0 because they are pure wiring.
**Wave 1 — P0 new surface:** CollectionSheet (N1) — a pure view over existing services.
**Wave 2 — new surfaces & corrections (register P0/P1 items needing service work):** StatementView (N2), WalletLedger (N4), CorrectionPreview contract (N3) across correction points, order price revision (D10/MC-02, impact-P0), purchase detail retarget + corrections (D11/MC-01, impact-P0), surfaced layers (D13), estimate edit (MC-07), success-closure feedback (MC-06), contextual back (D12).
**Wave 3 — P2:** PartyDetail (N5), catalog step-split + product→sale shortcut, supplier-name autocomplete (MC-23, later), direct-sale debts on Home (MC-22).

Each wave stays within the current slice discipline: independent branch → local checks → PR → CI/Cloudflare → independent acceptance → merge; `docs/operations/current-state.md` updated inside the PR; no Auth/Cloud/Market/Delivery; no schema/export change required by any Wave-0/1 item (CollectionSheet and statement are views over existing services).

## 7.4 Benchmark evidence summary (what transferred, what did not)

| Pattern | Who it serves / problem | Evidence | Transferred to Micro | Not transferred |
|---|---|---|---|---|
| P1 Bottom nav + central record button | one-handed owners | Material Design; Android design guidance; Smashing (≤5 destinations) | the five-destination shell confirmed | nav drawers; 6th destination; FAB-as-tab ambiguity (Micro's FAB opens a sheet) |
| P2 Thumb-zone reachability | one-handed use during physical work | Hoober (~1,333 users: 49% one-handed); Hurff; Smashing | FAB center-bottom; sticky CTA/result bars; save at form ends | nothing contradicting |
| P3 Khata/ledger apps (Khatabook, OkCredit) | micro-merchants tracking credit per customer | OkCredit Play listing; Khatabook features/reminders; market coverage | **collection-first mental model** (validates CollectionSheet as P0); per-customer readable ledger | SMS/WhatsApp/bot-call reminders (offline-first, no bell by E-00.14); UPI/payment links; customer-facing app; cloud sync |
| P4 Reverse-not-delete corrections | trustworthy small-business records | QuickBooks community; Xero journal guide; Sage Intacct; audit-trail sources | confirms MC-01/MC-02 as P0; MC-08 preview-before-commit | double-entry mechanics; accountant roles; period-lock |
| P5 First-run → first value | scared first-time owner | Amplitude TTV; LinkRunner; QBSE snap-receipt; Wave first-invoice | Micro's 1-mandatory-field Setup + FAB quick sale already beats these benchmarks — keep; MC-18 receipt-undo is the classic correction-confidence moment | OCR receipt-scan; estimate→invoice conversion (Micro has estimate→draft already) |
| P6 Zero-based allocation (YNAB) | money without a job | YNAB; Ramsey; NerdWallet | unallocated cash framing; quick-sale default fix (MC-11); cover-payment reachability (MC-04) | envelope budgets for spending categories; "age of money" |
| P7 Progressive disclosure | complexity management | NN/g progressive disclosure + complexity | collapsed Finance layers and classification drawer are correct usage | the failure mode transferred instead: over-hiding primary actions → MC-16 |
| P8 Empty states that teach | first contact with a module | NN/g; Pencil & Paper; Toptal | Micro mostly complies; Suppliers empty + Orders CTA are the lapses → MC-20 | — |
| P9 Arabic RTL mobile usability | RTL correctness | practitioner sources (uxdesign.cc, kristi.digital, purrweb) | Micro already does the hard parts (mirroring, bdi isolation, ASCII digits in inputs, د.أ suffix); label-expansion point supports the density compressions | Arabic-Indic vs Western numerals claims are context-dependent [assumption] |
| P10 Jordan small-business context | target population | IMF (HBB prevalence); UN Women; World Bank MSME; GSMA MENA; CBJ/Mastercard | one-owner shape; cash-first recording; «الدرج» default; Arabic-only low-jargon wording | **no tax/legal/regulatory requirements derived — anything regulatory is explicitly out of scope and labeled assumption** |

## 7.5 Final quality gate

If the owner opened the proposed future version today: **Home** would show the day's single priority with an action verb, one tap from its source, with honest money facts (Amanah qualifier, unallocated line, unknown roads, never 0.00); **سجّل** would record a sale in one input + a default drawer, a collection in two, and a receipt that can open or undo the record; **العمل** would put the priority first and compress lists; **مالي** would put the cash decision first, separate Amanah from profit with the dual-truth sentence, and route every alert to its resolution; **أدواتي** would keep the calculator free of any commitment with a live result always visible and saved estimates editable and convertible; every correction — including supplier purchases and order prices — would show what changes and what does not before confirming, preserve the original, and return safely; the week would have an honest one-page statement; absence would be guilt-free; and the backup truth would be visible daily. The register in Output D states exactly what must be added to reach this state, in what order, and with what confidence.

---

# 8. Evidence & References

## 8.1 Primary sources (repository, verified on `main` @ `1b37c77`)

`apps/prototype-web/client/src/pages/*` (35 page components read in full), `app/MicroRouter.tsx`, `app/navigation.ts`, `app/routeClassifier.ts`, `app/StartupGate.tsx`, `components/layout/MicroAppShell.tsx`, `components/layout/QuickActionSheet.tsx`, `components/layout/BottomNav.tsx`, `components/layout/AppHeader.tsx`, `components/forms/UnsavedChangesGuard.tsx`, `components/finance/EventsLayer.tsx`, `components/finance/CorrectionsLayer.tsx`, `application/**` (agreements, cash, catalog, cost, direct-sales, drafts, estimates, finance, financial-pulse, follow-up, fulfillment, g5, home, inventory, parties, suppliers, transfers services), `src/domain/**` (13 domain units), `storage/local/IndexedDbLocalStore.ts`, `docs/product-source-of-truth.md`, `docs/operations/current-state.md`, `docs/08-glossary.md`, `docs/expansion/README.md` (E-00.14).

## 8.2 External sources

| # | Title | URL | Supports |
|---|---|---|---|
| 1 | Material Design — Bottom navigation | https://m2.material.io/components/bottom-navigation | P1: ≤5 destinations, bottom nav + FAB |
| 2 | Android design — Layout and navigation patterns | https://developer.android.com/design/ui/mobile/guides/layout-and-content/layout-and-nav-patterns | P1 |
| 3 | Smashing Magazine — Golden rules of bottom navigation | https://www.smashingmagazine.com/2016/11/the-golden-rules-of-mobile-navigation-design | P1 |
| 4 | Hoober (UX Matters) — How Do Users Really Hold Mobile Devices? | https://www.uxmatters.com/mt/archives/2013/02/how-do-users-really-hold-mobile-devices.php | P2: 49% one-handed; thumb zone |
| 5 | Hurff — Designing for thumbs | https://www.scotthurff.com/posts/how-to-design-for-thumbs-in-the-era-of-huge-screens | P2 |
| 6 | Smashing Magazine — The Thumb Zone | https://www.smashingmagazine.com/2016/09/the-thumb-zone-designing-for-mobile-users | P2 |
| 7 | OkCredit (Google Play) | https://play.google.com/store/apps/details?id=in.okcredit.merchant | P3: receivables ledger for micro-merchants |
| 8 | Khatabook — features | https://khatabook.com/blog/khatabook-app-features | P3: reminders + reports as loved features |
| 9 | ET BFSI — Khatabook bot-call reminders | https://bfsi.economictimes.indiatimes.com/news/fintech/khatabook-rolls-out-automated-bot-call-reminder-feature-to-improve-credit-collection/87275626 | P3: collection-reminder centrality |
| 10 | Business Insider — Khatabook market position | https://www.businessinsider.com/khatabook-early-market-leader-in-digital-bookkeeping-in-india-2020-11 | P3: khata category context |
| 11 | QuickBooks community — reverse vs delete | https://www.facebook.com/groups/quickbooksonlinesupport/posts/4096052587388035 | P4 (practitioner) |
| 12 | Xero — Journal entries guide | https://www.xero.com/us/guides/journal-entry | P4: correcting/reversing standard |
| 13 | Sage Intacct — reversing posted entries | https://www.randgroup.com/insights/tip-of-the-month/sage-intacct-totm/sage-intacct-tip-of-the-month-correct-mistakes-faster-by-reversing-posted-journal-entries-in-sage-intacct | P4: reverse-not-rekey |
| 14 | Foundation Software — audit trails | https://www.foundationsoft.com/learn/audit-trails-date-sensitivity | P4: audit trail of every adjustment |
| 15 | Gimbla — audit trail glossary | https://gimbla.com/glossary/audit-trails | P4 |
| 16 | Amplitude — Time to Value | https://amplitude.com/blog/time-to-value-drives-user-retention | P5: TTV → retention |
| 17 | LinkRunner — onboarding metrics | https://linkrunner.io/blog/top-10-mobile-app-onboarding-metrics-that-predict-long-term-retention | P5: time-to-first-core-action |
| 18 | Userpilot — onboarding benchmarks | https://userpilot.com/blog/user-onboarding | P5 (directional) |
| 19 | QuickBooks Solopreneur | https://quickbooks.intuit.com/solopreneur | P5: solo-owner shape |
| 20 | Wave (App Store) | https://apps.apple.com/us/app/wave-small-business-software/id881629660 | P5: first-invoice path; editable records |
| 21 | YNAB — zero-based budgeting | https://www.ynab.com | P6: give-every-dollar-a-job |
| 22 | Ramsey — YNAB vs EveryDollar | https://www.ramseysolutions.com | P6 (practitioner) |
| 23 | NerdWallet — zero-based budgeting | https://www.nerdwallet.com | P6 |
| 24 | NN/g — Progressive Disclosure | https://www.nngroup.com/articles/progressive-disclosure | P7 + its failure mode |
| 25 | NN/g — Managing visual complexity | https://www.nngroup.com/videos/managing-visual-complexity | P7 |
| 26 | NN/g — Designing Empty States | https://www.nngroup.com/articles/empty-state-interface-design | P8 |
| 27 | Pencil & Paper — Empty State UX | https://www.pencilandpaper.io/articles/empty-states | P8 |
| 28 | Toptal — Empty-state UX design | https://www.toptal.com/designers/ux/empty-state-ux-design | P8 |
| 29 | uxdesign.cc — robust RTL UI | https://uxdesign.cc/designing-a-robust-right-to-left-ui-in-arabic-hebrew-and-farsi-d1e662a09cfa | P9 (practitioner) |
| 30 | kristi.digital — RTL mobile design | https://kristi.digital/shots/mobile-app-design-for-right-to-left-languages-arabic-language | P9 (practitioner) |
| 31 | Purrweb — designing an Arabic app | https://www.purrweb.com/blog/halal-design-how-to-make-an-app-in-arabic | P9 (practitioner) |
| 32 | IMF — Jordan: Selected Issues (2022) | https://www.elibrary.imf.org/view/journals/002/2022/222/article-A001-en.xml | P10: HBB prevalence |
| 33 | UN Women — Women's Informal Employment in Jordan (HBB brief) | https://jordan.unwomen.org/sites/default/files/Field%20Office%20Jordan/Attachments/publications/2021/JONAP_Womens%20Informal%20Employment%20in%20Jordan/Womens%20Informal%20Employment%20in%20Jordan%20-%20Challenges%20Facing%20Home-Based%20Businesses%20During%20COVID-19.pdf | P10 |
| 34 | UN Jordan — same brief (landing) | https://jordan.un.org/en/130281-womens-informal-employment-jordan-challenges-facing-home-based-businesses-during-covid-19 | P10 |
| 35 | EFI/IFE — formalizing Jordan's informal economy | https://www.efi-ife.org/en/pdf/policy-brief-formalizing-the-informal-economy-in-jordan-to-promote-women-s-economic-participation | P10: unregistered HBB context |
| 36 | World Bank — Developing MSMEs in Jordan | https://openknowledge.worldbank.org/entities/publication/0348731d-3449-5bb0-949e-0c90a18f6054 | P10 |
| 37 | DoS Jordan — Employment & Unemployment | https://dosweb.dos.gov.jo/labourforce/employment-and-unemployment | P10 (generic) |
| 38 | GSMA — Mobile Economy MENA 2025 | https://www.gsma.com/solutions-and-impact/connectivity-for-good/mobile-economy/mena | P10: smartphone-first |
| 39 | CBJ — Payment Systems Legislations | https://www.cbj.gov.jo/EN/List/Payment_Systems_Legislations | P10: regulatory existence only — no requirement derived |
| 40 | Mastercard × CBJ (2024) | https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2024/march/mastercard-partners-with-central-bank-of-jordan-to-build-a-more-robust-digital-payment-ecosystem-in-the-kingdom | P10: digital payments growing, not universal |
| 41 | Zoho Books mobile apps | https://www.zoho.com/us/books/accounting-mobile-apps | P5: estimates editable on mobile (MC-07 analog) |
| 42 | NN/g — Confirmation dialogs | https://www.nngroup.com/articles/confirmation-dialog | MC-08 support |
| 43 | NN/g — Preventing user errors | https://www.nngroup.com/articles/user-mistakes | MC-08 support |

**Assumptions labeled:** cash dominance in Jordanian micro-commerce [assumption — CBJ/Mastercard show digital payments growing, not universal]; cultural similarity of credit-book practice between South Asia and Jordan [heuristic, not requirement]; Arabic-Indic vs Western numerals preference [context-dependent]; informal status ≠ no bookkeeping need [evidence shows HBBs track cash/debt informally]. No legal, tax, or regulatory requirement was derived from any source.

**Docs ↔ code conflicts found (code wins):** source-of-truth says the distribute strip lives "في مالي/المحافظ" (code: Finance only); glossary forbids «أعلن» (code: Finance CTA violates it); route count 39 not 38; the exit map for count/distribute assumes a `/cash` linkage that was never built.
