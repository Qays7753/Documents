# Micro Standard v2

Micro Standard v2 is the current approved Arabic-first, RTL, phone-only visual foundation for Micro. It is based on the final Cloud Code Design Wave 2 foundation and the approved Micro Component Expansion v1, updated by execution run `run-20260913-msv2-zai-01` (Waves 0/A/B/C) on the branch `micro-standard-v2-execution-20260913`.

The package defines current tokens, named action classes, component contracts, financial-safe states, mobile geometry, interaction rules, navigation, empty/loading/error behavior, and a local interactive gallery. It does not define financial policy, financial formulas, synchronization behavior, or backend implementation.

## Official navigation

`الرئيسية` · `المالية` · `الطلبات` · `الأدوات`

`الأدوات` is a separate calculation and decision-support area, such as product-cost and salary estimation. A tool result does not create or alter a financial record unless a later product action explicitly does so.

## Current color roles

`#D97757` is identity/create/FAB. `#C96442` is pressed/chosen/current edge or underline. `#141413` is warm-ink commitment/value primary — its filled surface is reserved for high-consequence commitment. The warm canvas and surface layers are protected.

## Action classes (owner-approved)

| Class | Surface | Notes |
|---|---|---|
| Create / add / FAB | Clay `#D97757` | pressed `#C96442`; never a financial value |
| Ordinary save / confirm | Warm Tint `#F5F4ED` + ink `#141413` | pressed shows a `#C96442` edge; press is never success; completion = word + check marker |
| High-consequence commit | Warm ink `#141413` + white text | consequence word, icon, explanation, independent confirmation |
| Destructive | error `#B53333` ink + confirmation | uses the high-consequence contract |

Every financial state pairs a word with a non-color marker; pending never reads as success and unknown is separate from failure. No new color values were introduced by this run; two functional alpha derivatives (scrim, translucent header) are disclosed in `color-system.md`.

## Verification boundary

The gallery was re-verified locally at 320/360/390/430px, 100/130/200% text scale, RTL/LTR, reduced motion (control and system preference), and no horizontal overflow in headless Chromium during this run; computed-style contract checks cover the action classes, selection edges, scrim visibility, and chart states. Physical-device and screen-reader verification require separate testing and are not claimed.
