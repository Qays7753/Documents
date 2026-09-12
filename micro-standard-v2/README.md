# Micro Standard v2

Micro Standard v2 is the current approved Arabic-first, RTL, phone-only visual foundation for Micro. It is based on the final Cloud Code Design Wave 2 foundation and the approved Micro Component Expansion v1.

The package defines current tokens, component contracts, financial-safe states, mobile geometry, interaction rules, navigation, empty/loading/error behavior, and a local interactive gallery. It does not define financial policy, financial formulas, synchronization behavior, or backend implementation.

## Official navigation

`الرئيسية` · `المالية` · `الطلبات` · `الأدوات`

`الأدوات` is a separate calculation and decision-support area, such as product-cost and salary estimation. A tool result does not create or alter a financial record unless a later product action explicitly does so.

## Current color roles

`#D97757` is identity/create/FAB. `#C96442` is pressed/chosen/current edge or underline. `#141413` is warm-ink commitment/value primary. The warm canvas and surface layers are protected.

## Verification boundary

The gallery is verified locally at 320/360/390/430px, 100/130/200% text scale, RTL/LTR, reduced motion, and no horizontal overflow in the inspected browser states. Physical-device and screen-reader verification require separate testing.
