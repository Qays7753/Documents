# Micro — Color Role Map

All 24 tokens, their roles, and the computed contrast contract. Values are the exact
Micro specification — nothing invented, rounded, or legacy. Light mode only.

## 1 · Token roles

| Token | Value | Role | Used for | Forbidden for |
|---|---|---|---|---|
| brand-atmosphere | #CC785C | visible identity surface / graphic mark | brandmark, nav indicator, identity band (ink text only) | body text, number fills, borders, status |
| brand-tint | #F7EAE4 | brand wash | the ONE tinted QuickActionRail tile, avatar ground | fourth surface system, cards |
| brand-ink | #964E33 | brand text + limited filled CTA | quiet links, focus ring, filled primary button (white text) | general surfaces, numbers, borders |
| on-brand | #FFFFFF | text on brand-ink fill | primary CTA label | text on atmosphere (3.3:1 — forbidden) |
| press-overlay | rgba(31,30,29,.08) | press veil | every pressable | resting decoration |
| canvas | #FAF9F5 | page plane | screen background | cards |
| surface | #FFFFFF | content plane | groups, sheets, dialogs, inputs, nav | page background |
| sunken | #F0EEE6 | recessed plane | tracks, chips, icon wells, skeletons, disabled | text ground for small text |
| ink-strong | #1F1E1D | primary figures | 32px value, titles, active nav | — |
| ink | #33322E | body text | labels, qualifiers | — |
| ink-muted | #6E6A60 | secondary | labels, icons, meta | <14px text |
| ink-subtle | #767265 | tertiary hints | non-pressable hints only | pressable content, sunken ground (4.14:1) |
| ink-disabled | #B7B2A6 | disabled | disabled labels/icons (intentionally sub-AA, non-interactive) | anything interactive |
| line-soft | #EAE6DC | hairline | in-surface dividers (≤3 per composition) | input borders |
| line-strong | #DED9CB | control border | inputs, icon buttons, switch track off | dividers |
| scrim | rgba(31,30,29,.45) | overlay backdrop | sheet/dialog scrim | elevation definition alone (2.96:1) |
| positive / positive-tint | #2E7D57 / #E7EFE7 | cash-in, confirmed, completed, favorable | value color on white; chip = tint + icon + INK text | positive text on its own tint (4.27:1) |
| danger / danger-tint | #B42318 / #F7E7E2 | cash-out, negative, failure, destructive | value color on white; filled destructive CTA; chip tint+icon+ink | — |
| warning / warning-tint | #8A6520 / #F4EDD8 | overdue, threshold, attention | value color on white; chip tint+icon | small text on tint (3.87:1 under press) |
| info / info-tint | #3E5C76 / #E8EDF1 | in-progress, pending decision, neutral operational | value color on white; chip tint+icon | — |

## 2 · Computed contrast contract (WCAG relative luminance, AA)

Measured pairs (full arithmetic in Agent 04's `accessibility-rtl-report.md`;
re-verified at build time):

| Pair | Ratio | Ruling |
|---|---|---|
| ink-strong / canvas | 15.9:1 | PASS |
| ink / surface | 11.2:1 | PASS |
| ink-muted / surface | 5.5:1 | PASS |
| ink-subtle / surface | 4.8:1 | PASS (non-pressable only) |
| positive / surface | 5.0:1 | PASS |
| danger / surface | 6.6:1 | PASS |
| warning / surface | 5.3:1 | PASS |
| info / surface | 7.0:1 | PASS |
| brand-ink / surface | 6.1:1 | PASS |
| white / brand-ink | 6.1:1 | PASS (CTA) |
| ink-strong / brand-atmosphere | 5.0:1 | PASS (atmosphere text rule) |
| brand-ink / brand-tint | 5.2:1 | PASS (tinted tile) |
| danger / danger-tint | 5.6:1 | PASS |
| warning / warning-tint | 4.5:1 | PASS (borderline — icon+ink text pattern preferred) |
| info / info-tint | 5.9:1 | PASS |
| **positive / positive-tint** | **4.27:1** | **FORBIDDEN for text — chips use icon + ink text** |
| **white / brand-atmosphere** | **3.28:1** | **FORBIDDEN for text — ink-strong only over atmosphere** |

## 3 · Pairing rules (binding)

1. Semantic text only on `surface`/`canvas`; on its own tint, semantic appears as ICON
   with ink text (positive especially).
2. Atmosphere carries `ink-strong` text only; `on-brand` white is reserved for the
   `brand-ink` fill.
3. Pressable ink text must sit on `surface` (press veil costs ~0.9:1 on canvas).
4. `ink-disabled` is intentionally sub-AA and always non-interactive.
5. Status is never color-alone: sign + icon + label accompany every semantic use.
6. Color economy per composition: ≤2 semantic families, ≤2 colored numbers, 1 filled
   brand action, 1 tinted tile, ≤3 dividers, ≤2 nested surfaces.

## 4 · Where each pair is demonstrated

Foundation view (`view-foundation`): surfaces trio, brand family, ink ramp, lines, the
four semantic families as realistic chips + values; Verification view: the contrast
table (static) plus the runtime text scans. The Test Composition uses exactly two
families (positive + danger) and two colored numbers (+86.250, −182.500).
