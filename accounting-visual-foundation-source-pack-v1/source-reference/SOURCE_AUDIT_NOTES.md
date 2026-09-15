# Source Audit Notes

This file records source-level observations that the reviewing agent must verify. They are not automatic redesign instructions.

## Confirmed source patterns

- The source uses a warm terracotta identity family with a 50–900 ramp.
- The source uses a teal accent family with a 50–900 ramp and explicit text/light aliases.
- The source separates positive, negative, cool operational, and rare gold semantic families.
- The source uses warm greige neutrals, a white surface, and a recessed ivory area.
- The source includes named font families for Arabic sans and tabular mono numerals.
- The source includes named radius families for controls, cards, sheets, and pills.
- The source includes three main elevation levels plus aliases for cards, sheets, headers, and floating actions.
- The source includes reduced-motion handling, touch-target utilities, safe-area utilities, tabular numerals, and a 0.97 press scale.

## Items requiring audit

### Contrast pairing

The source primary button pairs `#CC785C` with white text. Verify the actual contrast for the intended font size and weight. If the pairing fails the applicable text contrast requirement, preserve the terracotta identity but correct the text-bearing pairing or restrict the source pairing to a role where the contrast is valid. Record the correction explicitly.

### Token aliases

The source contains compatibility aliases such as `primary-tint`, `primary-pill`, multiple background aliases, multiple withdrawal aliases, and repeated shadow aliases. Normalize names in the output without removing the source evidence. The final package must include an alias map and a deprecation decision for each alias.

### Semantic naming

The source uses product-adjacent names such as `income`, `expense`, `withdrawal`, and `returns`. In the neutral output, map these to generic semantic roles while preserving their visual values and relationships. Do not infer a new business meaning.

### Typography completeness

The source defines named title, section, card-title, and caption sizes but also relies on inherited or utility classes for body and numerical roles. Produce a complete typography matrix and identify which values are inherited versus explicit.

### Motion completeness

The source contains keyframes and transition timings. Produce a complete motion table covering default, pressed, focus, loading, enter, exit, sheet, dialog, skeleton, and reduced-motion states. Do not add decorative motion without evidence.

### Component isolation

Some reference components may contain product-specific copy or imports even though their visible structure is reusable. In the final neutral package, replace product-specific content with generic labels and keep the source file only as evidence. Do not copy product logic.

### Responsive evidence

The source must be rendered at 320, 360, 390, and 430 CSS pixels. Record any change in wrapping, clipping, height, or navigation fit. Do not claim responsive parity from a single 390px screenshot.

## Decision labels required in the final output

Every normalized item must be labeled as one of:

- `inherited`: visually preserved from the source.
- `normalized`: same intent, cleaned naming or structure.
- `corrected`: source issue fixed with evidence.
- `proposed`: optional addition not present in the source.
- `unresolved`: requires a human decision or more evidence.
