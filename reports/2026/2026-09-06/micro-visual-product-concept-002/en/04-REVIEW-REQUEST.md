# 04 — REVIEW REQUEST (Stage 3 — Approval Gate)

**To:** the Micro product owner
**From:** the visual-product orchestration agent
**Date:** 2026-09-06
**Status:** **Stage 2 complete. Waiting for your approval. Nothing will be finalized before you answer.**

> **Delivery-ID note:** this complete Stage 0–2 package is delivered as `micro-visual-product-concept-002`. A parallel execution of the same task pushed a partial Stage 0–1 text set (no HTML artifact, no review gate) under `micro-visual-product-concept-001`; per the delivery rules those files were **not overwritten** and remain in the repository as a partial record. All references below are to this delivery (‑002).

---

## 1. What is ready to inspect

| Item | Path |
|---|---|
| Interactive HTML review artifact (self-contained, browser-openable) | `prototype/micro-visual-concept-review.html` |
| How to review it (15-minute route) | `en/03-html-review-guide.md` |
| Source intake (what was present, what was absent, continuation verdict) | `en/00-SOURCE-INTAKE-REPORT.md` |
| Lessons the concept had to overcome | `en/01-current-work-lessons.md` |
| Research and direction synthesis (the decision document) | `en/02-research-and-direction-synthesis.md` |
| Five specialist reports | `subagents/01…05-*.md` |
| Measured contrast pairings (34 pairs, gate PASS) | `supporting/measured-contrast-pairs.md` |
| QA screenshots (10 verification captures) | `supporting/qa-screenshots/` |
| Delivery manifest | `metadata.yml` |

**Source intake status, stated honestly:** the three expected source packages (`micro-agent-input.zip`, `micro-recovery-docs.zip`, `MicroPrimitives-anti-reference.html`) were **not present** in the repository. Their absence is documented in the intake report with mitigations; all binding identity constraints came from the task's fixed constraint block (authority level 1), and structure/behavior grounding came from the repository's verified target-state design report and recovery packages. Nothing about the missing files' contents was invented.

## 2. Recommended direction

**A — «دفتر هادئ» The Calm Ledger.** A page of a trustworthy paper ledger: figures lead, hairlines separate, boxes almost never appear; warmth comes from the warm canvas, the terracotta header rule, and typographic craft. Chosen over B «مكتب المالك» (the cockpit direction — reads as a competent generic dashboard) and C «مسار المال» (the flow direction — its animated essence violates the binding motion register and its bars fail measured contrast on tinted zones). Adversarial ranking: **A 28/30 · C 18/30 · B 16/30**. C's verifiable ideas (the relationship bar with the hatched deposit bracket, the segmented composition row) and B's live status line were merged into A.

## 3. What you must compare

1. **The three directions** (Mode → «مقارنة الاتجاهات» in the HTML): A is the live concept; B and C are static single-frame previews with their rules and rejection reasons. Judge whether A is genuinely stronger, not merely different.
2. **Arabic RTL vs English LTR**: switch languages and confirm the mirror behaves (chevrons and chart mirror; money and dates never do).
3. **Light vs dark**: both are complete; confirm dark stays warm and the action role stays readable.
4. **Normal vs reduced motion**: run the quiet-save demo in both; confirm reduced motion is a full alternative, not a faster animation.
5. **Widths 320/360/390/430**: confirm the composition survives the narrow device.

## 4. Explicit questions requiring your answer

| # | Question | Why it needs you |
|---|---|---|
| Q1 | **Do you approve direction A (دفتر هادئ) as the Micro visual direction?** If not: reject with focused feedback, or select B/C with the specific properties you want carried into a revision. | This single decision gates all of Stage 4 |
| Q2 | The **center-slot text FAB «سجّل»** (64×48, radius 4, terracotta) instead of a floating circular icon button — do you accept this deliberate, un-generic form? | It is a visible identity decision (synthesis DSY-11) |
| Q3 | The **warm off-white canvas `#faf6f2`** (vs pure white) and the **two-tone dark** (`#1c1815` canvas + `#332d27` surfaces) — do you accept these as platform neutrals? | Neutrals were not fixed by the brand audit; they shape every frame (synthesis §5.1) |
| Q4 | **ASCII digits everywhere** for money and dates (input = display, receipts match paper) — confirm as the v1 numerals decision | Jordanian convention supports it; the alternative (Arabic-Indic display) would re-open every numeric surface |
| Q5 | **RTL time-flow in charts** (earliest at the right, mirrors in EN) — accept as the default, or prefer bank-statement LTR flow? | The RTL flow is the recommendation; real-owner validation is an open question either way |

## 5. Known limitations (do not read past these)

- The three source packages were absent; the concept is grounded in the task's fixed constraints plus the repository's verified design documentation, not in a code-level baseline of the production app.
- Demo writes are in-memory; screens other than live figures hold one scenario snapshot.
- No real-device testing has occurred (no touch hardware, screen readers, or haptics were available); reduced-motion and accessibility were implemented and console-verified only.
- Typography uses the two-font path (Noto Sans Arabic + Inter for tabular digits) with system fallbacks offline; the single-face production decision is a Stage-4 build gate.
- Out-of-scope surfaces (settings, party page, cash closing, assistant, wallet ledger) are named with reasons in `en/02` §4 and committed for Stage 4.

## 6. Waiting for approval

I am **stopped at the review gate**. Until you explicitly approve a direction:

- the final visual package (Stage 4: tokens, component/state contracts, motion system, chart system, content contract, current-work audit, implementation handoff) will **not** be produced;
- the production Micro codebase will **not** be modified;
- the concept is **not** claimed to be production-ready or approved;
- if you reject the direction, I will revise only the requested concept direction and regenerate the HTML review before any finalization.

**How to respond:** open `prototype/micro-visual-concept-review.html`, follow `en/03-html-review-guide.md`, then answer Q1–Q5 above (a short message is enough — e.g. "Approve A; FAB yes; neutrals yes; ASCII yes; RTL flow yes" or "Reject A because …, revise …").
