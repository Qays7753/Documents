# Typography

Arabic-first text uses the approved sans family ("IBM Plex Sans Arabic", system-ui fallback), with English numerals and tabular mono figures ("IBM Plex Mono") for amounts. Labels stay short, values are direct, and numeric bidi isolation prevents reordering in RTL.

## Type scale (recorded basis)

| Step | Size/line/weight | Use |
|---|---|---|
| title | 28/1.3/700 | screen titles |
| title-sm | 20/1.3/700 | bar and sheet titles |
| section | 17/1.4/600 | section headers |
| card-title | 15/1.4/600 | cards and rows |
| body | 15/1.6/400 | prose |
| label | 13/1.4/500 | field labels, chips, state words, navigation and segment labels — never below 13px |
| caption (floor) | 12/1.5/400 | non-financial metadata only — the 12px floor; never for labels or financial facts |
| kpi | 24 mono/600 | primary numbers |
| kpi-hero | 28 mono/600 | hero numbers |
| amount | 15 mono/600 | row and slot amounts |
| amount-input | 24 mono/600 | amount entry fields |

## Numeric hierarchy

The 30/20/15 hierarchy is the emphasis ladder (hero : primary : secondary) realized by the mono steps: hero 28, primary 24, secondary 15, tertiary 13. Labels never render below 13px. Financial facts and amounts never render below 15px; the 12px caption floor carries non-financial metadata only, and the tertiary 13px mono step is non-financial numeric metadata. Numerals are English digits with `unicode-bidi: isolate` in `dir="ltr"` slots so RTL composition cannot reorder them; grouping is applied as displayed text, never inside the numeric string.
