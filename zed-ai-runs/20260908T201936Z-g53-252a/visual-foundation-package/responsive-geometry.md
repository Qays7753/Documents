# Responsive Geometry

## Target viewports

The system is phone-first portrait, validated at **320, 360, 390, and 430 CSS pixels** (SOP §2; the raw source designs at 390 with a 360–430 working range — 320 is the accessibility floor this package adds as a hard check). There is no desktop layout, no multi-column dashboard mode, and no horizontal scrolling for primary content; the only horizontal scroller in the system is the chip row. Presentation shells (the source's 480px column and 420px phone frames) are viewer chrome, not layout tokens — the gallery reproduces the mobile geometry at the exact selected width.

## The geometry contract at every width

| Rule | Contract |
|---|---|
| Screen margin | 16px, all sides, all widths |
| Card grid | single column, 12px gaps |
| Two-tile grids | `calc((100vw − 2×16 − 12) / 2)` — 138px tiles at 320, 181px at 430; verified no wrap |
| Bottom nav | 3–5 destinations, equal flex, min-height 64 + safe-area; 5×64=320 fits the floor exactly |
| Chip rows | horizontally scrollable, `hide-scrollbar`, one active chip, never wrapped |
| Rows, cards, sheets | content-driven height — grow for Arabic and large text; no fixed clipping |
| Fixed chrome | top 56 + bottom 64+safe ≤ ~30% of viewport height (19.7% measured at 390) |
| First viewport | primary information + primary action visible without scrolling |

## 320px risk register (measured)

The A3 audit computed the tight cases, and the gallery renders them: a 5-segment segmented control gives ≥54px per segment (fits); the 2-tile KPI grid yields 138px tiles (fits with 24px KPI numerals truncating gracefully via `tnum` end-alignment); 5-destination nav at 64px items consumes the full width (fits, 6 destinations would not — hence the 5-destination cap, D-14); long Arabic titles use `truncate`/`line-clamp` rules rather than mid-word breaks.

## Safe areas

Safe-area behavior is inherited and applied on five surfaces: top bar (`padding-top: env(safe-area-inset-top)`), bottom nav (`padding-bottom: env(safe-area-inset-bottom)`), bottom sheets (inline `paddingBottom: env(safe-area-inset-bottom)`, `BottomSheet.jsx:153`), FAB (`margin-bottom: env(safe-area-inset-bottom)`, `Fab.jsx:40`), and the bottom action bar. Viewports use `viewport-fit=cover` so insets are honored. The system status bar belongs to the OS; the app colors `theme-color` (`#CC785C`) to match the identity.

## Zoom and scaling (corrected)

`user-scalable=no, maximum-scale=1.0` in the source mockup (`mockup:5`) blocks pinch zoom and violates WCAG 1.4.4 — prohibited in this package. The correct contract is `width=device-width, initial-scale=1` with zoom enabled; text scaling is supported through the rem-based scale plus the `.font-large` 17px mode (both demonstrated by the gallery's large-text toggle). `-webkit-text-size-adjust: 100%` prevents OS text inflation from breaking layout while leaving zoom functional.

## Large text

All type tokens are rem-based; `.font-large` raises the root from 16 to 17px, scaling the whole scale ~6%. Controls sized in rem (48px = 3rem) grow with the text so labels never clip; content-driven rows grow and wrap. Verified states: buttons (48→51px), inputs with labels, chips (36→38px with the 44px hit area preserved), nav labels, sheet titles, and KPI numerals — all rendered in the gallery's large-text mode without overflow.

## Density

The optional compact mode (`.density-compact`) reduces card padding 16→12 and row padding for dense data lists (inherited from `index.css.source:21–24`). It is a spacing utility, not a type-scale change, and is orthogonal to large text.

## Scrolling behavior

Scrolling is the norm; fixed chrome stays pinned and content scrolls between top bar and nav (raw SOP §6). The top bar is flat at rest and gains E2 only when content scrolls beneath it. Pull-to-refresh and re-tap-tab-to-top are interaction conventions outside this visual package's scope but their geometry (overscroll containment, `overscroll-behavior-y: none`) is inherited from the source base styles.
