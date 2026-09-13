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
| label | 13/1.4/500 | field labels, chips |
| caption (floor) | 12/1.5/400 | the 12px floor; never for financial facts |
| kpi | 24 mono/600 | primary numbers |
| kpi-hero | 28 mono/600 | hero numbers |
| amount | 15 mono/600 | row and slot amounts |
| amount-input | 24 mono/600 | amount entry fields |

## Numeric hierarchy

The 30/20/15 hierarchy is the emphasis ladder (hero : primary : secondary) realized by the mono steps: hero 28, primary 24, secondary 15, tertiary 13. Financial facts never render below 15px; the 12px caption floor carries metadata only. Numerals are English digits with `unicode-bidi: isolate` in `dir="ltr"` slots so RTL composition cannot reorder them; grouping is applied as displayed text, never inside the numeric string.
