# Strategy, Architecture & Future-Agent Governance Review — Agent 3 (A3)

**Scope:** Micro @ `ece7be3630739d551b9ba7caf37d30a9a63c872f` (branch `micro-standard-ui-aux-integration-20260914`), Standard = `documents/micro-standard-v2/` @ Documents main `f919982c` (31 files verified: 29 core + `MANIFEST.json` + `RELEASE.md`). Read-only audit: no file inside either clone was created, modified, or deleted; no git state was changed; no installs/tests/builds were run. All counts below were re-executed against the live tree with Grep/`wc -l`/read-only git.

---

## 1. Executive verdict

The fixed strategy (**Contract-first → Token-driven → Component-driven → Feature-oriented → Composition-based**, 7-layer authority ladder) is **real in the code, not just in the docs**. Every layer's claims were re-verified against the live tree and the Standard package: 118 `--vf-*` tokens (exact match to claim), all values trace to `micro-standard-v2/design-tokens.css`/`.json` with zero invented palette values; zero raw hex/rgb in non-test TSX/TS; primitives exist, are styled solely by `styles/primitives.css`, and every documented prop matches the code; the AUX shell contains no feature business logic beyond the ADR-004-sanctioned QuickActionSheet composition; the 299-Button/81-file and 8-ChoiceButton censuses reproduce exactly.

**However, the strategy is enforced unevenly.** The mechanically-enforced core (eslint layer bans, runtime-cycle guard, design-token guards, legacy-class census, vf-tokens tests) is strong; around it sit **doc-only rules and two parallel presentation vocabularies** that a future agent can violate with every guard green. The permanent future-agent documentation (`docs/architecture/` + `AGENTS.md`) is high quality and mostly code-accurate, but contains **one direct doc-vs-code contradiction (FeedbackNote vs SOURCE_OF_TRUTH.md)**, **one materially wrong dark-mode claim**, and several pointers that send future agents to **completed-run archival documents as if they were living registries**. `docs/operations/current-state.md` — the file `AGENTS.md` designates the *only* live state reference — was not touched by the branch and will be stale the moment the branch merges.

**Bottom line:** APPROVED-LIGHT scope is genuinely closed and evidenced; the governance layer needs ~6 targeted fixes (doc corrections + 2 small guards) before the next execution phase, none of which touch financial code. No BLOCKER, no HIGH. 13 findings: 6 MEDIUM, 7 LOW.

---

## 2. Layer-by-layer strategy verification (evidence)

### 2.1 Contract-first (Standard → runtime mapping) — VERIFIED

- `apps/prototype-web/client/src/styles/vf-tokens.css` defines exactly **118 unique `--vf-*` tokens** (regex census `^\s*--vf-[a-z0-9-]+:`, sorted-unique count = 118) — matches the claim "118 mapped".
- The Standard's token contract lives in `documents/micro-standard-v2/design-tokens.css` (`:root` + `html,body` demo rules) and `design-tokens.json` (roles/action_contracts/type_scale/geometry/elevation/motion). Value-by-value comparison of all 118 Micro tokens against the Standard:
  - **18 approved hex values** confirmed as the distinct palette set in both files: `#FAF9F5 #F5F4ED #F0EEE6 #FFFFFF #E8E6DC #D1CFC5 #87867F #141413 #4D4C48 #6B6962 #D97757 #C96442 #2C84DB #1490FF #629987 #B53333 #55524A #3D3D3A`. Micro's `vf-tokens.css` contains exactly these 18 hexes (case-insensitive; prettier lowercases — disclosed in `vf-tokens.test.ts:101-110`) and **no others**. Matches W1_REPORT/DARK_MODE_BOUNDARY "18 approved values".
  - Two alias-path differences resolve to identical values (no drift): `--vf-ink-pressed` = `#3d3d3a` (Standard: `var(--vf-btn-primary-bg-pressed)` = `#3D3D3A`); `--vf-action-save-bg` = `var(--vf-ground)` (Standard: `var(--vf-bg-secondary)` = `#F5F4ED`).
  - `--vf-touch-target: 44px` traces to the Standard (`design-tokens.json` `"touch_target_px": 44`; `accessibility.md` "44px touch targets") though it is absent from the Standard's `design-tokens.css` — the value is Standard-sourced, not invented.
  - Type scale, motion, elevation, geometry all match the Standard's unprefixed tokens (prefix policy disclosed in the vf-tokens.css header naming note). Disclosed derivatives (`--vf-scrim`, `--vf-header-translucent`, shadow rgba tone) match `design-tokens.json` `functional_derivatives` exactly.
  - Documented divergence: Micro keeps its §1.8 z-ladder (0/1/20/30/40/50/60/70) instead of Standard z 250–500 — declared in the vf-tokens.css header and `SOURCE_OF_TRUTH_MATRIX.md` §C.1, and guard-enforced (`Z_LADDER` in `scripts/design-token-guards.py:39`).
- **Verdict:** the mapping layer traces to the Standard with no invented values. Claim verified.

### 2.2 Token-driven (single definition source) — VERIFIED, with guard-scope nuances (findings A3-02, A3-09, A3-13)

- Only **3 CSS files** exist under `client/src`: `index.css` (6,415 lines), `styles/primitives.css` (484), `styles/vf-tokens.css` (167). Token-definition zones:
  - `styles/vf-tokens.css:23` `:root` — the only `--vf-*` definitions (28 internal `var(--vf-*)` chains).
  - `index.css:38` `:root` — Micro runtime names (`--color-*`, `--primary`, `--space-*`, `--radius-*`, `--elevation-*`) rebound to `var(--vf-*)`; contains exactly the 4 disclosed Micro-kept hex pairs (`#256b4a/#e4f2ea` success, `#7a5c20/#f6eccf` warning) and no others (verified against `vf-tokens.test.ts` MICRO_KEPT logic and direct read).
  - `index.css:107` `.dark` — preserved Micro-local legacy v0 palette (`#1c1917` canvas, `#d59172` brand, `#cc785c`, teal `#5ec0c1/#8fd5d6`), re-declaring only Micro runtime names, never `--vf-*` (claim 13 verified verbatim).
  - `index.css:14` `@theme inline` — Tailwind v4 bridge, `var()`-only.
- `--vf-*` is defined in no other file (the only other match is a test assertion string in `vf-tokens.test.ts:179`). Claim "0 tokens defined in more than one file" holds in the live tree.
- **Raw hex audit:** zero `#[0-9a-fA-F]{3,8}` and zero `rgb(`/`hsl(` in all non-test `client/src` TSX/TS (guard-context exclusions aside, none were needed). CSS hex/rgb outside zones: zero.
- `scripts/design-token-guards.py` (read in full) enforces: (a) CSS — no hex/rgb/hsl outside **any** `:root`/`.dark`/`@theme` block (comments stripped); (b) TSX/TS non-test — no hex/rgb/hsl at all (import/href/from-context heuristic); (c) §1 scale ladders for spacing/radius/font-size/z-index. Two scope nuances become findings:
  - The guard is **zone-based, not file-based**: any *new* CSS file with its own `:root { --x: #hex }` passes; and `vf-tokens.test.ts` only validates `var(--vf-*)` references *from index.css* — a new `--vf-foo` defined in `index.css :root` and consumed from `primitives.css`/TSX passes every guard (A3-02).
  - Files outside `client/src` are unscanned: `client/index.html:9-10` carries `#faf9f5`/`#1c1917` (legitimate theme-color metas) and `vite.config.ts:262-263` carries `#FAF9F5` — correct values today, unguarded tomorrow (A3-09).

### 2.3 Component-driven (primitives) — VERIFIED, with doc gaps (findings A3-01, A3-07, A3-13)

Inventory of `components/primitives/` (all exist, all styled only by `styles/primitives.css`, which consumes `--vf-*`/`--space-*`/`--color-border` exclusively):

| Primitive | File | Props in `COMPONENT_CONTRACTS.md` match code? | Tests |
|---|---|---|---|
| Button (8 action classes + loading/block/ref) | `Button.tsx` | ✓ exact (`action`, `loading`, `block`, HTML attrs, React 19 ref) | `primitives.test.tsx` (6) |
| ChoiceRow / ChoiceButton | `ChoiceRow.tsx` | ✓ (`selected`, `onClick`, `disabled`, `name`; also `type`, `className`) | (3) |
| StatusChip (+`chipPresentation`) | `StatusChip.tsx` | ✓ (`children` word + `state`) | (6) |
| Notice / QuietCompletion / InlineError / **FeedbackNote** | `Notice.tsx` | Notice family ✓; **FeedbackNote not documented** (A3-01) | (4) |
| Row / RowList | `Row.tsx` | ✓ (`lead`,`title`,`caption`,`state`,`trailing`,`stripeTone`,`as`) | (4) |
| Field | `Field.tsx` | ✓ (`label`,`hint`,`error`,`controlId`,`children`) | (3) |
| EmptyState | `EmptyState.tsx` | ✓ (`symbol`,`state`,`title`,`description`,`action`) | (2) |
| StateMarker | `markers.tsx` | ✓ (role-driven; documented under its own heading) | via chip/notice tests |
| MoneyValue / MoneyWithUnit | `components/presentation/DisplayValue.tsx` | ✓ (documented as living in `components/presentation/`) | (2) |

- Consumer claims in `COMPONENT_CONTRACTS.md` reproduce exactly: StatusChip → Orders, InventoryMaterials, Schedule; ChoiceRow → AssetEditor, OrderDepositPanels, G5DeclarationEditor; EmptyState → Orders, Schedule, Assets, Loans, FinanceActivity, OwnerEntitlement (grep-verified, no extras).
- `styles/primitives.css` owns all primitive styling (484 lines, no other file styles `.micro-prim-*`), with a CSS-contract test block in `primitives.test.tsx` (floors, 3px stripe cap, reduced motion, no hex).
- Nuances: (i) `MoneyWithUnit`'s CSS lives in `primitives.css` whose header scopes the file to "components/primitives" — misleading header (A3-13); (ii) `Row`/`Field` have **zero production consumers** (documented owner-deferred convergence waves — MIGRATION_STATUS rows 4/5); (iii) `FeedbackNote` (8 consumers) is absent from `COMPONENT_CONTRACTS.md` and contradicts `SOURCE_OF_TRUTH.md` line 16 (see §6).

### 2.4 AUX shell (`components/layout/`) — VERIFIED per ADR-004 (finding A3-03-adjacent nuance)

- `MicroAppShell.tsx` (123 lines): chrome composition, route-kind classification, keyboard heuristic, quick-action **route dispatch** (`order`→`/orders/draft/new?intent=customer_order`, etc.), idle prefetch. No financial logic.
- `AppHeader.tsx` (61): brand, context label, settings button, theme toggle. No feature logic.
- `BottomNav.tsx` (71): nav items from `app/navigation` + labeled FAB. No feature logic.
- `QuickActionSheet.tsx` (339): mode dispatch, open/close lifecycle, discard guard, receipt, read-only wallets/suggestions prefetch; composes `components/finance/Quick{Sale,Expense}Form` — **explicitly sanctioned** by ADR-004 as "the documented exception to strict downward-only imports at layer 4". 15 sheet tests confirmed (3 files: 7+5+3).
- Boundary nuance recorded (not a violation of the ADR's letter): the shell encodes the **sale default-wallet policy** (`wallet.kind === "cash_drawer"` → default, `QuickActionSheet.tsx:108-109`) while ADR-004 assigns "wallet attribution" to the feature forms and bans "product policy" in the shell. Small policy-in-shell precedent worth an ADR-004 clarifying sentence.

### 2.5 Feature-oriented (`components/<feature>/`) — VERIFIED (finding A3-07)

Live families: `finance, orders, order, cost, catalog, owner, loans, settings, security, presentation` — exactly the layer-5 list in `UI_AUX_ARCHITECTURE.md` §2, **plus two undocumented directories**: `components/forms/` (UnsavedChangesGuard, FormDraftRestoreBanner, LocalDateField, EnglishNumberInput/QuantityInput, useFormDraft/useFormDirty — cross-feature form infrastructure) and `components/ui/` (radix `drawer.tsx`). Neither has a slot in the ladder's layer-5 enumeration. `FEATURE_PATTERN_CATALOG.md` (run folder) documents the 6 Micro-owned patterns + composition patterns; representative evidence files all exist (`CorrectionsLayer.tsx`, `InventoryReversalEditor.tsx`, `DecisionPanel.tsx`, Home FactCard, EventsLayer) and pattern 4 (knowledge states) is genuinely adapter-backed. Pattern-to-catalog claims check out; the catalog itself is a completed-run artifact (see dry-run F).

### 2.6 Composition-based (pages) — VERIFIED (finding A3-09)

Read in full or in depth: `pages/Home.tsx` (489), `pages/Settings.tsx` (622), `pages/Finance.tsx` (996). All three compose primitives (`Button`, `MoneyValue`/`MoneyWithUnit`), feature components (`components/settings/*`), ratified link pattern (`micro-text-action`), and `micro-*` classes styled in `index.css`. Zero raw hex, zero CSS imports, zero styling logic.
- Violations found (structural only, no palette): **2 inline `style={{}}` sites** — `pages/DirectSaleEditor.tsx:631` (fieldset reset `border:0,padding:0,margin:0`) and `components/forms/UnsavedChangesGuard.tsx:293` (`marginInlineStart:"auto"`). No guard bans inline styles; these are precedents a future agent can cite (A3-09).
- Confirmed documented divergences visible in code: Home keeps `MoneyValue + د.أ` literal composition (SCREEN_COMPOSITION_MAP adoption note — verified); Finance uses `MoneyWithUnit` for the unallocated note (`Finance.tsx:945`) ✓.

### 2.7 Import direction — VERIFIED with registered exceptions (findings A3-06, A3-11)

What the guards actually enforce (read in full):
- `scripts/check-runtime-cycles.mjs` — AST-level **runtime value** import cycles only (type-only erased), across `src/` + `client/src/` production files (259 files, 0 cycles claimed; script logic verified).
- `eslint.config.js` (via `check-layer-boundaries.test.mjs` fixture tests) — domain purity (relative-only imports, no browser globals); pages/components → no runtime `@/storage/local/*` (type allowed) and no localStorage/sessionStorage; application/storage → no React and no `@/components|@/pages` even as types; app/ → storage runtime ban with 2 documented exceptions; Math rounding bans.
- Actual import edges audited by grep:
  - **pages → `@micro-domain`**: 25 files (mostly type-only; value imports of pure functions in `DirectSaleEditor.tsx:18`, `OrderDetail.tsx:44`, `CostEditor.tsx:5`). Ladder-legal (6→7 downward); but `SOURCE_OF_TRUTH.md` row "screens via usePrototypeServices" understates this direct path (doc-precision note).
  - **components → pages**: exactly one edge, the registered V-3 (`components/finance/FinancePeriodResultSection.tsx:12` type-imports `FinanceState` from `@/pages/Finance`) — unchanged, not replicated. ✓
  - **primitives**: import only `react`, `clsx`, `lucide-react`, `@/presentation/stateAdapter` (sanctioned leaf), siblings. ✓ Clean today — but the "primitives are leaves" rule (IMPORT_BOUNDARIES rule 2) has **no mechanical enforcement** (A3-06).
  - **layout → feature forms + application read-only**: sanctioned by ADR-004. ✓
  - **ROUTE_TEMPLATES (58 templates) ↔ MicroRouter ↔ routeClassifier**: no sync test exists — doc-mandated only (A3-11).

---

## 3. State adapter verification — VERIFIED; bypass analysis splits into two vocabularies (finding A3-03)

`presentation/stateAdapter.ts` (163 lines, read in full; **zero imports** — pure presentation):
- Maps **markerRole + tone + family + isKnowledge only**; no word production anywhere; `honestVoidDisplayValue` returns `"0"` only for `measured-zero`, `null` otherwise ("الكلمة/الشريحة ملك الشاشة").
- **pending ≠ success**: `pending → {clock, info}` (activity table); test asserts info-tone clock, never success. ✓
- **unknown ≠ failure**: `unknown → {question, neutral, outcome}`; `overdue` is the only due-family error tone. ✓
- **Knowledge states always neutral** (all 5: unconfirmed/incomplete/needs-review/estimated/unknown-magnitude), enforced by `isPermissibleTone` + tests. ✓
- **Empty-value trichotomy**: `unrecorded` (dot) / `unavailable` (none) / `measured-zero` (none, displays "0") — distinct keys, distinct presentations; plus no-data/no-results display voids. ✓
- 15 tests in `stateAdapter.test.ts` incl. the **union lockstep test** (line 57) tying `MicroActivityStatus` to `application/activity/activityService`'s `ActivityStatus` — a real drift guard. Consumers: only `StatusChip.tsx`/`markers.tsx` + the barrel. **No chip-level bypass exists** — the "0 state-adapter bypasses" claim holds for state chips.

**However**, a second, unregistered tone vocabulary runs in parallel for *surfaces*:
- `data-tone="accent" | "warning" | "danger" | "update" | "offline"` is assigned **directly in pages/components**: `Orders.tsx:152`, `Statement.tsx:501,561`, `DirectSaleEditor.tsx:599,608`, `Schedule.tsx:950`, `ActualMaterialPanel.tsx:28`, `FormDraftRestoreBanner.tsx:49`, `PwaRuntimeNotice.tsx:57,93`, `InfoCard.tsx`/`DecisionPanel.tsx` (prop-driven), styled per-component-class in `index.css` (`.micro-info-card[data-tone=…]`, `.micro-g5-card[data-tone=…]`, `.micro-runtime-card[data-tone=offline]`, …).
- `components/finance/G5DecisionPanel.tsx:116-122` computes `data-tone` from financial status (`available→accent`, `invalid→danger`, else `warning`) — a **hand-rolled state→tone mapping outside the adapter**, exactly the pattern ADR-003 exists to prevent, in a different vocabulary.
- `SOURCE_OF_TRUTH.md` line 14 says state tone is "Never defined in: pages (no direct data-tone)" — as written it is contradicted by the page-level `data-tone` assignments above (they are surface tones, not marker tones, but the doc sentence does not distinguish).
- Cross-contamination risk: `index.css:386-395` styles `.dark [data-tone="accent"]` / `.dark [data-tone="warning"]` **globally** — a future agent adding `data-tone="warning"` to a StatusChip (whose vocabulary has no "warning") would silently inherit dark-panel styles.

---

## 4. Duplication & oversized responsibility findings

**10 largest production (non-test) files** (`wc -l`):

| # | File | Lines | Note |
|---|---|---|---|
| 1 | `storage/local/IndexedDbLocalStore.ts` | 2,915 | storage; owner-registered monolith (§11 wave plan) |
| 2 | `storage/local/MemoryLocalStore.ts` | 1,570 | storage |
| 3 | `pages/OrderDetail.tsx` | 1,419 | largest page; composes layers, stays in layer |
| 4 | `application/inventory/inventoryMaterialService.ts` | 1,401 | application |
| 5 | `application/transfers/transferFamilyValidators.ts` | 1,377 | application |
| 6 | `application/finance/projectFinancialService.ts` | 1,280 | application |
| 7 | `application/finance/integrityCheckService.ts` | 1,182 | application |
| 8 | `pages/OwnerEntitlement.tsx` | 1,100 | page |
| 9 | `pages/FinancialEventEditor.tsx` | 1,064 | page |
| 10 | `application/transfers/transferSnapshotValidation.ts` | 1,061 | application |

Plus **`index.css` = 6,415 lines** — every screen/feature surface rule centralized in one file (documented convention: EXTENSION_PLAYBOOK A.4 routes all new screen CSS there; IMPORT_BOUNDARIES rule 7 forbids mass extraction without a wave). Not a layer violation, but it is the single biggest future-agent navigation burden in the UI layer, and its size makes "which rule owns this surface" increasingly grep-dependent.

**No page/component file mixes ladder layers** (import audit clean). Layer-mixing risk is concentrated in *breadth*, not direction.

**Duplicated logic patterns (quantified):**

| Pattern | Legacy/prevalent form | Converged form | Registered? |
|---|---|---|---|
| Form field composition | `label className="micro-field"` **×305 in 55 files** | `Field` primitive: **0 production uses** | ✓ MIGRATION_STATUS (owner wave) |
| Money rendering | `formatMoneyMinor(...)` + literal `د.أ` **×100 calls** (e.g. `Finance.tsx:866-869`) | `MoneyValue`/`MoneyWithUnit` ×201 uses / 43 files | ✓ (Row-convergence wave, ~30 sites listed) |
| Inline feedback | ~110 `role="status"` sites (FEATURE_PATTERN_CATALOG #6) | Notice/QuietCompletion/InlineError/FeedbackNote **×14 uses / 11 files** | ✓ (conditional ternaries ~22 surfaces listed) |
| List rows | finance-event card rows (Finance/Statement/FinanceActivity/WalletLedger) | `Row`/`RowList`: **0 production uses** | ✓ (owner visual wave) |
| **Verified-export download sequence** | duplicated verbatim within `pages/Settings.tsx` (`performExportLocal` 271-296 vs `performResetFlow` 307-328: Blob → objectURL → link.click → 30s revoke → markVerifiedExport) | none | **✗ NOT registered anywhere** (A3-12) |

The big four convergences are all owner-registered deferrals — honest, not silent. The Settings export duplication is small, new, and unregistered.

---

## 5. Documentation governance audit (per doc)

### `AGENTS.md` (root, 141 lines, read in full)
- §2 item 6 + the UI/AUX row mandate `docs/architecture/` (6 files) + `ADRs/` before any UI change, in order — **wiring verified**. All referenced paths exist (`docs/operations/current-state.md`, `.github/pull_request_template.md`, `.stylelintrc.json`, etc.).
- §10 numeric limits match code: lint budget 37, schema/export 35/27, bundle 650,000/155,000 (`check-bundle-budget.mjs`). ✓
- **Gap (A3-05):** §8 declares `docs/operations/current-state.md` the *only live state reference* which "must match main" — the branch does not touch it (last updated 2026-09-13, Group 11; zero mention of the Standard integration; `git diff origin/main..HEAD -- docs/operations/ todo.md` is empty). Post-merge, the mandated first read will describe a pre-integration repo. No branch doc (EXECUTION_REPORT, CHANGE_PROTOCOL closure steps) lists the current-state/todo update as a merge step.

### `docs/architecture/UI_AUX_ARCHITECTURE.md`
- Ladder, layer table, correct/incorrect examples, action-class table, §6 invariants — all verified against code (z-ladder matches guard; 44px/48px/13px floors match primitives.css).
- §2 "boundary precision" claims "the runtime-cycle guard plus these rules are the mechanical enforcement" — true for layer 7, **overstated for primitives-as-leaves** (A3-06). Layer-5 directory list omits `forms/` + `ui/` (A3-07).

### `docs/architecture/SOURCE_OF_TRUTH.md`
- 26 of 28 rows verified accurate (token ownership, button classes, choice contract, state words, AUX, z-ladder, route classification, storage/domain rows).
- **Row "Success/advisory/error feedback classification" (line 16) is contradicted by code (A3-01):** "Never defined in: the primitives (they render, never classify)" vs `FeedbackNote` in `components/primitives/Notice.tsx` which *owns* the success-prefix classification (`/^تم[ت ]/`) — and is documented as the authority in the run-folder `SOURCE_OF_TRUTH_MATRIX.md` line 79. The permanent doc is the stale one.
- Row "Status marker + tone + family … never defined in pages (no direct data-tone)" — too absolute given the surface-tone assignments in pages (A3-03).
- Row "financial meaning … consumed by screens via usePrototypeServices" — pages also import domain pure functions directly (ladder-legal; wording imprecise).

### `docs/architecture/EXTENSION_PLAYBOOK.md`
- Workflows A–G are complete and actionable (see §6 dry runs). Two pointer problems: B.6 "record in the source-of-truth matrix and the component catalog", E.3 "update `AUX_CONTRACT.md` (run folder)", F.4 "document in the feature-pattern catalog" all point at **completed-run archival artifacts** as living registries (A3-10). Verification-gates section matches the actual `pnpm check` inventory.

### `docs/architecture/CHANGE_PROTOCOL.md`
- Consistent with guards and ADRs; §2 scope rule (all-roots census) matches `legacyClassCensus.test.ts` (scans `pages/components/app/pwa/contexts`, strips comments, 10 retired classes). No issues found.

### `docs/architecture/COMPONENT_CONTRACTS.md`
- Props/consumers/responsibilities verified per primitive (§2.3 table). Missing: **FeedbackNote** section (A3-01). Correctly declares the run-folder `COMPONENT_CATALOG.md` "historical adoption census" — which makes the playbook's "record in the component catalog" instruction (B.6) ambiguous.

### `docs/architecture/MIGRATION_STATUS.md`
- **All 14 preserved-with-reason items verified present in code at the stated location with the stated behavior**: Loans error container (`Loans.tsx:62` `micro-empty-state` + load-failure aria-label); Statement quiet voids (`Statement.tsx:307,318`); conditional ternaries (present); finance-event card rows (present); Field non-adoption (`micro-field` ×305); `.dark` (index.css:107); `micro-text-action` (10 files); owner-page 17px svg (index.css:5264-5266); raw money compositions (Finance.tsx:866 etc.); Settings ✓ literal (`Settings.tsx:294`); FinanceActivity no-chip empty wording (`FinanceActivity.tsx:271-274`); Setup «التالي» save (`Setup.tsx:410`); Schedule capacity secondary (`Schedule.tsx:379-384`); quiet openers (`DirectSaleEditor.tsx:516`, OrderDetail ×7).
- Per-action totals match grep: 299 `<Button>` in 81 non-test files ✓; 8 `<ChoiceButton>` ✓.
- **Inaccuracy (A3-08):** "9 choice toggles → ChoiceRow (… + ActualTimePanel guided/unguided weight split)" — `ActualTimePanel.tsx` contains **no** ChoiceRow/ChoiceButton (verified by grep and read; it uses plain `<Button>`s at lines 273/329/377). The 9th "toggle" is not a ChoiceRow usage; actual count is 8.

### `docs/architecture/ADRs/ADR-001…008`
- ADR-001/002/003/005/007: verified consistent with code. ADR-003's "0 raw data-tone bypasses" holds for chip-level state marks (see §3 for the surface-tone nuance).
- ADR-004: matches QuickActionSheet implementation; "dispatch only, never product policy" vs the cash_drawer-default policy in the shell (§2.4 nuance).
- ADR-006: sound; says "299 across 80 files" — actual is 81 files (EXECUTION_REPORT and matrix both say 81) — internal inconsistency (A3-08).
- ADR-008: navigation-weight convention verified in code (Home/OrderDetail CTAs wear save); same ActualTimePanel parenthetical inaccuracy as MIGRATION_STATUS.

### Run-folder docs (spot-audited)
- `AUX_CONTRACT.md`: matches QuickActionSheet/BottomNav/AppHeader code and index.css rules; 15 sheet tests confirmed.
- `SCREEN_COMPOSITION_MAP.md`: pilots verified (Home keeps `MoneyValue+د.أ`; Finance uses `MoneyWithUnit` at :945).
- `SOURCE_OF_TRUTH_MATRIX.md`: accurate, including the completion-run additions table that documents FeedbackNote (the permanent doc lacks).
- `COMPONENT_CATALOG.md`: declared historical; stale vs final tree (no ChoiceRow/FeedbackNote rows) — acceptable as history, but the primitives barrel comment (`index.ts:4`) points to it as the ownership reference.
- `DARK_MODE_BOUNDARY.md`: **line 10 is materially wrong (A3-04)**: "Primitives added in W2 consume … the Micro alias names for mode-adaptive surfaces — so dark mode continues to resolve through the legacy alias layer exactly as before this run." Reality: `primitives.css` binds surfaces/marks to light-locked `--vf-*` (`--vf-surface`, `--vf-ground`, `--vf-ink`, marker hues), and `.dark` re-declares only `--color-*` names — so in dark mode a StatusChip renders a **white** surface and a commit button renders `#141413` on the `#1c1917` canvas (≈1.1:1 affordance). Dark is **user-reachable today** (`ThemeContext` defaults to `"system"` honoring `prefers-color-scheme: dark`, plus the live header toggle), so this is observable behavior, honestly declared untested (claim 11), but the doc's resolution claim would misdirect the future dark wave's scoping.
- `EXECUTION_REPORT.md` §8 one-step-behind nuance (claim 14): verified — `ece7be3` (actual Micro tip) itself records `81b1933`/`fe3f8db` as "final" in §8 + `DOCUMENTS_UPLOAD_STATUS.md`; the mirror `c8e5701` records "Micro final commit ece7be3". This is the inherent fixed-point of a commit recording its own push; honest, disclosed, and the orchestrator's CONTEXT.md holds the true tips. Classification: ALREADY_CLOSED_WITH_EVIDENCE (informational).

---

## 6. Future-agent dry runs (7 documented scenarios — workflow traced against docs + code; no code written)

### (a) Add a new screen
**Governed by:** EXTENSION_PLAYBOOK §A + UI_AUX_ARCHITECTURE + AGENTS.md §2.6.
**Workflow traced:** identify feature family → map screen (goal/primary action/states incl. honest voids) → reuse primitives (Button classes, StatusChip/EmptyState/Notice, MoneyValue/MoneyWithUnit, ChoiceRow) → CSS only if genuinely new, in `index.css` under `.micro-<screen>-` with `--vf-*` only → register route in `app/MicroRouter.tsx` (deep-before-`:id`, ordering comments verified present) → classify in `app/routeClassifier.ts` (`deepFlowPatterns` regex list) → register in `application/diagnostics/routeTemplate.ts` ROUTE_TEMPLATES (58 templates) → honest loading gate + `role="alert"` errors → journey/dom tests + text-density updates → update MIGRATION_STATUS/matrix/composition map.
**Friction points / wrong-change risks:**
1. **The three route registrations have no sync guard** (verified: no test ties ROUTE_TEMPLATES ↔ MicroRouter ↔ routeClassifier). Forgetting routeClassifier silently leaves bottom-nav visible on a deep editor (product-behavior change, no warning); forgetting ROUTE_TEMPLATES silently degrades diagnostics grouping. (A3-11)
2. Step 1 "which feature family owns it" — the sanctioned family list omits `components/forms/` and `components/ui/` (A3-07); a form-heavy screen has no documented home for its shared pieces.
3. Text-density mechanics ("caps are enforced; «جارٍ» excluded; prefer regex literals") are described operationally but the caps table itself lives only in `scripts/text-density-count.py` — the agent must read the script to learn the numbers.
**Verdict:** workflow complete and ordered; risk is concentrated in the unguarded triple registration.

### (b) Add a new primitive
**Governed by:** EXTENSION_PLAYBOOK §B + COMPONENT_CONTRACTS + ADR-001.
**Workflow traced:** prove 2–3 same-meaning usages → write contract in COMPONENT_CONTRACTS → place in layer → tests in `primitives.test.tsx` → styles in `primitives.css` (`--vf-*` only) → "record in the source-of-truth matrix and the component catalog".
**Friction points / wrong-change risks:**
1. **Two catalogs, one declared historical.** The playbook's final step points at the run-folder `SOURCE_OF_TRUTH_MATRIX.md`/`COMPONENT_CATALOG.md` (completed-run artifacts), while the permanent homes are `docs/architecture/SOURCE_OF_TRUTH.md`/`COMPONENT_CONTRACTS.md`. An agent following the letter updates the archive and the permanent contract never hears about the primitive. (A3-10)
2. **Precedent contradicts the entry rule:** §B.1 demands 2–3 real usages, but `Row` and `Field` shipped in W2 with **zero** production consumers ("available for later waves"). An agent can cite this to ship an unconsumed primitive — exactly the speculative abstraction ADR-001 forbids.
3. **Placement ambiguity:** `MoneyWithUnit` — documented as a primitive in COMPONENT_CONTRACTS — lives in `components/presentation/DisplayValue.tsx`, not `components/primitives/`. Copying that location for a new value-display primitive creates a third home; copying the folder rule contradicts the documented precedent.
4. No mechanical gate checks that contract doc + tests + styles were actually added (review-only).

### (c) Add a new token
**Governed by:** EXTENSION_PLAYBOOK §C + ADR-002 + CHANGE_PROTOCOL.
**Workflow traced:** change the authoritative definition once in `vf-tokens.css` (Standard change = owner decision in Documents first) → grep consumer inventory → visual/responsive checks → guard stays green → record old/new/rollback.
**Friction points / wrong-change risks:**
1. **The "ONE place" invariant has a mechanical hole (A3-02):** the design-token guard sanctions *any* `:root`/`.dark`/`@theme` block in *any* CSS file, and `vf-tokens.test.ts` resolves `var(--vf-*)` references **only from index.css**. A future agent who defines a new `--vf-foo` in `index.css :root` (the natural home of Micro runtime names) and consumes it from `primitives.css` or TSX passes every guard with a second token-definition site live. The W1 "0 tokens defined in more than one file" was a census, not a guard.
2. Value changes are well guarded: any of the 18 approved hexes disappearing (or a retired value appearing) fails `vf-tokens.test.ts`, correctly forcing Standard-first. Light-theme changes are the best-guarded scenario of the seven.

### (d) Add a new state marker (presentation/stateAdapter)
**Governed by:** EXTENSION_PLAYBOOK §D + ADR-003 + stateAdapter.test.ts.
**Workflow traced:** preserve product words (frozen by tests) → update the adapter if the semantic mapping changes → never bypass with a direct tone → grep word consumers → test pending/unknown/zero/error semantics; keep voids distinct.
**Friction points / wrong-change risks:**
1. The sanctioned path is genuinely well guarded: the **union lockstep test** (`stateAdapter.test.ts:57`) fails if `MicroActivityStatus` drifts from `application/activity/activityService`; permissible-tone, void-distinctness, and word-preservation tests all exist. Adding a new activity status forces adapter + dictionary + tests together.
2. But a second file must change that the playbook never names: **`markers.tsx` `ICON_BY_ROLE`** — a new markerRole compiles nowhere until mapped there (COMPONENT_CONTRACTS documents StateMarker, but workflow D omits the step).
3. **The main wrong-change risk is the parallel surface-tone system (A3-03):** an agent adding a "state" to a decision panel will find the local precedent (`G5DecisionPanel.tsx:116` ternary → `data-tone="accent|danger|warning"`) more copyable than the adapter path; nothing in the permanent docs names this vocabulary or forbids extending it.

### (e) Add a new AUX shell behavior
**Governed by:** EXTENSION_PLAYBOOK §E + ADR-004 + AUX_CONTRACT.md.
**Workflow traced:** verify safe areas/keyboard/back/focus/scroll/chrome/320px → run shell-adjacent suites (15 sheet tests, navigation contracts, lock gates, unsaved-changes — all located and counted) → update `AUX_CONTRACT.md` and architecture §6 if an invariant changed.
**Friction points / wrong-change risks:**
1. **Archival home problem:** E.3 instructs updating `AUX_CONTRACT.md` "(run folder)" — a dated, completed-run artifact. Post-run AUX invariants have no living contract file except the two-paragraph §6 of UI_AUX_ARCHITECTURE. (A3-10)
2. **Policy-in-shell precedent:** ADR-004 says the shell does "dispatch only, never product policy", but the sheet already encodes the cash_drawer-default-sale-destination policy. An agent adding a new quick action cannot tell from the docs whether default-value policy belongs in the shell (precedent) or the form (ADR-004 text). Wrong placement compounds silently.
3. Suite inventory is accurate and discoverable (3 test files under `components/layout/`).

### (f) Add a new feature pattern
**Governed by:** EXTENSION_PLAYBOOK §F + ADR-005 + FEATURE_PATTERN_CATALOG.md.
**Workflow traced:** keep product meaning in the feature boundary; pattern composes primitives; define the full state matrix (data/loading/empty/error/pending/unknown); never add implementations to the Standard; "document in the feature-pattern catalog".
**Friction points / wrong-change risks:**
1. **The catalog is a run-folder artifact with no successor.** `FEATURE_PATTERN_CATALOG.md` lives under `planning/micro-standard-ui-aux-integration-2026-09/`; ADR-005 (permanent) says patterns live in `components/<family>/` but hosts no catalog. After this run, a new pattern has **no documented living registry** — the instruction "document in the feature-pattern catalog" points at a closed run. (A3-10)
2. "A pattern without its state matrix and tests is incomplete" — review-enforced only; no guard counts states or tests per pattern.
3. The six-pattern inventory itself remains accurate against the tree (verified representative files).

### (g) Change the theme (light values / dark boundary)
**Governed by:** EXTENSION_PLAYBOOK §C (light) + §G (dark prep) + ADR-007 + DARK_MODE_BOUNDARY.md.
**Workflow traced (light):** single edit in `vf-tokens.css`; consumer inventory; captures; `vf-tokens.test.ts` enforces the 18 verbatim approved values (any light-value change fails tests until the Standard itself changes — by design, Standard-first). **Traced (dark):** extend semantic roles only inside the isolated boundary (`styles/semantic-roles.css` proposal, 19+ roles); parity matrix (role × surface × state, contrast floors); separate owner gate; additive rollback.
**Friction points / wrong-change risks:**
1. **DARK_MODE_BOUNDARY.md line 10 misdescribes today's resolution** (A3-04): primitives do *not* resolve surfaces through mode-adaptive aliases — `.dark` never re-declares `--vf-*`, so ~30 primitive bindings (chip surface, save/commit/secondary backgrounds, marker hues) are light-locked. A dark-wave agent scoping from line 10 would under-scope the remapping work; the semantic-roles proposal is the right mechanism, but the "current state" paragraph actively misleads.
2. **Dark is user-reachable now** (`ThemeContext` default `"system"` + header toggle): OS-dark users already see the unaudited legacy palette with light-locked primitives (commit button ≈1.1:1 affordance on dark canvas). Declared honestly as not-performed, but "NOT activated" in the docs reads stronger than the runtime reality; a future agent could wrongly assume no user can reach `.dark`.
3. No guard protects `.dark` values beyond two spot assertions (`vf-tokens.test.ts:192-193`: canvas `#1c1917` + `--primary` binding) — acceptable given the boundary, noted for completeness.

---

## 7. Findings

| ID | Area | Evidence path | Status | Severity | Owner | Affected layer | Action | Dependency | Acceptance criterion |
|---|---|---|---|---|---|---|---|---|---|
| A3-01 | Feedback classification: permanent doc contradicts code | `docs/architecture/SOURCE_OF_TRUTH.md:16` ("primitives … never classify") vs `client/src/components/primitives/Notice.tsx:77-97` (FeedbackNote owns `/^تم[ت ]/`); run-folder `SOURCE_OF_TRUTH_MATRIX.md:79` documents the opposite; `FeedbackNote` absent from `COMPONENT_CONTRACTS.md` | CLOSE_BEFORE_NEXT_PHASE | MEDIUM | MICRO_MAINTAINER | docs/architecture + primitives | Amend SOURCE_OF_TRUTH row to name FeedbackNote as the ratified centralized classifier; add the FeedbackNote contract section (props `word`/`advisory`, regex rule, 8 consumers) to COMPONENT_CONTRACTS | none | A future agent reading only permanent docs reaches the correct FeedbackNote conclusion; no doc says "primitives never classify" |
| A3-02 | Token single-source invariant only partially guarded | `scripts/design-token-guards.py:70-84` (any `:root`/`.dark`/`@theme` zone passes) + `styles/vf-tokens.test.ts:140-146` (resolves refs from index.css only) — a new `--vf-*` defined in `index.css :root` and consumed from `primitives.css`/TSX passes all guards | CLOSE_BEFORE_NEXT_PHASE | MEDIUM | MICRO_MAINTAINER | token mapping (layer 2) | Add a guard test: zero `--vf-*` declarations outside `vf-tokens.css` (repo CSS scan) | none | Test fails on any second `--vf-*` definition site |
| A3-03 | Parallel surface-tone vocabulary unregistered; local state→tone mapping outside adapter | `index.css:386-395,458-528,1746,1957-1963,2908-2987,3229-3242` (`data-tone` accent/warning/danger/update/offline); direct page assignments `Orders.tsx:152`, `Statement.tsx:501,561`, `DirectSaleEditor.tsx:599,608`, `Schedule.tsx:950`; local mapping `G5DecisionPanel.tsx:116-122`; `SOURCE_OF_TRUTH.md:14` "pages (no direct data-tone)" | OWNER_DECISION_REQUIRED | MEDIUM | OWNER | state presentation + feature patterns | Owner registers the surface-tone grammar (or routes surface state through the adapter); document the vocabulary and its dark-layer selectors; scope SOURCE_OF_TRUTH line 14 to marker tones | A3-04 (dark doc fix benefits from the same decision) | Surface tones have one authoritative definition location; a new state→tone need has a documented path; no page-level tone assignment outside it |
| A3-04 | Dark-boundary doc misstates primitive mode-resolution; dark user-reachable with light-locked surfaces | `planning/.../DARK_MODE_BOUNDARY.md:10` + `SOURCE_OF_TRUTH_MATRIX.md:57` vs `styles/primitives.css` (`--vf-surface/ground/ink` bindings) + `index.css:107-151` (`.dark` never re-declares `--vf-*`) + `contexts/ThemeContext.tsx:20-25,47-49` (system default + toggle) | CLOSE_BEFORE_NEXT_PHASE | MEDIUM | MICRO_MAINTAINER | dark boundary docs | Correct line 10 / divergence 3 to state that primitive surfaces are light-locked `--vf-*` and the semantic-roles wave must remap them; note `.dark` is user-reachable via system preference | none (doc edit; code change belongs to the owner-gated dark wave) | A dark-wave agent scoping from the boundary doc enumerates the ~30 light-locked primitive bindings as work items |
| A3-05 | `current-state.md`/`todo.md` not updated by branch; merge step unlisted | `git diff origin/main..HEAD -- docs/operations/ todo.md` empty; `docs/operations/current-state.md` last updated 2026-09-13 (Group 11), zero mention of Standard integration; `AGENTS.md` §8 designates it the live reference | CLOSE_BEFORE_NEXT_PHASE | MEDIUM | NEXT_EXECUTION_AGENT | docs/operations | Include the current-state + todo update in the merge/next-phase kickoff (per AGENTS.md §9), recording the integration branch, its guards, and the owner registers | merge decision (orchestrator/owner) | After merge, first-read of current-state.md describes the Standard integration and points to docs/architecture |
| A3-06 | "Primitives are leaves" rule not mechanically enforced | `eslint.config.js` (no rule for `components/primitives` → pages/app/application); `scripts/check-runtime-cycles.mjs` (cycles only, a DAG edge primitives→application passes); rule stated in `planning/.../IMPORT_BOUNDARIES.md` rule 2 + `COMPONENT_CATALOG.md:3` | CLOSE_BEFORE_NEXT_PHASE | MEDIUM | MICRO_MAINTAINER | import boundaries | Add an eslint `no-restricted-imports` pattern for `components/primitives/**` (ban `@/pages/*`, `@/app/*`, `@/application/*`, `@/storage/*` value+type) mirroring the STR-005 rule | none | A primitive importing application/pages fails lint |
| A3-07 | Layer-5 directory enumeration omits `components/forms/` and `components/ui/` | `docs/architecture/UI_AUX_ARCHITECTURE.md:24` lists 9 families; live tree has 11 component dirs (`forms/`, `ui/` missing) | CLOSE_BEFORE_NEXT_PHASE | LOW | MICRO_MAINTAINER | architecture docs | Add both directories to the layer-5 list with one-line ownership (forms = cross-feature form infrastructure; ui = vendored radix bridge) | none | The ladder accounts for every directory under components/ |
| A3-08 | Census wording inaccuracies in ADR-006/008 + MIGRATION_STATUS | `ADR-008:13` + `MIGRATION_STATUS.md:8` "9 choice toggles → ChoiceRow (… + ActualTimePanel …)" vs `components/presentation/ActualTimePanel.tsx` (no ChoiceRow; plain Buttons at 273/329/377; actual ChoiceButton count = 8); `ADR-006:5` "299 across 80 files" vs actual 81 (EXECUTION_REPORT correct) | CLOSE_BEFORE_NEXT_PHASE | LOW | MICRO_MAINTAINER | ADRs + MIGRATION_STATUS | Correct the ActualTimePanel parenthetical (describe it as a Button weight split, not a ChoiceRow toggle) and the 80→81 file count | none | All census sentences match grep-reproducible counts |
| A3-09 | Guard scope gaps: files outside client/src unscanned; inline styles unguarded (2 precedents) | `client/index.html:9-10` (`#faf9f5`/`#1c1917`), `vite.config.ts:262-263` (`#FAF9F5`) outside `design-token-guards.py` CLIENT_ROOT; inline styles at `pages/DirectSaleEditor.tsx:631`, `components/forms/UnsavedChangesGuard.tsx:293` | SAFE_TO_DEFER | LOW | MICRO_MAINTAINER | guards | Extend guard scope to `client/index.html` + `vite.config.ts` hex allowlist; add an inline-style lint rule or document the structural-reset exception | none | No raw color can enter the app shell files unnoticed; inline-style policy is stated |
| A3-10 | Playbook points future agents at completed-run archival docs as living registries | `EXTENSION_PLAYBOOK.md` B.6 ("source-of-truth matrix and the component catalog"), E.3 ("AUX_CONTRACT.md (run folder)"), F.4 ("feature-pattern catalog") → all under `planning/micro-standard-ui-aux-integration-2026-09/`; `COMPONENT_CONTRACTS.md:3` declares the catalog historical; `components/primitives/index.ts:4` points to COMPONENT_CATALOG | CLOSE_BEFORE_NEXT_PHASE | LOW | MICRO_MAINTAINER | extension playbook | Reword B.6/E.3/F.4 to name permanent homes (COMPONENT_CONTRACTS/SOURCE_OF_TRUTH/UI_AUX_ARCHITECTURE §6) and mark run-folder docs read-only historical; fix the barrel comment pointer | A3-01 (same doc family) | Every "record/document" instruction names a living file that survives the run |
| A3-11 | Route triple-registration (MicroRouter ↔ routeClassifier ↔ ROUTE_TEMPLATES) unguarded | `app/MicroRouter.tsx`, `app/routeClassifier.ts` (regex list), `application/diagnostics/routeTemplate.ts` (58 templates) — no test compares them; `SOURCE_OF_TRUTH.md:27` claims the sync | SAFE_TO_DEFER | LOW | MICRO_MAINTAINER | app/routing | Add a test asserting every router path has a classifier disposition and a ROUTE_TEMPLATES entry | none | Adding a route without one of the three registrations fails a test |
| A3-12 | Unregistered duplication: Settings verified-export download sequence duplicated | `pages/Settings.tsx:271-296` vs `307-328` (Blob → objectURL → link.click → 30s revoke → markVerifiedExport, verbatim ×2); absent from MIGRATION_STATUS registers | SAFE_TO_DEFER | LOW | MICRO_MAINTAINER | pages/Settings | Extract a shared `downloadVerifiedExport()` helper or register the duplication with a reason | none | One implementation of the verified-export download path |
| A3-13 | Stale permissive allowlist + misleading primitives.css header | `styles/vf-tokens.test.ts:38-46` MICRO_KEPT retains 3 dead hexes (`#3e5c76/#e8eef3`, `#b7b2a6` — "dead, W6 inventory"); `styles/primitives.css:2` header scopes the file to "components/primitives" while containing `MoneyWithUnit` (components/presentation) styles at :472-484 | SAFE_TO_DEFER | LOW | MICRO_MAINTAINER | token tests + styles | Drop dead hexes from MICRO_KEPT (or assert their absence); widen the primitives.css header comment to name the presentation-layer exception | none | Allowlist matches the live :root hex set; header names every component family it styles |

**Verified-clean (no finding needed):** 118-token census; 18-approved-value traceability to the Standard; zero raw hex/rgb in TSX/TS; single `--vf-*` definition site in the live tree; primitives props/consumers vs COMPONENT_CONTRACTS; AUX shell purity per ADR-004; 299-Button/81-file and 8-ChoiceButton censuses; 15 sheet tests; MIGRATION_STATUS preserved items (14/14 present in code); stateAdapter semantics + 15 tests incl. union lockstep; legacy-class census guard scope; eslint/layer-boundary fixture coverage; ROUTE/classifier/filesystem page count (52); EXECUTION_REPORT §8 one-step-behind SHA record (inherent fixed-point, disclosed; true tips held in CONTEXT.md).
