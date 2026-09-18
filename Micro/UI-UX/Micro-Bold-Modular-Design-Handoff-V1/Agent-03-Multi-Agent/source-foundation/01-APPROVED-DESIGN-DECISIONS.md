# Approved Design Decisions

## Status labels

- `LOCKED`: The visual designer must preserve it.
- `OPEN_FOR_EXPLORATION`: The designer must produce evidence-based alternatives.
- `OWNER_APPROVAL_REQUIRED`: The designer must not finalize it independently.
- `USER_TEST_REQUIRED`: It remains a hypothesis until tested.

## Locked product decisions

| ID | Decision | Status |
|---|---|---|
| UX-D01 | Primary user: a small-business owner with limited-to-moderate financial and digital experience, using a phone as the main device. | `LOCKED` |
| UX-D02 | Arabic-first and mobile-first. | `LOCKED` |
| UX-D03 | Financial truth is more important than visual optimism: unknown or incomplete data must never appear as zero or confirmed profit. | `LOCKED` |
| IA-D01 | Bottom navigation has five destinations: مشروعي الآن، العمل، المالية، أدواتي، السوق. | `LOCKED` |
| IA-D02 | منتجاتي وخدماتي is one contextual destination reachable from multiple places, not a sixth tab. | `LOCKED` |
| IA-D03 | The top zone is compact: Micro logo on the right; النقل والتوصيل and Ask Micro on the left; logo opens the account/project/settings menu. | `LOCKED` |
| IA-D04 | Dark mode remains inside settings, not in the main header. | `LOCKED` |
| PR-D01 | Micro is a financial and operational system, not an AI character or chatty companion. | `LOCKED` |

## Locked design strategy

| ID | Decision | Status |
|---|---|---|
| UI-D01 | Visual freedom: calculated full change is allowed. Existing cream and terracotta are candidates, not sacred assets. | `LOCKED` |
| UI-D02 | Energy model: bold and colorful in identity; active and balanced in use. | `LOCKED` |
| UI-D03 | Primary direction: **Bold Modular Micro**. | `LOCKED` |
| UI-D04 | Direction C leads composition and expression; A contributes warmth and approachability; B contributes financial discipline and trust. | `LOCKED` |
| UI-D05 | Calmness is a task state, not the entire brand personality. | `LOCKED` |
| UI-D06 | Stronger color blocks are allowed only when they communicate section, status, priority, action, change, or progress. | `LOCKED` |
| UI-D07 | Main/home screens may be highly expressive; finance is moderately expressive; records and settings are visually quieter. | `LOCKED` |
| UI-D08 | Do not use decorative notebook, receipt, or stamp metaphors as the main identity system. | `LOCKED` |

## Approved interaction principles

| ID | Decision | Status |
|---|---|---|
| IX-D01 | The home screen must answer “كيف وضع مشروعي؟” within five seconds. | `LOCKED` |
| IX-D02 | Repeated actions are visible and labeled; an icon-only hidden FAB is not sufficient. | `LOCKED` |
| IX-D03 | Quick Action Bar is the default exploration pattern. Do not duplicate it with a second persistent FAB. | `LOCKED` |
| IX-D04 | Success feedback must show what changed and where the value went. | `LOCKED` |
| IX-D05 | Every critical state uses text plus a second non-color cue. | `LOCKED` |

## Open visual decisions

| Topic | Required exploration | Status |
|---|---|---|
| Brand color | Keep, intensify, deepen, or replace the existing terracotta family through visual comparison. | `OWNER_APPROVAL_REQUIRED` |
| Base background | Compare warm-neutral canvas with cleaner neutral surfaces; avoid full-screen beige dominance. | `OWNER_APPROVAL_REQUIRED` |
| Trust color | Test a deep blue or blue-teal secondary without confusing it with financial positive. | `OWNER_APPROVAL_REQUIRED` |
| Icon expression | Evaluate current Lucide foundation versus a stronger single-family treatment; do not mix libraries. | `OPEN_FOR_EXPLORATION` |
| Module accents | Explore whether sections receive controlled accents without becoming separate applications. | `OPEN_FOR_EXPLORATION` |
| Motion signature | Explore “Success Impact”: saved operation → affected value visibly updates. | `USER_TEST_REQUIRED` |
| Micro Signal | Explore the repeated structure: status → reason → action. | `USER_TEST_REQUIRED` |

## Decisions deliberately postponed

- Final palette hex values.
- Final logo adjustment.
- Final component tokens.
- Final icon library migration.
- Final animation curves beyond concept guidance.
- Final charts and data-visualization library.
- Production implementation sequence.

