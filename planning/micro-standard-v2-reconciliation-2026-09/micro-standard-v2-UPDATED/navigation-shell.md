# Navigation Shell

Micro uses four owner-approved phone destinations: `الرئيسية`, `المالية`, `الطلبات`, and `الأدوات`. The shell is RTL, respects safe areas, uses persistent bottom navigation, and provides a restrained top action area. The identity FAB is placed in its own gutter and must not cover amount or action columns.

## AUX behavior addendum (visual/interaction contract)

- **Route-kind chrome.** Screen families may be classified by interaction depth: surface-like reading and list screens keep the persistent navigation; deep work and flow screens may hide it to protect focus. This is a chrome *behavior* contract — route lists, route names, and the classification of any concrete route remain product-owned.
- **Keyboard-driven chrome hiding.** While the software keyboard is open, transient chrome (the top bar and the bottom navigation) may hide so the working area keeps its height; content, the focused control, its label, and any helper or error text never hide. Chrome returns when the keyboard closes.
- **Safe-area clearance.** Bottom-anchored chrome pads with `env(safe-area-inset-bottom)`; sticky footers and action bars sit above it; the FAB keeps its own gutter and never covers amount or action columns.
- **Context-label suppression.** A top-bar context label may be suppressed when it would duplicate the screen's own heading; the title area stays stable with no layout jump.
- **Scroll-border behavior.** A hairline border or a stronger elevation tier appears under the top bar only after the content actually scrolls, and relaxes at the top.
- **Route transition guidance.** Route changes use the standard content transition timing (`--motion-normal` 200ms, easing per the motion contract) with no page-wide layout animation; the incoming screen's states (loading/empty/error) render immediately. Under reduced motion, transitions collapse per the motion contract.
