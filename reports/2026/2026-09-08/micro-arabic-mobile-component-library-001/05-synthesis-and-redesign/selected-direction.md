# Selected Direction — «دفء الطابون» · Taboun Warmth (Final)

Run `20260908T133450Z-16d11` · Agent 05 · One direction only.

## 1. Character statement

Taboun Warmth is the visual temperature of a working bakery at six in the morning — warm, composed, and already busy. The terracotta `brand-atmosphere` is the fired-clay wall of the taboun: visible exactly once per viewport. The semantic green and red are chalk marks of money actually moving; amber is the shelf threshold that cannot wait; the steel-blue is the delivery van still on the road. The 32px tabular value is the first thing أبو محمد sees — before any container, before any color. It is warm without becoming a beige monochrome, energetic without becoming noisy, and direct because hierarchy is built from size, spacing, and signs before it is ever built from color.

## 2. How the direction is realized (as built)

- **Surfaces**: warmth by deltas, not painted planes — `canvas #FAF9F5` → `surface #FFFFFF` → `sunken #F0EEE6`; strictly two nesting levels; no fourth surface exists. `PrimaryValueBlock` sits directly on the canvas: bigger, not boxed.
- **One brand moment per viewport**: the composition carries the single brand-family tint on the first rail tile (`brand-tint`, `brand-ink` icon); the filled `brand-ink` CTA appears only when a sheet is open (that layer's one filled brand action); the active nav indicator is a 24×3 `brand-atmosphere` bar; the avatar circle is `brand-atmosphere` with ink-strong initials.
- **Budgeted useful energy**: positive/danger pairs inside metrics (sign-first, color second), tinted state chips that are *sentences about money*, one warning clock in the follow-up section, one threshold count in warning. Two semantic families and two colored numbers per composition — never more.
- **Typography**: IBM Plex Sans Arabic 400/500/600; 32px/600/1.15 value; 15px labels; 13px Latin/numeric qualifiers; 14px Arabic floor; tabular lining digits everywhere numbers repeat; English digits; `د.أ` as a separate Arabic node; DD/MM/YYYY.
- **Geometry**: 16px screen edge at all widths; spacing 2–40; radius 6/12/16/24/full with BottomNavigation at 0; touch 44/48; rail geometry locked (88×92 min, gap 8, padding 16, label 13) with measured peeks 16/56/86/30.
- **Motion**: 80ms press ink-overlay, 120ms selection, 200ms state, 240/180ms sheet, 160/120ms dialog, 200ms scrim; no bounce, no spring, no count-up; reduced motion preserves state meaning in place.

## 3. What the direction refuses

Cold blue-white dashboards; card-per-metric galleries; desktop grids; decorative gradients and glassmorphism; dark mode; raw hex or token names inside product surfaces; legends detached from charts; color as the only signal; a fifth competing concept.
