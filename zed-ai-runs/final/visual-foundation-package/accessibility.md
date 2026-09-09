# Accessibility

Accessibility is where the five audits converged hardest: the source's *rules* were excellent (AA intent, non-color cues, focus, touch floors) while its *implementation* had measured gaps (five failing pairings, invisible focus, sub-12px text, sub-44px targets). This package keeps every source rule and closes every measured gap. All ratios are WCAG 2.1, computed with `scripts/sub3-contrast.py` and stored in `agents/sub3/contrast-results.json` (62 pairs); the numbers below survive independent recomputation.

## Contrast evidence — text-bearing pairings

| Foreground | Background | Ratio | AA 4.5 | Use |
|---|---|---:|---|---|
| ink `#1F1E1D` | canvas `#FAF9F5` | 15.80 | ✅ AAA | headings |
| ink | surface `#FFFFFF` | 16.64 | ✅ AAA | headings on cards |
| ink | recessed `#F0EEE6` | 14.33 | ✅ AAA | headings on ivory |
| ink-strong `#33322E` | canvas / surface / recessed | 12.18 / 12.83 / 11.05 | ✅ AAA | body |
| ink-secondary `#6E6A60` | surface / canvas / recessed | 5.39 / 5.12 / 4.64 | ✅ | secondary text everywhere |
| white | primary.700 `#964E33` | 6.11 | ✅ | primary button (corrected) |
| white | primary.800 `#783B28` | 8.55 | ✅ | pressed primary (ratio re-measured, R-33) |
| white | accent.600 `#057B7C` | 5.08 | ✅ | secondary button (corrected) |
| white | positive.500 `#2E7D57` | 5.02 | ✅ | positive filled button |
| white | negative.600 `#B42318` | 8.24 | ✅ | destructive button (corrected R-19; was 500-step 5.29) |
| white | operational.600 `#3E5C76` | 7.01 | ✅ | operational filled button (corrected) |
| white | gold.600 `#8A6927` | 5.08 | ✅ | gold filled button |
| positive.600 `#256A48` | positive.50 `#E4F2EA` | 5.62 | ✅ | positive badge/row (corrected role) |
| negative.600 `#B42318` | negative.50 `#FBE7E6` | 5.53 | ✅ | negative badge/row |
| operational.600 `#3E5C76` | operational.50 `#E8EEF3` | 5.99 | ✅ | operational badge/row |
| gold.700 `#644D1C` | gold.50 `#F6ECCF` | 6.80 | ✅ | gold/progress badge (corrected) |
| accent.600 `#057B7C` | accent.50 `#E3F5F5` | 4.51 | ✅ | selected option, ready badge |
| ink-secondary | recessed | 4.64 | ✅ | closed badge |
| primary.700 | surface | 6.11 | ✅ | active nav icon+label (corrected) |
| ink-secondary | surface | 5.39 | ✅ | inactive nav (corrected from disabled) |
| white | ink `#1F1E1D` | 16.64 | ✅ AAA | snackbar text |
| primary.200 `#E8C9B8` | ink | 10.68 | ✅ AAA | snackbar action |
| gold.600 `#8A6927` | surface | 5.08 | ✅ | gold text on white (corrected) |

Non-text (WCAG 1.4.11, 3:1): accent.500 focus border on surface = 3.24 ✅ · gold.500 icons on surface = 3.36 ✅ · primary.500 identity graphics on surface = 3.28 ✅ (identity FAB and icon-only identity surfaces) · menu check accent.600 on accent.50 = 4.51 ✅ (corrected from 2.88, R-20) · inset surface ring vs dark fills = 5.02–8.24 ✅. Exempt: disabled `#B7B2A6` on surface = 2.11 (inactive controls are exempt per 1.4.3; this is not a license to use it for active content).

**Corrected source pairings** (failures with evidence, now restricted): white on primary.500 3.28 · white on primary.600 4.45 · white on accent.500 3.24 · white on operational.500 4.39 · gold.500 on gold.50 2.85 · gold.500 as text on white 3.36 · positive.500 on positive.50 4.34 · primary.500 nav label 3.28 · disabled-as-inactive-nav 2.11 · source ring `primary/50` on white 1.73. Each restricted role is documented in `color-system.md` and `decision-log.md`.

## Focus visibility (corrected twice — D-07, then R-04/R-05)

The source shipped exactly one focus treatment (a `primary/50` ring measuring **1.73:1 — invisible**) and border-only input focus. The original package unified a 2px accent.600 ring but still suppressed it on inputs (`.input:focus { outline: none }`) and it vanished against dark fills (1.00–1.20:1). The repaired **dual-ring contract**:

```css
:focus-visible { outline: 2px solid var(--color-accent-600); outline-offset: 2px; }
.btn-primary:focus-visible, .fab:focus-visible /* + all dark filled controls */ {
  outline: 2px solid var(--color-surface); outline-offset: -4px;
}
```

accent.600 measures 4.38–5.08:1 on every light surface (canvas, surface, recessed); the inset surface ring measures 5.02–8.24:1 against every legal dark fill. Inputs keep the `accent.500` border shift **and** show the ring — `outline: none` without replacement is prohibited and no longer present. Focus moves into overlays on open and restores to the trigger on close (R-07). Every interactive element in the gallery demonstrates the contract.

## Touch targets

44×44 minimum, enforced (corrected: the source shipped a 40px header action and 28px clear buttons). Chips keep their 36px visual height with an `::after` pseudo-element extending the hit area to 44px (R-26 — the original padding approach measured 36px); segmented buttons are 44px minimum; header control segments use the same extension; snackbar actions reach 44px through row padding; all buttons, inputs, nav items, dropdown options, row chevrons, row remove buttons, rail cards, FAB, and sheet close are 44px+ by construction. Content-driven rows provide generous targets without fixed heights.

## Non-color state cues

Every semantic state pairs color with a sign and an icon (raw SOP §0.7): rows carry `+`/`−` signs and directional icons; badges carry small icons or dots where space allows (normalized — source badges were text-only); errors pair the negative color with an alert icon and message text; selected states pair fill with a check or underline; loading states are structural skeletons, not color pulses alone. Color is never the only signal.

## Typography floors

12px minimum everywhere (11px nav labels and badges corrected; the evidence-panel ramp labels were also lifted from 10px to 12px, R-27); line heights ≥1.3 headings / 1.6 body; no negative letter spacing on Arabic (preserved from source); full zoom support (`user-scalable=no` prohibited, WCAG 1.4.4); rem-based scale so text scaling works end-to-end. The gallery's text control steps **100 / 130 / 200%** (16 / 20.8 / 32px root — R-16); at 200% every rem token doubles (buttons 48→108px) and the layout reflows by wrapping, not clipping.

## RTL and bidi

Base direction handled by `[dir]` with logical properties; directional icons mirror selectively (never globally); numerals are bidi-isolated (`unicode-bidi: isolate` utility) so Latin digits never reorder Arabic text; amount inputs force `dir="ltr"`; end-alignment of numeric columns is preserved in both directions. The gallery's LTR/RTL toggle exercises every family in both geometries.

## Motion

`prefers-reduced-motion` disables all animation and transition (inherited kill-switch, `index.css.source:177–185`), plus a manual reduced-motion mode in the gallery. No motion is essential to state: sheets become instant, skeletons become static blocks, press feedback becomes color-only. Count-up animations are excluded entirely (the neutral SOP forbids them).

## What remains human verification

Screen-reader walkthroughs (VoiceOver/TalkBack roles/labels are specified in the contracts but not audibly tested), real-device safe-area behavior, real IBM Plex font rendering, and color-vision simulation on physical displays. These are declared limits in `verification-report.md`, not claims.
