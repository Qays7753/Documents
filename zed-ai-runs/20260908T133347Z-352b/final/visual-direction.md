# Micro — Visual Direction (Selected)

**Direction name:** «دفء الحانوت / The Warm Counter» — the single selected direction of this run.

## 1 · What the direction is

A warm, composed, practical small-business product: a cream canvas that feels lived-in,
ink-forward typography where the money is the loudest thing on screen, three quiet
surfaces, and one terracotta identity moment per viewport. Energy comes from **meaning**
— semantic states, the single brand action, tabular figures locked into columns, tight
alignment, and 80ms micro-motion — never from decoration. The register is the corner
shop counter (الحانوت): confident, busy, honest, immediately legible.

## 2 · Composition grammar

- **Canvas-first.** The page is `#FAF9F5`; blocks sit directly on it. The primary value
  is never boxed — hierarchy is typographic (32/600 ink-strong), not a card.
- **Loudness ladder** (fixed order): 32px value → 15px labels → one semantic state →
  the single brand moment → everything else muted. A stat-card grid inverts this ladder
  and is rejected.
- **One vertical rhythm.** 16px screen edge, 12px intra-group, 16–24px between blocks,
  32px between sections. Spacing separates content before hairlines ever do (≤3 dividers).
- **The rail, not a grid.** Capture actions live in one horizontal snap rail with the
  first action tinted — a counter-top of taps, not a dashboard.
- **Chrome discipline.** Bottom nav is the only persistent chrome (radius 0,
  edge-to-edge). The top zone is content with the single Avatar entry.

## 3 · Surface logic

Exactly three planes: `canvas` (page) → `surface` (groups, sheets, inputs) →
`sunken` (tracks, chips, icon wells, skeletons). Max two nested levels. No resting
shadows; elevation exists only during overlays (scrim 45% + a derived ink-12% sheet
shadow) and press (ink 8% veil). Semantic tints are statuses, never a fourth surface.

## 4 · Terracotta discipline (the arithmetic)

Per viewport exactly ONE filled brand-family element: **either** a `brand-ink` filled
CTA (white text, 6.1:1) **or** the `brand-tint` rail tile **or** an atmosphere identity
mark (with ink-strong text only — white-on-atmosphere text is forbidden at 3.3:1).
The nav indicator (24×3 bar) and the avatar tint are identity marks, not action
surfaces. Atmosphere never carries body text; `#B4613F` does not exist in this system.

## 5 · Where the energy comes from (and where it must not)

Legitimate: a green «+150.000» next to a «−182.500» (meaning, not paint); the check
that lands in the CTA after «تم الحفظ»; numbers that snap into tabular columns; the
8%-veil press. Forbidden: coloring whole cards for liveliness, a fifth semantic family,
count-up animations, bounce, gradient washes.

## 6 · Anti-drift guardrails

- **Not a SaaS dashboard:** no stat-card grid, no KPI tiles, no sidebar, no top app bar.
- **Not a paper ledger:** no ruled lines, no mono typography as product voice, no
  beige-on-beige monochrome — warmth stays in the ground, decisiveness in the figures.
- **Not an AI gallery:** every example is a working بقالة النور operational truth;
  matrices are inspection surfaces with one-line captions, not poster grids.

## 7 · First-glance test (acceptance)

Within 3 seconds, an Arabic-speaking owner can answer: **كم** (431.100 د.أ — the largest
element), **ماذا تغيّر** (+86.250 عن أمس), **ما يحتاج مني** (the tinted «إضافة بيع» +
the pending «بانتظار» chip), and **أن أثق** (updated state, quiet completion proof).
This test is enforced by the hierarchy ladder, not by reviewer goodwill.

## 8 · Evidence

Rendered and verified in `micro-component-visual-library.html` (Foundation view shows
the token system as real usage; the Test Composition shows the grammar live;
screenshots in `04-user-and-accessibility-review/screenshots/`).
