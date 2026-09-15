# 02 — Research and Direction Synthesis

**Delivery:** `micro-visual-product-concept-002`
**Task ID:** 2-f · **Agent:** Central orchestration agent (consolidation of sub-agent reports 01–05)
**Date:** 2026-09-06
**Inputs:** `subagents/01-visual-research-and-benchmarks.md` (2-a) · `subagents/02-art-direction-and-spatial-language.md` (2-b) · `subagents/03-mobile-motion-and-interaction.md` (2-c) · `subagents/04-rtl-accessibility-and-data-visualization.md` (2-d) · `subagents/05-adversarial-critique-and-decision.md` (2-e) · `en/00-SOURCE-INTAKE-REPORT.md` · `en/01-current-work-lessons.md`
**Method:** The five reports were read in full; conflicts were resolved by explicit ruling (adopting the adversarial judge's rulings R-A…R-J where sound, overriding where this synthesis has better grounds — every override is documented). No opinions were averaged; every decision below has one owner and one reason. Nothing in this document claims inspection of the three absent source packages.

---

## 1. The most important visual findings

1. **Trust in a financial product is typographic, not decorative.** Across every benchmark family that fits Micro (digital ledgers, neobank account composition, invoice-first small-business apps), the products that read as financially serious earn it through number discipline: tabular figures, decimal alignment, one money language, fixed amount columns, honest marks for unknowns. Micro's differentiation must therefore come from composition and typographic craft — exactly what C-17 permits and what the anti-reference squandered on card walls.
2. **The owner's day is figure-first and list-shaped.** The seven owner questions («وين الكاش؟ من عليّ؟ مين مدين لي؟») are answered by numbers and by named people — not by module chrome. Ledger vocabulary is even native to Micro's own glossary («دفتر الناس», «كشف الأسبوع», «السجل»). A visual language that mirrors the paper دفتر the owner already trusts (subject on the reading side, amounts in a fixed column on the other, hairline rhythm between rows) is both distinctive and pre-trusted.
3. **Calm is a countable property.** The concept can guarantee "calm but not empty, operational but not crowded" only as arithmetic: 2 elevation levels, ≤1 grouped surface per screen, ≤5–8 blocks before the first collapse, rows ≤3 lines, one primary action, one hero figure, 4 motion primitives, zero decorative motion.
4. **Motion's job is meaning, not energy.** Report 03's binding register (M-out/M-in/M-flat curves, 80–280ms classes, zero overshoot, forbidden bounce/counters/confetti) turns motion into a truth-carrier: saving, completion, waiting, location. The single most important choreography is quiet completion — the receipt that replaces the form with closure numbers, never a counter, never applause.
5. **The bidi contract is a correctness issue, not a style preference.** Report 04's ruling (ratified by 05 as "the single best catch"): isolate ONLY the digits inside `<bdi dir="ltr">`, keep the unit «د.أ» in the RTL flow — unit-inside-isolation renders «د.أ 20.00» in RTL and silently violates the binding "unit after the number" rule on every money string in the product.
6. **Contrast discipline is already decisive.** Measured: `#964e33`+white 6.11 (the only terracotta action bg that passes); `#b4613f`+white ≈4.42 audit (4.45 recomputed) — press-only, never described as a pass; `#cc785c`+white 3.28 — confirms C-02; `#057b7c` on soft fills 4.11 fails normal text. Roles, not hope, decide pairings.
7. **Charts must be answerable sentences.** Four chart contracts survived: paired bars (week in/out), person-list aging (receivables), relationship bar with hatched «عربون محفوظ» bracket (order payment), segmented row (wallet composition) — each with period, unit, source state, RTL time-flow, and a text interpretation that IS the non-visual alternative.

---

## 2. Three clearly differentiated concept directions

| | **D-A «دفتر هادئ» — The Calm Ledger** | **D-B «مكتب المالك» — The Owner's Desk** | **D-C «مسار المال» — The Flow of Money** |
|---|---|---|---|
| Essence | A page of a trustworthy paper ledger: figures lead, hairlines separate, boxes almost never appear; warmth from the warm canvas, the terracotta header rule, and typographic craft | A calm cockpit: persistent Top Focus Shell with a live figure, quiet grouped modules, restrained elevation hierarchy | Every amount is a directed movement (in/out/held) shown through relationship bars and flow compositions; motion carries direction |
| Geometry | Radius 0/4/12; 2 elevation levels; hairline-first; fixed 88px tnum amount column | Radius 6/10/14/20; 4 elevation levels; bordered modules; 96–112px sticky shell | Radius 8/16/999; 3 elevation levels; 6px relationship bars under rows; pill chips |
| Row grammar | Subject right + caption below; amount left in fixed column, decimal-aligned | 48px rows (breaches Arabic floors), inline amounts after labels | 60–72px bar rows; amount pairs «قبض 8.00 من 10.00»; bar fills right→left |
| Motion | 4 primitives: sheet rise, value settle, divider emphasis, success mark | 6 primitives incl. shell figure count-tween (violates forbidden register) | 8 primitives incl. number roll and 300–350ms travels (violate the 280ms cap and contrast physics) |
| **Strengths** | Answers owner questions in the first 88–96px with one 34px figure; thumb-zone compliance; RTL-native (mirrors the paper دفتر); trust-as-typography; countably calm; glossary-native grammar; cheap to build honestly | Operational focus figure always visible; strong guard against emptiness; familiar cockpit metaphor | Financial language made visible (in/out/held); relationship bars map directly to deposit/receivable semantics; RTL bar fill is native |
| **Risks** | Flatness/coldness if typographic craft or warmth tokens fail (mitigated: warm canvas `#faf6f2`, terracotta header rule, `#f4e4db` fills on facts/selected rows, 3xl hero breathing) | Reads as a competent generic dashboard (the direction a template would produce); 48px rows and 12px captions violate Arabic legibility floors; module chrome per screen; count-tween banned | Its essence is animated flow, and the binding motion register forbids its core primitives; bars fail 3:1 on tinted zones (measured 2.88:1); static form is a different, weaker direction; infographic energy reads younger than "financially serious" |
| Adversarial score | **28/30** | 16/30 | 18/30 |

---

## 3. Recommended direction — D-A «دفتر هادئ» The Calm Ledger

**Why it is stronger for Micro, in the order that matters:**

1. **It answers the owner's questions fastest.** «وين الكاش؟» is answered in the first 88–96px by one 34px hero figure with its unit — before any chrome, module, or bar. D-B needs 96–112px of shell; D-C needs bar rows to say the same thing.
2. **It is RTL-native without translation effort.** Subject-right / amount-left in a fixed LTR-isolated column mirrors the Arabic paper ledger the owner already trusts; reading direction and numeric order never fight (the bidi contract closes the last leak).
3. **It makes honesty positional, not stylistic.** «—» occupies the amount column at the exact size a number would; the deposit bracket lives inside the paid segment of a one-track bar; receipts are closure sentences with final tabular digits. These are grammar facts, unremovable by restyling.
4. **It is countably calm and countably operational** — the only direction whose calm can be verified in review (2 elevation levels, 1 card quota, ≤8 blocks, 4 motion primitives, one primary).
5. **It is distinctively Micro with zero palette or logo change** — the grammar derives from the product's own glossary and the mark's principles (weight, posture, proportion, contour, quiet detail), not from a component library.

**Merged into D-A from the rejected directions (nothing else):** the relationship bar with hatched «عربون محفوظ» bracket and the segmented wallet-composition row (D-C's verifiable ideas, already specified as chart contracts 3–4) as chart *content* inside Orders/Finance; and D-B's live status line under the header question («الحالة: مسجل · متزامن») as the truth slot. D-B's modules, elevation stack, and inline numbers are rejected; D-C's row anatomy, pill geometry, and motion primitives are rejected.

---

## 4. What will be visible in the HTML review (`prototype/micro-visual-concept-review.html`)

A single self-contained, browser-openable artifact with a review console (all controls strictly outside the phone frame) and a product-real phone:

- **Six in-phone surfaces, Arabic RTL default:** «مشروعي الآن» Home (sticky typographic header, 2px terracotta rule, today list ≤4 rows, ruled 2×2 facts grid with honest unknowns, recent changes, quiet links row); «العمل» Orders (decision line first, working search + filter chips, order rows with relationship bar and «قبض 30.00 من 50.00» pairs, sales, drafts); «مالي» Finance (34px hero figure, decision line with contextual primary, segmented wallet-composition row with hatched أمانات, ruled position grid with «سجّله» road, أمانات dual-truth line, collapsed layers); «كشف الأسبوع» StatementView (stack reader with back, period switcher, paired-bar week chart with unrecorded-day gap + footnote, cash line «82.50 د.أ ← 145.00 د.أ», receivables aging with micro-bars); «سجّل» Quick Capture sheet (menu → sale form with the NumericSurface — 6+2 slot grid, stable digits, position underline, stepper + keypad + quick chips, optional swipe → receipt with quiet completion → CorrectionPreview dialog from «تراجع»); «أدواتي» Tools (question header, live result bar in the thumb zone, saved estimates, module status rows).
- **The full state set inside real surfaces:** offline truth line (toggle), syncing→synced, unknown («سجّله», «غير محدد بعد», «غير متاح»), estimated (تقديري + dotted underline), loading skeleton (first-boot case), saving, quiet-completion success, failure-and-retry with preserved input, discard guard («في رقم مكتوب — تسجّله أو تتجاهله؟»), honest empty (search no-match), correction preview.
- **Review console (outside the phone):** AR⇄EN language toggle (full LTR mirror, chevrons and charts mirror, money never mirrors); light/dark; normal/reduced motion; width switcher 320/360/390/430; motion demonstrations (quiet save auto-run, offline→sync, failure→retry, first-paint skeleton); a measured-contrast legend; the coverage list; and a **directions comparison mode** showing static, type-floor-compliant, zero-animation single-frame previews of D-B and D-C beside the recommended D-A, with their rule bullets and why they lost.
- **Realistic, coherent Arabic financial content** from the verified corpus (مشغل ليان; سارة's صندوق خشبي 35.00 with عربون 15.00 محفوظ; خالد's 20.00 debt; ريم's draft; the 06–12/09/2026 week reconciling exactly: 82.50 + 85.00 − 22.50 = 145.00 د.أ).

**Coverage list (published in the artifact, per the integration judge's requirement):** in scope — Home, Orders, Finance, StatementView, Quick Capture sheet + NumericSurface, CorrectionPreview dialog, Tools (compact). Out of scope for this review, named with one-line reasons — Settings/vertical profile list (no open decisions depend on it); PartyDetail/دفتر الناس ledger page (its core pattern — per-party dominant balance — is previewed inside the aging list); cash closing count screens (deliberate thumb-zone exceptions, unchanged contracts); assistant conversation shell (Phase 2 defined boundaries; visual work deferred); WalletLedger (same contract as StatementView). All are committed for the Stage-4 final package after approval.

---

## 5. Decisions that must not be left ambiguous (binding for the build)

These are the resolved rulings and token sheet. Where they override a sub-agent proposal, the override is stated.

### 5.1 Unified token sheet (resolves the three-canvas blocker; adopts R-A with one override)

| Token | Light | Dark | Notes |
|---|---|---|---|
| canvas | `#faf6f2` | `#1c1815` | 02's warm light canvas + 04's two-tone dark; `#332d27` never appears in light theme |
| elevated surface (sheets/dialogs) | `#ffffff` | `#332d27` | dark elevation without new brand hues |
| ink (body) | `#221c18` | `#f4e4db` | overrides 04's `#332d27`-as-light-ink re-role (F-03: same hex as dark canvas would confuse reviewers) |
| ink-2 (secondary) | `#5c5148` | `#c9bdb3` | |
| hairline | `#e5dcd6` | `rgba(213,145,114,0.18)` | warm dark hairline to keep dark frames warm (RK-01) |
| scrim | `rgba(34,28,24,0.40)` | `rgba(0,0,0,0.50)` | |
| brand atmosphere / rules | `#cc785c` | `#d59172` | never white text on light brand; dark brand may carry text (5.26–6.82 measured) |
| action (primary bg) | `#964e33` + white (6.11) | `#8fd5d6` bg + `#1c1815` label (10.63) | C-03-compliant, hierarchy-justified |
| pressed (transient) | `#b4613f` | `#332d27` 24% overlay | C-04: press-only, ≈4.42:1 white pairing never called a pass |
| accent text / quiet actions | `#057b7c` | `#8fd5d6` | |
| accent graphics | `#079fa0` (≥3:1 only) | `#5ec0c1` | chart "in" bars, icons |
| out-deltas / decision marker | `#964e33` | `#d59172` | |
| focus ring & NumericSurface cursor | `#964e33` | `#8fd5d6` | R-B — never shares a hue with the success mark |
| success mark | `#057b7c` on `#e3f5f5` disc | `#8fd5d6` on `#332d27` | |
| danger / warning (functional text tokens) | `#b3362e` / `#9a6700` | `#ff9d94` / `#e6b455` | text/icon roles only — never chart coding; glyph+label is the encoding (R-H) |

### 5.2 Binding system decisions

| ID | Decision | Owner / basis |
|---|---|---|
| DSY-01 | Build D-A only; D-B/D-C are static, type-floor-compliant, zero-animation comparison previews; review controls live outside the phone frame | 05 resolution 1 |
| DSY-02 | Motion authority = report 03 in full (M-out `cubic-bezier(0.05,0.7,0.1,1)`, M-in `cubic-bezier(0.3,0,0.8,0.15)`, M-flat `cubic-bezier(0.4,0,0.2,1)`; micro 80–120 / standard 150–220 / surface 240–280ms; loops 1200ms linear; hold-release 600ms; no travel >280ms; forbidden register enforced) | R-C |
| DSY-03 | Reduced motion = full alternatives (instant swaps, static marks, focus/text compensation), never shortened animation; honors `prefers-reduced-motion` by default | R-D |
| DSY-04 | Bidi contract: `<bdi dir="ltr">` around digits only; unit «د.أ» in the RTL flow; signs inside the isolate (U+2212); dates isolated; parentheses avoided around money | R-I, 04 §1.4 |
| DSY-05 | Numerals: ASCII digits everywhere (input = display; receipts match paper; en-US grouping); Arabic-Indic appears nowhere in v1 numerics | 04 §1.5 |
| DSY-06 | Arabic floors: nothing below 13px; body 15px; rows ≥56px; body line-height ≥1.6 (overrides H-A's 12px overline and 1.55) | R-F, 04 §1.1 |
| DSY-07 | Type scale: hero 34/40 700 tnum · question 20/28 600 · section 16/24 600 · row 15/24 400 · row amount 16/24 600 tnum · caption 13/20 · overline 13/18 500 · button 15/20 600 | 02 §3.1 as amended by DSY-06 |
| DSY-08 | Geometry: radius 0/4/12 (page/controls/sheets+dialogs); 2 elevation levels (E0 hairline-flat, E1 floating sheets/dialogs/FAB); hairlines 1px `#e5dcd6`; emphasis rule 2px `#cc785c` under headers; attention = 2px `#964e33` right-edge marker; no border ≥3px | 02 §3.1, R-G |
| DSY-09 | Spacing: 4/8/12/16/24/32/48 named xs/sm/md/lg/xl/2xl/3xl; screen margin 16px; amount column fixed 88px | 02 §3.1 |
| DSY-10 | Hero figure renders in ink (`#221c18`/`#f4e4db`); `#964e33` reserved for the action role, out-deltas, and the decision marker | R-G |
| DSY-11 | FAB = 64×48 radius-4 center-slot text FAB «سجّل» in the five-destination bottom nav, `#964e33`+white (6.11), press `#b4613f` transient; dark: `#8fd5d6` bg + `#1c1815` label | 05 resolution 6 (overrules 04's 56px circle) |
| DSY-12 | Grouping: list-with-dividers default; grouped surface only if ≥2 of {same source record & destination · one semantic unit · must float}; card quota ≤1 per screen; Home facts = ruled 2×2 grid, not cards | 02 §3.1 |
| DSY-13 | Density: Home ≤8 blocks; Finance ≤5 before first layer; today ≤5 rows; recent changes 3; rows ≤3 lines (2 default); one hero per screen; one primary per screen; Finance text ≤257 words | 02 §2.5 |
| DSY-14 | Charts: the four contracts (paired bars / person-list aging / relationship bar with hatched deposit bracket / segmented row); time flows right→left in RTL and mirrors in EN; every chart carries period, unit, source state, and a text interpretation that IS the non-visual alternative; unrecorded day = gap + footnote, never a zero bar | 04 §3, ratified |
| DSY-15 | Status grammar: glyph shape + label word, color tertiary — filled=happened, hollow=expected, dashed=estimated, ring=attention, slash=offline, split=conflict, em-dash=unknown | 04 §2.3, R-H |
| DSY-16 | Money semantics visible: deposit = hatched bracket inside collected segment + caption «العربون كاش حقيقي في الدرج، مرتبط بطلب غير منجَز…»; أمانات = hatched segment + dual-truth sentence; unknown ≠ zero everywhere | C-19, 04 §4 |
| DSY-17 | First paint: cached figures + staleness qualifier when data exists; skeletons only for genuinely unknown content (first boot); CorrectionPreview = center dialog with static will-change/won't-change lists | R-J |
| DSY-18 | Quiet completion choreography per 03 §4 (T0 → saving 80ms → write → form fade → receipt 200ms M-out, mark 0.8→1 zero overshoot, closure sentence with final digits, action row, focus move + polite live region, one 600ms localized highlight beneath the scrim, «تم» closes); failure preserves the typed amount | 03 §4 |
| DSY-19 | NumericSurface: 6+2 slot grid, digits stable (deterministic single-slot shift per keypress), pinned entry-slot underline `#964e33`/`#8fd5d6`, literal (unmirrored) finger-to-slot swipe, full tap alternative (tappable slots + stepper + keypad), 4 quick-amount chips | 03 §2.3 |
| DSY-20 | Touch targets ≥44×44 (48 for keypad/primary); ≥8px separation; transparent padding expands quiet links to 44px | 04 §2.1 |
| DSY-21 | Accessibility: `tablist` navigation with focus-to-h1 on commit; row accessible names concatenate their data; charts `role="img"` with the interpretation sentence; money mutations announce politely, blocking errors assertively once | 04 §2.4–2.5 |
| DSY-22 | Typeface: two-font path for the review artifact — Noto Sans Arabic (Arabic) + Inter with locked tabular figures for digit runs inside the `bdi` isolate; single-face replacement is a Stage-4 build-gate decision | 05 resolution 10 |
| DSY-23 | Light and dark ship together for every frame from the start; every pairing used is measured (scripted check, fallbacks per §5.1, never eyeballed) | 05 resolutions 7–8 |
| DSY-24 | The 320px frame is built and verified first (long-content matrix + 88px-column arithmetic: 288 − 88 − 44 − 8 = 148px subject budget) before other widths | 05 resolution 9 |
| DSY-25 | One action word per row («حصّل»/«سلّم»/«أكمل»); details behind the row tap | 04 OQ-4 resolved |

### 5.3 Open questions closed (owner = central orchestrator unless noted)

| Source OQ | Resolution |
|---|---|
| 01 OQ-1 statement sharing / OQ-4 lifecycle rows / OQ-6 CorrectionPreview surface | Deferred to Stage 4 / lifecycle rows live in Orders lists, not Home / dialog per DSY-17 |
| 01 OQ-2 numeric typeface / OQ-3 dark-mode order / OQ-5 skeleton honesty | DSY-22 two-font path / both themes ship together (DSY-23) / DSY-17 cached-first |
| 02 OQ-1 dark role mapping / OQ-2 neutrals / OQ-3 semantic measurement / OQ-4 FAB / OQ-5 sticky scope | §5.1 (R-E) / §5.1 (R-A) / measured functional tokens, glyph+label binding (R-H) / DSY-11 / sticky on Home+Finance only; Orders/Statement/Tools static 72px headers |
| 03 OQ-1 haptics / OQ-2 dark pressed / OQ-3 cursor role / OQ-4 digit shift / OQ-5 Finance first paint | Out of scope for the HTML review (device-test question, listed in open questions) / `#332d27` 24% overlay + `#d59172` 16% row tint / DSY-19 cursor = focus family (R-B) / append-mode deterministic shift accepted / DSY-17 |
| 04 OQ-1 «د.أ» SR pronunciation / OQ-2 ink-canvas tokens / OQ-3 RTL time-flow / OQ-4 two actions at 320 / OQ-5 Arabic-Indic / OQ-6 export staleness | Device-test question (kept open for Stage 4) / §5.1 approved / DSY-14 adopted, flagged for usability validation / DSY-25 one action per row / DSY-05 ASCII locked for v1 / show when stale > 7 days (aligned with away-card trigger), rule flagged for product confirmation |

**Remaining open questions for the owner (review-gate questions, not blockers):** RTL chart time-flow validation with real owners; haptics policy; «د.أ» screen-reader pronunciation strategy; export-staleness threshold confirmation; single-face typography decision at Stage 4.

---

*This synthesis is the single decision source for the Stage-2 build. The integration judge's four pre-build fixes are satisfied: the token sheet (§5.1), motion authority (DSY-02), Arabic floors (DSY-06), and the coverage list (§4).*
