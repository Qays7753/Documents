# 04 — REVIEW REQUEST (Stage 3 — Approval Gate)

**To:** the Micro product owner
**From:** the central orchestrator, `micro-native-mobile-direction-002`
**Date:** 2026-09-07
**Status:** **Stage 2 complete, stopped at your gate. Nothing is finalized; Stage 4 has not started.**

---

## 1. What is ready to inspect

| Item | Path |
|---|---|
| **Interactive prototype — A «الطاولة» The Counter** | `prototype/direction-a/index.html` |
| **Interactive prototype — B «الأدراج» The Drawers** | `prototype/direction-b/index.html` |
| **Interactive prototype — C «الميزان» The Scale** | `prototype/direction-c/index.html` |
| Review index (links, state tour, experiments, questions) | `prototype/review-index.html` |
| How to review (20–30 min route) | `en/03-native-prototype-review-guide.md` |
| Previous-work lessons (Keep / Adapt / Reject / Verify) | `en/00-previous-work-lessons.md` |
| Intake & audit (why the previous two were rejected) | `en/01-intake-and-previous-work-audit.md` |
| Direction synthesis (full definitions + recommendation) | `en/02-native-direction-synthesis.md` |
| Five specialist reports | `subagents/01…05-*.md` |
| QA evidence (18 headless-browser captures) | `supporting/qa-screenshots/` |
| Delivery manifest | `metadata.yml` + folder `INDEX.md` |

**Source status (stated honestly, same as both previous deliveries):** `micro-agent-input.zip`, `micro-recovery-docs.zip`, and `MicroPrimitives-anti-reference.html` remain **absent** from the repository (repo-wide search, 2026-09-07). Documented, not invented; the fixed constraint block and the repository's own reports are the grounding.

## 2. What changed relative to the two rejected deliveries

The two previous concepts failed as **web compositions inside a phone frame** (001: bezel + stacked cards + desktop caption; 002: desktop review console + document-flow screen). This delivery changes the category, not the decoration:

- Each direction is a **working application route**: tab bars and seats, per-tab navigation stacks, RTL push/pop with parallax and dimming, interactive swipe-back from the right edge, bottom sheets with grabber drag-to-dismiss, dialogs only for consequential decisions, browser-back integration, keyboard-aware capture forms.
- The product surface contains **product UI only**. The review apparatus lives in `review-index.html` and a small out-of-frame pill.
- The rejected languages are hard-banned: no bezels, no fake status bars, no desktop console, no card walls, no document flow, no decorative terracotta washes, no scores posing as approval.
- The keepers survive intact: measured contrast doctrine (`#964e33`+white 6.11 resting; `#b4613f` press-only; never white on `#cc785c`), honest states (unknown never 0.00; تقديري/معلّق/تعارض/ملغي/تسوية as first-class glyph+label), the bidi contract (isolated digit runs, «د.أ» after the number), 3-decimal fils JOD, DD/MM/YYYY, ASCII digits, Arabic floors, quiet completion, and effect-preview before irreversible actions.
- One reconciled Arabic corpus (بقالة النور, 01–07/09/2026) drives all three: صندوق **431.100** مؤكد (+27.750 بانتظار المزامنة) · لي **664.250** · عليّ **348.500** — and every mutation (قبض، تسوية، حسم تعارض، إغلاق بفرق) updates the figures live and truthfully.

## 3. Recommendation (argued, not scored into authority)

**A — «الطاولة» The Counter** is recommended: it answers the owner's complaint most decisively (a card wall is structurally impossible; money truth is pinned chrome, not a floating hero card), carries the highest working density, and its tells — pinned band, frosted bar, swipe rows, interactive back — are unmistakably phone-native.
**B — «الأدراج»** is the safest build and the least distinctive. **C — «الميزان»** has the best capture ergonomics and the highest genericness risk.
The three prototypes exist precisely so your eye decides — not a rubric.

## 4. What you must judge (the primary decision is visual and experiential)

For **each** direction, on the phone-width window, in Arabic:

1. Does it feel like a **real mobile app** the moment it opens?
2. Does it feel like a **major-company product** — nothing you'd be embarrassed to hand a shop owner?
3. Is the composition **distinctive** rather than generic (not any-fintech, not Settings-in-terracotta)?
4. Is it **comfortable and clear in Arabic RTL** — names, numbers, chevrons, right-edge back, dense rows?
5. Does **finance stay central** without drifting into POS, banking, or ERP?
6. Do **navigation, sheets, back behavior, and motion** feel native — transitions connected to navigation events, not page fades?
7. Are the screens **coherent beyond home** — اليوم، المال، الناس/الزباين، الطلبيات، المشتريات، الإغلاق، الإعدادات، البحث؟

Do **not** judge colors in isolation, internal scores, or code quality. Those are not the decision.

## 5. Explicit questions

| # | Question | Notes |
|---|---|---|
| Q1 | **Which direction do you approve — A, B, or C?** (Or reject with focused feedback.) | This single decision gates Stage 4. "A + parts of B/C" is a composite instruction, not approval — if you want a merge, say so explicitly and it will be treated as a revision round. |
| Q2 | **JOD with 3 decimals everywhere** (fils-true, receipt=display=input) — confirm, or prefer 2? | One token change; defaults to 3. |
| Q3 | **Charts: earliest day on the right (RTL flow)** — accept as default pending a real-owner test, or prefer bank-statement left-to-right? | The alternative is pre-specified; labels carry the meaning either way. |
| Q4 | **Typography per direction** (A system · B Plex · C Readex) — confirm the winner's voice, or impose one face for all? | Production face decision remains a Stage-4 gate. |
| Q5 | **The missing source packages** — will you supply `micro-agent-input.zip` / `micro-recovery-docs.zip` / `MicroPrimitives-anti-reference.html` before Stage 4, or confirm the delivery proceeds on the documented constraints? | Affects Stage-4 grounding, not this review. |

## 6. Known limitations (do not read past these)

- HTML review medium: keyboard avoidance, safe areas, haptic moments, screen-reader behavior, and edge-swipe physics are **demonstrated, not device-proven** (V-02…V-04 open).
- In-memory demo data; reload resets state. Charts cover the 7 recorded days by design (the pre-01/09 gap is itself the honesty demo).
- Light English-LTR verification is a Stage-4 deliverable; these prototypes are Arabic-first.
- The specialist corpus table listed «ورشة أبو يوسف» as «حساب مسدّد» while its own reconciliation put the balance at 38.400 — the reconciliation wins in the prototypes (totals must sum), flagged here as a corpus erratum.
- Event 20 (بنزين) was adjusted 4.500 → **4.450** so the week reconciles exactly to the corpus's own 431.100 closing figure.

## 7. Waiting for approval — hard stop

Until you explicitly approve one direction (or return focused rejection feedback):

- Stage 4 (`en/05…en/16`, the approved-direction refinement and `prototype/approved-native-concept/`) **will not be produced**;
- the production Micro codebase **will not be touched**;
- nothing here is claimed to be approved or production-ready;
- on rejection, only the requested direction is revised and re-presented.

**How to respond** (a short message suffices): e.g., «أعتمد A؛ الفلوس 3 منازل؛ الاتجاه الزمني بالعربي يمين؛ صوت A؛ المصادر لاحقاً» — or «أرفض A لأن…، عدّل…».
