# Micro Standard v2 → Micro — Read-Only Integration Comparison Report

**Deliverable:** `MICRO_STANDARD_TO_MICRO_READONLY_INTEGRATION_COMPARISON_REPORT.md`
**Task type:** Read-only, independent integration and UI/AUX comparison — analysis and planning only. **No source repository, package, branch, or file was modified, created, or deleted by this task.** No code, patches, commits, or uploads were produced by the comparison itself.
**Date of analysis:** 2026-09-14 (Asia/Amman)
**Method:** Five-agent read-only inspection (inventories → mapping → boundary scan → feature gaps → adversarial cross-check), all findings re-verified against the exact commits listed in §2. Prior reports, Prototype v0, and session artifacts were excluded as decision sources.

---

## 1. Executive verdict (plain language)

The Micro Standard v2 Final Copy is an executable, self-consistent visual foundation — and Micro already shares its **skeleton**. Both sides agree on canvas `#FAF9F5`, white surface, recessed `#F0EEE6`, elevation values, control radii 12/16/20px, the 4px spacing grid, IBM Plex Sans Arabic + IBM Plex Mono, English digits with `د.أ` outside the number, numeric bidi isolation, a 4-destination RTL bottom navigation with a central create FAB, route-kind chrome gating (deep flows hide the nav), honest "غير مسجل — سجّله" void chips, safe-area handling, and keyboard chrome hiding.

But Micro currently runs a **divergent identity layer**: the retired v0 palette (`#CC785C` brand family, `#1F1E1D` ink, teal `#079FA0` accent, bespoke success/danger/warning/withdrawal colors) — **none of the 18 approved Standard hex values exists anywhere in the Micro repository today** — plus a fully live dark mode and theme toggle that the deliberately light-only Standard does not cover. The Standard's named action classes (Create `#D97757`, ordinary save `#F5F4ED` + `#C96442` pressed edge, high-consequence `#141413`), the selection edge, row state markers/edge stripes, the value-zone period/delta slots, the period chip, and skeletons are not implemented in Micro; conversely, six Micro runtime patterns (fact-state triad, documented-correction lifecycle, next-action rows, knowledge states, decision-card grammar, inline no-toast feedback) are **richer than anything the Standard can express** and must be preserved as Micro-owned Feature Patterns.

The gap is therefore **not structural**. It consists of: one runtime token-mapping layer (the strategy's layer 2), roughly a dozen contract adapters, a small set of concrete defects that need no decision (a warning chip that renders success-green, a dead tooltip provider, ≈256 duplicated CSS lines), and ~13 explicit owner decisions (palette adoption, FAB geometry, navigation labels, period control presentation, row state markers, dark-mode/teal scope, the 11–12px type floor, state-word orthography, knowledge states, the no-toast regime, and reader-route chrome depth). Under the fixed strategy — **Contract-first + Token-driven + Component-driven + Feature-oriented + Composition-based** — adoption is a bounded, low-risk sequence of five waves, not a rewrite, and does not require touching Micro's domain, application, or storage meaning, which are already cleanly layered.

## 2. Exact repository URLs and commit SHAs actually read

| Source | URL | Branch | Commit SHA (verified, read-only clone) | Commit date / subject |
|---|---|---|---|---|
| Micro (implementation) | https://github.com/Qays7753/Micro | `main` | `c0469e265f24c70427eb7826dee717be117cff87` | 2026-09-13 11:52:12 +0300 — "Merge pull request #159 from Qays7753/remediation/micro-full-hardening-2026" |
| Documents (Standard owner) | https://github.com/Qays7753/Documents | `main` | `864263c190f5d3da6041acfafb0720e85ac6e320` | 2026-09-13 14:00:23 +0000 — "docs: record final copy main publication verification" |
| Standard package | https://github.com/Qays7753/Documents/tree/main/micro-standard-v2 | `main` @ `864263c` | 31 files on disk | `MANIFEST.json` self-describes "29 core + 2 metadata" |

Notes:
- Documents `main` had advanced past the previously recorded `dfa8bf7d7f7a2c01f256d4c77d359c8a5770d60b`; this report reads the **current** `main` above, re-verified at clone time and re-checked before publication.
- The Standard Final Copy on `main` is the only Standard source used. Historical branches (`micro-standard-v2-foundation-development`, superseded runs), old prototypes, old prompts, and the earlier comparative review were **not** used as decision sources.
- Micro area inspected: `apps/prototype-web/client/src/` (all subfolders), `src/domain/`, `scripts/design-token-guards.py`, `docs/` (UI/design-relevant subset), `tests/`, root configs (`tsconfig.json`, `vite.config.ts`, `index.html`, `public/micro-mark.svg`, `package.json`).

## 3. Scope and limitations

**In scope:** mobile UI/UX organization; AUX/shell organization; design-token and component-contract mapping; shared primitives and composition boundaries; feature-pattern gaps; screen/route composition; UI source-of-truth conflicts and duplication; a read-only Structure/Architecture/Code Organization Scan limited to the UI/AUX/design-system boundary; responsive/RTL/accessibility/states/overlays/navigation patterns; future maintainability and safe change propagation.

**Explicitly out of scope (and not analyzed):** AI Assistant/LLM/chatbot/chat; backend redesign; financial formulas, posting, reversal, accounting policy, sync policy, permissions, product semantics; security/performance/infrastructure/database audits; the Accounting repository; Prototype v0 as a source of terminology, routes, data, or behavior; any code generation, editing, file moves, branches, commits, merges, uploads, or deployment.

**Limitations:**
1. Static, read-only repository analysis. The app was **not** built or run; no browser, device, or screen-reader session was performed. Runtime behavior claims are limited to what code and CSS deterministically imply.
2. The Standard's own verification is local headless-Chromium only; it explicitly does **not** claim physical-device or screen-reader testing (`README.md` L30; `coverage-matrix.json` `requires_separate_testing: ["physical_device","screen_reader"]`). This comparison inherits that boundary.
3. All quantitative claims were adversarially re-verified (Agent 5). Corrected figures are used throughout: 57 `<Route>` elements; 60 page `.tsx` files; 47 non-test component files; 29 deep-flow regexes; 25 `canonicalReturnFallbacks`; 275 exact `د.أ` literals across 53 files; 130-line CSS block triplicated (≈256 redundant lines, not ≈380); Standard/Micro elevation is **value-identical** (E2 differs textually: `0.10` vs `0.1`), not byte-identical.
4. Micro `index.html` meta `theme-color` carries canvas colors (`#faf9f5`/`#1c1917`) rewritten at runtime by `ThemeContext` — it is **not** a `#CC785C` twin (an earlier assumption corrected in §Annex A).
5. No access token was used or needed; both repositories were read anonymously.

## 4. Five-agent findings (by role)

**Agent 1 — Micro UI/AUX Inventory Analyst (COMP-1).** Produced the factual map: 57 routes through `MicroRouter.tsx` nested `MicroAppShell ▸ StartupGate ▸ AppLockGate ▸ Switch`; `routeClassifier.ts` splits setup/deep/surface and drives chrome visibility; `navigationContract.ts` is a hardened referrer/deep-link contract; shell = translucent blurred bottom nav (z-30) with in-grid FAB, header with scroll border and theme toggle, `QuickActionSheet.tsx` (761 lines, 4 modes, in-sheet sale/expense completion), full-screen lock veil, PIN gates, calm ErrorBoundary. Census: every component live except the never-rendered Tooltip API; `DisplayValue` is the most-imported component (49 importers); `presentation/formatters.ts` is the single money/date/digit authority; `index.css` mapped section-by-section (6,962 lines, 431 `.micro-*` families, only 2 hex literals outside token zones, 157 rules at 11–12px, ≈256 duplicated lines); UI guard suite ≈ 48 files / ≈260 `it()` blocks, of which exactly **one** (`U09.css.test.ts`) reads CSS.

**Agent 2 — Standard Contract Mapping Analyst (COMP-2).** Mapped the 31-file Final Copy: 18 approved hex values; 120 declared token properties; named action contracts (create/save/commit/destructive) all bound as aliases of approved values; 10-state financial matrix (word + marker + color); 6 screen-level states; 13-pair contrast table; phone geometry 320/360/390/430 @ 100/130/200%; deliberately-not-owned list (link-ink unratified, no dark mode, tool-result anatomy deferred as decision S-12, charts limited to one question-led family, physical device/screen reader unclaimed). Hex-presence audit: `#D97757`, `#C96442`, `#141413`, `#629987`, `#B53333`, `#2C84DB`, `#1490FF` → **zero hits** in Micro; overlap by value exists only for canvas/surface/recessed/elevation/radii/fonts/spacing. Classification: ≈7 token families transfer DIRECT; the entire `--vf-*` layer is a RUNTIME TOKEN MAPPING; ≈12 contract families need ADAPTERS; charts/tool-result/relationship-bar/edge-stripe have NO Micro counterpart.

**Agent 3 — Reuse, Composition & Boundary Analyst (COMP-3).** Boundary verdict: the downward layering (domain ← application ← UI) is disciplined — zero application→UI imports, zero relative layer escapes, `@micro-domain` alias used 212×, tsx contains zero color literals, inline styles ≈ zero. The gaps sit in the contract/primitive layer: `--color-border` triple alias chain; `--primary` changes role between light/dark; scrim implemented twice (one literal); 3 coexisting sheet systems; success-only status chip; 18 card variants; 13 row families in 2 anatomies; 4 empty-state variants; no Notice/Toast owner (34 pages hold local `setMessage`/`setNotice`); 275 inline `د.أ` compositions vs `formatMoneyWithUnit` in 6 files; 17 files import storage types; 2 `localStorage` leaks; 1 component→page type edge; guard suite cannot see tokens/CSS. Token-change propagation test: spacing/radius/elevation propagate; identity hexes fail to propagate to PWA manifest, logo SVG, and dark-mode re-declarations.

**Agent 4 — Feature-Pattern & Screen-Gap Analyst (COMP-4).** Surface-by-surface: Home (fact-state triad + road chips + priority block + away digest), Finance (period = native month inputs + quick-range text buttons; prose truth block; documented-correction lifecycle with impact previews; G5 statuses), Orders (row anatomy without state markers; decision panel; agreement memory; deposit panels), Inventory (**defect: `data-status="warn"` chip has no CSS rule → renders success green**), Suppliers/Parties (one search field; no sort), Cash (ledger rows, count flow, reversal confirmations), Tools (integrity PASS/WARN/FAIL rows; no charts), Schedule (capacity/recurrence/buckets; **no calendar grid or picker beyond `type=date`**), cross-cutting (0 tables, 0 charts, 0 skeletons, 0 toasts; 3 real sheets; destructive confirmation via inline impact panels + danger button, not the high-consequence dialog; 4 empty-state variants; ScreenState re-implemented ≈30×). Consolidated 22-item gap register G4-01..G4-22.

**Agent 5 — Independent Synthesis & Quality Reviewer (COMP-5).** Adversarial re-verification of 18 high-stakes claims: 13 CONFIRMED, 4 PARTIAL (numeric corrections listed in §3), 1 CONFIRMED-with-caveat (meta theme-color). Resolved all inter-agent contradictions (route count 57; duplication ≈256 lines; `د.أ` = 275/53 files; EventsLayer `د.أ` = ×12 not ×17; "byte-identical" downgraded to value-identical). Truth-source audit: clean — only the two pinned repos at the SHAs above were used; no Prototype v0 content, old report, or assumption was treated as product truth. Issued the final conservative classification (§7) and the top-5 safest next steps (§18).

## 5. Current Micro UI/AUX inventory (as read @ `c0469e2`)

Paths below are relative to `apps/prototype-web/client/src/` unless noted.

**5.1 Routes and chrome gating.** 57 `<Route>` entries + nested `<Redirect path="/review" to="/finance">` + catch-all `NotFound`; all pages lazy inside one Suspense with `role="status"` Arabic route-loading state. `app/routeClassifier.ts` (29 deep-flow regexes) classifies `setup | deep | surface`; `showsGlobalChrome()` keeps header+bottom nav+FAB on surfaces only. `app/navigationContract.ts` (200 lines) is the only referrer vessel (`?from=<internal-path>`, whitelist of 8 deep-link params, 25 canonical fallbacks + prefix rules). `app/navigation.ts`: `primaryNavigation` = `مشروعي الآن /`, `العمل /orders`, `مالي /finance`, `أدواتي /tools` + centered FAB `سجّل`. `app/StartupGate.tsx`: one boot per session, persistent-storage request, first-run → `/setup`, four distinct Arabic storage-recovery states.

**5.2 Shell anatomy.** `components/layout/MicroAppShell.tsx` (122 L): `data-route-kind`, `data-keyboard-open` via `visualViewport` listener (keyboard-open hides header+nav, index.css L775–777), QuickActionSheet lazy + idle-prefetched, `CONTEXT_REPEATS_H1` suppresses header context label when duplicating the page h1. `AppHeader.tsx` (61 L): brand lockup + context span + settings + **theme toggle**; `data-scrolled` strengthens border. `BottomNav.tsx` (71 L): fixed translucent blurred nav, `padding-bottom: env(safe-area-inset-bottom)`, 5-column grid with **FAB in-grid** (56×56, `translateY(-20px)`, `border-radius: 50%`, `background: var(--primary)`, label `سجّل`, opens QuickActionSheet); active pill = teal accent. `QuickActionSheet.tsx` (761 L): vaul drawer, 4 modes (menu / sale-form / expense-form / receipt), in-sheet discard `alertdialog`, idempotent submit, honest wallet-attribution receipt. `components/security/AppLockGate.tsx` (204 L): full-opacity veil (z-60) over `inert` content (cover, not redirect); `DataActionPinGate.tsx` for data-leaving actions; `ErrorBoundary.tsx`: focus-receiving Arabic card, no stack traces, local incident id. Z-ladder: sticky-save z-20 < nav z-30 < header z-40 < dialog overlay z-50 < dialog/sheet/lock z-60 (comment-enforced at index.css L190).

**5.3 Live component census (47 non-test files; all live except Tooltip API).** Highest reuse: `presentation/DisplayValue.tsx` (49 importers — `MoneyValue/IntegerValue/QuantityValue` with `bdi dir="ltr"`), `forms/EnglishNumberInput.tsx` (40), `forms/UnsavedChangesGuard.tsx` (26 pages + tests), `micro-form-actions` footer bar (51 files), `EnglishQuantityInput`, `LocalDateField`, `useFormDirty`/`useFormDraft`/`FormDraftRestoreBanner`. Feature groups: finance (EventsLayer 862 L, FinancePeriodResultSection 501 L, CorrectionsLayer, DepositsLayer, RestatementNote, AllocationReviewCard, CorrectionPreview, G5DecisionPanel 346 L), order (AgreementContextPanel, ActualMaterialPanel, OrderEventLog), orders (OrderDepositPanels 417 L), catalog sections ×5, cost/loans sheets (MaterialSheet, RepaymentSheet — 3 vaul sheets total), owner sections ×2, security ×3, settings ×4, presentation (DecisionPanel, InfoCard, ActualTimePanel, EventEffectPreview), pwa ×3.

**5.4 Presentation layer.** `presentation/formatters.ts` (148 L): `formatMoneyMinor` (Intl `en-US`, English digits always), `formatMoneyWithUnit` (`"<n> د.أ"` — canonical unit composition), Arabic 6-form plurals, exact milli quantities, numeric `DD/MM/YYYY` dates (no month names), Asia/Amman datetimes. Supporting: `cashCountMessages`, `plurals`, `g5Plurals`, `orderAgreementPresentation`, `catalogPresentation`, `ownerEntitlementPresentation`, `activityLabels`. Digits additionally enforced at entry by `EnglishNumberInput`/`EnglishQuantityInput` + `application/input/englishNumeric.ts` normalization.

**5.5 Global CSS map (`index.css`, 6,962 lines — the only stylesheet).** L9–31 `@theme inline` shadcn bridge; L33–75 `:root` micro tokens (25 colors: canvas/well/surface/border/divider/4-step text ramp/brand family `#cc785c·#b4613f·#964e33·#f4e4db`/teal `#079fa0·#057b7c·#e3f5f5`/success `#256b4a·#e4f2ea`/danger `#b42318·#fbe7e6`/warning `#7a5c20·#f6eccf`/withdrawal `#3e5c76·#e8eef3`; space 4→32; radii 12/16/20; elevation ×3; 2 easings); L76–94 shadcn aliases onto micro tokens; L97–144 `.dark` full mirror; L146–181 base; L183–6962 chrome + shared + feature families. Metrics: 440 unique selectors; 431 `.micro-*` family names; 30 media queries; 35 `!important`; 2 hex literals outside token zones (one is the sanctioned dialog scrim `color-mix(in srgb,#1f1e1d 45%,transparent)`); `font-size` 11px×38 + 12px×119 (+13px×98); 631 `--space-*` uses vs 7 raw margins; 105 logical properties and **zero physical `rtl:`** rules; `border-radius:999px` ×11; reduced-motion declared in 4 separate blocks; **triple-duplicated ≈130-line block** (`.micro-financial-pulse` at L1822/2074/2599, `.micro-home-heading` ×3, copies 1&2 byte-identical) ≈256 redundant lines. Build-time guard: `scripts/design-token-guards.py` (npm `design-guards`; raw-hex ban outside token zones with one sanctioned scrim string; part-level scale whitelists including a 13-size font whitelist that currently entrenches 11px; z whitelist 0–70) — **not** a palette freeze; passes today (exit 0).

**5.6 Docs and tests.** UI-relevant docs: `docs/product/design-system-v1.md` ("source of truth for values: index.css"), `docs/product/mobile-ui-ux-reference-v1.md`, `docs/contracts/26-navigation-referrer-and-deep-link-contract.md`, `docs/contracts/37-local-app-lock-contract.md`, decision records v3/v4/v5, per-wave UX acceptance reports, `AGENTS.md` mandatory-reading row, three executable `ai-skills` UI checklists. Tests: 165 test files in client/src; UI-guard subset ≈ 48 files / ≈260 `it()` blocks (navigation 29, lock gates 14, QuickActionSheet 15, unsaved-changes 18, chrome/PWA 15, journey suites 109, page `.ui` suites 70); `U09.css.test.ts` is the **only** CSS-reading test (3 touch-target string assertions); `U01` asserts LTR numeric isolation (English digits, no Arabic-Indic digits); nothing fails if a token value, hex literal, `!important` count, sheet count, or z-index drifts.

**5.7 Dead / duplicated / oddity flags.** `components/ui/tooltip.tsx`: only `TooltipProvider` mounted (`App.tsx` L15); Tooltip/Trigger/Content never rendered; a radix chunk is still shipped for it (`vite.config.ts` L334–335). Triple-duplicated CSS block (above). Reader-depth inconsistency: `/assets/:id` and `/loans/:id` classified `deep` (chrome hidden) while reader peers `/orders/:id` and `/cash/wallet/:id` are `surface`. No toast system (Toaster removed by decision Q-003; feedback is inline `role="status"` ×110 / `role="alert"` ×53 + receipt/outcome cards). No skeletons. No charts. No `<table>` elements.

## 6. Standard contract inventory (Final Copy @ `864263c`, 31 files)

**6.1 Package.** Governance: `README.md` (Final Copy identity + verification boundary), `MANIFEST.json`, `RELEASE.md`, `decision-log.md` (decisions 1–14 incl. token backfill, alpha derivatives, button ladder, gold retirement, reduced-motion fix, chart scope, S-12 deferral, text-bearing-Clay contrast fix, prototype boundary), `verification-report.md` (8 verified areas, explicit not-tested list), `self-critique.md`, `source-inventory.md`, `coverage-matrix.json`. Contracts: `visual-direction`, `color-system`, `surface-system`, `typography`, `spacing-radius-elevation`, `button-system`, `input-system`, `data-display-system`, `component-contracts`, `component-states`, `empty-loading-error-states`, `navigation-shell`, `overlay-system`, `motion-interaction`, `iconography`, `responsive-geometry`, `accessibility`, `content-guidelines`. Operative: `design-tokens.css` (120 properties) + `design-tokens.json`; gallery `component-gallery.html/css/js` (12 demo families + evidence panel + behaviors).

**6.2 Approved palette = 18 hex values.** Surfaces `#FAF9F5 · #F5F4ED · #F0EEE6 · #FFFFFF · #E8E6DC · #D1CFC5 · #87867F`; ink `#141413 · #4D4C48 · #6B6962 · #FFFFFF · #55524A`; identity/semantic `#D97757` (clay — non-text identity only, 3.12:1), `#C96442` (pressed/chosen/current **edge only**, 3.90:1), `#2C84DB` info, `#1490FF` status, `#629987` success, `#B53333` error (6.02:1, the only text-safe semantic); pressed `#3D3D3A`. Alpha derivatives disclosed (scrim `rgba(20,20,19,.45)`, header `rgba(250,249,245,.86)`) — not new palette. Tint aliases bind `--color-negative-50/-on-tint/positive-100/primary-100/200` to existing approved values.

**6.3 Named action classes (owner-approved).** Create/add/FAB = Clay `#D97757` (text-bearing uses dark `#141413` ink; icon-only uses white icons; pressed `#C96442`; never a financial value). Ordinary save/confirm = Warm Tint `#F5F4ED` + ink `#141413`, pressed shows 2px `#C96442` inset edge, press ≠ success, completion = word + check marker. High-consequence commit/destructive = warm-ink `#141413` fill + white text + consequence word + icon + explanation + independent confirmation path. `--vf-btn-primary-*` is re-scoped to high-consequence only (decision 5).

**6.4 Component contracts (status 🟢 fully specified / 🟡 named-but-thin / 🔴 absent).** 🟢 Buttons (7 classes incl. loading/quiet-completion/disabled), icon buttons, Field/Input (5 variants), Surface/Card, Row + trailing amount slot (`row-amt` mono 15/600, end-aligned, `dir="ltr"`, `unicode-bidi:isolate`; divider inset to 72px), state slot + ≤3px edge stripe (always paired with state word), Tag/Chip (tag = word + leading semantic marker; chip selection = 2px `#C96442` inset edge + bold ink, never black fill), Sheet (20px radius, drag handle/expand, 84→94%, 240/180ms, focus trap, scroll lock), Dialog (high-consequence anatomy), Snackbar (warm-ink, 5s hold, `role=status`), Tabs/Segmented (thumb + underline variants with `#C96442` edge/underline), Filter surface (one control + staged chips until Apply), Navigation (4 destinations, 64px nav, active pill with Clay edge), Header (56px, translucent-on-scroll), FAB (56px Clay, r12, own gutter 80px above nav, must not cover amount/action columns), value zone (label/value/currency-unit/period/delta slots + 3 honest voids: unrecorded → action chip, unavailable → "غير متاح", measured zero → "0"), period chip (36px visual/44px hit; time semantics product-owned), quick-action rail, empty/loading/error/unknown family, charts (one question per chart; neutral series + one semantic mark; zero = 2px baseline mark; no-data = word+icon; loading skeleton; **text alternative** `بالكلمات:`; no chart library). 🟡 Tool-result anatomy (S-12 deferred), order-detail/balance/attention/party/receivable compositions (named, no anatomy). 🔴 Dark mode (deliberate), chart library/deep charts (deliberate), link-ink value (unratified — owner decision pending).

**6.5 States.** Financial matrix (10 states): draft مسودة, pending بالانتظار (clock, Info), posted تم (check, Success), failed فشل (alert, Error), cancelled ملغي (close, neutral), reversed عُكس (return, Info + audit preserved), reviewed رُوجعت (eye, Status), partial جزئي, due/overdue مستحق/متأخر, unknown غير معروف (never success/failure). Rules: every state = word + non-color marker; color never carries state alone; pending never reads success. Screen states: no-data / no-results / loading (skeleton, `aria-busy`) / failure (retry, input preserved) / unknown / pending. Interactive: pressed 0.97 @ 80ms + class edge; loading (spinner, label persists, duplicate submit blocked); quiet completion (check + past-tense word).

**6.6 Accessibility + geometry.** 13-pair contrast table (17.50/18.43 AAA text pairs; `#B53333` 6.02 text-safe; identity hues non-text only; text-bearing Clay must use `#141413`); dual focus treatment (2px outline on light controls; inset surface ring on filled); 44px touch floor (36px chips via `::after` hit area); 200% text @ 320px no horizontal overflow; logical RTL everywhere; numerals English, bidi-isolated; reduced-motion contract. Geometry: control 48, chip 36/44, radii 12/16/18/20/full, topbar 56, nav 64, FAB 56 @ 80px, sheet 84–94%, icons 20/24, type scale 28/20/17/15/15/13/12 + numeric hierarchy hero 28 / primary 24 / secondary 15 / tertiary 13 (financial facts never < 15px), motion 80/120/200/240-180/160-120/1500/5000ms, z 250/300/400/500.

**6.7 Deliberately not owned.** Financial policy/formulas/sync/backend; tool time semantics (product-owned); tool-result anatomy (S-12 deferred); link/action ink (constraint only — "incumbent live value remains an explicit owner decision"); dark mode; chart depth beyond one family; value/period/row slot *meaningful use* ("neutral contracts — their meaningful use depends on Micro product composition"); gold/amber family (retired); physical-device and screen-reader verification (explicitly unclaimed); Prototype as source of truth (decision 13); over-use of the ink fill ("Micro compositions must adopt the save/create classes rather than reaching for the ink fill").

## 7. Coverage and gap matrix

Full 12-column matrix (identical data delivered as `MICRO_STANDARD_GAP_MATRIX.csv`). Classifications are final (Agent-5-conservative): **14 fix now in planning · 13 needs owner decision · 13 defer · 6 preserve · 1 out of scope** (47 rows). Gap types used: `covered by Standard`, `runtime token mapping`, `shared UI primitive`, `AUX shell`, `Micro feature pattern`, `screen composition`, `product/owner decision`, `not in Standard by design`, `out of scope`.

| ID | Area | Evidence (Micro @ `c0469e2` unless noted) | Current state | Standard coverage | Gap type | Classification | Recommended next step | Dependency | Risk | Acceptance criterion | Rollback boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|
| GAP-01 | Identity palette | `index.css` L51–75, L111; `vite.config.ts` L263; `public/micro-mark.svg` L3; `index.html` L9–10 | Retired v0 palette live (`#cc785c/#b4613f/#964e33`, ink `#1f1e1d`, teal `#079fa0`, success `#256b4a`, danger `#b42318`, warning `#7a5c20`, withdrawal `#3e5c76`); zero hits of the 18 approved hexes | 18-value approved palette + action classes | runtime token mapping | needs owner decision | Owner approves adoption → one PR: `--vf-*` mapping + shadcn bridge re-bind + twins + guard freeze | Decision pack D-01; Wave 2 | Identity-defining; contrast re-verification needed | 18 hexes present byte-for-byte; contrast table re-computed; guards green | Revert token+mapping commit (single commit) |
| GAP-02 | Token mapping architecture | `index.css` L9–31, L33–95 | No `--vf-*` layer; micro tokens + shadcn bridge + `@theme inline` coexist via ordering accident | Standard tokens canonical; strategy names a runtime mapping layer | runtime token mapping | fix now in planning | Design the mapping file + bridge + guard update now; values land after D-01 | GAP-01 (values only) | Namespace collision if a non-inline `@theme` color is added | Single declared owner of `--color-*` namespace; zero visual change | Revert PR |
| GAP-03 | Identity twins | `vite.config.ts` L262–263; `micro-mark.svg` L3; `index.html` L9–10 | PWA `theme_color #CC785C` + logo fill are manual mirrors; meta carries canvas colors (runtime-rewritten) | Identity flows from tokens | runtime token mapping | needs owner decision | Single-source build-time injection, bundled with D-01 | D-01 | App chrome drifts from app identity | Manifest/logo/meta derive from token source | Revert injection |
| GAP-04 | `--primary` role drift | `index.css` L82 vs L131 | Primary button = brand-text brown in light, light terracotta in dark | Mode-symmetric button ladder | runtime token mapping | needs owner decision | Resolved inside the D-01 mapping (one decision, not two) | D-01 | Contract cannot state button appearance per mode | One primary role in both modes | Token revert |
| GAP-05 | Teal accent + dark mode | `index.css` L64–66, L97–144; `ThemeContext.tsx`; `AppHeader.tsx` L48–56; `App.tsx` L14 | Teal accent live (nav pill, text-action, focus ring); dark mode + toggle fully live (`switchable`) | Standard light-only; no link-ink ratified | product/owner decision | needs owner decision | D-02: decide teal fate + link-ink; D-03: dark-mode fate (keep/flag/freeze) | Independent | Standard cannot verify dark; unratified link ink | Recorded decision; Standard unchanged until approved | N/A (decision) |
| GAP-06 | Token guard coverage | `scripts/design-token-guards.py` (npm `design-guards`) | Bans raw hex outside token zones; **not** a palette freeze; font whitelist entrenches 11px | Frozen approved palette expected | runtime token mapping | fix now in planning | Extend guard to freeze chosen palette + `--vf-*` checks at mapping time | GAP-01/02 | Silent palette drift | Guard fails on unapproved hex | Guard revert |
| GAP-07 | Border token alias chain | `index.css` L28, L54, L92 | `--color-border` triple alias (micro → shadcn → `@theme`) | One namespace owner | runtime token mapping | fix now in planning | Delete dead alias; add namespace guard test | None | Future `@theme` color emits a competing variable | Single definition remains; test added | Revert |
| GAP-08 | Scrim duplication | `index.css` L711–716 vs `components/ui/drawer.tsx` L28–30 | Same 45% scrim implemented twice (one literal, one token) | `--vf-scrim rgba(20,20,19,.45)` | shared UI primitive | fix now in planning | Sheet primitive owns one scrim; delete the literal | Wave 3 sheet work | Overlay scrim drift | One scrim implementation | Revert |
| GAP-09 | Token hygiene (pill, focus ring) | `index.css` L1094; `999px` ×11 | Pill radius + focus-ring composition untokenized | `--radius-full`, focus tokens | runtime token mapping | defer | Backfill tokens in the hygiene batch | Wave 2 | Low | Tokens consumed; literals reduced | Revert |
| GAP-10 | Type scale floor | 11px×38 + 12px×119 (157 rules); 13 raw sizes; guard 13-size whitelist | 11–12px widespread; Standard floor is 12px caption; financial facts ≥15px | Standard type scale | screen composition | needs owner decision | D-04: set the floor (12px vs 13px vs 15px for money); tokenize scale; mass rewrite deferred | GAP-09 | Readability; whitelist entrenchment | Scale tokens defined; whitelist updated | Revert |
| GAP-11 | Warn chip defect | `index.css` L250–261 (no `[data-status]` variants); `InventoryMaterials.tsx` L369, L374; `Orders.tsx` L335; `Schedule.tsx` L246 | `data-status="warn"` unstyled → warning and empty-state chips render success-green | Word+marker+color binding; pending never success | shared UI primitive | fix now in planning | Add `[data-status]` variants bound to existing `--color-warning-*`/info tokens | None | Color contradicts content | Warn renders warning tokens; journey tests green | Revert CSS |
| GAP-12 | Status chip primitive | Same + `LoanDetail.tsx` L136 (improvised overline) | Success-only chip; no tone slots; statuses improvised per page | Tag grammar (10 states, marker+word) | shared UI primitive | fix now in planning | One StatusChip primitive with tone slots (same PR as GAP-11) | GAP-11 | Divergent status UI | One primitive; ad-hoc uses migrate progressively | Revert |
| GAP-13 | Row state presentation | `Orders.tsx` L128–148; `FinanceActivity.tsx` L106–118; stripe grep = 0 | Row status = plain small text; no marker icon or edge stripe anywhere | Row slots + ≤3px stripe + word+marker | shared UI primitive | needs owner decision | D-05: approve marker/edge-stripe adoption → Row primitive implements slots | Wave 2/3 | Visual identity change | Rows render marker+word; stripe ≤3px | Revert component |
| GAP-14 | Skeleton loading | grep skeleton = 0; `index.css` L354, L761 | Loading = text + spinner only | Skeleton promising real layout, `aria-busy` | shared UI primitive | defer | ScreenState primitive gains a skeleton tier later | Wave 3 | Low (additive) | `aria-busy`; layout-promising skeleton | Revert |
| GAP-15 | Sheet systems | `index.css` L711–751, L857, L872–1000; `drawer.tsx`; `QuickActionSheet.tsx` L393–421 | 3 coexisting systems (vaul bridge / `.micro-sheet-*` / `.micro-dialog`) | One sheet contract | shared UI primitive | defer | Consolidate on vaul when the overlay contract lands | Wave 3 | Refactor risk | One sheet implementation owning scrim/focus/z | Revert |
| GAP-16 | Feedback regime | `App.tsx` L2 (Q-003 removed Toaster); 110 `role="status"`; 53 `role="alert"`; `resultFeedback.ts`; 34 pages with local `setMessage/setNotice` | Deliberate inline regime; no snackbar; per-page notice markup | Snackbar contract exists | product/owner decision | needs owner decision | D-06: ratify no-toast inline regime (then Standard gains a note) or adopt snackbar; then one Notice primitive | Wave 3 | Regime fork persists | Recorded decision; single feedback contract | Revert |
| GAP-17 | Surface primitive | 18 `micro-*card*` variants; `InfoCard` tone slots used by 2 files | Card variant zoo; no Surface with slots | Surface ladder + card contract | shared UI primitive | defer | Surface primitive with tone/elevation slots | Wave 3 | Zoo persists | One surface family | Revert |
| GAP-18 | Row primitive | 13 row families, 2 anatomies (divider-row vs bordered-card-row) | Anatomies fork | One row grid (R-10) | shared UI primitive | defer | Row primitive normalizes families | Wave 3 | Wide touch points | Single anatomy; inset dividers | Revert |
| GAP-19 | Empty-state variants | `index.css` L590; `Parties.tsx` L138–147; `Home.tsx` L331–334; `FinanceActivity.tsx` L270 | 4 competing implementations | Empty contract (tile+copy+one action) | shared UI primitive | defer | EmptyState primitive with compact/inline variants | Wave 3 | Inconsistent empties | One primitive | Revert |
| GAP-20 | ScreenState duplication | ≈30 page-local loading/error blocks (e.g., `Home.tsx` L154–173, `Finance.tsx` L250–265) | Loading/error/retry re-implemented per page; unknown state unowned | 6 screen states incl. unknown | shared UI primitive | defer | ScreenState primitive wired to the taxonomy | Wave 3 | Unknown-state gaps | One component; taxonomy covered | Revert |
| GAP-21 | Dead tooltip | `components/ui/tooltip.tsx`; `App.tsx` L15; `vite.config.ts` L334–335 | Provider mounted, never rendered; radix chunk shipped | Component economy | shared UI primitive | fix now in planning | Delete tooltip + provider + dependency; re-run bundle budget | None | Dead surface + bundle cost | No tooltip references; budget green; tests green | Revert |
| GAP-22 | Amount unit composition | 275 exact `د.أ` literals across 53 files; `formatMoneyWithUnit` in 6 files; 30 files hand-roll `dir="ltr"` isolation | Unit composition inline everywhere | Unit beside value; amount slot | shared UI primitive | defer | Centralize via MoneyValue/formatters after value-zone lands | Wave 3/4 | Mechanical but wide | Single formatter path; literals reduced | Revert |
| GAP-23 | Value-zone slots | `Finance.tsx` L757–834; value sizes 20/24/26/28/31px | Label/value/unit realized; period + delta slots never rendered; scale ad hoc | Value zone + numeric hierarchy | screen composition | defer | Adopt slots behind Wave 2 tokens | Wave 2/3 | Inconsistent emphasis | Slots rendered; scale tokenized | Revert |
| GAP-24 | Period control | `FinancePeriodResultSection.tsx` L62–87 (native `type=month`); `FinanceActivity.tsx` L226–252; `Statement.tsx` L276 (quick ranges); `period-chip` grep = 0 | Native month inputs + quick-range text buttons | Period chip contract 🟢 (36/44) | covered by Standard | needs owner decision | D-07: adopt chip vs keep month inputs (if kept, Standard gains an explicit variant note) | Wave 2 | Time semantics are product-owned | Decision recorded; control anchored to its value | Revert |
| GAP-25 | Third-party styling drift | `drawer.tsx` L48–100; `tooltip.tsx` L37–43 | shadcn-default utilities outside the micro class system | One component grammar | shared UI primitive | fix now in planning | Absorb drawer styling into micro classes (with GAP-15); tooltip deleted via GAP-21 | GAP-15/21 | Two grammars coexist | Micro classes own all chrome | Revert |
| GAP-26 | Storage type edges | 17 files import `@/storage/local/types` (e.g., `NewDraft.tsx` L6, `OrderDetail.tsx` L43) | UI imports storage record shapes (type-only) | UI binds to contracts, not storage | screen composition | fix now in planning | Move shared shapes to domain/application contracts | None | Contract-first violation | Zero storage imports in UI | Revert |
| GAP-27 | localStorage leaks | `application/drafts/legacyFormDraftMigration.ts` L32; `application/diagnostics/localDiagnosticsService.ts` L174 | 2 persistence uses outside `storage/` (both injectable) | Persistence stays in storage layer | screen composition | fix now in planning | Relocate behind the storage interface | None | Boundary hygiene | Only `storage/` touches persistence | Revert |
| GAP-28 | Component→page edge | `components/finance/FinancePeriodResultSection.tsx` L12 | Type-only import of `FinanceState` from `pages/Finance` | Layering forbids component→page | screen composition | fix now in planning | Move the type to application/model | None | Near-cycle | No component→page imports; guard test added | Revert |
| GAP-29 | Inline business vocab | `FinancialEventEditor.tsx` L152–157; page-local subsystems (Schedule ×7, Finance ×5) | Domain vocabularies defined inside screens | Screens compose; meaning lives domain-side | screen composition | defer | Extract vocab in sequenced waves | Wave 4 | Large; regression-prone | Vocab imported, not inlined | Revert |
| GAP-30 | FAB geometry | `BottomNav.tsx` L29–32; `index.css` L828–852 vs Standard `design-tokens.css` L139–140 + gallery `.fab` | In-grid round (50%) text FAB on `var(--primary)` vs Standard 56px Clay r12 icon-only in own gutter 80px above nav | FAB contract 🟢 | AUX shell | needs owner decision | D-08: pick geometry (in-grid labeled FAB is a deliberate Micro pattern) then align tokens | Wave 2 | Identity-level | FAB matches decision; covers no amount column | Revert |
| GAP-31 | Navigation labels | `navigation.ts` L14–17 vs Standard `README.md` L9 | «مشروعي الآن/العمل/مالي/أدواتي» vs «الرئيسية/المالية/الطلبات/الأدوات» | Official navigation | AUX shell | needs owner decision | D-09: ratify Micro's labels («أدواتي» already decreed in code) → Standard text truthing, not code | Wave 5 | Copy mismatch | Labels ratified on both sides | Doc revert |
| GAP-32 | Unspecified AUX behaviors | `MicroAppShell.tsx` L26–33, L62–69, L90–119; `index.css` L300–305 | Keyboard chrome-hide, context-label suppression, route-kind gating, scroll-border header, 260ms route transition — working but contract-less | Standard silent | AUX shell | preserve | Keep; document as AUX-shell addendum at the next Standard revision (motion table gains a route row) | Wave 5 | None (works) | Behaviors documented + guarded | N/A |
| GAP-33 | Reader chrome depth | `routeClassifier.ts` L52, L55 | `/assets/:id`, `/loans/:id` = deep (nav hidden) while `/orders/:id`, `/cash/wallet/:id` = surface readers | Persistent nav on surfaces | AUX shell | needs owner decision | D-10: ratify per-family reader depth (contract-29 wording supports reader=surface) | None | Inconsistent reader UX | Classifier matches decision; tests updated | Revert |
| GAP-34 | Micro feature patterns | Home fact triad (`Home.tsx` L43–89); EventsLayer correction grammar L166–768; DecisionPanel; knowledge states; decision-card grammar; inline feedback | Six runtime patterns richer than the Standard | Named as domain compositions only | Micro feature pattern | preserve | Document as Micro-owned Feature Patterns; Standard may reference, never absorb | Wave 4 | Flattening risk | Patterns documented with evidence | N/A |
| GAP-35 | Knowledge states | `InventoryMaterials.tsx` L354–379; `G5DecisionPanel.tsx` L23–33 | Unconfirmed quantity / unknown cost / needs-review lack canonical matrix rows | 10-state matrix lacks a knowledge tier | product/owner decision | needs owner decision | D-11: approve a states-matrix amendment bound to existing approved values only | Wave 5 | New state semantics | Matrix rows added; zero new hex | Standard revert |
| GAP-36 | State-word orthography | مسودة ×35; «بانتظار قرار» ×7; ملغى ×7; رُوجعت = 0 hits; «متراجع موثقًا» in activityLabels | Word variants diverge from the Standard's example words | Matrix words are examples; binding is word+marker+color | product/owner decision | needs owner decision | D-12: ratify canonical Arabic words; update copy + matrix examples | Wave 2/5 | Copy inconsistency | Canonical word list on both sides | Revert |
| GAP-37 | Charts | grep `<svg`/`<canvas`/chart = 0 across src | Zero charts; Standard ships a question-led chart contract with floors | Chart contract 🟢 (one family) | product/owner decision | defer | Keep deferred per owner stop rule; floors become acceptance criteria for the first chart | Owner decision | First chart must meet floors | Floors documented; first chart complies | N/A |
| GAP-38 | Integrity-check pattern | `ToolsIntegrity.tsx` L58–201; `index.css` L6557–6578 | PASS/WARN/FAIL rows + drift line + offenders disclosure + version | Standard silent (adjacent to S-12) | Micro feature pattern | preserve | Keep; optional one-line Standard pointer later | Wave 5 | None | Pattern documented | N/A |
| GAP-39 | Scheduling composition | `Schedule.tsx` L258–524 (capacity, recurrence, buckets, month-less lists); `ScheduleEditor.tsx` L228–272 | No calendar grid/picker beyond `type=date`; all product-local | Standard silent by design | not in Standard by design | preserve | Keep product-owned; document as feature pattern | Wave 4 | None | Documented | N/A |
| GAP-40 | Forms-protection stack | `UnsavedChangesGuard` (26 pages) + `useFormDraft` + `FormDraftRestoreBanner` + `resultFeedback.ts` + review-lock note | Shared contract-like stack, unspecified anywhere | Standard: "input preserved" one line | Micro feature pattern | preserve | Document the pattern; Standard pointer at next revision | Wave 5 | None | Documented + test-guarded (already) | N/A |
| GAP-41 | Filters / sort | `FinanceActivity.tsx` L226–267; `CorrectionsLayer.tsx` L238–252; sort grep = 0; one search field (`Parties.tsx` L134) | Ad-hoc `aria-pressed` text-button filters; no sort; Standard filter-surface staging unused | Filtering family 🟢 | screen composition | defer | Adopt filter surfaces when filters grow; per-surface decision | Wave 4 | Unmanaged feature growth | Per-surface decision recorded | Revert |
| GAP-42 | index.css organization | 6,962 L; ≈2/3 feature-scoped; 30 media queries; 35 `!important` | Accreted feature CSS | Feature-oriented split is the target state | screen composition | defer | Split behind contracts — after dedup (GAP-43), never before | GAP-43 | Fossilizes duplicates if early | Families per feature; no dup blocks | Revert per file |
| GAP-43 | CSS duplication | `.micro-financial-pulse` L1822/2074/2599; `.micro-home-heading` L1760/1952/2204; 130-line unit, ≈256 redundant lines | Triple block; copies 1&2 byte-identical; CSS tests read the first match | One truth per rule | screen composition | fix now in planning | Remove copies 2+3 behind a computed-style/screenshot check | None | Tests may read the wrong match | Single definition; visual snapshot equal | Revert |
| GAP-44 | Guard suite scope | `U09.css.test.ts` (3 assertions) vs 165 test files | Only 3 CSS touch-target strings guarded; no token/hex/z/sheet guards | Contract-first must be enforceable | runtime token mapping | fix now in planning | Extend guards: hex budget, `--color-*` namespace, z-ladder, sheet count, dup-block detector | GAP-06 | Drift invisible today | Guards fail on each violation class | Revert |
| GAP-45 | Token core health | 631 `--space-*` uses vs 7 raw margins; 94 radius uses; 21 elevation uses; 105 logical properties; 0 `rtl:` hacks; tsx zero color literals | Discipline already token-driven | Strategy's token-driven layer exists | runtime token mapping | preserve | Formalize via the mapping layer (GAP-02); do not rebuild | Wave 2 | None | Ratios maintained | N/A |
| GAP-46 | Standard manifest count | `documents/micro-standard-v2/MANIFEST.json` | `file_count: 29` vs 31 files on disk (self-documented "29 core + 2 metadata") | Manifest accuracy | not in Standard by design | fix now in planning | Standard-side doc fix at next revision (make the 29+2 split explicit in the field) | Wave 5 | Cosmetic | Field states the split | Doc revert |
| GAP-47 | Accounting-port pressure | Prior adversarial verdicts (historical context only) | Potential future pressure to port Accounting hexes/heroes/gold/steel-blue/fonts/5-tab nav | Contradicts Standard + standing owner bans | out of scope | out of scope | Keep banned; restate bans in every wave plan | — | Regression risk | Bans restated | — |

## 8. Read-only Structure / Architecture / Code Organization Scan (summary)

The full nine-area scan is delivered as `MICRO_UI_AUX_STRUCTURE_SCAN.md`. Headline results:

1. **Module/feature boundaries:** clean downward layering (`src/domain` ← `application` ← UI) with 212 `@micro-domain` imports, zero relative escapes, zero application→UI imports; the UI side has no primitive/pattern layer — feature CSS (≈2/3 of `index.css`) and page-local sub-components (Schedule ×7, Finance ×5) act as an informal pattern layer.
2. **File responsibilities/oversized:** `index.css` 6,962 L; `OrderDetail.tsx` 1,412 L; `OwnerEntitlement.tsx` 1,096 L (51 `useState`); `FinancialEventEditor.tsx` 1,055 L (inline vocab L152–157); `Schedule.tsx` 1,028 L (7 local components); `EventsLayer.tsx` 862 L ("a page wearing a component costume"); `QuickActionSheet.tsx` 761 L (4 sub-sheets inline).
3. **Dependency/layer violations:** 17 type-only storage imports into UI; 2 `localStorage` leaks; 1 component→page type edge; otherwise none found.
4. **Cycles and guard limitations:** no runtime cycles; one near-cycle via the type edge above. Guard suite asserts copy/roles/journeys but only 3 CSS strings — nothing guards tokens, hex, z-ladder, sheet count, or duplication.
5. **Duplication/competing truths:** 3 sheet systems; 18 card variants; 13 row families ×2 anatomies; 4 empty-state variants; ≈256-line triple CSS block; scrim ×2; `د.أ` composition ×275; identity hexes mirrored in PWA manifest/logo.
6. **Feature discoverability:** good route/label mapping (`getNavigationLabel`, 15 prefixes); pattern discoverability poor (patterns live inside pages/CSS, not documented modules).
7. **Storage/application/domain/UI composition:** runtime storage imports only at composition roots (`StartupGate`, `PrototypeServicesContext`); services own persistence via store interfaces; domain owns meaning and is UI-free.
8. **Test/documentation mapping:** 165 test files incl. ≈260 UI-guard `it()` blocks; docs designate `index.css` as the value source of truth — accurate today, and exactly the file the token mapping would extend.
9. **Target module map:** proposed only (§10), labeled `proposed — not executed`; no bulk moves recommended.

Every finding carries exactly one classification (`fix now in planning` / `preserve` / `defer` / `needs owner decision` / `out of scope`) in §7; nothing is classified as "fix now in code" — implementation requires owner approval of this report first.

## 9. Source-of-truth matrix

| Category | Current authoritative source (evidence) | Conflicts / drift today | Recommended authoritative source after integration |
|---|---|---|---|
| Color tokens | Micro `index.css :root/.dark` (per `docs/product/design-system-v1.md` §"values") | Retired palette; Standard's 18 hexes absent; twins in PWA/logo | Standard palette (approved values) → consumed via new `--vf-*` runtime mapping in Micro |
| Action classes (create/save/commit) | Implicit per-page button usage (`--primary`) | One primary class vs Standard's 3-class ladder | `button-system.md` contract → Micro button classes as adapters |
| Selection grammar | Teal accent pill (`index.css` L820–823) | Teal unratified; no `#C96442` edge | Standard: 2px `#C96442` inset edge + non-color cue |
| Type scale | 13 raw px sizes; guard whitelist | 157× 11–12px; no scale tokens | Standard scale (28/24/15/13) → Micro type tokens |
| Elevation / radii / spacing / fonts | Micro tokens (value-identical to Standard) | None material | Standard values, Micro tokens as the mapped carriers |
| Money formatting / digits / dates | `presentation/formatters.ts` + `EnglishNumberInput` | 275 inline `د.أ` bypasses; 30 hand-rolled isolations | Keep `formatters.ts` as runtime authority behind a MoneyValue primitive; Standard owns the contract |
| Component classes (sheets/cards/rows) | `index.css` families | 3 sheet systems; 18 cards; 13 row families | Shared primitives (`ui/primitives/`) consuming tokens; one system each |
| States (financial) | Ad-hoc per-page words/tones | `warn` chip unstyled; no markers; orthography variants | `component-states.md` matrix → StatusChip/StateMark primitive |
| Routes / chrome gating | `routeClassifier.ts` + `navigationContract.ts` + tests | Reader-depth inconsistency (`/assets/:id`, `/loans/:id`) | Keep Micro files authoritative (AUX shell); ratify depth per family |
| Navigation destinations | `navigation.ts` (4 + FAB) | Labels differ from Standard README | Micro runtime authoritative for labels after D-09; Standard text updated |
| Empty/loading/error | 4 empty variants + per-page ScreenState | Unknown state unowned | Standard taxonomy → ScreenState/EmptyState primitives |
| Overlays / z-ladder | Comment in `index.css` L190 + per-component hardcodes | Not enforced | AUX-shell-owned ladder, guarded by tests |
| Page composition & copy | Pages themselves | — | Pages remain authoritative (screens own composition/data/copy) |
| Domain meaning & policy | `src/domain` (+ `application`, `storage`) | None found (clean) | Unchanged; never depends on UI |

## 10. Target module map — `proposed — not executed`

**This is a proposal for owner review. Nothing has been moved, created, renamed, or deleted.** No bulk move is recommended; each box below is introduced incrementally behind the waves in §17.

```
apps/prototype-web/client/src/
├── styles/                        (proposed) token + base layers
│   ├── tokens.standard.css        --vf-* runtime mapping of Standard values (Wave 2)
│   ├── tokens.micro.css           existing micro tokens, re-pointed/reduced as mapping lands
│   └── index.css                  entry only; feature CSS migrates out gradually (Wave 4)
├── ui/primitives/                 (proposed) shared UI primitives (strategy layer 3)
│   ├── Button.tsx                 create / save / commit / destructive / secondary / outline / ghost
│   ├── Field.tsx                  text/search/amount/select/textarea variants
│   ├── Surface.tsx                tone + elevation slots (replaces 18 card variants over time)
│   ├── Row.tsx                    identity lead / title-caption / state slot / trailing amount slot
│   ├── StatusChip.tsx             word+marker+color binding, tone slots
│   ├── Sheet.tsx / Dialog.tsx     one overlay system owning scrim/focus/z
│   ├── Notice.tsx                 inline feedback primitive (per D-06 outcome)
│   ├── EmptyState.tsx / ScreenState.tsx  incl. skeleton tier + unknown state
│   └── MoneyValue.tsx             wraps DisplayValue + formatMoneyWithUnit (unit beside value)
├── aux/                           (proposed) application chrome (strategy layer 4)
│   ├── AppHeader / BottomNav / Fab    (migrated from components/layout once contracts land)
│   ├── routeChrome.ts             routeClassifier + showsGlobalChrome (existing logic, formalized)
│   └── keyboard.ts                visualViewport handling (existing logic, formalized)
├── patterns/                      (proposed) Micro-owned Feature Patterns (strategy layer 5)
│   ├── finance-value-zone/        value + period + delta slots, truth block
│   ├── period-controls/           chip or month-input variant per D-07
│   ├── correction-lifecycle/      reverse / atomic edit / documented delete / undo grammar
│   ├── order-rows/                next-action state machine + agreement memory
│   ├── fact-cards/                known / not_initialized / incomplete triad + road chips
│   ├── knowledge-states/          unconfirmed quantity / unknown cost presentation
│   ├── integrity-check/           PASS/WARN/FAIL rows + drift + offenders
│   └── scheduling/                capacity / recurrence / buckets (product-owned)
├── features/<family>/             (proposed, gradual) page + family-scoped CSS extracted from index.css
├── presentation/                  (existing, unchanged) formatters, labels, plurals
├── app/                           (existing, unchanged) router, classifier, nav contract, StartupGate
├── application/                   (existing, unchanged) services own use cases + persistence via stores
├── storage/local/                 (existing, unchanged) IndexedDB/Memory adapters + commit guards
├── contexts/                      (existing) ThemeContext — fate per D-03
└── pages/                         (existing) composition, data binding, copy, feature meaning
src/domain/                        (existing, unchanged) meaning, policy — never depends on UI
```

Rules attached to the map: pages never redefine tokens or duplicate primitives; primitives never import pages; patterns import primitives only; domain/application/storage never import UI; every arrow left-pointing is a violation (test-guarded after GAP-44).

## 11. What transfers from Standard (adoptions)

1. **Token values**: the 18 approved hexes via the `--vf-*` mapping (canvas/surface already match; ground `#F5F4ED`, tint `#E8E6DC`, border `#D1CFC5`, boundary `#87867F`, ink set, 5 semantic hues are new values in Micro).
2. **Action classes**: create/save/commit/destructive ladder incl. pressed-edge treatment, quiet completion, loading/duplicate-submit rules.
3. **Selection grammar**: 2px `#C96442` inset edge + non-color cue on chips/tabs/nav (replacing improvised teal pill).
4. **State presentation**: word + marker + color bindings, edge stripes ≤3px, pending-never-success, unknown separate from failure.
5. **Value zone + honest voids**: label/value/unit/period/delta slots; unrecorded → action chip; unavailable → "غير متاح"; zero → "0".
6. **Period chip** (if D-07 adopts it) and its staged-in-filter behavior.
7. **Row slots** incl. trailing amount slot and inset dividers.
8. **Sheet/dialog/snackbar anatomy** (if D-06 keeps snackbar) and overlay rules (one modal, staged filters, safe dismissal).
9. **Empty/loading/error taxonomy** incl. skeleton promise, `aria-busy`, retry-preserves-input, unknown-with-check-path.
10. **Chart floors** as acceptance criteria for Micro's first chart (charts themselves remain deferred).
11. **Accessibility contract**: 13-pair table as the regression baseline; dual focus; 44px targets; 200%/320px no-overflow; bidi rules.
12. **Verification discipline**: viewport/zoom/RTL/reduced-motion batteries extended to Micro screens after each wave.

## 12. What remains Micro-specific (not to be flattened into Standard components)

1. **Fact-state triad + road chips** (known / not_initialized / incomplete → value / "غير مسجل — سجّله…" / "غير محدد بعد") with source-linked qualifiers.
2. **Documented-correction lifecycle**: reverse / atomic edit / documented delete / undo-of-correction with impact previews, "الأثر بعد التراجع" disclosure, reversibleNote, audit lines ("سجل لا يحذف بصمت").
3. **Next-action state machine** on order rows + always-present priority DecisionPanel (incl. honest empty).
4. **Knowledge states** (unconfirmed quantity, unknown cost, needs-review G5) distinct from the financial state matrix.
5. **Decision-card grammar** (truth + next-action) and away-digest/priority block on Home.
6. **Inline no-toast feedback regime** (110 `role="status"`, receipt/outcome cards, `micro-local-truth`) — pending ratification D-06, but it is Micro's own aliveness asset.
7. **Integrity-check presentation** (PASS/WARN/FAIL + drift + offenders).
8. **Scheduling composition** (capacity model, recurrence panel, buckets, week-pressure question) — product-owned time semantics.
9. **AUX behaviors**: keyboard chrome hiding, context-label suppression, route-kind gating, scroll-border header, 260ms route transition.
10. **Forms-protection stack**: UnsavedChangesGuard + drafts + restore banner + stale-conflict copy.
11. **Layers/`<details>` disclosure grammar** (EventsLayer, CorrectionsLayer, owner layers, additional-details) as the dominant composition device.

## 13. What is missing and where it should live

| Missing piece | Lives in | Row refs |
|---|---|---|
| `--vf-*` runtime token mapping + namespace guard | Micro `styles/` (mapping layer) | GAP-01/02/06 |
| Approved palette adoption + twin updates | Micro tokens + PWA manifest/logo/meta | GAP-01/03/04 |
| StatusChip tones / warn fix | Micro `ui/primitives` | GAP-11/12 |
| Row slots + state markers/stripes | Micro `ui/primitives` (Row) after D-05 | GAP-13 |
| Skeletons / ScreenState / EmptyState consolidation | Micro `ui/primitives` | GAP-14/19/20 |
| One sheet system owning scrim/focus/z | Micro `ui/primitives` (Sheet) | GAP-08/15/25 |
| Notice primitive (per D-06) | Micro `ui/primitives` + AUX slot | GAP-16 |
| Value-zone period/delta slots + value scale | Micro `patterns/finance-value-zone` | GAP-23 |
| Period chip (per D-07) | Micro `patterns/period-controls` | GAP-24 |
| Unit composition centralization | Micro `presentation` + `MoneyValue` | GAP-22 |
| Feature-pattern documentation (6 patterns) | Micro `patterns/` docs | GAP-34 |
| Knowledge-states matrix amendment | Standard `component-states.md` (revision, owner-approved) | GAP-35 |
| Word orthography ratification | Micro copy + Standard matrix examples | GAP-36 |
| AUX-shell addendum (keyboard, gating, transition row) | Standard `navigation-shell.md`/`motion-interaction.md` revision | GAP-31/32 |
| Navigation-label truthing | Standard `README.md` text (if D-09 keeps Micro labels) | GAP-31 |
| Manifest count fix | Standard `MANIFEST.json` (revision) | GAP-46 |
| Link-ink decision + dark-mode decision | Owner decision record; Standard untouched until approved | GAP-05 |

## 14. What must be preserved

1. The **token discipline** already in Micro: 631 spacing-token uses vs 7 raw margins, single elevation system, logical properties with zero `rtl:` hacks, zero color literals in TSX (GAP-45).
2. The **layering discipline**: domain ← application ← UI with alias-based imports and services owning persistence (verified clean).
3. The **six runtime feature patterns** (§12.1–6) — Micro's aliveness; a future Standard revision may reference them but must never absorb them silently.
4. The **honest-void family** ("غير مسجل — سجّله", "غير متاح", measured zero) — the Standard codified it; Micro pioneered it.
5. **Micro's navigation labels and in-grid labeled FAB** until/unless the owner decides otherwise (D-08/D-09) — they are deliberate, tested patterns.
6. **The guard culture**: `design-token-guards.py`, journey suites, navigation contract tests, lock gates — extended (GAP-44), never weakened.
7. **Bidi/digit discipline**: English digits, `dir="ltr"` isolation, numeric DD/MM/YYYY dates — already superior to the Standard's minimum.

## 15. What must be rejected or ignored from Prototype (v0) and other historical sources

1. Prototype v0 is **evidence only** (Standard decision 13): its routes, labels, numbers, categories, fake data, and interactions must not be copied into Micro or cited as product truth. (This report used none of them.)
2. Gallery demo vocabulary (Received / In progress / Moved / Returned / Ready / Sent / Closed tags) is demo content inside the Standard gallery, not the canonical state words — do not import it into Micro copy.
3. Retired values must not return as tokens or primary buttons: `#964E33`, `#5F3120` (and Micro's incumbent `#CC785C` family is itself retired once D-01 approves adoption).
4. `#B79C86` / `#8C7A66` remain logo-reference neutrals only; no new palette; no new Teal; no gold/amber family (decision 8).
5. No dark mode may enter the Standard, and Micro's live dark mode must be resolved by explicit owner decision (D-03), never silently ratified.
6. Terracotta must never be recast as a data/success/failure color; identity `#D97757` never touches financial values, chart fills, or status.
7. Accounting-derived porting ideas (semantic ramps, solid heroes displaying invented zeros, steel-blue withdrawal, font swap, 5-tab nav) remain banned by earlier adversarial verdicts (GAP-47).

## 16. Owner decisions required

| ID | Decision | Options | Report's recommended default |
|---|---|---|---|
| D-01 | Adopt the approved 18-value palette via `--vf-*` mapping (incl. twins: PWA manifest, logo, meta) | (a) adopt fully; (b) defer | (a) adopt — values are owner-approved already; swap is token-level |
| D-02 | Teal accent fate + link/action ink | (a) retire teal, links use ink-secondary per Standard constraint clause; (b) keep teal, Standard gains ratified link-ink role | (a) — closes an unratified role cleanly |
| D-03 | Dark mode fate | (a) keep as Micro-local feature (Standard stays light-only, documented divergence); (b) freeze/hide toggle until Standard ever covers it | (a) keep but document as Micro-local; verification burden stays with Micro |
| D-04 | Type floor for 11–12px | (a) floor at 12px (Standard caption); (b) floor at 13px for labels; money ≥15px either way | (b) 13px label floor; caption 12px only for non-financial metadata |
| D-05 | Row state markers + ≤3px edge stripe | (a) adopt Standard marker/stripe; (b) keep words-only | (a) — it is the Standard's non-color redundancy rule |
| D-06 | Feedback regime | (a) ratify inline no-toast as Micro's contract; (b) adopt snackbar for transient confirmations | (a) ratify inline; revisit snackbar only if a real need appears |
| D-07 | Period control presentation | (a) adopt Standard period chip; (b) keep native month inputs + quick ranges (Standard gains variant note) | (b) keep month inputs (product-owned time semantics), Standard note added |
| D-08 | FAB geometry | (a) keep in-grid labeled FAB (Micro pattern); (b) move to Standard own-gutter r12 icon FAB | (a) keep — it is tested, deliberate, and labeled |
| D-09 | Navigation labels | (a) ratify «مشروعي الآن/العمل/مالي/أدواتي»; (b) adopt Standard README labels | (a) ratify Micro's; Standard text truthed |
| D-10 | Reader-route chrome depth (`/assets/:id`, `/loans/:id`) | (a) surface (reader=chrome, like orders/wallet); (b) keep deep | (a) surface for consistency with reader peers |
| D-11 | Knowledge-states amendment to the Standard states matrix | (a) approve amendment (existing values only); (b) keep Micro-local | (a) approve — closes G4-10 cleanly |
| D-12 | Canonical state-word orthography (ملغى/ملغي; بالانتظار vs بانتظار قرار; رُوجعت) | (a) ratify one canonical list; (b) leave per-context | (a) ratify — copy consistency is cheap now, expensive later |

## 17. Minimum safe remediation waves (proposed — not executed)

**Wave 1 — Zero-visual hygiene batch (no owner decisions needed).**
Contents: GAP-11+12 (warn-chip variants + StatusChip primitive), GAP-21+25 (delete dead tooltip/provider/dep; absorb drawer styling), GAP-43 (dedup ≈256 lines behind a computed-style check), GAP-26/27/28 (storage type contracts, localStorage relocation, component→page type move), GAP-07 (border alias cleanup), GAP-44+06 prep (guard extensions: namespace, z-ladder, sheet count, dup detector — armed in observe mode).
Dependencies: none. Risks: lowest in the whole program; CSS tests read first matches (mitigated by the dedup check). Acceptance: full test suite green; `design-guards` exit 0; screenshot/computed-style equality on affected surfaces; zero visual change by definition. Rollback: each item is an independent revertable commit; batch reverts cleanly.

**Wave 2 — Owner decision pack + token mapping (the identity wave).**
Contents: apply D-01…D-04 answers: `--vf-*` mapping file, shadcn bridge re-bind, `--primary` symmetry, twins (PWA/logo/meta), guard freeze of the palette; D-09/D-08/D-10 code-or-doc changes; orthography updates (D-12); Standard-side truthing batch (README labels, motion-table route row, manifest count, AUX addendum) as a separate Documents commit.
Dependencies: D-01…D-12 answered; Wave 1 merged. Risks: identity-defining; contrast re-verification mandatory; dark-mode re-declarations must be regenerated from the mapping. Acceptance: 18 hexes present; contrast table re-computed; journey + UI suites green at 320/360/390/430 @ 100/130/200% RTL; no horizontal overflow. Rollback: revert the mapping commit; tokens return to prior values; Standard-side doc commit reverts independently.

**Wave 3 — Shared primitives (component-driven layer).**
Contents: Row primitive with slots (per D-05), ScreenState + skeleton tier, EmptyState consolidation, Sheet consolidation (one overlay owner), Notice primitive (per D-06), Surface primitive start, MoneyValue adoption campaign (GAP-22 begins), value-zone period/delta slots (GAP-23).
Dependencies: Wave 2 tokens; D-05/D-06 answers. Risks: widest touch points; mitigated by migrating surfaces incrementally (old and new coexist during migration). Acceptance: each migrated surface passes the journey suites + state battery (focus/pressed/disabled/loading/quiet completion) + no-overflow battery; primitives have their own unit/DOM tests. Rollback: per-primitive revert; migration flags per surface.

**Wave 4 — Feature patterns + screen adoption (feature-oriented layer).**
Contents: document the six Micro feature patterns with evidence; extract page-local pattern components (finance value zone, period controls, correction lifecycle, order rows, fact cards, integrity check, scheduling docs); `د.أ` centralization completed; index.css feature-split begins (after dedup); filters/sort decisions per surface (GAP-41); vocab extraction (GAP-29).
Dependencies: Wave 3 primitives. Risks: largest diff volume; strictly incremental per family. Acceptance: each family's tests green before the next moves; no behavior change; patterns documented. Rollback: per-family revert.

**Wave 5 — Standard revision (Documents side, separate approved change).**
Contents: knowledge-states matrix amendment (D-11), navigation-label truthing (D-09), AUX-shell addendum + motion-table route row (GAP-31/32), manifest count fix (GAP-46), optional pointers to Micro feature patterns, optional filter/month-input variant notes (D-07).
Dependencies: owner approval; Waves 1–4 learnings. Risks: none to Micro (Documents-only); Standard integrity checks re-run. Acceptance: Standard package self-consistent; gallery/verification re-run for touched contracts. Rollback: branch + revert in Documents per its own policy.

**Hard boundaries for every wave:** never push to `main`; never modify `micro-standard-v2` outside an approved Wave 5; no new hex values ever; no financial meaning/formulas/permissions/sync changes; no Prototype content; physical-device and screen-reader claims only after such testing actually happens.

## 18. Recommendation for the next step

Approve **Wave 1 immediately** (it needs no decisions, fixes a real content/color contradiction, removes dead weight, and strengthens the guard suite), and answer decision pack **D-01…D-12** in parallel — D-01 (palette adoption), D-05 (row markers), and D-03 (dark mode) unblock everything else. Then run **Wave 2** as a single, revertable identity wave with full contrast and viewport re-verification. Do not begin Wave 3 primitives before the token mapping lands, and do not split `index.css` before the dedup and primitives exist. This sequencing is the smallest-risk path to "Micro rebuilt around the Standard" under the fixed strategy, and it never touches domain meaning, formulas, posting, permissions, or sync.

## 19. Evidence appendix

**Repositories / commits:** Micro `main` @ `c0469e265f24c70427eb7826dee717be117cff87`; Documents `main` @ `864263c190f5d3da6041acfafb0720e85ac6e320`; Standard = `micro-standard-v2/` (31 files).

**Key Micro paths cited (relative to repo root):**
- Router/chrome: `apps/prototype-web/client/src/app/MicroRouter.tsx` (57 routes; redirect; catch-all), `app/routeClassifier.ts` (L18–55 patterns; L52/L55 asset/loan deep), `app/navigation.ts` (L14–17 labels), `app/navigationContract.ts`, `app/useReturnNavigation.ts`, `app/StartupGate.tsx`, `components/layout/MicroAppShell.tsx` (L26–33, L62–69, L90–119), `components/layout/AppHeader.tsx` (L48–56), `components/layout/BottomNav.tsx` (L29–32), `components/layout/QuickActionSheet.tsx` (L393–421, L435), `components/security/AppLockGate.tsx`, `components/security/DataActionPinGate.tsx`, `components/ErrorBoundary.tsx`.
- Global CSS: `apps/prototype-web/client/src/index.css` (L9–31 `@theme`; L33–75 micro tokens; L76–94 shadcn aliases; L82 vs L131 `--primary`; L97–144 `.dark`; L250–261 status chip; L288/297 route-kind clearance; L300–305 page transition; L711–716 dialog scrim; L775–777 keyboard; L781/790–798 nav grid; L806–852 nav+FAB; L857 vaul bridge; L872–1000 sheet family; L1094 focus ring; L1177 sticky save; L1822/2074/2599 triplicated block; L6886–6905 lock veil).
- Presentation: `presentation/formatters.ts` (L50 `formatMoneyMinor`, L57 `formatMoneyWithUnit`), `presentation/cashCountMessages.ts`, `plurals.ts`, `g5Plurals.ts`, `orderAgreementPresentation.ts`, `catalogPresentation.ts`, `ownerEntitlementPresentation.ts`, `activityLabels.ts`; `components/presentation/DisplayValue.tsx`.
- Forms: `components/forms/EnglishNumberInput.tsx`, `EnglishQuantityInput.tsx`, `LocalDateField.tsx`, `UnsavedChangesGuard.tsx` (L260–285 dialog), `useFormDirty.ts`, `useFormDraft.ts`, `FormDraftRestoreBanner.tsx`.
- Feature surfaces: `pages/Home.tsx` (L43–89 fact triad; L154–173 loading/error; L317–350 today list; L331–334 quiet; L365–408 units; L438–484 recent), `pages/Finance.tsx` (L287–318 tabs; L373–481 truth block; L398–416 unallocated; L757–834 pulse; L837–950 decision cards; L952–988 Metric/PositionCard), `components/finance/EventsLayer.tsx` (L166–768 correction grammar; L111 local row), `components/finance/FinancePeriodResultSection.tsx` (L12 type edge; L62–87 month inputs; L367+ dl grid), `pages/Orders.tsx` (L91–110 decision panel; L128–148 rows; L335 chip), `pages/OrderDetail.tsx` (L654–713 summary/amendment; L836–873 cancel; L968–1003 deposit; L1057–1092 reversal lock; L1332 result card), `pages/InventoryMaterials.tsx` (L265+ inactive; L283 decision; L354–379 tracked rows + warn chips; L582–631 confirmations; L679 audit promise), `pages/InventoryMovementEditor.tsx` (L543–733), `pages/Suppliers.tsx` (L77–182), `pages/Parties.tsx` (L128–176), `pages/CashWallets.tsx` (L103–295), `pages/WalletLedger.tsx` (L97–181), `pages/CashCount.tsx` (L123–207), `pages/Collect.tsx` (L199–233 receipt), `pages/OwnerEntitlement.tsx` (L600–945), `pages/OwnerWithdrawalEditor.tsx` (L142–226), `pages/Tools.tsx` (L195–260), `pages/CostCalculator.tsx` (L316–451), `pages/ToolsIntegrity.tsx` (L58–201), `pages/Schedule.tsx` (L242–524 incl. 7 local components), `pages/ScheduleEditor.tsx` (L228–272), `pages/Statement.tsx` (L32, L179+, L276), `pages/Settings.tsx` (L584 deletion alertdialog).
- Boundary evidence: 17 files importing `@/storage/local/types` (incl. `NewDraft.tsx` L6, `OrderDetail.tsx` L43, `Finance.tsx` L31, `ScheduleEditor.tsx` L11); `application/drafts/legacyFormDraftMigration.ts` L32; `application/diagnostics/localDiagnosticsService.ts` L174; `components/finance/FinancePeriodResultSection.tsx` L12; `tsconfig.json` L19–22 + `vite.config.ts` L306–311 aliases; `vite.config.ts` L227–245 budget gate, L262–263 PWA colors, L334–335 radix chunk; `index.html` L9–10; `public/micro-mark.svg` L3; `scripts/design-token-guards.py`; `App.tsx` L2 (Q-003), L14–15; `contexts/ThemeContext.tsx`.
- Tests: `app/navigation.test.ts`, `app/navigationContract.test.ts`, `app/routeClassifier.test.ts`, `U09.css.test.ts`, `U01.dom.test.tsx` (L112–126 LTR digits), `EventsLayer.familyGuard.dom.test.tsx`, journey suites (Home/G2–G6/Cash/Finance/D005/U-series), page `.ui` suites — 165 test files total.
- Standard paths: `micro-standard-v2/README.md` (L9 navigation; L30 verification boundary), `design-tokens.css` (120 props; L139–140 FAB), `design-tokens.json`, `color-system.md` (12-role table; link-ink clause), `button-system.md`, `component-contracts.md` (L5–15 actions; L20–28 value zone; L30–32 period chip; L36 row slots+stripe; L38 domain compositions), `component-states.md` (10-state matrix), `empty-loading-error-states.md`, `navigation-shell.md`, `overlay-system.md`, `motion-interaction.md` (timing table, no route row), `responsive-geometry.md`, `accessibility.md` (13 pairs), `data-display-system.md` (chart contract), `coverage-matrix.json` (L90–93 requires_separate_testing), `decision-log.md` (decisions 1–14; #8 gold retirement; #10 charts; #11 S-12; #13 prototype boundary), `verification-report.md`, `self-critique.md`, `source-inventory.md`, `MANIFEST.json` (`file_count: 29`), `component-gallery.{html,css,js}`.

**Inspection method:** read-only git clone; `git rev-parse`/`log` for SHAs; targeted `Read`/`Grep` across the paths above; all quantitative claims re-verified by the adversarial agent (§3 corrections applied); no build/run/device sessions; no file in either repository was modified, created, or deleted.

---

## Annex A — Required comparison questions, answered from evidence

**A1. If Micro adopts the Standard contracts, which screens/components are covered immediately?**
Buttons, fields, inputs (incl. English-number entry), surfaces/cards, sheets (3 real ones), dialogs, value+unit presentation, empty/error wording, tab/segmented selections, and the whole state-word vocabulary transfer with light adaptation. Structurally ready surfaces: Home, Finance, Orders, OrderDetail, Inventory, Suppliers/Parties, Cash suite, Tools, Schedule, Catalog — all already consume tokens and shared classes, so contract adoption is per-component, not per-architecture.

**A2. Which UI/AUX elements are missing from the Standard but belong as Micro Feature Patterns?**
The six runtime patterns (§12.1–6) plus integrity-check presentation and the scheduling composition (§12.7–8), and the AUX behaviors (§12.9) which belong in an AUX-shell addendum — not in the Standard core.

**A3. Which gaps are true Standard contract gaps vs implementation-mapping gaps?**
True Standard gaps: knowledge states (no matrix rows), link-ink value (unratified), tool-result anatomy (S-12 deferred), AUX behaviors (keyboard/chrome/transition), order-detail/balance compositions (named, no anatomy). Everything else — palette, action classes, selection edge, stripes, chips, value-zone slots, period chip, skeletons, sheets — exists as a contract and is an implementation-mapping gap in Micro.

**A4. Where does Micro currently duplicate colors, spacing, state styles, button behavior, rows, sheets, or shell geometry?**
Colors: identity hexes mirrored in PWA manifest/logo; scrim ×2; `--primary` role split. Spacing: effectively none (631 token uses vs 7 raw). State styles: warn chip unstyled; statuses improvised per page. Buttons: one primary class vs the needed ladder. Rows: 13 families × 2 anatomies. Sheets: 3 systems. Shell geometry: duplicated reduced-motion/380px media blocks; comment-enforced z-ladder.

**A5. Where are the current sources of truth for tokens, components, patterns, pages, routes, and state presentation?**
Tokens: `index.css :root/.dark` (declared by `design-system-v1.md`). Components: `components/` + `.micro-*` classes. Patterns: informal, inside pages/CSS. Pages: `pages/`. Routes/chrome: `app/` (router, classifier, contract) + tests. State presentation: ad-hoc per page/chip. (Full matrix §9.)

**A6. Which source should become authoritative after integration?**
Standard = contract authority (values, classes, states, a11y). Micro runtime mapping = value carrier. `ui/primitives` = component authority. `patterns/` = feature-pattern authority. `pages/` = composition/copy authority. `app/` remains route/chrome authority. `formatters.ts` remains the numeric/date authority. `src/domain` remains meaning authority.

**A7. What must be preserved from Micro because it is product-specific?**
§14 in full — especially the six feature patterns, honest-void family, labels/FAB pattern, guard culture, and bidi/digit discipline.

**A8. What must not be copied from Prototype v0?**
§15 in full — its routes/labels/numbers/categories/interactions; gallery demo tag words; retired hexes; any new palette/teal/gold; silent dark mode; Terracotta as data color.

**A9. Where would a change to one token or component fail to propagate today?**
Identity hex changes fail at `vite.config.ts` (PWA `theme_color`), `public/micro-mark.svg`, `.dark` re-declarations, and the literal dialog scrim; status styling fails at the success-only chip; component changes fail wherever pages improvise (LoanDetail overline, bespoke empty blocks); CSS changes fail silently in the triple-duplicated block (tests read the first match).

**A10. What is the safest target module map without a bulk move?**
§10 — an additive `styles/ + ui/primitives + aux + patterns` structure grown incrementally behind the waves, with existing layers untouched.

**A11. What minimum implementation waves would be needed after the owner accepts this report?**
Five: hygiene (no decisions) → token mapping (decisions) → primitives → patterns/screens → Standard revision. §17 details contents, dependencies, risks, acceptance, rollback.

**A12. Dependencies, risks, acceptance criteria, rollback boundaries per wave?**
Tabulated per wave in §17 (each wave is independently revertable; Waves 1 and 5 are Documents/zero-visual bounded; Wave 2 carries the only identity risk and mandates contrast re-verification).

**A13. Which unresolved choices require the owner's explicit decision before implementation?**
D-01…D-12 in §16; nothing in this report implements any of them.
