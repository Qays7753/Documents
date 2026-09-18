# Evidence and Constraints Map

## Evidence classes

- `CONFIRMED_CURRENT`: observed or measured in the live audit.
- `STANDARD_BACKED`: supported by a formal standard.
- `APPROVED_DECISION`: explicitly approved by the owner.
- `DESIGN_DIRECTION`: professional recommendation to explore.
- `RESEARCH_HYPOTHESIS`: requires user testing.
- `IMPLEMENTATION_HANDOFF`: issue to transfer later to the code track.

## Confirmed foundations to preserve

| Finding | Class | Design implication |
|---|---|---|
| Arabic RTL product with JOD and Latin financial digits | `CONFIRMED_CURRENT` | Test mixed-direction content in every direction. |
| IBM Plex Sans Arabic and mono/tabular numbers are already part of the system | `CONFIRMED_CURRENT` | Use as baseline; replacement needs material proof. |
| “Unknown/incomplete is not zero” logic exists | `CONFIRMED_CURRENT` | Make incomplete state prominent and actionable. |
| Human terms such as لي عند العملاء and عليّ للموردين exist | `CONFIRMED_CURRENT` | Preserve plain-language financial understanding. |
| Five-tab navigation is implemented and approved | `CONFIRMED_CURRENT` + `APPROVED_DECISION` | Do not redesign navigation scope. |
| Existing light primary text contrast is strong | `CONFIRMED_CURRENT` | Retain a strong reading foundation while adding energy. |

## Confirmed or high-confidence current problems

| Problem | Class | Design response |
|---|---|---|
| Quick actions can be obscured by bottom navigation | `IMPLEMENTATION_HANDOFF` | Concept must keep primary action visible above obstruction. |
| Repeated beige/cream surfaces create flatness | `DESIGN_DIRECTION` grounded in audit | Explore cleaner surfaces and stronger modular fields. |
| Current warning, success, info, and terracotta text roles include low-contrast pairs | `CONFIRMED_CURRENT` | Create separate text and fill tokens; measure every pair. |
| Sheet may retain stale values after success | `IMPLEMENTATION_HANDOFF` | Design success transition and clean close state. |
| Unsaved warning may appear after successful save | `IMPLEMENTATION_HANDOFF` | Specify correct draft/saved behavior. |
| English date control and inconsistent date format appear in Arabic flow | `IMPLEMENTATION_HANDOFF` | Design Arabic RTL date field and one display convention. |
| Long UUID can appear to the user | `IMPLEMENTATION_HANDOFF` | Use a human reference in concept content. |
| Debt figures may differ across surfaces | `IMPLEMENTATION_HANDOFF` | Design cannot solve logic; make source/completeness visible and flag for code track. |

## Recalculated contrast samples from the current/proposed reports

| Foreground | Background | Ratio | Implication |
|---|---|---:|---|
| `#141413` | `#faf9f5` | 17.50:1 | Strong baseline. |
| `#d97757` | `#ffffff` | 3.12:1 | Not for normal text. |
| `#141413` | `#d97757` | 5.90:1 | Dark text can work on terracotta fill. |
| `#629987` | `#ffffff` | 3.27:1 | Not for normal text. |
| `#d9b978` | `#faf9f5` | 1.79:1 | Fails as text or critical icon. |
| `#2c84db` | `#ffffff` | 3.87:1 | Not for normal text. |
| `#6b6962` | `#e8e6dc` | 4.39:1 | Fails 4.5:1 threshold for normal text. |

## Standards that constrain concepts

- WCAG 2.2 contrast: 4.5:1 normal text and 3:1 large text.
- WCAG 2.2 target-size minimum is 24×24 CSS px with exceptions; Micro intentionally uses a stronger 44–48px usability contract for important touch controls.
- Critical status cannot rely on color alone.
- Dialog/sheet designs need focus entry, contained focus, close behavior, and logical focus return.

## Approved strategic conclusions

| Conclusion | Class |
|---|---|
| Primary user is limited-to-moderate in financial/digital experience | `APPROVED_DECISION` |
| Calculated full visual change is allowed | `APPROVED_DECISION` |
| Visual expression is bold/colorful but operationally balanced | `APPROVED_DECISION` |
| Bold Modular Micro is the parent direction | `APPROVED_DECISION` |
| C leads; A warms; B disciplines | `APPROVED_DECISION` |
| Micro Signal is a candidate functional signature | `DESIGN_DIRECTION` |
| Success Impact is a candidate motion signature | `DESIGN_DIRECTION` |

## Hypotheses the designer must not present as facts

- One visual style is preferred across all Jordanian governorates.
- Terracotta automatically feels Jordanian.
- A stamp or receipt metaphor increases trust.
- A more colorful interface increases retention.
- Micro Signal reduces missed collection.
- Users prefer “صافي” over “نتيجة” or “ربح”.
- Users understand “غير موزع” without explanation.
- One icon family is inherently more accessible without testing.

## Reference-use rule

Reference products may provide patterns, not surfaces to copy:

- Shopify/Square: action-oriented operational home.
- Xero/QuickBooks: traceable figures and mobile task completion.
- Stripe/Wise: status, exceptions, and impact clarity.
- Arabic regional tools: terminology and RTL lessons, not country-specific policies.
- Careem/Talabat: status progression patterns, not brand styling.

The final concepts must remain recognizably Micro.

