# Supporting — Review Evidence

Headless-Chromium captures of the three native direction prototypes (390×844 and 320×780 viewports, Arabic RTL default), taken during build QA on 2026-09-07. These are evidence of the delivered state; the interactive prototypes remain the actual review artifacts.

| # | File | What it shows |
|---|---|---|
| 01 | `01-b-register-390-light-ar.png` | Direction B «الدفتر» — register root 390 light: compact bar + 2px terracotta rule, pinned truth bar (النقد · لك · عليك), hairline rows with fixed mono money column, FAB, tab bar |
| 02 | `02-b-position-week-chart.png` | B — pushed المركز المالي screen: position rows, week in/out chart with the unrecorded Friday as a gap, aging buckets |
| 03 | `03-b-capture-quiet-receipt.png` | B — capture sheet quiet-completion state: check mark, closure sentence with the new cash total, تراجع/تم |
| 04 | `04-b-register-320.png` | B — register at 320px: truth figures verified to fit without truncation |
| 05 | `05-a-brief-390-light-ar.png` | Direction A «الخلاصة اليومية» — brief root: large title, cash figure, hairline لك/عليك rows, timeline with right-side rail and hollow nodes |
| 06 | `06-a-large-title-collapsed.png` | A — scrolled state: large title collapsed, compact bar carries the cash figure |
| 07 | `07-c-hub-390-light-ar.png` | Direction C «الصندوق» — hub root: deep cash hero, لك/عليك counter split on one hairline, day strip |
| 08 | `08-c-hub-320.png` | C — hub at 320px |
| 09 | `09-b-people-list.png` | B — الناس list: avatars, aging sub-lines, segmented control, chips, amounts column |
| 10 | `10-b-register-dark.png` | B — warm-dark register theme |

Verification basis: `agent-browser` (headless Chromium) — screenshots plus programmatic checks (truth-figure fit at 320/390, queue-badge geometry, capture→receipt→truth-update flow, live filter, conflict resolution, closing flow, offline/error demos, no console errors). VLM review passes were used as an additional inspection layer; every flagged defect was either fixed or documented in `en/03` §7.
