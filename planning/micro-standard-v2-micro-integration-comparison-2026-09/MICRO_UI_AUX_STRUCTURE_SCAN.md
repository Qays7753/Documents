# Micro UI/AUX Structure & Organization Scan (Read-Only)

**Deliverable:** `MICRO_UI_AUX_STRUCTURE_SCAN.md`
**Scope:** Read-only Structure/Architecture/Code Organization Scan limited to the UI/AUX/design-system boundary of the Micro repository. **Nothing was reorganized, moved, renamed, edited, or deleted.** No item is classified as "fix now in code" — implementation requires the owner's approval of the parent report first.
**Subject:** Qays7753/Micro `main` @ `c0469e265f24c70427eb7826dee717be117cff87` (verified 2026-09-14).
**Reference:** Qays7753/Documents `main` @ `864263c190f5d3da6041acfafb0720e85ac6e320`, package `micro-standard-v2/` (31 files).
**Accepted strategy (fixed):** Contract-first + Token-driven + Component-driven + Feature-oriented + Composition-based.
Paths are relative to the Micro repo root; `SRC` = `apps/prototype-web/client/src`.

---

## 1. Module and feature boundaries

**Observed boundaries (verified):**
- `src/domain/` — 15 domains (actual-time, asset, cash-continuity, catalog, craft-order, direct-sale, financial-event, g5, inventory-material, loan, owner-entitlement, recurring-margin, supplier-purchase) + `shared/` (businessTime, currency, numeric). Owns types + policies; zero UI imports.
- `SRC/application/` — ~113 service files across 20+ feature folders (finance, fulfillment, agreements, cash, catalog, collections, cost, drafts, diagnostics, direct-sales, estimates, follow-up, fulfillment, g5, home, inventory, financial-pulse, owner, transfers…). Import domain types + storage interfaces; zero UI/CSS imports (the two grep hits are comments in `costService.ts` L3 and `agreementService.ts` L3: "React never calculates…").
- `SRC/storage/local/` — IndexedDB + Memory adapters behind interfaces, commit guards (`deliveryReversalCommitGuard`, `loanCommitGuard`, `supplierScheduleCommitGuard`), migrations, snapshot. Runtime storage imports occur only at composition roots: `app/StartupGate.tsx` L5–6 and `app/PrototypeServicesContext.tsx` L53.
- `SRC/presentation/` — formatting/labeling utilities (formatters, plurals, cashCountMessages, orderAgreementPresentation, catalogPresentation, ownerEntitlementPresentation, activityLabels, g5Plurals). Owns no time logic (re-exports `localDateInAmman` from `@micro-domain/shared`).
- `SRC/app/` — router, route classifier, navigation contract, StartupGate (AUX composition roots).
- `SRC/components/` + `SRC/pages/` + `SRC/contexts/` — UI layer.
- Alias edges: `@/*` → `client/src/*`, `@micro-domain/*` → `src/domain/*` (`tsconfig.json` L19–22, mirrored in `vite.config.ts` L306–311). Zero relative layer escapes found.

**Boundary quality:** the downward flow (domain ← application ← UI) is disciplined and matches strategy layer 7. What the UI side lacks is the strategy's layers 2–5 as *declared modules*: there is no runtime token-mapping module, no shared-primitive module, no AUX-shell module, no feature-pattern module — their functions are spread across `index.css` families, `components/`, and page-local code (details in §5).

**Feature-family CSS coupling:** ≈2/3 of `index.css` is feature-scoped (home ×32 selectors, finance ×21, month ×19, g5 ×17, owner ×16, activity ×13, sheet ×11, recurrence ×10, foundation ×8, cash ×8, schedule ×7, period ×7, integrity ×7, insights ×7, decision ×7…). Feature boundaries exist but live inside one 6,962-line file.

## 2. File responsibilities and oversized files

| File | Lines | Mixed responsibilities (evidence) |
|---|---|---|
| `SRC/index.css` | 6,962 | Token blocks (3 vocabularies) + base + chrome + shared components + ≈15 feature CSS families + 4 reduced-motion blocks + 30 media queries in one accreted file (section map §5) |
| `SRC/storage/local/IndexedDbLocalStore.ts` | 2,915 | Storage adapter (out of UI/AUX scope; noted for completeness) |
| `SRC/pages/OrderDetail.tsx` | 1,412 | Data orchestration across 5+ services (L187, 213, 329, 393, 470, 479…), deposit/cost/price panels, status branching ×4, 19 inline `د.أ` compositions (L465, 703–04, 779–80), `setMessage` feedback machine (L311–327), error threading to 4 inline confirm panels |
| `SRC/pages/OwnerEntitlement.tsx` | 1,096 | 51 `useState`, 3 `useMemo`, ~32 validation branches, 33 tone mentions, layout + formatting inline |
| `SRC/pages/FinancialEventEditor.tsx` | 1,055 | Business vocabulary constants inline (L152–157: RELATIONSHIP/BEHAVIOR/PURPOSE/KNOWLEDGE/SHARED_MODE), local `ExpenseClassification` (L881), dead wrapper `formatMoneyOption` (L877), 29 `useState` |
| `SRC/pages/Schedule.tsx` | 1,028 | A whole calendar subsystem as 7 page-local components (L395 CapacityDecisionSurface, L442 RecurrencePanel, L693 MonthSchedulePanel, L811 MonthDayCell, L884 MonthDayDetail, L938 ScheduleSection, L996 WeekDay) |
| `SRC/pages/Finance.tsx` | 988 | Hosts EventsLayer (862 L child) + 5 local components (L757 ReviewPulseSection, L837 OwnerDecisionCard, L877 CashDecisionSurface, L952 Metric, L967 PositionCard) |
| `SRC/pages/DirectSaleEditor.tsx` | 974 | 31 `useState`, 42 `if` branches, difference-decision panel inline (L848+), hand-rolled notice `<p className="micro-field-error" role="status">` (L844–847) |
| `SRC/pages/SupplierPurchaseEditor.tsx` | 965 | Same editor genre: classification branching + 16 tone mentions + own field blocks |
| `SRC/pages/InventoryMovementEditor.tsx` | 947 | Consumption rows + validation + formatting inline |
| `SRC/pages/Catalog.tsx` | 924 | Product rows, stock/active states, form + list in one file (sections extracted to components/catalog/*) |
| `SRC/components/finance/EventsLayer.tsx` | 862 | Event list + summary + audit + routing to editors inside one `<details>` layer — "a page wearing a component costume" |
| `SRC/components/layout/QuickActionSheet.tsx` | 761 | vaul Drawer + micro-class bridging + 4 sub-sheets inline (menu/sale/expense/receipt, L393–421) |

Cross-cutting: inline `style={{` is nearly absent (2 total); the size problem is component/branch count, not style strings. Pages total ≈25,140 lines across 60 `.tsx` page files; components: 47 non-test files.

## 3. Dependency and layer violations (UI/AUX boundary)

| # | Edge | Evidence | Severity | Classification |
|---|---|---|---|---|
| V-1 | UI → storage types (type-only) | 17 files import `@/storage/local/types`: `pages/NewDraft.tsx` L6, `pages/Tools.tsx` L14, `pages/AgreementEditor.tsx` L16, `pages/Settings.tsx` L33, `pages/ScheduleEditor.tsx` L11, `pages/CostEditor.tsx` L16, `pages/OrderDetail.tsx` L43, `pages/EstimateDetail.tsx` L15, `pages/DraftEditor.tsx` L12, `pages/CostCalculator.tsx` L18, `pages/Finance.tsx` L31, `pages/Orders.tsx` L15, `components/order/AgreementContextPanel.tsx` L8, `components/cost/MaterialSheet.tsx` L14, `components/settings/SettingsOperatingModeSection.tsx` L8, `components/forms/useFormDraft.ts` L12 | Medium — binds UI composition to storage record shapes instead of contracts | fix now in planning (GAP-26) |
| V-2 | Persistence outside storage/ | `application/drafts/legacyFormDraftMigration.ts` L32; `application/diagnostics/localDiagnosticsService.ts` L174 (`globalThis.localStorage`) — both behind injectable interfaces | Low | fix now in planning (GAP-27) |
| V-3 | Component → page (type-only) | `components/finance/FinancePeriodResultSection.tsx` L12 imports `type FinanceState` from `@/pages/Finance` | Low — the only component→page edge; near-cycle | fix now in planning (GAP-28) |
| V-4 | Application → UI | None (zero imports; comments only) | — | preserve |
| V-5 | UI → domain | 212 non-test `@micro-domain/*` imports (27 page files + ~12 components) — **allowed by design** (domain owns meaning) | — | preserve |
| V-6 | Relative layer escapes / cycles | Zero relative escapes; no runtime cycles found; near-cycle only via V-3 | — | preserve (after V-3 fix) |

## 4. Cycles and guard limitations

**Cycles:** none at runtime. The single near-cycle is V-3 (Finance ↔ FinancePeriodResultSection via a type import). `pwa/dirtyRegistry.ts` and the UnsavedChanges provider form an intentional registry pattern, not a cycle.

**Guard limitations (verified):**
- 165 test files in `SRC`; UI-guard subset ≈ 48 files / ≈260 `it()` blocks — strong on copy, roles, aria, journeys, navigation contract, route classification, lock gates, unsaved-changes.
- **Only one test reads CSS**: `U09.css.test.ts` (3 string assertions: 48px period input, 44×48 `.micro-text-action`, 44px `.micro-button-quiet`) — `indexOf`-based, fragile, and it reads the *first* matching rule (hazard given the triple-duplicated block, §5).
- Nothing fails on: token value changes, a second `--color-border`, new hex literals inside token zones, `!important` growth (35 today), a 4th sheet system, z-index drift, or dark-mode mapping breakage.
- `scripts/design-token-guards.py` (npm `design-guards`, run passes today, exit 0): bans raw hex/rgb/hsl in non-test tsx/ts and CSS outside `:root/.dark/@theme` zones (one sanctioned scrim string `color-mix(in srgb, #1f1e1d 45%, transparent)`); enforces part-level whitelists (spacing 2–32px set + var/calc/env/clamp; radius {0,12,16,20,999px,50%}; 13-size font whitelist 11–31px; z {0,1,20,30,40,50,60,70}). It is **not** a palette freeze — any hex inside token zones passes — and it is not wired into `vite build` (package.json L11 script only).
- Build-time guard: `vite.config.ts` L227–245 D-034 bundle budget gate with `manifest: true` (L324) — size only, no design assertions.

## 5. Duplication and competing sources of truth

**`index.css` section map (anchor lines):**
L1–8 principle comments + Tailwind imports · L9–31 `@theme inline` shadcn bridge · L33–75 `:root` micro tokens (25 colors, space, radii, elevation, motion) · L76–94 shadcn aliases onto micro tokens · L97–144 `.dark` mirror · L146–181 base layer · L183–249 app chrome · L250–286 status chip + icon button · L287–432 page/heading/route-loading/priority · L433–476 buttons (`.micro-button` L433, primary L457, secondary L468) · L477–708 sections/info-card/tone slots/text-action/empty/copy-tone · L693–751 dialog overlay + dialog · L752–805 spinner + keyboard chrome-hide · L806–871 bottom nav + FAB + vaul bridge · L872–1159 sheet family + form fields · L1160–1230 form card + sticky footer · L1609–1760 event list + collection actions · L1760–1986 home families · L1986–2243 schedule · L2243–3139 finance + owner + finance-event · L3139–3449 supplier · L3449–3842 G5 · L3842–4196 month panel · L4196–4829 recurrence + decision surfaces · L4829–5099 truth-road · L5099–5826 profile + home heading + last events + owner entitlement · L5826–6154 catalog + chip-list · L6161–6237 insights · L6237–6554 "أدواتي" wave + party entry · L6554–6962 integrity + asset/loan cards + lock veil/overlay.

**Competing truths / duplication (all verified):**
1. **Triple-duplicated ≈130-line block, ≈256 redundant lines**: `.micro-financial-pulse {` at L1822 / 2074 / 2599; `.micro-home-heading {` ×3 (L1760/1952/2204); also `.micro-record-summary`, `.micro-section-title`, `.micro-decision-surface`, `.micro-review-result`, `.micro-review-empty`, `.micro-scope-line`, `.micro-button-block` … Copies 1&2 byte-identical; copy 3 matches the first 126 lines then extends with schedule rules. Hazard: string-based CSS tests read the first match.
2. **`--color-border` triple alias**: micro L54 `--color-border:#eae6dc` → shadcn L92 `--border: var(--color-border)` → `@theme inline` L28 `--color-border: var(--border)`. Works only because `inline` does not emit variables; any future non-inline `@theme` color would emit a competing `--color-border`.
3. **Two scrim implementations**: literal `color-mix(in srgb, #1f1e1d 45%, transparent)` (`.micro-dialog-overlay` L711–716, the guard's sanctioned exception) vs token-driven `color-mix(in_srgb, var(--color-ink-on-color) 45%, transparent)` (`drawer.tsx` L28–30). Same alpha, different base-ink mechanism.
4. **`--primary` role flip**: light L82 `var(--color-brand-text)` (#964e33 brown) vs dark L131 `var(--color-brand-primary)` (#d59172 light terracotta) — `.micro-button-primary` (L457) renders a different brand role per mode.
5. **3 sheet systems**: `.micro-sheet-*` family (L872–1000), `.micro-dialog*` (L711–751), vaul bridge `.micro-bottom-sheet` (L857) — plus `QuickActionSheet` bridging both worlds.
6. **18 `micro-*card*` variants**; only `InfoCard` has tone slots, used by 2 files.
7. **13 row families, 2 anatomies**: `.micro-activity-row` (divider-only row) vs `.micro-event-row` (bordered card row).
8. **4 empty-state variants**: `.micro-empty-state` (6 surfaces), `.micro-empty-inline`, `.micro-home-quiet`, `.micro-empty-copy`.
9. **Identity hexes mirrored outside CSS**: `vite.config.ts` L262–263 (PWA `background_color "#FAF9F5"`, `theme_color "#CC785C"`), `public/micro-mark.svg` L3 (`fill="#CC785C"`), `index.html` L9–10 (meta theme-color = canvas colors, rewritten at runtime by ThemeContext — not a brand twin).
10. **Unit composition**: 275 exact `د.أ` literals across 53 files vs `formatMoneyWithUnit` in 6 files; 30 files hand-roll `dir="ltr"` isolation that `DisplayValue`/`MoneyValue` already encapsulates.
11. **Per-feature repeats**: `prefers-reduced-motion` blocks ×4 (L768, L3289, L4188, L6043); `max-width:380px` media ×8; `min-height:44px` floor ×13; `border-radius:999px` ×11; `!important` ×35 across 16 rules.
12. **Dead surface**: `components/ui/tooltip.tsx` — provider mounted (`App.tsx` L15), Tooltip/Trigger/Content never rendered; radix chunk shipped (`vite.config.ts` L334–335).

**What is NOT duplicated (verified, to the record's credit):** one elevation system (21 var uses vs 1 literal ring); rgba literals only inside token definitions; zero color literals in TSX; zero physical `rtl:` rules (105 logical properties); 631 `--space-*` uses vs 7 raw margins (all 2–4px nudges); 94 radius-token uses.

## 6. Feature discoverability

- **Routes/screens:** excellent — router + `navigation.ts` contextual labels (15 prefixes) + `routeClassifier` + tests; a reader can map every URL to a page in minutes.
- **Design values:** good entry point (`docs/product/design-system-v1.md` designates `index.css` as the value source) but no module boundary: primitives and patterns are discoverable only by reading 6,962 CSS lines or grepping class names.
- **Patterns:** poor — the six runtime feature patterns (fact triad, correction grammar, next-action rows, knowledge states, decision cards, inline feedback) exist only inside pages/components; no pattern index or module owns them.
- **Docs:** `docs/00-document-index.md` provides reading order; UI-relevant contracts (26, 29, 37) are binding; `AGENTS.md` mandates the UI reading list; three `ai-skills` checklists cover anti-template/UX/QA. Discoverability of *rules* is better than discoverability of *code*.

## 7. Storage / application / domain / UI composition

- Runtime store creation and injection occur only at `app/StartupGate.tsx` + `app/PrototypeServicesContext.tsx`; services receive store interfaces (dependency-inverted).
- `storage/local` imports domain types (downward, correct); commit guards enforce honest write semantics; 54 storage files carry their own tests.
- Domain is pure: no React, no CSS, no storage imports; policies + types per domain; shared numeric/time/currency helpers (`src/domain/shared/`).
- UI never persists directly (2 exceptions, §3 V-2); UI never calculates money (formatters/presentation own display; domain/application own meaning).
- The composition root pattern (`PrototypeServicesContext`) is the correct place where a future runtime token-mapping module would similarly inject — the app already has the shape the strategy needs.

## 8. Test and documentation mapping

- Tests: 165 files; ≈260 UI-guard `it()` blocks across navigation (29), lock gates (14), QuickActionSheet (15), unsaved-changes/drafts (18), chrome/PWA (15), journey suites (109), page `.ui` suites (70); presentation unit guards (formatters 15, plurals, cashCountMessages, orderAgreementPresentation, exact-values ×15).
- Docs: `design-system-v1.md` (value SoT + §9 token guards), `mobile-ui-ux-reference-v1.md`, `placement-principles-v1.md`, `guidance-interaction-policy-v1.md`, `home-navigation-proof-v1.md`, decisions v3/v4/v5, contracts 26/27/28/29/30/31/32/33/36/37/38, per-wave UX acceptance reports G20–G23, `product-source-of-truth.md`, `00-document-index.md`.
- Mapping gaps: no doc maps the `.micro-*` CSS families to contracts (the Standard's component contracts have no Micro-side implementation map); no test guards tokens/CSS beyond U09; the Standard↔Micro traceability does not exist yet — this comparison and its CSV are the first such map.

## 9. Target module map — `proposed — not executed`

Identical to parent report §10. Restated compactly: introduce `SRC/styles/` (token mapping files), `SRC/ui/primitives/` (Button, Field, Surface, Row, StatusChip, Sheet, Dialog, Notice, EmptyState, ScreenState, MoneyValue), `SRC/aux/` (AppHeader, BottomNav, Fab, routeChrome, keyboard), `SRC/patterns/` (finance-value-zone, period-controls, correction-lifecycle, order-rows, fact-cards, knowledge-states, integrity-check, scheduling), and grow `SRC/features/<family>/` gradually out of `index.css` — **without any bulk move**; existing `app/`, `application/`, `presentation/`, `storage/`, `pages/`, `src/domain/` remain as-is. Dependency rules: pages → (primitives | patterns | presentation | application); primitives/patterns never import pages; domain/application/storage never import UI; one arrow direction only, enforced by new guard tests (GAP-44).

**Explicitly a proposal.** No directory exists yet; no file was created, moved, or edited in the repository. Execution requires owner approval and follows the wave plan in the parent report §17.

## Classification summary (this scan)

| Classification | Items |
|---|---|
| fix now in planning | V-1 (storage types), V-2 (localStorage ×2), V-3 (type edge) + GAP-07 alias, GAP-08 scrim, GAP-21 tooltip, GAP-25 third-party styling, GAP-43 dedup, GAP-44 guards, GAP-06 guard freeze prep, GAP-02 mapping architecture (≈13 items; see parent report §7) |
| preserve | Layering discipline, token discipline, 6 feature patterns, AUX behaviors, route/docs discoverability, forms-protection stack (≈8 items) |
| defer | index.css split, primitive consolidations (sheets/cards/rows/empty/ScreenState), vocab extraction, type-scale tokenization, filter/sort, skeleton tier (≈13 items) |
| needs owner decision | Palette + twins + `--primary`, teal/dark mode, FAB geometry, nav labels, reader depth, period control, row markers, knowledge states, orthography, no-toast ratification, 11–12px floor (13 items = decision pack D-01…D-12) |
| out of scope | Accounting-port pressure; all non-UI/AUX boundaries (financial/permissions/sync/security/performance) |
