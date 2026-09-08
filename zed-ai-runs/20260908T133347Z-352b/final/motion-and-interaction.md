# Micro — Motion & Interaction

All timings are token values (`tokens.css` §5). Motion law: **no bounce, no springs,
no overshoot, no count-up — the final numeric value appears immediately.** Entrances
use `--ease-standard cubic-bezier(0.2,0,0,1)`; exits use `--ease-exit
cubic-bezier(0.4,0,1,1)`. All overlay motion is vertical/opacity only, which makes it
RTL-safe by construction.

## 1 · Duration scale

| Token | Value | Used by |
|---|---|---|
| dur-press | 80ms | press veil (every pressable) |
| dur-fast | 120ms | segmented thumb, switch dot, checkbox, input border, tab underline |
| dur-normal | 200ms | state swaps, meter fill, scrim |
| dur-sheet-in / out | 240ms / 180ms | bottom sheet |
| dur-dialog-in / out | 160ms / 120ms | centered dialog |
| dur-scrim | 200ms | scrim fade both ways |
| (component) | 0.8s/loop | spinner rotation |
| (component) | 1.2s/loop | skeleton shimmer |

## 2 · Interaction contracts (what the lab actually proves)

| Contract | Behavior | Where demonstrated |
|---|---|---|
| Press | 8% ink veil fades in 80ms on `:active`, fades out on release; never scales/bounces | every `.mc-btn`, tile, row, icon button, nav item |
| Focus | 2px `brand-ink` outline, 2px offset, `:focus-visible` only (mouse users don't get rings) | keyboard-tab through any view |
| Loading (button) | label swaps to spinner + «جارٍ…», size locked, pointer-events off | «حفظ المصروف» cycle; every sheet save |
| Loading (list) | exactly 3 skeleton rows, sunken blocks, 1.2s shimmer, zero layout shift | Components states matrix; retry demo |
| Error → retry | one automatic attempt only; failure shows state with a clear manual «إعادة المحاولة»; retry → skeletons → rows | retry demo (live) |
| Quiet completion | CTA flips to ✓ + «تم …» on positive-tint, persists ~1.1s, sheet then closes; metrics and the operations list update to FINAL values instantly (never count-up); `aria-live` region announces «تم حفظ المصروف · 12.500 د.أ» | save demos (expense/collect/sale/purchase/payment) |
| Sheet | opens 240ms from any trigger (rail tile or matrix button); closes 180ms via ✕, scrim tap, Escape, or drag past 120px; focus → first data field; focus returns to trigger; page scroll locked | 5 sheets |
| Dialog | 160/120ms opacity+8px rise; destructive confirm applies state change + live announcement | «إلغاء الفاتورة؟» |
| Drag dismiss | grabber + sheet header track pointer; sheet follows finger; >120px closes, else springs back (no bounce curve — linear follow) | expense sheet |
| Reduced motion | `data-motion="reduced"` OR system `prefers-reduced-motion: reduce` → all transitions/animations collapse to ≤1ms; sheets/dialogs become opacity fades (state meaning preserved without spatial animation); shimmer freezes | lab toggle «مخفّضة» |

## 3 · RTL & direction safety

Overlay motion is translateY/opacity only (mirroring cannot break it). The rail scrolls
natively RTL with proximity snap; the snapport preserves the 16px start padding
(`scroll-padding-inline-start: 16px`) so Chrome's initial snap cannot scroll the first
tile past its padding — this protects the locked peek geometry (16/56/86/30 device-true).

## 4 · Forbidden register (all absent from the build)

Toast-only completion proof · count-up financial values · fake system status bar ·
page-wide slide transitions · bounce/spring easings · parallax · auto-carousels.
Each was checked at build time (grep + review) and none exists in the code.
