# Variant–State Matrix — Micro Component Library

Agent 03 · Run `20260908T133450Z-16d11` · Maps every SPEC §6.9 family to variants, states, and CSS hooks.

**How to read this matrix**

- **Variant** = static authoring modifier (`.family--variant`).
- **State** = runtime condition. Real hooks: `data-state="…"` (JS-written), pseudo-classes (`:focus-visible`, `:active`, `[disabled]`), ARIA (`aria-checked`, `aria-current`). `.is-*` classes are **exhibit-only mirrors** used in matrix cells to freeze a state visually; they are never set by JS.
- **CSS hook(s)** = the exact selectors the lab stylesheet implements.
- **Must exhibit** = MUST appear visibly in the HTML lab. Per SPEC §6.9 ("the lab must show each family as a visual matrix") and SPEC §8 (buttons with loading/disabled/focused/pressed/quiet-completion; inputs with focus/error/filled/disabled; all ten state-family conditions; sheets/dialogs; charts with text alternatives), **every row below is Yes**. Location key: **L** = Component Library matrix view, **T** = Test Composition, **V** = Verification view.
- `data-tone="positive | danger | warning | info"` carries semantic accent; it maps SPEC wording "negative"→danger and "attention"→warning. Color is always paired with a sign/icon/label, never used alone.
- Tone hook CSS: `[data-tone="positive"] { color: var(--mc-positive); }`, etc.; tints via `background: var(--mc-*-tint)` on chips/notice surfaces.

---

## 1. PrimaryValueBlock (`.primary-value-block`)

| Family | Variant | State | CSS hook(s) | Must exhibit |
|---|---|---|---|---|
| PrimaryValueBlock | default (canvas, number first) | resting | `.primary-value-block` | Yes — T, L |
| PrimaryValueBlock | default, negative direction | sign-led | `[data-tone="danger"]` (sign is primary signal, color secondary) | Yes — L |
| PrimaryValueBlock | `--with-state` | decision-relevant pending | `.primary-value-block--with-state[data-state="pending"]` | Yes — T, L |
| PrimaryValueBlock | `--with-state` | unavailable (never rendered as 0) | `[data-state="unavailable"]` | Yes — L |
| PrimaryValueBlock | default | reduced motion (value appears instantly, no count-up) | no animation hook — value static | Yes — V |

## 2. MetricGroup (`.metric-group`)

| Family | Variant | State | CSS hook(s) | Must exhibit |
|---|---|---|---|---|
| MetricGroup | default (one surface, 2–5 rows) | resting | `.metric-group` + `.metric-row` | Yes — T, L |
| MetricGroup | default | loading (3 skeleton rows) | `[data-state="loading"]` → `.metric-row` skeleton | Yes — L, V |
| MetricGroup | default | partial unavailability | row-level `[data-state="unavailable"]` | Yes — L |

## 3. MetricRow (`.metric-row`)

| Family | Variant | State | CSS hook(s) | Must exhibit |
|---|---|---|---|---|
| MetricRow | neutral | resting | `.metric-row` | Yes — T, L |
| MetricRow | positive | resting | `[data-tone="positive"]` | Yes — L (cash received) |
| MetricRow | negative | resting | `[data-tone="danger"]` + minus sign | Yes — L (expense/cash out) |
| MetricRow | attention | resting | `[data-tone="warning"]` | Yes — L (overdue/threshold) |
| MetricRow | info | resting | `[data-tone="info"]` | Yes — L (in progress) |
| MetricRow | unavailable | unknown ≠ 0 | `[data-state="unavailable"]` | Yes — L |
| MetricRow | — | loading | `[data-state="loading"]` (skeleton) | Yes — V |

## 4. CompactTile (`.compact-tile`)

| Family | Variant | State | CSS hook(s) | Must exhibit |
|---|---|---|---|---|
| CompactTile | comparison-pair member (max one pair/composition) | resting | `.compact-tile` | Yes — T, L |
| CompactTile | `--tinted` | resting | `.compact-tile--tinted` | Yes — L |
| CompactTile | — | loading | `[data-state="loading"]` | Yes — L |
| CompactTile | — | pressed | `:active` / `.is-pressed` (press overlay) | Yes — L |

## 5. OperationalRow (`.operational-row`)

| Family | Variant | State | CSS hook(s) | Must exhibit |
|---|---|---|---|---|
| OperationalRow | supplier purchase (neutral) | resting | `.operational-row` | Yes — T, L |
| OperationalRow | receivable collection | resting, positive | `[data-tone="positive"]` | Yes — L |
| OperationalRow | expense paid | resting, danger | `[data-tone="danger"]` | Yes — L |
| OperationalRow | material threshold | warning | `[data-tone="warning"]` | Yes — L |
| OperationalRow | delivery settlement | decision-critical pending | `[data-state="pending"]` (info cue) | Yes — L |
| OperationalRow | — | completed | `[data-state="completed"]` | Yes — L |
| OperationalRow | — | failed (retry action, no auto-retry) | `[data-state="failed"]` | Yes — L, V |

## 6. QuickActionRail (`.quick-action-rail`)

| Family | Variant | State | CSS hook(s) | Must exhibit |
|---|---|---|---|---|
| QuickActionRail | 5 stable actions, primary first, RTL scroll + snap | resting | `.quick-action-rail` (scroll-snap-type: x proximity; edge fade) | Yes — T, L |
| QuickActionRail | one tinted tile (max) | resting | `.quick-tile--tinted` (brand-tint) | Yes — T, L |
| QuickActionRail | — | pressed | `.quick-tile:active` / `.is-pressed` | Yes — L |
| QuickActionRail | — | focused | `.quick-tile:focus-visible` (2px ring) | Yes — L |
| QuickActionRail | next-item peek cue | responsive | locked geometry — see peek table below | Yes — V (all 4 widths) |

## 7. Button (`.button`)

| Family | Variant | State | CSS hook(s) | Must exhibit |
|---|---|---|---|---|
| Button | `--primary` (brand-ink fill, on-brand text) | resting | `.button--primary` | Yes — T, L |
| Button | `--primary` | loading (label preserved, spinner, 48px target) | `[data-state="loading"]` / `.is-loading` | Yes — L |
| Button | `--primary` | disabled | `[disabled]`, `[data-state="disabled"]` / `.is-disabled` | Yes — L |
| Button | `--primary` | focused | `:focus-visible` / `.is-focused` | Yes — L |
| Button | `--primary` | pressed | `:active` / `.is-pressed` (press overlay 80ms) | Yes — L, V |
| Button | `--secondary` (surface, line-strong border) | resting | `.button--secondary` | Yes — L |
| Button | `--secondary` | disabled | `[disabled]` / `.is-disabled` | Yes — L |
| Button | `--secondary` | focused + pressed | `:focus-visible`, `:active` | Yes — L |
| Button | `--quiet` (text button) | resting | `.button--quiet` | Yes — L |
| Button | `--quiet` | quiet completion (check + "تم" proof) | `[data-state="completed"]` | Yes — L, V |
| Button | `--destructive` | resting + focused | `.button--destructive`, `:focus-visible` | Yes — L |
| Button | `--destructive` | pressed | `:active` | Yes — L |
| Button | `--icon` (icon-only, 44px target) | resting | `.button--icon` | Yes — L |
| Button | `--icon` | disabled | `[disabled]` / `.is-disabled` | Yes — L |

## 8. Input (`.input`)

| Family | Variant | State | CSS hook(s) | Must exhibit |
|---|---|---|---|---|
| Input | `--text` | default / empty | `.input--text` | Yes — L |
| Input | `--text` | focus | `.input-field:focus-visible` / `.is-focused` | Yes — L |
| Input | `--text` | error (+ concise hint + recovery) | `[data-state="error"]` / `.is-error` | Yes — L |
| Input | `--text` | filled (has value; empty ≠ unknown) | `[data-state="filled"]` / `.is-filled` | Yes — L |
| Input | `--text` | disabled | `[disabled]` / `.is-disabled` | Yes — L |
| Input | `--amount` (tabular-nums, د.أ affix, LTR digit span) | resting / filled | `.input--amount` + `.input-affix` | Yes — L |
| Input | `--amount` | error | `[data-state="error"]` | Yes — L |
| Input | `--search` | resting + focus | `.input--search`, `:focus-visible` | Yes — L |
| Input | `--date` (DD/MM/YYYY, bidi-isolated) | resting | `.input--date` | Yes — L |
| Input | `--select` (selection) | resting + disabled | `.input--select`, `[disabled]` | Yes — L |

## 9. Segmented (`.segmented`) · Tab (`.tab`)

| Family | Variant | State | CSS hook(s) | Must exhibit |
|---|---|---|---|---|
| Segmented | default | one option selected | `.segmented-item[data-state="selected"]` (`aria-pressed`) | Yes — L |
| Segmented | default | option disabled | `[data-state="disabled"]` / `[disabled]` | Yes — L |
| Segmented | default | pressed / focused | `:active`, `:focus-visible` (120ms selection move) | Yes — L, V |
| Tab | default | unselected | `.tab-item` | Yes — L |
| Tab | default | selected | `[data-state="selected"]` (`aria-selected`) | Yes — L |
| Tab | default | focused | `:focus-visible` | Yes — L |

## 10. Switch (`.switch`) · Checkbox (`.checkbox`)

| Family | Variant | State | CSS hook(s) | Must exhibit |
|---|---|---|---|---|
| Switch | immediate setting only | off | `.switch[aria-checked="false"]` | Yes — L, V (toggleable) |
| Switch | — | on | `.switch[aria-checked="true"]` | Yes — L, V |
| Switch | — | disabled | `[data-state="disabled"]` / `[disabled]` | Yes — L |
| Switch | — | pressed | `:active` (80ms overlay; reduced motion = instant state change) | Yes — V |
| Checkbox | default | unchecked | `.checkbox input:not(:checked)` | Yes — L |
| Checkbox | default | checked | `input:checked` | Yes — L |
| Checkbox | default | disabled | `input:disabled` | Yes — L |
| Checkbox | default | focused | `input:focus-visible` | Yes — L |

## 11. State family (`.state-notice`) — all ten SPEC §6.8/§6.12/§6.9 conditions

| Family | Variant | State | CSS hook(s) | Must exhibit |
|---|---|---|---|---|
| StateNotice | line-based, icon + one line + optional action | empty | `.state-notice[data-state="empty"]` | Yes — L |
| StateNotice | — | loading | `[data-state="loading"]` (skeleton, static under reduced motion) | Yes — L, V |
| StateNotice | — | error (+ retry action, no auto-retry) | `[data-state="error"]` (danger) | Yes — L, V |
| StateNotice | — | offline / local-save | `[data-state="offline"]` (info) | Yes — L |
| StateNotice | — | decision-critical pending (user wording, not infra language) | `[data-state="pending"]` | Yes — L |
| StateNotice | — | conflict | `[data-state="conflict"]` (warning) | Yes — L |
| StateNotice | — | failed | `[data-state="failed"]` (danger) | Yes — L |
| StateNotice | — | completed | `[data-state="completed"]` (positive) | Yes — L |
| StateNotice | — | cancelled | `[data-state="cancelled"]` | Yes — L |
| StateNotice | — | reversed | `[data-state="reversed"]` | Yes — L |

## 12. Sheet · Dialog · Scrim

| Family | Variant | State | CSS hook(s) | Must exhibit |
|---|---|---|---|---|
| Sheet | default bottom sheet | closed → open | `.sheet[data-state="open"]` (240ms ease-enter) | Yes — L, V (interactive) |
| Sheet | default | open → closed | `[data-state="closed"]` (180ms ease-exit) | Yes — V |
| Sheet | default | drag-to-dismiss (threshold; tap under reduced motion) | pointer drag + `[data-state="closed"]` | Yes — V |
| Sheet | default | focus trap, Escape, focus return | JS module `Micro.components.sheet` + `.sheet:focus-visible` | Yes — V |
| Dialog | `--alert` (informational) | open | `.dialog--alert[data-state="open"]` (160ms) | Yes — L, V |
| Dialog | `--confirm` (no scrim dismiss, no Escape) | open | `.dialog--confirm[data-state="open"]` | Yes — L, V |
| Dialog | `--destructive` (danger confirm) | open + focused action | `.dialog--destructive[data-state="open"]` | Yes — L, V |
| Dialog | any | focus return to invoker | JS module `Micro.components.dialog` | Yes — V |
| Scrim | default | visible / hidden | `.scrim[data-state="visible"]` (200ms fade) | Yes — V |

## 13. Bottom Navigation + integrated top zone (Avatar)

| Family | Variant | State | CSS hook(s) | Must exhibit |
|---|---|---|---|---|
| BottomNavigation | 4 destinations + labelled More (labels fit at 320px) | active item | `.nav-item[aria-current="page"]` | Yes — T, L |
| BottomNavigation | — | inactive items | `.nav-item` | Yes — T, L |
| BottomNavigation | — | pressed | `.nav-item:active` (press overlay) | Yes — L, V |
| BottomNavigation | — | reduced motion (no spatial slide) | `html[data-motion="reduced"]` | Yes — V |
| TopZone / Avatar | integrated into page content (not a detached bar) | resting | `.top-zone`, `.avatar` | Yes — T |

## 14. Chart primitives (time axis stays LTR; Arabic labels RTL)

| Family | Variant | State | CSS hook(s) | Must exhibit |
|---|---|---|---|---|
| Chart | `.chart-sparkline` (sparkline) | resting | `.chart-sparkline` (inline SVG, `dir="ltr"`) | Yes — L, T |
| Chart | `.chart-compare` (planned vs actual, texture + direct labels, not color alone) | resting | `.chart-compare` + direct labels | Yes — L |
| Chart | `.chart-target` (target meter) | resting | `.chart-target` | Yes — L |
| Chart | `.chart-trend-marker` (direct-labelled trend marker) | resting | `.chart-trend-marker` | Yes — L |
| Chart | all | text alternative (visible, concise) | `.chart-alt` sibling | Yes — all charts (SPEC §6.13) |
| Chart | all | reduced motion (no draw-in animation) | `html[data-motion="reduced"]` | Yes — V |

---

## QuickActionRail responsive peek table (geometry LOCKED)

Model: full-bleed rail, `padding-inline` 16 (= screen edge), tiles 88×92, tile gap 8, 5 tiles.
Formula: **peek = (W − 16) − (n × 88 + (n − 1) × 8) − 8**, where n = maximum fully visible tiles.

| Viewport width | Full tiles (n) | Next-item peek | Meets ≥28px target? | Notes |
|---|---|---|---|---|
| 320px | 3 | **16px** | No — documented spec exception (SPEC §6.8) | Geometry NOT changed to fake 28px |
| 360px | 3 | **56px** | Yes | (344 − 280) − 8 |
| 390px | 3 | **86px** | Yes | (374 − 280) − 8 |
| 430px | 4 | **30px** | Yes | (414 − 376) − 8; 4 full tiles + 5th peek |

- Tile width (88), tile height (92), tile gap (8), and start padding (16) are **locked at every width**; only the measured peek differs.
- At 430px a rail needs **5 actions** for a next-item cue to exist (4 tiles + 30px peek); the lab rail therefore uses 5 tiles.
- Right-to-left horizontal scrolling with `scroll-snap-type: x proximity` and a subtle canvas edge fade at the inline-end.
- Verification view must report **measured** values per width; overclaiming a universal 28px is prohibited (SPEC §6.8).

---

**Coverage totals:** 14 family groups · ~75 variant/state rows · all rows MUST be visibly exhibited (L/T/V locations above). This file is the coverage checklist for the lab build; `final/coverage-matrix.md` must map each row to an actual HTML location and a verification status ("documented" ≠ "implemented").
