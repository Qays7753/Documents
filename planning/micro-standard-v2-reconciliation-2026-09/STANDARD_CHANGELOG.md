# Standard Changelog — run run-20260914-msv2-reconciliation-01

**Package:** Micro Standard v2 (29 core files + 2 metadata records = 31 files).
**Branch:** `micro-standard-v2-reconciliation-final-20260914` (from Documents/main `864263c`).
**Final-for-review copy:** `planning/micro-standard-v2-reconciliation-2026-09/micro-standard-v2-UPDATED/`.
**Rule honored:** no new palette value, timing value, or geometry value was introduced anywhere; the 18 approved hex values and 2 disclosed alpha derivatives are the complete color universe.

## The 17 changed files and why

| # | File | Why it changed |
|---|---|---|
| 1 | `component-states.md` | **New knowledge-state presentation contract** (confirmed/unconfirmed/incomplete/needs-review/estimated/unknown-magnitude: word + non-color marker + neutral tone, orthogonal to outcomes, distinct from honest voids; register U-05/U-11) + **quiet-feedback variant** (inline/quiet completion as a legitimate channel; Snackbar optional; ink marker on warm-tint surfaces; register U-07). |
| 2 | `component-contracts.md` | Knowledge-state pointer sentence; **period-control variants** (chip + native month/date input; register U-08); row-marker clarification (word + marker primary; stripe hue ≥3:1 vs actual background); **overlay-versus-in-flow guidance** (register U-17). |
| 3 | `navigation-shell.md` | **AUX behavior addendum** (route-kind chrome, keyboard-driven chrome hiding with the never-hide rule, safe-area clearance, context-label suppression, scroll-border behavior, route transition guidance; register U-10). |
| 4 | `motion-interaction.md` | **Route/content transition row** bound to the existing `--motion-normal` 200ms (no new timing; Micro's 260ms not adopted) + rules sentence. |
| 5 | `typography.md` | **Type-floor clarification** (labels ≥13px; 12px non-financial metadata only; financial facts/amounts ≥15px; tertiary 13 mono = non-financial numeric metadata; register U-04). |
| 6 | `iconography.md` | **Icon and RTL adapter guidance** (mirror flags, semantic icon roles, no mandated production library; register U-13). |
| 7 | `README.md` | **Authority ladder** (Standard = contracts; Micro mapping = carrier; Micro docs = guidance; domain/application/storage = meaning/persistence; register U-19) + explicit 29+2 package split. |
| 8 | `MANIFEST.json` | **Split correction** (GAP-46): `file_count: 29` → explicit `31 total = 29 core + 2 metadata` with the metadata files named; `updated_by` records this run. |
| 9 | `RELEASE.md` | Run section: what this release adds (all ten additions + the gallery consistency fixes), and the unchanged foundations. |
| 10 | `verification-report.md` | This run's re-verification record (static audit, 98-token resolution, computed action/tag/label styles, interactions smoke, 24-combo geometry, reduced motion, contrast recomputation) with testing limitations preserved verbatim and the pre-existing spinner-track item disclosed. |
| 11 | `coverage-matrix.json` | New families (`knowledge_states`, `aux_behavior`, `period_variants`, `quiet_feedback`, `overlay_vs_inflow`, `type_floor`, `icon_adapter`), `updated_by`, extended `verification` array; `requires_separate_testing` unchanged. |
| 12 | `decision-log.md` | Append-only decisions **15–22** (knowledge states; AUX + route row; period variants; quiet feedback; overlay vs in-flow; type floor + gallery label migration; contrast bindings + gallery fixes; bottom-nav compression fix). Decisions 1–14 untouched. |
| 13 | `self-critique.md` | Stale "Tag text at 12px" sentence rewritten to the clarified floor; reconciliation-run critique section added (what improved, what was corrected, what stays restrained). |
| 14 | `empty-loading-error-states.md` | **U-18 loading rider**: honest text or skeleton; skeleton optional and scoped (chart loading keeps its recorded basis). |
| 15 | `accessibility.md` | **Surface-specific contrast bindings** (computed): Success/Status meet 3:1 non-text only on Surface (3.27/3.25) and marginally on Canvas (3.10/3.08); below 3:1 on Ground/Recessed (2.96/2.95, 2.81/2.80) — must not serve as marks there; Info on Ground 3.51; Error text-safe 5.46/6.02; text-safe ink ranges recorded. |
| 16 | `color-system.md` | Tint-grammar **application rule** sentence (success/status marks on Surface/Canvas-with-word; Info/Error or neutral ink on Ground/Recessed) cross-referencing `accessibility.md`. |
| 17 | `component-gallery.css` | **Gallery consistency fixes** (proven contradiction class): tag/nav/segment/count words to 13px; tag words in text-safe ink with semantic hue on the leading marker (success/status markers on white Surface); quiet-completion word + check in ink; row amounts in ink with the sign as the direction marker (negative keeps error ink); delta lines at 15px; icon tiles in neutral ink; `.bottomnav` safe-area clearance; bottom-nav compression (`min-width: 44px; flex: 1 1 0` + label ellipsis guard) fixing a proven pre-existing 14px overflow at 320px. No selector, layout rule, or color value added or removed. |

## The 14 unchanged files and why

- `button-system.md`, `surface-system.md`, `visual-direction.md`, `spacing-radius-elevation.md`, `responsive-geometry.md`, `input-system.md`, `data-display-system.md`, `content-guidelines.md`, `overlay-system.md` — no approved addition touches their contracts; the overlay-vs-in-flow guidance lives in `component-contracts.md` (per the audited smallest-safe-set); the chart skeleton basis stays as recorded (scoped by the U-18 rider instead of editing `data-display-system.md`).
- `design-tokens.css`, `design-tokens.json` — the token values are untouched (no new palette, timing, or geometry); `design-tokens.json`'s `updated_by` intentionally stays as-is because the file's content is byte-identical to baseline (decision recorded here per the adversarial review).
- `component-gallery.html`, `component-gallery.js` — all gallery fixes are style rebindings; markup and behavior are unchanged.
- `source-inventory.md` — the core evidence/contract inventory record remains byte-identical; the source basis did not change. The two metadata records are `MANIFEST.json` and `RELEASE.md`.

## Prototype v1 (new, outside the package)

`prototype-v1/` — standalone HTML/CSS/JS visual-validation artifact demonstrating every changed contract with neutral illustrative content; labeled "Visual validation prototype — not product truth"; not part of the 31 and not a source of product truth.
