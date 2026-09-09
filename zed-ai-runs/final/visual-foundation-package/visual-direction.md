# Visual Direction

## The one direction

This foundation is a **calm, warm, operational mobile system**: terracotta identity islands on open ivory surfaces, a cool teal interaction accent, and four strictly separated semantic families, expressed through a compact vertical rhythm, a three-level warm elevation system, and quiet, immediate touch feedback. It must read as a serious native mobile interface — trustworthy without being cold, warm without being decorative, energetic without being loud.

This is the only direction in this package. There are no alternative themes, no dark mode, no user-selectable identity, and no secondary palette. The source pack defines one visual language; this package normalizes it and nothing more. Any future variant would be a new, separately reviewed decision — not an option hidden inside this one.

## Where the energy comes from

A calm system still needs life. Here, energy is structural, not decorative. It comes from five deliberate sources, all preserved from the source language:

1. **Action hierarchy.** Exactly one filled identity action leads each viewport; secondary, outline, and ghost actions step down in emphasis. The hierarchy is instantly readable because the terracotta fill is reserved, never repeated at equal weight, and never decorative.
2. **Purposeful semantic color.** Positive green, negative crimson, cool operational steel-blue, and rare gold appear only where state carries meaning, always paired with a sign and an icon so color is never the only signal. Gold is rare by contract — if gold appears often, it is being misused.
3. **Clear selection.** Selected chips, segmented thumbs, active navigation pills, and focused fields all use the same recognizable grammar: a filled or tinted terracotta/teal state that contrasts with the quiet ivory default, with one active element per control group.
4. **Compact operational rhythm.** 48px controls, 16px screen margins, 12px card gaps, 24px section breaks, content-driven rows with ≥56px height, and a restrained type scale (12–28px) create a dense, workmanlike vertical cadence that feels like a tool, not a magazine.
5. **Responsive feedback and meaningful depth.** An 80ms press-scale (0.97), immediate border-color focus shifts, 120–240ms overlay motion on the run's timing system, and the E1→E2→E3 warm shadow ladder make every touch and every layer change feel physical and intentional.

## Where it must never come from

The source explicitly forbids the following, and this package preserves every prohibition: gradients and glow; glassmorphism as a general treatment; neon or colored shadows; emoji as UI iconography; currency symbols attached to numerals; extended dark terracotta surfaces in the everyday layer; blue-grey neutrals mixed with the ivory system; decorative colored borders; heavy borders combined with shadows on the same element; and a theme switcher of any kind. Terracotta owns the warm hue exclusively — semantic families stay cool or separated so financial meaning never blends with brand identity.

## Surfaces and depth

The everyday world lives on warm ivory (`#FAF9F5`) with white cards raised by E1, ivory recesses (`#F0EEE6`) for grouping and KPI emphasis, and E2/E3 reserved for sheets, dialogs, and floating actions. Depth is created by surface contrast and spacing first, shadows second, and never by borders plus shadows together. The scrolled header may use a translucent ivory veil with blur — that is the only glass-like behavior in the system, and it exists to keep content visible under persistent chrome.

## Numerals and scripts

Numbers are citizens of equal rank: IBM Plex Mono with tabular figures, end-aligned, thousands-comma separated, sign-prefixed (`+` / `−`), bidi-isolated when embedded in Arabic text, and never smaller than 12px. Arabic text uses IBM Plex Sans Arabic with generous line heights (headings ≥1.3, body 1.6–1.8) and never negative letter spacing. Both scripts use one type family each, one icon style, and one set of mirroring rules.

## What "done" looks like

A screen built from this foundation should be recognizable at arm's length: warm paper background, one terracotta action, quiet white cards with semantic accents living inside them, a teal-only focus language, and bottom chrome that respects the safe area. It should feel like it belongs to the same product family as every other screen — because it does. This package's job is to make that family reproducible without the original repository.
