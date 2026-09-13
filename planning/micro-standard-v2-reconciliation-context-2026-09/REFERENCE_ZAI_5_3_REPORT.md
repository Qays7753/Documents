# Micro Standard v2 ↔ Micro — Integration Comparison and Read-Only UI/AUX Scan

**Report date:** 2026-09-14
**Mode:** Read-only analysis and planning only. No code was generated. No file in either repository was modified. No access token was used. No branch was created. Nothing was uploaded.
**Strategy under evaluation (fixed, not open to replacement):** Contract-first + Token-driven + Component-driven + Feature-oriented + Composition-based.

---

## 1. Executive verdict (plain language)

The current Micro UI can be rebuilt around Micro Standard v2 **without touching a single financial rule and without any bulk restructuring** — but only after the owner makes **thirteen explicit decisions**, almost all of them about color and naming rather than architecture.

The comparison found a clear asymmetry. Micro's *behavioral grammar* is already ahead of the Standard in the places that matter most for a financial product: honest voids (unrecorded / unavailable / measured-zero), state words, pending-never-reads-as-success, idempotency copy, bidi isolation, English digits, a pure domain layer, and guard-enforced token discipline are all implemented, tested, and must be **preserved, not replaced**. Micro is *behind* the Standard precisely in the presentation plumbing the Standard was built to own: a single 6,962-line `index.css` simultaneously carries tokens, component styles, and page styles; only **3 token names intersect exactly** with the Standard; **7 shared color roles have drifted in value**; **no shared UI primitives exist** (492 raw `<button>` elements across 84 files hand-type their class strings); per-page status-label maps and tone unions are duplicated 15+ times; and the AUX-layer `QuickActionSheet` quietly contains a complete sale/expense finance feature (761 lines) that belongs in the Feature-Pattern layer.

The Standard, for its part, is a genuine **contract package, not a component library**: it owns tokens (120 custom properties, 18 approved hex values), owner-approved action classes, the financial-state presentation matrix, value-zone / period-chip / operational-row slot contracts, overlay rules, phone geometry, and accessibility constraints — and it explicitly refuses to own product semantics, which is exactly the boundary the fixed strategy requires.

**Bottom line:** nothing found in this comparison requires re-architecture, and nothing requires changing financial meaning, posting behavior, permissions, or sync. The work is: make the thirteen owner decisions, then execute six small, independently revertable waves (guards → token adapter → primitives → sheet/dialog unification → QuickActionSheet split → patterns/structure). Until the owner decides, nothing color- or naming-related should change. No stop condition was triggered.

---

## 2. Exact sources read

| Source | URL | Branch | Commit SHA actually read | Commit metadata |
|---|---|---|---|---|
| Micro repository | https://github.com/Qays7753/Micro | `main` | `c0469e265f24c70427eb7826dee717be117cff87` | 2026-09-13 11:52:12 +0300 — "Merge pull request #159 from Qays7753/remediation/micro-full-hardening-2026" |
| Documents repository | https://github.com/Qays7753/Documents | `main` | `864263c190f5d3da6041acfafb0720e85ac6e320` | 2026-09-13 14:00:23 +0000 — "docs: record final copy main publication verification" |
| Standard package | https://github.com/Qays7753/Documents/tree/main/micro-standard-v2 | `main` | (same as Documents, above) | 31 files verified present |

Both repositories were cloned **anonymously and read-only** (public HTTPS, no credentials). The access token included in the request's "GitHub upload inputs" was **not used**, per the mission's non-negotiable rules ("Do not use an Access Token. No GitHub write operation is authorized.") and the final instruction ("Do not create a branch"). Consequently, no upload to `planning/micro-standard-v2-micro-integration-comparison-2026-09/` on branch `micro-standard-v2-micro-integration-comparison-20260913` was performed; this report is delivered in chat and as a downloadable Markdown file for the owner to place there if they choose.

**Standard package completeness check (all present, 31 files):** README.md, RELEASE.md, MANIFEST.json, design-tokens.css, design-tokens.json, component-gallery.html, component-gallery.css, component-gallery.js, component-contracts.md, button-system.md, component-states.md, color-system.md, accessibility.md, verification-report.md, coverage-matrix.json, decision-log.md, self-critique.md, source-inventory.md, typography.md, surface-system.md, visual-direction.md, input-system.md, motion-interaction.md, empty-loading-error-states.md, content-guidelines.md, data-display-system.md, iconography.md, navigation-shell.md, spacing-radius-elevation.md, responsive-geometry.md, overlay-system.md. All 17 files listed in the mission were found; the package additionally contains 14 further spec files, all of which were read.

---

## 3. Scope and limitations

**What was done.** Five specialized agents ran against the two clones at the SHAs above: (1) a factual Micro UI/AUX inventory, (2) a full Standard contract mapping, (3) a reuse/composition/boundary analysis with the required read-only Structure/Architecture/Code Organization Scan, (4) a feature-pattern and screen-gap analysis, and (5) an independent synthesis and quality review that re-verified the other four agents' headline claims directly against the repositories. All agents were read-only; the only writes were to a local shared worklog outside both repositories.

**Limitations, stated honestly:**

- **Static analysis only.** Micro's tests were read and mapped but not executed; no dev server was run. Behavioral claims rest on test files, code reading, and the repo's own QA documentation.
- **Sampled verification.** The "~27 dead CSS classes" figure is directionally confirmed (7/7 spot-checks dead) but is not acceptance-grade until a class-existence guard exists (dynamic class construction is proven at `FinanceActivity.tsx:110`). Feature-pattern host files were sampled, not exhaustively re-read by the synthesizer.
- **Standard evidence accepted as recorded.** The Standard's headless-Chromium verification claims (contrast pairs, token resolution, geometry) were read as recorded evidence, not re-executed. The Standard itself does not claim physical-device or screen-reader testing; none was performed here either.
- **Counting methodology variance.** Micro class-selector counts vary by method (~430–440 unique `.micro-*` classes); exact figures are given with their method where they matter.
- **Out-of-scope respected throughout:** AI/chat systems, backend, financial formulas, posting/reversal/accounting policy, sync, permissions, product semantics, security/performance/infrastructure audits, the Accounting repository, and any use of Prototype v0 content as product truth. No finding below depends on Prototype content, old reports, or assumptions.

**Stop conditions:** none triggered. Both repositories opened; both SHAs recorded; the Standard package is present and matches the `Documents/main` link; no part of the analysis required modifying either repository.

---

## 4. Five-agent findings (separated by role)

### Agent 1 — Micro UI and AUX Inventory Analyst

Mapped the full route surface: **56 route entries → 52 page components** (64 files in `pages/`, of which 12 are co-located tests; no orphan pages), classified `setup | deep | surface` by `app/routeClassifier.ts` (~29–35 regex patterns), with global chrome (BottomNav + FAB + QuickActionSheet) shown only on `surface` routes and the header always rendered. Route knowledge is deliberately quadruplicated (router, classifier, `navigationContract.ts` fallbacks, `navigation.ts` labels) and kept in sync by `app/routeKnowledgeSync.test.ts`. The AUX shell is small and centralized (4 layout files) with keyboard-hide via `visualViewport`, safe-area handling, and a 116px surface clearance. Overlay behavior is split across **three mechanisms** (vaul drawer; hand-rolled `UnsavedChangesGuard` dialog; hand-rolled lock veils) with **no toast/snackbar** (deliberately removed, `App.tsx` Q-003) and **no shared Confirm component**. The shared-primitives layer is thin (`components/ui/` = drawer + tooltip, with tooltip primitives dead); the real shared surface lives in `presentation/` and `forms/`. `index.css` (6,962 lines) is simultaneously the token file, the component stylesheet, and the page stylesheet. Dead/duplicated items found: dead tooltip primitives, `components/order/` vs `components/orders/` split, a z-70 "toast" ladder step with no toast, a legacy `/review` redirect, an intentionally-retained fallback key for a deleted route literal, and doc/code drift on two frozen color values.

### Agent 2 — Micro Standard Contract Mapping Analyst

Read all 31 Standard files. The Standard owns: the approved 18-value palette and named roles; owner-approved action classes (create/FAB clay; ordinary save warm-tint with clay pressed edge; high-consequence commit warm-ink fill; destructive via the high-consequence contract); the chosen/current selection grammar (2px `#C96442` edge + non-color cue, never automatic black fills); the 11-state presentation matrix (word + marker, pending ≠ success, unknown ≠ failure); value-zone slots (label/value/unit/period/delta) with three honest voids; the period chip (36px visual / 44px hit, staged until applied); operational-row slots with the ≤3px state edge stripe rule; the overlay system (shared scrim, staging, one-active-modal); the 4-destination nav shell + FAB gutter; a11y constraints; phone geometry (320–430px, 100/130/200% text scale, RTL/LTR); the type scale with a 12px floor; a 43-glyph icon registry with mirror flags; motion timings; spacing/radius/elevation; and content language rules. It explicitly does **not** own product implementation, financial policy/formulas/sync/backend, period/time semantics, currency/rounding policy, link-ink (left as an owner decision), domain compositions, dark mode, a chart library, or Prototype-derived content. Token mapping surface: **only 3 exact-name intersections** (`--radius-control/card/sheet`); ~6–8 value-identical mappings under different names; ~18 Micro-only roles with no Standard binding (teal accent, warning family — gold retired in the Standard, withdrawal family, brand text/soft, tint hexes); ~60+ Standard tokens unconsumed by Micro (zero `--vf-` references in `client/src`); and **value drift on 7 shared roles** (ink, clay, pressed, tint, divider, success, danger). Nine contract families cannot be applied directly without adapters (namespace, value migration, Button behavioral API, state-matrix enum mapping, period/void semantics, z-index layers, charts, icon registry, gallery-code-is-evidence).

### Agent 3 — Reuse, Composition, and Boundary Analyst

`index.css` anatomy: one `:root` block with **61 custom properties**, a `.dark` mirror with 46, a Tailwind `@theme inline` bridge of 21 — 132 definitions / 83 unique names total; 1,345 class-selector occurrences; ~432–438 unique classes; hex discipline is excellent (51 literals, 39 unique, only 2 outside token blocks, one being the sanctioned scrim). But the file contains **competing internal truths**: `.micro-button-block` ×3 identical, `.micro-button-quiet` ×2 **conflicting** (44px min-height vs compact — the later rule silently wins color), `.micro-number` ×3, `.micro-sheet-title` ×2; plus ~27 probably-dead classes. The component layer has **no strategy primitives at all** — 492 raw `<button>` elements across 84 files carry hand-typed class strings; every editor re-declares ad-hoc feedback tone unions; 15+ files define their own status-label maps. `QuickActionSheet.tsx` (761 lines) embeds complete sale/expense financial flows inside the AUX shell (layer 4 vs 5 violation). Layer discipline, by contrast, is strong and must anchor the integration: single token source, ESLint layer guards, verified domain purity, a clean services composition root (~44 services), money policy out of pages. Agent 3 also produced the nine-area Structure/Architecture/Code Organization Scan, a proposed (not executed) target module map with boundary adapters, token/component propagation failure points, and a risk register (quiet-button regression, geometry drift, dark-mode breakage, guard bypass, cascade-order dependencies, confirm-wording divergence, sheet-form coupling, dead-CSS false positives).

### Agent 4 — Feature-Pattern and Screen-Gap Analyst

Per-surface inspection found that Micro's screens already implement most of the Standard's *behavioral* contracts: value zones (Home `FactCard`, Finance `PositionCard`/`Metric`), operational row slots (Orders draft rows, `FinanceActivity` rows), state words everywhere, honest voids fully implemented ("غير مسجل — سجّله…", "غير متاح", "صفر مؤكد", "لا يُعرض صفر مكان المجهول"), pending ≠ success, and idempotency copy. Fifteen **Micro Feature Patterns** are needed at Layer 5 — home control-center, period-result reading, correction flow, read-only registry layer, restatement disclosure, pre-save computation review, decision surface, order-detail composition, inventory knowledge row, cash count/collect/distribution, tool result, scheduling buckets + capacity, party ledger, question-led chart, staged filter/period-chip surface. **Thirteen of the fifteen already have working reference implementations** in named Micro files (migration, not build); charts and staged filters are greenfield. Genuine gaps vs the Standard: no charts at all, no staged-Apply filter surface, no sort UI anywhere, route loading is text rather than skeleton, non-color state markers are inconsistent (`micro-status-chip` is text-only), and the period chip (36/44 geometry) does not exist. One hard divergence: **navigation labels** (Micro: مشروعي الآن / العمل / سجّل (FAB) / مالي / أدواتي vs Standard: الرئيسية / المالية / الطلبات / الأدوات).

### Agent 5 — Independent Synthesis and Quality Reviewer

Re-verified the headline numbers and **corrected the record** where agents disagreed or erred: index.css truth is `:root` = 61 / `.dark` = 46 / `@theme` = 21 → 132 definitions / 83 unique names (Agent 1's "~95 in :root" rejected; Agent 3's "61" and Agent 2's "132/83" both correct for their scopes); the Standard's `design-tokens.css` holds **120 custom properties (67 `--vf-*` + 53 unprefixed), not 138**; `.micro-home-heading` is not an empty rule (triplicated, real body); `MaterialSheet.tsx` also uses the `micro-bottom-sheet` skin (RepaymentSheet is the sole raw-skinned consumer); 22 (not 23) manual `د.أ` occurrences in OrderDetail; 40 (not 78) non-test files import `formatMoneyMinor`; 492 buttons in exactly 84 non-test files confirmed; 52 pages / 56 route entries confirmed; "no charts" confirmed by dependency and markup search; nav-label divergence, dead tooltip primitives, dual z-index systems, doc/code palette drift, and the QuickActionSheet layering violation all confirmed directly. Under-covered surfaces (Setup, Foundation, NotFound, SharePreview, Profile, AgreementEditor, Settings, pwa, app-lock) were verified healthy and folded in. **Prototype-contamination check: none found** — no agent justified any finding by Prototype content. Agent 5 consolidated everything into a 40-item finding register (Section 7), thirteen owner decisions (Section 16), and seven remediation waves W0–W6 (Section 17).

---

## 5. Current Micro UI/AUX inventory

All paths relative to `apps/prototype-web/client/src/` in the Micro repository unless noted. Counts verified by Agent 5.

### 5.1 Routes and chrome model

- Router: `app/MicroRouter.tsx` (wouter `Switch`, all pages lazy). 56 route entries → 52 page components; `/review` is a legacy redirect to `/finance`; `*` → `NotFound`.
- Classification: `app/routeClassifier.ts` — `MicroRouteKind = "setup" | "deep" | "surface"` via `deepFlowPatterns`. `showsGlobalChrome()` = surface only → BottomNav + FAB + QuickActionSheet; header always rendered.
- Route knowledge is deliberately kept in four synced files (`MicroRouter.tsx`, `routeClassifier.ts`, `navigationContract.ts`, `navigation.ts`) with `app/routeKnowledgeSync.test.ts` as the sync guard.

| Route | Page | Kind |
|---|---|---|
| `/` | `Home.tsx` ("مشروعي الآن" control center) | surface |
| `/setup` | `Setup.tsx` | setup |
| `/foundation` | `Foundation.tsx` | surface |
| `/orders`, `/orders/new` (redirect → `/orders/draft/new?intent=`), `/orders/:id` | `Orders`, `NewDraft`, `OrderDetail` | surface / deep / surface |
| `/orders/draft/:id`, `/agreement`, `/cost`, `/orders/:id/deliver` | `DraftEditor`, `AgreementEditor`, `CostEditor`, `DeliveryReview` | deep |
| `/direct-sales/new`, `/direct-sales/:id` | `DirectSaleEditor` | deep |
| `/schedule`, `/schedule/:id` | `Schedule`, `ScheduleEditor` | surface / deep |
| `/finance`, `/finance/statement`, `/finance/activity` | `Finance`, `Statement`, `FinanceActivity` | surface |
| `/finance/new/:type`, `/finance/withdraw`, `/finance/owner-entitlement`, `/finance/g5/declaration` | `FinancialEventEditor`, `OwnerWithdrawalEditor`, `OwnerEntitlement`, `G5DeclarationEditor` | deep |
| `/cash`, `/cash/wallet/:id` | `CashWallets`, `WalletLedger` | surface |
| `/cash/wallet/new`, `/opening-later`, `/adjust` | `CashWalletEditor`, `CashOpeningLaterEditor`, `CashAdjustmentEditor` | deep |
| `/cash/transfer`, `/distribute`, `/count`, `/cash/entry/:id/reverse` | `CashTransferEditor`, `CashDistribution`, `CashCount`, `CashReversalEditor` | deep |
| `/collect` | `Collect` | deep |
| `/inventory`, `/inventory/material/new`, `/inventory/material/:id/confirm`, `/inventory/movement/:type`, `/inventory/movement/:id/reverse` | `InventoryMaterials`, `MaterialEditor` (create/confirm), `InventoryMovementEditor`, `InventoryReversalEditor` | surface / deep ×4 |
| `/catalog` | `Catalog` | surface |
| `/tools`, `/tools/calculator`, `/tools/estimate/:id`, `/tools/integrity` | `Tools`, `CostCalculator`, `EstimateDetail`, `ToolsIntegrity` | surface / deep / deep / surface |
| `/assets`, `/assets/new`, `/assets/:id` | `Assets`, `AssetEditor`, `AssetDetail` | surface / deep / deep |
| `/loans`, `/loans/new`, `/loans/:id` | `Loans`, `LoanEditor`, `LoanDetail` | surface / deep / deep |
| `/suppliers`, `/suppliers/purchase/:id(/payment)` | `Suppliers`, `SupplierPurchaseEditor` | surface / deep |
| `/parties`, `/share/preview`, `/settings`, `/profile`, `/review`→`/finance`, `*` | `Parties`, `SharePreview`, `Settings`, `Profile`, redirect, `NotFound` | surface / deep / surface / surface |

### 5.2 Shell / AUX chrome (`components/layout/`)

- **MicroAppShell.tsx** (122 lines) — root chrome: `UnsavedChangesProvider`, `dir="rtl"`, `data-route-kind`, `data-keyboard-open` (visualViewport shrink > 120px hides chrome), idle-prefetch of the lazy QuickActionSheet, FAB intent routing (`customer_order` / `planned_design` / `collection`), renders PWA install control + runtime notice.
- **AppHeader.tsx** (61 lines) — sticky `z-40`, brand lockup + contextual label from `navigation.ts`, settings gear, theme toggle, scroll divider + 18px backdrop blur.
- **BottomNav.tsx** (71 lines) — fixed `z-30`, 5-column grid (2 items | center FAB "سجّل" | 2 items), prefix active matching, `aria-current`.
- **QuickActionSheet.tsx** (761 lines / 34KB) — vaul `Drawer` with modes `menu | sale-form | expense-form | receipt`; five quick actions; sale/expense completion **inside** the sheet (credit sale, wallet destination, expense-category chips, receipt mode, quiet-discard confirm, idempotency keys). This is the layering outlier (finance feature inside AUX chrome).
- Safe areas: 16 `env(safe-area-inset-*)` usages; scroll clearance: `.micro-main[data-route-kind="surface"]` bottom padding 116px (index.css:297); z-ladder documented as a comment at index.css:191 (content 0 / panel 1 / stickies 20 / nav+FAB 30 / header 40 / overlay 50 / sheet 60 / toast 70 — **z-70 has no component**).

### 5.3 Overlays

Shared: `components/ui/drawer.tsx` (vaul wrapper, Tailwind `z-50`/`z-[60]` — a second z system) used by QuickActionSheet, `MaterialSheet.tsx`, `RepaymentSheet.tsx`; `UnsavedChangesGuard.tsx` (hand-rolled dialog, focus trap, Esc = stay, history sentinel, `beforeunload`, PWA dirty-registry bridge); `AppLockGate` / `DataActionPinGate` lock veils. Page-local in-flow "layers": Finance `EventsLayer`/`CorrectionsLayer`/`DepositsLayer`/`G5DecisionPanel`, Schedule capacity layer, Catalog extras, OrderDetail cancel/price/deposit/delivery-reversal panels, Statement, AssetDetail ×3, LoanDetail ×2, G5DeclarationEditor, DirectSaleEditor cancel, ToolsIntegrity. **No toast/snackbar** (Toaster deliberately removed — `App.tsx` Q-003). **No shared Confirm component** (inline `micro-confirm-warning` labels at `AgreementEditor.tsx:325`, `SettingsOperatingModeSection.tsx:107`).

### 5.4 Shared components & utilities

- `components/presentation/`: `DisplayValue.tsx` (Money/Integer/Quantity/LocalDate/DateTime/Time/Month renderers with LTR/bdi walls — ~30 consumers), `InfoCard.tsx`, `DecisionPanel.tsx`, `EventEffectPreview.tsx` (real domain dry-run), `ActualTimePanel.tsx`.
- `components/forms/`: `EnglishNumberInput` (ASCII/LTR money, minor units), `EnglishQuantityInput` (milli), `LocalDateField` (DD/MM/YYYY in `bdi`, `lang="en"`), `UnsavedChangesGuard`, `useFormDirty`, `useFormDraft` (contract 36), `FormDraftRestoreBanner`.
- `presentation/`: `formatters.ts` (money minor/100 en-US 2dp, Asia/Amman dates, `formatArabicPlural`, `formatMoneyWithUnit` → "… د.أ" — single currency-unit source), `plurals.ts`, `g5Plurals.ts`, `activityLabels.ts`, `catalogPresentation.ts`, `ownerEntitlementPresentation.ts`, `orderAgreementPresentation.ts` (status → next-action map), `cashCountMessages.ts`.
- `components/ui/`: only `drawer.tsx` + `tooltip.tsx` (tooltip primitives dead; only `TooltipProvider` used).
- `contexts/ThemeContext.tsx`: light/dark/system, persisted; `.dark` block = 46 token overrides (index.css:98–144).

### 5.5 Feature components

`finance/` (8: EventsLayer, CorrectionsLayer, DepositsLayer, FinancePeriodResultSection, CorrectionPreview, AllocationReviewCard, G5DecisionPanel, RestatementNote) · `order/` (3: ActualMaterialPanel, AgreementContextPanel, OrderEventLog) · `orders/` (1: OrderDepositPanels — imports `order/`) · `catalog/` (5 sections) · `cost/MaterialSheet` · `loans/RepaymentSheet` · `owner/` (2) · `security/` (3) · `settings/` (4 sections). The `order/` vs `orders/` split is a same-feature duplication.

### 5.6 index.css and other UI source-of-truth files

`index.css` (6,962 lines): Tailwind v4 + `@theme inline` bridge (19 shadcn names, L9–31) → `:root` **61 custom properties** (L33–96) → `.dark` **46 overrides** (L98–144) → `@layer base` → ~6,800 lines of per-feature CSS; ~432–438 unique classes; feature prefixes (`micro-finance` ×77, `micro-home` ×76, `micro-month` ×64, `micro-owner` ×61…); 30 media queries; only 2 `[dir=rtl]` rules (logical properties used elsewhere); hex discipline excellent (2 sanctioned exceptions). Companion guard scripts at repo root: `scripts/design-token-guards.py` (raw-hex ban, scale rules, `Z_LADDER={0,1,20,30,40,50,60,70}`, sanctioned scrim), `scripts/text-density-count.py`. UI docs: `docs/product/design-system-v1.md` (claims authority; palette table drifts from code — success `#2e7d57`/warning `#8a6927` vs code `#256b4a`/`#7a5c20`), `placement-principles-v1.md`, `mobile-ui-ux-reference-v1.md` (§6.1/6.2/6.4 self-cancelled), `apps/prototype-web/ARCHITECTURE.md`, `AGENTS.md`.

### 5.7 UI test families

27 `*.dom.test.tsx` journey tests at `src/` root; 12 co-located `*.ui.test.*` page acceptance tests; `U09.css.test.ts` (reads index.css text); QuickActionSheet guard/category/unit trio; navigation contract tests (`navigation`, `navigationContract`, `routeClassifier`, `routeKnowledgeSync`, `StartupGate.recovery`); docs-consistency tests (`group2–6Docs.test.ts`); exact-value characterization + cross-surface tests; UnsavedChangesGuard trio; ErrorBoundary; build gates (`design-token-guards.py`, `check-bundle-budget.mjs`).

---

## 6. Standard contract inventory (Micro Standard v2 Final Copy)

Verified counts (Agent 5): `design-tokens.css` = **120 custom properties (67 `--vf-*` + 53 unprefixed), all unique; exactly 18 approved hex values; 2 disclosed alpha derivatives** (scrim `rgba(20,20,19,.45)`, translucent header `rgba(250,249,245,.86)`).

- **Tokens**: surface ladder (canvas `#FAF9F5` / ground `#F5F4ED` / recessed `#F0EEE6` / surface `#FFFFFF` / tint `#E8E6DC` / soft `#D1CFC5`), ink ladder (`#141413`/`#4D4C48`/`#6B6962`/white), identity clay `#D97757` + interactive `#C96442`, semantic roles (info `#2C84DB`, status `#1490FF`, success `#629987`, error `#B53333`, focus, disabled pair), action aliases (`--vf-action-create*`, `--vf-action-save*`, `--vf-action-commit*`), `--vf-btn-*` bindings, 11-step type scale (28/24/20/17/15/13/12 with roles incl. `--text-kpi-*` and `--text-amount-*`), elevations `--shadow-sm/e1/e2/e3`, 10 motion durations + 3 easings, z-layers (`--z-scrim 250 / overlay 300 / fab 400 / snackbar 500`), control geometry (48px control, 36px compact, 56px topbar, 64px nav-min, 56px FAB + 16px offset, 20/24px icons, 8px progress track), radii (12/16/18/20/999), tint aliases, fonts (IBM Plex Sans Arabic / IBM Plex Mono).
- **Action classes (owner-approved)**: create/add/FAB = clay with dark ink (text-bearing) or white icon (icon-only), pressed `#C96442`, **never a financial value**; ordinary save/confirm = warm tint + ink with 2px clay pressed edge, press ≠ success, completion = check + past-tense word; high-consequence commit = warm-ink fill + white text + consequence word + icon + explanation + independent confirmation path; destructive = error ink via the high-consequence contract. Decision-log #5: "primary" re-scoped to high-consequence only.
- **Component contracts**: financial value zone (label / value [English numerals, tabular mono, bidi-isolated, end-aligned] / unit [`د.أ`/`دأ` outside the number] / period / delta); three honest voids (unrecorded → action chip "سجّله"; unavailable → "غير متاح"; measured zero → "0" + label); period chip (36px visual / 44px hit, staged until applied); operational-row grid (identity lead, wrapping Arabic title/caption, one-word + marker state slot, stable trailing amount slot, optional ≤3px inline-start stripe always paired with the state word, inset dividers); selection grammar (2px `#C96442` edge/underline + non-color cue; never automatic black fills).
- **States**: draft/pending/posted/failed/cancelled/reversed/reviewed/partial/due/overdue/unknown — word + non-color marker, color never alone; pending ≠ success; unknown ≠ failure; reversed preserves audit; save six-state frame (default / pressed-hold / focused / disabled / loading with aria-busy + duplicate guard / quiet completion); ELEU six distinctions (no-data / no-results / loading / failure / unknown / pending) with retry + input preservation.
- **Overlays**: sheet/dialog/menu/filter share warm surface + scrim + focus containment + one-active-modal; staging until Apply; destructive confirmation; timings.
- **Navigation shell**: 4 official destinations (الرئيسية / المالية / الطلبات / الأدوات), RTL, persistent bottom nav, restrained top area, FAB in its own gutter, current-destination clay edge.
- **Accessibility**: contrast table (ink pairs 17.50/18.43 AAA; clay 3.12 as non-text-only mark; edge 3.90; error 6.02), 44px targets, focus rules, 320px / 200% no overflow; physical-device + screen-reader testing explicitly **not claimed**.
- **Responsive geometry**: 320/360/390/430px; 100/130/200% text scale; RTL/LTR; logical properties; no horizontal overflow; FAB must not cover amount/action columns.
- **Inputs, data display, icons, motion, content, spacing**: field anatomy + amount entry (English digits, LTR in RTL) with product-owned currency/rounding; direct values first, relationship bars only when parts sum, question-led charts with data/zero/no-data/loading + mandatory text alternative; 43-glyph icon registry with mirror flags; motion timing table (entrances decelerate, exits accelerate, no count-up, reduced-motion collapse); Arabic-first Jordanian content rules with English numerals and `د.أ`/`دأ`; 4px spacing grid (4–32), radius table, elevation E1–E3.
- **Explicitly NOT owned**: product implementation; financial policy/formulas/sync/backend; period/time semantics (product-owned); currency/rounding policy; link-ink (owner decision); domain compositions ("the visual foundation must not invent product policy inside a primitive"); dark mode; chart library; new palette (gold retired permanently); Prototype-derived content; physical-device/screen-reader verification.

---

## 7. Coverage and gap matrix

Classifications are exactly one of: `fix now in planning` / `preserve` / `defer` / `needs owner decision` / `out of scope`. Gap types are from the mission's allowed set. "Std" = the Standard's coverage. Dependencies reference owner decisions D1–D13 (Section 16) and waves W0–W6 (Section 17).

| ID | Area | Evidence path/route | Current state | Standard coverage | Gap type | Classification | Recommended next step | Dependency | Risk | Acceptance criterion | Rollback boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-01 | Token namespace | `index.css` L9–144 vs `design-tokens.css` | 83 Micro names vs 120 Standard; 3 exact-name matches; ~60+ Std tokens unconsumed; zero `--vf-` refs | Full token contract exists | runtime token mapping | fix now in planning | Owner-ratified name+value mapping table + adapter block in Micro token layer | D1, D2 | Silent visual regressions | Every Std token mapped, diverged-with-reason, or marked not-adopted; guard extended | Delete adapter block |
| F-02 | Value drift, 7 shared roles | `index.css` vs `design-tokens.css` | ink `#1F1E1D`/`#141413`, clay `#CC785C`/`#D97757`, pressed, tint, divider, success `#256B4A`/`#629987`, danger `#B42318`/`#B53333` | Std is contract-of-record; Micro has S3-06 contrast rationale | runtime token mapping | needs owner decision | Decide adopt / keep-with-recorded-divergence / partial per role | D1 | Visual change on every surface | Documented per-role decision; contrast re-checked | Per-role token revert |
| F-03 | Micro-only color roles (~18) | `index.css` `:root` | teal accent family, warning family (gold retired in Std), withdrawal family, brand text/soft, tint hexes, text-strong | Std forbids new palette/tint hexes | product/owner decision | needs owner decision | Ratify as Micro extension, map to Std roles, or retire | D2 | Surfaces losing semantic cues | No surface loses its meaning cue | Per-role revert |
| F-04 | Dark mode | `index.css` `.dark` (46); `contexts/ThemeContext.tsx` | Live light/dark/system | None — no dark mode by design | not in Standard by design | needs owner decision | Keep as documented extension / freeze / remove | D3 | `:root`-only Std mapping silently drops dark | Dark parity preserved or consciously frozen | ThemeContext revert |
| F-05 | z-index literals + dual system | `index.css` literals + comment ladder L191; `drawer.tsx` z-50/z-[60] | Literals 1–60; z-70 reserved, unused; Tailwind second system | `--z-scrim/overlay/fab/snackbar` 250–500 | runtime token mapping | fix now in planning | Introduce `--z-*` vars; fold Tailwind z classes into guard | F-01 | Overlay stacking regressions | Single z source; guard green | Revert var block + allowlist |
| F-06 | Raw scrim | `index.css` L715 | Sanctioned `color-mix(#1f1e1d 45%)` | `--vf-scrim rgba(20,20,19,.45)` | runtime token mapping | fix now in planning | Elevate to token | F-01 | None (value-equivalent) | Scrim token consumed; guard updated | Single-line revert |
| F-07 | Type-scale/motion literals | `index.css` (no `--text-*`/`--motion-*` consumed) | Hundreds of literal font sizes / ms values | 11-step type scale + 10 motion durations + easings | runtime token mapping | defer | Fold into token adapter later | F-01 | Mass-edit churn if rushed | (deferred — no criterion yet) | (deferred) |
| F-08 | Doc/code palette drift | `docs/product/design-system-v1.md:37,39` vs `index.css:67,71` | success/warning hex differ (S3-06 fixes in code) | n/a | product/owner decision | needs owner decision | Set authority direction, then align the doc | D8 | Teams following stale doc | Doc and CSS assert identical values | Doc-only revert |
| F-09 | No primitives; 492 raw buttons | 84 files; `components/ui/` = drawer+tooltip | Hand-typed `micro-button*` class strings; typo = unstyled | Action classes are behavioral contracts | shared UI primitive | fix now in planning | Class-bridge Button first; adopt per-surface | W2 | Restyle churn; silent typos | No new hand-typed button strings in touched code | Per-surface revert |
| F-10 | Dead exports | `ui/tooltip.tsx`; `drawer.tsx` DrawerTrigger | Zero usages (only TooltipProvider used) | n/a | shared UI primitive | fix now in planning | Remove or deliberately adopt | W1 | None | No dead exports remain | Trivial revert |
| F-11 | No Toast/Snackbar | `App.tsx` Q-003; z-70 reserved | Deliberately removed | Snackbar contract exists (hold 5000ms) | shared UI primitive | needs owner decision | Reintroduce per Std or record removal as final | D5 | Re-adding noise to a quiet product | Decision recorded; z-70 used or de-reserved | Component-level revert |
| F-12 | No shared Confirm/Dialog | `AgreementEditor.tsx:325`; `SettingsOperatingModeSection.tsx:107`; `EstimateDetail.tsx:43`; `DraftEditor.tsx:111`; `Tools.tsx:164`; `QuickActionSheet.tsx:88` | Inline warning labels; bespoke per-page flows | High-consequence dialog contract | shared UI primitive | fix now in planning | Dialog primitive; port exact wording | F-09, D12 | Losing honesty wording in port | Every confirm keeps wording + independent confirmation path | Per-surface revert |
| F-13 | Tone unions + 15+ label maps | `SupplierPurchaseEditor.tsx:58`; `OwnerEntitlement.tsx:34`; `Schedule.tsx:947`; `OrderDetail.tsx:49`; `EventsLayer.tsx:22`; `DeliveryReview.tsx:40`; `Parties.tsx:17` | Per-page ad-hoc state presentation | 11-state presentation matrix | shared UI primitive | fix now in planning | Status/Chip primitive + central state matrix | F-01, F-02, D11 | Wrong state presentation | All states word+marker from one matrix | Per-feature revert |
| F-14 | Markers inconsistent | `micro-status-chip` (index.css:250) | Words universal; non-color markers ad-hoc | word + non-color marker required | shared UI primitive | fix now in planning | Marker set per state | D11 | Color-only reliance (a11y) | Every state has a non-color marker | Chip-level revert |
| F-15 | Sheet skins split | QAS + `MaterialSheet.tsx:44` vs `RepaymentSheet.tsx` | 3 sheets, 2 skins (one raw DrawerContent) | Sheet contract + timings | shared UI primitive | fix now in planning | Sheet primitive over vaul + `micro-bottom-sheet` | F-05 | Motion/skin divergence | One sheet skin; z from tokens | Per-component revert |
| F-16 | Currency-unit duplication | `presentation/formatters.ts:57` vs OrderDetail (22 manual `د.أ`) | Single source exists; ~12 files concatenate manually | Unit slot in value zone | shared UI primitive | fix now in planning | CurrencyUnit/Amount + lint rule | F-09 | Unit drift | Zero manual unit concatenations in touched files | Per-file revert |
| F-17 | Icon registry vs lucide | gallery 43-glyph sprite vs lucide imports | Lucide superset in use | 43-glyph registry + mirror flags | product/owner decision | needs owner decision | Adopt registry or keep lucide + mirror rules | D6 | Mirroring errors in RTL | Mirror-flag rule enforced | Per-icon revert |
| F-18 | Shell chrome clean | `MicroAppShell.tsx` (122L); `AppHeader.tsx` (61L); `BottomNav.tsx` (71L) | Centralized, class-styled, keyboard/safe-area aware | Nav shell contract aligns | AUX shell | preserve | Keep as integration anchor | — | — | — | — |
| F-19 | Finance flows in AUX sheet | `QuickActionSheet.tsx` (761L) | Sale/expense forms inside shell layer | n/a (product concern) | AUX shell | fix now in planning | Split forms → `components/finance/`; chrome + dispatch stays; `QuickAction` type preserved | W4 | Draft keys `sheet-expense-*`, prefetch, idempotency, tests | All QAS tests green post-split | Single-move revert |
| F-20 | Nav labels diverge | `navigation.ts:14–17` vs `navigation-shell.md:3` | مشروعي الآن / العمل / سجّل(FAB) / مالي / أدواتي vs الرئيسية / المالية / الطلبات / الأدوات | Official 4 destinations fixed | AUX shell | needs owner decision | Adopt Std labels or keep Micro set | D4 | Wayfinding confusion for the owner | `navigation.test.ts` updated; owner sign-off | Label-only revert |
| F-21 | Route knowledge ×4 | `MicroRouter` + `routeClassifier` + `navigationContract` + `navigation` + sync test | Deliberate quadruplication, guarded | n/a | AUX shell | preserve | Keep + sync test | — | — | — | — |
| F-22 | Legacy fallback key | `navigationContract.ts:143`; `routeKnowledgeSync.test.ts:270` | Keys deleted route literal; intentional + tested | n/a | AUX shell | preserve | Keep documented | — | — | — | — |
| F-23 | `/review` redirect | `MicroRouter.tsx:151` | Legacy redirect to `/finance` | n/a | screen composition | defer | Remove in later cleanup | — | — | — | — |
| F-24 | 15 feature patterns, 13 referenced | See §13 hosts | Working reference implementations exist for 13 of 15 | Slot contracts available | Micro feature pattern | fix now in planning | Consolidate as Layer-5 patterns (migration) | W3 | Regressions in migrated surfaces | Pattern parity tests green | Per-pattern revert |
| F-25 | Charts absent | No chart code/dep/markup; feeders: `statementService`, `projectFinancialService`, `readPeriodWaste` | Textual reports only | Question-led chart contract (greenfield) | Micro feature pattern | needs owner decision | Scope which questions charts answer | D10 | Misleading data presentation | Chart states data/zero/no-data/loading + text alternative | Feature-flag revert |
| F-26 | Staged filter/period chip absent | `FinanceActivity` FAMILY_FILTERS; `CorrectionsLayer` chips; `Statement` ranges | Filters apply immediately; no 36/44 chip | Period chip + staging contract | Micro feature pattern | fix now in planning | Build staged filter surface + period chip (semantics product-owned) | F-13 | Accidental premature application | Staged-until-applied verified | Per-surface revert |
| F-27 | No sort UI | Grep-verified across surfaces | No sort controls anywhere | n/a (product choice) | product/owner decision | needs owner decision | Decide product need | D9 | — | Decision recorded | — |
| F-28 | Page-local panels vs overlays | OrderDetail panels; Finance layers; Schedule capacity | In-flow expandable layers | One-active-modal overlay system | product/owner decision | needs owner decision | Migrate to overlays or ratify in-flow pattern | D12 | Focus/scroll behavior changes | Owner sign-off per surface | Per-surface revert |
| F-29 | Loading is text | `.micro-route-loading` (index.css:354) | Text loading, no skeletons | Skeleton timing contract (`--motion-skeleton 1.5s`) | Micro feature pattern | needs owner decision | Skeleton vs honest text (lean defer) | D13 | Perceived-performance regressions | Owner sign-off | Per-surface revert |
| F-30 | Honest voids + state words implemented | `Home.tsx`; `Finance.tsx`; `InventoryMaterials.tsx`; `WalletLedger.tsx`; `EventsLayer.tsx`; `ActualMaterialPanel.tsx` | Mature, tested (unrecorded/unavailable/zero; pending≠success; idempotency copy) | Matches Std contract exactly | Micro feature pattern | preserve | Keep; unify presentation only | F-13 | — | — | — |
| F-31 | Oversized pages | OrderDetail 1412; OwnerEntitlement 1096; FinancialEventEditor 1055; Schedule 1028; Finance 988; DirectSaleEditor 974; SupplierPurchaseEditor 965; InventoryMovementEditor 947; Catalog 924 | 9 pages >900 lines; Schedule/Finance ≈ single 1,000-line JSX | n/a | screen composition | needs owner decision | Set split cadence; decompose opportunistically | D7 | Journey regressions | Page tests green post-split | Per-page revert |
| F-32 | `order/` vs `orders/` | `components/order` (3 files) vs `components/orders` (1 file) | Two dirs, one feature, one consumer | n/a | screen composition | fix now in planning | Single documented move | W6 | Import churn | ARCHITECTURE.md extraction map updated | Single-move revert |
| F-33 | Storage type imports | 19 files type-import `@/storage/local`; `eslint.config.js:132–162` | Types leak storage vocabulary; value imports blocked (2 legitimate) | n/a | screen composition | fix now in planning | `application/*/types.ts` re-export shim | W6 | None (type-only) | Zero UI imports of storage paths | Shim deletion |
| F-34 | Dead CSS | ~27 candidates; 7 verified (micro-eyebrow, -intent-card, -period-truth, -review-empty, -truth-banner, -guidance-grid, -material-row) | Unreferenced classes; dynamic classes exist (`FinanceActivity.tsx:110`) | n/a | runtime token mapping | fix now in planning | Delete only after class-existence guard runs | W1 | Dynamic-class false positives | Guard green; zero visual change | CSS-only revert |
| F-35 | Duplicate/conflicting CSS rules | `.micro-button-block` ×3 (L1756/1948/2200); `.micro-button-quiet` ×2 conflicting (L3243 vs L4326); `.micro-number` ×3; `.micro-sheet-title` ×2; `.micro-home-heading` ×3 | Cascade silently decides; live conflict on quiet button | n/a | runtime token mapping | fix now in planning | Cascade-audited dedupe (preserve 44px min-height) | W1 | MR-03 touch-target regression | 44px preserved; visual diff clean | Per-rule revert |
| F-36 | Guard suite gaps | `scripts/*` + app guards | Strong: hex ban, layer boundaries, cycles, entity touchpoints, text density. Missing: dead CSS, duplicate selectors, TSX↔CSS existence, docs↔CSS sync, primitive reuse | n/a (Micro-side enforcement) | runtime token mapping | fix now in planning (extend) | Add the five missing checks as guards | W1 | False positives (allowlist) | New guards green on current tree | Guard-only revert |
| F-37 | Domain purity + composition root | `src/domain/**` relative-only; `PrototypeServicesContext.tsx` (~44 services) | Verified pure; money policy out of pages | n/a (by design) | out of scope | preserve | Keep untouched | — | — | — | — |
| F-38 | Under-covered surfaces healthy | Setup 427L; Foundation 246L; NotFound 17L; SharePreview 106L; Profile 337L; AgreementEditor 455L; Settings 621L; pwa/*; lock veils | All exist, dom-tested, honest-voids reference in Setup | Slot contracts available | screen composition | preserve | Fold into pattern consolidation | F-24 | — | — | — |
| F-39 | Prototype boundary | `decision-log.md` #13 | Prototype excluded from acceptance | n/a | not in Standard by design | preserve | Standing constraint | — | — | — | — |
| F-40 | Docs authority ladder | `design-system-v1.md:3`; `AGENTS.md`; `ARCHITECTURE.md`; `mobile-ui-ux-reference-v1.md` §6 self-cancelled | Multiple claimants; unenforced vs index.css | n/a | product/owner decision | needs owner decision | One named authority per category | D8 | Teams following stale docs | Authority ladder documented and linked from AGENTS.md | Doc-only revert |

---

## 8. Read-only Structure/Architecture/Code Organization Scan (UI/AUX/design-system boundary only)

Every finding classified exactly one of `fix now in planning` / `preserve` / `defer` / `needs owner decision` / `out of scope`. Nothing was classified "fix now in code" — no code was changed.

### 8.1 The nine required areas

1. **Module and feature boundaries.** Feature surfaces are spread across `pages/` + `components/<feature>/` + `application/<feature>/` + `src/domain/<feature>/` with inconsistent naming (`order` vs `orders`; `cost` vs `catalog`). Navigation knowledge is centralized and sync-tested (good). Classification: **fix now in planning** (a rename/merge plan only — F-32).
2. **File responsibilities and oversized files.** `index.css` (6,962 lines) is tokens + components + pages in one file; `QuickActionSheet.tsx` (761 lines) is chrome + finance feature; 9 pages exceed 900 lines, with `Schedule.tsx` and `Finance.tsx` being near-single-JSX monoliths (~1,000-line return blocks). Classification: oversized-file cadence **needs owner decision** (D7); page decomposition **defer**; sheet split **fix now in planning** (F-19).
3. **Dependency and layer violations.** 19 files type-import from `@/storage/local` (ESLint blocks value imports; 2 legitimate value imports at the composition root). Domain layer verified pure (relative imports only; no React/CSS/browser globals; D-02 Math ban enforced). The one real layering violation is QuickActionSheet's embedded finance flows. Classification: type-shim + sheet split **fix now in planning** (F-33, F-19); domain purity **preserve** (F-37).
4. **Cycles and guard limitations.** Runtime value-import cycles: clean (`check-runtime-cycles.mjs`); one intentional type-only cycle is documented. Guard gaps: no dead-CSS detection, no duplicate-selector detection, no TSX↔CSS class-existence check, no docs↔CSS sync check, no primitive-reuse rule (492 raw buttons are legal). Classification: existing detectors **preserve**; the five missing checks **fix now in planning** (F-36).
5. **Duplication and competing sources of truth.** Intra-CSS duplicates including one **live conflict** (`.micro-button-quiet`: L3243 supplies 44px min-height, L4326 silently wins color); 492 hand-typed button class strings; per-page tone unions (≥3 different ad-hoc unions); 15+ status-label `Record` maps; ~12 files manually concatenate `د.أ` beside a single-source formatter; 4 distinct confirm/sheet mechanisms; dual z-index systems; doc/code palette drift. Classification: **fix now in planning** (F-35, F-09, F-13, F-16, F-15); docs authority **needs owner decision** (D8).
6. **Feature discoverability.** Route-level discoverability is excellent (4 synced files + tests). CSS-level discoverability is poor: feature styling is findable only by prefix archaeology in one giant file (`micro-finance` ×77, `micro-home` ×76…). Classification: navigation **preserve**; CSS discoverability **defer** (improves naturally as primitives absorb classes).
7. **Storage/application/domain/UI composition.** Strong: services composition root wires ~44 services; all pages access data via `usePrototypeServices()`; pages display but never compute money; presentation utilities own formatting; domain owns policy. Classification: **preserve** (F-37) — this is the integration anchor.
8. **Test and documentation mapping.** Test families (27 dom journeys, 12 ui acceptances, css test, navigation sync tests, guard scripts, exact-value tests) cover behavior and tokens well, but not CSS hygiene or docs consistency. Docs: `design-system-v1.md` claims authority while drifting from code; `mobile-ui-ux-reference-v1.md` partially self-cancels; `ARCHITECTURE.md` defers to `product-source-of-truth.md`. Classification: tests **preserve**; docs authority **needs owner decision** (D8).
9. **Target module map.** Provided in Section 10, clearly as a proposal. Classification: execution **out of scope** for this task.

### 8.2 Propagation failure points (where a single change would NOT propagate today)

- **z-index**: literals at 6+ sites plus a comment ladder plus `drawer.tsx` Tailwind classes outside the ladder — changing the ladder comment changes nothing.
- **Font sizes / motion**: literal on-scale values across hundreds of declarations; a scale change means mass edits plus a guard-set change.
- **`.micro-button-quiet` / `.micro-number` / `.micro-sheet-title` / `.micro-home-heading`**: duplicated definitions — editing one copy silently loses to cascade order.
- **Buttons**: a restyle touches 9 interleaved CSS sections (L433–5477) while 492 call sites hand-type class strings with no existence check (a typo renders unstyled).
- **Sheets/confirms**: a behavior change must touch 3 sheet components + inline confirm labels across pages.
- **Status presentation**: a tone or wording change requires editing every page's bespoke map/union.
- **Currency unit**: `د.أ` changes must chase ~12 files of manual concatenations despite `formatMoneyWithUnit` existing.
- **Elevation**: tokens duplicated between `:root` and `.dark`.
- **Dark mode**: a Standard token overlay mapping only `:root` silently drops `.dark` values.

---

## 9. Source-of-truth matrix

| Category | Current source(s) | Conflict / drift | Authoritative after integration | Notes |
|---|---|---|---|---|
| Palette values | `index.css` `:root`/`.dark` (61+46 defs) vs `docs/product/design-system-v1.md` palette table | Yes — success/warning hex differ (code cites S3-06 contrast fixes) | **Micro Standard `design-tokens.css`** as contract of record; Micro runtime token mapping as implementation authority; docs downstream (D1/D8) | Value drift on 7 shared roles needs an explicit owner decision |
| Token names | `index.css` `--color-*`/`--space-*`/`--radius-*` (83 unique) | Namespace distance from `--vf-*` (3 exact intersections) | **Runtime token mapping layer** (adapter in Micro token files) renaming/mapping Standard names to Micro-consumable variables | No removals before the adapter exists |
| Component styles | `index.css` `.micro-*` classes (~438 unique) + hand-typed strings in 84 files | Internal duplicates + one live conflict | **Shared UI primitives** (`components/ui/`) owning behavior; `micro-*` classes become the bridge the primitives render | Class-bridge so CSS need not change first |
| State presentation | Per-page tone unions + 15+ label maps + `data-state/status/effect` attributes | Duplicated, inconsistent markers | **Central state matrix** (Status/Chip primitive) mapping domain enums to Standard presentations | `data-*` attributes are a clean existing hook |
| Money & currency | `presentation/formatters.ts` (`formatMoneyMinor`, `formatMoneyWithUnit`) | ~12 files bypass with manual `د.أ` | **formatters.ts stays authoritative**, wrapped by Amount/CurrencyUnit primitives + lint | Single source already exists — enforce it |
| Dates | `formatters.ts` (Asia/Amman, DD/MM/YYYY) + `LocalDateField` | None observed | **Unchanged** | Preserve |
| Routes | 4 synced files + `routeKnowledgeSync.test.ts` | Deliberate quadruplication, guarded | **Unchanged (preserve)** | Sync test is the enforcement |
| Nav labels | `navigation.ts:14–17` | Diverges from Standard's official 4 | **Owner decision (D4)** then one file | `navigation.test.ts` asserts labels |
| Patterns | Scattered across pages/components (13 of 15 with references) | Implicit, undocumented as patterns | **Layer-5 feature patterns** colocated with features | Migration, not invention |
| Pages | `pages/` (52 components) | Oversized but single-purpose | **Unchanged (composition-only rule)** | No new tone unions/label maps/button strings |
| z-index / geometry / motion / type scale | Literals + comment ladder + shell CSS | Two z systems; no motion/type tokens | **Standard tokens via runtime mapping** (`--z-*`, `--text-*`, `--motion-*`) | Std fills a vacuum rather than conflicting (except z) |
| Docs | `design-system-v1.md`, `placement-principles-v1.md`, `mobile-ui-ux-reference-v1.md`, `ARCHITECTURE.md`, `AGENTS.md` | Authority overlap; one self-cancelled section | **One documented authority ladder (D8)**: Standard = contracts; token mapping = implementation; docs = guidance | Add docs↔CSS sync guard |

---

## 10. Target module map — **PROPOSED, NOT EXECUTED**

This is a proposal only. Nothing was moved, renamed, created, or deleted. The map satisfies the fixed strategy with minimal motion and explicit boundary adapters; every step is separately revertable.

| Layer | Proposed home | Current state | Adapter required |
|---|---|---|---|
| L1 Micro Standard (visual contracts) | Stays external: `Documents/micro-standard-v2` | Already exists | None — consumed as contract + `design-tokens.css` |
| L2 Runtime token mapping | Keep `index.css` `:root`/`.dark` as the adapter target; add a `design/tokens.css` mapping block (Standard aliases alongside Micro names — **no removals**); add `--z-*` variables; elevate the scrim to a token | Tokens exist but names/values diverge | Owner-ratified name+value mapping table; `design-token-guards.py` allowlist update |
| L3 Shared UI primitives | Grow `components/ui/`: `Button` (class-bridge rendering existing `micro-button*` classes), `Field` (wraps `micro-field` + English inputs), `Surface` (from `InfoCard`), `Row`, `Status`/`Chip` (absorb tone unions + label maps + markers), `Sheet` (unify vaul + `micro-bottom-sheet` skin), `Dialog` (absorb inline confirms), `Amount`/`CurrencyUnit` (wrap `MoneyValue` + `formatters.ts` unit), `Icon` (lucide pass-through + mirror rules) | Only drawer/tooltip exist today | Class-bridge pattern; shared tone/status TS types exported from one module |
| L4 AUX shell | Keep `components/layout/` (MicroAppShell, AppHeader, BottomNav); shrink QuickActionSheet to chrome + dispatch; move sale/expense forms to `components/finance/QuickSaleForm.tsx` + `QuickExpenseForm.tsx` | Shell clean; QAS overweight | `QuickAction` type stays exported from shell; draft keys + prefetch preserved |
| L5 Feature patterns | Colocate with features; merge `components/order/` + `components/orders/` → `components/orders/`; feature tone/label maps move beside features or to `presentation/` | 13 of 15 patterns have working references | Pattern parity tests before/after each migration |
| L6 Screens | `pages/` stays composition-only; rule (guarded): no new tone unions, label maps, or button class strings in pages | 9 oversized pages | None — decomposition deferred to owner-set cadence |
| L7 Domain/application/storage | Untouched | Verified pure | None |

**Boundary adapters (the controlled seams):** storage-type re-export shim (`application/*/types.ts` re-exporting `storage/local/types`); z-token layer folding in the Tailwind classes; Button class bridge; docs updated to point at primitives instead of raw classes.

---

## 11. What transfers from the Standard (covered immediately on adoption)

- **Token contracts**: the 18-value approved palette and named roles, surface/ink ladders, control geometry, radii, elevation set, motion timings, z-layers, scrim/translucent-header derivatives, fonts — via the runtime token mapping (F-01). Geometry, elevation, fonts, and radii are essentially already aligned (near-zero-cost adoption); the color roles are the part requiring owner decisions (F-02/F-03).
- **Action classes**: create/FAB clay, ordinary save with pressed edge, high-consequence commit, destructive — presentation binds via tokens; the *behavioral* parts (six-state save frame, duplicate guard, quiet completion, independent confirmation path) land in the Button/Dialog primitives (F-09/F-12).
- **Selection grammar**: 2px clay edge + non-color cue for chips/segments/nav-current — Micro already uses edge stripes (~30 `border-inline-start` sites) but not the chosen/current grammar for selection (F-13/F-14).
- **State presentation matrix**: the 11-state word+marker grammar maps onto Micro's existing `data-state/status/effect` attributes and state words; the missing piece is the central matrix + markers (F-13/F-14).
- **Value-zone slots, honest voids, period chip, operational-row slots**: presentation contracts Micro's screens can consume immediately — Home `FactCard`, Finance `PositionCard`/`Metric`, Orders/FinanceActivity rows already implement most slots informally; the period chip and staged-Apply filter surface are the new builds (F-24/F-26).
- **Overlay system**: scrim, staging, one-active-modal, timings — binds to the Sheet/Dialog primitives and the z-token layer (F-05/F-12/F-15).
- **Navigation shell geometry**: persistent bottom nav, restrained header, FAB gutter, safe areas — Micro's shell already matches structurally (F-18); only labels diverge (F-20).
- **Accessibility constraints**: contrast pairs, 44px targets, focus rules, 320px/200% no-overflow, reduced-motion collapse — mostly direct where tokens map (F-02 decides the color bindings).
- **Typography scale, icon mirroring rules, content language rules (`د.أ`/`دأ`, English numerals, bidi isolation)**: transfer as tokens/conventions; Micro's practice already conforms on content rules (F-30).

## 12. What remains Micro-specific (must not be flattened into generic components)

- The **15 Feature Patterns** (Section 13) — Micro's operational grammar: correction flows with idempotency and family-owner routing, read-only registry layers, restatement disclosure, pre-save computation review, decision surfaces, order-detail composition, inventory knowledge rows, count-compare-settle, collect-with-source, distribution, tool results, scheduling buckets + capacity, party ledger, home control-center.
- **Honest-void semantics wiring**: which data condition yields unrecorded / unavailable / measured-zero is product-owned (Standard covers presentation only).
- **Knowledge-state vocabulary**: Micro's `incomplete` / `needs_review` / `unconfirmed` / `estimated` mapping to Standard words is a product decision (D11).
- **Period/time semantics**: which ranges exist and their defaults (Standard explicitly product-owned).
- **Arabic product copy** everywhere (resultFeedback texts, confirm wording, idempotency messages) — the Standard's content guidelines constrain language conventions, not wording.
- **Dark mode** (pending D3), **Micro-only color roles** (pending D2), **nav labels** (pending D4) — until decided, these stay exactly as they are.
- **Domain, application, storage layers** — untouched by this integration entirely (F-37).

## 13. What is missing and where it should live

| Missing piece | Where it should live | Status |
|---|---|---|
| Runtime token mapping (name+value adapter, `--z-*`, scrim token) | L2 — Micro token files (`index.css` `:root`/`.dark` or `design/tokens.css`) | Build (F-01/F-05/F-06) |
| Button, Field, Surface, Row, Status/Chip, Sheet, Dialog, Toast?, Icon, Amount, CurrencyUnit | L3 — `components/ui/` | Build as class-bridges (F-09 et al.) |
| QuickActionSheet split (forms out of shell) | L4 chrome stays; forms → L5 `components/finance/` | Split (F-19) |
| Period chip + staged-Apply filter surface | L5 feature pattern (hosts: `FinanceActivity`, `CorrectionsLayer`, `Statement`) | Greenfield (F-26) |
| Question-led simple chart | L5 feature pattern (feeders: `statementService`, `projectFinancialService`, `readPeriodWaste`) | Greenfield, owner-scoped (F-25) |
| Central state matrix + non-color markers | L3 primitive + product-owned enum mapping | Build (F-13/F-14) |
| Skeleton loading (vs honest text) | L3/L5 | Owner decision (F-29) |
| Sort controls | L5 | Owner decision — may be intentionally absent (F-27) |
| Toast/snackbar | L3 | Owner decision — currently deliberately removed (F-11) |
| Guard extensions (dead CSS, duplicate selectors, class existence, docs sync, primitive reuse) | Micro guard scripts | Build (F-36) |
| `order/`+`orders/` merge, storage type shim | L5/L6 structure | Plan, single moves (F-32/F-33) |

## 14. What must be preserved (product-specific value)

- The **AUX shell** as-is (MicroAppShell, AppHeader, BottomNav, route classification, keyboard/safe-area/clearance behavior) — the cleanest layer in the repo (F-18).
- **Honest-void rendering, state words, pending≠success, idempotency copy, "لا يُعرض صفر مكان المجهول"** and all exact-value behavior (F-30; enforced by `exact-values.*` tests).
- **`presentation/formatters.ts`** as the single money/date/currency source; `DisplayValue`'s bidi/LTR walls (index.css:4446 "A2 presentation contract").
- **`EnglishNumberInput` / `EnglishQuantityInput` / `LocalDateField`** — they already satisfy the Standard's input contract nearly fully.
- **`UnsavedChangesGuard`** — a staged-decision overlay more complete than the Standard's one-line claim (301 lines, history sentinel, beforeunload, PWA dirty bridge).
- **Domain purity, the services composition root, ESLint layer guards, the existing guard scripts** (F-37) — the integration anchor.
- **Route-knowledge quadruplication with its sync test** (F-21/F-22) — deliberate and guarded.
- **The full UI test families** (27 dom journeys, 12 ui acceptances, css test, navigation tests, docs-consistency, exact-value tests).
- **Quiet-completion discipline** (no toasts by default), guard-verified token hygiene (hex ban), and text-density budgets.

## 15. What must be rejected or ignored from Prototype v0

Per the Standard's own decision-log #13 ("the Prototype remains visual evidence only. It is not a source for Micro product copy, domain behavior, routes, or Final Copy acceptance"):

- **No Prototype labels, numbers, categories, fake interactions, routes, or business logic** may enter Micro through this integration. The five agents' justifications were traced: none relied on Prototype content.
- **The gallery's English demo copy must never become product copy**; the gallery is a contract demonstration, not a terminology source.
- **Gallery JavaScript is evidence, not production code**: its focus trap, scroll lock, and drag-dismiss behaviors demonstrate contracts but must be reimplemented in Micro's shared primitives/AUX shell under Micro's own tests.
- **Stale internal measurements are not current truth**: e.g., `docs/inventory/05-unreachable.md` lists capabilities that were later surfaced (F-078 now lives in Home's "اليوم" section) — point-in-time inventories must be re-verified before use.
- **Superseded docs** (`mobile-ui-ux-reference-v1.md` §6.1/6.2/6.4 self-cancelled sections) must not be cited as authority.

## 16. Owner decisions required (blocking implementation)

| # | Decision | Options (evidence) |
|---|---|---|
| D1 | **Value drift on 7 shared color roles** (F-02) | (a) adopt Standard values everywhere; (b) keep Micro values with recorded divergence rationale (S3-06 contrast work); (c) partial, a11y-driven per role |
| D2 | **Micro-only color roles (~18)** (F-03) | ratify as Micro extension / map to Standard roles / retire (warning family = retired gold in Standard) |
| D3 | **Dark mode** (F-04) | keep as documented extension / freeze / remove (Standard has none) |
| D4 | **Navigation labels** (F-20) | Standard's four (الرئيسية/المالية/الطلبات/الأدوات) / keep Micro's five-seat set (مشروعي الآن/العمل/سجّل/مالي/أدواتي) |
| D5 | **Toast/snackbar** (F-11) | reintroduce per Standard contract / record removal as final |
| D6 | **Icon registry** (F-17) | adopt 43-glyph registry / keep lucide superset + mirror rules |
| D7 | **Page-split cadence** (F-31) | set a cadence for decomposing the 9 oversized pages / defer indefinitely |
| D8 | **Docs authority + drift direction** (F-08/F-40) | name one authority per category; decide whether code or doc wins the two drifted hex values |
| D9 | **Sort controls** (F-27) | product need or intentionally absent |
| D10 | **Charts scope** (F-25) | which questions the first charts answer (natural feeders: statement, project financials, period waste) |
| D11 | **State marker + word mapping** (F-13/F-14) | which non-color marker per state; map Micro knowledge vocabulary (incomplete/needs_review/unconfirmed/estimated) to Standard words |
| D12 | **Overlay vs in-flow panels** (F-28) | migrate OrderDetail/Finance/Schedule expandable layers to the overlay contract or ratify in-flow as a Micro pattern |
| D13 | **Loading style** (F-29) | skeletons vs honest text (current text style is defensible; lean defer) |

## 17. Minimum safe remediation waves (after owner acceptance)

Each wave is independently revertable, requires no bulk moves, and changes no financial semantics. Dependencies reference the decisions above.

| Wave | Content | Depends on | Risks | Acceptance criteria | Rollback boundary |
|---|---|---|---|---|---|
| **W0 — Decisions & mapping (no code)** | Owner resolves D1–D13; produce the token name+value mapping table (F-01); confirm wave order | — | Decisions made on stale info (mitigated by this report's evidence) | Signed decision list + ratified mapping table | n/a |
| **W1 — Guard hardening + CSS hygiene** | Add class-existence, duplicate-selector, docs↔CSS sync checks; delete the 7 verified-dead classes (more only per guard output); cascade-audited dedupe of triplicated rules; remove dead tooltip primitives/DrawerTrigger | W0 | Dynamic-class false positives (allowlist); MR-03 touch-target regression in quiet-button dedupe | New guards green; visual diff shows 44px min-height preserved on quiet buttons | Pure CSS/guard revert; independent of all other waves |
| **W2 — Token adapter** | Add `--z-*` vars; elevate scrim to token; add owner-approved Standard aliases alongside Micro names (**no removals**); update guard allowlist | W0 (D1–D4) | Silent visual regressions; `.dark` dropped if mapping covers `:root` only | Zero visual diff where values unchanged; drift only where the owner approved it; dark parity intact | Delete the adapter block |
| **W3 — Core primitives** | Button (class-bridge), Status/Chip (absorb tone unions + label maps + markers per D11), Amount/CurrencyUnit (+ lint); adopt in new code + 2–3 pilot surfaces | W2 | Pilot regressions | Pilot surfaces pixel-stable; no new tone unions/label maps/button strings in touched code | Per-surface revert; primitives unused elsewhere are inert |
| **W4 — Sheet/Dialog unification** | Sheet primitive over vaul + `micro-bottom-sheet` with z tokens; re-skin RepaymentSheet; Dialog absorbs inline confirms with **exact wording port** | W2, D12 | Losing confirm wording/honesty states; focus/scroll behavior changes | Every confirm keeps its wording + independent confirmation path; one sheet skin | Per-component revert |
| **W5 — QuickActionSheet split** | Forms → `components/finance/QuickSaleForm` + `QuickExpenseForm`; chrome + dispatch stays in L4; preserve draft keys, prefetch, idempotency; update tests | W4 | Breaking draft persistence (`sheet-expense-*`), offline prefetch, quiet-discard guard | All QuickActionSheet guard/category/journey tests green post-split | Single-move revert |
| **W6 — Structure & patterns** | `order/`+`orders/` merge; storage type shim; L5 pattern consolidation (13 migrations); charts + staged filters **only** per D10 scope | W3, D9/D10/D12 | Regression in migrated surfaces | Pattern parity tests green per migration; zero UI imports of storage paths | Each item independent; per-pattern revert |

**Wave order rationale:** W1 is safest and unlocks safe CSS work; W2 must precede any visual adoption; W3 must precede W4/W5 (primitives are their building blocks); W6 is last because it migrates working code and benefits from all prior safety nets. Nothing in any wave touches `src/domain`, financial formulas, posting, permissions, or sync.

## 18. Recommended next step

1. **Accept this report as the planning baseline** and place it in the Documents repository at the intended location (`planning/micro-standard-v2-micro-integration-comparison-2026-09/`) through the owner's own upload process — this task was forbidden from writing.
2. **Run W0 now**: answer the thirteen decisions (D1–D13) and ratify the token mapping table. Everything else is blocked on these; nothing else is blocked on anything outside this list.
3. **Execute W1 first** (guards + verified-dead/duplicate CSS cleanup): it is independent of all color decisions, produces the safety net every later wave needs, and is revertable in isolation.
4. **Re-verify SHAs before implementation begins.** This report is pinned to Micro `c0469e2` and Documents `864263c`; if either repository moves, re-run the affected verification rather than assuming stability.
5. **Do not start with the token adapter or any color change** — D1–D4 must be settled first, or visual regressions will be attributed to the Standard rather than to undecided mappings.

---

## Appendix A — Evidence index (primary citations)

**Micro repository** (`main @ c0469e265f24c70427eb7826dee717be117cff87`, paths under `apps/prototype-web/client/src/` unless noted):

- Router & navigation: `app/MicroRouter.tsx`; `app/routeClassifier.ts`; `app/navigationContract.ts` (fallback key L143; dangling comment L199); `app/navigation.ts` (labels L14–17); `app/routeKnowledgeSync.test.ts` (L270); `app/useReturnNavigation.ts`; `app/StartupGate.tsx`; `app/resultFeedback.ts`; `app/PrototypeServicesContext.tsx` (composition root, L53).
- Shell: `components/layout/MicroAppShell.tsx` (122L); `AppHeader.tsx` (61L); `BottomNav.tsx` (71L); `QuickActionSheet.tsx` (761L; finance imports L22, L91, L111; `micro-bottom-sheet` L393).
- Overlays: `components/ui/drawer.tsx` (z-50/z-[60] at L28/L48); `components/ui/tooltip.tsx` (dead primitives); `components/forms/UnsavedChangesGuard.tsx` (301L); `components/security/AppLockGate.tsx`; `DataActionPinGate.tsx`; inline confirms at `pages/AgreementEditor.tsx:325`, `components/settings/SettingsOperatingModeSection.tsx:107`; bespoke confirms at `pages/EstimateDetail.tsx:43`, `pages/DraftEditor.tsx:111`, `pages/Tools.tsx:164`, `QuickActionSheet.tsx:88`.
- Shared: `components/presentation/DisplayValue.tsx`; `InfoCard.tsx`; `DecisionPanel.tsx`; `EventEffectPreview.tsx`; `ActualTimePanel.tsx`; `components/forms/*` (EnglishNumberInput, EnglishQuantityInput, LocalDateField, useFormDirty, useFormDraft, FormDraftRestoreBanner); `presentation/formatters.ts` (L57 `formatMoneyWithUnit`); `presentation/activityLabels.ts`; `orderAgreementPresentation.ts`; `contexts/ThemeContext.tsx`.
- Feature components: `components/finance/` (EventsLayer L22 label map; CorrectionsLayer; DepositsLayer; FinancePeriodResultSection; CorrectionPreview; AllocationReviewCard; G5DecisionPanel; RestatementNote); `components/order/` (3 files) vs `components/orders/OrderDepositPanels.tsx`; `components/catalog/` (5 sections); `components/cost/MaterialSheet.tsx` (L44 skin); `components/loans/RepaymentSheet.tsx`; `components/owner/`; `components/security/`; `components/settings/`.
- Pages (52): including Home, Setup (427L), Foundation (246L), Orders, NewDraft, DraftEditor, AgreementEditor (455L), CostEditor, OrderDetail (1412L; 22 manual د.أ; label map L49), DeliveryReview (label map L40), DirectSaleEditor (974L; tone union), Schedule (1028L; tone union L947), ScheduleEditor, Finance (988L), Statement, FinanceActivity (FAMILY_FILTERS; dynamic classes L110), FinancialEventEditor (1055L), OwnerWithdrawalEditor, OwnerEntitlement (1096L; tone union L34), G5DeclarationEditor, CashWallets, CashWalletEditor, WalletLedger, CashOpeningLaterEditor, CashAdjustmentEditor, CashTransferEditor, CashDistribution, CashCount, CashReversalEditor, Collect, InventoryMaterials, MaterialEditor, InventoryMovementEditor (947L), InventoryReversalEditor, Catalog (924L), Tools, CostCalculator, EstimateDetail, ToolsIntegrity, Assets, AssetEditor, AssetDetail, Loans, LoanEditor, LoanDetail, Suppliers, SupplierPurchaseEditor (965L; tone union L58; CorrectionPreview at L142/479/621/756), Parties (label map L17), SharePreview (106L), Settings (621L; inline lock overlay L581–601), Profile (337L), NotFound (17L).
- CSS & tokens: `index.css` (6,962L; `@theme inline` L9–31; `:root` L33–96 = 61 props; `.dark` L98–144 = 46; z-comment L191; header L188–190; clearance L296–298; keyboard L774–778; nav L797; FAB L828; route loading L354; status chip L250; scrim L715; duplicates at L883/890, L1756/1948/2200, L1812/2064/2589, L3243 vs L4326; A2 bidi contract L4446; nav math L3949; lock veils L6889/6898).
- Guards & config (repo root): `scripts/design-token-guards.py` (Z_LADDER L38); `scripts/check-layer-boundaries.test.mjs`; `scripts/check-runtime-cycles.mjs`; `scripts/check-test-focus.mjs`; `scripts/check-entity-touchpoints.mjs`; `scripts/text-density-count.py`; `eslint.config.js` (L132–162 storage-import boundary); `apps/prototype-web/scripts/check-bundle-budget.mjs`.
- Tests: 27 `*.dom.test.tsx` at `src/` root; 12 co-located `*.ui.test.*`; `U09.css.test.ts`; QuickActionSheet guard/category trio; `app/navigation.test.ts`; `routeKnowledgeSync.test.ts`; `exact-values.characterization.test.ts`; `exact-values.cross-surface.test.ts`; UnsavedChangesGuard trio.
- Docs: `docs/product/design-system-v1.md` (authority claim L3; palette drift L37/39); `docs/product/placement-principles-v1.md`; `docs/product/mobile-ui-ux-reference-v1.md`; `docs/product/owner-decisions-v1.md`; `apps/prototype-web/ARCHITECTURE.md`; `AGENTS.md`; `docs/inventory/05-unreachable.md` (stale measurement).

**Standard package** (`Documents/main @ 864263c190f5d3da6041acfafb0720e85ac6e320`, under `micro-standard-v2/`): all 31 files listed in Section 2 were read; decisive citations: `README.md` (action classes, official navigation, verification boundary); `RELEASE.md` (run `run-20260913-msv2-zai-01`, token truthing, Prototype exclusion); `design-tokens.css` (120 custom properties; 18 hex; derivatives); `design-tokens.json` (`product_boundary: "Visual contracts only"`); `component-contracts.md` (value zone, period chip, row slots, "domain compositions sit above these primitives"); `button-system.md`; `component-states.md`; `color-system.md` (link-ink = owner decision; tint grammar); `accessibility.md` (contrast table; device/AT not claimed); `verification-report.md`; `coverage-matrix.json` (families "current"; `requires_separate_testing`); `decision-log.md` (#5 primary re-scope; #8 gold retirement; #13 Prototype boundary); `self-critique.md` (no dark mode/chart library/product policy); `source-inventory.md`; `navigation-shell.md` (4 destinations); `overlay-system.md`; `input-system.md`; `data-display-system.md`; `empty-loading-error-states.md`; `typography.md` (12px floor); `iconography.md`; `motion-interaction.md`; `spacing-radius-elevation.md`; `responsive-geometry.md`; `content-guidelines.md`; `surface-system.md`; `visual-direction.md`; `component-gallery.html/.css/.js` (12 demo families; 43-glyph sprite; six-state save; chart state cycle; staged filter state machine).

## Appendix B — Required comparison questions → where answered

1. Screens/components covered immediately → §11, §7 (F-30, F-24 rows), Agent 4 §B.
2. Missing from Standard but Micro Feature Patterns → §13, F-24/F-25/F-26.
3. True Standard contract gaps vs implementation mapping gaps → §7 "Gap type" column (contract gaps: charts, staged filters, snackbar-stance, skeleton; mapping gaps: namespace, values, z, type/motion).
4. Where Micro duplicates → §8.1 item 5, §8.2, F-09/F-13/F-15/F-16/F-32/F-35.
5. Current sources of truth → §9 (column 2).
6. Authoritative source after integration → §9 (column 4).
7. What must be preserved as product-specific → §12, §14.
8. What must not be copied from Prototype → §15.
9. Where token/component changes fail to propagate → §8.2.
10. Safest target module map without bulk moves → §10.
11. Minimum implementation waves → §17.
12. Wave dependencies/risks/acceptance/rollback → §17 table.
13. Unresolved owner choices → §16 (D1–D13).
