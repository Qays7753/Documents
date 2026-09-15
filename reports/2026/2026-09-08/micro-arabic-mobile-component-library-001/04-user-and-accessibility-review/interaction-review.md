# Interaction Review — Targets, Thumb Zones, Motion, Dismissal, Lists

Agent 04 · Task 3 · Run `20260908T133450Z-16d11`. Audited against the proposals of Agents 01–03 (contracts, tokens.css `--mc-motion-*`/`--mc-geometry-*`, `component-architecture.md` §7–9, `variant-state-matrix.md`). Every finding ends in a concrete fix.

---

## 1. Touch-target audit (44px minimum, 48px primary, 8px adjacent gap)

| Component | Proposed target | Verdict |
|---|---|---|
| QuickActionRail tile | 88×92 | PASS (≈2× minimum) |
| Button primary / secondary / quiet | 48 / 44 / 44 | PASS |
| Button icon-only | 44×44 | PASS |
| Input fields / amount / date | 48 | PASS |
| Segmented / tab | 44 | PASS |
| Checkbox / switch visual | 20 / 48×28 on 44px targets | PASS |
| BottomNavigation seat | 64px+ (320px: 64) | PASS |
| Avatar | 32 visual / 44 hit | PASS |
| MetricRow / OperationalRow / CompactTile | 44 / 56 / 84 | PASS |
| State chip | 28px, non-interactive | PASS (hit via whole row) |
| **Quick-fill chip (`240.00` in collection sheet)** | 28px chip, but **tappable** | **FAIL** |
| **Sheet drag handle** | 32×4 visual | **FAIL unless hit area ≥44px** |

Fixes: (a) any **tappable** chip (quick-fill `240.00`, date quick chip `اليوم`) must expose a ≥44px hit area — render as a 44px secondary button or grow the chip hit box with invisible padding; the 28px spec applies only to non-interactive state chips. (b) The drag handle's touch region must be ≥44px tall (invisible padding around the 32×4 visual, or the whole sheet header draggable); Escape and scrim tap remain the guaranteed alternatives. Adjacent gaps: rail gap 8 ✓, button pairs 8 ✓; contiguous nav seats are a platform pattern (documented exception). Micro's 44/48 rule also exceeds WCAG 2.2 §2.5.8 (24px AA) — the Micro rule wins and stands.

## 2. One-hand thumb-zone mapping

The rule "read high, touch low" is respected: sheet CTAs are bottom-pinned inside the sheet footer (thumb zone by construction); BottomNavigation occupies the bottom band; the rail sits at the top of the comfortable stretch band with 88×92 targets — acceptable as a single confident strike. Two placements fail the rule: (1) the **inline retry button** on failed rows sits mid-screen at the row's inline-end — visual left in RTL, the far side for a right thumb; fix: row tap opens the detail sheet with the retry bottom-pinned (inline retry stays for glance use). (2) The **Avatar** is top-end, but it is low-frequency profile entry — acceptable, documented. WCAG 2.2 §2.4.11 (Focus Not Obscured, AA): the scroll owner must set `scroll-padding-bottom` ≥ 64px + safe-area so a focused row near the bottom is never hidden behind the persistent nav — **add this to the base CSS layer** (currently absent from all three proposals).

## 3. Motion contract vs SPEC §6.11

Verified in tokens.css: press 80ms, fast 120ms, normal 200ms, sheet in/out 240/180ms, dialog in/out 160/120ms, scrim 200ms — all spec-exact. Easings `cubic-bezier(0.2,0,0,1)`, `(0.05,0.7,0.1,1)`, `(0.3,0,0.8,0.15)` have all control points within [0,1] — **computed: no overshoot, hence no bounce/spring** ✓. No count-up: values render immediately; skeletons pulse via a 200ms opacity loop only; the sheet's drag is finger-follow with no rebound. One inconsistency: Agent 01 says dialogs enter "fade-scale-less" at 160ms while Agent 03 says "scales/fades 160ms". **Fix (Agent 05):** unify — dialog enters with opacity + 0.97→1 scale over 160ms (native feel, still no overshoot); reduced-motion uses opacity only. Under `html[data-motion="reduced"]` all spatial transitions collapse to 0ms: sheets/dialogs appear in place, scrim is instant, skeletons are static, the switch knob snaps, and state meaning (loading/error/completed indicators) is preserved — exactly the SPEC §6.11 requirement; make each of these an interactive Verification-view proof, not a prose claim.

## 4. Sheet and dialog dismissal rules

The proposed contract: scrim tap, Escape, and drag-to-dismiss (40% threshold or velocity) close sheets; focus is trapped while open and returns to the invoker; the page behind does not scroll. This matches phone-native behavior and WCAG §2.1.1/2.1.2 (drag has tap/Escape alternatives). Three gaps:

1. **Destructive dialogs ignore Escape and scrim.** Agent 03 flags this for my challenge. Ruling: **keep it** — an accidental Escape must not dismiss a destructive confirm — on three conditions: `إلغاء` is a real focusable button reachable by Tab (so no keyboard trap), the destructive action is never the initially focused control, and the decision is logged in `decision-log.md` as a deliberate Micro-over-generic deviation.
2. **Dirty sheets must route all dismissal routes through the guard.** Scrim tap, drag, Escape, and back gesture on an edited sheet must open `تجاهل التغييرات؟` — none may silently discard (money records). Currently only "dismiss attempt" is specified.
3. **Focus return must survive the guard chain**: sheet → guard dialog → cancel must return focus to the *sheet*, not jump to the page. Specify the invoker chain explicitly in the JS module contract.

Reduced-motion dismissal: drag reduces to a tap threshold (already specified); scrim and Escape are unaffected — meaning preserved without spatial animation ✓.

## 5. Segmented, tab, and switch immediacy

Correct per SPEC §6.9.7: switches appear only for immediate settings and toggle instantly (80ms knob shift; instant under reduced motion) with `aria-checked` mirrored; segmented selection moves in 120ms with `aria-pressed`; tabs crossfade content in 120ms with `aria-selected`/`aria-current`. Mode segments are capped at two options and tabs at three (`اليوم | الأسبوع | الشهر`) so neither ever scrolls at 320px ✓. One check to add at 200% text scale: tab labels at 26px must still fit 288px of content width without clipping — JS-measure in Verification (wrap gracefully, never truncate).

## 6. List behavior and empty states

The contracts specify: 20-row batch, prefetch triggered within the last 5 rows, 3 skeleton rows while fetching, automatic retries stop after the first failure with a visible `إعادة المحاولة`. All correct; the risk is implementation drift — these numbers are contract-level, so the final lab must demonstrate them **interactively** (scroll the picker list to row ~15 and show 3 skeletons appearing, then the next batch; trigger one failure and show that no second automatic attempt occurs). Empty states are line-based with one useful action (`لا عمليات اليوم` + `سجّل بيعًا`; `لا نتائج مطابقة` + `مسح البحث`) — no illustration theatre ✓. Empty search exposes the clear action as a ≥44px quiet button ✓. Loading regions announce once via `aria-busy` + a single live announcement, not per row ✓.

## 7. Findings and required fixes for Agent 05

1. Tappable chips (quick-fill, date quick chips) → ≥44px hit areas; 28px remains for non-interactive state chips only.
2. Drag-handle hit region ≥44px tall; Escape/scrim as guaranteed alternatives.
3. `scroll-padding-bottom: calc(64px + safe-area)` on the scroll owner (WCAG 2.2 §2.4.11).
4. Retry in the thumb zone: bottom-pinned inside the failed row's detail sheet.
5. Dialog entry unified (opacity + 0.97→1 scale, 160ms; reduced-motion = opacity only).
6. Destructive-dialog Escape exemption kept, with `إلغاء` tabbable, destructive action not initially focused, decision logged.
7. Dirty-guard routing for scrim, drag, Escape, and back; focus-return chain sheet→guard→sheet specified.
8. Interactive (not exhibit-only) proofs for: 20/5/3 list batching, single-failure retry stop, press 80ms, loading footprint, completion dwell, and reduced-motion state preservation.
