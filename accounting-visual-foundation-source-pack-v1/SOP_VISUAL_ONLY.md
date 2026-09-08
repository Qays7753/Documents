# Visual Foundation SOP — Neutral Mobile System

## 1. Purpose

This document defines a neutral, mobile-first visual and interaction foundation extracted from an existing production-oriented system. It governs the visible experience only: visual hierarchy, color, typography, geometry, components, states, motion, accessibility, and responsive behavior. It is intentionally independent of any product domain.

The purpose of the review is not to replace the visual language with a new theme. The purpose is to make the existing language coherent, measurable, reusable, accessible, and implementation-ready.

## 2. Platform and viewport

The system is designed for phone-first portrait use. Validate at 320, 360, 390, and 430 CSS pixels. The content must remain usable with large text, Arabic and Latin scripts, RTL and LTR geometry checks, safe-area insets, and reduced motion.

The system must not be presented as a desktop dashboard, a dense desktop table, a web page placed inside a phone frame, or a decorative card gallery. It should read as a native-feeling mobile interface.

## 3. Visual direction

The visual direction is warm terracotta identity, open ivory backgrounds, warm neutral text and surfaces, separated cool semantic accents, and controlled elevation. The system should feel calm and dependable without becoming inert. Energy comes from clear action hierarchy, purposeful semantic color, compact information rhythm, responsive feedback, and depth—not from gradients, glow, decoration, or uncontrolled color variety.

The review must preserve the recognizable visual character of the source while correcting measurable defects. Any proposed change must state whether it is a correction, a normalization, or an optional alternative. Optional alternatives must not silently replace the source direction.

## 4. Color foundation

### Identity

| Role | Source value | Intended use |
|---|---|---|
| Primary terracotta | `#CC785C` | Brand identity, primary visual accent, calm filled identity surfaces, and important links or actions when contrast is verified |
| Pressed terracotta | `#B4613F` | Pressed/active state for primary terracotta treatment |
| Deep terracotta | `#964E33` | Stronger text-bearing action treatment or text/icon role when needed for contrast |
| Soft terracotta | `#F4E4DB` | Light selected or identity-tinted surface |
| Teal accent | `#079FA0` | Interactive accent, selected control, focus, or secondary action when the role is clear |
| Teal text | `#057B7C` | Text or icon on a light teal surface |
| Teal tint | `#E3F5F5` | Light interactive/selected surface |

The reviewer must test each foreground/background pairing. Do not assume that a brand color is automatically suitable for white text. If a pairing fails normal text contrast, preserve the visual role and correct only the foreground/background pairing or restrict the use to non-text graphics.

### Warm neutrals

| Role | Value |
|---|---|
| App canvas | `#FAF9F5` |
| Recessed/ivory area | `#F0EEE6` |
| Surface | `#FFFFFF` |
| Soft border | `#EAE6DC` |
| Strong divider | `#DAD5C8` |
| Disabled | `#B7B2A6` |
| Secondary text | `#6E6A60` |
| Strong text | `#33322E` |
| Primary ink | `#1F1E1D` |

### Semantic colors

| Role | Text/icon | Fill | Light background |
|---|---|---|---|
| Positive | `#2E7D57` | `#A7D8BE` | `#E4F2EA` |
| Negative/danger | `#B42318` | `#DB514C` | `#FBE7E6` |
| Cool operational/withdrawal | `#3E5C76` | `#5B7C99` | `#E8EEF3` |
| Rare gold/return | `#B08532` | `#D6AB38` | `#F6ECCF` |

Semantic color must never be the only state signal. Pair it with sign, icon, label, structure, or another non-color cue. Use no more than two semantic families in one composition unless the component is explicitly a multi-series data visualization.

### Color review rules

Do not add a new color merely to make a screen feel more exciting. A new color requires a unique product-independent role, a foreground/on-color, a tint, pressed/focus behavior, contrast evidence, and a demonstration in the component gallery. Do not use semantic colors as decoration.

## 5. Elevation, surfaces, borders, and shadows

The system uses a small elevation vocabulary. Prefer surface contrast and spacing before shadows. Do not place a shadow and a border on the same element unless the component contract explicitly requires it.

| Level | Shadow | Typical role |
|---|---|---|
| Flat | `none` | Canvas content and edge-to-edge regions |
| Card | `0 1px 2px rgba(60,50,40,.06), 0 4px 12px rgba(60,50,40,.06)` | Raised surface/card |
| Sheet | `0 6px 20px rgba(60,50,40,.10)` | Bottom sheet, floating header when scrolled |
| Modal/FAB | `0 16px 40px rgba(60,50,40,.16)` | Dialog or floating action element |

Do not apply the strongest shadow to ordinary cards. Do not add glow, neon shadow, glassmorphism, or colored shadow. A review may adjust a shadow only if it documents the measured issue and preserves the three-level elevation logic.

## 6. Spacing and dimensions

Use a 4px base unit and the following allowed values: 4, 8, 12, 16, 20, 24, and 32px. Use 16px screen edge padding, 12px between cards, 24px between major sections, and 16px internal card padding unless a component contract says otherwise.

| Element | Target |
|---|---:|
| Minimum touch target | 44 × 44px |
| Standard action/input height | 48px |
| Filter chip height | 36px |
| Small icon | 20px |
| Default icon | 24px |
| Compact top bar | 56px |
| Bottom navigation | 56–64px plus safe-area inset |
| Floating action button | 56 × 56px |
| Screen edge | 16px |

Variable-content rows must remain content-driven. Do not use fixed heights that clip Arabic or large text. Keep fixed dimensions only for controls whose content contract is known.

## 7. Shape language

Use the source radius family: 12px for controls and fields, 16px for cards, 20px for sheets, and full radius for chips/tags. Preserve consistent nested-corner logic: an inner radius should be smaller than the outer radius by the relevant padding relationship.

Do not introduce competing radius families, square corners, excessive pills, or random rounded containers. A pill shape is for a chip, tag, or compact control—not a default treatment for every component.

## 8. Typography and numerals

Use IBM Plex Sans Arabic for interface text and IBM Plex Mono for tabular numerals. Use Latin digits where the source contract calls for them, with tabular numerals and bidi isolation for values, dates, percentages, and mixed-direction strings. Do not use negative letter spacing on Arabic. Keep Arabic line-height generous enough to preserve joining and legibility.

The source scale includes 28px screen title, 20px compact title, 17px section title, 15px card title/body, 13px secondary label, 12px caption, and 24–28px KPI numerals. The reviewer may normalize names and token structure, but must preserve the visual hierarchy unless evidence shows a clipping, contrast, or readability problem.

## 9. Component families

The neutral package must document and demonstrate each family separately:

- Primary, secondary, outline, ghost, destructive, disabled, loading, pressed, focused, and quiet-completion buttons.
- Text, amount, search, select, and multiline fields, including focus, error, disabled, and long-content states.
- Filter chips, tabs, segmented controls, tags, and semantic badges.
- Cards, KPI/value surfaces, grouped surfaces, and content-driven rows.
- Bottom sheets, dialogs, scrims, menus, and confirmation patterns.
- Top bars, page headers, bottom navigation, and floating actions.
- Empty, skeleton/loading, error, retry, no-results, and success feedback.
- Icons and directional RTL mirror rules.

Every family requires a contract containing anatomy, dimensions, tokens, allowed content, states, interaction feedback, accessibility requirements, and one positive example.

## 10. Buttons

Buttons must have a coherent hierarchy. A filled primary action is the highest-emphasis action, a filled secondary action uses the cool accent role, outline is a lower-emphasis action, ghost is a low-emphasis text action, and destructive is reserved for destructive intent. Do not present several filled buttons with equal visual weight in one viewport.

The standard button target is 48px minimum height, 12px radius, 600 font weight, source-consistent horizontal padding, and a 0.97 pressed scale where motion is allowed. Every button must show disabled, pressed, focus, loading, and completion behavior. Loading must prevent duplicate activation. The text and icon must remain readable at large text settings.

## 11. Navigation and overlays

Preserve the source mobile shell geometry and safe-area behavior. The bottom navigation is persistent chrome; sheets and dialogs must have a clear scrim, focus containment, a single close path, and correct back behavior. Do not invent a desktop sidebar or a multi-level navigation model during visual normalization.

## 12. Motion

Use short, purposeful transitions: press feedback near 120ms, regular UI transitions around 150–300ms, and sheet/modal motion matching the source. Avoid bounce, decorative spring, automatic count-up, page-wide slides, or motion that delays the final value. Reduced-motion mode must remove nonessential movement while preserving state clarity.

## 13. RTL and accessibility

Test RTL geometry and directional icon mirroring explicitly. Do not globally flip every SVG. Maintain touch targets of at least 44px, visible focus, readable contrast, non-color state cues, large-text behavior, and content-driven height for Arabic strings.

## 14. Validation requirements

The final review must include:

1. A token inventory with source evidence and normalized names.
2. A geometry matrix for spacing, height, radius, shadow, and touch targets.
3. A component state matrix.
4. A color contrast report for all text-bearing pairings.
5. Offline HTML gallery screenshots at 320, 360, 390, and 430px.
6. RTL/LTR checks, large text checks, and reduced-motion checks.
7. A list of preserved source decisions, corrected source defects, optional proposals, assumptions, and unresolved items.

Completion means the output is internally coherent and evidence-backed. It does not mean that the neutral foundation has been adapted to any particular product.
