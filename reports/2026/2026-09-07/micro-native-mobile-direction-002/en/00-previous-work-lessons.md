# 00 — Previous Work Lessons

**Delivery:** `micro-native-mobile-direction-002` · Stage 0 · 2026-09-07
**Author:** central orchestrator
**Inputs read in full or in part:** `micro-visual-product-concept-001` (Warm Ledger) and `micro-visual-product-concept-002` (Calm Ledger) — syntheses, lessons tables, review requests, metadata, QA screenshots (including `01-today-390-light-ar.png` and `shot-01-home-light-ar.png`).

**Standing verdict (restated from the task and confirmed by this audit):** both previous deliveries are **rejected as final visual directions** because they read as web compositions rendered inside a phone frame — a design-review artifact, not a native mobile product. Their *decisions and behaviors* can still be kept, some of their *principles* can be adapted, and large parts of their *visual language* must be explicitly rejected. Their internal scores (7.90/10, 28/30) carry **no authority** in this delivery; neither predicted the owner's rejection.

This file sorts everything the audit found into four buckets. It is the shared ground truth that the five specialists and the synthesis build on.

---

## 1. Keep as a decision or behavior

These are measured or product-level decisions that survive the rejection of both visual languages. They are adopted as-is unless a later measured audit overturns them.

| # | Kept decision / behavior | Source | Why it survives |
|---|---|---|---|
| K-01 | **Contrast doctrine:** white text never rests on `#cc785c` (3.28:1) or `#079fa0` (3.24:1); `#964e33` + white (6.11:1) is the only legal terracotta resting action fill; `#b4613f` (≈4.45:1) is **press-only** and must never be described as a passing pairing | 001 D1–D2, 002 measured pairs (34 scripted pairs) | Computed, documented, and consistent with the fixed audit; re-verified conceptually this run |
| K-02 | **Dark roles are deliberate, not inverted:** dark action uses `#8fd5d6`-family foregrounds/backgrounds with measured pairings; dark stays warm (`#332d27` surfaces) | 002 §5.1 | Prevents the classic "inverted light theme" web smell |
| K-03 | **Honest financial states:** unknown is never a confident `0.00` — «قيمة غير محددة بعد» / «سجّله»; estimated carries تقديري marking; pending/offline/syncing/synced/conflict/cancelled/reversed/correction are first-class, visible states | 001 D6–D7, 002 DSY-15/16 | This is the product's trust core, independent of styling |
| K-04 | **State grammar is glyph+label, color tertiary:** shape + word carries meaning; color only reinforces; alerts use `role="alert"` and are never quiet chips | 002 DSY-15, 001 D7 | Accessibility + honesty; survives any palette |
| K-05 | **Bidi contract:** isolate **digits only** in `<bdi dir="ltr">`; the unit «د.أ» stays in the RTL flow *after* the number; signs live inside the isolate; dates isolated; avoid parentheses around money | 002 DSY-04 | Correctness issue, not style; prevents «د.أ 20.00» rendering bugs |
| K-06 | **Numerals:** ASCII digits everywhere in v1 (input = display; receipts match paper), `tabular-nums`, decimal-aligned money columns | 002 DSY-05/07, 001 D5 | Owner-verified convention (Jordanian context) |
| K-07 | **Arabic legibility floors:** nothing below 13px; body 15px; rows ≥56px; line-height ≥1.6; **never letter-space Arabic** (breaks joins) | 002 DSY-06, 04 report | Hard floor from RTL specialist review |
| K-08 | **Quiet completion:** saving resolves to a closure sentence with final digits + a single localized highlight; **never** counters, confetti, applause, or overshoot | 002 DSY-18, 001 motion report | Motion-as-meaning doctrine |
| K-09 | **Effect preview before irreversible actions** (e.g., correction: will-change / won't-change lists in a center dialog) | 001 conflict alert, 002 CorrectionPreview | Trust behavior for money actions |
| K-10 | **Chart honesty contract:** a chart exists only to answer a real question; carries period + unit + source state + a text interpretation that IS the non-visual alternative; unrecorded ≠ zero (gap + footnote) | 002 DSY-14, 001 charts | Prevents decorative chart panels |
| K-11 | **Review controls live strictly outside the product surface**; the product frame contains only product UI | 001 lessons row 2, 002 DSY-01 | Directly implicated in the failure; must be kept but enforced harder (see R-01/R-02) |
| K-12 | **Thumb-zone discipline:** primary capture action in bottom reach; safe areas; 44pt minimum targets (48 for primary/keypad); ≥8px separation | both, 002 DSY-20 | Native ergonomics, independent of looks |
| K-13 | **Format constants:** JOD with «د.أ»; `DD/MM/YYYY`; realistic Jordanian Arabic content; long-name/long-number stress testing | fixed constraints + both | Non-negotiable identity constraints |
| K-14 | **Coverage honesty:** out-of-scope surfaces are named with reasons rather than faked; missing sources documented, never invented | 002 §4, 001 intake | Delivery integrity rule |
| K-15 | **Deeper operational coverage of 001 is a useful checklist** (capture flow, effect previews, conflict alerting, purchases with received-value bridge) even though its look was rejected | 001 synthesis §4 | Behavior coverage, not visuals |

## 2. Adapt as a principle

These were the right *ideas* expressed in the wrong *medium*. This delivery keeps the idea and re-grounds it in native application anatomy.

| # | Principle | How the previous deliveries expressed it | How it must be adapted |
|---|---|---|---|
| A-01 | "Composition is the differentiation lever, not color" | 001: hero truth block + full-width bands; 002: ruled ledger page | The lever is right, but composition must come from **application anatomy** (app bar, nav destinations, stacks, sheets, list grammar) — not from web page sections or print composition |
| A-02 | One dominant truth block per screen | A tinted hero card (001) / a 34px figure at top (002) | Truth must be **structural** — part of the screen's persistent header region / first scroll moment — never a decorative rounded card floating in a column |
| A-03 | Fixed amount column, decimal alignment | 88px LTR-isolated column (002) | Keep the discipline; express it in native row grammar per direction (list rows, event lines, or numeric surfaces) |
| A-04 | Countable calm (quotas) | ≤8 blocks, ≤1 card, ≤5 today rows (002) | Keep quotas; re-derive them for native lists/sheets (e.g., "one screen = one question; details are pushes; actions are sheets") |
| A-05 | Warm, deliberate neutrals | canvas `#faf6f2`, two-tone dark `#1c1815`/`#332d27` (002) | Neutrals are free design space; each new direction may tune them, but warmth + measured pairings remain the rule |
| A-06 | Question-led headers («ماذا أعلى اليوم؟» style) | 002 headers as owner questions | Strong, distinctive; keep, but render as native large-title / compacting header behavior, not a document H1 |
| A-07 | Large, safe money entry (NumericSurface discipline) | 6+2 slot grid, stable digits, pinned underline | The *discipline* (big digits, visible state, tap+swipe alternatives) feeds the new keyboard-aware capture forms; the exact slot widget is not sacred |
| A-08 | 320px-first verification arithmetic | DSY-24 | Keep: build for 320 first, then confirm 360/390/430 |
| A-09 | Motion register (80–280ms classes, zero overshoot, meaning-only) | 002 DSY-02, 001 tokens | Keep the register; *add* what was missing: **transition grammar connected to navigation events** (push/pop/sheet/tab), which both deliveries largely ignored because they had no real navigation model |
| A-10 | Five-seat destination vocabulary «مشروعي الآن · العمل · سجّل · مالي · أدواتي» | 001 D9 (from an older target-state doc) | The *count and thumb placement* are sound; the exact seat set must be re-derived for a native information architecture and re-confirmed by the owner |

## 3. Reject as visual language

This is the core of the owner's complaint. None of the following may reappear.

| # | Rejected pattern | Seen in | Why it fails the "native" bar |
|---|---|---|---|
| R-01 | **Phone bezel + fake status bar (09:41 / 8:26, battery, signal icons) on a dark desktop stage** | 001 screenshot; 002 phone frame | Mockup theater. A real app screenshot needs no costume; the bezel tells the reviewer "this is a picture of an app," which is exactly the category error |
| R-02 | **Desktop review console as the dominant visual experience** — wide control strips, demo buttons, annotated side columns with spec prose | 002 screenshot (control bar + comparison columns + caption banner); 001 caption under phone | The reviewer's eye lands on the *review apparatus*, not the product. The product screen must be the first and main thing |
| R-03 | **Stacked rounded cards/banners as the default composition** (offline banner card, hero card, white band cards) | 001 | Card-wall = web dashboard grammar; every surface announces itself as a floating box instead of an organized screen |
| R-04 | **Document-flow composition inside the screen** — headings, rules, and paragraphs scrolling like an article page | 002 in-frame feel | A ledger page is a beautiful idea for *content*, but with no visible app chrome (nav bar behavior, back affordances, section logic) it reads as a styled web page |
| R-05 | Fake device chrome as substitute for real app behavior | both | Status bars and bezels were used *instead of* real stack transitions, back behavior, and sheet mechanics |
| R-06 | Terracotta as atmosphere everywhere (spines, washes, tinted hero slabs) | 001 | Decorative color erodes the action hierarchy; terracotta must be scarce and structural |
| R-07 | Stat tiles, chart panels, and SaaS dashboard rhythm | 001 (partially), anti-reference lineage | The exact generic look the owner rejects |
| R-08 | Equal-tile settings grids | 001 lessons | No reading order; breaks scanning |
| R-09 | Scores presented as design authority (7.90/10, 28/30) | both | Internal rubrics did not predict the owner's verdict; this delivery reports rationale, not scores-as-proof |
| R-10 | Spec prose and coverage lists visible *around* the product as part of the review experience | 002 | Review narrative belongs in `en/` documents and the review index, never framing the product screen |
| R-11 | Page-fade "transitions" or no transitions at all | both (effectively) | Transitions disconnected from navigation events are a defining web tell; native transition grammar is mandatory |
| R-12 | Jordanian decorative motifs (shemagh, maps, mosaics, ornaments) | — (postponed by constraint) | Fixed constraint; repeated here as a standing rejection |

## 4. Needs independent verification

Carried from both deliveries as open items; this delivery does **not** inherit them as settled.

| # | Item | Why it needs verification |
|---|---|---|
| V-01 | RTL chart time-flow (earliest at right) with real owners | 002 flagged it as an open usability question; plausible but unproven |
| V-02 | Screen-reader pronunciation of «د.أ» and amount strings | Never tested with an actual screen reader |
| V-03 | Haptics policy | Both deliveries deferred; device-only question |
| V-04 | Real-device behavior: keyboard avoidance, safe areas, edge-swipe back, scroll ownership | Neither delivery touched hardware; all claims are browser-level |
| V-05 | Typography path (Noto Sans Arabic + Inter digit font, or a single face) | Review-only decision; production choice was left as a Stage-4 gate |
| V-06 | Destination set / information architecture for a native app | The five-seat shell came from an older target-state doc; must be re-derived and re-confirmed for the native direction |
| V-07 | All inherited "verified" claims (contrast pairs, coverage, console-error counts) | Inherited evidence is accepted as documentation but is re-checked only where this delivery re-measures; anything not re-measured is labeled inherited |

## 5. Missing sources (documented, not invented)

Repo-wide search on 2026-09-07 confirmed the following are **absent** from the repository:

- `micro-agent-input.zip` — **absent**
- `micro-recovery-docs.zip` — **absent**
- `MicroPrimitives-anti-reference.html` — **absent**

Nothing about their contents was invented. Their relevant decisions are available through the prior reports' documentation (both previous deliveries recorded the same absence) and through this task's fixed constraint block, which is treated as authority level 1. Continuation is safe: the constraint register and the repository's own reports are sufficient grounding for a visual-direction delivery.
