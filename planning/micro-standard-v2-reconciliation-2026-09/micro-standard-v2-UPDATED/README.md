# Micro Standard v2 — Final Copy

Micro Standard v2 is the Final Copy for the Arabic-first, RTL, phone-only visual foundation for Micro. It is based on the final Cloud Code Design Wave 2 foundation and the approved Micro Component Expansion v1, reconciled against execution run `run-20260913-msv2-zai-01` and the independent post-run audit on branch `micro-standard-v2-final-copy-20260913`. It is the official visual foundation published in Documents `main`; it is not a Micro product implementation.

The package defines current tokens, named action classes, component contracts, financial-safe states, mobile geometry, interaction rules, navigation, empty/loading/error behavior, and a local interactive gallery. It does not define financial policy, financial formulas, synchronization behavior, or backend implementation.

## Authority ladder

Micro Standard v2 = visual contracts (tokens, action classes, component and state contracts, geometry, accessibility, composition guidance). The Micro runtime token mapping = the carrier that binds implementation variables to these contracts. Micro docs = implementation guidance. Micro domain/application/storage layers = product meaning and persistence. Contracts never encode product meaning; runtime never redefines contract values. The package is **29 core files + 2 metadata records** (`MANIFEST.json`, `RELEASE.md`). `source-inventory.md` remains one of the 29 core evidence/contract files. This classification preserves the established baseline and was reconciled after the initial run record.

## Official navigation

`الرئيسية` · `المالية` · `الطلبات` · `الأدوات`

`الأدوات` is a separate calculation and decision-support area, such as product-cost and salary estimation. A tool result does not create or alter a financial record unless a later product action explicitly does so.

## Current color roles

`#D97757` is identity/create/FAB. `#C96442` is pressed/chosen/current edge or underline. `#141413` is warm-ink commitment/value primary — its filled surface is reserved for high-consequence commitment. The warm canvas and surface layers are protected.

## Action classes (owner-approved)

| Class | Surface | Notes |
|---|---|---|
| Create / add / FAB | Clay `#D97757` | text-bearing controls use dark `#141413`; icon-only FAB/icon buttons use white icons; pressed `#C96442`; never a financial value |
| Ordinary save / confirm | Warm Tint `#F5F4ED` + ink `#141413` | pressed shows a `#C96442` edge; press is never success; completion = word + check marker |
| High-consequence commit | Warm ink `#141413` + white text | consequence word, icon, explanation, independent confirmation |
| Destructive | error `#B53333` ink + confirmation | uses the high-consequence contract |

Every financial state pairs a word with a non-color marker; pending never reads as success and unknown is separate from failure. No new color values were introduced by this run; two functional alpha derivatives (scrim, translucent header) are disclosed in `color-system.md`.

## Verification boundary

The Standard package and Gallery were re-verified locally at 320/360/390/430px, 100/130/200% text scale, RTL/LTR, reduced motion (control and system preference), and no horizontal overflow in headless Chromium during Final Copy reconciliation; computed-style contract checks cover the action classes, selection edges, scrim visibility, and chart states. The Prototype remains evidence only and is excluded from Final Copy acceptance. Physical-device and screen-reader verification require separate testing and are not claimed.
