# Color System

## Approved roles

| Role | Value | Use |
|---|---|---|
| Canvas | `#FAF9F5` | phone canvas |
| Ground | `#F5F4ED` | grouping ground; ordinary save/confirm surface |
| Recessed | `#F0EEE6` | tracks and skeletons |
| Surface | `#FFFFFF` | sheets, fields, elevated content |
| Secondary tint | `#E8E6DC` | secondary action and quiet grouping; quiet hairline tier (`--vf-border-soft` alias) |
| Warm ink | `#141413` | key values, primary commitment, focus |
| Clay | `#D97757` | identity, create, FAB |
| Clay interactive | `#C96442` | pressed/chosen/current edge or underline; ordinary-save pressed edge |
| Info | `#2C84DB` | attention/pending mark |
| Status | `#1490FF` | reviewed/current mark |
| Success | `#629987` | settled/success mark |
| Error | `#B53333` | error/destructive mark |

## Action roles (owner-approved)

| Action class | Surface | Ink | Pressed | Words |
|---|---|---|---|---|
| Create / add / FAB | Clay `#D97757` | `#141413` for text-bearing buttons; white for icon-only FAB/icon buttons | Clay interactive `#C96442` | create/add wording; never a financial value |
| Ordinary save / confirm | Ground `#F5F4ED` | warm ink `#141413` + icon | `2px` inset `#C96442` edge; surface stays Warm Tint | save/confirm wording; press is not success |
| High-consequence commit | Warm ink `#141413` | white | `#3D3D3A` fill | consequence word + icon + short explanation + independent confirmation |
| Destructive | outline/surface | error `#B53333` + icon | error-tinted press per tint grammar | consequence wording + confirmation |

The filled warm-ink surface is reserved for the high-consequence class. It is not the default background for every important element, not decoration, and not an all-ink chart color.

## State marks and tint grammar

Every financial state pairs a word with a non-color marker (icon, shape, or sign); color never carries a state alone. Pending never reads as success; unknown is separate from failure. Tinted state marks reuse the existing Warm Tint ground (`#F5F4ED` / `#F0EEE6`) with the semantic ink — for example the negative pair (`--color-negative-50` = ground, `--color-negative-on-tint` = error ink). No new tint hex values exist in this package.

## Functional derivatives (disclosed, not new palette)

Two alpha composites of approved base values exist for functional needs: the overlay scrim (warm ink `#141413` at 45% — required by the overlay contract) and the translucent header (canvas `#FAF9F5` at 86%). Elevation shadows use the recorded warm shadow tone `rgba(60,50,40,x)`. These are derivatives of approved values, not palette members, and must not be repurposed as fills, text, or identity colors.

## Link/action ink — constraint only

A text affordance (link-style action) must use a text-safe ink, never a financial-semantic color, and never the Clay identity as body-size text. No link-ink value is ratified in this package; the incumbent live value remains an explicit owner decision. Until the owner decides, implementers use warm ink or ink-secondary for text affordances.

## Restraint rule

Do not turn every chart, card, or button into Clay or black. Richness comes from meaningful composition and semantic contrast. Charts use semantic marks only when they answer a clear question; black is not the default for every series, and Terracotta never becomes a data, success, or failure color.
