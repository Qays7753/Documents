# Wave A Report — Contracts and Token Truthing

- **Run**: `run-20260913-msv2-zai-01` · **Branch**: `micro-standard-v2-execution-20260913`
- **Commit**: `125115d` · **Rollback**: `git reset --hard df4018e` (Wave 0) or `dfa8bf7` (main)
- **Status**: **PASS**

## What changed (12 files) and why

| File | Change | Reason (evidence) |
|---|---|---|
| `design-tokens.css` | Materialized the 62 consumed-but-undefined tokens (type scale, radius set, E1–E3 + sm, motion timings, easing, z-layers, phone geometry, icons, scrim, tint aliases) and added the owner action-contract aliases (`--vf-action-create/save/commit*`, `--vf-btn-save/create-*`). Canonical `--vf-radius-*` plus unprefixed gallery aliases. | 62 custom properties were consumed by `component-gallery.css` but defined nowhere → declarations invalid at computed-value time: borders fell back to `currentColor`, scrim rendered invisible (overlay contract requires one), type/motion degraded. Values come from the package's own evidence panel — none invented. |
| `design-tokens.json` | Added `action_contracts`, `semantic_state_presentation`, `functional_derivatives` disclosure, `type_scale`, `geometry` (topbar/nav/FAB/touch), `elevation`, `motion`; kept all existing keys byte-compatible. | Contracts must be machine-readable and match CSS; parity truthing. |
| `color-system.md` | Added action-role table, tint grammar (`negative-50` = ground + error ink), functional-derivative disclosure, link-ink constraint (value explicitly NOT ratified), restraint rule. | Owner decisions require executable action classes; scrim/header derivatives disclosed as alpha composites of approved values, not new palette. |
| `button-system.md` | Replaced the single "warm-ink primary" ladder with the four named action classes (create/save/high-consequence commit/destructive + secondary/outline/ghost), pressed-edge rules, non-color state rules. | Owner contract: ordinary save must not be a filled black surface; `#141413` fills are reserved for high-consequence commitment. |
| `component-states.md` | Added state presentation matrix (draft/pending/posted/failed/cancelled/reversed/reviewed/partial/due/overdue/unknown) with word + marker + color binding; pressed≠success; quiet completion wording. | Wave A contract list requires success/error/pending/unknown/review distinctions with non-color signals. |
| `component-contracts.md` | Added action contract table, financial value zone slots (label/value/unit/period/delta + three honest voids), period chip contract, operational row slots (optional ≤3px state edge stripe always paired with word). | Owner contract list: amount/value/context/period slots; S-5/S-6/S-8 materialized as neutral slots. |
| `typography.md` | Recorded type scale + numeric hierarchy reconciliation (30/20/15 ladder = 28/24/15/13 mono), caption floor rule, bidi examples. | 3-line file could not produce the verified interface (S-1). |
| `spacing-radius-elevation.md` | Recorded 4px grid, radius table, E1–E3 + sm values. | Values existed only in the gallery evidence panel (S-2). |
| `motion-interaction.md` | Recorded timing table, easing, reduced-motion contract. | Same basis (S-2). |
| `accessibility.md` | Recorded 13-pair contrast table with permitted-use constraints; focus/state non-color rules. | Numeric constraints existed only in evidence panel (S-10); computed values verified to match exactly (see tests). |
| `data-display-system.md` | Added value-zone reference and question-led chart contract: zero = visible 2px baseline mark + label; no-data = word+icon state; loading = skeleton; text alternative required; period binding. | Wave B gallery must demonstrate chart states; contract previously implied but unstated. |
| `empty-loading-error-states.md` | Distinguished unknown result from failure/no-data with presentation rules; pending ≠ success; quiet completion proof wording. | Wave A contract list requires unknown/pending separation. |

## Explicitly NOT changed
`input-system.md`, `surface-system.md`, `iconography.md`, `navigation-shell.md`, `overlay-system.md`, `responsive-geometry.md`, `content-guidelines.md`, `visual-direction.md`, `source-inventory.md`, `README.md`, `RELEASE.md`, `MANIFEST.json`, `coverage-matrix.json`, `verification-report.md`, `decision-log.md`, `self-critique.md`, gallery trio (Wave B scope). No file moved, renamed, added, or deleted (still 31 files).

## Decisions recorded (owner-constraint compliance)
1. **No new hex values** — audit proves the hex set is byte-identical to baseline (18 values, zero additions). `#964E33`, `#5F3120`, `#B79C86`, `#8C7A66` absent; no Teal role; no Dark Mode; Terracotta untouched as identity/create only.
2. **Scrim & translucent header** = alpha composites of approved `#141413` (45%) and `#FAF9F5` (86%), disclosed in `color-system.md` and `design-tokens.json`. The retired palette's `rgba(31,30,29,…)` (#1F1E1D) was deliberately not reused. Rationale: the scrim is *required* by `overlay-system.md` and currently renders invisible — a concrete proven defect; an alpha composite introduces no new hue.
3. **`#3D3D3A`** pre-exists in the baseline token file (pressed warm ink) and is now bound only to the high-consequence pressed state.
4. **Tint aliases** (`--color-negative-50`, `--color-positive-100`, `--color-primary-100/200`) bind to existing ground/surface/ink values, following the package's own tint grammar; no tint hex invented.
5. **Tag text contrast note (pre-existing)**: success-ink-on-ground measures 2.96:1 at tag sizes — below AA text. This grammar predates this run; the non-text-only constraint is now documented, and Wave B state tags place the semantic hue on a marker with text-safe ink for words.
6. **Link-ink role** (S-9): constraint recorded; value decision explicitly left to the owner. No teal ratification.

## Tests (all executed locally)
- `git diff --check` → clean.
- JSON parse `design-tokens.json` → valid; existing keys preserved.
- **Hex audit**: baseline 18 hex values vs current 18 — zero new (`wave_a_tests.json`).
- **Token resolution**: every consumed custom property now resolves (133 defined; 0 unresolved).
- **Contrast**: 19 pairs computed; the 10 documented claims match to the digit (17.50 / 18.43 / 3.12 / 2.96 / 3.90 / 6.02 / 3.87 / 3.25 / 3.27 / 3.65). Ordinary-save pair ink-on-ground = 16.72:1 AAA; commit pair white-on-ink = 18.43:1.
- Gallery runtime smoke test after token changes: no console/page errors; evidence ramps, controls, loading guard, sheet, nav, FAB all functional.
- Not tested / not claimed: physical device, screen reader.

## Wave boundary
Gate passed → Wave B (gallery composition) may proceed. Rollback: `git reset --hard df4018e`.
