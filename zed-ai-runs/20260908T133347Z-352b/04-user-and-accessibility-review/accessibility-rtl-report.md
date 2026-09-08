# Accessibility & RTL Report — Agent 04 (Computed Audit + Rules)

Run: `20260908T133347Z-352b` · Task `2-d` · WCAG 2.2 AA baseline · Arabic-first RTL · light-mode only.

This report is the computed accessibility basis for the final library. Every contrast ratio below was calculated from the exact token hex values with the WCAG 2.x relative-luminance formula — no ratio in this document is estimated or taken from a tool screenshot. Where a pair fails, the pairing rule that follows tells the builder exactly which token to use instead, so the failure never reaches a real screen. The RTL/bidi section gives per-string markup and the exact expected on-screen glyph order, because bidi bugs are the class of defect most likely to corrupt money values ("‎-182.500" becoming "182.500-" is a financial error, not a cosmetic one). The touch-target, text-scaling, mirroring, reachability, and non-color-signaling sections convert the persona's physical reality (one hand, thumb reach, 200% text, sun on the screen) into geometry the coordinator can measure with a ruler on a screenshot.

---

## (a) WCAG contrast audit — computed

**Method.** For each color, channels are linearized: for c = channel/255, if c ≤ 0.04045 then c′ = c/12.92, else c′ = ((c+0.055)/1.055)^2.4. Relative luminance L = 0.2126·R′ + 0.7152·G′ + 0.0722·B′. Contrast ratio CR = (L₁+0.05)/(L₂+0.05), L₁ = lighter. AA normal text (14px Arabic counts as normal — never "large") requires 4.5:1; AA large text (≥24px, or ≥18.66px at weight ≥600) and non-text UI (1.4.11) require 3:1.

**Worked example (ink-strong #1F1E1D on canvas #FAF9F5).**
R = 31 → c = 0.12157 > 0.04045 → R′ = ((0.12157+0.055)/1.055)^2.4 = (0.16737)^2.4 = 0.01370. G = 30 → G′ = 0.01298. B = 29 → B′ = 0.01229.
L(ink-strong) = 0.2126·0.01370 + 0.7152·0.01298 + 0.0722·0.01229 = 0.0131.
Canvas: R = 250 → R′ = 0.95597; G = 249 → G′ = 0.94731; B = 245 → B′ = 0.91310. L(canvas) = 0.2126·0.95597 + 0.7152·0.94731 + 0.0722·0.91310 = 0.9467.
CR = (0.9467+0.05)/(0.0131+0.05) = 0.9967/0.0631 = **15.80:1 → PASS**.

**Relative luminance of all tokens (computed):**

| Token | Hex | R′ | G′ | B′ | L |
|---|---|---|---|---|---|
| surface | #FFFFFF | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| canvas | #FAF9F5 | 0.9560 | 0.9473 | 0.9131 | 0.9467 |
| sunken | #F0EEE6 | 0.8714 | 0.8550 | 0.7913 | 0.8539 |
| positive-tint | #E7EFE7 | 0.7991 | 0.8632 | 0.7991 | 0.8449 |
| warning-tint | #F4EDD8 | 0.9047 | 0.8469 | 0.6867 | 0.8476 |
| info-tint | #E8EDF1 | 0.8070 | 0.8469 | 0.8796 | 0.8408 |
| danger-tint | #F7E7E2 | 0.9301 | 0.7991 | 0.7605 | 0.8242 |
| brand-tint | #F7EAE4 | 0.9301 | 0.8228 | 0.7758 | 0.8422 |
| line-soft | #EAE6DC | 0.8228 | 0.7913 | 0.7157 | 0.7925 |
| line-strong | #DED9CB | 0.7305 | 0.6939 | 0.5972 | 0.6947 |
| ink-disabled | #B7B2A6 | 0.4735 | 0.4452 | 0.3813 | 0.4466 |
| brand-atmosphere | #CC785C | 0.6038 | 0.1878 | 0.1070 | 0.2704 |
| brand-ink | #964E33 | 0.3050 | 0.0762 | 0.0331 | 0.1217 |
| danger | #B42318 | 0.4564 | 0.0168 | 0.0091 | 0.1097 |
| info | #3E5C76 | 0.0482 | 0.1070 | 0.1812 | 0.0999 |
| warning | #8A6520 | 0.2542 | 0.1301 | 0.0144 | 0.1481 |
| positive | #2E7D57 | 0.0273 | 0.2051 | 0.0953 | 0.1594 |
| ink-muted | #6E6A60 | 0.1559 | 0.1441 | 0.1170 | 0.1447 |
| ink-subtle | #767265 | 0.1812 | 0.1683 | 0.1301 | 0.1683 |
| ink | #33322E | 0.0331 | 0.0319 | 0.0273 | 0.0318 |
| ink-strong | #1F1E1D | 0.0137 | 0.0130 | 0.0123 | 0.0131 |

**Pair table (the division shown is the arithmetic):**

| # | Pair | Computation | CR | AA 4.5 normal | AA 3.0 large/UI |
|---|---|---|---|---|---|
| 1 | ink-strong on canvas | 0.9967/0.0631 | **15.80:1** | PASS | PASS |
| 2 | ink on canvas | 0.9967/0.0818 | **12.18:1** | PASS | PASS |
| 3 | ink-muted on canvas | 0.9967/0.1947 | **5.12:1** | PASS | PASS |
| 4 | ink-subtle on canvas | 0.9967/0.2183 | **4.57:1** | PASS (resting only — see rule 5) | PASS |
| 5 | ink-strong on surface | 1.0500/0.0631 | **16.64:1** | PASS | PASS |
| 6 | ink on surface | 1.0500/0.0818 | **12.83:1** | PASS | PASS |
| 7 | ink-muted on surface | 1.0500/0.1947 | **5.39:1** | PASS | PASS |
| 8 | ink-subtle on surface | 1.0500/0.2183 | **4.81:1** | PASS (resting only — rule 5) | PASS |
| 9 | ink-strong on sunken | 0.9039/0.0631 | **14.33:1** | PASS | PASS |
| 10 | ink on sunken | 0.9039/0.0818 | **11.05:1** | PASS | PASS |
| 11 | ink-muted on sunken | 0.9039/0.1947 | **4.64:1** | PASS | PASS |
| 12 | positive on surface | 1.0500/0.2094 | **5.02:1** | PASS | PASS |
| 13 | danger on surface | 1.0500/0.1597 | **6.57:1** | PASS | PASS |
| 14 | warning on surface | 1.0500/0.1981 | **5.30:1** | PASS | PASS |
| 15 | info on surface | 1.0500/0.1499 | **7.01:1** | PASS | PASS |
| 16 | positive on canvas | 0.9967/0.2094 | **4.76:1** | PASS | PASS |
| 17 | danger on canvas | 0.9967/0.1597 | **6.24:1** | PASS | PASS |
| 18 | warning on canvas | 0.9967/0.1981 | **5.03:1** | PASS | PASS |
| 19 | info on canvas | 0.9967/0.1499 | **6.65:1** | PASS | PASS |
| 20 | positive on positive-tint | 0.8949/0.2094 | **4.27:1** | **FAIL** (large/UI only) | PASS |
| 21 | danger on danger-tint | 0.8742/0.1597 | **5.47:1** | PASS | PASS |
| 22 | warning on warning-tint | 0.8976/0.1981 | **4.53:1** | PASS (resting only — rule 4) | PASS |
| 23 | info on info-tint | 0.8908/0.1499 | **5.94:1** | PASS | PASS |
| 24 | brand-ink on surface | 1.0500/0.1717 | **6.11:1** | PASS | PASS |
| 25 | brand-ink on brand-tint | 0.8922/0.1717 | **5.20:1** | PASS | PASS |
| 26 | brand-ink on canvas | 0.9967/0.1717 | **5.80:1** | PASS | PASS |
| 27 | on-brand (white) on brand-ink | 1.0500/0.1717 | **6.11:1** | PASS | PASS |
| 28 | ink-strong on brand-atmosphere | 0.3204/0.0631 | **5.08:1** | PASS | PASS |
| 29 | white on brand-atmosphere | 1.0500/0.3204 | **3.28:1** | **FAIL** (large only) | PASS |
| 30 | white on danger | 1.0500/0.1597 | **6.57:1** | PASS (filled destructive button) | PASS |
| 31 | white on positive | 1.0500/0.2094 | **5.02:1** | PASS | PASS |
| 32 | white on info | 1.0500/0.1499 | **7.01:1** | PASS | PASS |
| 33 | white on warning | 1.0500/0.1981 | **5.30:1** | PASS | PASS |
| 34 | ink-strong on brand-tint | 0.8922/0.0631 | **14.14:1** | PASS | PASS |
| 35 | ink on brand-tint | 0.8922/0.0818 | **10.90:1** | PASS | PASS |
| 36 | ink-disabled on surface | 1.0500/0.4966 | **2.11:1** | FAIL — *exempt (disabled, rule 7)* | FAIL (exempt) |
| 37 | line-strong on surface | 1.0500/0.7447 | **1.41:1** | decorative only (rule 8) | — |
| 38 | line-soft on surface | 1.0500/0.8425 | **1.25:1** | decorative only (rule 8) | — |

**Alpha composites (computed with simple sRGB alpha compositing, fg over bg):**

| Composite | Result | Check (computed) |
|---|---|---|
| Press 8% ink over surface | #EDEDED, L = 0.8469 | ink 10.96:1 ✓ · ink-muted 4.61:1 ✓ · ink-subtle **4.11:1 ✗** |
| Press 8% ink over canvas | #E8E7E4, L = 0.7991 | ink 10.38:1 ✓ · ink-muted 4.36:1 ✗ |
| Press 8% ink over brand-tint | #E6DAD4, L = 0.7172 | ink-strong 12.16:1 ✓ |
| Press 8% ink over brand-ink | #8C4A31, L = 0.1069 | white 6.69:1 ✓ |
| Press 8% ink over positive-tint | #D7DED7, L = 0.7160 | positive **3.66:1 ✗ (normal)** · ink 9.36:1 ✓ |
| Press 8% ink over warning-tint | #E3DCC9, L = 0.7173 | warning **3.87:1 ✗ (normal)** · ink 9.38:1 ✓ |
| Press 8% ink over info-tint | #D8DCE0, L = 0.7117 | info 5.08:1 ✓ |
| Press 8% ink over danger-tint | #E6D7D2, L = 0.7008 | danger 4.70:1 ✓ |
| Scrim 45% ink over canvas | #979694, L = 0.3053 | white sheet vs scrim **2.96:1** (< 3.0 — rule 9) |

**Pairing rules that follow (binding for the build):**

1. **positive-on-positive-tint (4.27:1) is body-text forbidden.** Positive may sit on positive-tint only as large text (≥24px or ≥18.66px @600) or as an icon/graphic (3:1). Body text on positive-tint is ink/ink-strong; positive carries the icon or the big number.
2. **White text is never set on brand-atmosphere (3.28:1).** brand-atmosphere is decorative atmosphere only; the only text allowed on it is ink-strong (5.08:1), and only at large sizes.
3. All semantic fills pass with white content: white on brand-ink 6.11:1, danger 6.57:1, positive 5.02:1, warning 5.30:1, info 7.01:1 — filled semantic buttons are safe with white labels at any size ≥14px.
4. **warning-on-warning-tint (4.53:1) holds only at rest.** Under the 8% press overlay it drops to 3.87:1. Therefore warning-colored *text* on warning-tint is limited to ≥18.66px/600 or icons; 14px chip/row copy on warning-tint uses ink with the warning color reserved for the icon + word chip. danger-on-danger-tint (4.70:1 pressed) and info-on-info-tint (5.08:1 pressed) may carry 14px text.
5. **ink-subtle is resting-state-only inside non-interactive regions** (captions, timestamps, update lines). During press, ink-subtle falls to 4.11:1 (on surface) / 3.89:1 (on canvas). Inside pressable rows/tiles, secondary text = ink-muted; ink-subtle appears only in ≥24px or non-pressable positions.
6. **ink-muted dips to 4.36:1 on pressed canvas** → pressable content (rows, tiles, chips) must be surface-backed, not canvas-backed. Canvas is the page backdrop behind non-interactive composition; interactive elements render on surface tokens so the 8% overlay never breaks their text.
7. **ink-disabled (2.11:1) only for the disabled state** — WCAG 1.4.3 exempts disabled controls, so pair it with `pointer-events: none`, `aria-disabled="true"`, and opacity on the whole control; disabled text is never the only copy of information.
8. **line-soft / line-strong (1.25:1 / 1.41:1 on surface) are decorative dividers only** — never the sole boundary or state indicator of a control. Input fields are identified by their ink labels + placeholder hierarchy; on focus, the 2px ink-strong ring (≥3:1 everywhere) carries the state per 1.4.11.
9. **Sheet-vs-scrim edge = 2.96:1 (just under 3:1):** the sheet must not rely on scrim alone — it requires an elevation shadow (≥8px blur, ink ≥12% alpha) plus 16px top radius; the shadow, scrim, and bottom anchoring together define the boundary.
10. Focus ring = ink-strong 2px, 2px offset — ≥12:1 on every background it can appear on; satisfies 2.4.11 (focus appearance) and 1.4.13 (not obscured).

---

## (b) Touch targets and gap math

**QuickActionRail geometry (tile 88×92, gap 8, full-bleed scroll container, first tile inset 16px from the screen's start edge).** Tile pitch = 88 + 8 = 96. Tile start positions (x, from the left edge of the LTR check / mirrored identically in RTL): t₁ = 16, t₂ = 112, t₃ = 208, t₄ = 304, t₅ = 400. A tile's on-screen width = min(W, start+88) − start.

| Viewport W | Full tiles | Next-tile peek (arithmetic) | Verdict |
|---|---|---|---|
| 320 | t₁–t₃ (end 296) | 320 − 304 = **16px** | documented 320px exception — acceptable, must be stated in the rail docs |
| 360 | t₁–t₃ | 360 − 304 = **56px** | PASS ≥28 |
| 390 | t₁–t₃ (t₄ 86/88 visible) | 390 − 304 = **86px** | PASS ≥28 |
| 430 | t₁–t₄ (end 392) | 430 − 400 = **30px** | PASS ≥28 |

Tile hit target 88×92 ≥ 48×48 (primary-class target) ✓; inter-tile gap 8 ≥ 8 ✓; rail-to-nav separation ≥ 8 ✓. **If the builder changes tile width or inset, the peek must be recomputed with the same formula: peek(W) = W − (16 + 96·k) for the first tile whose end exceeds W; requirement ≥28px at 360/390/430, 16px documented at 320.**

**Bottom navigation.** 4 tabs, item width = W/4: 80 / 90 / 97.5 / 107.5px at 320/360/390/430 — every tab ≥44px wide ✓. Nav content height ≥56px (icon 24 + 4 gap + 14px Arabic label, persistent), hit area = full item width × ≥56 ≥ 44×44 ✓. Tab items are one segmented control — the 8px *gap* rule applies to separately-bounded targets (buttons, rows, tiles), not within the bar; instead, icon+label groups require ≥8px optical separation inside the item. Active tab state is never color alone: icon stroke weight/fill + label weight 600 + 3px indicator bar under the item (ink-strong or brand-ink, both ≥3:1 vs nav surface).

**General target budget:** primary buttons 48px height; secondary buttons, inputs, rows, keypad keys ≥44px; any two adjacent independent targets ≥8px apart (or separated by a divider ≥1px line-strong + 8px optical). Visual glyphs may be smaller than the hit area, but the hit area may never be smaller than the visual target's row/tile bounds — no invisible shrink, no hit-area inflation into neighboring labels.

---

## (c) Text scaling risk analysis (100% / 130% / 200%)

All font sizes must be expressed in `rem` so the harness can scale by setting the root font size (16px base → 20.8px = 130%, 32px = 200%). Fixed heights on text containers are forbidden; containers grow with content.

| Text role | Base | @130% | @200% | Expected behavior |
|---|---|---|---|---|
| Primary value (money) | 32px | 41.6px | 64px | `431.100` ≈ 7 latin glyphs ≈ 250px wide @64px + `د.أ` ≈ 90px → exceeds 288px content width at 320: **currency wraps to its own line** (still `dir="ltr"`-isolated), block grows downward. NEVER clipped, NEVER ellipsized, NEVER letter-spaced to fit. |
| MetricRow label (Arabic) | 14px | 18.2px | 28px | Long labels ("إجمالي المبيعات لهذا الأسبوع") wrap to 2 lines (max 3); value and label stay in the same row structure; row height grows; divider spans full width. |
| MetricRow value | 16px | 20.8px | 32px | Numbers wrap at the thousands separator only if unavoidable; no truncation; sign stays attached (bdi). |
| Qualifiers / rail labels (13px allowed) | 13px | 16.9px | 26px | Rail tile 92px tall absorbs 1→2 line wrap; label never exceeds tile bounds; if 2 lines + icon > 92px, tile grows, not clip. |
| Bottom nav labels | 14px | 18.2px | 28px | "الرئيسية" ≈ 8 glyphs ≈ 112px @28px > 80px tab width at 320 → wraps to 2 lines max, nav grows; no ellipsis. |
| Buttons | 14–16px | — | 32px | Button height grows (48 → ~64); label wraps inside padding; press target ≥44 always. |

**Never-clip invariants (checked at every width × scale):** money digits, dates, entry IDs, signs (+/−/%), and percentages. Truncation with `…` is only permitted for *narrative* text (notes, customer names in secondary positions) — never for values. At 200% the whole page becomes vertically scrollable; **horizontal overflow is a failure at any width/scale** (checklist item: `document.scrollingElement.scrollWidth ≤ innerWidth` at all 4 widths × 3 scales, both directions).

---

## (d) Bidi scenarios — required markup and expected rendering

Base direction is RTL on `html` (`dir="rtl"`). Isolation is applied at the money/number level with `<bdi dir="ltr">…</bdi>` (equivalently `dir="ltr"` spans, or a leading LRM U+200E for sign attachment); the parent stays RTL. Currency `د.أ` is always a separate Arabic run outside the number cluster.

| # | Content | Required markup | Expected on-screen rendering (described left→right) | Failure without markup |
|---|---|---|---|---|
| 1 | Negative amount | `<bdi dir="ltr">-182.500</bdi> <span>د.أ</span>` | `د.أ -182.500` — currency to the LEFT of the money cluster; cluster renders exactly `-182.500` (minus welded to the digits' left edge). Reading RTL: amount first, then currency. | Hyphen-minus is bidi ES → neutral → takes RTL: minus detaches and lands on the wrong side (`182.500-`), or migrates next to `د.أ`; the value reads as positive 182.500. |
| 2 | Mixed sentence | `دفع خالد <bdi dir="ltr">150.000</bdi> من أصل <bdi dir="ltr">1,312.400</bdi>` | Screen L→R: `1,312.400 أصل من 150.000 خالد دفع` — each number intact LTR; reading RTL reconstructs "دفع خالد 150.000 من أصل 1,312.400". | Grouping commas (CS) usually hold between digits, but any adjacent neutral (parenthesis, slash, trailing punctuation) can split the run and reorder digits across the Arabic words; copy/paste can reverse. bdi is the guard. |
| 3 | Date | `<bdi dir="ltr">08/09/2026</bdi>` (DD/MM/YYYY only) | Cluster renders exactly `08/09/2026`; in an RTL sentence it appears to the left of the preceding words (i.e., it *follows* them in reading order). | At run edges or with adjacent punctuation, separators can reorder (`2026/09/08`); ISO `YYYY-MM-DD` is forbidden in user-facing strings. |
| 4 | Percentage | `<bdi dir="ltr">+9%</bdi>` | Cluster renders exactly `+9%` — plus at the left of the digits, % at the right. | Bare in RTL: `+` (ES) detaches and reappears on the wrong side — `9%+` or `%9+` — the sign reads as trailing decoration and the delta's direction is lost. |

Additional bidi rules: keypad emits ASCII 0–9 and ASCII `.`/`,` only (Arabic-Indic ٠-٩ and Arabic comma `،` are forbidden inside values); never wrap the currency *inside* the digits' bdi; never rely on CSS `direction` alone for numbers — use the bdi/isolating markup so copy/paste and screen readers inherit it; and dates are never the only temporal signal when ambiguity is possible — label them ("استحق بتاريخ 08/09/2026").

---

## (e) Icon mirroring policy

| Icon / class | Policy in RTL | Rationale |
|---|---|---|
| Back chevron (رجوع) | **MIRROR** — points right in RTL | "Previous" is toward the reading start = screen right. |
| Forward chevron / "التالي" | **MIRROR** — points left | Forward follows reading direction = screen left. |
| Row disclosure chevrons | **MIRROR** — point left | Continuation of an RTL row flows left. |
| Directional arrows (next/previous, flow arrows, stepper) | **MIRROR** | Direction is reading-order-relative. |
| Sort-order arrows if directional | **MIRROR** | Same rule. |
| Wallet, box, truck, users, receipt, calculator | **NEVER MIRROR** | Objects have no reading direction; a mirrored truck reads as a truck facing the wrong way. |
| Check, X, alert, info, clock | **NEVER MIRROR** | Semantic glyphs — a check must stay a check. |
| Charts, sparklines, all chart primitives | **NEVER MIRROR**; time axis stays LTR inside the chart even in RTL | Time is not a reading-direction concept; the chart's internal geometry is fixed LTR. |
| Brand marks / logo | **NEVER MIRROR** | Brand integrity. |
| Plus / minus / math signs | **NEVER MIRROR** | Signs are mathematical, not directional. |
| Digits, Latin fragments, entry IDs | **NEVER MIRROR** (bidi handles them) | Mirroring would corrupt values. |
| Paper-plane send icon | **FORBIDDEN — never used at all** | Replace send/save actions with Arabic text labels ("إرسال", "حفظ") plus, if needed, a directional arrow that mirrors per this table. |

Implementation: mirroring via `[dir="rtl"] .icon--mirror { transform: scaleX(-1) }` or RTL-specific sprite assets; never mirror an icon containing digits/Latin text or a brand mark; mirror decisions live in the icon registry so components can't guess.

---

## (f) One-hand reachability

Primary money actions must live in the **bottom 60%** of the viewport; the strict thumb zone (bottom 25%) gets the single most likely action of the current surface. At 390×844 the bottom-60% band starts at y = 337.6; at 360×667 it starts at y = 266.8. Computed placements: QuickActionRail top ≈ 844 − 34 (safe area) − 60 (nav) − 8 − 92 (rail) = **y 650 ✓** (and ≈ 503 on the 667-tall device ✓); bottom nav is by definition in-zone; sheet primary buttons are pinned within ~160px of the sheet bottom ✓. Nothing "primary-only" may sit above 40% of viewport height (the top zone is for identity/status, not for the actions the thumb needs). The sheet's drag handle sits at the sheet top — acceptable only because Esc, scrim-tap, and (on real devices) back gesture are equivalent dismissal paths. Reachability is verified in the checklist by bounding-box measurement, not by feel.

---

## (g) Non-color status signaling (per state)

Color is never the only status signal; each state carries at least two non-color channels (sign, word, icon, or structure):

| State | Color token | Required non-color signals |
|---|---|---|
| Cash received / confirmed / completed / favorable | positive | `+` sign on the value; word (وارد / مكتمل); check icon; count/position when in a list. |
| Cash out / negative / real failure / destructive | danger | `−` sign on the value; word (صادر / فشل / حذف); X or alert icon. |
| Overdue / threshold / attention / estimate exceeded | warning | word (متأخر / تجاوز الحد); alert icon; structural priority (pinned row). |
| In progress / decision-critical pending / neutral operational | info | word (معلّق / قيد المعالجة); clock icon; spinner when tied to a live action. |
| Unknown (data not available) | info or ink per context | the words `غير متوفر`; info icon; em-dash value — **never 0.000**. |
| Disabled | ink-disabled + control opacity | `pointer-events:none`; `aria-disabled`; the action's unavailability is stated, not just grayed. |
| Chart series: planned / actual / forecast | line colors | line texture (solid / dashed / dotted) + direct Arabic labels at line ends; legend never color-only; full text alternative (visually-hidden table or `aria-label` summary) per chart. |
