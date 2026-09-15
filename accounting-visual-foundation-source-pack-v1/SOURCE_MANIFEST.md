# Source Manifest — Independent Visual Foundation Pack

## Scope

This pack contains visual and directly felt interaction evidence extracted from one mobile interface system. It is intentionally detached from any product domain. The receiving reviewer must treat it as a neutral visual foundation, not as an application to rebuild.

## Included groups

| Path | Contents | Purpose |
|---|---|---|
| `SOP_VISUAL_ONLY.md` | Neutral visual and interaction rules | Primary human-readable source of truth for the review |
| `source-reference/accounting-sop.source.md` | Raw source SOP from Accounting | Evidence only; extract visual rules and ignore product-specific logic, labels, and workflows |
| `AGENTS.md` | Stable execution boundaries | Keeps the reviewing agent inside the visual-only scope |
| `source-reference/tailwind.config.source.js` | Source color ramps, font families, radii, shadows, spacing, motion tokens | Evidence of the implemented token system |
| `source-reference/index.css.source` | Source CSS for global behavior and visible component styles | Evidence of actual button, field, card, sheet, chip, badge, and accessibility behavior |
| `reference-components/ui/` | Neutral-relevant UI component references | Shows visual anatomy and states of fields, sheets, controls, feedback, and icons; product-specific calendar/diagnostic components were excluded |
| `reference-components/layout/` | Layout component references | Shows top bar, page header, bottom navigation, safe-area, and shell geometry |
| `reference-components/sheets/` | Sheet and action references | Shows bottom-sheet forms, FAB, confirmation surfaces, and interaction composition |
| `rendered-reference/accounting-mockup.html` | Rendered visual reference | Shows the source language in a composed mobile mockup |
| `rendered-reference/accounting-color-identity.html` | Color identity reference | Shows the intended palette and relationships visually |
| `rendered-reference/accounting-mobile-components.html` | Mobile component reference | Shows the source component family and responsive intent |
| `reference-assets/` | Brand/icon files used by the source | Visual asset evidence only |

## Deliberately excluded

The following are intentionally not part of this pack: application pages, routing, contexts, stores, database code, business calculations, product-specific workflows, product-specific copy, environment files, package lock files, test fixtures tied to business logic, Git history, credentials, and unrelated repositories.

## Source limitations to audit

The source implementation may contain aliases, backward-compatibility names, repeated values, product-specific labels inside component references, and component behaviors that require normalization. Treat those as audit inputs, not as unquestionable rules. Preserve the visual intent when correcting them.

## Evidence policy

A source value is authoritative only when it is supported by an actual source file or rendered reference. A suggestion made by an agent must be labeled as `proposed`, not presented as an existing source decision. The final package must distinguish `inherited`, `normalized`, `corrected`, `proposed`, and `unresolved` items.

## Required final package

The receiving agent must create a new output package under `output/<RUN_ID>/`. It must not write into this source pack. The required output package and its 29-file index are defined by the task prompt that will be written after this pack is reviewed.
