# Spacing, Radius, and Elevation

## The 4px grid

The grid is inherited without modification (`SOP_VISUAL_ONLY.md §6`, raw SOP §3): base unit 4px, allowed steps 4 / 8 / 12 / 16 / 20 / 24 / 32, plus two documented named extras — the 52px nav pill (`tailwind.config.source.js:199`) and the 56px FAB basis (`:201`).

| Token | Value | Primary use |
|---|---|---|
| `space.1` | 4px | icon↔text micro gap |
| `space.2` | 8px | label↔field, chip gap, button↔search |
| `space.3` | 12px | **between cards**, control padding, sheet grid gap |
| `space.4` | 16px | **screen edge**, card padding, row padding |
| `space.5` | 20px | wide padding (sheet header/content) |
| `space.6` | 24px | **between major sections** |
| `space.7` | 32px | opening space, empty-state breathing room |

Layout constants (inherited, raw SOP §3:103): screen margin 16 · card gap 12 · section gap 24 · card padding 16 · label-to-field 8. Micro-spacing below 4px is not part of the system; the source's 1–2px usages (badge `py-px`, segmented `gap-1.5`) are normalized to the 4px track or expressed as fixed sub-token geometry (badge padding 4×12, per SOP §7.9).

## Control geometry

| Token | Value | Notes |
|---|---|---|
| `control.height` | 48px | buttons, inputs, sheet action rows |
| `control.height-compact` | 36px | chips (hit area padded to 44) |
| `touch.target` | 44px | **minimum for every interactive element** (corrected: source shipped 40px and 28px cases) |
| `topbar.height` | 56px | compact sticky bar |
| `topbar.height-large` | 112px | large title bar, shrinks to 56 on scroll |
| `nav.height-min` | 64px | bottom nav (source range 56–64, fixed at 64) + safe-area |
| `actionbar.height` | 72px | bottom action bar (range 64–72, fixed at 72) + safe-area |
| `fab.size` | 56px | FAB |
| `fab.offset` | 80px | FAB above nav (80 per `Fab.jsx:39`; mockup's 88 deprecated) |
| `icon.sm` / `icon.md` | 20px / 24px | icon sizes |
| `row.height-min` | 56px | rows are content-driven and may grow (titles wrap + 2-line clamp) |
| `progress.track-height` | 8px | summary-metric relationship bar track [proposed R-14] |

Chrome budget: fixed top + bottom chrome must stay ≤ ~30% of screen height (raw SOP §4) — the source shell measures 19.7% at 390px (A3 audit), leaving ample headroom. Fixed heights are legal only where the content contract is known; rows, cards, sheets, and dialogs are content-driven so Arabic and large text never clip (SOP §6).

## Radius family

One soft-cornered family, inherited intact: **12px controls** (buttons, fields, inner tiles, FAB), **16px cards**, **20px sheets** (top corners only), **18px segmented track** (so the 12px thumb nests visibly inside it — `tailwind.config.source.js:170`), and **full radius** for chips, tags, and badges.

The nested-corner rule from raw SOP §4:135 is preserved: an inner radius equals the outer radius minus the padding between them (a 16px card with 16px padding hosts 12px inner tiles = 16 − 4 ≥ 12; the rendered refs' 16-in-16 stacking is flagged but tolerated as the source's own visual choice for grouped KPI tiles). Pills are for chips/tags/compact controls only — never a default treatment. Square corners, competing radius families, and random rounded containers are prohibited.

## Elevation

Warm shadows only — every shadow is `rgba(60,50,40,α)`, never black, never colored, never glowing (raw SOP §1). Three levels plus one documented micro level:

| Token | Shadow | Role |
|---|---|---|
| `shadow.e1` | `0 1px 2px rgba(60,50,40,.06), 0 4px 12px rgba(60,50,40,.06)` | cards, raised surfaces |
| `shadow.e2` | `0 6px 20px rgba(60,50,40,.10)` | sheets, dialogs' parent layer, scrolled header |
| `shadow.e3` | `0 16px 40px rgba(60,50,40,.16)` | dialogs, FAB, snackbar |
| `shadow.sm` | `0 1px 2px rgba(60,50,40,.04)` | segmented thumb micro-shadow |

Rules preserved from the source: prefer surface contrast and spacing before shadows; never combine a border and a shadow on the same element (the bottom nav's top border is the documented exception — it has no shadow); never put E3 on ordinary cards; the strongest shadow belongs to the floating layer only. The header gains E2 **only when content scrolls beneath it** (IntersectionObserver pattern, `PageHeader.jsx:62–71`) — at rest it is flat.

Deprecated: the rendered-reference sheet variant `0 -4px 24px rgba(60,50,40,.10)` (D-12), the never-used `shadow-nav` token (D-10), and the cold page shadow `rgba(33,36,39,.08)` (presentation chrome, excluded).

## Surface stack

The depth model is four layers (raw SOP §2): canvas `#FAF9F5` → white surface + E1 → recessed ivory insets `#F0EEE6`/`#FAF9F5` inside cards → floating E2/E3. See `surface-system.md` for the full contract.
