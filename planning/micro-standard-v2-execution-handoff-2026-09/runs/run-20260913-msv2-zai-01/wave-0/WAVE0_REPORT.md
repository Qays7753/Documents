# Wave 0 Report — Baseline and Rollback

- **Run**: `run-20260913-msv2-zai-01`
- **Branch**: `micro-standard-v2-execution-20260913` (created from verified `main`)
- **Base commit**: `dfa8bf7d7f7a2c01f256d4c77d359c8a5770d60b`
- **Status**: **PASS**

## What was done
1. Verified live remote state via `git ls-remote` + `git fetch` before branch creation: `origin/main` = `dfa8bf7d…` (matches the handoff declaration exactly). `origin/micro-standard-v2-foundation-development` and historical `f64e8616…` confirmed absent from the remote and not used.
2. Created work branch `micro-standard-v2-execution-20260913` from `main` at `dfa8bf7d…`. Zero content modifications inside `micro-standard-v2/` in this wave.
3. Generated the full 31-file inventory (29 core + `MANIFEST.json` + `RELEASE.md`) with per-file SHA-256, byte size, and boundary role: `baseline_inventory.json`, `baseline_sha256.txt`.
4. Recorded the rollback boundary (`rollback_boundary.json`): git-native rollback to `dfa8bf7d…` on this branch; baseline hashes allow per-file verification at any later wave.
5. Recorded main-untouched proof (`main_untouched_proof.json`).

## File-boundary register (summary)
All 31 files are Standard-owned. No file is Micro-owned, Accounting-derived, or Prototype-derived. Roles per file are recorded in `baseline_inventory.json` (`boundary_role`): token sources (`design-tokens.css/json`), contracts (`color/button/component/state/data/input/surface/type/geometry/shell/overlay/motion/icon/a11y/content/direction`), gallery demo trio (`component-gallery.html/css/js`), governance (`decision-log`, `self-critique`, `source-inventory`), verification (`coverage-matrix.json`, `verification-report.md`), metadata (`MANIFEST.json`, `RELEASE.md`, plus package overview `README.md`).

## Concrete baseline findings that motivate the approved delta (evidence, not edits)
1. **62 custom properties** are consumed by `component-gallery.css` but defined nowhere in the package (border-radius, shadows, full type scale, motion, easing, z-index, scrim, tint pairs). Undefined custom properties make declarations *invalid at computed-value time* — borders fall back to `currentColor` (harsh black), the scrim background renders **invisible** even though `overlay-system.md` requires one, and type/motion degrade to browser fallbacks.
2. The gallery's own evidence panel records the operative spec (type scale, 4px grid, radii 12/16/18/20/full, E1–E3, motion table, 13 contrast pairs) — i.e., the values exist inside the package but in the wrong layer, while `typography.md` is 3 lines and `spacing-radius-elevation.md` names no numbers.
3. `--vf-btn-primary-bg: var(--vf-ink)` makes every "primary" demo a filled black surface; the owner-approved action contract requires ordinary save on Warm Tint `#F5F4ED` with a `#C96442` pressed edge and reserves `#141413` fills for high-consequence commitment.
4. The segmented-control section text already claims "the selected/current state uses the current Clay edge role," but the CSS implements ink fills/underlines — intent vs implementation gap; the owner decision (`#C96442` = selected/current/pressed edge and underline) resolves it.
5. The evidence panel's "155 tokens, CSS↔JSON parity verified, zero mismatches" claim is false for the shipped package (44 defined properties in CSS; JSON has 13 roles) — corrected in later waves rather than silently kept.

## Tests (Wave 0)
- `git diff --check` → clean (no content changes yet).
- JSON parse of `MANIFEST.json`, `design-tokens.json`, `coverage-matrix.json` → all valid.
- Branch/base verification → PASS (see `main_untouched_proof.json`).
- Not tested / not claimed: physical device, screen reader (per boundary).

## Wave boundary
Stop condition met: none. Baseline and rollback proven. Waves A–C may proceed on this branch.
