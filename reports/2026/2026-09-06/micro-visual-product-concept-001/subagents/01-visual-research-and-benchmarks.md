# 01 — Visual Research & Benchmarks (Stage 1 · Sub-agent 1)

Delivery: `micro-visual-product-concept-001` · Task ID 1-a · 2026-09-06
Scope: pattern evaluation of named real products for Micro's visual product concept — patterns, not clones.

## 1. Method & limitations

This is a **knowledge-based pattern evaluation**. The named products are real and known to the author at pattern level; no live web fetch was performed, so **no version numbers, metrics, screenshots, or "current behavior" claims** are made. Each claim is a recollected pattern and why it works — enough for pattern decisions, not a competitive audit. No open-source code or visuals were inspected or copied; any repository consulted later requires a license check, and code/visuals must never be copied into Micro regardless of license.

Grounding comes from two verified layers: (a) the brief's immutable constraints (fixed Terracotta palette, measured contrast roles, five-seat shell, honest-unknown copy, effect previews, documented reversal); (b) repository evidence summarized in the Stage 0 intake report (`en/00-SOURCE-INTAKE-REPORT.md`). The anti-reference `MicroPrimitives` file is absent, so its avoid-list is used as characterized by the brief. Verdicts: **adopt** (use near-verbatim), **adapt** (keep the principle, reshape the form), **reject**.

## 2. Pattern evaluation table

| # | Pattern | Exemplar products | Why it works | Risk if misused for Micro | Verdict |
|---|---|---|---|---|---|
| P1 | Person-ledger receivables: money grouped by customer, with age and last activity | Khatabook, OkCredit, Vyapar | "Who owes me" is a people question; grouping by person makes collection actionable | Becomes a contacts directory that hides totals, aging, and dispute state | **Adopt** |
| P2 | One dominant position figure with delta line ("safe to spend") | Tide, Copilot Money | Answers "where do I stand" in one glance; delta pre-answers "what changed" | Decays into vanity stat tiles; confident zero shown for unknown values | **Adapt** |
| P3 | Event feed with explanation lines and source chips | Monzo/Starling transaction feed; QuickBooks activity | "Why did it change" is answered in place, at the row | If the home screen is a transaction list, Micro reads as a banking clone | **Adapt** |
| P4 | Envelope/"available" framing: money framed by what it must do | YNAB categories | Matches "what does today require" better than raw balances | Category sprawl too heavy for a micro owner | **Adapt** |
| P5 | Order status stepper with explicit completion moment | Shopify mobile orders; Talabat/Careem tracking | Mirrors operational reality; gives sale-recognition a visible moment | Decorative progress bars with no financial meaning attached | **Adopt** |
| P6 | Bottom action sheet with consequence preview before irreversible actions | iOS HIG confirmations; Micro's existing effect-preview evidence | Forces consequence reading in the thumb zone | Modal fatigue if triggered for trivial confirmations | **Adopt** |
| P7 | Persistent offline/sync truth (status the system states about itself) | Square seller offline mode; Google Docs offline | Field commerce has real connectivity loss; trust survives it | Permanent nag banner when everything is synced | **Adopt** |
| P8 | Recency-driven adaptive home | Notion mobile recents; WhatsApp chat list | Answers "what needs attention today" from real events, not widgets | Algorithmic noise; home becomes unpredictable | **Adapt** |
| P9 | Large numeric entry surface with visible context | Square tender amounts; Copilot amount entry | Money entry is Micro's most-used action; digits need scale and position | Keypad hides balance context while entering | **Adopt** |
| P10 | Quiet completion with an undo window | Gmail undo snackbar; restrained iOS haptics | Calm professionalism; makes documented reversal («تراجع موثق») natural | Celebratory confetti and success spam | **Adopt** |

## 3. Explicit REJECT list

- **Equal stat-tile grids** — generic SaaS rhythm; no reading order; the anti-reference's card wall in another costume.
- **Dense data tables and ribbon/toolbars** — desktop ERP compressed into a phone; violates Micro's measured density cap (finance 277→257); impossible one-handed.
- **Banking-clone home** — giant balance + Send/Request button row + transaction list. Micro is not a money-mover; it connects operations to financial truth.
- **POS tender grid** — oversized category buttons as the entry screen; Micro is not a POS.
- **Purple-gradient fintech cliché, glassmorphism, neon glow** — trendy, and the palette is immutable anyway.
- **Badge-spam** — red dots everywhere; attention inflation destroys "what needs attention today".
- **Card walls and showcase/lab controls inside the product frame** — the anti-reference verbatim.
- **Gamified streaks, confetti, celebratory money moments** — conflicts with quiet completion and financial seriousness.
- **Jordanian decorative identity** (shemagh, mosaics, maps, flag colors, landmarks) — explicitly banned; differentiation comes from composition and behavior.
- **White text on `#cc785c` resting states; `#b4613f` as a resting color** — fails the measured contrast audit (3.28:1; 4.42:1 is press-only). `#964e33` is the only eligible high-contrast action fill.
- **Chart-panel vanity dashboards without source-state captions** — dishonest by Micro's own chart-honesty precedent (bar-proportion labeling).
- **Icon-only bottom shell** — the five seats must keep their Arabic labels («مشروعي الآن | العمل | سجّل | مالي | أدواتي»).

## 4. Recommended patterns for Micro (10)

Each: what it is · why it fits the owner's seven questions · ergonomics · RTL.

**R1 — Truth Block.** One dominant per-screen block: money-now in large tabular numerals («1,245.50 د.أ»), a state chip (مُزامن / غير متصل / تقديري), and a one-line delta linking to the change ledger. Answers *position now* and pre-answers *what changed*. Ergonomics: read-zone at top; zero interaction cost. RTL: stable tabular digits inside the RTL line; «د.أ» suffix per verified format.

**R2 — Change Ledger.** Grouped rows (اليوم / أمس / سابقًا): amount, source chip (نقدي / — غير نقدي: لا يخرج كاش ولا يدخل نتيجة الفترة), one-line cause. Answers *what changed* and *why*. Ergonomics: 48pt full-width rows. RTL: leading icon on the right, trailing numerals directionally stable.

**R3 — People-first receivables.** A «من لي عليه؟» surface grouped by customer: outstanding amount, age, last event; tap opens the person's ledger with a collect action. Answers *who owes me*. Ergonomics: sticky sort (الأحدث/الأقدم) above thumb reach. RTL: Arabic names lead from the right; call/WhatsApp actions trail left, under the thumb.

**R4 — Obligations band.** A conditional band for *what I owe*: visible only when payables exist, due-today first; quiet omission when empty, never a zero. Answers *what do I owe* and part of *what today requires*. Ergonomics: horizontal band inside the one-handed sweep; expands to a list. RTL: due chips mirror with the flow.

**R5 — Completion-gated sale stepper.** Order cards carry a vertical stepper (طلب → تحضير → تسليم) marking the exact moment «تم الاعتراف بالبيع», with deposits shown as a «سيولة مرتبطة بالتزام» chip until completion. Separates liquidity from profit honestly. Ergonomics: stepper inside the card, no nested navigation. RTL: connectors and fill mirror right-to-left.

**R6 — Effect-preview action sheets.** Every irreversible action opens a bottom sheet whose preview box names the money effect and the obligation/inventory effect, with a ≤24-char Arabic confirm label. Confirm fill: `#964e33` resting, `#b4613f` press-only. Ergonomics: bottom sheet = thumb zone; one dominant confirm. RTL: sheet and its lines mirror.

**R7 — Honest-unknown state system.** Unknowns render «قيمة غير محددة بعد» at full content size with a dashed tonal border — never small gray, never 0.00. One chip family: تقديري / معلّق / غير متصل / مزامنة / مُزامن / تعارض. Answers *position* truthfully. Ergonomics: readable at arm's length, never tooltip-sized. RTL: chips flow RTL; digits inside remain LTR-stable.

**R8 — NumericSurface entry.** Full-width keypad sheet: large tabular digits, a context line above («رصيدك بعد هذه العملية: …»), visible tap controls, reduced-motion alternative. Ergonomics: one-handed entry with no reach to the top. RTL: bidi-safe grouping; currency suffix after digits.

**R9 — Attention list on the home seat.** «مشروعي الآن» opens with an adaptive 3–5 item list generated from events (تحصيل مستحق اليوم، مشتريات لم تُستلم، مصروف غير مسجل), each row with one action button. Answers *what needs attention today* and *what next*. Ergonomics: action buttons sit in the lower thumb arc of each row. RTL: rows mirror; actions trail left.

**R10 — Quiet completion + documented reversal.** Success is one calm line plus a «تراجع موثق» affordance for its validity window; the reversal becomes a visible ledger entry. A reversal is a change with provenance. Ergonomics: bottom snackbar, undo on the thumb side. RTL: mirrored placement, same timing.

## 5. What "trust" must look like in Micro

Trust in Micro is a rendering contract, not a tone of voice. Four pillars, each anchored in verified conventions:

1. **State truth.** Unknown is a first-class visual state («قيمة غير محددة بعد», «قيمة الهدر غير معروفة بعد») at full size — a confident zero is forbidden. Non-cash rows carry the disclaimer in place. Charts carry source-state captions and honest proportion labeling.
2. **Consequence preview.** Before any irreversible action, an effect-preview box states the money effect and the operational effect in the owner's language. No hidden side effects.
3. **Reversibility.** «تراجع موثق» is not an apology; it is a designed state with a visible trace in the ledger, plus the correction disclosure («تصحيح هذه العملية») where density allows.
4. **Sync truth.** غير متصل / مزامنة / مُزامن / تعارض are persistent, calm chips — never alarm banners. Deposits are always labeled as liquidity with an unfinished obligation; sale recognition happens only at completion.

Visually, trust means restraint: terracotta soft surfaces for atmosphere, `#964e33` reserved for the single high-contrast confirm per view, one accent family (`#079fa0`/`#057b7c`/soft) carrying all state chips. When color says less, the owner believes the numbers more.

*End of report — Stage 1, sub-agent 1 of 5.*
