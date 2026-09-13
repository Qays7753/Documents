# Decision Log

## Current Standard

The approved current basis is Cloud Code Design Wave 2 plus Micro Component Expansion v1. The owner-approved roles are Clay identity/create, interactive Clay chosen/current, warm-ink commitment/value primary, and warm canvas/surface layers.

## Run run-20260913-msv2-zai-01 decisions (Waves 0–C)

Recorded so no silent change exists. All bind to the owner-approved decisions; none opens a rejected direction.

1. **Branch naming** — the execution prompt specifies `micro-standard-v2-execution-20260913`; the upload policy example says `micro-standard-v2-zai-execution-20260913`. Resolved in favor of the owner's execution prompt; discrepancy recorded here and in the run README.
2. **Token backfill** — 62 gallery-consumed custom properties were undefined (borders fell back to `currentColor`; scrim invisible; type/motion degraded). Materialized from the package's own evidence-panel values. This is documentation truthing, not a visual redesign; no new hex value was introduced (audited: 18 approved values, unchanged).
3. **Functional alpha derivatives** — scrim `rgba(20,20,19,0.45)` (warm ink at 45%) and translucent header `rgba(250,249,245,0.86)` (canvas at 86%) are alpha composites of approved base values, disclosed in `color-system.md` and `design-tokens.json`. The retired palette's `rgba(31,30,29,…)` (#1F1E1D) was deliberately not reused. Rationale: `overlay-system.md` requires a scrim; it rendered invisible — a concrete proven defect.
4. **Tint aliases** — `--color-negative-50`, `--color-positive-100`, `--color-primary-100/200` bind to the existing Warm Tint ground and ink values, following the package's own tag tint grammar; no tint hex was invented.
5. **Button ladder** — "primary" is re-scoped to the high-consequence commitment class (filled warm ink). Ordinary save/confirm is a new class on the Warm Tint surface with the `#C96442` pressed edge; create is the Clay class. Legacy `--vf-btn-*` compatibility names are preserved.
6. **Semantic support buttons** — the baseline filled success/info demo buttons placed white text at 3.27:1 / 3.87:1 (AA text failure) and relied on color alone. Restated on the Warm Tint surface with semantic marker icons and text-safe ink; the semantic values themselves are untouched.
7. **Selection grammar** — chips, segmented thumb/underline, and the current-destination nav pill implement the documented "2px `#C96442` edge + non-color cue" (the gallery text already claimed this; the CSS had implemented ink fills). The section header's existing claim is now true.
8. **Gold retirement** — `tag-gold`/`t-gold`/`.gold` demo roles move to the neutral ink pair (`tag-neutral`/`t-neutral`/`.neutral`); the evidence-panel gold ramp note records the retirement. No amber/gold family returns.
9. **Reduced-motion fix** — the gallery motion control set `html[data-motion="reduced"]` with no consuming CSS (a no-op). Added the reduced-motion block honoring both the control and `prefers-reduced-motion`.
10. **Chart example scope** — the Wave B chart is a neutral composition demo of the existing `data-display-system.md` contract (question-led, semantic marks, text alternative, zero/no-data/loading honesty). It introduces no chart library, no product data, and no new palette; Terracotta is never a data color.
11. **S-12 / tool-result anatomy** — remains deferred; not implemented in this run.

## Product boundary

Tools calculate and explain; they do not silently write financial records. Delivery, assistant, multi-device conflict policy, and financial formulas require product implementation decisions outside this visual foundation.

## Final Copy reconciliation decisions

12. **Text-bearing Clay contrast** — the audit found white text on `#D97757` at 3.12:1 while the Gallery rendered a 15px text-bearing Create button. Final Copy separates the roles: text-bearing Create/add uses `#141413`; icon-only FAB/icon buttons retain white icons. This preserves Terracotta identity without using an inaccessible text treatment.

13. **Prototype boundary** — the Prototype remains visual evidence only. It is not a source for Micro product copy, domain behavior, routes, or Final Copy acceptance.

14. **Handoff integrity** — the stale historical `work_branch_head` and file-count claim were removed from the Final Copy manifest. The source head is recorded separately; publication status remains pending until the main merge and remote verification are completed.
