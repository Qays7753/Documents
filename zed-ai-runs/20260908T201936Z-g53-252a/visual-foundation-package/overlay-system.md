# Overlay System

Overlays are the floating layer: E2/E3 surfaces above the standard scrim on the z-ladder (scrim 40 → overlay 50 → snackbar 60). Every overlay shares one interaction contract, inherited from the source sheet: clear scrim, one close path, focus containment, and correct dismissibility (SOP §11).

## Bottom sheet (inherited geometry)

| Property | Value |
|---|---|
| Anchor | bottom, full width (within the shell column) |
| Surface | white, 20px radius **top corners only**, E2 |
| Snap points | collapsed ≤ 84vh · expanded 94vh |
| Drag handle | 36×5px `divider` pill, 12px/8px vertical padding, optional "drag to expand" caption |
| Header | 20px/700 title + 44px close (12px-radius recessed button), 20px/8px padding |
| Content | 20px side padding, 32px bottom, internal scroll, `hide-scrollbar` |
| Action rows | every action 48px; 1px `border-soft` separators; destructive rows in `negative.600` text |
| Motion | slide 340ms `cubic-bezier(.16,1,.3,1)`; height 320ms; scrim fade 200ms |
| Drag | up −50px expands · down +130px closes · −44px clamp when collapsed; transition suppressed during drag |
| Safe area | bottom inset padding |

Accessibility (inherited from `BottomSheet.jsx`): `role="dialog"`, `aria-modal="true"`, `aria-label` from the title, focus moved to the first focusable on open, Tab trapped inside, focus restored to the trigger on close, Escape closes (collapsing first if expanded), body scroll locked while open.

## Dialog (normalized gap-fill, D-20)

The source requires dialogs and confirmations (SOP §9, §11; raw SOP §8.5) but ships no component; the contract is derived strictly from source rules: centered card, white surface, 16px radius, E3 shadow, standard scrim, 20px side padding; `title-sm` 20px/700 title, `body` 15px/1.6 message, 24px content gap, then an action row — one filled primary (or destructive for confirmations) + one outline cancel, both 48px, full-width on 320–360. Motion: `scaleIn` 200ms (0.95→1 + fade), reduced-motion instant. Same focus contract as the sheet. Destructive confirmations lead with the destructive filled button and never rely on color alone (alert icon + explicit copy).

## Menu / dropdown panel (normalized from raw SOP §7.4)

12px-radius E2 panel anchored to its trigger, 44px option rows with 1px `border-soft` separators, selected option = `accent.50` background + `accent.600` 13px/600 text + 20px check in `accent.500`. Opens 200ms fade/scale; closes on outside touch or Escape. Same focus containment.

## Scrim

`rgba(31,30,29,0.4)` — ink at 40%, tokenized from four identical inline source usages (D-18). One scrim per overlay stack; never stacked scrims. Scrim tap closes the overlay (the single close path).

## Snackbar (inherited)

Fixed above the nav (96px offset), `z-snackbar`, ink `#1F1E1D` surface, 16px radius, E3, 16/12px padding, max-width 448px, full-width minus 32px margins. Message 15px/500 white (16.64:1); optional action 14px/700 `primary.200` (10.68:1) — "Undo" in the soft-delete pattern. Enter 300ms slide+fade; auto-dismiss 5000ms + 250ms exit; `role="status"` + `aria-live="polite"`. One snackbar at a time; a new one replaces the old.

## Quiet overlays

Toast-like success feedback and the quiet-completion button state are color-structural, not overlay surfaces; they never steal focus or block interaction. Overlays never spawn overlays: a sheet may open a dialog only by closing first (single focus context).

## Gallery demonstrations

Sheet (open, expanded snap, with header and action rows, live drag-handle affordance), dialog (default + destructive confirmation, live trigger), dropdown panel (open state with selected option), and snackbar (triggered live, undo action), all in both directions, with reduced-motion instant appearances.
