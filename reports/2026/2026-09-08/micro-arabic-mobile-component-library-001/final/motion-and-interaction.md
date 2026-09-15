# Motion & Interaction — Micro Component Library

Run `20260908T133450Z-16d11` · All durations and easings are consumed from `tokens.css` (`--mc-motion-*`, `--mc-ease-*`). Verified values: sheet 240ms in / 180ms out; dialog 160ms in / 120ms out; scrim 200ms; press 80ms; fast 120ms; normal 200ms.

## 1. Motion tokens

| Token | Value | Used by |
|---|---|---|
| `--mc-motion-press` | 80ms | press-overlay fade on every `.pressable` |
| `--mc-motion-fast` | 120ms | selection (segmented/tab/switch), color/opacity state changes |
| `--mc-motion-normal` | 200ms | general state transitions, meter fill |
| `--mc-motion-sheet-in/out` | 240 / 180ms | sheet translateY enter (ease-enter) / exit (ease-exit) |
| `--mc-motion-dialog-in/out` | 160 / 120ms | dialog scale+fade enter / exit |
| `--mc-motion-scrim` | 200ms | scrim opacity |
| `--mc-ease-standard` | cubic-bezier(0.2, 0, 0, 1) | presses, fades, selection |
| `--mc-ease-enter` | cubic-bezier(0.05, 0.7, 0.1, 1) | arriving surfaces |
| `--mc-ease-exit` | cubic-bezier(0.3, 0, 0.8, 0.15) | leaving surfaces |

No curve overshoots 1.0 — bounce and spring are structurally impossible. There is no count-up: financial values render their final text immediately.

## 2. Per-family interaction contracts

**QuickActionRail** — horizontal scroll with `scroll-snap-type: x proximity`; tiles snap with `scroll-snap-align: start` and `scroll-padding-inline: 16px`; press overlay 80ms on each 88×92(min) tile; focus ring on keyboard focus; the first tile opens the quick-entry sheet.

**Button** — press overlay on `:active` (and `.is-pressed` exhibit); loading replaces the label with spinner + «جاري الحفظ…» with stable footprint and `aria-busy`; quiet completion swaps to a positive-tinted check + «تم التسجيل»; disabled blocks pointer and dims via tokens; the interactive flow demo runs loading → completion → reset.

**Sheet** — enters at 240ms ease-enter, exits 180ms ease-exit; scrim fades 200ms; drag handle zone is a 44px hit area with pointer-capture drag that maps downward translation 1:1 and commits dismissal past 72px (8px under reduced motion); Escape and scrim tap request dismissal; a dirty sheet routes through «تجاهل التغييرات؟» before discarding; focus is trapped while open and returned to the invoker on close; completion dwell is 1.6s before auto-close so the proof is seen.

**Dialog** — 160/120ms scale+fade; destructive dialogs are modal (`aria-modal`, Escape and scrim ignored — explicit choice only, `إلغاء` initially focused); alert dialogs (dirty guard) treat Escape as "keep editing".

**Inputs** — focus ring 2px ink-strong; error state uses a danger border + 14px helper with icon and `aria-describedby`; amount fields format to two decimals with grouping on blur; search reveals a 44px clear action that refocuses the input; segmented/tabs/switch update `aria-pressed`/`aria-selected`/`aria-checked` within 120ms.

**State notices** — loading uses 3 pulsing skeleton rows (opacity pulse; static under reduced motion); retry is a single explicit action that transitions the notice to loading then completed; announcements go to a `role="status"` live region.

**BottomNavigation** — seat press overlay; active seat switches with 24×3 atmosphere indicator; «المزيد» opens the destinations sheet; the avatar opens the same unified profile/settings sheet.

## 3. Reduced motion

`html[data-motion="reduced"]` (auto-set from `prefers-reduced-motion`, overridable in the lab) collapses every transition/animation duration to ~0 and stops the spinner rotation and skeleton pulse. Spatial animation disappears; **state meaning survives**: sheets and dialogs appear in place, loading is still labeled, completion still shows the check, errors still show the word. The drag threshold drops to a tap-equivalent 8px so dismissal stays available.

## 4. What motion never does

No bounce, no spring, no overshoot, no count-up of financial values, no page-wide slide transitions, no toast-only completion proof, no hover-only state evidence, no entrance animation for the primary value.
