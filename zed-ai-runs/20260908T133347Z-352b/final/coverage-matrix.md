# Micro — Coverage Matrix

"Implemented" = a visible, interactive instance exists at the location.
"Verified" = exercised during headless verification (interaction and/or runtime audit
and/or VLM visual pass). Documented-only items do not exist here.

Legend: **T** Test Composition (`view-composition`) · **C** Components view
(`view-components`, section heading id) · **F** Foundation view · **V** Verification
view (4 live clones of T + audit panel).

## 1 · Component families

| Family / variant-state | Location | Implemented | Verified |
|---|---|---|---|
| PrimaryValueBlock — basic | C `mx-value-title` item 1 | ✅ | ✅ visual |
| PrimaryValueBlock — with state chip | C item 2 («محدّث الآن») | ✅ | ✅ visual |
| PrimaryValueBlock — with positive delta | C item 3 + T (431.100 +86.250 + freshness «محدّث الآن 09:40») | ✅ | ✅ interaction (updates on save) |
| PrimaryValueBlock — unavailable (never 0) | C item 4 («غير متوفّر») | ✅ | ✅ visual |
| MetricGroup — titled, 4 rows | T «ملخص اليوم» | ✅ | ✅ interaction (live updates) |
| MetricGroup — state sample (4 variants) | C `mx-metric-title` | ✅ | ✅ visual |
| MetricRow — plain / colored / attention / unavailable | inside both groups | ✅ | ✅ visual + 200% scan |
| CompactTile — comparison pair (نقدي/آجل) | C `mx-tile-title` | ✅ | ✅ visual |
| QuickActionRail — 5 tiles, first tinted, snap, fade | T + C `mx-rail-title` + V frames | ✅ | ✅ measured peeks 16/56/86/30 (device-true) |
| QuickActionRail — press + focus | same | ✅ | ✅ press veil (CSS) + focus ring |
| OperationalRow — financial (positive/danger) | C `mx-oprow-title` panel A | ✅ | ✅ visual |
| OperationalRow — follow-up (warning/info chips) | C panel B | ✅ | ✅ visual |
| OperationalRow — live list (4 rows + prepend) | T `data-op-list` | ✅ | ✅ save demo prepends rows |
| OperationalRow — cancelled state | C dialog demo row (`is-cancelled`) | ✅ | ✅ dialog confirm flips it |
| Button — primary (default) | C `mx-btn-title`, sheets, dialog | ✅ | ✅ press/focus |
| Button — primary loading | C matrix + every save demo | ✅ | ✅ live cycle |
| Button — primary quiet completion | C matrix + save demos («تم …») | ✅ | ✅ live cycle |
| Button — primary disabled | C matrix | ✅ | ✅ visual |
| Button — secondary / quiet / destructive / icon-only | C matrix + dialog | ✅ | ✅ visual + press |
| Input — text | C `mx-input-title`, sheets | ✅ | ✅ focus border |
| Input — amount (ltr, unit) | C + 5 sheets | ✅ | ✅ fill + save reads value |
| Input — search + clear | C | ✅ | ✅ visual |
| Input — date (DD/MM/YYYY ltr) | C + expense sheet | ✅ | ✅ visual |
| Input — select (native) | C + sheets | ✅ | ✅ visual |
| Input — error state + helper | C (`25.5` invalid) | ✅ | ✅ visual |
| Input — disabled | C | ✅ | ✅ visual |
| Segmented control (اليوم/الأسبوع/الشهر) | C `mx-choice-title` + sale sheet | ✅ | ✅ click switching |
| Tabs (نقدي/آجل/الكل) | C | ✅ | ✅ click switching |
| Checkbox | C | ✅ | ✅ toggle (CSS) |
| Switch (immediate setting) | C | ✅ | ✅ toggle (CSS) |
| State — empty (line-based + action) | C `mx-state-title` | ✅ | ✅ visual |
| State — loading (3 skeletons) | C | ✅ | ✅ live shimmer |
| State — error → manual retry → rows | C retry demo | ✅ | ✅ live flow |
| State — offline/local-save | C | ✅ | ✅ visual |
| State — pending (decision) | C + T row chip | ✅ | ✅ visual |
| State — conflict | C | ✅ | ✅ visual |
| State — failed (with retry) | C | ✅ | ✅ visual |
| State — completed | C + save demos | ✅ | ✅ live (incl. entry-ID «قيد NNNN» proof on the new row + announcement) |
| State — cancelled | C (row + state card) | ✅ | ✅ live via dialog |
| State — reversed | C | ✅ | ✅ visual |
| Sheet — reference (expense, 4 fields) | overlay layer; T rail + C trigger | ✅ | ✅ open/focus/fill/save/drag/Esc |
| Sheet — compact (collect/sale/purchase/payment) | overlay layer ×4 | ✅ | ✅ collect opened; sale/purchase/payment openable |
| Dialog — destructive confirm | overlay layer; C trigger | ✅ | ✅ confirm applies + announces |
| BottomNavigation — live sticky | T | ✅ | ✅ active switching |
| BottomNavigation — static anatomy | C `mx-nav-title` | ✅ | ✅ visual |
| TopZone — integrated + Avatar single entry | T + C | ✅ | ✅ visual |
| Chart — sparkline + direct peak marker | C `mx-chart-title` | ✅ | ✅ visual + text alt |
| Chart — planned-vs-actual (dashed/solid + 2 labels) | C | ✅ | ✅ visual + text alt |
| Chart — target meter (62% + tick) | C | ✅ | ✅ visual + aria |

## 2 · Foundations

| Item | Location | Implemented | Verified |
|---|---|---|---|
| Three surface roles (nested demo) | F `fv-surface-title` | ✅ | ✅ visual |
| Brand family (atmosphere w/ ink text, tint, ink) | F `fv-brand-title` | ✅ | ✅ visual |
| Ink ramp + lines | F `fv-ink-title` | ✅ | ✅ visual |
| Four semantic families (realistic chips + values) | F `fv-sem-title` | ✅ | ✅ visual |
| Type scale (32/15/14/13, weights, tabular column) | F `fv-type-title` | ✅ | ✅ visual |
| Spacing scale + radius + edge rule | F `fv-space-title` | ✅ | ✅ visual |
| Icon mirror registry (mirror vs never) | F `fv-icon-title` | ✅ | ✅ CSS-verified flip |
| Motion scale + press demo chip | F `fv-motion-title` | ✅ | ✅ press veil |

## 3 · Cross-cutting rules

| Rule | Check | Status |
|---|---|---|
| Light mode only (no .dark / prefers-color-scheme) | grep + runtime scan | ✅ 0 occurrences |
| Currency «د.أ» only, never JOD | grep + runtime scan | ✅ 0 occurrences |
| English digits in all values | runtime scan | ✅ 0 Arabic-Indic |
| Arabic ≥14px everywhere incl. «د.أ» units (rail labels 13px = spec-pinned exception; 13px digits/Latin only) | CSS audit + AC-03 fix | ✅ (CompactTile/chart-head units were 13px — corrected to 14px before upload) |
| 44/48px targets, 8px gaps | runtime audit | ✅ 0 violations |
| ≤2 semantic families / ≤2 colored numbers / 1 brand fill / 1 tinted tile / ≤3 dividers in T | composition review | ✅ (positive+danger; +86.250 & −182.500; primary CTA in sheets; tile 1; 2 content hairlines + nav chrome) |
| One PrimaryValueBlock / one rail / one MetricGroup / one scroll owner in T | structure | ✅ |
| No paper-plane icon | sprite audit | ✅ absent |
| No count-up / bounce | code review + demo runs | ✅ values land instantly |
| Reduced motion (toggle + system) | toggle + CSS | ✅ |
| 320/360/390/430 no overflow @100% & @200% | runtime audit | ✅ 0/0 all frames |
| RTL default + LTR geometry check | toggle | ✅ (screenshot 13) |
