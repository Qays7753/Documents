# 04 — Arabic RTL, Accessibility, Data Visualization & Trust Recommendations

**Delivery:** `micro-visual-product-concept-002`
**Task ID:** 2-d · **Agent:** Sub-agent 4 — Arabic RTL, Accessibility, Data Visualization & Trust Specialist
**Date:** 2026-09-06
**Inputs:** worklog brief (2-0), `00-SOURCE-INTAKE-REPORT.md` (C-01…C-20), `01-current-work-lessons.md`, `Micro-Target-State-Design-Report.md` §4.0/§4.1/§4.4/§4.12 (N2), Phase 2 scenarios (owner vocabulary, deposit semantics).
**Honesty note:** all contrast figures below are computed with the WCAG 2.x relative-luminance formula (arithmetic shown); bidi and chart recommendations are professional-knowledge-based analysis, labeled as such; no live web research was used; no absent source file is quoted.

---

## 1. Arabic RTL Composition (A)

### 1.1 Typography, line-height, and the no-uppercase constraint

Arabic composes differently from Latin in four ways that change layout decisions:

1. **Letter joining (shaping).** Arabic letters connect within a word; truncation mid-word breaks cursive shaping and produces a mangled glyph string, not a shortened word. Any truncation must therefore happen at **word boundaries only** — never a fixed character count.
2. **Word length distribution.** Arabic equivalents run ~15–25% longer than English (e.g., "Settings" → «الإعدادات», 9→10 glyphs but wider joined forms; "Record a sale" → «سجّل بيعًا»). Buttons, chips, nav labels, and empty-state sentences must be designed at **Arabic lengths**, with English strings treated as the short variant, not the baseline.
3. **No uppercase.** Arabic has no case, so the Latin trick of small-caps overlines for hierarchy is unavailable and must not be simulated by letterspaced Latin caps inside Arabic surfaces. Hierarchy comes from **weight (600/700), size steps, and ink color** — this is also why the fixed palette's text roles matter more here than in an LTR system.
4. **Diacritics.** UI copy rarely carries tashkeel, but two owned words do: the badge «مُقدَّر» (estimated) and «مُستحق» forms. Stacked marks (shadda/damma) extend above the x-height; tight line-height or badge padding clips them.

**Line-height minimums (binding recommendation):**

| Surface | Arabic line-height | Reason |
|---|---|---|
| Body / paragraph / empty-state sentences | **1.6 minimum (1.65 recommended)** | Arabic ascender–descender spread + diacritic headroom |
| List row secondary lines | 1.5 minimum | single-line rows may go 1.4 only if the row's fixed height supplies optical space |
| Headings / overlines | 1.35–1.45 | avoid clipping tails of ج، خ، س، ص |
| NumericSurface (hero digits) | 1.1–1.2 with `tabular-nums` | stable digits (see S-7 principles carried by S-1) |
| Buttons | 48px min height, label 1.4 | two-line Arabic labels at 320px must not clip |

Minimum Arabic body size: **15px** (Arabic joined forms degrade faster than Latin below this); caption floor 13px and only with the near-black inks of §2.2.

### 1.2 Truncation policy — never on money

| Content | Ellipsis allowed? | Rule |
|---|---|---|
| Money, dates, deltas | **NEVER — under any width** | A truncated number is a different number: `12,450.750…` reads as a fabricated amount. If it does not fit, the layout is wrong — reduce elsewhere, wrap the money+unit pair to its own line, or move it to the NumericSurface. Money + unit wrap as ONE unit: number island is `white-space: nowrap` and the unit never separates from it. |
| Party / business names in rows | No ellipsis; **2-line clamp** then fade | full name always in the accessible name and on the detail screen |
| Secondary/helper text, long descriptions | Yes — word boundary only | `text-overflow: ellipsis` on whole-word truncation, never mid-word (shaping) |
| Primary action labels | **NEVER** | at 320px the button wraps to 2 lines and grows; if a label needs a 3rd line, the label is rewritten, not shrunk |
| State words («مسجل»، «غير متاح»، «متأخر») | Never | states are trust signals; truncating them deletes the truth |

### 1.3 Alignment and logical properties

Arabic body text is **right-aligned and top-anchored** (`text-align: start`). All layout CSS must use **logical properties** — `margin-inline-start`, `padding-inline-end`, `border-inline-start`, `inset-inline-start` — never physical `left/right`, so the English LTR verification view (C-20) is a direction flip, not a re-authoring. Row leading glyph/dot sits at inline-start; trailing amount sits at inline-end. Root contract: `dir="rtl" lang="ar"` on the app shell; the LTR toggle sets `dir="ltr" lang="en"` on the same tree.

### 1.4 Bidi markup contract

**Core decision — unit OUTSIDE the LTR isolation.** Isolate exactly what bidi can break — the numeric string (digits, `en-US` grouping separators, decimal point, sign) — inside `<bdi dir="ltr">`, and let the unit «د.أ» flow in the Arabic run.

**Justification (professional-knowledge-based bidi analysis):** in an RTL paragraph, a later-reading element renders further **left**; the unit must come *after* the number in reading order («عشرون دينارًا», the grammatical order and the source's logical contract `20.00 د.أ`), so the unit must sit in the RTL flow to the left of the digit island. If the unit is placed *inside* `dir="ltr"` (e.g. `<bdi dir="ltr">20.00 د.أ</bdi>`), the isolate lays out internally LTR and the unit lands on the isolate's right edge — which is the edge an RTL reader meets **first**: the string then reads «د.أ 20.00», unit *before* number, inverting the binding rule "unit after the number". The unit-outside contract is also direction-symmetric: in the EN LTR view the same markup renders `20.00 د.أ` with unit to the right — reading order number→unit holds in **both** directions. Isolation of the number alone still buys everything isolation is for: grouping separators, the decimal point, and the leading `+`/`−` sign are protected from neutrals resolving to the RTL base (the classic sign-detachment and range-reversal bugs).

| Content | Markup contract | Notes |
|---|---|---|
| Plain money | `<span class="money"><bdi dir="ltr">20.00</bdi> <span class="u">د.أ</span></span>` | the outer span is the nowrap wrap-unit; visible reading order «20.00 د.أ» in both directions; never «دينار» in the same surface (C-09) |
| Signed delta | `<bdi dir="ltr">+5.00</bdi> د.أ` / `<bdi dir="ltr">−5.00</bdi> د.أ` — use one minus codepoint (U+2212, as in the target-state doc) | the sign MUST be inside the isolate or it detaches to the wrong end |
| Large value | `<bdi dir="ltr">12,450.750</bdi> د.أ` | comma/period between digits are part of the EN run — safe inside |
| Date | `<bdi dir="ltr">12/09/2026</bdi>` | DD/MM/YYYY (C-10); Arabic long date in headers stays pure Arabic |
| Date range | `<bdi dir="ltr">06/09/2026</bdi> إلى <bdi dir="ltr">12/09/2026</bdi>` | the Arabic word between two isolates is safe; a bare hyphen range `06/09–12/09` would visually reverse — forbidden unless itself isolated |
| Parenthesized LTR content | `<bdi dir="ltr">(85.00)</bdi>` | parentheses belong INSIDE the isolate with their content; auto-mirroring of parens in RTL otherwise splits the pair. Better: avoid parentheses around money entirely (the target wireframes use dashes/commas) |
| Mixed Arabic/Latin party names | bare `<bdi>مكتب العبدلي Ltd</bdi>` (no dir — first-strong auto-isolation) | protects Latin runs at line edges; never rely on the paragraph's base direction |
| Trailing sentence period | `… د.أ.` — period resolves to the RTL base and lands leftmost, correctly *after* the unit in reading order | no isolation needed for the period |

### 1.5 Numerals decision

| Decision | Value | Rationale |
|---|---|---|
| **Primary (money, dates, counts)** | **ASCII digits `0-9`** | (1) Binding rule C-09 already fixes ASCII — this is compliance plus rationale, not a new choice. (2) Financial readability: receipts, bank SMS, POS displays, and invoice paper in Jordan present ASCII digits; display matching paper removes a transcription layer. (3) Input = display: numeric keypads emit ASCII; if display were ٠١٢٣ the owner would mentally convert every typed number — an error surface where errors cost money. (4) `en-US` grouping (`1,245.50`) only composes reliably on the ASCII run. |
| Arabic-Indic ٠١٢٣ | **Not used on any numeric surface in v1** | the only permitted Arabic numeral form is **words** in long header dates («12 أيلول 2026» — spelled month, ASCII digits), per C-10; no surface mixes the two systems |
| Font discipline | choose an Arabic typeface whose default digit set is ASCII, or pin digits to the Latin subset | many Arabic-first fonts contextually swap `0→٠`; this must be locked at the type level, not hoped for |

### 1.6 English LTR verification checklist (for the C-20 toggle)

| Element | Mirrors to LTR? |
|---|---|
| Chevrons / list disclosure arrows | **YES** — point start→end (right in LTR, left in RTL) |
| Back arrows | **YES** — point outward from content (left in LTR, right in RTL) |
| Progress direction (stepper fill, progress bars, onboarding) | **YES** — fills start→end |
| Chart time axis and bar growth | **YES** — full mirror (see §3) |
| Edge-swipe / sheet peek / dismiss gestures | **YES** — back-swipe from the leading edge |
| Slider fill, tab underline position | **YES** — follow inline-start |
| FAB «سجّل» | **NO** — bottom-center per S-2 §4.3; position is symmetric, nothing to mirror |
| Numbers, money islands, dates | **NEVER** — always internally LTR; only their position in the row moves |
| Logo | **NEVER** — fixed artwork (C-07) |
| Direction-neutral icons (check, plus, gear, magnifier, spinner rotation) | NO — no directional semantics |
| Spinners / loading rotation | NO |

### 1.7 Long-content test matrix (the concept must pass all rows at 320px)

| Test case | Expected behavior |
|---|---|
| Long Arabic business name «مؤسسة الوردة البيضاء لصناعة الحلويات والمعجنات» | 2-line clamp + fade; full name in accessible name; no mid-word break |
| Long button label «سجّل قبضًا أو دفعًا متوقعًا» at 320px | wraps to 2 lines, button grows to 48px+; never ellipsis, never below 15px |
| Large value `12,450.750 د.أ` | one nowrap unit, tabular digits, no truncation, unit never orphaned |
| True zero `0.00 د.أ` | full-weight number only where a real zero balance exists (e.g. «عليّ للموردين 0.00 د.أ») |
| Missing | «—» lighter weight + road («سجّله») — C-11 |
| Unknown | «غير محدد بعد» (wallet opening: «رصيد الافتتاح غير محدد بعد — سجّله») — never 0.00 |
| Estimated | full number + «مُقدَّر» badge (dashed-outline) + bounded-gap sentence «تقديري — تكلفة بيعين غير معروفة» |
| Mixed name «مكتب العبدلي وشركاه Ltd» | bare `<bdi>` isolation; renders correctly at row start or end |
| Delta `+12.00 د.أ` / `−10.00 د.أ` | sign inside island; never detached |
| Week header «كشف الأسبوع — 06/09/2026 إلى 12/09/2026» | two isolated dates with the Arabic «إلى» between |

---

## 2. Accessibility (B)

### 2.1 Touch targets

- **Minimum 44×44px** (WCAG 2.5.5; the 2.5.8 AA floor of 24px is not the ambition); **48px recommended** for all primary controls, list-row actions, and keypad keys (the QuickActionSheet fast path is a money surface — accuracy is trust).
- Full-row list rows are single targets, 56–64px tall; secondary text inside the row is not a separate target.
- **≥8px separation** between adjacent targets (mis-tap protection; see OQ-4 for the 320px two-action row case).
- Visual size may be smaller than hit size: transparent padding brings a quiet text link («سجّله», «عرض السجل») to 44px without visual inflation.
- FAB 56px, bottom-center, always visible (S-2 §4.1).

### 2.2 Contrast calculations (arithmetic shown)

Formula: for each channel `c = c/255`; linear `c' = c/12.92` if `c ≤ 0.03928` else `((c+0.055)/1.055)^2.4`; luminance `L = 0.2126·R' + 0.7152·G' + 0.0722·B'`; ratio `= (L₁+0.05)/(L₂+0.05)` with L₁ the lighter. AA thresholds: **4.5:1 normal text, 3:1 large text (≥18.66px bold / 24px) and non-text UI**.

**Worked example — #964e33 on #ffffff:** R=150→`((150/255+0.055)/1.055)^2.4 = 0.30499`; G=78→`0.07619`; B=51→`0.03310`. `L = 0.2126×0.30499 + 0.7152×0.07619 + 0.0722×0.03310 = 0.12172`. White `L=1.0`. Ratio `= (1.0+0.05)/(0.12172+0.05) = 1.05/0.17172 = 6.11:1` → **PASS AA normal** (fails AAA normal at 7:1; passes AAA large).

| Pair (fg on bg) | Linearized R'·G'·B' (fg / bg) | L fg / L bg | Ratio | Verdict at AA |
|---|---|---|---|---|
| **#964e33 on #ffffff** | 0.30499·0.07619·0.03310 / 1·1·1 | 0.12172 / 1.0 | **6.11** | **PASS** normal; also 3:1 large/UI |
| **#ffffff on #964e33** | (symmetric) | 1.0 / 0.12172 | **6.11** | **PASS** — #964e33 is the only terracotta that fully passes with a white label; eligible for the high-contrast action role per C-03 |
| **#057b7c on #ffffff** | 0.00152·0.19807·0.20156 | 0.15653 | **5.08** | **PASS** normal — accent-TEXT role |
| **#964e33 on #f4e4db** | 0.12172 / 0.90466·0.77582·0.70838=0.79834 | — | (0.84834)/(0.17172) = **4.94** | **PASS** normal, margin 0.44 — usable, prefer ≥16px on soft surfaces |
| **#d59172 on #1c1815** | 0.66539·0.28315·0.16827=0.35612 / 0.01161·0.00913·0.00750=0.00954 | — | (0.40612)/(0.05954) = **6.82** | **PASS** normal — dark warm emphasis |
| **#8fd5d6 on #332d27** | 0.27468·0.66539·0.67244=0.58283 / 0.03310·0.02624·0.02029=0.02727 | — | (0.63283)/(0.07727) = **8.19** | **PASS** normal — dark accent-text |
| #b4613f + #ffffff | 0.45641·0.11954·0.04971=0.18612 | — | 1.05/0.23612 = **4.45 computed** (audit authority: ≈4.42) | **FAIL** AA normal → **press-only** (C-04); never describe as a full pass; passes 3:1 large only |
| #cc785c + #ffffff | 0.60383·0.18782·0.10702=0.27043 | — | 1.05/0.32043 = **3.28** | **FAIL** normal — computed confirmation of the C-02 prohibition; light #cc785c stays atmosphere/surface |
| #079fa0 on #ffffff | 0.00212·0.34670·0.35153=0.27380 | — | 1.05/0.32380 = **3.24** | FAIL normal; **PASS 3:1** → graphics/large text only (chart bars, icons, rules) |
| #332d27 on #ffffff (light ink) | 0.02727 | — | 1.05/0.07727 = **13.59** | PASS (AA + AAA normal) |
| #f4e4db on #332d27 (dark body ink) | 0.79834 | — | 0.84834/0.07727 = **10.98** | PASS |
| #f4e4db on #1c1815 | 0.79834 / 0.00954 | — | 0.84834/0.05954 = **14.25** | PASS |
| #8fd5d6 on #1c1815 | 0.58283 | — | 0.63283/0.05954 = **10.63** | PASS |
| #d59172 on #332d27 | 0.35612 | — | 0.40612/0.07727 = **5.26** | PASS |
| #5ec0c1 on #332d27 | 0.43929 | — | 0.48929/0.07727 = **6.33** | PASS — dark accent graphics |
| #cc785c on #1c1815 | 0.27043 | — | 0.32043/0.05954 = **5.38** | PASS — #cc785c may carry secondary text on the dark canvas (deliberate mapping, C-05) |
| #057b7c on #f4e4db | 0.15653 | — | 0.84834/0.20653 = **4.11** | FAIL normal; PASS large only |
| #057b7c on #e3f5f5 | 0.15653 / 0.88228 | — | 0.93228/0.20653 = **4.51** | razor pass (margin 0.01) — restrict to large/bold; small text on accent-soft should use #964e33 (5.43) |

**Recommended role assignments (all fixed tokens, roles only):**
- **Light theme:** canvas #ffffff; ink/body = **#332d27** (13.59 on white; 10.98 on #f4e4db) — the dark token re-roled as light ink; emphasis/secondary text = **#964e33** (6.11 / 4.94); accent-text/links = **#057b7c** (5.08, on #e3f5f5 only large); accent #079fa0 = graphics & large text only (3.24 ≥ 3:1 non-text); #964e33 may take the high-contrast action bg with a white label (6.11) when hierarchy justifies (C-03); #b4613f strictly press (C-04); #cc785c atmosphere only (C-02).
- **Dark theme:** canvas **#1c1815** (recommended near-black warm neutral — a canvas role, not a brand-color replacement; all-fixed-token fallback: canvas #332d27, inks still pass), elevated surface **#332d27**; body ink **#f4e4db** (10.98–14.25); warm emphasis **#d59172** (5.26–6.82); accent-text **#8fd5d6** (8.19–10.63); accent graphics **#5ec0c1** (6.33). Never text on a #cc785c dark surface (#d59172 on #cc785c = 1.27).
- **Non-text UI** (focus rings, bar outlines, input borders) must clear 3:1 against adjacent colors — #964e33 (6.11) and #057b7c (5.08) work everywhere on light; #8fd5d6/#5ec0c1 on dark.

### 2.3 Non-color state cues and the status-glyph table

Every status = **glyph shape + text label**; color is tertiary (C-06, and N3's "never color-alone"). Dot grammar: filled = happened/complete; hollow = expected/not-yet; dashed = estimated; ring = attention; slash = unavailable; split = conflict; em-dash = unknown.

| State | Glyph shape | Label (AR / EN) | When color alone fails |
|---|---|---|---|
| Paid / complete | filled dot + check | «مدفوع» / «مكتمل» — paid / complete | teal-vs-brown confusion under color-vision deficiency; grayscale print; bright sun |
| Outstanding / due | hollow (outline) dot | «مستحق» / outstanding | hollow vs filled reads even in monochrome |
| Pending / expected | dashed-outline dot | «متوقع» / expected | dashed = not-yet-real; no color needed |
| Estimated | dashed-fill dot + badge | «تقديري» / «مُقدَّر» badge — estimated | estimate must never look identical to a fact |
| Unknown | hollow circle containing an em-dash | «غير محدد بعد» / not set yet | dash ≠ 0: shape encodes "no value" |
| Offline | cloud with slash | «غير متصل» / offline | slash icon + label survive any palette |
| Syncing | two circular arrows (animated, off under reduced motion) | «جارٍ المزامنة…» / syncing | motion-independent label |
| Synced | double check | «متزامن» / synced | distinguishes "saved locally" from "synced" without hue |
| Conflict | split/two-tone dot (or diamond) | «تعارض» / conflict — «نسختان من هذا السجل» | the one state that must never be mistakable for synced; shape carries it |
| Overdue | attention ring around hollow dot | «متأخر» / overdue | ring = urgency that reads without red |

### 2.4 Accessible names

- **List rows:** the row's accessible name concatenates its data: `[type]: [party], [amount], [state], [date]` — e.g. «تحصيل مستحق: خالد، 20.00 د.أ، مستحق منذ 11/09/2026». Visible text is the base of the name (WCAG label-in-name); never silently substitute «دينار» for «د.أ» in the name — wording consistency is binding (SR pronunciation is OQ-1).
- **Row action buttons** carry their own full names: «حصّل 20.00 د.أ من خالد».
- **Charts:** `role="img"` with `aria-label` = the interpretation sentence verbatim; the visible interpretation line IS the non-visual alternative (§3) — no parallel hidden DOM.
- **NumericSurface:** one labeled group: «[question]: [value] [unit], [state]» — «الكاش المسجل الآن: 145.00 د.أ، مسجل». The stable-digits contract means the announced value does not re-read on non-semantic re-renders.
- **Position triad** («الوضع المسجل»): one labeled group announced as a single reading — «الوضع المسجل: المتاح 145.00 د.أ، لي عند العملاء 20.00 د.أ، عليّ للموردين 0.00 د.أ» — because the triad is one semantic fact; individual values then become focusable within the group.

### 2.5 Live regions and screen-reader financial truth

- Money mutations (save receipts, collection, corrections): **polite** — the quiet closure sentence («سُجّل بيع 20.00 د.أ — الكاش صار 165.00 د.أ») announced once, never stacked.
- Background sync status: **polite**, low frequency; syncing chatter is suppressed unless a write is in flight.
- Blocking errors that stop a money write (validation, idempotency conflict): **assertive once**; conflicts: assertive once, then downgrade — never repeated assertive announcements (assertive spam is the trust-destroying pattern).
- Loading states: `aria-busy`, never announced as error.

---

## 3. Data Visualization (C)

### 3.1 Universal chart contract (all charts, no exceptions)

Every chart states: **(1) period** (isolated dates, e.g. «06/09/2026 إلى 12/09/2026»), **(2) unit** «د.أ» in the chart header, **(3) source state** («مسجل» / «محلي — لم يُزامن» / «جزئي»), **(4) a text interpretation line** that answers the owner question in words, **(5) a non-visual alternative — the text IS the alternative** (role="img" + the same sentence). **RTL direction: time flows right-to-left** — earliest at the inline-start (right) edge, latest at the left; bars and fills grow from inline-start. Justification: Arabic readers scan from the right; a left-flowing chart forces reversed reading load against the bidi base of the whole screen; localizing the axis keeps the chart inside the same reading rhythm as its Arabic interpretation line; the EN LTR toggle mirrors the chart with the same data. Every chart maps to an action or a decision ("who to collect from") — a chart that answers nothing is decoration (rejected).

### 3.2 Chart 1 — «كيف تحرّك أسبوعي؟» Cash in vs out per day

| Contract | Value |
|---|---|
| Owner question | «How did this week move?» — cash in vs cash out, per day |
| Form | **Small paired bar columns** — 7 day-columns, each two thin bars (in / out) from a shared baseline |
| Why this form (mobile+RTL) | two flows of one metric side-by-side at 320px: ~40px per column pair; paired bars compare in/out per day without a legend hunt; a **diverging bar is rejected** because in/out are two flows, not positive/negative of one measure — diverging also wastes the center and its "negative" side visually flips in RTL |
| Colors (graphics, ≥3:1) | in = #079fa0 (3.24 on white; dark: #5ec0c1, 6.33); out = #964e33 (6.11); labels «قبض»/«صرف» as a two-word legend, plus distinct heights — not color alone |
| Period & unit labeling | header «الأسبوع: 06/09/2026 إلى 12/09/2026 · د.أ»; short Arabic weekday labels under columns; values labeled only at totals and the peak day (clutter cap) |
| Source state | chip «مسجل» or «محلي — لم يُزامن» beside the header |
| Missing / incomplete data | a day with **no records renders a gap + footnote** «أيام بلا تسجيل: …» — unrecorded ≠ zero; only a day explicitly closed at zero may show zero-height bars |
| RTL direction | columns run right→left (6th at right, 12th at left); EN toggle mirrors |
| Text interpretation (example) | «هذا الأسبوع: قبضت 85.00 د.أ وصرفت 22.50 د.أ — أعلى يوم قبض كان الخميس 40.00 د.أ.» |

### 3.3 Chart 2 — «مين علينا؟ ومَن مدين لي؟» Receivables aging

| Contract | Value |
|---|---|
| Owner question | «Who owes me, and how old is it?» |
| Form | **Non-chart first: a person list**, oldest-first, each row carrying an optional inline **segment bar** (length = amount; solid = current, diagonal-hatch = overdue) |
| Why | aging is a *per-person decision*; with the scenario-realistic N of 1–5 debtors, a standalone chart hides the name — the exact thing the owner acts on; the micro-bar inside the row preserves magnitude comparison without demanding chart literacy; sorting encodes age, which no bar encodes honestly |
| Period & unit labeling | per-row «مستحق منذ 11/09/2026» + amount «20.00 د.أ»; group header total «لي عند العملاء 20.00 د.أ · د.أ» |
| Source state | row-level «مسجل»; unknown age → «تاريخ الاستحقاق غير محدد بعد» (never a fake age) |
| Missing data | unknown due-date rows sort last under «غير محدد بعد», with a road to set the date |
| RTL direction | rows scan top-down; segment bars grow from inline-start (right); hatch pattern distinguishes overdue without color |
| Text interpretation (example) | «لي عند العملاء 20.00 د.أ: دين واحد على خالد — متأخر منذ يوم واحد.» |

### 3.4 Chart 3 — «قد إيش هالطلب مدفوع؟» Order payment relationship bar

| Contract | Value |
|---|---|
| Owner question | «How much of this order is paid?» |
| Form | **One horizontal relationship bar** = the full order value; segments: collected (solid) / outstanding (dashed-outline); the collected segment carries a **hatched bracket zone labeled «عربون محفوظ»** when the order is unfinished |
| Why | a part-of-total question is exactly a track; one line survives 320px and reads linearly in RTL; segments with pattern + amount labels need no legend |
| Period & unit | «طلب صندوق خشبي · 35.00 د.أ إجمالي»; segment ends labeled «محصّل 15.00 د.أ» / «متبقٍ 20.00 د.أ» |
| Source state | the record's state on the row («مسجل») |
| Missing data | unknown agreed price → no bar: «السعر غير محدد بعد» + road (never a fabricated total) |
| RTL direction | fill grows from inline-start (right); deposit bracket sits inside the collected segment from the start edge |
| Text interpretation (example) | «طلب صندوق خشبي 35.00 د.أ: محصّل 15.00 (منها عربون محفوظ 15.00)، متبقٍ 20.00 د.أ.» Caption below (§4.3). |

### 3.5 Chart 4 — «ممّ يتكوّن المتاح عندي؟» Wallet composition

| Contract | Value |
|---|---|
| Owner question | «What makes up my available money?» |
| Form | **Segmented row** (single-line stacked bar, 24–28px tall): free / earmarked («مخصّص») / amanah / unallocated; labels below segments (value + word), never inside |
| Why | one number's parts = one track; stacked columns waste height; a pie is rejected (4 slices, angles unreadable at small size, no RTL benefit); the segmented row keeps the composition inside the Finance reading rhythm |
| Patterns | amanah segment = diagonal hatch (real cash, not yours); unallocated = dotted; free = solid; unknown opening → **the whole row is not rendered** («رصيد الافتتاح غير محدد بعد — سجّله») because composition of an unknown base is fiction |
| Period & unit | «الكاش المسجل الآن · د.أ»; segment labels «حر 135.00 د.أ» etc.; segments under ~8% width list as a footnote row instead of inline labels |
| Source state | «مسجل» chip |
| RTL direction | segments run from inline-start (right) in priority order: free → earmarked → amanah → unallocated |
| Text interpretation (example) | «الكاش المسجل 145.00 د.أ: 135.00 حرة الاستخدام + 10.00 أمانات — الأمانات كاش في الدرج، ليست لك ولا ربحًا.» |

### 3.6 Rejected forms (binding)

Decorative 3D (distortion + depth noise on a trust surface); **pie charts > 3 slices**; **truncated bar axes** — a bar starting above zero fabricates magnitude, fatal for an owner who spot-checks; **sparklines without context** (no period/unit/interpretation = decoration); **any chart without a text summary or action** — the text is the truth surface, the chart is its shape.

---

## 4. Trust & Honesty Surface Patterns (D)

### 4.1 Offline / sync truth

**Never block writes** (local-first). The offline/sync line is a **quiet truth line**, never a modal, never a banner across content:

| State | Wording (AR) | Placement | Behavior |
|---|---|---|---|
| Offline | «شغال بدون إنترنت — بياناتك محفوظة على هذا الجهاز» | one row under the header truth area (S-2 §4.1 slot ②) | writes queue locally; FAB and all recorders stay enabled |
| Stale export | «آخر نسخة مصدّرة 12/09/2026» + link «الإعدادات» | same truth slot, with the isolated date | guilt-free; the away card carries the nudge, not this line |
| Saving | «جارٍ الحفظ…» | in-sheet, above the primary button | polite live region |
| Syncing | «جارٍ المزامنة…» + circular-arrows glyph | low-emphasis end of the truth slot | motion off under reduced motion |
| Synced | double-check glyph + «متزامن» | quiet, same slot | never a toast for routine success |
| Conflict | «تعارض — نسختان من هذا السجل. راجع قبل المتابعة.» | on the affected record row + assertive announcement once | opens a compare view; the product never auto-picks a winner |
| Local-only record | «محفوظ محليًا — لم يُزامن بعد» | source-state chip on the record | the record is still true, still counted, labeled |

### 4.2 Unknown vs zero distinction table

| Financial condition | Mark | Typographic weight | Road / link | Example |
|---|---|---|---|---|
| True zero (balance really is zero) | `0.00 د.أ` | full weight, normal ink | none needed | «عليّ للموردين 0.00 د.أ» |
| Unknown (never recorded) | «—» | lighter weight | «سجّله» | «مال المالك المسجل — سجّله» |
| Unknown opening balance | «رصيد الافتتاح غير محدد بعد» | lighter, sentence | «سجّل رصيدًا موثقًا» | WalletLedger |
| Unavailable (cannot compute honestly) | «غير متاح» | lighter + reason | explains what's missing | profit with unknown cost |
| Estimated | full number + «مُقدَّر» badge | full weight + dashed badge | bounded-gap sentence | «27.50 د.أ (تقديري — تكلفة بيعين غير معروفة)» |
| Unrecorded day (charts) | gap, not a zero bar | — | footnote «أيام بلا تسجيل» | weekly chart |

### 4.3 The deposit-honesty visual («عربون محفوظ»)

The relationship bar (§3.4) + its caption are the deposit truth surface:

- The deposit amount renders as a **hatched bracket zone inside the collected segment**, labeled «عربون محفوظ 15.00 د.أ» — pattern + words, never the label «مدفوع» before completion.
- Caption (always present when a retained deposit exists): «العربون كاش حقيقي في الدرج، مرتبط بطلب غير منجَز — يُطبَّق مرة واحدة عند الإكمال، وليس ربحًا بعد.»
- At completion, the bracket dissolves into the solid paid segment and the caption changes to explain the conversion — the owner *sees* the state change rather than inferring it.
- Double-count guard: the bar's track is the order total only; the deposit never adds a segment beside the total («sales + deposit» is the forbidden arithmetic — Phase 2 §6).
- Sibling rule for amanah in composition (§3.5): hatch + the dual-truth sentence «كاش حقيقي في الدرج لكنه ليس لك ولا يدخل الربح».

---

## 5. Open questions (max 6)

1. **SR pronunciation of «د.أ»** under VoiceOver/TalkBack Arabic: if the abbreviation is unreadable, decide an alias strategy that does not break the visible-wording consistency rule (2.5.3 label-in-name).
2. **Ink/canvas token confirmation:** #332d27 as light-theme ink and #1c1815 as dark canvas are role assignments/a neutral addition — needs central-agent confirmation, or accept the all-fixed-token fallback (dark canvas #332d27, all recommended inks still pass).
3. **RTL time-flow validation:** the right-to-left chart direction is the recommendation; Arabic usability testing should confirm against owners habituated to LTR bank-statement charts.
4. **Two inline row actions at 320px:** 44px + 8px + 44px ≈ 96px inside a 288px content row crowds Arabic labels — confirm one action per row («حصّل») with details behind the row tap.
5. **Arabic-Indic digits:** confirm no owner segment reads ASCII money materially slower (Phase-2 field validation list) before locking the numerals decision permanently.
6. **Export-staleness threshold** for showing «آخر نسخة مصدّرة…» is not defined in the sources; needs a product rule (aligned with the 7-day away-card trigger).

*End of report — Task 2-d.*
