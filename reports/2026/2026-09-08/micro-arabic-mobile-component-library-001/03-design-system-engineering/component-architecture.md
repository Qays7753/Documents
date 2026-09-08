# Component Architecture — Micro Arabic-First Mobile Library

Agent 03 · Design-System & Tailwind v4 Architecture · Run `20260908T133450Z-16d11`
Companion files: `tokens.css`, `tailwind-v4-theme.css`, `variant-state-matrix.md`.

## 1. Purpose and principles

This document defines the architecture of the final HTML lab and the strategy by which a third party later extracts a single component family. The governing principles: **framework-neutral CSS first** (plain custom properties and classes; Tailwind v4 mapping is optional), **Light Mode only** (no `.dark`, no `prefers-color-scheme`), **tokens over literals** (every color/spacing/radius/duration in component CSS comes from `--mc-*`), and **one direction** (no alternate themes). The lab is a verification instrument, not a product: matrices are exempt from the composition budget; only the Test Composition view obeys SPEC §6.10 (one `PrimaryValueBlock`, one `QuickActionRail`, one `MetricGroup`, max three surfaces, one scroll owner).

## 2. File structure

```
final/
├── micro-component-visual-library.html   # lab shell + 4 views (Foundation / Library / Test Composition / Verification)
├── micro-component-visual-library.css    # base behaviors + all component families + .lab-* chrome
├── micro-component-visual-library.js     # vanilla behavior modules, zero dependencies, zero network
└── tokens.css                            # source of truth (spec-exact --mc-* values)
```

CSS internal order: (1) `@import "./tokens.css";` (2) a small **base layer** — font stack, `tabular-nums` rule for financial values, the `:focus-visible` rule, the press-overlay base, `.icon-mirror`, and `html[data-motion="reduced"]` overrides; (3) component families, each wrapped in `/* ===== .family — deps: … ===== */` markers; (4) `.lab-*` chrome last so it can never bleed into extraction. JS registers modules on `window.Micro.components` (`sheet`, `dialog`, `segmented`, `switch`, `list`, `motion`) and binds via data attributes — no framework, no build step, no remote runtime.

## 3. Class naming conventions

Kebab-case throughout, mirroring SPEC §6.9 family names. Pattern: `.family` root, `.family-child` elements, `.family--variant` modifiers. One documented deviation: the State family root is `.state-notice` (a bare `.state` class is too collision-prone for extraction).

| Family | Root | Variants (`--`) | Elements |
|---|---|---|---|
| PrimaryValueBlock | `.primary-value-block` | `--with-state` | `.primary-value`, `.primary-label`, `.primary-qualifier` |
| MetricGroup | `.metric-group` | — | `.metric-group-title`, `.metric-row` |
| MetricRow | `.metric-row` | tone via `data-tone` | `.metric-row-label`, `-value`, `-qualifier` |
| CompactTile | `.compact-tile` | `--tinted` | `.compact-tile-label`, `-value` |
| OperationalRow | `.operational-row` | tone via `data-tone` | `.operational-row-icon`, `-title`, `-amount`, `-meta` |
| QuickActionRail | `.quick-action-rail` | — | `.quick-tile`, `.quick-tile--tinted`, `.quick-tile-icon`, `.quick-tile-label` |
| Button | `.button` | `--primary --secondary --quiet --destructive --icon` | `.button-icon`, `.button-spinner` |
| Input | `.input` | `--text --amount --search --date --select` | `.input-label`, `.input-field`, `.input-affix`, `.input-hint` |
| Segmented / Tab | `.segmented` / `.tab` | — | `.segmented-item`, `.tab-item` |
| Switch / Checkbox | `.switch` / `.checkbox` | — | `.switch-thumb`, `.checkbox-box` |
| State family | `.state-notice` | state via `data-state` | `.state-notice-icon`, `-text`, `-action` |
| Sheet / Dialog / Scrim | `.sheet` / `.dialog` / `.scrim` | `--alert --confirm --destructive` (dialog) | `.sheet-handle`, `-title`, `-body`, `-footer`; `.dialog-title`, `-body`, `-actions` |
| Bottom Navigation | `.bottom-navigation` | — | `.nav-item`, `.nav-icon`, `.nav-label`; top zone `.top-zone`, `.avatar` |
| Charts | `.chart-sparkline`, `.chart-compare`, `.chart-target`, `.chart-trend-marker` | — | `.chart-alt` (text alternative) |

## 4. Variant and state hook strategy

Three mechanisms, never mixed:

- **Variants** are static `--modifier` classes chosen at authoring time (e.g. `.button--destructive`).
- **Dynamic states** are a single `data-state` attribute: `loading | disabled | error | filled | empty | offline | pending | conflict | failed | completed | cancelled | reversed | unavailable | open | closed | selected | visible`. JS is the only writer of `data-state`, and mirrors native semantics where they exist (`aria-busy`, `aria-checked`, `aria-current`, `aria-expanded`). Semantic accent is a separate `data-tone="positive | danger | warning | info"` attribute so state and tone compose independently; color is always paired with a sign, icon, or label (never color alone).
- **`.is-*` exhibit classes** (`is-pressed`, `is-loading`, `is-error`, `is-disabled`, `is-focused`, `is-open`) exist ONLY inside matrix cells to freeze states that cannot be triggered on demand. JS never sets them; extraction consumers never use them. Interactive examples must additionally demonstrate the real, triggerable behavior (SPEC §8).

## 5. RTL strategy

`<html dir="rtl" lang="ar">` is the default; a geometry-only LTR check exists in the Verification view. Component CSS uses **logical properties only** — `padding-inline`, `margin-inline-start`, `inset-inline-end`, `border-inline`, `text-align: start` — and contains no physical `left/right` declarations, so the same sheet renders correctly in both directions. Directional icons (back chevron, forward arrow, list chevrons) carry an explicit `.icon-mirror` class; the single rule `html[dir="rtl"] .icon-mirror { transform: scaleX(-1); }` is the entire mirror registry. Semantic/object icons (plus, trash, receipt, wallet, check, calendar) never mirror. No paper-plane send icon exists. Numbers, dates, percentages, and mixed currency strings are isolated with `<bdi>` or `dir="ltr"` spans; charts set `dir="ltr"` internally while their Arabic labels remain RTL (SPEC §6.13).

## 6. Typography: rem components, px chrome

Component typography consumes the `--mc-type-*-size-rem` aliases (2rem / 0.9375rem / 0.8125rem = 32 / 15 / 13px at a 16px root) while tokens.css keeps the px values as the declared source of truth. Lab chrome (`.lab-*`) and all geometry locks (tiles, targets, rail) stay in px. The Verification view scales `html { font-size: 16 → 20.8 → 32px }` to prove 100/130/200% text scaling: text grows, frames and tile geometry hold, and rail labels clamp to two lines. Known limitation: the rem bridge is a manual px÷16 sync documented in tokens.css.

## 7. Focus and press contracts

**Focus:** `:focus-visible { outline: 2px solid var(--mc-brand-ink); outline-offset: 2px; }` applied via one base-layer rule so every interactive family inherits it. The ring draws outside the component over canvas/surface/tints, where `#964E33` holds ≈6.3–6.8:1 contrast. Mouse focus (`:focus:not(:focus-visible)`) suppresses the ring; outlines are never removed without this replacement. Focus order follows DOM order, which is the visual RTL order.

**Press:** one shared base — a `::after` overlay with `background: var(--mc-press-overlay)` (`rgba(31,30,29,.08)`, never `#B4613F`), `border-radius: inherit`, `pointer-events: none`, fading in over `var(--mc-motion-press)` (80ms) with `var(--mc-ease-standard)` on `:active`. The ink overlay works over any fill, including brand surfaces. Matrix cells also show `.is-pressed` for the frozen treatment.

## 8. Motion and reduced motion

Every transition uses a token pair (duration + easing) from SPEC §6.11: press 80ms, fast 120ms, normal 200ms, sheet in/out 240/180ms, dialog in/out 160/120ms, scrim 200ms. Easing: standard `cubic-bezier(0.2,0,0,1)` for presses and fades; enter `cubic-bezier(0.05,0.7,0.1,1)` for arriving surfaces; exit `cubic-bezier(0.3,0,0.8,0.15)` for leaving surfaces. None overshoots — no bounce, spring, or count-up; final numbers appear immediately. `html[data-motion="reduced"]` (initialized from `prefers-reduced-motion`, also a lab switch) sets transition/animation durations to 0ms for spatial properties: sheets and dialogs appear in place, the scrim is instant, skeletons become static. State **meaning** is preserved — loading, completion, and error indicators still render, just without movement.

## 9. Sheet and dialog contract

Opening a sheet: scrim fades in 200ms, sheet translates up 240ms ease-enter; dialog scales/fades 160ms. Closing reverses with 180/120ms ease-exit. The JS module traps focus (Tab/Shift+Tab wrap inside the layer, opener disabled while open), sets `role="dialog"`/`alertdialog`, `aria-modal="true"`, moves focus to the first meaningful control, and **returns focus to the invoker** on close. Escape and scrim tap dismiss sheets and informational dialogs; destructive `--confirm`/`--destructive` dialogs ignore both and require an explicit choice (safe dismissal). Sheets additionally support drag-to-dismiss with a distance threshold that reduces to a tap under reduced motion.

## 10. Extraction recipe (one family, later, by a third party)

1. Copy `tokens.css` (and `tailwind-v4-theme.css` only if the host project uses Tailwind v4).
2. Copy the family's marked CSS section; its header lists dependencies — always the base layer (focus rule, press base, `.icon-mirror`, reduced-motion rule, ~30 lines) and its JS module if any.
3. Copy the JS module(s) named in the section header; they are self-contained.
4. Copy the family's HTML matrix snippet as the canonical markup example.
5. Verify against `variant-state-matrix.md`: every row's hooks and states must survive the copy.
No family depends on another family's CSS; only tokens and the shared base travel with each extraction.

## 11. Known limitations and handoff

Two elevation levels only; bottom-sheet shadow flips the y sign (documented in tokens.css); 320px rail peek is a documented 16px exception (see matrix); rail label 13px is both a typography role and a geometry lock — at 200% text it wraps to two lines inside the locked 88px tile, pending Agent 04's verdict; the rem bridge requires manual sync. Handoff to Agent 05: build the four code files directly from this architecture, consume `--mc-*` exclusively, and use the variant-state matrix as the coverage checklist.
