# Accounting Visual Foundation Source Pack v1

## What this is

This is a neutral, product-independent source pack for a professional review of a mobile visual and interaction foundation. It contains the visible design language and directly felt interaction patterns extracted from an existing phone-first system.

The pack is not an application, not a product specification, and not a business-logic repository. It is meant to be given to a design-system reviewer or an AI design agent that must normalize, verify, and document the visual foundation before it is used in another product.

## Read first

Read these files in order:

1. `AGENTS.md` — execution boundaries and safety rules.
2. `SOURCE_MANIFEST.md` — what is included and excluded.
3. `SOP_VISUAL_ONLY.md` — neutral visual and interaction rules.
4. `source-reference/SOURCE_AUDIT_NOTES.md` — source-level items that require verification.
5. `source-reference/tailwind.config.source.js` and `source-reference/index.css.source` — literal implementation evidence.
6. `rendered-reference/` — visual reference documents.
7. `reference-components/` — component anatomy and behavior references.

## What the reviewer should produce later

The receiving task will request a complete neutral UI/UX foundation package, including normalized tokens, typography, spacing, radius, elevation, iconography, button and field systems, component contracts, state matrices, motion rules, an offline component gallery, and evidence-based verification. That package must be written under a new `output/<RUN_ID>/` folder and must not modify this source pack.

## Important interpretation

Preserve the recognizable source visual language. Improve consistency, naming, measurement, accessibility, and implementation clarity. Do not invent a new brand direction merely to appear original. Do not carry product-specific labels, calculations, business workflows, or page maps into the neutral output.

## Source limitations

The source contains implementation aliases, product-adjacent names, and some behaviors that may need normalization. These are review inputs. The receiving reviewer must label each final decision as inherited, normalized, corrected, proposed, or unresolved and provide evidence for corrections.

## Offline and handoff expectation

The final neutral package should be usable by a later designer or engineer without needing access to the original product repository. The component gallery must be self-contained and must render without network access, missing placeholders, or hidden product dependencies.
