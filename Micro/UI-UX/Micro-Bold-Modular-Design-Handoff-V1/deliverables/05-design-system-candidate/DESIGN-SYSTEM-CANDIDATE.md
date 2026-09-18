# C2R — Candidate Visual System (Refined Selected Direction)

> **Status:** expert recommendation pending owner approval and real-user validation.
> **Base:** C2 — Confident Bold (provisional rubric winner, `reports/comparison-and-recommendation.md`).
> **Refinement borrowings:** warmth moments from C1; progress/status language from C3. The three original directions remain fully preserved and unmerged in their own folders.

## 1. Identity concept

**C2R — نظام تشغيل مالي واثق وحيّ:** شريط معماري أزرق عميق يحمل الثقة والسياق، فعل طيني دافئ يحمل البدء والإنشاء، أرقام بصرامة التقارير، ودفء إنساني في لحظات الإشارة والنجاح.

Five adjectives: واثق · منضبط · حديث · دافئ (مقترض من C1) · واضح.

## 2. Token source of truth

- Machine-readable: `prototype/c2r-selected-candidate/tokens.json` (light + dark + type scale + measured contrast).
- CSS custom properties: `prototype/c2r-selected-candidate/tokens.css` (generated; do not hand-edit).
- Stylesheet: `prototype/c2r-selected-candidate/c2r.css` = C2 base + refinement layer (each rule annotated with its borrowing rationale).

All 213 measured WCAG 2.2 pairs (light + dark) pass — see `reports/contrast-evidence.md`. Proposed hex values remain proposals pending owner approval (brand color, base background, trust color are `OWNER_APPROVAL_REQUIRED`).

## 3. Component rules (concept level — not production components)

| Component | Rule |
|---|---|
| **Business Status Hero** | White surface, 5px state-color start-edge, squared 12px radius. State = chip (icon+text) + result value in mono; never color-only. Four states: positive (green), incomplete (amber + progress + action), negative (red + reason + action), empty (neutral). |
| **Micro Signal** | Warm brand-softer ground + brand start-edge (C1 borrow): the action hub is the warmest element on home. Anatomy fixed: حالة ← سبب ← فعل (labeled button, never icon-only). |
| **Quick Action Bar** | White bar, five labeled actions (بيع، مصروف، طلب، تحصيل، المزيد), 48px icon tiles, always visible above nav; "المزيد" opens a bottom sheet; no duplicate FAB. |
| **Completion progress** | 12px attention-bordered rail + bold textual note (C3 borrow): incompleteness must visually compete with complete results. |
| **Step rail** | Four labeled stages (اتفاق → تنفيذ → جاهز → تم التسليم) + متأخر exception flag; current node enlarged with soft ring (C3 borrow). |
| **Impact preview / Success impact** | Impact preview on trust-soft ground before commit; success shows amount → destination → updated value with single highlight + delta; flash disabled under reduced motion. |
| **Bottom navigation** | Five locked tabs; active = ink-filled tile + bold label; inactive tertiary. |
| **Chips** | Tinted ground + deep text + icon; filled chips only for status language; never color-only. |
| **Buttons** | Primary: terracotta fill (48px, 9px radius). Secondary: outlined surface. Quiet: trust-blue text. |
| **Focus** | 3px brand outline, offset 3px, on every interactive element (`:focus-visible`). |

## 4. Dark mode

Not a literal inversion: band becomes deep navy `#10293B`; surfaces cool-dark; semantic colors lightened for glare; active nav becomes ink-tile inverted; every corrected pair measured (see contrast evidence, dark tables).

## 5. Motion signature — "Success Impact" (USER_TEST_REQUIRED)

1. Immediate press feedback (button settles 1px).
2. Saving state «جارٍ التسجيل…» blocks double-submit.
3. Success confirmation: amount + destination.
4. Return to context (عرض العملية).
5. Single highlight pulse on the affected value (161.00) — **one** pulse, ≤1.1s, disabled under `prefers-reduced-motion` (static border remains).

Prohibited (unchanged): confetti, count-up delays, repeating pulses, bounce, parallax.

## 6. Implementation-transfer notes (for the future code track)

- Tokens map 1:1 to CSS custom properties already (`tokens.css`); keep the light/dark pair structure.
- Keep `on_brand`/`on_fill`/`band` as **distinct** text tokens — never compute text color on the fly.
- The 44–48px target contract and QAB-above-nav geometry are layout invariants; the sticky nav must reserve ≥76px + safe area.
- Numerals: IBM Plex Mono with `font-variant-numeric: tabular-nums`, wrapped in isolated LTR spans (`unicode-bidi: isolate`).
- Arabic date convention: `DD/MM/YYYY` in isolated runs; one convention only.
- Mixed-direction text (names like أم محمد + amounts + #142) requires the same bidi-isolation pattern used in the prototype.
- Debt-figure source consistency and sheet stale-value behaviors remain open implementation handoffs (file 10) — design provides the states; logic is out of scope here.

## 7. What is explicitly NOT final

Logo adjustment, final hex canon, icon library migration (Lucide-foundation retained), animation curves beyond concept guidance, chart library, production component API, and the Market module identity (C3's zone grammar is the leading candidate there — a separate future decision).
