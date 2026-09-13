# Independent visual findings notes

## Home and Finance screenshots

The rendered screenshots expose a significant fixed-bottom navigation overlap: at the lower fold, the navigation bar sits over quick actions on Home and over the SimpleChart transition on Finance. The content has bottom padding, but the screenshot shows the bar obscuring content in the reading path; this is a prototype composition/viewport issue, not a Standard token issue.

The overall warm canvas, white surfaces, direct values, Arabic RTL hierarchy, and status markers read coherently and remain close to Micro's intended operational tone. The Home scene is information-rich and useful for review, but the lower quick-action area becomes visually interrupted by the fixed nav.

Finance is materially stronger as a composition test than a gallery card: Metric, Parts/Whole, chart, and explicit states create a clear vertical story. However, the chart reads visually black-heavy because the bars use Warm-Ink with limited secondary role contrast; this is likely a Micro composition decision using existing roles rather than a missing Standard primitive. The chart also begins below the fold in the captured viewport, which reduces first-glance comprehension on phone.

At the screenshot width observed by the renderer, no horizontal overflow is visible, but the evidence filename was generated after the last loop viewport and should be labelled by measured viewport rather than assumed filename.

## Orders and Detail screenshots

Orders is the most Micro-like scene: long Arabic title wrapping works, the amount slot remains visually stable, and status words use non-color markers. The fixed bottom navigation still covers the lower boundary section, reducing confidence that the last explanatory content is reachable without extra scroll.

Detail makes lifecycle language tangible and correctly avoids reading unknown as success. The main value/context and neutral party information are clear. A notable Arabic-first quality issue remains: English review labels such as `Lifecycle`, `State language`, `policy`, and `reversal` leak into the Arabic scene. This is content/composition polish rather than a missing Standard contract, unless the Standard intends a fully localized label vocabulary.

The Detail scene is comparatively sparse below the main value, while the lifecycle control and relationship grid are visually strong. The fixed nav again masks the beginning of the final record-boundary section.

## Tools and scale evidence

Tools clearly separates an illustrative calculation from record writing and uses a deterministic local result. This is a strong boundary decision. However, the scene exposes English metadata (`ToolResult boundary`) inside an Arabic-first screen, and the fixed bottom navigation obscures the lower record-separation copy. The scene is functionally clear but visually sparse compared with Accounting's richer layered benchmark.

The first generated file named `scene-finance-200pct.png` was captured while the page was on the Tools route due to a harness sequencing mistake; it must not be treated as valid Finance 200% evidence. This is a validation artifact issue, not a prototype rendering claim, and the harness should be corrected and rerun before delivery. The prototype itself is not being repaired at this stage.

## Interaction harness finding

The additional interaction harness successfully opened the custom period sheet, cycled lifecycle through unknown → pending → retryable → result → reversed-as-audit-effect, and opened the confirmation boundary. However, changing the salary input from 980 to 1200 and pressing recalculate returned `1,156.4 د.أ` (the old 980-based result) instead of the expected deterministic illustrative `1,416 د.أ`. This is a genuine prototype interaction defect: the input change is not reflected in the rendered calculation result. It is intentionally not repaired before the critique is documented.

The failed harness attempt before this result was a test-harness sheet-close issue and was corrected without changing prototype source. The second run exposed the actual stale-result behavior above.
