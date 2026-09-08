# Visual Foundation Package — README

A neutral, implementation-ready mobile visual foundation normalized from the read-only source pack `accounting-visual-foundation-source-pack-v1` (evidence preserved, direction preserved, measured defects corrected). Built by a five-audit, one-synthesis pipeline; every decision is classified and evidenced. Nothing here assumes the original repository.

## Open the gallery

Open `component-gallery.html` directly from this folder (double-click, or `file://…/component-gallery.html`). Keep the three gallery files and `design-tokens.css` together. It runs fully offline: no server, no build tool, no framework, no network requests, no remote fonts. Use the header controls to switch viewport width (320/360/390/430), direction (LTR/RTL), text size (normal/large), and motion (normal/reduced); the **Evidence** button opens the documentation panel with the measured contrast table, ramps, and geometry — technical content lives there, never inside the component frames.

> Font note: the gallery intentionally falls back to system fonts so it can run offline. Production apps must self-host and preload IBM Plex Sans Arabic and IBM Plex Mono; the gallery's type rendering is a documented approximation, not the final look.

## Source boundary

- **Source of truth (read-only, never modified):** `accounting-visual-foundation-source-pack-v1/` — its SOP, Tailwind tokens, CSS, component references, and rendered references.
- **This package:** a normalized, product-neutral derivative. All product-adjacent labels from the source were replaced with neutral examples (`content-guidelines.md`).
- **Excluded by boundary:** the source's product workflows, its "investor mode" color exception, its app-level behaviors (PIN, history, PWA specifics) — recorded in `decision-log.md` (D-33), not carried in.

## File map (exactly 29 files)

| # | File | What it is |
|---|---|---|
| 01 | `README.md` | this guide |
| 02 | `source-inventory.md` | complete token inventory with file:line evidence + 18 documented source conflicts |
| 03 | `visual-direction.md` | the single direction — what the system is and is not |
| 04 | `color-system.md` | ramps, roles, pairings, measured contrast evidence, prohibited misuse |
| 05 | `design-tokens.css` | all 148 tokens as plain CSS custom properties + base behaviors — usable without any build tool |
| 06 | `design-tokens.json` | machine-readable token records (name, value, role, classification, usage, evidence) |
| 07 | `typography.md` | the 11-role rem scale, Arabic rules, numerals and bidi |
| 08 | `spacing-radius-elevation.md` | 4px grid, control geometry, radius family, E1–E3 |
| 09 | `iconography.md` | the outline icon language + RTL mirroring rules |
| 10 | `responsive-geometry.md` | 320–430 contract, safe areas, large text, density |
| 11 | `accessibility.md` | full measured contrast table, focus, touch, non-color cues |
| 12 | `motion-interaction.md` | motion tokens, press/focus/loading/completion grammar |
| 13 | `surface-system.md` | the four-layer depth model |
| 14 | `button-system.md` | button ladder, states, corrections |
| 15 | `input-system.md` | field variants and states |
| 16 | `navigation-shell.md` | top bar, bottom nav, FAB, action bar |
| 17 | `overlay-system.md` | sheet, dialog, menu, snackbar, scrim |
| 18 | `data-display-system.md` | rows, KPI, badges, chips, number formatting |
| 19 | `component-contracts.md` | per-family contracts (anatomy/geometry/states/a11y) |
| 20 | `component-states.md` | the state matrix |
| 21 | `empty-loading-error-states.md` | the four mandatory screen states |
| 22 | `content-guidelines.md` | neutral copy, numbers, scripts |
| 23 | `component-gallery.html` | the offline gallery |
| 24 | `component-gallery.css` | gallery styling (consumes design-tokens.css) |
| 25 | `component-gallery.js` | gallery interactions (vanilla) |
| 26 | `coverage-matrix.json` | family × state coverage with verification status |
| 27 | `decision-log.md` | 34 evidence-backed decisions |
| 28 | `self-critique.md` | honest limits and judgment calls |
| 29 | `verification-report.md` | commands, renders, results, manifest, assumptions |

## Inherited vs normalized vs corrected

- **Inherited (69 tokens):** every color value, the 4px grid, control heights, radii, elevation, motion durations, z-ladder, safe areas — the source's spine, untouched.
- **Normalized (74):** renames (`income→positive`, `expense→negative`, `withdrawal→operational`, `returns→gold`, `background→canvas`, `mute/ivory→recessed`), collapsed alias trees, tokenized prose roles (body 15, label 13, KPI mono), derived dialog/menu/quiet-completion contracts, conflict resolutions that favor the implemented value.
- **Corrected (5 token-level + record-level):** text-bearing pairings moved to passing steps *within the source ramps* — primary button `#CC785C→#964E33` (3.28→6.11:1), secondary `#079FA0→#057B7C` (3.24→5.08), gold badge text `→#644D1C` (2.85→6.80), operational fill `→#3E5C76` (4.39→7.01), nav active `→#964E33` — plus the systemic focus ring, the 12px floor, 44px touch enforcement, rem-based scaling, and zoom un-blocking. Full evidence: `decision-log.md`, `color-system.md`, `accessibility.md`.

## Applying the tokens

Link `design-tokens.css` and consume the custom properties (`var(--color-primary-700)`, `var(--radius-card)`, …). Apply the base behaviors from the same file (press, focus-visible, tnum, bidi isolate, safe areas, reduced motion) and follow `component-contracts.md` for anatomy. The JSON is for tooling and audits. TypeScript/theme maps, React components, and Tailwind v4 themes are the receiver's build choices — the CSS is deliberately framework-free.

## Provenance

Run `20260908T201936Z-g53-252a` · generated from source commit `9bcf5315ea8f3135d8250e431112e85272aa774c` (source tree `74386cd…`, verified unmodified). Verification details, command log, and remaining human-review items: `verification-report.md`.
