# Verification Checklist — Agent 04 (Executable, Run Against the Built Library)

Run: `20260908T133347Z-352b` · Task `2-d` · Execute in Task 4 **verbatim**.
`<ART>` = the built artifact root (e.g. `RUN_ROOT/final/`). Every item is objectively checkable: a measurement, a grep, a frame-count, or a yes/no on a screenshot. Record PASS / FAIL / N-A per item; **any FAIL is a build-blocker** unless it is one of the three documented exceptions (E-320 rail peek 16px; ink-disabled contrast; line-soft/line-strong decorative-only).

**Harness setup (applies to all groups):**
- Viewports (portrait only): **320×568, 360×740, 390×844, 430×932**.
- Default direction: `dir="rtl"`, `lang="ar"`. LTR check: re-render same pages with `dir="ltr"` (geometry-only check — Arabic copy is expected to remain Arabic).
- Text scale: inject `document.documentElement.style.fontSize` = `16px` (100%) / `20.8px` (130%) / `32px` (200%). Valid only because all font sizes are in `rem`.
- Reduced motion: emulate `prefers-reduced-motion: reduce` (DevTools → Rendering, or Playwright `emulateMedia({reducedMotion:'reduce'})`).
- Measurement: DOM `getBoundingClientRect()` via console/Playwright; screenshots for visual items.

---

## A. Viewport & overflow (320 / 360 / 390 / 430)

1. **Full-set screenshots** — Screenshot every composition at all 4 widths, 100% scale, RTL. PASS: all four sets exist and render (no blank frames, no rendering errors).
2. **No horizontal overflow** — At each of the 4 widths × 3 text scales × 2 directions run `document.scrollingElement.scrollWidth <= window.innerWidth` (and no element's bounding box exceeds the viewport right/left edge by >1px). PASS: true for all 24 combinations.
3. **Edge integrity** — Inspect screenshots at 320 and 430: no text touches the screen edge (<8px from either side), no cut-off glyphs at the line-clamp or wrap boundary. PASS: zero clipped glyphs.

## B. Direction & bidi geometry

4. **RTL is default** — `<ART>` pages declare `dir="rtl"`/`lang="ar"` at the document level. PASS: attribute present; layout starts at the right edge (padding/margins symmetric mirror).
5. **LTR geometry-only check** — Same page with `dir="ltr"`: layout mirrors (rail scroll starts left, sheet primary button right-anchored… left-anchored), no overlapping elements, no untranslated geometry bugs (icons that overlap text, negative margins). PASS: mirrored without breakage; Arabic strings may remain Arabic.
6. **Bidi money rendering** — On any negative amount demo, the on-screen order is `د.أ` then the LTR cluster `-182.500` (minus welded to the digits). Test: screenshot + zoom; also `bdi`/`dir="ltr"` present in markup (`rg -n 'dir="ltr"' <ART>` finds the value wrappers). PASS: rendering matches scenario table in `accessibility-rtl-report.md` §(d); no `182.500-`, no detached minus.
7. **Bidi mixed sentence & date & percent** — Strings "دفع خالد 150.000 من أصل 1,312.400", "08/09/2026", "+9%" each render as specified (numbers intact LTR, date DD/MM/YYYY, `+9%` with plus left of digits). PASS: screenshot comparison per §(d); any digit reordering = FAIL.

## C. Text scaling (100 / 130 / 200)

8. **Scaling propagates** — With root font 32px, ALL text visibly scales (spot-check nav labels, metric values, qualifiers). PASS: no text stays fixed-size (no stray `px` font sizes: `rg -n 'font-size:\s*\d+px' <ART>` → 0 in component CSS).
9. **Primary value at 200%** — At 320px + 200%, the 32px value block wraps (currency to its own line) and remains fully visible. PASS: no clipping, no `…`, no letter-spacing tricks, no overlap with neighbors.
10. **Metric rows at 130/200** — Labels wrap to ≤3 lines, values never truncate, row height grows, dividers still span full width. PASS on screenshots at 360×390.
11. **Bottom nav at 200%** — Labels wrap to ≤2 lines or nav grows; no ellipsis, no clipped descenders (Arabic ي/ج tails). PASS at 320.
12. **Min font sizes** — Scan computed styles: every user-facing Arabic text ≥14px; 13px only on qualifier/QuickActionRail-label classes. Test: console snippet listing elements with computed font-size < 14px → all must be `qualifier`/`rail-label` classes. PASS: no violations.

## D. Reduced motion

13. **Media query honored** — With reduced motion emulated, sheet opens without slide (≤100ms fade or instant), dialog without scale, skeletons static, no shimmer loops. PASS: video/frames show no spatial movement on state changes.
14. **State meaning preserved** — Static before/after screenshot pair (sheet closed/open; loading/idle; default/selected): state difference still perceivable without animation. PASS for every demo.
15. **No motion-only affordances** — No meaning is carried by movement alone (e.g., a "pending" state that is only a pulsing dot). PASS: pending states have word/icon signals (§g rules).

## E. Currency & digits (grep-enforced)

16. **"JOD" forbidden** — `rg -in '\bJOD\b' <ART>` → **0 matches**. Currency appears only as `د.أ`. PASS: grep exits empty.
17. **English digits only in values** — `rg -n '[٠-٩۰-۹]' <ART>` → 0 matches anywhere in markup/JS string literals. PASS: grep exits empty.
18. **3-decimal fils** — Every money value in demos renders exactly 3 decimals (`431.100`, `1,312.400`, `150.000`). PASS: screenshot + `rg -n '\d+\.\d{3}\b'` shows the pattern is used; no 2-decimal or 0-decimal money strings.
19. **Date format** — All user-facing dates are DD/MM/YYYY (`rg -n '\d{2}/\d{2}/\d{4}'` present; `rg -n '\d{4}-\d{2}-\d{2}' <ART>` → 0 user-facing ISO matches). PASS: both conditions hold.

## F. Light-mode only

20. **No dark theme code** — `rg -in 'prefers-color-scheme|\.dark\b|data-theme|color-scheme:\s*dark' <ART>` → 0 matches. PASS: grep exits empty.
21. **Colors are the exact tokens** — Audit CSS custom properties against the 22 spec hex values (`#FAF9F5, #FFFFFF, #F0EEE6, #CC785C, #F7EAE4, #964E33, #1F1E1D, #33322E, #6E6A60, #767265, #B7B2A6, #EAE6DC, #DED9CB, #2E7D57, #E7EFE7, #B42318, #F7E7E2, #8A6520, #F4EDD8, #3E5C76, #E8EDF1`). PASS: every token present, none redefined, no off-spec hex in component CSS.

## G. Color budget (per composition — count on each gallery screen)

22. **≤2 semantic color families** — Count distinct semantic hues (positive/danger/warning/info) used per composition. PASS: ≤2 everywhere (chart legends exempt within chart primitives, still ≤3).
23. **≤2 colored numbers** — Count numbers rendered in a semantic color per composition. PASS: ≤2; all other numbers in ink tokens.
24. **1 filled brand action** — Exactly one brand-ink-filled button per composition (primary action). PASS: count = 1 (0 or ≥2 = FAIL).
25. **≤1 tinted tile** — Count tint-background tiles (brand/semantic tints) per composition. PASS: ≤1 tinted tile + status chips (chips are components, not tiles).
26. **≤3 dividers** — Count horizontal rule elements per composition. PASS: ≤3.
27. **≤2 nested surfaces** — Count surface-in-surface nesting depth (surface on canvas = 1; card in card = 2). PASS: max nesting 2.

## H. Component coverage matrix (each family must have a visible demo showing its variants/states)

28. **PrimaryValueBlock** — demo with label, 32px value (bdi, English digits, د.أ), delta line, update timestamp, and an *unknown* variant ("غير متوفر"). PASS: both variants present; exactly one per composition (see item 56).
29. **MetricGroup** — demo with 2–4 MetricRows incl. a warning row and an info row. PASS: visible, spacing consistent.
30. **MetricRow** — label + value + qualifier + optional icon; states: plain, warning, info. PASS: all three rendered; non-color signals per §(g).
31. **CompactTile** — tinted tile with icon + number + label; 13px qualifier allowed. PASS: present; icon ≥3:1 on tint (per computed table).
32. **QuickActionRail** — horizontally scrollable, tiles 88×92, 13px labels, ≥28px peek at 360/390/430, 16px at 320 (see item 58 for measurement). PASS: present with ≥5 tiles so peeks are testable.
33. **OperationalRow** — customer/stock row: name, amount, status chip (word + icon + tint), disclosure chevron mirrored. PASS: rendered; chip not color-only.
34. **Button** — matrix: primary (brand fill, white text, 48px), secondary (outline/quiet, 44px), destructive (danger fill, white), disabled, loading (spinner + fixed width), completion (check + "تم الحفظ"). PASS: all 6 states visible.
35. **Input** — labeled text field: label ink, resting border line-strong + label pairing, focus ring ink-strong 2px/2px offset, error state (danger tint + icon + Arabic message), amount-display variant (bdi, 3-decimal, د.أ). PASS: all states rendered.
36. **State** — gallery: empty, loading (skeleton ×3), offline (info banner + cached value), pending ("معلّق" badge), unknown ("غير متوفر"), failed (retry action). PASS: all 6 present with correct wording.
37. **Sheet** — demo: opens 240ms, scrim 45%, drag handle, primary 48px button, focus trap + return. PASS: interactive demo exists (see item 47).
38. **Dialog** — confirm + destructive demos; destructive = danger-filled confirm + consequence-stating title. PASS: both present.
39. **BottomNavigation + top zone** — 4 tabs, persistent Arabic labels ≥14px, active state = weight + indicator + icon treatment (not color alone); top zone (title/identity) exists without primary actions. PASS: rendered at all 4 widths.
40. **Chart primitives** — planned/actual/forecast demo: solid/dashed/dotted textures + direct Arabic labels at line ends; time axis LTR inside the chart in RTL mode; text alternative present. PASS: grayscale the screenshot — all three series still distinguishable (texture survives).
41. **Keypad** — amount keypad demo: ASCII digits, ≥48px keys, ≥8 gaps, backspace, live 3-decimal display, press overlay. PASS: present and measurable (see item 50).

## I. Interaction demos (exercise each contract)

42. **Press** — Pointer-down on button/row/tile/keypad key: 8% ink overlay visible within 80ms (frame-step a 60fps screen recording); no scale/motion change. PASS: overlay in frame ≤5, text contrast ≥4.5 mid-press (values from report §a composites).
43. **Selection** — Chip/tab/row selection states: selected state perceivable in static screenshot (fill/weight/indicator, not color-only); keyboard selectable (arrows in rail/nav). PASS: both.
44. **Loading** — Button→spinner+label at identical bounding box (±1px); list→3 skeletons matching row geometry; no full-screen spinners. PASS: box measurement + screenshot.
45. **Completion** — Save demo: check + "تم الحفظ"/"تم تسجيل الدفعة" + entry-ID proof + value updates discretely. Frame-step the value change: **no intermediate numbers** (no count-up). PASS: old number → new number in consecutive frames.
46. **Error retry** — Failure demo: exactly 1 auto retry, then Arabic error + "أعد المحاولة" ≥44px; typed data preserved; retry completes per contract. PASS: event log shows 2 attempts max, input intact.
47. **Sheet open/dismiss** — Timings 240ms±40 open / 180ms±40 close; dismiss by swipe (≥40px commit, <40px returns), Esc, scrim tap; focus trapped inside, returns to trigger on close. PASS: all measured/observed.
48. **Dialog destructive** — 160ms±30/120ms±30; Esc = safe action; Enter on confirm fires once (rapid ×5 → 1 event). PASS: timings + single event.
49. **Reduced motion pass-through** — Repeat 42/45/47/48 with reduced motion: all states still reachable and perceivable, no spatial animation. PASS: same outcomes without movement.

## J. Touch targets & focus

50. **Target sizes** — Console audit of all interactive elements (`a, button, [role=button], input, select, [tabindex]:not([tabindex="-1"])`): `min(w,h) ≥ 44` for all, `≥ 48` for elements in `.primary`/keypad keys/sheet confirm. PASS: zero violations (print the offending list — must be empty).
51. **Gaps** — For sibling interactive targets in the same group (buttons, rows, rail tiles, chips): center-to-center separation ensures ≥8px gap between hit boxes (rail: 8 exactly ✓). PASS: no touching hit boxes outside the segmented bottom nav.
52. **Focus visibility** — Tab through every page: each interactive element shows the 2px ink-strong ring (screenshot each), nothing skips, ring never clipped; mouse click does NOT paint a ring. PASS: 100% coverage, zero clipped rings.

## K. Content & data-display rules

53. **Unknown ≠ zero** — Every unknown-value demo shows "غير متوفر" (or em-dash + info icon), never `0.000`. PASS: screenshot check; `rg -n 'غير متوفر' <ART>` finds the state demos.
54. **Negative sign primary** — Negative amounts render with a leading minus welded to the digits inside the bdi (never parentheses, never trailing minus, never color-only). PASS: demo present + rendered as scenario 1.
55. **Chart text alternatives** — Every chart demo has a text alternative (visually-hidden table with the series values, or an `aria-label`/`aria-describedby` summary in Arabic). PASS: `rg -n 'aria-label|sr-only|visually-hidden' <ART>` hits each chart; screen-reader tree shows the summary.
56. **One PrimaryValueBlock per composition** — Count per gallery composition: exactly 1. PASS: count = 1 everywhere.
57. **Trust wording** — No infrastructure jargon in primary cards: `rg -in 'sync|مزامنة|server|خادم|API|token|cache|كاش' <ART>` → 0 matches in user-facing demo strings (footnote "محفوظ على الجهاز" allowed). PASS: grep clean.

## L. Anti-patterns & special measurements

58. **Rail peek measurements** — Measure the first partially visible rail tile's on-screen width: 320 → **16px (documented exception)**, 360 → ≥28, 390 → ≥28, 430 → ≥28. PASS: measured values meet thresholds; the 320 exception is documented in the rail's comment/docs.
59. **No fake system UI** — No drawn status bar, battery, clock, notch, or home indicator: inspect top/bottom of every screenshot + `rg -in 'status-bar|notch|battery|home-indicator' <ART>` → 0. PASS: app-owned pixels only.
60. **No paper-plane icon** — `rg -in 'paper|plane|telegram|send\b' <ART>` → 0 icon class/SVG matches; visual scan of all icons confirms no paper-plane glyph; send/save actions use Arabic text labels. PASS: both checks.
61. **No toast-only proof / no count-up** — Search demos for completion flows: every save confirmation persists on screen (record/entry state), none exists only as a transient toast; no numeric tween code (`rg -in 'requestAnimationFrame|count-up|odometer|tween' <ART>` → 0 in component JS, or demos show discrete value change per item 45). PASS: both.
62. **No page-wide slide transitions / no spring** — Tab/section navigation swaps content without full-page slide (≤120ms crossfade or instant); no bounce/overshoot anywhere except the sheet-cancel spring-back ≤150ms ≤40px. PASS: video review of all navigation.

---

**Scoring:** 62 items. FAIL on any item = blocker for Task 3 delivery, except documented exceptions: item 58@320 (16px peek), ink-disabled contrast (item 21 token audit must still pass), line-soft/line-strong usage limited to decorative dividers (item 35 pairing). Attach the completed checklist, screenshots, and grep outputs to the run report.
