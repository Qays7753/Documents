# Motion Storyboard & Interactive Prototype — Micro Bold Modular V1

## 1. Motion principles (file 05 §8)

Motion in Micro communicates **causality and state change** — nothing else. Energy model (locked UI-D02): bold at decision/action points, quiet during analysis. Prohibited everywhere: confetti, count-up delays on financial answers, repeating pulses, bounce, parallax, and any motion that survives `prefers-reduced-motion: reduce`.

## 2. The Success Impact sequence (candidate signature — `USER_TEST_REQUIRED`)

Storyboard frames for the sale flow (fixtures F → G):

| Frame | State | What the user sees | Timing |
|---|---|---|---|
| 1 | **Press** | Button responds instantly (settles 1px / warm press state) | ≤100ms |
| 2 | **Saving** | Button becomes «جارٍ التسجيل…», disabled, blocks double-submit | ~600ms (≈50ms reduced-motion) |
| 3 | **Confirmation** | «تم تسجيل البيع» + amount 25.00 د.أ + «أُضيف المبلغ إلى درج المحل» | persists |
| 4 | **Return to context** | «عرض العملية» returns to the home context | user-paced |
| 5 | **Impact highlight** | The affected value «الكاش المسجل الآن 161.00» pulses **once** (hale/ring, no movement of the number itself), delta badge +25.00 beside it | ≤1.1s, disabled under reduced-motion (static border remains) |

Per-direction treatments (all honor the same anatomy):
- **C1:** soft warm halo pulse around the impact card.
- **C2 / C2R:** single trust-blue ring expansion + return to white.
- **C3:** offset-shadow contract pulse (one beat).

## 3. Micro Signal behavior (concept)

The signal is a static, scannable structure (حالة ← سبب ← فعل) — it does **not** animate to attract attention; a repeating pulse is prohibited. Its "motion" is the state change it enables: acting on it resolves the signal (it leaves the screen on next visit).

## 4. Interaction states covered

- Press feedback on all buttons/QAB items (per-direction press language: C1 scale-down, C2 settle, C3 shadow-contract).
- Focus ring on keyboard focus (visible in `exports/focus-proof/`).
- Saving/busy state on the primary form action.
- Choice chips toggle with `aria-pressed` + container change (never color alone).
- Sheets: backdrop + handle; dialogs: alertdialog semantics.

## 5. Interactive prototype

- **Location:** `prototype/` (self-contained; no build step, no network needed).
- **Run:** open `prototype/index.html` in any browser (or serve the folder: `python3 -m http.server`). The hub links every screen of C1, C2, C3 and the refined C2R candidate.
- **Interactive path:** home → Quick Action «بيع» → sale form (amount pre-filled 25.00) → «سجّل البيع» → saving state → success screen with impact → «عرض العملية» returns home.
- **Proof controls (query params, no visible chrome):**
  - `?scale=text200` — 200% text stress.
  - `?static=1` — neutralizes the sticky nav for clean full-page screenshots.
- **Reduced motion:** honor `prefers-reduced-motion` automatically (OS setting or `agent-browser set media reduced-motion`).
- **Fonts:** IBM Plex Sans Arabic + IBM Plex Mono bundled under `prototype/assets/fonts/` (OFL) — renders offline.
- Boundaries: static prototype inside the handoff repository only; the Micro production repository is untouched.

## 6. What remains a hypothesis

- Whether the single-pulse impact highlight actually increases the owner's understanding that "the value changed" (user test: "وين راح المبلغ بعد التسجيل؟").
- Whether the saving-state duration (600ms) feels trustworthy vs. sluggish for recording operations.
- Whether the QAB press language reads as responsive on low-end Android hardware (performance handoff).
