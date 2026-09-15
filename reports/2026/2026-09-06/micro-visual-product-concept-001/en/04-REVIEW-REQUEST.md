# 04 — Review Request (Stage 3 Gate)

To: the product owner of Micro
From: the central design-research & visual-product orchestration agent
Date: 2026-09-06 · Delivery `micro-visual-product-concept-001`

## 1. What is ready to inspect

- **`prototype/micro-visual-concept-review.html`** — a self-contained, interactive HTML artifact. Open it in any browser. It contains the recommended concept as a working mobile composition (9 screens, Arabic RTL default), compact real previews of the two rejected directions, and review controls: Arabic RTL / English LTR, Light / Dark, normal / reduced motion, 320 / 360 / 390 / 430 widths.
- `en/03-html-review-guide.md` — the route through the artifact and what to inspect on each screen.
- Five specialist reports + the adversarial critique under `subagents/`, the direction synthesis under `en/02-…`, source intake `en/00-…`, lessons `en/01-…`.
- Verification evidence screenshots under `supporting/review-evidence/` (captured from the actual artifact in a headless browser).

## 2. The recommended direction

**A — «السجل الدافئ» / The Warm Ledger**: one continuous ledger per screen — a dominant truth block, full-width question-headed bands, a strict money column, a 3px terracotta spine marking the primary surface — with two deliberate borrowings (concentric hero carve; node dots restricted to the «العمل» timeline). Adversarial score 7.90/10 versus 6.45 (B) and 6.40 (C). The full rationale and the three binding conditions adopted from the critique are in `en/02` and `subagents/05`.

## 3. What you must compare

1. **A against B and C** (Direction switch) — decide whether the ledger composition is the Micro identity you want.
2. **Arabic RTL against English LTR** — the English mode exists to prove mirroring; confirm you accept RTL-first with English as verification.
3. **Light against Dark** — confirm the dark mapping reads as deliberate, not inverted.
4. **Motion normal against reduced** — confirm the calm signature (color-press, 6dp digit drift, quiet completion) and that reduced motion loses no meaning.
5. **390 against 320** — confirm the truncation honesty at the narrowest contracted width.

## 4. Known limitations (stated, not hidden)

- The three named source packages were **absent** (`micro-agent-input.zip`, `micro-recovery-docs.zip`, `MicroPrimitives-anti-reference.html`); constraints were taken from the brief plus actually-present repository reports. See `en/00`. If you supply them later, the audit (`en/11`) can be re-run without redesign.
- The artifact is a **concept simulation**: no persistence, no backend; save/collect/closing are visual flows with demo data; the assistant answers from canned but number-consistent content.
- The English layer is a verification mode, not finalized localized copy; the pending-state copy «قيمة غير محددة بعد» / «قيد الانتظار» register needs your confirmation (D6/D10 in `en/02`).
- Verified in Chromium at the four widths and both themes; **no real-device testing has been performed** (none is claimed).
- The press pairing white-on-`#b4613f` (4.45:1) remains a transient press state, not a full AA pass — documented per the color audit.

## 5. Explicit questions requiring your approval

1. **Direction:** do you approve **A — The Warm Ledger** as the sole basis for the Stage 4 final visual package (or do you request a revision of A, or a different direction)?
2. **Borrowings:** keep the concentric hero carve and the «العمل»-only node dots, or strip them for a purer ledger?
3. **State copy register:** confirm «قيمة غير محددة بعد» for unknown values and «قيد الانتظار» for pending (plus «تقديري / غير متصل / جارٍ المزامنة / مُزامن / تعارض»).
4. **Numerals & formats:** confirm Western tabular digits, «1,245.50 د.أ», `DD/MM/YYYY` as the contract.
5. **Scope of Stage 4:** produce the full package (`en/05…en/14` + final prototype + asset inventory) for this direction without further direction changes?

## 6. Status

**This agent is waiting for your approval.** No Stage 4 work (final visual package `en/05–en/14`, final prototype, asset inventory, implementation handoff) has been started, and the production Micro codebase has not been touched. On approval, Stage 4 proceeds exactly for the approved direction; on rejection with focused feedback, only the requested direction is revised and the HTML review is regenerated before anything is finalized.
