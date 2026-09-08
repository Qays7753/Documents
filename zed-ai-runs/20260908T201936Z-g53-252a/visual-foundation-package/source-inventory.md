# Source Inventory

Complete token-level inventory of `accounting-visual-foundation-source-pack-v1` with exact evidence. Read-only audit performed by Subagent 1 (full machine-readable version: `agents/sub1/inventory.json`; the A2/A3 component and accessibility evidence merges into the decision log). Line references are pack-relative; `TW` = `source-reference/tailwind.config.source.js`, `ICSS` = `source-reference/index.css.source`, `SOP` = `SOP_VISUAL_ONLY.md`, `ASOP` = `source-reference/accounting-sop.source.md`.

## Color inventory — 81 unique hex, 10 rgba

**Canonical 68** (extracted to `source-tokens.json:116–186`): six ramps of ten steps (primary `TW:22–34`, accent `TW:36–50`, income `TW:52–66`, expense `TW:68–82`, withdrawal `TW:84–98`, returns `TW:100–114`) plus 9 neutrals and 16 named aliases/roles (`TW:116–158`).

**Extra 13**: 6 forbidden-documentation colors (`#023852, #F4F7F9, #E4EAEE, #647680, #FE8801, #1F6FE8`, `accounting-color-identity.html:95–97`) · 2 divergent fills `#DC2E2F` / `#E0A200` (`ASOP:65,67,203`; `color-identity:246,260`) · 2 investor-mode colors (`#FBFAF7`, `#2A2521`, `ASOP:318,320` — out of scope) · 1 untokenized stage `#ECE9E4` (`AppLayout.jsx:23`) · 2 off-palette brand-asset colors `#1F6FE8`/`#23C35B` (`reference-assets/accounting-icon.svg:3,7`).

**rgba set** (10): the 5 warm shadow alphas `.04/.06/.06/.10/.16` (`TW:173–185`) · scrim `rgba(31,30,29,.4)` inlined at `ICSS:70`, `BottomSheet.jsx:137`, `ASOP:218`, `mobile-components:305` · header veil `rgba(250,249,245,0.88)` (`PageHeader.jsx:109`) · cold page shadow `rgba(33,36,39,0.08)` (`AppLayout.jsx:24`) · snackbar overlay variants.

## Named color roles with evidence

| Role | Value | Evidence |
|---|---|---|
| Primary terracotta / pressed / deep / soft | `#CC785C` / `#B4613F` / `#964E33` / `#F4E4DB` | `SOP:27–30`; `TW:28–30,33` |
| Teal accent / text / tint | `#079FA0` / `#057B7C` / `#E3F5F5` | `SOP:31–33`; `TW:42,48–49` |
| Positive text/fill/bg | `#2E7D57` / `#A7D8BE` / `#E4F2EA` | `SOP:55`; `TW:58,64–65` |
| Negative text/fill/bg | `#B42318` / `#DB514C` / `#FBE7E6` | `SOP:56`; `TW:79–81` |
| Operational text/fill/bg | `#3E5C76` / `#5B7C99` / `#E8EEF3` | `SOP:57`; `TW:95–97` |
| Gold text/fill/bg | `#B08532` / `#D6AB38` / `#F6ECCF` | `SOP:58`; `TW:111–113` |
| Neutrals (canvas/recessed/surface/borders/ink trio/disabled) | 9 values | `SOP:39–49`; `TW:116–141` |
| Status progress/ready/closed | `#C99100` / `#079FA0` / `#6E6A60` | `TW:152–158` |
| Badge pairs | progress/ready/closed | `ICSS:136–150` |
| Nav active/inactive | `#CC785C` / `#B7B2A6` | `ICSS:152–153` |
| Destructive button | `bg-expense-500` → `#C9322A` | `ICSS:101–104` |
| Sheet scrim | `rgba(31,30,29,0.4)` | 4 sites (above) |

## Alias and duplicate map (19 aliases, 29 duplicates)

| Value | Names in source | Canonical here |
|---|---|---|
| `#F4E4DB` | primary.100, primary-tint, primary-pill, primary.tint (HTML) | `color.primary.100` |
| `#E8EEF3` | withdrawal.50, withdraw-bg, withdrawal-bg, (divider alias in 3 HTML configs) | `color.operational.50` |
| `#6E6A60` | ink.secondary, text.secondary, txt.secondary, faint, sub, closed, status.closed | `color.ink-secondary` |
| `#B7B2A6` | disabled, placeholder, text.tertiary, txt.tertiary | `color.disabled` |
| `#1F1E1D` | ink, text.primary, txt.primary, bg-text-primary (snackbar misuse) | `color.ink` |
| `#B08532` | returns.500/DEFAULT, amber | `color.gold.500` |
| `#F0EEE6` | ivory, mute | `color.recessed` |
| `#FAF9F5` | background, altRow | `color.canvas` |
| shadows | e1=card, e2=sheet=header=lg, e3=fab=xl | `shadow.e1/e2/e3` |
| radius | 12=xl, 16=2xl=card, 20=3xl=sheet | role names |
| fonts | sans=cairo=ibm | `font.sans` |

Full deprecation decisions: `design-tokens.json → aliases` (15 entries, each with evidence).

## Typography evidence

Named tokens `TW:188–194` (title 28/1.3/700 · title-sm 20/1.3/700 · section 17/1.4/600 · card-title 15/1.4/600 · caption 12/1.5/400). Prose roles `ASOP:147–155` (body 15/400 · label 13/500 · KPI 24–28/600 mono · row number 15/600 mono). Fonts `TW:160–165`, `ICSS:53`. Tabular utilities `ICSS:50,53,170`. Arabic no-tracking rule `TW:186–187`, `ASOP:157` (the historical `-0.01em` bug documented as removed). Large-text `ICSS:18–19` (17px root + 1.7 body line-height). Density `ICSS:21–24`. Off-scale sizes found: 10px (`mockup:241`), 11px (`mockup:315–340`; `mobile-components:95–97,335–372`), 13px (`mobile-components:93`), 14px (`text-sm` across 6 components), 16px (`text-base` Fab labels), 18px/22px/36px (document chrome), 19px (`mobile-components:297`).

## Geometry evidence

Spacing scale `TW:195–201` (4/8/12/16/20/24/32 + 52 + 56) with usage constants `ASOP:103`. Heights: control 48 (`ICSS:77–110`), chip 36 (`ICSS:118`), touch 44 (`ICSS:172`), top bar 56 (`PageHeader.jsx:101`), nav 56–64→64 (`ASOP:116`; `BottomNav.jsx:131`), action bar 64–72 (`ASOP:117`), FAB 56 (`Fab.jsx:39`), large title 112–140 (`ASOP:114`). Sheet: snaps 84/94vh, drag −50/+130/−44 (`BottomSheet.jsx:130–131,103,117–119`), handle 36×5 (`:165`). Radii `TW:166–172` + nested-corner rule `ASOP:135`. Shadows `TW:173–185`; z-ladder 10/20/30/40/50/60 (see token JSON). Motion: 7 keyframes `TW:203–220`; press `ICSS:51–52`; reduced-motion `ICSS:177–185`; snackbar 5000ms+250ms (`Snackbar.jsx:9,19`).

## Component evidence (9 JSX + 3 HTML)

`PageHeader.jsx` (sticky bar, veil+blur, scroll shadow sentinel, icon-expand search, 44px actions) · `BottomNav.jsx` (64px bar, 52×32 pill, focus ring `primary/50`, 5–6 items) · `AppLayout.jsx` (480px shell, stage, pb-28) · `EmptyState.jsx` (64px tile anatomy) · `Snackbar.jsx` (ink surface, undo action, z-60) · `BottomSheet.jsx` (full drag/focus-trap contract) · `Icon.jsx` (51 outline icons, stroke 1.8, RTL chevron semantics `:91–98,174–177`) · `SegmentedControl.jsx` (pill + underline variants, sliding thumb) · `AmountInput.jsx` (LTR mono decimal, live formatting) · `Fab.jsx` (56px E3, semantic action grid) · rendered HTML references (composed evidence + the divergences catalogued above).

## Responsive / RTL / safe-area evidence

Viewports 320/360/390/430 (`SOP:11`); design 390 range 360–430 (`ASOP:24`); safe-area utilities `ICSS:173–174` + inline insets (`Fab.jsx:40`, `BottomSheet.jsx:153`); `viewport-fit=cover` and the `user-scalable=no` defect (`mockup:5`); `[dir=rtl]` alignment `ICSS:37`; `dir=ltr` numeric inputs (`AmountInput.jsx:47`); `unicode-bidi: isolate` (`ASOP:344`); physical-anchoring violations found at `Fab.jsx:39`, `mockup:301`, `mobile-components:316` (FAB `left-4`), `PageHeader.jsx:138,148,155` (search icon/clear).

## The 18 documented source conflicts

1. Destructive fill 3-way: `#DC2E2F` (`ASOP:65,203`; `color-identity:246`; `mobile-components:92`) vs `#DB514C` (`SOP:56`; `TW:80`) vs `#C9322A` implemented (`TW:74`; `ICSS:102`) → **normalized to `#C9322A` for fills** (D-03).
2. Gold fill: `#E0A200` (`ASOP:67`; `color-identity:260`) vs `#D6AB38` (`SOP:58`; `TW:112`) → **`#D6AB38`**.
3. Sheet shadow: `0 -4px 24px` (`color-identity:67`; `mockup:67` — contradicting its own line 400) vs `0 6px 20px` (`TW:175`; `ICSS:66`; `BottomSheet.jsx:152`) → **`0 6px 20px`** (D-12).
4. Divider: `#DAD5C8` (`TW:136`) vs `#EAE6DC` (aliased in all 3 HTML configs) → **both retained as distinct roles** (D-11).
5. Off-scale type: 10/11/13/14/16/18/19/22/36px (locations above) → **mapped to the scale** (D-08).
6. Touch targets: 40px (`mockup:101`), 28px (`PageHeader.jsx:155`, `Snackbar.jsx:54`) → **44px enforced** (D-13).
7. Brand assets off-palette (`accounting-icon.svg`) → **flagged, human decision**.
8. Untokenized `#ECE9E4` + cold page shadow (`AppLayout.jsx:23–24`) → **excluded as presentation chrome** (D-19).
9. Untokenized header veil (`PageHeader.jsx:107–110`) → **tokenized** (`color.header-translucent`).
10. Mockup currency symbol + dot separator + ASCII hyphen (`mockup:118,166,175`) → **numbers-only rule enforced** (D-22).
11. `user-scalable=no` (`mockup:5`) → **prohibited** (D-25).
12. Shell width 480 (`AppLayout.jsx:24`) vs 420 (`mockup:89`) → **presentation, not foundation** (D-28).
13. FAB offset 80 (`Fab.jsx:39`) vs 88 (`mockup:301`) → **80** (D-27).
14. Badge size 12px (`ICSS:137`) vs 11px (`mobile-components:95–97`) → **12px** (D-16).
15. Chip text 14px (`ICSS:117`) vs 13px (`mobile-components:93`) → **13px label** (D-08).
16. `shadow-nav` defined, never used (`TW:182`) → **deprecated** (D-10).
17. HTML configs truncate ramps at 700 yet reference 800/900 (`color-identity:305–376`); `primary.tint` exists only there → **full ramps canonical**.
18. Nav icon always outline (`BottomNav.jsx:148`) vs SOP filled-active (`ASOP:181`) → **filled active** (D-15).

## Verification of source integrity

Baseline at audit time: commit `9bcf5315ea8f3135d8250e431112e85272aa774c`, source tree hash `74386cdd619e1d3d4514981500459367a275a1ad` — unchanged at package time (see `verification-report.md`).
