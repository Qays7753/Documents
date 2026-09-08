# Surface System

## The four-layer depth model

Depth is made of surface contrast first, spacing second, warm shadows last (raw SOP §2). The model has exactly four layers:

| Layer | Surface | Elevation | Contains |
|---|---|---|---|
| 1. Canvas | `#FAF9F5` | none | page background, edge-to-edge regions, alternate rows |
| 2. Raised surface | `#FFFFFF` | E1 | cards, inputs, tiles, nav |
| 2a. Recessed inset | `#F0EEE6` (or canvas) inside a card | none | KPI featured tiles, grouped content, skeletons |
| 3. Floating | `#FFFFFF` | E2 / E3 | sheets, dropdown panels, scrolled header (E2); dialog, FAB, snackbar (E3) |

The rule that keeps the model honest: **never a border and a shadow on the same element** (raw SOP §1:73). Cards float with E1 and no border; inputs and outline buttons define their edge with a 1px border and no shadow; the bottom nav's top border is the single documented exception (it is chrome separation, carries no shadow, and sits against the canvas, not floating above content).

## Card

The workhorse surface: white, 16px radius, 16px padding, E1 shadow, no border (`index.css.source:57–61`). Cards stack with 12px gaps inside 16px screen margins; 24px separates card groups. Content is content-driven — a card grows with its text and never clips. Compact density (optional) reduces padding to 12px.

## Recessed card (KPI featured)

Inherited `.kpi-card-dark` (misleadingly named — it is ivory): `#F0EEE6`, 16px radius, 16px padding, E1 shadow (`index.css.source:155–160`). It hosts the featured KPI anatomy: 13px secondary label, 24–28px mono number in a state color, and a 12px change line. Inner white tiles (12px radius, 16px padding) sit inside it for grouped sub-values — the "ivory with white recess" pattern that replaced the source product's old dark-navy treatment.

## Grouped surfaces

Rows grouped in a card share 1px `border-soft` separators (raw SOP §7.7) with alternating rows on canvas tint; the group is one E1 unit, not several. Dropdown panels and menus are single surfaces (12px radius, E2) with 44px option rows divided the same way. Chips and tags are pill surfaces — outline-only when unselected (1px divider border, white fill), filled when selected.

## Overlay surfaces

Sheets: white, 20px top-only radius, E2, safe-area bottom padding, drag handle 36×5 `divider`. Dialogs: white, 16px radius, E3, centered with the standard scrim. Snackbar: ink `#1F1E1D` (the one dark surface in the system), 16px radius, E3. Scrim: `rgba(31,30,29,0.4)` over everything below `z-scrim`.

## Chrome surfaces

Top bar: canvas-colored at rest; when scrolled, `rgba(250,249,245,0.88)` + `blur(12px)` + E2 — the only translucent surface in the system, existing so content remains visible under persistent chrome. Bottom nav: white, top border 1px `border-soft`, safe-area bottom. Action bar (forms): white or canvas with top border, rising above the keyboard.

## Surface discipline

1. Canvas and recessed surfaces never carry shadows.
2. E1 is the default elevation for content; E2/E3 belong to floating layers only.
3. Do not stack E2 on E2; a floating layer above another uses the z-ladder, not a deeper shadow.
4. Shadows are always warm `rgba(60,50,40,α)` — never black, never colored, never glow.
5. The scrolled-header veil is the only blur; glassmorphism as a general treatment is prohibited.
6. Presentation chrome (the source's `#ECE9E4` desktop stage and cold page shadow) is excluded from the foundation (D-19).
