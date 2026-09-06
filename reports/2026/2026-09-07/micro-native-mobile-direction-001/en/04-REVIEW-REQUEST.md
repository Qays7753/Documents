# 04 — REVIEW REQUEST (Stage 3 Approval Gate)

**Delivery:** `micro-native-mobile-direction-001`
**To:** the owner
**From:** central orchestrator
**Date:** 2026-09-07
**Status:** ⏸ **Waiting for the owner's decision. Nothing below has started and nothing will start until an explicit approval arrives.**

---

## 1. What is ready to inspect

Three complete, independently reviewable native mobile product concepts for Micro, each opening as a real application screen (no phone bezel, no review console in the viewport), each in Arabic RTL first, each carrying the fixed Terracotta palette, the same money discipline, and the same honest state system:

| Direction | Path | Essence |
|---|---|---|
| **B — «الدفتر» The Register** *(recommended)* | `prototype/direction-b/` | The register itself is the home; a pinned live truth bar filters it; FAB capture; long-press and swipe grammar |
| **A — «الخلاصة اليومية» The Daily Brief** | `prototype/direction-a/` | The day is the app: a collapsing large title that absorbs the numbers, a timeline of the day, attention rows |
| **C — «الصندوق» The Counter Hub** | `prototype/direction-c/` | Position-first: deep cash hero, لك/عليك counter split on one hairline, day strip with paging agenda, sheet-first work |

Open `prototype/review-index.html` first; it links everything with the review states. Full guidance: `en/03-native-prototype-review-guide.md` (~15–20 minutes).

## 2. Why B is recommended (decide freely — this is a recommendation, not a verdict)

B's anatomy is the hardest to mistake for a web page: a working list as the home surface, a truth bar that visibly re-filters the register, FAB capture, long-press context menus, swipe actions on operational rows, and push/pop with reliable back. Its risks are quality risks (a gray, boring table — mitigated with warm ink hierarchy, Almarai + mono money voice, and demonstrated gestures), not category risks. A leans toward the editorial/web-article error (bounded here: every row actionable, digest capped); C leans toward the wallet/dashboard silhouette (mitigated: labeled truth hero, no spend affordances, single-hairline split). The adversarial critic's scores are risk assessments, not approvals: B 80.5 · A 64.9 · C 63.0.

## 3. The decision you are asked to make

Compare the three directions and answer:

1. **Does it feel like a real mobile app** — not a web page inside a phone frame?
2. **Does it feel like a major company's product** — mature, calm, trustworthy?
3. **Is the composition distinctive** — an identity you would recognize, not a generic template?
4. **Is it comfortable and clear in Arabic RTL** — written for the owner's speech, not translated?
5. **Does finance stay central** without becoming a POS, a banking wallet, or an ERP?
6. **Do navigation, back, sheets, and motion feel native** — predictable, quiet, honest?
7. **Are the screens coherent beyond the home** — الدفتر/الناس/العمل/الأدوات, details, closing, states?

This is a **visual and experiential decision**. Please do not decide on colors (fixed by identity), internal scores, or code quality — the previous cycle's concepts scored well and were still rightly rejected for the category error.

**Choose one:**
- **Approve one direction** (e.g., "B approved as the native visual direction") → Stage 4 begins: the approved direction is refined and the final handoff package (`en/05`–`en/16` + `prototype/approved-native-concept/`) is produced. Production integration remains a separate later step.
- **Reject with focus** (e.g., "all three still read web-like in X" / "B is right but the register is too plain") → a focused revision cycle runs before any finalization.
- **Request a hybrid** (e.g., "B's structure with A's briefing tone") → the orchestrator will rule on feasibility against the one-signature-per-direction constraint and document the trade-offs.

## 4. What has explicitly NOT started

- No Stage 4 files exist (`05`–`16`), and no `prototype/approved-native-concept/` exists.
- No production Micro code was touched, read for write, or integrated with in any way.
- No final token sheets, no implementation handoff, no production typeface decisions.

## 5. Known limitations carried into this review

HTML is the review medium, not the product: platform behaviors (predictive back, haptics, OS keyboard, real detents) are approximated and labeled; data is a static arithmetically-consistent corpus; sync is choreography; the fixed logo asset is absent from the repository and a reserved placeholder slot stands in its single sanctioned place; B carries full English LTR verification while A and C carry layout-level mirroring only. Full list in `en/03` §6.

---

**This delivery stops here, at the gate.** The success condition is yours to judge: open a screen and check whether it finally feels like a serious native mobile product — a phone application first — rather than a web page assembled by code. Your approval of one direction (or focused rejection) is the only trigger for what comes next.
