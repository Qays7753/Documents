# Component Contracts

Shared components consume `--vf-*` roles and expose slots for primary commitment, neutral secondary, outline, ghost, Clay identity, chosen/current edge, semantic outcome, and non-color state marker.

## Action contract (owner-approved)

| Contract | Binding | Non-color signal |
|---|---|---|
| create/add/FAB | `--vf-action-create` (`#D97757`), pressed `#C96442` | plus icon; create wording; never a financial value |
| ordinary save/confirm | `--vf-action-save-bg/ink` (`#F5F4ED` / `#141413`); pressed edge `#C96442` | save icon; press shows edge only; completion = check + past-tense word |
| pressed save | Warm Tint surface persists; `2px` inset `#C96442` edge | pressing is not success |
| high-consequence commit | `--vf-action-commit-bg/ink` (`#141413` / `#FFFFFF`); pressed `#3D3D3A` | consequence word + icon + explanation + independent confirmation path |
| destructive | error `#B53333` ink + confirmation step | alert icon + consequence wording |
| success/error/pending/unknown/review | semantic roles with tint grammar | word + marker always; color never alone |

Selection and current state use the chosen/current edge role: a `2px` `#C96442` edge or underline plus a non-color cue (bold weight, check, or filled icon). Selected chips, segments, and tabs do not automatically become black fills.

## Financial value zone

A primary value composition exposes named slots so screens stay comparable:

- **label** — short Arabic label of what the number is;
- **value** — English numerals, tabular mono, bidi-isolated, end-aligned in its slot;
- **currency unit** — contextual `د.أ` / `دأ` beside the value, never inside the number;
- **period** — the period chip text (e.g., "آخر 30 يوم") anchored to the value it qualifies;
- **delta** — optional comparison with a direction word and marker.

Honest voids are part of the contract: an unrecorded value shows an action chip ("سجّله"); an unavailable value shows the word "غير متاح"; a measured zero shows "0" with its label. A void is never styled as success, failure, or decoration.

## Period chip

The period control is a chip or segmented row that states the qualifying range in Arabic with English numerals. It sits with the value or list it qualifies, keeps 36px visual / 44px hit-area geometry, and stages range changes until applied when used inside filter surfaces. Time semantics (what ranges exist, defaults) are product-owned; this contract covers presentation only.

## Operational row slots

Rows use one grid: an optional identity lead (icon tile or avatar), a flexible title/caption column that wraps Arabic safely, an optional state slot (one word + marker), and a stable trailing slot for tabular amounts and actions. An optional state edge stripe (≤3px, the state's semantic color) may mark the row's inline-start edge — always paired with the state word in the row. Rows keep inset dividers and never rely on the stripe alone.

Micro domain compositions sit above these primitives: balance, attention, party, receivable, operational row, order detail, tool result, simple chart, and period control. The visual foundation must not invent product policy inside a primitive.
