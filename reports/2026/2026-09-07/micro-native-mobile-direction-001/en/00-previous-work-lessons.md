# 00 — Previous Work Lessons

**Delivery:** `micro-native-mobile-direction-001`
**Stage:** 0 — separation of retained lessons from rejected visual language
**Date:** 2026-09-07
**Author:** central orchestrator (independent execution, no chat memory assumed)
**Evidence base:** direct inspection of `reports/2026/2026-09-06/micro-visual-product-concept-001/` (Warm Ledger) and `reports/2026/2026-09-06/micro-visual-product-concept-002/` (Calm Ledger), including both synthesis reports, both lessons/intake reports, and the structural anatomy of both prototype HTML artifacts.

---

## 0. Source-package presence (binding honesty check)

Re-verified today against the full Documents repository (file listing + extension search):

| Named source | Status | Consequence |
|---|---|---|
| `micro-agent-input.zip` | **ABSENT** — no `.zip` exists anywhere in the repository | No baseline snapshot inspected; nothing invented for it |
| `micro-recovery-docs.zip` | **ABSENT** | No recovery-corpus re-verification; nothing invented |
| `MicroPrimitives-anti-reference.html` | **ABSENT** — only the two concept-review HTML artifacts and the user-flow atlas HTML exist | The anti-reference is used only as the characterization given in the task brief (card-wall composition, lab/showcase exposure), never as a quoted file |

This matches the source-intake reports of both prior deliveries (S2/S3/S4 marked NOT FOUND). The relevant decisions those packages would have carried are already summarized in the repository reports and in the task brief, so execution continues with the present evidence only.

---

## 1. Keep as a decision or behavior

These are verified product behaviors, measured facts, or truth-disciplines that survive the rejection of both visual directions. They are binding inputs for the native direction, not suggestions.

1. **Money language.** JOD amounts formatted `1,245.50 د.أ` — ASCII digits, two decimals, unit written after the number in the Arabic flow, `tabular-nums`, thousands grouping with comma, decimal point. Signs inside the digit isolate (U+2212 for minus). One money language everywhere; signed deltas for change.
2. **The bidi isolation contract.** Isolate **only the digit run** inside an LTR isolate (`<bdi dir="ltr">` or equivalent); keep the unit «د.أ» in the RTL flow; isolate dates `DD/MM/YYYY`. Unit-inside-isolation was measured to render «د.أ 20.00» in RTL and silently violate the unit-order rule — the single best correctness catch of the whole prior cycle.
3. **Honest financial states.** Unknown is never a fabricated `0.00` («قيمة غير محددة بعد», «—» occupying the amount column at number size); estimated carries a تقديري mark; conflict is an alert row, never a quiet chip; cancelled/reversed entries stay visible with their correction pair linked; unrecorded chart days render as gaps with a footnote, never zero bars.
4. **Measured contrast pairs (light).** White on `#cc785c` ≈ 3.28:1 — atmosphere/surface role only. White on `#b4613f` ≈ 4.4:1 — press-only, never described as a pass. `#964e33` + white ≈ 6.11:1 — the justified high-contrast action pairing. `#057b7c` + white ≈ 5.08:1 — accent text on light canvas. Dark `#d59172` may carry dark text where measured (5.26–6.82:1).
5. **Arabic legibility floors.** Nothing below 13px; body 15px; rows ≥56px; body line-height ≥1.6; button labels capped ~24 Arabic characters; long-name and long-label testing at 320px.
6. **Motion register.** Duration classes micro 80–120ms / standard 150–220ms / surface 240–280ms; zero overshoot; forbidden: bounce, counters, confetti, number rolls, decorative loops; reduced-motion = full alternatives (instant swaps, static marks), never shortened animation.
7. **Quiet completion.** A write finishes with a receipt-like closure sentence containing final tabular digits, one calm mark, and a `aria-live` polite announcement — then the surface settles. No applause.
8. **Operational coverage set.** The screen set both deliveries converged on — owner overview/Today, financial truth, quick capture, receivables/obligations, orders context, purchases/supplier context, cash closing, settings/profile — is the right scope and is retained.
9. **Touch geometry.** Targets ≥44×44 (48 for primary/keypad); rows ≤3 lines; one primary action per screen; one action word per row («حصّل»/«سلّم»/«أكمل»); details behind the row tap.
10. **Chart discipline.** Every chart answers a real owner question and carries period, unit, source-state, and a text interpretation that *is* the non-visual alternative. RTL time-flow mirrored in LTR verification.

## 2. Adapt as a principle

These were good ideas expressed in web-page form. The principle survives; the original expression does not.

1. **"Calm as countable arithmetic."** Block budgets, one hero figure, card quota ≤1, one primary — keep the arithmetic, apply it to *native screen anatomy* (stack levels, sheet content, tab roots) instead of page sections.
2. **Ledger vocabulary as voice.** «دفتر الناس», «كشف الأسبوع» — keep the language the owner already trusts in copy and naming, but a native product is not a paper-page simulation; the دفتر metaphor informs hierarchy, not skeuomorphic page layout.
3. **Typographic trust.** Number discipline, fixed money alignment, one hero figure per screen — keep, but as *native* typographic systems (large-title headers, compact stack titles, tabular rows), not as a typographic "web statement" composition.
4. **Warm neutral ladders.** The neutral token sets (light canvas `#faf7f4`, ink `#1f1a17`-family; dark canvas `#1a1613`-family with `#332d27` elevation) were measured and coherent — adapt them per direction with re-measured pairs rather than re-deriving from zero.
5. **Truth hierarchy.** Cash → receivables → payables with deltas and a "what changed and why" explanation — keep the hierarchy; rebuild its surface as app-level composition (position surfaces, counters, day digests) rather than dashboard blocks.

## 3. Reject as visual language

These are the specific properties that made both deliveries read as web pages inside a phone frame. They may not return in any native direction.

1. **The device frame itself.** `.device` box with 44px bezel radius, camera cutout, fixed 780/844px height, simulated status bar — a mockup, not an application screen.
2. **The desktop review console around the phone.** Grid layouts with 340px sidebars, control panels, contrast legends, and comparison thumbnails *surrounding* the product frame as the primary experience. Review affordances must live outside the app viewport entirely (URL parameters + a separate review index).
3. **Page-section composition as screen anatomy.** "One continuous page read top-to-bottom like a web article/dashboard" — bands, modules, grouped surfaces stacked into a scrollable page — instead of an app information hierarchy with destinations, stack levels, and contextual surfaces.
4. **CSS view-switching presented as navigation.** Swapping visible `<div>`s with no navigation stack, no back behavior, no push/pop choreography, no keyboard handling, no predictable scroll ownership.
5. **Both prior directions as final identities.** Warm Ledger's banded page + concentric hero carve, and Calm Ledger's single-column typographic statement page — both are web compositions. They are not candidates, not baselines to cosmetically improve, and their internal scores (7.90/10, 28/30, VLM 8.5–9/10) are self-assessments, **not approvals**.
6. **Static direction-preview thumbnails** as the way alternatives are compared (exhibit-style review artifacts).
7. **POS/banking/ERP drift patterns** already rejected in the prior cycle (checkout grids, wallet balance hero, dense reading walls, canned next-step text) remain rejected.

## 4. Needs independent verification

1. **Five-seat shell labels** «مشروعي الآن | العمل | سجّل | مالي | أدواتي» — verified as the current product's shell, but the native IA may re-map destinations; the owner must ratify the new top-level set (this review's explicit job).
2. **RTL chart time-flow (right→left)** with real Jordanian owners — usability validation still open.
3. **«د.أ» screen-reader pronunciation** strategy — device-test question.
4. **Haptics policy** — out of scope for HTML review; listed for Stage 4.
5. **Typeface path.** Prior cycle deferred a one-face vs two-face decision (Noto Sans Arabic + Inter with locked tabular digits). Each native direction now proposes its own Arabic type system; needs owner reaction + device verification.
6. **Offline-first sync choreography specifics** (queue badge, conflict copy, staleness threshold) — behaviors specified, not owner-validated.
7. **Prior QA claims** ("0 console errors", VLM self-scores) — not re-verified here; the present delivery runs its own independent browser QA and publishes its own evidence.

---

*This file is the boundary between evidence and invention: everything above is either verified in the repository or explicitly marked for verification. The three absent packages were not reconstructed.*
