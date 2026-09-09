# Visual Foundation Package — README

A neutral, implementation-ready mobile visual foundation normalized from the read-only source pack `accounting-visual-foundation-source-pack-v1` (evidence preserved, direction preserved, measured defects corrected) — **and repaired** by run `20260908T222534Z-g53-5538`, which closed the usability, density, alignment, state, interaction, motion, accessibility, and documentation gaps found by a fresh four-auditor wave. Built by a five-audit, one-synthesis pipeline in the original run and a four-audit, one-synthesis repair pass; every decision is classified and evidenced. Nothing here assumes the original repository.

## Open the gallery

Open `component-gallery.html` directly from this folder (double-click, or `file://…/component-gallery.html`). Keep the three gallery files and `design-tokens.css` together. It runs fully offline: no server, no build tool, no framework, no network requests, no remote fonts. Use the header controls to switch viewport width (320/360/390/430), direction (LTR/RTL), **text scale (100/130/200%)**, and motion (normal/reduced); the **Evidence** button opens the documentation panel with the measured contrast table, ramps, and geometry — technical content lives there, never inside the component frames.

What to try in the gallery: tap the **Filter** control and stage choices before applying (Cancel and drag-away discard them); drag the sheet handle down to dismiss or up to expand; tap the **loading** button twice to feel the duplicate-submit guard; remove a row and press **Undo** (a real restore, not a message); press **Simulate update** and watch the bar move while the numbers land immediately; submit the recovery form empty, then fix it in place; drag the quick-action rail and note the peeking next card.

> Font note: the gallery intentionally falls back to system fonts so it can run offline. Production apps must self-host and preload IBM Plex Sans Arabic and IBM Plex Mono; the gallery's type rendering is a documented approximation, not the final look.

## Source boundary

- **Source of truth (read-only, never modified):** `accounting-visual-foundation-source-pack-v1/` — its SOP, Tailwind tokens, CSS, component references, and rendered references.
- **This package:** a normalized, product-neutral derivative, repaired in staging and verified before publishing. All product-adjacent labels from the source were replaced with neutral examples (`content-guidelines.md`).
- **Excluded by boundary:** the source's product workflows, its "investor mode" color exception, its app-level behaviors (PIN, history, PWA specifics) — recorded in `decision-log.md` (D-33), not carried in.

## File map (exactly 29 files)

| # | File | What it is |
|---|---|---|
| 01 | `README.md` | this guide |
| 02 | `source-inventory.md` | complete token inventory with file:line evidence + 18 documented source conflicts |
| 03 | `visual-direction.md` | the single direction — what the system is and is not |
| 04 | `color-system.md` | ramps, roles, pairings, measured contrast evidence, prohibited misuse |
| 05 | `design-tokens.css` | all 155 tokens as plain CSS custom properties + base behaviors — usable without any build tool |
| 06 | `design-tokens.json` | machine-readable token records (name, value, role, classification, usage, evidence) |
| 07 | `typography.md` | the 11-role rem scale, Arabic rules, numerals and bidi, the 100/130/200% scale |
| 08 | `spacing-radius-elevation.md` | 4px grid, control geometry, radius family, E1–E3 |
| 09 | `iconography.md` | the outline icon language, the 43-glyph operational registry, RTL mirror rules |
| 10 | `responsive-geometry.md` | 320–430 contract, safe areas, text scaling, density |
| 11 | `accessibility.md` | full measured contrast table, dual-ring focus, touch, non-color cues |
| 12 | `motion-interaction.md` | the 80/120/200/240/180/160/120/200 timing system + interaction grammar |
| 13 | `surface-system.md` | the four-layer depth model + the one divider rule |
| 14 | `button-system.md` | button ladder, the six interaction states, corrections |
| 15 | `input-system.md` | field variants, states, error recovery at the control |
| 16 | `navigation-shell.md` | top bar, bottom nav, identity FAB, action bar |
| 17 | `overlay-system.md` | sheet, filter sheet, dialog, menu, snackbar, scrim — with real motion |
| 18 | `data-display-system.md` | filter pattern, metric compositions, row grid, badges, number formatting |
| 19 | `component-contracts.md` | per-family contracts (anatomy/geometry/states/a11y) |
| 20 | `component-states.md` | the state matrix |
| 21 | `empty-loading-error-states.md` | the four mandatory screen states + recovery |
| 22 | `content-guidelines.md` | neutral copy, numbers, scripts |
| 23 | `component-gallery.html` | the offline gallery |
| 24 | `component-gallery.css` | gallery styling (consumes design-tokens.css) |
| 25 | `component-gallery.js` | gallery interactions (vanilla) |
| 26 | `coverage-matrix.json` | family × state coverage with verification status |
| 27 | `decision-log.md` | 34 original decisions (D-01…D-34) + 33 repair decisions (R-01…R-33) |
| 28 | `self-critique.md` | honest limits and judgment calls |
| 29 | `verification-report.md` | commands, renders, results, manifest, assumptions |

## Inherited vs normalized vs corrected

- **Inherited (65 tokens):** every color value, the 4px grid, control heights, radii, elevation, z-ladder, keyframes, skeleton/snackbar durations, safe-area utilities — the source's spine, untouched.
- **Normalized (78):** renames (`income→positive`, `expense→negative`, `withdrawal→operational`, `returns→gold`), collapsed alias trees, tokenized prose roles, the filter-control pattern, the quick-action rail, local row changes with real undo, dialog/menu timing tokens, dual-ring geometry, drag-to-dismiss.
- **Corrected (11 + record-level):** the run-mandated timing system (80/120/200/240/180/160/120/200 — R-01); overlay motion actually implemented (R-02); the `[hidden]` display bug that kept dismissed overlays on screen (R-03); visible input focus (R-04); the dual focus ring (R-05); the destructive fill → negative.600 `#B42318` (R-19); metric compositions that sum (R-09); wrapping rows (R-10); 130/200% text scaling (R-16); safe areas in code (R-17); the FAB identity restoration (R-18); plus the earlier text-bearing pairing corrections (D-01…D-07). Full evidence: `decision-log.md`, `color-system.md`, `accessibility.md`.
- **Proposed (1):** the 8px relationship-bar track — no source precedent, on the 4px grid, documented.

## Applying the tokens

Link `design-tokens.css` and consume the custom properties (`var(--color-primary-700)`, `var(--radius-card)`, `var(--motion-sheet-in)`, …). Apply the base behaviors from the same file (press, dual focus-visible rings, tnum, bidi isolate, safe areas, reduced motion, the `[hidden]` guard) and follow `component-contracts.md` for anatomy. The JSON is for tooling and audits. TypeScript/theme maps, React components, and Tailwind v4 themes are the receiver's build choices — the CSS is deliberately framework-free.

## Provenance

Original run `20260908T201936Z-g53-252a` · repaired by run `20260908T222534Z-g53-5538` · generated from source commit `9bcf5315ea8f3135d8250e431112e85272aa774c` (source tree `74386cd…`, verified unmodified in both runs). Verification details, command log, and remaining human-review items: `verification-report.md`.
