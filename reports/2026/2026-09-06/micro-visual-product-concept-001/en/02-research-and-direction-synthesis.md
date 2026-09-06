# 02 — Research & Direction Synthesis

Delivery: `micro-visual-product-concept-001` · Stage 1 · 2026-09-06
Author: central orchestrator (decision owner). Inputs: sub-agent reports 01–05, source intake 00, lessons 01.

## 1. The most important findings

1. **Composition, not color, is the differentiation lever.** All five agents independently converged on this: the palette is fixed, the anti-reference is a card wall, and every rejected look (SaaS, POS, bank, ERP) is a *composition* failure before it is a styling failure. The winning direction must make hierarchy structural — one dominant truth block, full-width bands, a strict money column — instead of decorative.
2. **The measured contrast audit produces a hard design doctrine.** White on `#cc785c` (3.28:1) and on `#079fa0` (3.24:1) fails normal text; only `#964e33` (6.11:1) and `#057b7c` (5.08:1) are legal resting fills for labeled controls in light theme; `#b4613f` (4.45:1) is press-only. The critic caught a second-order consequence: the decorative terracotta spine fails even as non-text on brand-soft slabs (2.65:1). Doctrine adopted: **words never sit on mid-tone brand fills; the spine sits only on canvas/band tones, or becomes `#964e33` on soft slabs.**
3. **One neutral token set, not two.** The critic found the art-direction and a11y reports had proposed divergent neutrals. Resolved here as binding (computed-pass): light — canvas `#faf7f4`, band `#ffffff`, ink `#1f1a17`, muted `#5c5148`, hairline `rgba(31,26,23,.10)`; dark — canvas `#191512`, band `#201b17`, raised `#292420`, soft `#332d27`, ink `#f1e9e3`, muted `#b9aca2`, hairline `rgba(241,233,227,.12)`.
4. **Motion identity is a press signature, not an entrance show.** The motion report's tokens (`settle` `cubic-bezier(.22,1,.36,1)` 160–280ms; `leave` `cubic-bezier(.4,0,1,1)` 120–200ms; `steady` linear; `instant` ≤80ms), the color-press identity (`#b4613f` at 90ms + 6% terracotta wash, never scale), and the 6dp directional digit drift give Micro an interaction signature that is calm, RTL-mirrored, and NumericSurface-safe (stable digits).
5. **Trust is a visible system.** Honest states («قيمة غير محددة بعد», never a confident 0.00), the seven-state chip family, effect-preview sheets before irreversible actions, chart source-state captions («طول الشريط = نسبة من أكبر قيمة»), and quiet completion announced via `aria-live` — these are the trust surface that makes Micro feel like a mature product, and they will be *shown*, not described.
6. **The verified product skeleton is kept.** Five-seat shell «مشروعي الآن | العمل | سجّل | مالي | أدواتي», JOD «1,245.50 د.أ», `DD/MM/YYYY`, 24-char Arabic button cap, documented reversal — the concept builds on verified behavior, which is what separates this from a Dribbble shot.

## 2. The three differentiated directions

| | **A — «السجل الدافئ» / The Warm Ledger** (recommended) | **B — «الحرفة الهادئة» / Quiet Craft** (rejected preview) | **C — «التيار المالي» / The Financial Stream** (rejected preview) |
|---|---|---|---|
| Core idea | The screen is one continuous ledger: a hero truth block carved concentrically (20/8/12 radii), then full-width bands separated by tonal steps and hairlines; 3px terracotta spine marks the primary band's start edge | Chunky inset slabs with carved concentric corners; atmosphere-forward, 60px rows, fewer items per viewport | A chronological event stream on a terracotta rail with money/operational node dots; densest, 10–11 rows |
| Strengths | Composition *is* the owner's mental model (read the business top-to-bottom like a ledger); scales from 320px to 430px; highest calm-trust per density unit; dark theme is a deliberate luminance ladder | Distinctive warmth; strong on a single-task screen; pleasant hero moments | Best-in-class recency storytelling; great for the «عمل» (work) timeline; high scan speed |
| Risks (and fixes) | Band sameness → question-copy band headers; density creep → fold budget (1 hero + 3 bands, ≈6–7 rows at 390px); hairline DPR rendering → 1px + tonal step as belt-and-braces | Starves list screens (≈6 rows/viewport); reads as a "settings" product, weak for operations | Chronology is wrong for tools/settings/inventory; forced chronology distorts financial truth; rail on every screen becomes wallpaper |
| Critic score | **7.90 / 10** | 6.45 | 6.40 |

(H4 «المنضدة» was dropped before the matrix: its persistent position plateau fails short viewports and sticky-RTL edge cases — recorded in report 05.)

## 3. Recommendation and why it is stronger for Micro

**Direction A wins, with two selective adoptions** (group-synthesis style, documented in report 05): the concentric hero carve from B, and full-opacity node dots *restricted to the «عمل» timeline* from C. The decisive reason: Micro's owner does not browse — she interrogates the business ("what changed? who owes me? what needs attention today?"). A banded ledger answers each question in a fixed, learnable place with one dominant entry point per screen, and it does so at 320px without compromise. B buys warmth at the cost of operational density; C buys recency at the cost of truthful structure; A refuses the trade-off.

## 4. What will be visible in the HTML review artifact

- **Main review path (Direction A)** as a real, interactive phone-frame composition: Today (control center with truth block + attention band), Financial Truth (available / owed to me / owed by me with deltas), Quick Capture (NumericSurface with tap controls + digit drift), Receivables (people-first ledger with aging), Orders (status pipeline with search/filter + sheet), Purchases (supplier context + received-value bridge), Cash closing (counted vs system), Settings (vertical rows), Assistant entry shell.
- **Truth system live:** loading → quiet completion; offline banner; pending/estimated/synced/conflict chips; honest unknown («قيمة غير محددة بعد»).
- **Charts:** 14-day cash in/out columns + receivables aging buckets, RTL geometry, period + JOD + source-state captions, textual interpretation.
- **Controls outside the frame:** Arabic RTL default / English LTR verification, Light/Dark, normal/reduced motion, width 320/360/390/430, and compact previews of B and C with rejection rationale.
- **Motion demonstrations** per the inventory (sheet, push, digit drift, press identity, banner slide, quiet completion).

## 5. Decisions that must not be left ambiguous

| # | Decision | Binding choice |
|---|---|---|
| D1 | Resting control fills (light) | `#964e33` primary / `#057b7c` accent only; `#cc785c`/`#079fa0` never under body-size text |
| D2 | Press state | `#b4613f` 90ms color-press + ≤6% wash; no scale, never resting |
| D3 | Terracotta spine | 3px on canvas/band only; on brand-soft slabs it becomes `#964e33` |
| D4 | Row heights | Financial rows 64px / secondary 56px; top bar 64px; bottom shell 64px + safe-area |
| D5 | Numerals & formats | Western digits, `tabular-nums`, LTR isolates for «1,245.50 د.أ» and dates in RTL |
| D6 | Pending copy | «قيمة غير محددة بعد» for unknown values; pending state «قيد الانتظار» (register to be confirmed by owner in review) |
| D7 | Conflict presentation | Alert row (`role="alert"`), never a quiet chip |
| D8 | Warning pairing | text `#6d4a00` on `#f9eedb` (≥4.5:1) — replacing the failing `#a86a12` pair |
| D9 | Navigation shell | Five-seat labels kept exactly as verified; shell pixel-static through transitions |
| D10 | Direction previews | B and C shown compact, clearly labeled as not-recommended, with the reason |

## 6. Provenance note

Sources actually present were used (intake report 00); the three named packages remain missing and nothing was invented for them. All research claims are knowledge-based pattern evaluation of named products unless marked otherwise; the contrast values cited here were computed programmatically in report 04 and re-checked by the critic.
