# Navigation Shell

## The shell

The app shell is a phone-portrait column: canvas background, one sticky 56px top bar, scrollable content between chrome, and persistent bottom navigation with safe areas. Fixed chrome stays ≤ ~30% of viewport height (measured 19.7% at 390). Scrolling is the norm; the first viewport shows the key information and the primary action. There is no desktop sidebar, no drawer, and no multi-level nav model (SOP §11).

## Top bar (PageHeader pattern, inherited)

- Sticky, 56px, `z-header`, 16px horizontal padding, 8px vertical padding, safe-area top.
- Flat at rest; when content scrolls beneath: `rgba(250,249,245,0.88)` veil + `blur(12px)` + E2 (IntersectionObserver sentinel pattern, `PageHeader.jsx:62–71`).
- Title at left (logical start): 28px/700, collapsing to 20px/700 in the bar as the large title scrolls away; home variant shows a 44px round identity avatar tile (`primary.100` + 20px primary glyph) + greeting caption + name at `title-sm`.
- Actions at the logical end: max two 44px round buttons — identity actions filled `primary` with white icons (stroke 2.5), quiet actions `recessed` with `ink-secondary` icons (stroke 2). Search, when present, is the icon-expand pattern (44px `recessed` round button → field + cancel).
- One obvious path back when a page has a parent: back chevron at the leading edge (mirrored in RTL).

## Bottom navigation (inherited + corrected)

- Fixed, full width, white surface, top border 1px `border-soft`, min-height 64 + safe-area bottom, `z-scrim` layer, centered max 480px column.
- **3–5 destinations only** — primary destinations, never actions (raw SOP §6). The source's conditional 6th tab is a product behavior, excluded from the neutral shell (D-14).
- Item: 48×64 (min-height 48, focusable, scale 0.97 press, dual-ring focus).
- Active state: 52×32 `primary.100` pill behind a **filled 24px icon** in `primary.700` + 12px/600 label in `primary.700` (filled-active corrected D-15; icon size corrected to 24px, R-27).
- Inactive: outline 24px icon (stroke 1.8) + 12px/600 label in `ink-secondary` (corrected from the disabled color).
- Tabs switch with history-replace semantics (never stack); re-tapping the active tab scrolls to top (product convention documented, not rendered).

## Page header (large title pattern)

Content pages open with the large title (28px/700) in a scrolling subheader row, optionally carrying a segmented control or KPI summary card; only the compact 56px bar is sticky. The title shrinks into the bar when the subheader scrolls past it. 112px is the canonical large-title bar height (source range 112–140, normalized D-08).

## Floating action (FAB)

56×56, 12px radius, **identity fill `primary.500 #CC785C` with a white plus glyph** (24px, stroke 1.5 — non-text 3.28:1 ≥ 3:1, restored from the source's own `bg-primary` FAB, R-18), pressed `primary.600`, E3 shadow, `z-fab`, anchored at the logical end 16px inset, **80px above the nav via `--fab-offset`** (the token is now actually consumed — the original demo overlapped the nav) + safe-area margin. It opens the creation sheet; only one FAB may exist per screen, and it never duplicates a visible primary button.

## Bottom action bar (forms)

Forms with a primary submit pin a 72px (+ safe area) white bar above the nav or in place of it, carrying the single filled primary action full-width minus margins; the bar rises above the keyboard (visualViewport pattern documented) and never overlaps the input in focus.

## Gallery demonstrations

The full shell — top bar (default + scrolled shadow state), bottom nav with four destinations in active/inactive/focused states (3–5 allowed; the gallery demonstrates 4 comfortably at every width), the identity FAB anchored above the nav, and the action bar with safe area — rendered inside the 320/360/390/430 frames in both LTR and RTL with mirrored chrome.
