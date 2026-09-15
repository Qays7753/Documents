# Measured Color Pairings — HTML Review Artifact

**Delivery:** `micro-visual-product-concept-002` · **Stage:** 2 build gate (synthesis §5.2 DSY-23, integration resolution 8)
**Method:** WCAG 2.x relative-luminance formula computed by script (`scripts/measure_contrast.py`, kept with the delivery source); thresholds: 4.5:1 normal text, 3.0:1 large text / non-text UI.
**Context:** pairings measured against the canvas/surface values from the synthesis token sheet (§5.1).

| Pair | Foreground | Background | Class | Ratio | AA verdict |
|---|---|---|---|---|---|
| L1 body ink on canvas | `#221c18` | `#faf6f2` | text | 15.66:1 | PASS |
| L2 secondary ink on canvas | `#5c5148` | `#faf6f2` | text | 7.17:1 | PASS |
| L3 body ink on surface (sheet) | `#221c18` | `#ffffff` | text | 16.84:1 | PASS |
| L4 secondary ink on surface | `#5c5148` | `#ffffff` | text | 7.70:1 | PASS |
| L5 white label on action #964e33 (btn/FAB) | `#ffffff` | `#964e33` | text | 6.11:1 | PASS |
| L6 quiet action #057b7c on canvas | `#057b7c` | `#faf6f2` | text | 4.73:1 | PASS |
| L7 quiet action #057b7c on surface | `#057b7c` | `#ffffff` | text | 5.08:1 | PASS |
| L8 out-delta / marker #964e33 on canvas | `#964e33` | `#faf6f2` | text | 5.69:1 | PASS |
| L9 emphasis #964e33 on brand-soft #f4e4db | `#964e33` | `#f4e4db` | text | 4.94:1 | PASS |
| L10 chart IN bar #079fa0 on canvas (non-text) | `#079fa0` | `#faf6f2` | non-text | 3.02:1 | PASS |
| L11 chart OUT bar #964e33 on canvas (non-text) | `#964e33` | `#faf6f2` | non-text | 5.69:1 | PASS |
| L12 success mark #057b7c on accent-soft disc #e3f5f5 | `#057b7c` | `#e3f5f5` | text | 4.51:1 | PASS |
| L13 warning #9a6700 on canvas | `#9a6700` | `#faf6f2` | text | 4.53:1 | PASS |
| L14 danger #b3362e on canvas | `#b3362e` | `#faf6f2` | text | 5.61:1 | PASS |
| L15 focus ring #964e33 on canvas (non-text) | `#964e33` | `#faf6f2` | non-text | 5.69:1 | PASS |
| L16 pressed: white on #b4613f (TRANSIENT, press-only) | `#ffffff` | `#b4613f` | press-only | 4.45:1 | n/a (documented) |
| L17 PROHIBITED reference: white on #cc785c | `#ffffff` | `#cc785c` | prohibited | 3.28:1 | n/a (documented) |
| L18 ink on #cc785c brand rule context (non-text adjacency) | `#221c18` | `#cc785c` | non-text | 5.14:1 | PASS |
| D1 body ink #f4e4db on canvas #1c1815 | `#f4e4db` | `#1c1815` | text | 14.25:1 | PASS |
| D2 secondary #c9bdb3 on canvas | `#c9bdb3` | `#1c1815` | text | 9.58:1 | PASS |
| D3 body ink #f4e4db on surface #332d27 | `#f4e4db` | `#332d27` | text | 10.98:1 | PASS |
| D4 secondary #c9bdb3 on surface | `#c9bdb3` | `#332d27` | text | 7.39:1 | PASS |
| D5 action label #1c1815 on #8fd5d6 (btn/FAB) | `#1c1815` | `#8fd5d6` | text | 10.63:1 | PASS |
| D6 accent-text #8fd5d6 on canvas | `#8fd5d6` | `#1c1815` | text | 10.63:1 | PASS |
| D7 warm emphasis #d59172 on canvas | `#d59172` | `#1c1815` | text | 6.82:1 | PASS |
| D8 warm emphasis #d59172 on surface | `#d59172` | `#332d27` | text | 5.26:1 | PASS |
| D9 accent-text #8fd5d6 on surface | `#8fd5d6` | `#332d27` | text | 8.19:1 | PASS |
| D10 chart IN bar #5ec0c1 on canvas (non-text) | `#5ec0c1` | `#1c1815` | non-text | 8.22:1 | PASS |
| D11 chart OUT bar #d59172 on canvas (non-text) | `#d59172` | `#1c1815` | non-text | 6.82:1 | PASS |
| D12 success mark #8fd5d6 on #332d27 disc | `#8fd5d6` | `#332d27` | text | 8.19:1 | PASS |
| D13 warning #e6b455 on canvas | `#e6b455` | `#1c1815` | text | 9.26:1 | PASS |
| D14 danger #ff9d94 on canvas | `#ff9d94` | `#1c1815` | text | 8.82:1 | PASS |
| D15 focus ring #8fd5d6 on canvas (non-text) | `#8fd5d6` | `#1c1815` | non-text | 10.63:1 | PASS |
| D16 secondary text #cc785c on dark canvas (deliberate role) | `#cc785c` | `#1c1815` | text | 5.38:1 | PASS |

## Notes

- `L16` (white on `#b4613f`) is the **press-only transient**: computed 4.45:1 / audit authority ≈4.42:1 — below AA normal, permitted only during the press instant per C-04; never a resting pair and never described as a pass.
- `L17` (white on `#cc785c`, 3.28:1) is measured to **confirm the prohibition** (C-02): the light brand value never carries white text anywhere in the artifact.
- `D16` (`#cc785c` secondary text on the dark canvas, 5.38:1) is the deliberate dark-theme role mapping (C-05), not an inversion.
- Row press tints (`#d59172` 16% over canvas, brand 10% over canvas) are transient interaction feedback; their resting equivalents (L1/D1) carry the text duty.

No resting text or non-text pairing used by the artifact fails its threshold; the two sub-threshold rows are the documented press-only and prohibited-reference pairs. **Gate: PASS.**
