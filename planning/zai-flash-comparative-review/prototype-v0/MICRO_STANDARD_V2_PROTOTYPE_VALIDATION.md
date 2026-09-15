# Micro Standard v2 Prototype Validation

## Scope and environment

Validation used a local Python HTTP server at `http://127.0.0.1:4183/index.html` and installed headless Chromium controlled by Playwright. The run was local-only with no external network dependency. The harness and raw JSON results are included in `evidence/`.

## Viewport results

| Width | RTL | Horizontal overflow | Scenes exercised | Result |
|---:|:---:|:---:|---:|:---:|
| 320px | Yes | Not detected by DOM measurement | Home smoke | Pass |
| 360px | Yes | Not detected by DOM measurement | Home smoke | Pass |
| 390px | Yes | Not detected by DOM measurement | Home, Finance, Orders, Detail, Tools | Pass |
| 430px | Yes | Not detected by DOM measurement | Home smoke | Pass |

The five scenes rendered with reachable buttons and no DOM-measured horizontal overflow. The screenshots are evidence of the composition, not a claim of physical-device behavior.

## Interaction results

Custom period sheet opened. Sheets opened and closed. Lifecycle cycled through `نتيجة غير معروفة`, `قيد الانتظار`, `يمكن إعادة الفحص`, `نتيجة مؤكدة توضيحيًا`, and `أثر معكوس — audit effect`. The confirmation boundary opened. Chart alternative text was shown. The tool opened and accepted input. However, the independent interaction harness found that changing salary input from 980 to 1200 and pressing recalculate left the displayed result at `1,156.4 د.أ` instead of the expected illustrative `1,416 د.أ`. This is recorded as an unfixed prototype defect.

## Scale results

The lightweight CSS zoom proxy reported no DOM-measured overflow at 100%, 130%, and 200%. The 200% screenshot, however, visibly shows enlarged content clipped by the viewport and is therefore treated as a **failed/inconclusive visual scale result**, not as a pass. The test harness used CSS zoom as a proxy and does not replace browser text-zoom or physical-device testing.

## Accessibility and state checks

The prototype uses RTL, visible words plus markers for states, accessible chart `aria-label` text, a visible chart alternative paragraph, keyboard-reachable buttons, and focus-visible styles. Pending and unknown are not styled as success. Reversed is labelled as an audit effect and does not imply erasure. The test did not include a physical screen reader.

## Reduced motion

The CSS includes a `prefers-reduced-motion: reduce` rule that suppresses non-essential animation while preserving content and interaction. The harness created the browser context with reduced motion enabled for the main checks.

## Evidence files

The five 390px scene screenshots are `scene-home-390.png`, `scene-finance-390.png`, `scene-orders-390.png`, `scene-detail-390.png`, and `scene-tools-390.png`. `scene-finance-200pct.png` is the 200% visual evidence. Raw results are in `BROWSER_VALIDATION_RESULTS.json`, `INTERACTION_VALIDATION.json`, `validation-run-final.log`, and `validate.mjs` / `validate_interactions.mjs`.

## Limitations

No physical Samsung device, physical screen reader, production browser matrix, real data, backend, database, accounting engine, sync, permissions, delivery behavior, or record-writing action was tested. The prototype remains review-only.
