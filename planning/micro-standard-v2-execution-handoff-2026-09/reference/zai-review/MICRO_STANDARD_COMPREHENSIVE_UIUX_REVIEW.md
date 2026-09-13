STATUS: READ-ONLY UI/UX REVIEW COMPLETE — NO SOURCE MODIFIED — WAITING FOR OWNER REVIEW

# MICRO STANDARD — COMPREHENSIVE COMPARATIVE UI/UX REVIEW

**Subject:** Why Micro and Accounting feel more beautiful, alive, rich, clear, and professional than the current 29-file Micro Standard (micro-standard-v2) — and what to improve so the Standard can produce a better Micro experience with first-glance comprehension and minimal reading.
**Scope:** UI/UX, visual design, product comprehension, user-facing composition only.
**Session type:** Read-only comparative review. Analysis and planning only. No implementation, no repairs, no transfers.
**Date:** 2026-09-13 · **Lead:** synthesizing reviewer + 5 specialized sub-agents (first-glance user; Micro operational UX; 29-file Standard; Accounting visual benchmark; adversarial/regression guard).

---

## 0. Session transparency statement

- **Micro Live was opened and actually tested.** `https://micro-prototype.pages.dev` was driven as a real user at 390×844 (Arabic RTL): completed open onboarding (project «مشروع التجربة», default wallet «الدرج», opening balance 1,500.00 JOD known-amount path), recorded a 250.00 JOD cash direct sale, and toured: `/setup` (3 steps), `/foundation`, Home `/`, Work `/orders`, sale detail (correction form), `/finance` (both tabs «الوضع الآن» and «شو صار خلال الفترة»), «فحص سلامة مالي» (integrity check executed, result «سليم»), `/tools`, the «سجّل» record dialog and sale form, and the dark-mode toggle. No credentials were requested or invented; 11 screenshots were captured (`evidence/live/live-*.png`). Routes not exercised live are covered by repository reading and are listed in the limitations (§16).
- **Accounting was successfully run locally.** `npm install` + `vite build` + `vite preview` on port 4173 succeeded (React 18 + Vite + Tailwind + Dexie PWA). Inspected at 390×844 in Arabic RTL: onboarding (3 steps), Home, Finance, Orders (empty + with a real test order), order-detail bottom sheet, Debts, Reports (with chart), Quick sale, Settings. 12 screenshots captured (`evidence/accounting/acct-*.png`). This was visual inspection only; nothing was copied.
- **Repositories and review inputs read:** `Qays7753/Micro` (pages: Home/Finance/Orders/Parties/CashCount/Collect/Tools; presentation helpers; `apps/prototype-web/client/src/index.css` tokens; layout/navigation components), `Qays7753/Accounting` (pages, OrderCard/OrderDetailSheet/PageHeader/EmptyState/BottomNav, `tailwind.config.js`, `src/styles/index.css`, design SOP «نظام-التصميم-SOP.md», identity HTML documents), `Qays7753/Documents` → `micro-standard-v2` (all 29 files) and `planning/zai-flash-comparative-review` (README, MANIFEST, `zai_flash_next_step_source_brief.md`, all Prototype v0 documents and evidence notes).
- **No source file was modified.** No commit, push, merge, PR, token change, code change, or repair of Prototype v0. Output artifacts (this report, screenshots, notes) live only in the reviewer workspace.
- **No code-quality, security, performance, architecture, build/deployment, repository-hygiene, dependency, or test-infrastructure audit was performed.** Source files were read only to understand what a user sees and why it renders that way. Technical facts are cited solely when they visibly change what the user sees, reads, understands, or can do, and are classified as user-facing composition/prototype issues.

---

## 1. Executive answer — why Micro and Accounting feel better than the Standard

The Standard's foundation is genuinely strong — the role triad (#D97757 / #C96442 / #141413), the «color never carries a financial state alone» law, direct-value-first presentation, the stable RTL amount slot, and honest-state vocabulary are all real and verified. The gap is not talent or direction. Five concrete, evidence-backed causes explain the felt difference:

1. **The operative specification is locked in the wrong layer.** The real type scale, spacing values, radii, elevation levels, motion timings, and the contrast/use table exist only inside `component-gallery.html`'s hidden evidence panel (lines ~871–980), while the corresponding `.md` contracts are 1–4-line summaries (typography.md is three sentences). The gallery consumes ~14 tokens (negative tint pair, card/full/segment radii, E1–E3 shadows, caption size, skeleton motion…) that the shipped `design-tokens.css/json` do not define. **The verified look and the documented basis are two different systems**, so anyone composing from the documents builds flatter scenes than the artifact proves possible. Prototype v0 observed exactly this («Finance and Tools read partly like a refined gallery»).
2. **Richness lives in usage grammar and contracts the Standard does not yet have — not in more palette.** Missing: a financial value-zone contract (primary number + currency + period + delta + the three honest voids «unrecorded → action / unknown → غير متاح / zero only when measured»), an operational-row anatomy with a real status and amount channel (badge + optional edge stripe), a period-chip contract, a state→tag mapping, and a «one anchor per screen» composition rule. Micro Live and Accounting both improvise or enforce these in code; the Standard cannot reproduce or verify them.
3. **Micro Live feels alive because its composition exceeds its Standard — creating drift.** The live product ships a teal action-ink/link family (#079fa0/#057b7c/#e3f5f5), decision-panel grammar, honest «roads» («غير مسجل — سجّله»), and value qualifiers — none documented in the Standard (no link/accent role exists at all). The aliveness is real; it is just unratified, therefore unreproducible and unverifiable.
4. **Accounting feels professional because it enforces visual contracts in code**: one solid semantic hero per page, 5–6-channel rows (identity chip / name / caption / status badge / context / big end-aligned amount) with a status edge stripe, layered surface ladder (canvas → card → recess → sheet with scrim and drag handle), grouped dense settings rows, chart legibility floors (axis ticks, zero-day marks, text answer), and one shared chrome grammar on every screen. Repetition of structure is what reads as «drawn by one hand».
5. **Both feel clearer because meaning is carried by anatomy; the Standard's output leans on prose and fine print.** Live Micro sets 157 rules at 11–12px (verified by count), embeds numbers inside prose sentences («ما نعرفه الآن»), and repeats boilerplate next-step lines per row — reading demanded where structure, scale, and state words should carry meaning.

**Smallest honest summary:** the Standard does not need a new palette, dark mode, or decoration. It needs (a) its own hidden truth promoted into its documents and tokens, (b) a short list of missing visual contracts (value zone, row anatomy, states, period, anchor, link ink), and (c) Micro composition fixes that let recorded reality drive the first glance.

---

## 2. First-glance user review and minimum-reading assessment

Reviewed as a fast, impatient Arabic-speaking shop owner on a phone (3 seconds per screen; recognition before reading).

### 2.1 First-3-seconds verdict per key screen

| Screen | What lands before reading | What fails | Scan path today |
|---|---|---|---|
| **Home** | Header chrome (PWA install banner «ثبّت Micro على جهازك», floating settings/dark buttons, avatar) and the «اليوم» prose card — which still says «سجّل أول بيع» **after** a sale was recorded | The strongest number (الكاش المسجل 1,750.00) sits mid-page under three text zones; four equal fact cards give no entry point; «شلون البدرانة اليوم؟» is unanswered without reading | banner → title/date → اليوم prose → 4-card facts → doors → activity |
| **Finance** | Tabs «الوضع الآن / شو صار خلال الفترة»; cash 1,500.00; teal-tinted net card | Page opens with an abstract 2×2 «قبض ودين ونتائج» pulse before any anchor; «ما نعرفه الآن» is numbers embedded in prose sentences; the week's story hides behind tab + collapsed disclosures | breadcrumb → tabs → pulse grid → teal card → prose wall → link list |
| **Orders (العمل)** | «الأولوية الآن» panel — currently occupied by an empty-state essay | Sale rows are 4 near-equal small text lines; amount is not a visual channel; lifecycle states are plain words; «مين عليه إلي؟» is nowhere at first glance | heading → priority essay → small sale rows → quick actions |
| **Sale detail** | Honesty notice «حد الحقيقة — التحصيل ليس ربحًا» + structured fields | Six explanation elements (notice + three «+ معنى…» disclosures + two field instructions) compete with the fields; form-with-footnotes feeling | title → truth limit → fields → disclosures |
| **Tools** | H1 «احسب قبل أن تلتزم» + rule card | Nine administrative unit-state rows in identical anatomy; the alive part (the calculator) is one tap away while the page reads like a rules inventory | h1 → rule card → calculator door → 9 uniform rows |

### 2.2 Minimum-reading assessment (ranked — reading demanded where meaning should be carried structurally)

1. **Finance «ما نعرفه الآن»** — a paragraph does the work of a table; numbers live inside prose separated by «·». Should be labeled value rows (label → trailing amount → source tap).
2. **Sale-detail explanation cluster** — truth-limit sentence + three progressive-disclosure explainers + two field instructions in one view. State chips («قُبض كاملًا») should carry what sentences carry now; long forms stay behind the existing «+» pattern.
3. **Home's three prose zones before any number** — «اليوم» card + device-data note + PWA banner. The day state should be event-derived («اليوم: قبضت 250.00 د.أ») with the backup note as a dismissible action card.
4. **Per-row boilerplate «الخطوة التالية: راجع أو صحح البيع عند الحاجة.»** — repeated on rows where nothing is due; trains the owner to skip the next-action channel. Show it only when a real step exists; terminal rows get a state word.
5. **Tools unit rows + «قاعدة الأداة»** — administrative state labels in fine print. Icon + name + one-word state; rules belong inside the calculator where the risk occurs.

### 2.3 What the owner actually experiences (confirmed)

- After recording 250.00, Home's loudest line still invites a first record — **the screen contradicts the user's own action** (verified in source: today-items fire for orders only, so a direct sale produces no state change; Home.tsx quiet block L330–335 + service L286–299).
- The single most trustworthy element on Home is the facts row's honest behavior: cash shows its true value; unrecorded facts show actions, never invented zeros. This is Micro's identity — and it currently arrives without hierarchy, so its power is muted.
- Cross-screen consistency is real (Home and Finance render the same recorded-cash field; 1,500 + 250 = 1,750). A suspected mismatch was **falsified** — it was an observation-order artifact of the review session (see F-22).
- The interface feels calm and honest but **administrative** — an audit worksheet, not a live till. It becomes alive when the numbers change what the screen says; today the screen mostly says the same thing regardless of the data behind it.

---

## 3. Full UI/UX comparison — Micro Live vs Accounting vs Standard vs Prototype v0

### 3.1 Where each system excels

| Dimension | Micro Live | Accounting (benchmark) | Standard (29 files) | Prototype v0 |
|---|---|---|---|---|
| Honesty of money states | **Best in class**: empty = action chip; «الربح «غير متاح» لا صفر»; over-collection blocked; «الفحص يقيس الاتساق لا الجدوى» | Weak: confident literal «0» on unknown values (حق المحل 0، كسبت 0) | Values the rule but does not give it visual anatomy | Proves the rule composable; some staleness/sparsity issues |
| Page anchoring | No anchor on Home; Finance pulse-first | **One solid semantic hero per page** (net result, debt direction) | Anchor not specified (only kpi numerics) | Flat cards; Warm-Ink-heavy chart |
| Row anatomy | 4 small text lines; boilerplate next-steps | **5–6 channels + badge + edge stripe + internal divider** | One-grid anatomy exists (rows demo) but badge/edge unspecified | Rows prove the slot pattern works with long Arabic titles |
| Semantic color economy | Teal link/action ink + tints — alive but undocumented | **Full economy**: identity barred from numbers; income/expense/withdrawal families; word+icon always paired | Roles complete; no link role; negative-tint pair undefined; semantic hues non-text-only (hidden constraint) | Conservative; black-heavy chart series |
| Layering/surfaces | Canvas + cards + sheets (dialog record flow) | **Canvas → card → recess → sheet + scrim + drag handle** | Surface ladder named; concrete values only in gallery | Close to Standard grammar |
| Charts | None | **Reports daily-sales chart** with ticks, zero-day marks, best-day text | «Question-led, label, text alternative» — no legibility floors | One bar chart, all Warm-Ink series (flagged) |
| Long-page density | Finance long but prose-heavy; Tools uniform | **Grouped settings rows: icon chip + title + subtitle + control** | Principles present; no group/row composition contract | Sparse details |
| Copy discipline | Jordanian voice for owner questions (excellent); policy prose leaks into action surfaces (weak) | Compact rows; terms/modes multiplicity (weak) | Content guidelines strong (RTL, numerals, register) | Faithful but verbose in places |
| Trust & verification | **فحص سلامة مالي: 16 read-only checks, promise card, version line** — unmatched by benchmark | None equivalent | «Tool result» named once, never specified | Demonstrates intent |
| Continuity | Same nav/FAB grammar; chrome clutter (install banner + floating toggles) | **One PageHeader everywhere, scroll shadow, one nav grammar** | Navigation shell rules solid | Consistent |

### 3.2 The felt difference, reduced to mechanics

- **Alive** = the screen visibly reacts to recorded reality (state-aware day card, newest event first, per-row state channels). Micro has the data discipline for this; the composition doesn't spend it.
- **Rich** = rows carry who/what/state/when/how-much in one glance (Accounting) vs Micro's sentences. Richness here is anatomy, not decoration.
- **Professional** = one anchor per page + shared chrome + consistent slot grammar. Accounting repeats structure; Micro repeats prose.
- **Calm** = warm canvas, white cards, one accent moment per screen — **both** systems prove restraint wins; this must be preserved.
- **Clear** = color with words and markers, scale hierarchy, numbers in slots. Fine print and prose-embedded numbers are the clarity killers in Micro's current output.

### 3.3 What Prototype v0 evidence contributes (and its status)

- **Real evidence:** long Arabic titles survive in a trailing-slot row anatomy without pushing values off-screen; the «color never alone» law composable; light-only rendering stable; tool/record separation holds; bottom-nav clearance and detail-sparsity issues are composition-level, not Standard-level.
- **Composition/prototype issues (not Standard defects):** stale tool result, English label leaks, sparse detail scenes, Warm-Ink-heavy chart series, missing task story in Finance/Tools.
- **Would justify a Standard change only if reproduced in the Standard itself:** the chart-black issue traces to a thin chart contract; per the owner's stop rule, the Standard chart expansion **defers** until Micro's first real chart exists (acceptance floors defined in §14).
- Prototype v0 is **not** a repair list; it is the proof that the Standard's grammar, once the missing contracts land, can produce Accounting-grade richness without borrowing Accounting's skin.

---

## 4. What is already strong and must be preserved exactly

1. **Role triad discipline** — #D97757 identity/create/FAB; #C96442 chosen/current/pressed edge; #141413 Warm-Ink for primary values, commitment actions, justified danger. Never diluted into body text or chart fills. (color-system.md, button-system.md, README)
2. **«Color never carries a financial state alone»** — every financial state pairs word + shape/icon/sign/marker. This is Micro's core honesty mechanism. (color-system.md; component-states.md; design-tokens.json state_rule)
3. **Direct values first + stable trailing RTL amount slot + bidi-isolated English numerals + explicit «د.أ»** — prototype-proven with long Arabic titles; superior to Accounting's unit-less number rule for Micro's audience. (typography.md; content-guidelines.md; data-display-system.md)
4. **Honest voids: empty ≠ zero** — «غير مسجل — سجّله» action chips; «غير متاح» ≠ «صفر»; measured zero only when measured. Must never be KPI-ized into invented 0.00 values. (live-verified; input-system.md)
5. **Relationship-bar honesty rule** — parts/whole bars only «when parts genuinely sum to a whole». (data-display-system.md; gallery Metrics)
6. **State-honesty vocabulary** — pending never reads as success; unknown ≠ failure; reversed preserves audit trail. (component-states.md; empty-loading-error-states.md)
7. **Tool/record separation** — tools calculate and explain, never write records. (decision-log.md; README)
8. **The raised terracotta «سجّل» FAB with named one-line choices** — recording is one tap from anywhere with honest options. (live-verified)
9. **Jordanian colloquial voice for owner questions** («وين تحط فلوسك؟», «شو وضع الدرج هلق؟») — recognition through the owner's own words. (content-guidelines.md; live onboarding)
10. **Warm cream canvas + white surfaces + restrained single-level shadows + light-only** — the calm-till temperament. (visual-direction.md; surface-system.md)
11. **Phone geometry + honest verification boundary** — 320–430px widths, 100/130/200% zoom, 44–48px targets, device/screen-reader testing explicitly out of current claim. (responsive-geometry.md; README)
12. **Self-audit as a trust feature** — فحص سلامة مالي's read-only promise and per-check status words. (live-verified; to be contracted later, F-20)

---

## 5. Root-cause gap map

| Root cause | What it produces today | Where it must be fixed | Evidence anchors |
|---|---|---|---|
| Operative spec hidden in gallery evidence panel | Composers build from 3-line summaries → flat scenes | Standard docs (truthing) | F-14 |
| Shipped tokens ≠ gallery tokens (14 undefined) | Verified look unreproducible; verification claim false | design-tokens.css/json + verification files | F-15 |
| No financial value-zone contract | Prose-embedded numbers; voids re-decided per screen | data-display-system.md | F-17 |
| Row anatomy lacks status/amount channels | Rows read as sentences; lists feel like documents | data-display-system.md / component-contracts.md (slot vocabulary), Micro composition (adoption) | F-08, F-09 |
| No anchor rule | Pages without a primary reading; equal-weight everything | visual/composition rule (Standard, conditioned) + Micro scenes | F-06 |
| State→visual mapping missing; tag-gold holdover | No authoritative badge language; deprecated ramp leaks via gallery | component-states.md + gallery | F-18 |
| No link/action-ink role | Live improvises teal; Standard can't verify its own product | color-system.md (role defined, value owner-pending) | F-16 |
| Period control named, never specified | Period framing re-invented per screen | component-contracts.md | F-19 |
| Numeric hierarchy unreconciled (30/20/15 vs kpi 24/28) + 157× 11–12px in live | Fine-print interface; hero numbers unanchored | typography.md + Micro CSS | F-14, F-24 |
| Composition habits: prose walls, boilerplate next-steps, contentless units, chrome clutter | Reading demanded; noise; stale guidance | Micro composition only | F-01–F-05, F-23 |
| State-blind result screens (count/collection) | Moments of truth look like every other card | Micro composition (state words + sign + roles) | F-12 |
| Failure/retry inconsistency | Read failure feels like losing the page | Micro composition | F-13 |

---

## 6. Warm-Ink/black audit — one section inside the larger review

**Where Warm-Ink #141413 is correct today (preserve):** primary recorded values (1,750.00 on Home; row amounts); commitment actions («احفظ وافتح صفحة الأساس»-class confirmations); the truth-limit wordings; danger where justified (destructive confirmation paths). The live product does **not** currently overuse black surfaces — its problem is the opposite: under-developed scale hierarchy that forces ink to do all the work.

**Where Warm-Ink is overused or at risk:**
1. **Charts:** Prototype v0 rendered all series in Warm-Ink black (Prototype ISSUES #4; SELF_CRITIQUE §4) — black-as-default chart series is the clearest overuse pattern observed. Resolution: distribute series across documented neutral/info/status/success roles with a legend; do **not** open a Standard chart wave now (defer per stop rule), but the floors in §14 bind the first real chart.
2. **«All important elements inked» tendency:** when everything is #141413, nothing is. The anchor rule (§12) fixes this by scale/weight first, allowing at most one solid Warm-Ink surface per screen as an exception — never on empty/zero/unknown states.
3. **Borders/secondary controls:** gallery secondary elements sit close to ink-weight; the type-scale extraction (F-14) plus the caption floor keeps secondary chrome visually lighter than primary values.
4. **Guard:** the regression contract (§12.4, prohibition 2/4) makes «no success tint on void» and «≤1 solid anchor per route» testable, so Warm-Ink cannot silently expand into a default surface color.

**Verdict:** Warm-Ink remains the correct ink for truth; the fix is hierarchy and state-color grammar around it, not less Warm-Ink.

---

## 7. Semantic state and color matrix — when to use color, tint, marker, edge, words, or no color

All rows obey the law: **color never alone — always word + (sign | icon | marker)**. Tints are derived only from already-approved hues; hue values themselves are frozen pending the owner decision pack (§10).

| Situation | Surface treatment | Ink | Non-color redundancy | Notes |
|---|---|---|---|---|
| Primary recorded value (known, current period) | White card / recess | Warm-Ink #141413, display size, tabular | Label + period chip + «د.أ» | One per screen as anchor (scale/weight first) |
| Favorable non-zero result (net result > 0, settled) | Neutral or success-tint surface (allowed exception) | Deep success ink pair | Word («ربح»/«سليم») + «+» sign + icon | Tint forbidden at 0.00/unknown |
| Negative result / loss | Neutral surface | Error ink pair (word + «−») | Word + sign | Danger solid reserved for destructive commitment |
| Unrecorded (void) | White/ground | Neutral ink | Action chip «غير مسجل — سجّله» routed to its recorder | Never 0.00, never dash-only |
| Unknown / not applicable («غير متاح») | Neutral | Neutral ink + word | «غير متاح» word + info marker | Must never render as success or as zero |
| Pending / in-progress | Neutral or info-tint surface | Info pair | Badge word + optional ≤3px same-role edge stripe | Edge never without the word |
| Attention / review needed | Attention-tint surface | Status ink pair | Badge + edge + count where relevant | One chip per row maximum |
| Retryable failure | Error-tint surface | Error pair | Word + retry action «إعادة المحاولة» in place | One failure pattern app-wide |
| Completed / closed | Neutral (quiet) | Warm-Ink small state word | State word replaces boilerplate next-step | Success tint only if result ≠ 0 and material |
| Comparison vs previous period | Neutral | Neutral ink | Delta line «+12 د.أ عن الفترة السابقة» with sign word | Delta requires both values known; otherwise «غير متاح» |
| Parts/whole (cash distribution, cost composition) | Neutral track + segment fills from semantic roles | Labels outside segments | Legend + text alternative «الدرج 1,500 من 1,750» | Only when parts genuinely sum to the whole |
| Links / inline actions | No surface | Link/action ink (role to be defined; value = owner decision; incumbent live #057b7c) | Underline-on-interaction or icon per navigation grammar | Never a financial-semantic hue; AA text ratio |
| Chosen/current/selected | Pressed-edge #C96442 | Normal ink | Edge + selected word | Existing role, unchanged |
| Identity / create (FAB, avatar) | Clay #D97757 | Contrast ink per AA | Icon | Never displays data values |
| Decorative / empty space | No color | — | — | Color without meaning is forbidden |

---

## 8. Standard gap list — exact target files and rationale

All items are documentation/token truthing or slot-level contracts. **No palette change, no dark mode, no role-value changes** except the two owner-pending marks flagged in §10.

| # | Gap | Target file(s) | Change | Rationale | Risk of returning an old problem |
|---|---|---|---|---|---|
| S-1 | Type scale, numeral-size mapping (30/20/15 vs kpi 24/28), bidi examples | `typography.md` | Extract the gallery evidence-panel scale into the contract; reconcile numeric hierarchy; caption floor 13px; «financial facts never below 15px» | 3-sentence file cannot produce the verified interface; fixes fine-print drift | Low — pure truthing |
| S-2 | Spacing list, radius set (12/16/18/20/full), E1–E3 shadows, motion timings | `spacing-radius-elevation.md`, `motion-interaction.md` | State the concrete values already rendered by the gallery | «Use the established scale» without stating it is unverifiable | Low |
| S-3 | ~14 gallery-consumed tokens missing from shipped files (incl. negative-tint pair) | `design-tokens.css`, `design-tokens.json` | Backfill with the values the gallery actually renders; update parity note | Verified artifact currently renders on browser fallbacks; «zero mismatches» claim false | Low; values are de-facto |
| S-4 | Negative-tint role (bg+ink pair) undocumented | `color-system.md` | Document name/value/use + «word+icon required» | Danger/failed states unreproducible from documents | Low |
| S-5 | Financial value-zone contract: label/value/currency/period/delta + three honest voids | `data-display-system.md` | Add anatomy + the void presentations (action chip / «غير متاح» / measured zero) | The app's defining honesty device has no Standard backing | Low — codifies existing live truth |
| S-6 | Operational-row slot vocabulary + optional ≤3px state edge stripe | `data-display-system.md`, `component-contracts.md` | Named optional slots: identity lead, title/caption, state slot (one word+marker), trailing tabular amount; edge stripe always paired with word | Rows are the product's ledger; anatomy is missing; optional vocabulary keeps Micro's captions intact | Medium-low — must be framed as optional slots, not a copy of Accounting's 44px-chip rows (guard §12.4-7) |
| S-7 | State→tag anatomy mapping; retire `tag-gold` from gallery | `component-states.md`, `component-gallery.*` | Map all documented states (draft/pending/posted/failed/cancelled/reversed/reviewed/partial/due/overdue) to word+icon+optional tint+marker; remove or re-justify gold tags | Documented states and demo tags don't map; deprecated ramp leaks via the demo | Low — gallery-only edit |
| S-8 | Period-chip visual contract (chip anatomy, range display, where period context sits on every metric) | `component-contracts.md` | One-paragraph contract; **time semantics stay product-owned** | «آخر 30 يوم» framing is re-invented per screen | Low — visual only |
| S-9 | Link/action-ink role definition (constraints now; value owner-pending) | `color-system.md` | Define the role class: text affordance ink, never financial-semantic, AA text ratio; incumbent live value recorded as owner-pending | No executable «pull back» exists (no role to pull back to); silence is the real risk | Medium — handled as owner decision, not reviewer ratification |
| S-10 | Contrast/use constraints (semantic hues 3.25–3.90 non-text-only; Clay 3.12 identity-only) | `accessibility.md` | Absorb the gallery contrast table's numeric constraints | Implementers used success/teal as body text in live | Low |
| S-11 | Verification reproducibility | `verification-report.md`, `coverage-matrix.json` | Regenerate after S-3; per-capability rows instead of family-level «current»; record the discrepancy | «Verified» must be falsifiable | Low |
| S-12 | Read-only tool/integrity result anatomy | `component-contracts.md` | **Deferred** until product confirms tool surfaces; then one edit (inputs, promise line, per-item status, «not a record» boundary) | Live pattern is mature; contract premature without product roadmap | None while deferred |

**Already strong — no Standard edit needed:** role triad, color-alone law, surface ladder principles, RTL/numeral rules, tool/record separation, phone geometry, honest verification boundary, gallery long-title wrap craft.

---

## 9. Micro composition gap list — must NOT be moved into the Standard

These live in Micro's scene design, flows, or product voice. Moving them into the Standard would standardize sameness, smuggle policy into primitives, or immortalize current noise.

| # | Gap | Fix in Micro composition | Why not Standard |
|---|---|---|---|
| M-1 | Stale «اليوم» guidance after a sale (derivation covers orders only) | Derive the day block from all recorded events; after a sale show «اليوم: قبضت 250.00 د.أ» + next honest action; keep «يومك مفتوح» only for truly empty days | Per-route operational logic, not a visual contract |
| M-2 | Home lacks a first-glance anchor | Promote recorded cash (when known) via scale/weight + amount slot; other three facts stay visible and quiet; `not_initialized` keeps the road chip | Scene weighting, not a component |
| M-3 | Finance opens with abstract pulse; «ما نعرفه الآن» = numbers in prose | Reorder: cash decision surface → position value rows → pulse; convert prose block to label→trailing-amount rows; keep honesty inventory ≤2 taps deep | Scene structure; reviewer flow intent needs owner confirmation |
| M-4 | Rows: no state channel, boilerplate next-steps | State chip (one word + marker) on order/sale/supplier/schedule rows; next-step line only when a real step exists; terminal rows get state words | Row adoption is composition; the Standard only supplies optional slots (S-6) |
| M-5 | Parties balance inline mid-sentence | Name + one direction-worded amount in the trailing slot («عليك 45.00 د.أ»); movements stay in disclosures | Scene composition |
| M-6 | Period reading = flat 15-row ledger + 25-word formula sentence | Anchor the net result; three grouped subtotals (إيراد/تكلفة/مصروف) with rows collapsed beneath; scope notes as one disclosure | Scene structure; labels only, no new math |
| M-7 | Contentless Home units (مالي / منتجاتي وخدماتي = button-only cards) | One honest live line each (recorded fact or road phrase) or merge into one quiet places row | Scene design |
| M-8 | Truth-limit prose in the reading path | Compress to chips («التحصيل ≠ ربح») + keep verbatim text behind «+» disclosures; remove implementation-negation sentences from user surfaces | Editorial/scene decision; content-guidelines already covers register |
| M-9 | Identical repeated «غير مسجل — سجّله» chips | Differentiate by destination noun + specific verb («سجّل دين عميل»، «سجّل مال المالك»); optional combined «أكمل صورة المال» when ≥2 empty | Flow wiring and roads |
| M-10 | PWA install banner + floating settings/dark chrome on every screen | One-time dismissible slim install card; fold dark toggle into settings (fate tied to owner decision D-2); no floating chrome over content | App shell behavior |
| M-11 | Orders empty-state essay occupies the prime slot | Compress to ≤2 lines + action when empty; after data, anchor today's collected total | Scene logic (honesty preserved: no fabricated priority) |
| M-12 | Failure/retry full-page and inconsistent (reload vs token vs navigate-home) | One pattern: message + in-place retry + return-to-source; one retry verb; section-level loading where safe | App behavior |
| M-13 | Count/collection results don't distinguish matched vs adjusted | Matched = quiet success word; difference = warning/error word + sign; amounts trailing | Scene state rendering using existing roles |
| M-14 | Zero charts/visual comparisons despite honest candidates | One parts/whole bar under الكاش المسجل (wallets + غير الموزع) and one under تكوين التكلفة, each with text alternative — using existing Standard rules | Composition choice; Standard already permits it |

**Guard:** the DecisionPanel grammar (label/ما نعرفه الآن/الخطوة التالية), honesty qualifiers («لا يساوي كاش المشروع»), unallocated-cash strip, and amanah handling are **Micro's voice and policy surfaces** — the Standard must style them, never author them.

---

## 10. Product decisions that cannot be solved honestly without the owner

| ID | Decision | Options | Reviewer position |
|---|---|---|---|
| D-1 | Fate of the live teal accent (#079fa0/#057b7c/#e3f5f5) as link/action ink | (a) ratify as the Standard's link-ink value; (b) choose another value; (c) remove teal from Micro | Reviewers define the **role** and constraints now (S-9); the **value** is the owner's call. Not ratifying-by-silence |
| D-2 | Dark mode: live ships a working toggle; Standard is light-only | (a) remove the toggle from Micro; (b) commission an explicit dark scope (new effort, out of current Standard) | Standard stays light-only until owner decides; no half-support |
| D-3 | Anchor exception rule: may a page use ONE solid Warm-Ink surface block as its anchor? | (a) approve as conditioned exception (never Clay-as-data, never on void states, ≤1/route); (b) scale/weight-only anchoring | Default scale/weight; exception only with owner approval |
| D-4 | Finance flow intent: pulse-first was an earlier deliberate choice | (a) approve reorder to value-first; (b) keep pulse-first and only fix prose | Reviewer recommends value-first; needs owner confirmation because it reverses a recorded intent |
| D-5 | Currency/rounding display policy (`د.أ` vs `دأ`, decimals, unit placement) | Document once in content-guidelines per Micro truth | Reviewers keep explicit «د.أ» + tabular numerals (superior for the audience); owner ratifies |
| D-6 | Tool/integrity surface roadmap (whether S-12 lands now) | Confirm tool screens in scope → contract; else defer | Deferred by default |

---

## 11. Rejected historical or unsafe directions — and why they must not return

1. **Restoring the old gold ramp** — retired by decision; gallery still ships `tag-gold`/`t-gold`/`rc-gold` (S-7 retires it). Amber «in-progress» families would recreate it; pending maps to the Info role instead.
2. **Broad terracotta recolor / terracotta as data ink** — identity hue #D97757 legally stays out of numbers and data surfaces (contrast 3.12 identity-only; benchmark SOP independently enforces the same principle).
3. **Dark mode as a quiet capability** — exists live; unsupported by the Standard; keeping it unratified is the worst of both worlds (D-2).
4. **Success/positive tint on zero or unknown results** — a green 0.00 card claims unearned success; tint only with known non-zero results (F1-12, accepted by adversarial agent).
5. **KPI-dashboard drift: invented metrics, fabricated anchors, fake priorities** — anchors must be recorded facts with period words; the code's own «لا تُفبرك أولوية» rule stands.
6. **Copying Accounting's skin**: their palette hexes, IBM Plex typeface swap, unit-less numbers (SOP «أرقام فقط»), 5-tab nav with center quick-sale, solid direction heroes with literal zeros, steel-blue debt semantics, tap-to-confirm hard delete — each would erase Micro identity or honesty. Principles transfer; pixels do not.
7. **Color without semantics / color-alone states** — every colored state keeps word + sign/icon/marker; grayscale readability stays an acceptance test.
8. **Moving Micro's operational grammar (DecisionPanel, roads, qualifiers, amanah strip) into the Standard** — would template-ize Micro's voice and smuggle financial policy into primitives.
9. **Card-gallery / decoration growth** — more cards, shadows, or tinted surfaces as a richness strategy is rejected; richness comes from anatomy, anchors, and state channels.
10. **Expanding the Standard from prototype evidence alone** (charts, tool-result contracts) — the owner stop rule holds: Standard composition-affecting waves wait until the need is reproduced in the Standard's own scope or product confirms the surface.

---

## 12. Minimum professional improvement set (ordered by comprehension gain × safety)

### 12.1 Wave 0 — Standard truthing (zero visual change; do first)
1. S-1 typography.md scale + numeral mapping · 2. S-2 spacing/elevation/motion values · 3. S-3 token backfill (incl. negative-tint pair, S-4) · 4. S-7 state→tag map + gallery gold retirement · 5. S-10 a11y constraints absorption · 6. S-11 verification regeneration.
*Cost: documentation only. Visual output: identical. Removes the hidden-spec risk for every later wave.*

### 12.2 Micro composition — top 8 (highest comprehension per risk)
1. **M-1 state-aware اليوم** — the screen stops contradicting the owner (trust fix, derivation-only).
2. **M-4 + M-5 row channels** — trailing amount slot + one state word per row; retire boilerplate next-steps.
3. **M-2 cash anchor on Home (conditioned)** — scale/weight first; only when known; qualifiers travel with the value.
4. **M-3 Finance value-first** — decision surface → value rows → pulse; numbers out of prose.
5. **M-6 period anchor + 3 subtotals** — the week's story becomes an answer.
6. **M-9 differentiate the four road chips** — per-fact nouns/verbs.
7. **M-7 give contentless units one live fact** — no button-only cards.
8. **M-10 tame chrome** — one-time install card; settings-folded toggles.
*(M-8 copy compression, M-11 empty-state compression, M-13 result states, M-14 parts/whole bars follow in wave B.)*

### 12.3 Standard contract batch (palette-frozen; after Wave 0, alongside/after owner answers)
S-5 value-zone contract · S-6 row slot vocabulary + optional edge · S-8 period chip · S-9 link-ink role (value pending D-1).

### 12.4 Regression contract — ten testable prohibitions for all future waves
1. No new hue family without a signed owner decision record (teal/gold/steel included).
2. No success/positive tint on 0.00, unknown, or uninitialized states.
3. No color-alone money states — word + sign/icon/marker in the same component.
4. ≤1 solid anchor surface per route; none on empty/zero/unknown; Clay never displays data.
5. Light mode only — no `.dark` tokens in any Standard artifact.
6. No financial policy in primitives — slots and anatomy only, no formulas or KPI names.
7. Truth captions («حد الحقيقة», roads) are non-removable; boilerplate next-steps retire only where a state word makes them factually redundant.
8. Amount integrity — tabular numerals, explicit or column-carried «د.أ», bidi-isolated; no bare digits inside RTL prose.
9. Empty ≠ zero — road entries stay actionable, differentiated per fact, never globally replaced by 0.00.
10. Standard scope freeze — until the owner answers D-1/D-2/D-3, Standard changes are limited to documentation truthing; no composition-affecting Standard waves.

---

## 13. Future development blueprint (plan only — execution requires explicit owner approval)

**Goal:** improve the 29-file Standard, then validate through a new Prototype built above the improved Standard, then stop for owner review before any transfer into Micro.

**Wave 0 — Standard truthing batch.**
- Files owned: `typography.md`, `spacing-radius-elevation.md`, `motion-interaction.md`, `accessibility.md`, `design-tokens.css`, `design-tokens.json`, `color-system.md`, `component-states.md`, `component-gallery.html/css/js`, `verification-report.md`, `coverage-matrix.json`.
- Changes: S-1, S-2, S-3, S-4, S-7, S-10, S-11.
- Dependencies: none. One agent per file family; gallery must render pixel-identically before/after.
- Rollback boundary: per-file git revert; gallery render diff as the tripwire.
- Acceptance: gallery opens with only `design-tokens.css` and renders the verified look; every evidence-panel value has a `.md` home; no unmapped gallery tag; coverage matrix has one row per capability.
- **Gate:** owner reviews Wave 0 diff + answers decision pack D-1/D-2/D-3 (+D-4, D-5).

**Wave 1 — Standard contract batch (small, palette-frozen).**
- Files: `data-display-system.md` (S-5 value zone + S-6 row slots/edge), `component-contracts.md` (S-8 period chip), `color-system.md` (S-9 link-ink role with owner-ratified value from D-1), gallery additions demonstrating each new contract.
- Dependencies: Wave 0 (tokens exist); D-1 answered (link-ink value); D-3 answered (anchor exception wording lands in visual-direction.md or decision-log.md).
- Rollback: revert file + gallery demo; contracts are additive and optional by construction (slots are vocabulary, not requirements).
- Acceptance: a composer can build all three honest voids, a delta, a period-framed metric, a stateful row, and a compliant link from documents alone; component-gallery demonstrates each; verification regenerated.

**Wave 2 — Prototype v0.1 (validation prototype above the improved Standard).**
- Scope: the four highest-impact composition fixes (M-1, M-4/M-5, M-2-conditioned, M-3) inside Micro-like scenes, built only from the improved Standard's contracts; light mode; no new palette.
- Dependencies: Wave 1 + D-4 answer (Finance order).
- Rollback: prototype is an isolated artifact; discard freely.
- Acceptance: §14 validation criteria pass.

**Wave 3 — Composition wave B + hardening.**
- Scope: M-6, M-9, M-7, M-10, M-8, M-11, M-13, M-14 in the prototype; M-12 failure pattern if exercised.
- Dependencies: Wave 2 validation pass.
- Rollback: per-scene revert inside the prototype.
- Acceptance: §14 criteria re-run at 100%; regression contract (§12.4) asserted programmatically where applicable.

**STOP POINT — hard gate before transfer into Micro:** owner reviews Prototype v0.1 against §14 criteria and the §12.4 contract; only an explicit owner approval opens any Micro transfer work. No Micro repository file is touched in any wave of this plan.

**Parallel non-UI track:** none required; all items are inside the waves above. Estimated relative size: Wave 0 ≈ documentation-day; Wave 1 ≈ small contract batch; Waves 2–3 are prototype-scoped.

---

## 14. Prototype validation blueprint (what the post-Standard prototype must prove — not built now)

The prototype must demonstrate, with real (recorded, never invented) data:

1. **State-aware day:** record a sale → Home's day block names it (word + amount) without refresh; an empty day still reads «يومك مفتوح».
2. **One anchor per screen:** Home (recorded cash when known), Finance «الوضع الآن» (position anchor), period tab (net result anchor) — each passable in a 3-second hallway test; nothing above the anchor is visually heavier.
3. **Row channels:** a mixed list (order pending / order ready / direct sale completed / receivable due) locatable by state word + marker without reading labels; grayscale-screenshot test passes; amounts never wrap; long Arabic names clamp.
4. **Honest voids in all three forms:** unrecorded (action chip, differentiated per fact), unknown («غير متاح» ≠ صفر), measured zero (neutral, never success-tinted).
5. **Numbers out of prose:** «ما نعرفه الآن» as value rows; every number sits in a slot; first viewport sentence ≤ ~12 words.
6. **Period framing:** every metric shows or consciously omits a period chip per the contract; period tab anchors the result with three derived subtotals from recorded events only.
7. **Comparison honesty:** delta lines appear only when both values are known; otherwise «غير متاح».
8. **Parts/whole bars (if included):** only true sums (cash distribution; cost composition), with legend + text alternative.
9. **Chart floors (if a chart is included):** labeled axis ticks, zero-day minimum mark, one text answer («أعلى يوم…»); series use ≥2 documented roles with a legend; no all-black series.
10. **Result states:** matched vs adjusted count distinguishable in greyscale; retryable failure shows one in-place retry pattern.
11. **Consistency test:** one named metric («الكاش المسجل») shows one value across Home/Finance/wallet ledger in the same state; navigation revalidates.
12. **Chrome discipline:** no non-business chrome above the h1 after first dismissal; install prompt appears once; settings folded.
13. **Language:** Jordanian voice for owner questions; no implementation-negation sentences in user surfaces; truth-limits ≤8 words in first viewports with verbatim text one tap away.
14. **Platform:** 390px primary; spot-check 320/430 and 130/200% zoom; light mode only; RTL with isolated English numerals and «د.أ».
15. **Regression asserts:** §12.4 prohibitions encoded as checks where the prototype can assert them (tint-on-void, color-alone, anchor count, dark tokens absent).

---

## 15. Final expert recommendation — one safe next step

Send the owner a **three-question decision pack** — (D-1) ratify/replace/remove the live teal as link-action ink, (D-2) keep or remove the dark toggle, (D-3) approve the one-anchor exception rule — and, in parallel, approve the **zero-visual-change Wave 0 truthing batch** plus the **top-4 Micro composition fixes (M-1, M-4/M-5, M-2-conditioned, M-3)** as the Prototype v0.1 scope. Everything ships light-mode, palette-frozen, behind the ten prohibitions — so every later step is validated by test, not taste.

---

## 16. Evidence register and limitations

**Primary evidence artifacts (in reviewer workspace):**
- `evidence/live/LIVE_OBSERVATIONS.md` + 11 screenshots (`live-*.png`, 390×844): setup ×3 steps, foundation, home (before/after sale, dark, scrolled viewport), work (before/after), record dialog + sale form + confirmation, finance ×2 tabs, sale detail, integrity check ×2, tools.
- `evidence/accounting/ACCT_LOCAL_RUN_NOTES.md` + 12 screenshots (`acct-*.png`, 390×844): onboarding ×3, home, finance, orders (empty/with order), order detail sheet, quick sale, settings, debts, reports.
- Micro repository reads: `Home.tsx`, `Finance.tsx`, `Orders.tsx`, `Parties.tsx`, `CashCount.tsx`, `Collect.tsx`, `Tools.tsx`, `homeControlCenterService.ts`, `orderAgreementPresentation.ts`, `FinancePeriodResultSection.tsx`, layout/navigation components, `apps/prototype-web/client/src/index.css` (token/accent verification: accent #079fa0/#057b7c/#e3f5f5 at L64–74; 157× font-size 11–12px verified by count).
- Accounting repository reads: `tailwind.config.js` (semantic 50–900 families), `src/styles/index.css` (card/sheet/badge/num tabular), `OrdersPage.jsx` OrderCard + STATUS_CONFIG + filter counts, `OrderDetailSheet.jsx`, `ReportsPage.jsx` (hero + chart implementation), `DebtsPage.jsx`, `SettingsPage.jsx`, `PageHeader.jsx`, `EmptyState.jsx`, `BottomNav.jsx`, «نظام-التصميم-SOP.md», color/component identity HTML docs.
- Standard: all 29 files of `micro-standard-v2` (incl. `design-tokens.css/json`, `component-gallery.html` evidence panel L871–980, `coverage-matrix.json`, `verification-report.md`).
- Prototype v0: all listed documents + `evidence/VISUAL_FINDINGS_NOTES.md`, `evidence/micro_prototype_v0_inspection_live_findings.md`, `source/` skim, test JSONs.

**Verification spot-checks (adversarial agent):** 157× 11–12px claim re-verified by regex count; 14 undefined tokens verified token-by-token; «no link/accent role in Standard» verified by grep; Home/Finance cash-field identity (`position.recordedCashMinor` both surfaces) verified — mismatch hypothesis falsified; dark-mode absence in Standard verified (zero matches across 29 files).

**Limitations (stated plainly):**
1. Micro Live routes not exercised live: parties/people book, suppliers & purchases detail, notes/collections flows, period statement and full period reading screens, appointments grid, product-cost calculator internals, salary estimation. These were reviewed from repository code and copy only.
2. Only a direct sale was recorded live; the order lifecycle (draft → agreement → execution → completion → review) was not completed end-to-end in the live session; lifecycle rendering evidence comes from code + Prototype v0.
3. Accounting was inspected via local build in advanced mode with one test order; BOM inventory, PDF export, calendar view, WhatsApp share were not exercised. Sub-agent 4 relied on capture notes + source verification (its context could not render the PNGs); all its visual-mechanism claims were independently verified in source.
4. One reviewer sub-agent discarded an OCR/VLM read of screenshots after hallucinated Arabic text contradicted session notes — evidence discipline held; claims rest on the structured notes and source.
5. The suspected cross-screen cash mismatch was falsified as an observation-order artifact; it is retained only as an acceptance test (§14-11), not a defect.
6. Arabic RTL rendering was reviewed in Chromium at 390×844 only; device-native rendering, OS-level bidi quirks, and screen readers were not tested (consistent with the Standard's own verification boundary).
7. «First-3-seconds» verdicts are professional inference from anatomy and the owner persona; no human user testing was performed in this session.
8. The live deployment may change independently of the reviewed repositories; screenshot evidence pins the observed state to 2026-09-13.

---

## 17. SUB-AGENT SYNTHESIS

**Sub-agent 1 — First-glance user (12 findings).** Established that Home/Finance/Orders answer none of the owner's four questions before reading; the strongest number lands mid-page; stale «اليوم» guidance breaks trust; typography is fine-print (157× 11–12px); «ما نعرفه الآن» and truth-limit prose demand reading; identical void chips read as boilerplate; proposed the one-anchor rule, row amount channel, and copy compression. Synthesis: accepted in full except F1-08 (cash mismatch) which the adversarial pass falsified as an observation-order artifact (downgraded to acceptance test); F1-02's "hero" framing conditioned to recorded-facts-only anchoring.

**Sub-agent 2 — Micro operational UX (13 findings).** Mapped screen-by-screen composition strengths/weaknesses; identified pulse-first Finance, prose-embedded numbers, state-blind rows, boilerplate next-steps, contentless Home units, inconsistent failure/retry, and the live-vs-Standard teal drift; produced the «must not move into Standard» list (DecisionPanel grammar, roads, qualifiers, amanah strip, retry mechanics, dark mode). Synthesis: accepted; its F2-04 (honest parts/whole bars) joins wave B; its reorder proposal carries the owner-confirmation condition (D-4).

**Sub-agent 3 — 29-file Standard (14 findings).** Diagnosed the four structural causes (hidden operative spec, artifact/basis token divergence, named-but-unspecified contracts, vocabulary mismatch); produced the file-by-file gap list with exact targets (S-1…S-12) and the must-preserve list; deferred chart/tool-result expansions per the owner stop rule. Synthesis: accepted in full; S-9 reframed from «document positive tint» to «define link-ink role with owner-pending value» after the adversarial pass showed no executable pull-back alternative.

**Sub-agent 4 — Accounting benchmark (12 findings + principles P1–P11).** Verified the local run in source; extracted the transferable principles (one anchor per page, semantic color economy with identity-barred-from-numbers, badge+edge states, row slots, surface ladder, grouped density, chart floors, learned-hue action grammar, teaching empty states, shared chrome, restraint bans); produced the do-not-copy list. Synthesis: accepted with two demotions — solid anchor blocks demoted from default to owner-conditioned exception (B3), and 44px identity chips not adopted (Micro keeps its caption/voice identity); tint-triplet proposal accepted only as derivations of Micro's own approved hues.

**Sub-agent 5 — Adversarial/regression guard.** Verdicts: teal → accept-with-conditions (define role now, value owner-pending; silence is the real risk); tint pairs → accept-with-conditions (same-hex derivations, complete pairs, marks only); solid anchor → accept-with-conditions (default scale/weight; exception ≤1/route, never on void); charts → defer Standard edit, keep floors as acceptance criteria. Falsified the cash-mismatch defect; confirmed the 157× count, the 14 undefined tokens, the missing link role, and the model-driven staleness of Home's day card. Produced the ten-prohibition regression contract and the three-question decision pack. Synthesis: adopted wholesale; its rankings define §12's order.

**Disagreements resolved:** anchor color → scale/weight default, solid exception owner-gated (§10 D-3). Teal → role now, value owner-gated (D-1). Charts now-vs-defer → defer Standard expansion, floors bind the first real chart (§14-9). Row anatomy location → slot vocabulary in Standard as optional; adoption per screen is Micro composition; truth captions non-removable. State chips → one word+marker per row; icon-chip stacks forbidden.

---

## 18. Finding register (required format, consolidated)

Format per finding: ID · Evidence · Confidence · User impact · Area · Classification · Recommended solution · Regression risk · Acceptance criterion.

- **F-01 (F1-01/F2-01)** · LIVE §2 + `Home.tsx:330–335` + service L286–299 · Confirmed · Screen contradicts the owner's own action after a sale; trust break on the primary screen · state/composition · Improve in Micro composition · Event-derived day block (word + amount) with honest empty state · Invented-summary drift; keep strictly event-derived · Recording a sale updates «اليوم» without refresh; empty day still reads «يومك مفتوح».
- **F-02 (F1-02/F2-02)** · LIVE §2 + `Home.tsx:351–363` + `index.css:5152–5186` · Confirmed · No first-glance answer to «شو وضع المشروع؟»; four equal cards · hierarchy/composition · Improve in Micro composition (Standard rule S-5/S-6 supports) · Recorded cash as anchor by scale/weight when known; others quiet · KPI-ization; keep labels neutral and all facts visible · 3-second hallway test names the cash figure first.
- **F-03 (F1-03/F2-11/F3-09/F4-07)** · live teal `index.css:64–74` vs `color-system.md` (11 roles, no link) · Confirmed divergence; resolution owner-gated · Standard cannot verify its own product; live aliveness unreproducible · color/governance · Product decision required (D-1) + Standard role definition (S-9) · Decorative-color licensing; bind role to use-list · Every live color token maps to a named role or is removed.
- **F-04 (F1-04/F2-05/F2-06/F4-02/F4-03)** · `Orders.tsx:164–196` vs Accounting OrderCard + `component-states.md` · Confirmed · Rows read as sentences; state and amount not glance channels · row/state · Improve in Standard (optional slots S-6) + Micro adoption (M-4/M-5) · Sameness with benchmark; keep Micro captions as caption slot · Mixed list scannable by state without reading; amounts never wrap.
- **F-05 (F1-05)** · `typography.md` (3 sentences) + live 157× 11–12px (verified) · Confirmed · Fine-print interface; financial facts below reading comfort · typography · Improve in Standard (S-1) + Micro CSS · Density loss; offset by hierarchy · Money values ≥15px; 11–12px reduced ≥80% to metadata.
- **F-06 (F1-12)** · LIVE §7 teal net card at 0.00 · Confirmed observation; misread Inferred · Zero can read as «you're fine» — false positive · color/state · Improve in Standard (grammar) + Micro · Aliveness loss; compensate via anchors · No participant reads zero net as profit; tint only with known non-zero.
- **F-07 (F2-03/F1-06)** · `Finance.tsx:309–481` · Confirmed · High reading load to find «كم معي الآن» · hierarchy/content · Improve in Micro composition (M-3) · Reverses recorded pulse-first intent (D-4) · Every position number sits in a value slot; inventory ≤2 taps deep.
- **F-08 (F2-07)** · `Parties.tsx:150–170` · Confirmed · «مين عليه إلي؟» not skimmable · row · Improve in Micro composition (M-5) · Dual-direction parties need two-line slot · Per-party direction-amount readable at scroll speed.
- **F-09 (F2-08)** · `FinancePeriodResultSection.tsx:92–303` · Confirmed · Period story unreadable at a glance · hierarchy/density · Improve in Micro composition (M-6) · Subtotals must derive from recorded events only · Net result is the page's primary value; detail ≤1 tap.
- **F-10 (F2-09/F1-11)** · `Home.tsx:364–408`, `Orders.tsx:89–110` · Confirmed · Contentless shells and empty-state essays occupy prime slots · density/state · Improve in Micro composition (M-7, M-11) · Inventing values when empty; show road phrase · No button-only permanent unit; empty priority ≤2 lines.
- **F-11 (F2-10/F1-10)** · retry code paths + LIVE §1 · Confirmed · Failures feel like lost pages; chrome competes with business · state/navigation · Improve in Micro composition (M-12, M-10) · Feature discoverability; mitigate via settings · One retry pattern app-wide; zero business chrome above h1 after dismissal.
- **F-12 (F2-13)** · `CashCount.tsx:186–203`, `Collect.tsx:199–221` · Inferred (not both states live-exercised) · Moments of truth look like every card · state/color · Improve in Micro composition (M-13) · Color-alone misuse; pair word+sign · Matched vs adjusted distinguishable in greyscale.
- **F-13 (F2-04)** · no chart components; `data-display-system.md` allows honest bars · Confirmed · Spatial relationships must be read as parallel numbers · chart/composition · Improve in Micro composition (M-14) · Chart misuse; restrict to true sums · Cash distribution understandable without reading numbers.
- **F-14 (F3-01/F3-12)** · gallery evidence panel L871–980 vs 3-line md files · Confirmed · Composers cannot reproduce the verified interface · documentation/typography · Improve in Standard (S-1, S-2) · Near zero · Every evidence-panel value has a .md home.
- **F-15 (F3-02/F3-03/F3-11)** · gallery css tokens vs shipped files; verification claims · Confirmed · Verified look renders on fallbacks; «verified» unfalsifiable · tokens/governance · Improve in Standard (S-3, S-4, S-11) · Low · Gallery renders from design-tokens.css alone; parity claim true.
- **F-16 (S-9/B1)** · no link role; live teal as links/nav/tints · Confirmed divergence · Link affordance undocumented; a11y exposure if semantic hues used as text · color · Improve in Standard role + Product decision D-1 · New-palette violation if reviewers ratify value · Role defined with AA constraint; value owner-recorded.
- **F-17 (F3-04)** · `input-system.md` void rule with no visuals; live honesty pattern mature · Confirmed · Defining honesty device re-decided per screen · data display · Improve in Standard (S-5) · Low · All three voids + delta composable from documents.
- **F-18 (F3-05)** · documented states vs gallery tags; gold tags shipped · Confirmed · No authoritative badge language; deprecated ramp leaks · states · Improve in Standard (S-7) · Low · Every gallery tag names a documented state; gold retired/re-justified.
- **F-19 (F3-07)** · «period control» named once; live has chips; benchmark has segmented+dates · Confirmed · Period framing re-invented per screen · data display · Improve in Standard (S-8; time semantics product-owned) · Low · Metrics show/consciously omit period per written rule.
- **F-20 (F3-14)** · live integrity-check pattern mature; «tool result» named once · Confirmed pattern · Trust screens have no shared look · contracts · Defer (D-6) then Standard edit · None while deferred · When product confirms, anatomy lands in one edit.
- **F-21 (F3-10/C12)** · live dark toggle vs light-only Standard · Confirmed · Unsupported mode reachable in product · governance · Product decision (D-2); Standard stays light-only · None for Standard · No unapproved mode in production builds.
- **F-22 (F1-08)** · Home 1,750 vs Finance 1,500 — falsified: same field `position.recordedCashMinor`; session captured Finance pre-sale · Owner decision → downgraded · None (artifact); consistency still worth asserting · state · Acceptance test only (§14-11) · None · Same metric shows one value across screens in the same state.
- **F-23 (F1-07/F2-12)** · truth-limit copy at glance points; «هذا لا ينشئ بيعًا تلقائيًا…» on empty مبيعاتي · Confirmed · Honesty voiced as disclaimers; reading demanded at action points · content/language · Improve in Micro composition (M-8) · Over-compression eroding truthfulness; verbatim text stays one tap away · No truth-limit sentence >8 words in first viewports; long form ≤1 tap.
- **F-24 (F4-10)** · benchmark `.num/.tnum` tabular + unit-less rule vs Micro explicit «د.أ» · Confirmed · Alignment/trust in numeric columns; unit clarity · typography · Product decision (D-5, minor): tabular hard rule + keep «د.أ» · Porting unit-less rule would reduce clarity · All amounts tabular, end-aligned, unit documented once.
- **F-25 (F4-05/F4-06/F4-08/F4-11/F4-12)** · settings grouped rows; chart floors; teaching empty states; shared header; persistent nudges · Confirmed · Long-page scannability; chart legibility; next-move clarity; chrome continuity; safety actions completed · density/chart/state/navigation · Standard contracts (S-batch) + Micro composition · Busier interfaces; guard §12.4-7 · Group/row grammar everywhere; charts meet floors; nudges dismiss on action only.

---

## 19. Decision separation (explicit)

- **Confirmed current facts:** §0 session statements; F-01–F-05, F-07–F-15, F-17–F-21, F-23–F-25 evidence lines; falsification of F-22.
- **Professional inferences:** F-06 (misread risk), F-12 (both states not live-exercised), §2.3 felt-experience synthesis, §3.2 mechanics reduction.
- **Recommendations for the 29-file Standard:** S-1…S-11 (S-9 value owner-pending); S-12 deferred.
- **Recommendations for Micro composition:** M-1…M-14 (M-3 conditioned on D-4; M-2 conditioned on D-3).
- **Product decisions for the owner:** D-1 teal/link-ink value · D-2 dark mode · D-3 anchor exception · D-4 Finance flow intent · D-5 currency/rounding policy · D-6 tool-surface roadmap.
- **Deferred items:** S-12 tool-result contract; Standard chart expansion (until first real chart exists); dark-mode scope (until D-2).
- **Rejected historical/unsafe directions:** §11 items 1–10 (gold ramp, terracotta-as-data, quiet dark mode, tint-on-void, KPI drift, Accounting-skin copying, color-alone states, Standardizing Micro's voice, decoration growth, evidence-free Standard expansion).
- **Limitations from access constraints:** §16 items 1–8 (unexercised live routes; sale-only lifecycle; Accounting deep flows; OCR discard; artifact falsification; single-browser RTL; no human testing; deployment drift).

*End of report. No implementation prompt follows. The Standard, Micro, Accounting, Prototype v0, and Documents remain untouched. Awaiting owner review.*
