# 02 — Art Direction, Shape, Surface & Composition

**Delivery:** `micro-visual-product-concept-002`
**Task ID:** 2-b
**Agent:** Sub-agent 2 — Art Direction, Shape, Surface, and Composition Specialist
**Date:** 2026-09-06
**Basis:** Design reasoning on verified constraints only — intake registers C-01..C-20, the 12-row lessons table, and the Target-State screen contracts §4.0–§4.12. No live research claimed. No inspection of absent files claimed (logo file, recovery zip, anti-reference HTML were not present). All contrast ratios marked "computed" were derived in this report with the WCAG 2.x relative-luminance formula and await tool verification; authority-measured values are quoted as authority, not re-measured.

---

## 1. Design problem statement

Micro's owner stands between two customers, holding the phone in one hand, and asks seven questions all day: *What financial position am I in now? What changed? Why? Who owes me? What do I owe? What needs attention today? What should I do next?* The visual language must therefore make **figures legible at arm's length in under 2 seconds** (a hero figure ≥28px, tabular digits, decimal-aligned in a fixed column), make **every row answerable with one thumb tap** (row ≥52px height, whole-row tap target, top ~25% orientation-only, primary path in the bottom ~33% per C-13), and make **the absence of a number as carefully typeset as a number** («—» occupies the amount column at full size — C-11). This report defines the grammar that delivers those outcomes: corner radii, elevation levels, hairline logic, a named spacing scale, an Arabic type scale, row anatomy, density caps, canvas/surface relationships in both themes, one list-vs-card decision rule, one financial-number composition rule, and a header model — each stated as measurable values, because the palette is fixed and only composition may differentiate Micro (C-17).

The constraint set is unusually tight: a fixed 7-role Terracotta palette in which the brand color never carries white text (C-02), a press-only color whose white pairing is a measured ≈4.42:1 and must never be called a pass (C-04), a logo that may not be repeated as decoration (C-07), no Jordanian ornament (C-08), RTL-first Arabic with LTR-isolated ASCII money `20.00 د.أ` (C-09), dates `DD/MM/YYYY` LTR-isolated (C-10), one primary action per screen with the FAB «سجّل» as global recorder (C-14), and twelve anti-patterns that must not return — card walls, component galleries, 6–9-line rows, silent saves, zero standing in for unknown. "Calm but not empty" must therefore be produced as a countable property — N elevation levels, N borders per screen, N rows before the fold — not as adjectives.

---

## 2. Foundations register (fixed inputs)

### 2.1 Fixed palette — roles and measured pairings

| Role (light) | Hex | Allowed use | Measured pairings (computed, this report) |
|---|---|---|---|
| brand | `#cc785c` | atmosphere/surface/graphic rule only; **never white text** (C-02) | white on it 3.28:1 (fail — prohibited anyway); ink `#221c18` on it 5.14:1 (pass) |
| pressed | `#b4613f` | **press-only tint** (C-04) | white on it ≈4.42:1 (authority value; computed here 4.45:1 — either way below the 4.5 AA threshold for normal text; usable only as a transient tint or with large text) |
| brand-text | `#964e33` | high-contrast action background (with white label) and figure/text role, only when hierarchy justifies it (C-03) | white on it 6.11:1 (pass); as text on white 6.11:1 (pass); on soft `#f4e4db` 4.94:1 (pass) |
| soft | `#f4e4db` | quiet fills (selected rows, emphasis zones) | `#964e33` on it 4.94:1 (pass); `#057b7c` on it 4.11:1 (**fail** normal text — large text only) |
| accent | `#079fa0` | surfaces, icons, large figures (≥24px) | white on it 3.24:1 (large text only; never normal-size text) |
| accent-text | `#057b7c` | text/figure role, quiet actions | on white 5.08:1 (pass); on accent-soft `#e3f5f5` 4.51:1 (pass, borderline) |
| accent-soft | `#e3f5f5` | in-flow emphasis fills | fill role |

**Dark set (verbatim, fixed):** `#d59172, #cc785c, #8fd5d6, #332d27, #5ec0c1, #8fd5d6, #332d27`. Working positional mapping (light role → dark value): brand→`#d59172` (on `#332d27` 5.26:1 — **dark brand may carry text and figures, unlike light**), pressed→`#cc785c` (4.15:1 — press tint only), brand-text→`#8fd5d6` (8.19:1), soft→`#332d27`, accent→`#5ec0c1` (6.33:1), accent-text→`#8fd5d6`, accent-soft→`#332d27`. Two consequences follow from this fixed list and are treated as deliberate (C-05): (1) both soft roles converge on `#332d27`, so in dark theme emphasis zones must switch from fills to hairline enclosures or edge marks; (2) the two text roles converge on `#8fd5d6`. Both flagged in OQ-1.

### 2.2 Platform neutrals (proposed — non-brand scaffolding, flagged for confirmation)

| Token | Light | Dark | Measured |
|---|---|---|---|
| canvas | `#faf6f2` (warm near-white) | `#332d27` (from fixed set) | ink on light canvas 15.66:1; ink on dark canvas 11.91:1 |
| surface (sheets) | `#ffffff` | `#3c352e` (proposed) | dark ink on it 10.57:1 |
| ink | `#221c18` | `#f5efe9` | see above |
| ink-2 (secondary) | `#5c5148` | `#c9bdb3` | 7.17:1 / 7.39:1 |
| hairline | `#e5dcd6` | `rgba(213,145,114,0.18)` | decorative, non-text |
| scrim (behind sheets) | `rgba(34,28,24,0.40)` | `rgba(0,0,0,0.55)` | interaction-blocking layer |

### 2.3 Semantic state layer (proposed — functional, non-brand, flagged for contrast + distinctness measurement)

| State | Light text | Dark text | Form (never color alone — matches CorrectionPreview rule) | Measured (white / `#332d27`) |
|---|---|---|---|---|
| success / recorded | `#256b45` | `#7fd0a4` | 16px check outline (2px stroke) + quiet closure sentence | 6.43:1 / 7.42:1 |
| danger / error / loss | `#b3362e` | `#ff9d94` | icon + label; destructive confirm disabled until reason rule passes | 6.03:1 / 6.80:1 |
| warning / attention | `#9a6700` | `#e6b455` | label + road link; on soft fills, large text only (3.93:1 on `#f4e4db` — fail normal) | 4.87:1 / 7.13:1 |
| estimated | — | — | **typographic only**: 1px dotted underline + «تقديري» caption | n/a |
| pending | — | — | hollow chip (1px border, 12px label) | n/a |
| unknown-value | — | — | **typographic only**: «—» in the amount column + road («سجّله», «غير محدد بعد», «غير متاح») | n/a |
| focus | `#057b7c` | `#8fd5d6` | 2px outline + 2px offset | 5.08:1 / 8.19:1 |
| loading / disabled | — | — | spinner in secondary ink / 40% ink, no shadow, no press | exempt (flagged) |

Distinctness flags: `#256b45` vs accent `#079fa0` (both green-family) and `#b3362e` vs brand `#cc785c` (both warm) require a side-by-side distinctness check before the prototype; if either fails, state encoding shifts to the leading marker shape, not a new hue.

### 2.4 Logo → principle translation (no shape transfer; C-07)

The logo file was not present to inspect; the brief describes a calm, trustworthy, fixed mark. Translation is made at **principle level only**:

- **P1 Weight — low stroke contrast.** No UI stroke above 2px except type; hairlines 1px; emphasis rules 2px. Nothing in the UI is heavier than the typography that carries it.
- **P2 Posture — upright, steady baseline.** All containers axis-aligned; motion only along the x/y axes; rotation, skew, and parallax are forbidden everywhere (also the reduced-motion posture, C-18).
- **P3 Proportion — restrained ratios.** Module width:height between 1:1 and 3:1; hero figure size : unit size ratio ≤ 3:1; the amount column is one fixed width (88px) on every screen.
- **P4 Contour continuity — one radius per component.** A component uses exactly one corner radius (sheets: top-only radius, bottom corners 0). Mixed radii on a single edge are forbidden.
- **P5 Quiet detail at small sizes.** Icons ≤24px with ≥2px minimum feature; state markers 12–16px; no gradients, textures, or pattern fills anywhere.

### 2.5 Carried caps and anti-patterns (binding for all three hypotheses)

Home ≤8 top-level blocks before «ما تغير مؤخرًا»; Finance ≤5 body blocks before the first collapsed layer; today list ≤5 rows; recent changes 3 rows; rows ≤3 lines (2 default); text budget on Finance ≤257 words (recovery-verified cap); one primary per screen; FAB «سجّل» is the only global recorder. The 12 lessons (L-01..L-12) are treated as prohibitions: no card walls, no component gallery, no lab controls in the product frame, no 6–9-line rows, no mixed money language, no silent saves, no zero-for-unknown, no notification chrome, no Material/shadcn defaults, no default-wallet/silent-discard behaviors.

---

## 3. Three hypotheses

In all tables, "leading" = right edge (RTL reading start), "trailing" = left edge. Reference viewport 360×640 (top 25% = 160px orientation zone; bottom 33% = 211px thumb zone).

### 3.1 H-A «دفتر هادئ» — The Calm Ledger

**Essence:** the screen is a page of a trustworthy paper ledger — figures lead, hairlines separate, boxes almost never appear; warmth comes from the warm canvas, the terracotta header rule, and typographic craft.

| Rule area | Rule (values) |
|---|---|
| Corner radius | Scale: **0 / 4 / 12**. 0 = all page-level surfaces, ruled grids, dividers; 4 = fields, chips, buttons, FAB; 12 = bottom sheets (top corners only) and dialogs. Nothing else exists. |
| Elevation | **2 levels.** E0 flat: no shadow, separation = 1px hairline. E1 floating (sheets, dialogs, FAB): light `0 -12px 32px rgba(34,28,24,0.18)` + 1px top hairline; dark `0 -12px 32px rgba(0,0,0,0.40)`; scrim per §2.2. |
| Border logic | Hairlines are *the* separator: 1px `#e5dcd6` light / `rgba(213,145,114,0.18)` dark; divider inset 16px on the leading (right) side, bleeding to the trailing edge. Full 1px border boxes only on CorrectionPreview's two lists. Inputs: 1px bottom hairline → 2px `#964e33` on focus. Emphasis rule: 2px `#cc785c` under headers and on attention lines. No border ≥3px anywhere. |
| Spacing scale | 4px base, named: `xs` 4 · `sm` 8 · `md` 12 · `lg` 16 (screen margin) · `xl` 24 (between sections) · `2xl` 32 (major break) · `3xl` 48 (hero breathing). |
| Arabic type scale | Hero figure 34/40 **700** tnum · screen question 20/28 600 · section header 16/24 600 · row body 15/24 400 · row amount 16/24 600 tnum · caption/secondary 13/20 400 · overline 12/16 500 · button 15/20 600. Minimum 12px anywhere; Arabic body line-height ≥1.55; digit-only lines 1.2. One family, weights 400/500/600/700, Arabic-first with tnum-capable digits (font selection is a build decision; acceptance: no synthetic bold, tabular digits, full tashkīl clearance). |
| Row anatomy | Height 56px (min 52, max 64 for 2 lines). Padding 12 vertical / 16 horizontal. Leading (right): subject 15px + caption 13px below (date/status). Trailing (left), from edge inward: action word 13px `#057b7c` (44×44 tap target), 8px gap, then **amount column fixed at 88px, left-aligned, tnum** — decimal alignment across every row. Whole row tappable. |
| Density targets | First paint: Home ≤8 blocks, Finance ≤5, Orders ≤5 sections; 5±2 rows visible; lines/row ≤3 (2 default); ≤1 hero figure per screen; Finance text ≤257 words. |
| Background & canvas | Light: canvas `#faf6f2`, page elements sit directly on canvas (no card fill); `#f4e4db` only as quiet emphasis fill (facts grid, selected row, Tools result bar); sheets `#ffffff`. Dark: canvas `#332d27` = surface color (one color, hairline separation); emphasis zones switch to 1px hairline enclosures (form swap, not color). |
| Grouping rule | **List-with-dividers is the default.** Grouped surface (card) only if ≥2 of: rows share one source record & one tap destination · the group is semantically ONE unit (an order + its items; CorrectionPreview's will-change/won't-change lists) · the group must float (sheet, dialog, capture). Record streams, today lists, events, ledgers: always list. **Card quota ≤1 per screen** (plus sheets). The Home 2×2 facts render as a **ruled grid** (2 vertical + 1 horizontal hairline, 4 cells of 64px) — not 4 cards. |
| Financial-number composition | Amount 16/600 tnum (hero 34/700), ASCII digits, `en-US` grouping, `bdi dir="ltr"`, unit «د.أ» after the number at 12–13px secondary, 4px gap, baseline-aligned, never line-broken. Deltas signed `+`/`−` inside the LTR isolate, 13px, in = `#057b7c` / out = `#964e33` — **on white/canvas only**; on `#f4e4db` fills they must be ≥18.66px bold or switch to ink (measured 4.11:1 fail). Unknown: «—» at the amount's exact position and size + caption road — never 0.00, never italic (Arabic does not italicize). Estimated: 1px dotted underline + «تقديري». Recorded zero renders as a normal `0.00 د.أ`. In RTL sequences, arrows point left «110.00 د.أ ← 145.00 د.أ» (start at right); digits themselves never mirrored. NumericSurface principles encoded: digits stable on state change (tnum, no reflow), context moves while figures settle, position always visible (running balance in receipts), tap alternative (4 quick-amount chips beside the keypad). |
| Header treatment | Typographic header, sticky on Home & Finance only, height 88–96px (inside the 160px orientation zone): overline 12px secondary (screen name · activity), question 20/28, long Arabic date 13px, **2px `#cc785c` rule** across 16px margins, 12px gap below. Transparent over canvas; on scroll, canvas-colored backdrop + 1px bottom hairline. No boxed app bar. |
| Motion implication | **4 primitives:** sheet rise 240ms `cubic-bezier(0.2,0,0,1)`; value settle 150ms fade (digits do not slide); divider emphasis 100ms; success mark draw 200ms. No ripple, no parallax, no count-up. Reduced motion: 100ms crossfade; sheets fade in place. |

### 3.2 H-B «مكتب المالك» — The Owner's Desk

**Essence:** a calm cockpit — one persistent focus figure pinned on top, quiet grouped modules below, elevation speaks only when work is in motion.

| Rule area | Rule (values) |
|---|---|
| Corner radius | Scale: **6 / 10 / 14 / 20**. 6 = chips; 10 = buttons/fields; 14 = modules and FAB (56×56); 20 = bottom sheets. |
| Elevation | **4 levels.** E0 canvas (no shadow). E1 module: `0 1px 3px rgba(34,28,24,0.07)` + 1px border `rgba(34,28,24,0.08)`. E2 half-open sheet: `0 -8px 16px rgba(34,28,24,0.12)`. E3 modal sheet: `0 -16px 40px rgba(34,28,24,0.20)` + scrim 0.44. |
| Border logic | Every module carries a 1px border + E1; dividers inside modules 1px; buttons borderless (filled); chips hollow 1px. No hairline-only page separation — modules are the separator. |
| Spacing scale | 4 · 8 (inner module) · 12 (module gap) · 16 (screen margin) · 20 · 24 · 32. |
| Arabic type scale | Shell figure 28/32 700 tnum · H1 16/24 600 · module title 14/20 600 · row 14/22 400 · row amount 15/22 600 tnum · caption 12/16 · button 14/20 600. Minimum 12px; body line-height ≥1.55. |
| Row anatomy | Height 48px (1 line) / 56px (2 lines, hard cap 2). Padding 8 vertical / 12 horizontal. Leading: subject 14px + status caption. Trailing: amount 15px then 16px chevron at the far edge. |
| Density targets | ≤5 modules before first collapse (matches Finance contract); ≤6 rows per module; lines/row ≤2; Finance text ≤257 words; 1 live figure (the shell). |
| Background & canvas | Light: canvas = solid `#f4e4db` (soft role as ambient desk surface), modules `#ffffff`. Dark: canvas `#2b2620` (proposed neutral, flagged), modules `#332d27`. |
| Grouping rule | **Grouped module is the default** for any titled question-block; plain lists only inside modules or in settings utilities. Decision rule: titled functional block → module; homogeneous record stream → in-module list. Module quota ≤5 per screen (Finance contract). |
| Financial-number composition | Amount 15/600 tnum inline after its label; shell figure 28/700 + unit 12px; deltas as hollow chips (1px border, 12px signed text, in `#057b7c` / out `#964e33` text inside); unknown «—» at figure size inside the module row + road link; unit, digits, isolation rules identical to the binding C-09 set. |
| Header treatment | **Top Focus Shell** (preserved recovery principle): sticky 96–112px on every destination except Tools — overline + question 16/24 + live figure 28/32 + status line 12px; orientation-only (complies with C-13). Module headers 14/20 with row-count caption. |
| Motion implication | **6 primitives:** shell figure count-tween 200ms on change; module collapse/expand 180ms (height + opacity); sheet 260ms; scrim fade 160ms; press = flat tint change 100ms (no ripple); toast settle 180ms. Reduced motion: crossfades only, no count-tween. |

### 3.3 H-C «مسار المال» — The Flow of Money

**Essence:** every amount is a directed movement with a relationship — in / out / held — shown through relationship bars and flow compositions, with motion carrying direction.

| Rule area | Rule (values) |
|---|---|
| Corner radius | Scale: **8 / 16 / 999**. 8 = fields; 16 = cards; 999 (pill) = relationship bars, chips, FAB. Sheets 24. |
| Elevation | **3 levels.** E0 flat zones (no shadow). E1 flow cards: `0 2px 6px rgba(34,28,24,0.08)` + 3px leading-edge color bar (in `#079fa0` / out `#cc785c` / held neutral). E2 sheets: `0 -12px 36px rgba(34,28,24,0.16)` + scrim 0.42. |
| Border logic | Pills outlined 1px; flow bars borderless (fill contrast only); cards 1px hairline + edge bar; no boxed page sections. |
| Spacing scale | 4 · 8 · 12 · 16 · 24 · 32 · 40. |
| Arabic type scale | Flow hero 24/30 700 tnum · H1 18/26 600 · section 15/22 600 · row 14/22 400 · amount pair 16/22 600 tnum · caption 12/16. Minimum 12px; body line-height ≥1.55. |
| Row anatomy | Height 60–72px (bar rows). Padding 12/16. Leading: subject + relation caption («من خالد», «الباقي 2.00 د.أ دَين»). Trailing: amount pair «قبض 8.00 من 10.00». Under the text: **6px relationship bar** full row width inset 16px, filling right→left (RTL reading direction); filled = paid (accent), remaining = outstanding (brand soft/brand), marker dot = held. |
| Density targets | 4±2 rows visible first paint; lines/row ≤3; **≤1 bar per row**; text budget ≤220 words (bars carry part of the meaning); Finance ≤5 blocks. |
| Background & canvas | Light: canvas `#ffffff`; flow zones tinted `#e3f5f5` (in) / `#f4e4db` (out/held). Dark: canvas `#332d27`; because dark soft roles converge (§2.1), flow zones switch from fills to the 3px edge bar on flat `#332d27`. |
| Grouping rule | Default: list rows with relationship bars. Flow cards only for multi-party compositions (CollectionSheet, statement cash line, wallet composition). Card quota ≤3 per screen. |
| Financial-number composition | An amount never stands alone: always amount + relation («+5.00 د.أ من خالد»). Relationship pairs typeset tnum 16/600; unit/`bdi`/unknown rules identical to the binding set; unknown renders as a **dashed empty bar + «—»** at pair size; deltas inherit the in/out palette mapping (in = accent family, out = brand family, held = neutral ink). |
| Header treatment | Composition header 80px: question 18/26 + **flow strip** — three 4px-high mini bars summarizing in/out/held totals for the screen's period. |
| Motion implication | **8 primitives:** bar fill 300ms; direction nudge 120ms (8px translate along x only); number roll 250ms; sheet 260ms; scrim 160ms; flow-draw 350ms on period change; press tint 100ms; success bar completion pulse 200ms. Reduced motion: bars render filled, no nudges, no rolls. |

---

## 4. Comparison table

| Target-feel criterion | H-A Calm Ledger | H-B Owner's Desk | H-C Flow of Money |
|---|---|---|---|
| Calm, not empty | **Strong:** 2 elevation levels, 0 default card borders, 1 hero figure, hairline rhythm; emptiness is paper, not blank | Medium: 4 elevation levels + bordered modules add chrome per screen; persistent 96–112px shell guards against emptiness | Weakest: 8 motion primitives + bars everywhere raise visual energy above "calm" |
| Professional, not cold | **Strong:** accounting-craft cues (tabular column, decimal alignment, ledger rules) read as financial seriousness; warm canvas + terracotta rule keep warmth | Strong: cockpit precision reads professional; `#f4e4db` ambient canvas keeps it warm | Medium: infographic energy reads modern but younger than "financially serious" |
| Operational, not crowded | Strong: decision-first via hierarchy; ≤8 blocks / ≤5 rows enforce it contractually | **Strong:** shell + ≤5 titled modules is explicitly operational; ≤2 lines per row is the strictest cap | Medium: 60–72px bar rows reduce rows per screen; crowding risk inside multi-party compositions |
| Mobile-native | Strong: bottom sheets, sticky headers, OS keypad + quick chips, center-slot FAB, thumb-zone compliance | Strong: same primitives; shell is a header-pattern, native | Medium: bars and flows are web-dashboard vocabulary more than mobile-native |
| RTL-natural | **Strong:** subject-right / amount-left mirrors the Arabic paper دفتر; digits LTR-isolated in a fixed left column — zero conflict between reading and numeric order | Medium: inline label-then-amount ordering re-fragments the numeric column; chevrons need RTL mirroring | Medium: right→left bar fill is RTL-native, but pill rows break column alignment |
| Distinctively Micro (no palette/logo change) | **Strong:** the product's own glossary is ledger vocabulary («دفتر الناس», «كشف», «السجل») — the visual language *is* the product's language; competitor ledger apps (card-dashboard style) look like H-B | Medium: module cockpit resembles dashboard/SaaS patterns (anti-pattern L-01 adjacent); must be actively de-genericized | Medium: relationship bars are differentiating but trend-adjacent (Dribbble risk, L-07) |

---

## 5. Recommendation — **H-A «دفتر هادئ» The Calm Ledger**

**Why A wins, tied to the binding criteria:**

1. **Owner questions are figure-first.** "وين الكاش؟" is answered in the first 88–96px by one 34px hero figure; H-B answers in 96–112px of shell + module chrome; H-C needs 60–72px bar rows to say the same thing.
2. **Thumb-zone ergonomics (C-13).** A's QuickActionSheet puts the 34px amount field, the 48px primary, the OS keypad, and 4 quick-amount chips (NumericSurface tap alternative) all in the bottom 33%; the top 25% stays orientation-only. Nothing in A's grammar places an input above the fold.
3. **Arabic RTL composition.** Subject-right / amount-left with a fixed 88px tnum column mirrors the physical دفتر the owner already trusts; digits stay LTR-isolated (C-09) inside a stable left column, so reading direction and numeric order never fight.
4. **Financial trust.** Trust in a financial product is typographic discipline: one money language, decimal alignment across every row, «—» occupying the exact position where a number would be (C-11), receipts as closure sentences, corrections previewed inside the only bordered box on the screen. A makes all of these *positional* facts, not stylistic ones.
5. **Calm-but-operational.** A is countably calm (2 elevation levels, 1 card quota, 4 motion primitives) and countably operational (decision line first, ≤5-row today list, one 34px figure per screen).
6. **Distinctively Micro without logo or palette change (C-17).** The concept's grammar — ruled grids, hairline rhythm, terracotta header rule, ledger column — is derived from the product's own vocabulary and from the mark's principles (P1–P5), not from a component library.

**What A means concretely for the five representative screens:**

- **Home «مشروعي الآن»:** sticky typographic header 88px (overline «مشروعي الآن · مشغل ليان», question 20px, long date, 2px terracotta rule) → «اليوم» list: ≤5 rows × 56px, hairline dividers, action words («حصّل», «سلّم», «أكمل») as 13px `#057b7c` trailing text buttons → facts as a **ruled 2×2 grid** (4 cells, 64px, hairline cross, `#f4e4db` fill): label 13px + figure 18/600 + qualifier; unknown fact renders «—» + «سجّله (نقرة)» → «ما تغير مؤخرًا» 3 rows + «عرض السجل» → quiet links row → FAB «سجّل» as the center slot of the 64px bottom nav (64×48, radius 4, `#964e33`, white label — 6.11:1 measured). No in-page primary anywhere.
- **Finance «مالي»:** sticky header 96px with the hero figure (الكاش المسجل 34/700 + unit 14px) → decision line: 2px terracotta right-edge marker + truth sentence + the single contextual primary (48px, radius 4, `#964e33`, white label) → unallocated strip as a full-width row with a terracotta attention rule → position 2×2 as the ruled grid → Amanah line: 1px terracotta top rule + dual-truth sentence 13px → collapsed layers as list rows with 12px disclosure. ≤5 blocks before the first layer.
- **Orders «العمل»:** DecisionPanel first as a decision line (marker + «دين مستحق بعد التسليم: 20.00 د.أ» + «حصّل المتبقي أو سجّله دينًا» as a quiet action) → «طلباتي / مبيعاتي / مسودات» as hairline lists; sale rows ≤3 lines with «قبض 8.00 من 10.00» typeset tnum in the amount column and «الباقي 2.00 د.أ دَين على خالد» as caption + action; secondary CTAs («تسجيل بيع مباشر», «إنشاء مسودة أخرى») as quiet links row, never filled buttons.
- **Quick Capture sheet «سجّل»:** sheet radius 12 top-only, E1, scrim 0.40 → menu rows 56px hairline list → in-sheet sale form: amount field 56px with 34/700 tnum digits and 1px→2px `#964e33` focus underline; primary «سجّل البيع» 48px directly beneath; «خيارات أكثر» collapsed behind a hairline; quick-amount chips ×4 → receipt: 200ms success mark + closure sentence 15px («سُجّل بيع 20.00 د.أ — الكاش صار 165.00 د.أ») + «تراجع» (quiet, routes to documented correction) + «تم» (the one filled button).
- **Financial Truth composition (كشف الأسبوع / StatementView):** six plain lines max, each = label 15px right + figure 18/600 tnum left in the 88px column + honesty qualifier («مسجل», «تقديري») 12px; unknown lines «—» + «غير متاح»; cash line as an RTL sequence «110.00 د.أ ← 145.00 د.أ» (left-pointing arrow, LTR-isolated figures); period switcher ◀ ▶ as 44px text targets; every line tappable to its source.

---

## 6. The two rejected directions as compact previews

Both survive as **static single-frame comparisons** in the review artifact (a "directions" tab, controls strictly outside the phone frame per C-20):

- **H-B preview — one 390×844 Finance frame:** Top Focus Shell (96px, live figure 28px) + 3 white modules on `#f4e4db` canvas (decision module, position 2×2 module, layers module) + 6 rows. Six rule bullets (radius 6/10/14/20; 4 elevation levels; ≤5 modules; 48px rows; inline numbers; shell motion 200ms). Three contrast bullets vs A: persistent shell vs typographic header; module borders vs hairlines; inline amounts vs ledger column.
- **H-C preview — one 390×844 Finance frame:** composition header + flow strip + 2 flow cards (3px edge bars) + 4 relationship-bar rows (6px bars filling right→left). Six rule bullets + three contrast bullets vs A (bars vs tnum column; 8 motion primitives vs 4; 60–72px rows vs 56px). Rendered in reduced-motion state (bars static, filled).

Budget per preview: one frame, ≤3 surfaces, ≤10 rows, zero interactivity — enough for a reviewer to compare directions without rebuilding either system.

---

## 7. Open questions for the orchestrator (max 5)

1. **Dark role mapping confirmation (OQ):** the fixed dark list maps both text roles to `#8fd5d6` and both soft roles to `#332d27` (positional reading, §2.1). Confirm the intended mapping — it changes dark-theme text-color and fill rules materially.
2. **Neutrals approval:** the canvas/ink/hairline/scrim values in §2.2 are platform scaffolding, not brand palette. Confirm or replace with approved neutrals before the prototype build.
3. **Semantic layer measurement:** success `#256b45` / danger `#b3362e` / warning `#9a6700` (+ dark counterparts) need tool-verified contrast and a side-by-side distinctness check vs accent teal and terracotta; fallback is shape-encoded state, not new hues.
4. **FAB form factor:** A's center-slot FAB is a 64×48 radius-4 rectangle with a text label — deliberately un-generic. Confirm this trade with the interaction/motion sub-agents (Task 2-c/2-d) before it is frozen.
5. **Sticky header scope:** A keeps the 88–96px sticky header on Home and Finance only (scroll-ownership budget). Confirm whether Orders and StatementView also need stickiness, or accept static 72px headers there.

---

*End of report. All values in this document are proposals grounded in the fixed constraint registers; none overrides a fixed palette value, the logo rule, or a binding content rule. Contrast values are computed per WCAG 2.x and flagged for tool verification.*
