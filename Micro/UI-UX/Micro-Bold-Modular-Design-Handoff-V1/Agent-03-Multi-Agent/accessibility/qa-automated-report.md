# Automated QA Report — Agent-03 Prototype

Date: 2026-09-18 · Tool: agent-browser (headless Chromium) + DOM assertions
Checks: 97 · Passed: 97 · Failed: 0

| Check | Result | Detail |
|---|---|---|
| [c1-warm-bold] fixture values verbatim (55 values) | ✅ PASS | all present |
| [c2-confident-bold] fixture values verbatim (55 values) | ✅ PASS | all present |
| [c3-dynamic-modular] fixture values verbatim (55 values) | ✅ PASS | all present |
| [c1-warm-bold] bottom nav = 5 tabs | ✅ PASS | got 5 |
| [c1-warm-bold] tab labels exact | ✅ PASS | مشروعي الآن|العمل|المالية|أدواتي|السوق |
| [c1-warm-bold] QAB = بيع|مصروف|طلب|تحصيل|المزيد | ✅ PASS | بيع|مصروف|طلب|تحصيل|المزيد |
| [c1-warm-bold] QAB labels visible | ✅ PASS | — |
| [c2-confident-bold] bottom nav = 5 tabs | ✅ PASS | got 5 |
| [c2-confident-bold] tab labels exact | ✅ PASS | مشروعي الآن|العمل|المالية|أدواتي|السوق |
| [c2-confident-bold] QAB = بيع|مصروف|طلب|تحصيل|المزيد | ✅ PASS | بيع|مصروف|طلب|تحصيل|المزيد |
| [c2-confident-bold] QAB labels visible | ✅ PASS | — |
| [c3-dynamic-modular] bottom nav = 5 tabs | ✅ PASS | got 5 |
| [c3-dynamic-modular] tab labels exact | ✅ PASS | مشروعي الآن|العمل|المالية|أدواتي|السوق |
| [c3-dynamic-modular] QAB = بيع|مصروف|طلب|تحصيل|المزيد | ✅ PASS | بيع|مصروف|طلب|تحصيل|المزيد |
| [c3-dynamic-modular] QAB labels visible | ✅ PASS | — |
| [c1-warm-bold] no horizontal scroll @320px | ✅ PASS | scrollWidth=320 innerWidth=320 |
| [c1-warm-bold] no horizontal scroll @390px | ✅ PASS | scrollWidth=390 innerWidth=390 |
| [c1-warm-bold] no horizontal scroll @430px | ✅ PASS | scrollWidth=430 innerWidth=430 |
| [c1-warm-bold] no horizontal scroll @320 (incomplete) | ✅ PASS | 320>320 |
| [c1-warm-bold] no horizontal scroll @320 (negative) | ✅ PASS | 320>320 |
| [c1-warm-bold] no horizontal scroll @320 (empty) | ✅ PASS | 320>320 |
| [c1-warm-bold] no horizontal scroll @zoom200 | ✅ PASS | 390>390 |
| [c1-warm-bold] no horizontal scroll @zoom200 (sale) | ✅ PASS | 390>390 |
| [c2-confident-bold] no horizontal scroll @320px | ✅ PASS | scrollWidth=320 innerWidth=320 |
| [c2-confident-bold] no horizontal scroll @390px | ✅ PASS | scrollWidth=390 innerWidth=390 |
| [c2-confident-bold] no horizontal scroll @430px | ✅ PASS | scrollWidth=430 innerWidth=430 |
| [c2-confident-bold] no horizontal scroll @320 (incomplete) | ✅ PASS | 320>320 |
| [c2-confident-bold] no horizontal scroll @320 (negative) | ✅ PASS | 320>320 |
| [c2-confident-bold] no horizontal scroll @320 (empty) | ✅ PASS | 320>320 |
| [c2-confident-bold] no horizontal scroll @zoom200 | ✅ PASS | 390>390 |
| [c2-confident-bold] no horizontal scroll @zoom200 (sale) | ✅ PASS | 390>390 |
| [c3-dynamic-modular] no horizontal scroll @320px | ✅ PASS | scrollWidth=320 innerWidth=320 |
| [c3-dynamic-modular] no horizontal scroll @390px | ✅ PASS | scrollWidth=390 innerWidth=390 |
| [c3-dynamic-modular] no horizontal scroll @430px | ✅ PASS | scrollWidth=430 innerWidth=430 |
| [c3-dynamic-modular] no horizontal scroll @320 (incomplete) | ✅ PASS | 320>320 |
| [c3-dynamic-modular] no horizontal scroll @320 (negative) | ✅ PASS | 320>320 |
| [c3-dynamic-modular] no horizontal scroll @320 (empty) | ✅ PASS | 320>320 |
| [c3-dynamic-modular] no horizontal scroll @zoom200 | ✅ PASS | 390>390 |
| [c3-dynamic-modular] no horizontal scroll @zoom200 (sale) | ✅ PASS | 390>390 |
| [c1-warm-bold] QAB above bottom nav (no occlusion) | ✅ PASS | ok |
| [c2-confident-bold] QAB above bottom nav (no occlusion) | ✅ PASS | ok |
| [c3-dynamic-modular] QAB above bottom nav (no occlusion) | ✅ PASS | ok |
| [c1-warm-bold] primary action visible in initial viewport | ✅ PASS | ok |
| [c2-confident-bold] primary action visible in initial viewport | ✅ PASS | ok |
| [c3-dynamic-modular] primary action visible in initial viewport | ✅ PASS | ok |
| [c1-warm-bold] incomplete hero has NO result number | ✅ PASS | ok |
| [c2-confident-bold] incomplete hero has NO result number | ✅ PASS | ok |
| [c3-dynamic-modular] incomplete hero has NO result number | ✅ PASS | ok |
| [c1-warm-bold] html lang=ar dir=rtl | ✅ PASS | ar/rtl |
| [c2-confident-bold] html lang=ar dir=rtl | ✅ PASS | ar/rtl |
| [c3-dynamic-modular] html lang=ar dir=rtl | ✅ PASS | ar/rtl |
| [c1-warm-bold] no English leakage | ✅ PASS | [] |
| [c2-confident-bold] no English leakage | ✅ PASS | [] |
| [c3-dynamic-modular] no English leakage | ✅ PASS | [] |
| [c1-warm-bold] no dead href="#" links (data-close sheets excluded by behavior) | ✅ PASS | 0 dead anchors found |
| [c2-confident-bold] no dead href="#" links (data-close sheets excluded by behavior) | ✅ PASS | 0 dead anchors found |
| [c3-dynamic-modular] no dead href="#" links (data-close sheets excluded by behavior) | ✅ PASS | 0 dead anchors found |
| [c1-warm-bold] QAB+nav touch targets ≥44px | ✅ PASS | ok |
| [c2-confident-bold] QAB+nav touch targets ≥44px | ✅ PASS | ok |
| [c3-dynamic-modular] QAB+nav touch targets ≥44px | ✅ PASS | ok |
| [c1-warm-bold] validation intercept blocks submit on 0 | ✅ PASS | url=file:///home/z/my-project/repos/Micro-Bold-Modular-Design-Handoff-V1/agent-runs/agent-03-multi-agent/prototype/c1-warm-bold/sale.html err=True |
| [c1-warm-bold] zoom200 actually enlarges text | ✅ PASS | 14.5px -> 29px |
| [c1-warm-bold] zoom200 enlarges inline styles too (multi-element) | ✅ PASS | {"body":"15.5px","cur":"16px","label":"13px"} -> {"body":"31px","cur":"32px","label":"26px"} |
| [c1-warm-bold] closed sheet hidden from focus | ✅ PASS | hidden |
| [c1-warm-bold] date field value clean | ✅ PASS | 18/09/2026 |
| [c1-warm-bold] PIN switch does not toggle theme | ✅ PASS | light -> light |
| [c1-warm-bold] success amount is ink (no green) | ✅ PASS | rgb(35, 26, 20) |
| [c2-confident-bold] validation intercept blocks submit on 0 | ✅ PASS | url=file:///home/z/my-project/repos/Micro-Bold-Modular-Design-Handoff-V1/agent-runs/agent-03-multi-agent/prototype/c2-confident-bold/sale.html err=True |
| [c2-confident-bold] zoom200 actually enlarges text | ✅ PASS | 14.5px -> 29px |
| [c2-confident-bold] zoom200 enlarges inline styles too (multi-element) | ✅ PASS | {"body":"15.5px","cur":"16px","label":"13px"} -> {"body":"31px","cur":"32px","label":"26px"} |
| [c2-confident-bold] closed sheet hidden from focus | ✅ PASS | hidden |
| [c2-confident-bold] date field value clean | ✅ PASS | 18/09/2026 |
| [c2-confident-bold] PIN switch does not toggle theme | ✅ PASS | light -> light |
| [c2-confident-bold] success amount is ink (no green) | ✅ PASS | rgb(22, 32, 43) |
| [c3-dynamic-modular] validation intercept blocks submit on 0 | ✅ PASS | url=file:///home/z/my-project/repos/Micro-Bold-Modular-Design-Handoff-V1/agent-runs/agent-03-multi-agent/prototype/c3-dynamic-modular/sale.html err=True |
| [c3-dynamic-modular] zoom200 actually enlarges text | ✅ PASS | 14.5px -> 29px |
| [c3-dynamic-modular] zoom200 enlarges inline styles too (multi-element) | ✅ PASS | {"body":"15.5px","cur":"16px","label":"13px"} -> {"body":"31px","cur":"32px","label":"26px"} |
| [c3-dynamic-modular] closed sheet hidden from focus | ✅ PASS | hidden |
| [c3-dynamic-modular] date field value clean | ✅ PASS | 18/09/2026 |
| [c3-dynamic-modular] PIN switch does not toggle theme | ✅ PASS | light -> light |
| [c3-dynamic-modular] success amount is ink (no green) | ✅ PASS | rgb(31, 28, 25) |
| [c1-warm-bold] submit link preserves state=success (P0 regression) | ✅ PASS | sale.html?state=success |
| [c1-warm-bold] submit link keeps theme AND state | ✅ PASS | sale.html?state=success&theme=dark |
| [c1-warm-bold] zero amount still blocked after P0 fix | ✅ PASS | file:///home/z/my-project/repos/Micro-Bold-Modular-Design-Handoff-V1/agent-runs/agent-03-multi-agent/prototype/c1-warm-bold/sale.html |
| [c1-warm-bold] timestamp color is darkened inkFaint | ✅ PASS | rgb(122, 106, 92) |
| [c2-confident-bold] submit link preserves state=success (P0 regression) | ✅ PASS | sale.html?state=success |
| [c2-confident-bold] submit link keeps theme AND state | ✅ PASS | sale.html?state=success&theme=dark |
| [c2-confident-bold] zero amount still blocked after P0 fix | ✅ PASS | file:///home/z/my-project/repos/Micro-Bold-Modular-Design-Handoff-V1/agent-runs/agent-03-multi-agent/prototype/c2-confident-bold/sale.html |
| [c2-confident-bold] timestamp color is darkened inkFaint | ✅ PASS | rgb(93, 111, 128) |
| [c3-dynamic-modular] submit link preserves state=success (P0 regression) | ✅ PASS | sale.html?state=success |
| [c3-dynamic-modular] submit link keeps theme AND state | ✅ PASS | sale.html?state=success&theme=dark |
| [c3-dynamic-modular] zero amount still blocked after P0 fix | ✅ PASS | file:///home/z/my-project/repos/Micro-Bold-Modular-Design-Handoff-V1/agent-runs/agent-03-multi-agent/prototype/c3-dynamic-modular/sale.html |
| [c3-dynamic-modular] timestamp color is darkened inkFaint | ✅ PASS | rgb(115, 103, 94) |
| [selected-direction] submit link preserves state=success (P0 regression) | ✅ PASS | sale.html?state=success |
| [selected-direction] submit link keeps theme AND state | ✅ PASS | sale.html?state=success&theme=dark |
| [selected-direction] zero amount still blocked after P0 fix | ✅ PASS | file:///home/z/my-project/repos/Micro-Bold-Modular-Design-Handoff-V1/agent-runs/agent-03-multi-agent/prototype/selected-direction/sale.html |
| [selected-direction] timestamp color is darkened inkFaint | ✅ PASS | rgb(122, 106, 92) |
