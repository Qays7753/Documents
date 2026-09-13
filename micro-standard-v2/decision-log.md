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

## Reconciliation run run-20260914-msv2-reconciliation-01 decisions (append-only)

Recorded so no silent change exists. All bind to the unified decision register (U-01…U-20); none opens a rejected direction; no new palette value, timing value, or geometry value was introduced.

15. **Knowledge-state presentation contract** (register U-05/U-11) — added to `component-states.md` as a presentation-only tier (word + non-color marker + neutral tone) orthogonal to the outcome matrix; example words («غير مؤكد», «غير مكتمل», «بحاجة لمراجعة», «تقديري», «غير معروف») are examples and remain product-owned; knowledge states never bind Success/Error colors and never collapse the honest voids.
16. **AUX behavior addendum + route transition** (register U-10) — `navigation-shell.md` gains the behavior contract (route-kind chrome, keyboard-driven chrome hiding with the never-hide rule for focused content, safe-area clearance, context-label suppression, scroll-border behavior); `motion-interaction.md` gains a route/content transition row bound to the existing `--motion-normal` 200ms. Micro's 260ms value was deliberately not adopted (no new timing basis).
17. **Period-control variants** (register U-08) — the period chip becomes variant (a); a native month/date-input variant (b) is documented (LTR-isolated entry, 13px label, 44px hit, wrapper focus). Time semantics stay product-owned.
18. **Quiet feedback as a first-class variant** (register U-07) — inline/quiet completion documented as a valid alternative to Snackbar; Snackbar stays optional. On warm-tint quiet surfaces the completion marker renders in ink (the check shape carries the meaning).
19. **Overlay versus in-flow** (register U-17) — consequential confirmation/deletion use Dialog/Sheet; continuous explanation/editing stay in-flow; no wholesale overlay conversion.
20. **Typography floor + gallery label migration** (register U-04) — labels ≥13px; 12px is non-financial metadata only; financial facts ≥15px; tertiary 13px mono disambiguated as non-financial numeric metadata. The gallery's state tags, navigation labels, segment options, and count badges moved from the 12px caption token to the 13px label token accordingly.
21. **Surface-specific contrast bindings + gallery consistency fixes** (computed this run; Agent-3/Agent-5 evidence) — Success `#629987` and Status `#1490FF` meet the 3:1 non-text minimum only on Surface (3.27/3.25) and marginally on Canvas (3.10/3.08); on Ground/Recessed (2.96/2.95, 2.81/2.80) they must not serve as marks. Documented in `accessibility.md`/`color-system.md` and applied in `component-gallery.css`: tag words in text-safe ink with semantic hue on the leading marker (success/status markers on Surface), quiet-completion word/check in ink, row amounts in ink with the sign as the direction marker (negative keeps error ink), delta lines at 15px, icon tiles in neutral ink, `.bottomnav` safe-area clearance. No selector, layout, or color value was added or removed.
22. **Bottom-nav compression fix** (proven pre-existing geometry defect) — the gallery's `.bottomnav` overflowed its demo screen by 14px at 320px even in the baseline (four `min-width: 64px` items exceeded the available 254px; the 64px token is the nav *height* minimum, not an item width). Fixed with `min-width: 44px; flex: 1 1 0` (touch floor preserved) and a `.navlabel` ellipsis guard; re-measured clean across 320/360/390/430 × 100/130/200% × RTL/LTR. Recorded as a gallery-consistency fix under the responsive-geometry no-overflow claim, not a contract change.
