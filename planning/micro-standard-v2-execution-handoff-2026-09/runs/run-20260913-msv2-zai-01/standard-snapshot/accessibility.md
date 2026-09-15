# Accessibility

The system preserves 44px touch targets (36px visual chips carry an extended hit area), visible focus, RTL logical properties, bidi-isolated numerals, reduced motion, and non-color state signals. Warm ink is used for focus on light surfaces; filled controls use an inset surface ring.

## Contrast constraints (WCAG 2.1, recorded evidence)

| Pair | Ratio | Permitted use |
|---|---|---|
| warm ink `#141413` / canvas `#FAF9F5` | 17.50 | AAA text |
| warm ink `#141413` / surface `#FFFFFF` | 18.43 | AAA text |
| Clay `#D97757` / surface | 3.12 | non-text identity only |
| Clay / canvas | 2.96 | non-text identity only |
| Clay interactive `#C96442` / surface | 3.90 | chosen/current edge only |
| error `#B53333` / surface | 6.02 | text/icon semantic |
| info `#2C84DB` / surface | 3.87 | non-text attention mark |
| status `#1490FF` / surface | 3.25 | non-text reviewed mark |
| success `#629987` / surface | 3.27 | non-text settled mark |
| neutral boundary `#87867F` / surface | 3.65 | interactive boundary |
| surface ring / warm-ink fill | 18.43 | inset focus |
| Clay icon / identity surface | 5.90 | identity glyph pairing |
| warm-ink snackbar / surface text | 18.43 | pass |

Consequently: semantic hues (info, status, success) are non-text marks unless paired with a word in a text-safe ink; Clay is non-text-only when paired with white, while text-bearing Clay controls must use a text-safe dark ink such as `#141413`; state meaning is always carried by word + marker so no state depends on color, and low-ratio hues never carry it alone.

## Focus, states, and verification

Focus is a 2px outline with offset on light controls and an inset surface ring on filled controls; it is never suppressed. Disabled, loading, pressed, and completion states are all conveyed by more than color (icon swap, label persistence, `aria-busy`, past-tense words). Zoom to 200% and 320px width must not create horizontal overflow. Physical-device and screen-reader verification are separate release checks and are not claimed by this package.
