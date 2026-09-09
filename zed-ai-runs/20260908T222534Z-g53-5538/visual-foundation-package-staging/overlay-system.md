# Overlay System

Overlays are the floating layer: E2/E3 surfaces above the shared scrim on the z-ladder (scrim 40 → overlay 50 → snackbar 60). Every overlay shares one interaction contract, inherited from the source sheet: clear scrim, one close path, focus containment + restore, Escape, and body scroll lock while open (SOP §11). The repair run made every documented motion real (R-02) and closed the `[hidden]`/`display` defect that kept dismissed overlays on screen (R-03).

## Bottom sheet (inherited geometry, now with real motion)

| Property | Value |
|---|---|
| Anchor | bottom, full width within its frame; mounts into the screen whose control opened it |
| Surface | white, 20px radius **top corners only**, E2 |
| Snap points | collapsed ≤ 84% height · expanded 94% (class `is-expanded`) |
| Drag handle | 36×5px `divider` pill, 12px/8px vertical padding, `touch-action: none` |
| Header | 20px/700 title + 44px close (12px-radius recessed button), 20px/8px padding |
| Content | 20px side padding, internal scroll, scrollbar hidden |
| Action rows | every action 48px; 1px `border-soft` separators; destructive rows in `negative.600` text |
| Footer actions | Reset (ghost) + Apply (primary), 12px gap, top divider, safe-area bottom padding |
| Motion | **enter 240ms / exit 180ms** `cubic-bezier(.16,1,.3,1)` on transform; height snap 200ms; scrim 200ms (R-01/R-02) |
| Drag | up −50px expands · down +130px collapses or dismisses · −44px clamp when collapsed; transition suppressed during drag (source `BottomSheet.jsx:88–126`) |
| Close paths | scrim tap · header close · Escape · drag-to-dismiss — one stack, top layer closes first |
| Safe area | `env(safe-area-inset-bottom)` on the footer/actions area (R-17) |

Accessibility (inherited from `BottomSheet.jsx` and repaired): `role="dialog"`, `aria-modal="true"`, `aria-label` from the title, focus moves to the first focusable on open, Tab is trapped inside, **focus restores to the trigger on close** (R-07 fixed the capture bug), Escape closes, the page scroll locks while open (R-28).

### The filter sheet (Repair C)

The filter sheet is the canonical sheet use: a compact Filter control (icon + label + count badge) opens it. Groups inside: Status (multiple choice, `aria-pressed` chips), Date range (single choice, radiogroup chips), Type (multiple choice). Selections are **staged** — Apply commits and closes, Reset clears the draft, Cancel/scrim/Escape/drag discards, and reopening stages from the last applied state (R-29). After Apply, the parent shows only the active summary line and the count badge — never a wall of chips. The sort dropdown stays outside the sheet as the one sanctioned compact single-choice control.

## Dialog (normalized gap-fill, D-20; centered, R-30)

The source requires dialogs and confirmations (SOP §9, §11; raw SOP §8.5) but ships no component; the contract is derived strictly from source rules: a centered card (grid anchor, `place-items: center`), white surface, 16px radius, E3 shadow, standard scrim, 20px side padding; `title-sm` 20px/700 title, `body` 15px/1.6 message, then an action row — one filled primary (or destructive for confirmations) + one outline cancel, both 48px, full-width on 320–360. Motion: **scale+fade enter 160ms / exit 120ms** (R-01). Clicking the anchor outside the card closes. Same focus contract as the sheet.

## Menu / dropdown panel (normalized from raw SOP §7.4)

12px-radius E2 panel anchored below its trigger, 44px option rows with 1px `border-soft` separators, selected option = `accent.50` background + `accent.600` 13px/600 text + 20px check glyph in `accent.600` (4.51:1, corrected from the 2.88:1 500-step, R-20). Opens with a 120ms fade+scale (R-02); closes on option select, outside click, or Escape (R-23); focus returns to the trigger. One dropdown per context — never two side by side.

## Scrim

`rgba(31,30,29,0.4)` — ink at 40%, tokenized from four identical inline source usages (D-18). One scrim per overlay stack, mounted into the active screen; never stacked scrims. Scrim tap closes the top overlay (the single close path). Fade: 200ms both directions.

## Snackbar (inherited)

Anchored 24px above the frame bottom, `z-snackbar`, ink `#1F1E1D` surface, 16px radius, E3, 12/16px padding, max-width 448px. Message 15px/500 white (16.64:1); optional action 13px/700 `primary.200` (10.68:1) with a 44px row. **Enter 200ms slide+fade / exit 120ms** (R-01/R-02); auto-dismiss 5000ms + 120ms exit; `role="status"` + `aria-live="polite"`. One snackbar at a time per screen; a new one replaces the old. When the action is reversible, the snackbar carries a **real** Undo that restores the removed DOM node (R-13) — toast-only proof is prohibited.

## Quiet overlays

Toast-like success feedback and the quiet-completion button state are color-structural, not overlay surfaces; they never steal focus or block interaction. Overlays never spawn overlays: a sheet may open a dialog only by closing first (single focus context — the stack enforces one top layer).

## Gallery demonstrations

Sheet (open, drag-to-dismiss, expand snap, header close, action rows), the staged filter sheet (Apply/Reset/Cancel live, rows filter and sort, no-results state appears), centered dialog (open/confirm/cancel/outside-click), dropdown menus (filter sort + input select, Escape + outside close), and the undo snackbar with a real restore — all in both directions, with reduced-motion instant appearances.
