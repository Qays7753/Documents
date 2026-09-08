# Typography

## Families

| Token | Stack | Role |
|---|---|---|
| `font.sans` | IBM Plex Sans Arabic → IBM Plex Sans → Segoe UI → Noto Sans Arabic → system-ui | all UI text, Arabic and Latin |
| `font.mono` | IBM Plex Mono → SFMono-Regular → Roboto Mono → Consolas | all numerals: amounts, dates, times, counts, KPI values |

One sans family carries both scripts — the source uses IBM Plex Sans Arabic for Latin as well, keeping a single texture across mixed content. In production the fonts must be self-hosted and preloaded (`accounting-sop.source.md:142`); the offline gallery deliberately falls back to system fonts because remote fonts would break offline use, and this substitution is documented as a known rendering limitation, not a design decision. Every numeral role additionally applies `font-variant-numeric: tabular-nums` (`.tnum` / `.num` utilities, `index.css.source:50,53`).

## The scale

The source's named tokens (`tailwind.config.source.js:188–194`) plus the prose-only roles from the raw SOP §5 are unified into eleven roles. Sizes are now **rem-based** so the source's own large-text mode works: `html.font-large { font-size: 17px }` (`index.css.source:18`) scaled nothing when tokens were px — a measured defect, corrected here (decision D-08).

| Token | Size / line / weight | rem | Source |
|---|---|---|---|
| `text.title` | 28 / 1.3 / 700 | 1.75rem | inherited — screen title, collapses on scroll |
| `text.title-sm` | 20 / 1.3 / 700 | 1.25rem | inherited — collapsed bar title, sheet title |
| `text.section` | 17 / 1.4 / 600 | 1.0625rem | inherited — section headers |
| `text.card-title` | 15 / 1.4 / 600 | 0.9375rem | inherited — card and row titles |
| `text.body` | 15 / 1.6 / 400 | 0.9375rem | normalized — existed only as SOP prose |
| `text.label` | 13 / 1.4 / 500 | 0.8125rem | normalized — field labels, chips, KPI labels |
| `text.caption` | 12 / 1.5 / 400 | 0.75rem | inherited — the hard 12px floor |
| `text.kpi` | 24 / 1.1 / 600 mono | 1.5rem | normalized — SOP's 24–28 KPI range, compact step |
| `text.kpi-hero` | 28 / 1.1 / 700 mono | 1.75rem | normalized — the 28 hero step |
| `text.amount` | 15 / 1.4 / 600 mono | 0.9375rem | normalized — in-row amounts |
| `text.amount-input` | 24 / 1.2 / 700 mono | 1.5rem | normalized — amount entry field |

## Off-scale size mapping (corrected)

The audits found ten stray sizes across the source's utility usage. Every one maps to a scale token:

| Stray size | Found at | Maps to |
|---|---|---|
| 10px | `mockup:241` color captions | `text.caption` 12px |
| 11px | nav labels, badges (`mockup:315`, `mobile-components:95–97`) | `text.caption` 12px |
| 13px | chips, greeting (`mobile-components:93`) | `text.label` |
| 14px | `text-sm` usages (empty desc, snackbar, search) | `text.body` 15 (prose) or `text.label` 13 (chips) |
| 16px | FAB sheet action labels | `text.card-title` + 700 |
| 18px / 22px / 36px | rendered-reference document chrome | presentation only — not app tokens |
| 19px | sheet title (`mobile-components:297`) | `text.title-sm` 20 |
| 22px | mockup home name (`mockup:99`) | `text.title-sm` 20 |

The 12px floor is absolute (`accounting-sop.source.md:142`): no UI text renders below 12px at any setting, including badges and nav labels — both were 11px in the rendered references, both corrected (D-17).

## Arabic rules

1. **No negative letter spacing, ever** (`tailwind.config.source.js:186–187`, raw SOP §5). The source once shipped `title` with `-0.01em` and removed it; the ban is preserved as a hard rule. Positive tracking is permitted only on small Latin-only labels.
2. **Generous line heights**: headings ≥1.3, body 1.6–1.8. The `leading-tight` (1.25) overrides in `PageHeader.jsx:125–126` and `mockup:99` are corrected to 1.3.
3. **Content-driven heights**: rows, cards, and sheets grow with Arabic strings; fixed heights are allowed only for controls with known content (buttons, chips, inputs) — `SOP_VISUAL_ONLY.md §6`.
4. **Correct plurals and verb-first button copy** are content rules carried into `content-guidelines.md`.

## Numerals and bidi

Numbers are Latin digits inside Arabic text, always: `dir="ltr"` on amount inputs (`AmountInput.jsx:47`), `unicode-bidi: isolate` on embedded numeric spans (raw SOP §13.5, now the `.bidi-isolate` utility), tabular figures for alignment, end-alignment for column values, thousands separator `,`, no currency symbols, `+` / `−` (U+2212) signs in the state color. Amount inputs use `inputMode="decimal"` with live grouping (`1,500` while typing) and reject invalid input rather than clamping silently.

## Large text and density

The large-text mode (`.font-large`, 17px root) scales every rem token ~6%; controls sized in rem grow with it, so no text clips — verified in the gallery's large-text toggle. The optional compact density (`.density-compact`: card padding 16→12, row padding 10) is inherited as a utility for dense lists and is orthogonal to the type scale.
