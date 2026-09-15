# Accessibility & RTL Report — Micro Library (Final)

Run `20260908T133450Z-16d11` · Agent 04's accessibility/RTL review with recomputed contrast evidence (`contrast_check.py` in the same agent folder). All required fixes were applied to the build (see `decision-log.md` and `verification-report.md` §7): ink-strong focus ring; 44px hit areas for avatar, header action, search clear and drag handle; rail tile min-height; completion dwell ≥1.5s; dirty-guard dismissal; scroll-padding on the rail; bracket-isolation for percentages; `inputmode="decimal"` on amount fields.

---

# Accessibility & RTL Report — Computed Evidence and Rulings

Agent 04 · Task 3 · Run `20260908T133450Z-16d11`. All ratios **recomputed** with `contrast_check.py` (this folder; WCAG 2.2 relative-luminance formula, alpha composited first). Thresholds: 4.5:1 normal text; 3:1 large text (≥24px, or ≥18.66px bold) and non-text graphics (§1.4.11).

---

## 1. Computed contrast — Agent 02's claims, independently verified

**Result: 62/62 recomputed pairs match Agent 02's numbers** (the single flagged row, `ink`/`positive-tint` 10.94 vs the prose range "10.7–11.0", is a range-vs-point artifact, not an error). Agent 02's math is trustworthy. One **correction elsewhere**: Agent 03 claims the `brand-ink` focus ring holds "≈6.3–6.8:1" — recomputed it is **5.09–6.11:1** (still passing 3:1, but the stated range is wrong; fix `component-architecture.md` §7).

### Text pairs — full computed table (PASS = ≥4.5:1; ◆ = LARGE ONLY 3–4.5; ✗ = fail normal-text bar)

| fg/bg | ratio | fg/bg | ratio | fg/bg | ratio |
|---|---|---|---|---|---|
| ink-strong/surface | 16.64 | ink-muted/sunken | 4.64 | warning/warning-tint | 4.53 ⚠0.03 |
| ink-strong/canvas | 15.80 | ink-subtle/surface | 4.81 | info/surface | 7.01 |
| ink-strong/sunken | 14.33 | ink-subtle/canvas | 4.57 | info/canvas | 6.65 |
| ink-strong/brand-atmo | 5.08 | ink-subtle/sunken | 4.14 ◆ | info/info-tint | 5.94 |
| ink/surface | 12.83 | ink-disabled/surface | 2.11 ✗ | on-brand/brand-ink | 6.11 |
| ink/canvas | 12.18 | ink-disabled/canvas | 2.01 ✗ | on-brand/positive | 5.02 |
| ink/sunken | 11.05 | brand-ink/surface | 6.11 | on-brand/danger | 6.57 |
| ink/brand-atmo | 3.92 ◆ | brand-ink/canvas | 5.80 | on-brand/warning | 5.30 |
| ink-muted/brand-atmo | 1.65 ✗ | brand-ink/sunken | 5.26 | on-brand/info | 7.01 |
| ink-muted/surface | 5.39 | brand-ink/brand-tint | 5.20 | on-brand/brand-atmo | 3.28 ◆ |
| ink-muted/canvas | 5.12 | ink/positive-tint | 10.94 | ink-strong/positive-tint | 14.19 |
| positive/surface | 5.02 | ink/danger-tint | 10.68 | ink-muted/positive-tint | 4.60 |
| positive/canvas | 4.76 | ink/warning-tint | 10.97 | ink/info-tint | 10.89 |
| positive/sunken | 4.32 ◆ | danger/surface | 6.57 | danger/canvas | 6.24 |
| positive/positive-tint | 4.27 ◆ | danger/sunken | 5.66 | danger/danger-tint | 5.47 |
| warning/surface | 5.30 | warning/canvas | 5.03 | | |

### Graphics/structure (3:1) and composites

`brand-atmosphere`/surface 3.28 PASS · /canvas 3.11 PASS (narrow — verify on device) · /brand-tint 2.78 **FAIL** (no atmosphere icon on the tinted tile — use `brand-ink`) · `brand-ink`/positive-tint 5.21 PASS · semantic solids on own tints 4.27–5.94 PASS · lines 1.18–1.41 and surface steps 1.05–1.16 — **sub-3:1 by design**: identification never relies on them (fill vs canvas, typography, focus ring). Composites: press 8% over surface → `#EDEDED` (ink 10.96, ink-muted 4.61); over brand-ink → `#8C4A31` (white 6.69); over canvas → `#E8E7E4` (ink-strong 13.46); scrim 45% over canvas/surface → `#979694`/`#9A9A99`, nothing readable on scrim — ✓ all as claimed.

**Ruling (bold interpretation).** Agent 02 treats weight 600 as "bold" for the 18.66px threshold; WCAG's bold convention is 700. Conservative ruling for Agent 05: claim the large-text exemption only at ≥24px any weight, or ≥18.66px at 700. No current pairing violates this (the 32px/600 value qualifies by size alone), but 15–17px/600 semantic-on-tint text must use `ink`, and `positive`-on-tint stays reserved for 32px values, icons, and signs.

## 2. Focus-ring conflict — three agents, three rings (ruling required)

Agent 01's Input contract proposes `brand-atmosphere` rings; Agent 02's law says `ink-strong`; Agent 03 implements `brand-ink`. Computed as graphics (3:1) over every drawable surface: `ink-strong` 14.12–16.64 on all surfaces/tints (5.08 on atmosphere) — **passes everywhere**; `brand-ink` 5.09–6.11 on light surfaces — passes, but 1.87 on atmosphere; `brand-atmosphere` 3.28 on surface / 3.11 on canvas — **fails on sunken (2.82) and every semantic tint (2.73–2.80)**, exactly where input fields live.

**Ruling: adopt `ink-strong`, 2px, 2px offset, everywhere.** It is the only candidate with no failing surface, matches Agent 02's locked law and Agent 01's majority contracts, and stays out of the brand budget. Agent 01's input ring and Agent 03's implementation must both change.

## 3. Bidi strategy audit

The pattern — numeric string in `<bdi dir="ltr">`, `د.أ` as a separate Arabic node — is verified correct for leading signs (`-92.50` keeps the minus leftmost), thousands separators (`1,284.50`), `DD/MM/YYYY`, times, identifiers; reading order label → number → currency matches Arabic convention. Three gaps:

1. **Bracketed percentages.** `هدف الشهر — 1,950.00 من 3,000.00 (65%)` — parentheses are mirroring neutrals; `(65%)` as plain RTL text can render with flipped brackets. **Fix:** isolate the whole token: `<bdi dir="ltr">(65%)</bdi>` — or drop the brackets in copy.
2. **Unknown dash alignment.** `—` should sit inside the same LTR isolate structure as numbers so the value column keeps one alignment; a bare neutral dash in RTL flow is technically safe but visually inconsistent. **Fix:** `<bdi dir="ltr">—</bdi>` in value positions.
3. **Amount input.** Add `inputmode="decimal"` + `type="text"` + `dir="ltr"` (contract implies but does not state it); grouping applies on blur, digits stay plain while typing.

## 4. Icon mirror registry audit

Consistent across all three agents: **mirror** back/forward chevrons, drill chevrons, horizontal directional arrows via `html[dir="rtl"] .icon-mirror { transform: scaleX(-1); }`; **never mirror** semantic/object icons (check, clock, plus, receipt, package, banknote, trash, calendar) and vertical trend arrows. **No paper-plane send icon exists** in any proposal and none is needed (`إرسال التذكير` is text). Verdict: adopt Agent 03's one-rule registry verbatim; add a checklist row asserting no `.icon-mirror` lands on semantic icons and no send glyph is introduced.

## 5. Text-scaling risk register (100/130/200%)

| # | Risk | Ruling / fix |
|---|---|---|
| 1 | Rail label 13→26px at 200% inside locked 88×92 tile; icon 24 + gap 8 + two 26px lines ≈ 105px+ — overflows the fixed 92px height | Treat 92px as **min-height, not fixed height**; width 88, gap 8, rail padding 16 stay locked (peek math is horizontal). SPEC §6.5 forbids fixed heights for variable Arabic; §6.8 locks default-scale geometry. Clamp label to 2 lines; JS-measure at all widths × 3 scales |
| 2 | 13px qualifier vs 14px Arabic minimum (SPEC §6.4 internal conflict) | **Ruling below (§7)** |
| 3 | Nav labels 14px at 320px: `المبيعات` (~58px of glyphs + 16px padding) can clip in a 64px seat | JS-measure; fallback copy drops the article: `مبيعات` (fits, natural Arabic, no shrink) |
| 4 | State chips fixed 28px with 13px word at 200% | Chip height grows content-driven (single line kept) |
| 5 | Sheet CTA fixed 48px with 15px label at 200% | 48 is a **minimum**; height = max(48, content) |
| 6 | MetricRow value column ~96px at 200% | Label wraps under value; numeric rail never breaks — verify |

## 6. Non-color status signals per semantic family

positive: `+` sign, check icon, word `تم`/`مكتمل`. danger: `-` sign or `فشل`/`حذف` word + danger icon. warning: clock/threshold icon + word `بانتظار`/`متبقي` + since-date or count. info: word `قيد`/`بانتظار التأكيد` + queue/progress icon. cancelled/reversed: neutral ink-muted word `أُلغيت`/`معكوسة`, quiet by design. All proposals comply; the sole violation found is the CompactTile "warning dot" (journey review) — drop it or give it an accessible name.

## 7. Ruling: the 13px-vs-14px tension (for Agent 05)

SPEC §6.4 sets qualifiers at "approximately 13px" **and** an Arabic minimum of 14px; SPEC §6.8 fixes rail labels at 13px. Ruling: (a) **numeric/Latin runs** (dates, times, IDs, amounts in qualifiers) stay 13px — digit content, not Arabic script; (b) **QuickActionRail labels stay 13px** — §6.8 is the more specific rule and mandates it (spec-internal precedence, logged in `decision-log.md`); (c) **Arabic-word qualifiers, state lines, and input helper/error text render at 14px** (`--mc-type-min-arabic` exists) — `حتى 14:20`, `عند 4 عملاء`, `بانتظار تحويل…`, `أدخل مبلغًا أكبر من صفر`. "Approximately" is the latitude that makes this consistent: the Arabic floor governs where Arabic script is read; the 13px role survives where content is numeric.

## 8. Focus and keyboard semantics

Buttons must be `<button>`; every input has a visible bound `<label>` (never placeholder-as-label); icon-only buttons carry `aria-label` (`إضافة`, `مسح البحث`, `الحساب والإعدادات`); completion and error are live-announced — `role="status"` for `تم تسجيل البيع`, `role="alert"` for `فشل الإرسال` (SC 4.1.3); focus order follows DOM = visual RTL order; `:focus-visible` shows the 2px `ink-strong` ring, `:focus:not(:focus-visible)` suppresses it for pointer users. Micro-over-WCAG conflicts, documented: 44/48px targets exceed WCAG §2.5.8's 24px (Micro wins, stricter); `ink-disabled` 2.11:1 relies on WCAG's disabled-incidental exemption plus non-color cues; destructive dialogs refusing Escape is a deliberate Micro deviation with a tabbable `إلغاء` (no keyboard trap, SC 2.1.2 satisfied).
