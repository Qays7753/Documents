# Micro — Accessibility & RTL Report

Build-time verification of the delivered lab. Arithmetic and full pair tables were
computed by Agent 04 (`04-user-and-accessibility-review/accessibility-rtl-report.md`);
this file records what the final artifact actually passed.

## 1 · Contrast (verified)

See `color-role-map.md` §2 — the two forbidden pairs (positive-on-tint 4.27:1,
white-on-atmosphere 3.28:1) never appear as text in the build; the used pairs all
pass AA (4.5:1) or large-text (3:1) as appropriate. Disabled ink is sub-AA by intent
and non-interactive.

## 2 · Touch targets (measured)

Runtime audit across the four verification frames: **56 interactive elements, zero
below 44px** (buttons 48, icon buttons 44×44, tiles 88×92, rows ≥56, nav items ≥44,
segmented options 44, clear button 44). Gaps ≥8px everywhere.

## 3 · Text scaling (measured)

`--text-scale` (1 / 1.3 / 2) multiplies every font-size token via `calc()`.
At 200% on all four widths: **no horizontal overflow, zero clipped elements**
(runtime scan of rows, figures, buttons, inputs, sheets, nav, charts). Numbers never
wrap (`white-space: nowrap` on value runs); Arabic labels wrap instead.

## 4 · Bidi & digits (verified)

- All money: English digits inside `<bdi dir="ltr">`, U+2212 minus, 3-decimal fils,
  thousands comma, «د.أ» outside the isolated run. Runtime scan: **zero Arabic-Indic
  digits** in value runs; grep: the string "JOD" appears nowhere in the product files.
- Dates: `DD/MM/YYYY` isolated LTR («08/09/2026»).
- Signed renderings verified visually: «−182.500 د.أ» (RTL: sign+digits right-run,
  unit to its left), «+150.000», mixed «دفعة جزئية من 450.000».

## 5 · Icon mirroring registry (as built)

- **Mirror (directional, flipped only in RTL):** back arrow, chevrons (start/end),
  cash-out arrow-up-right, cash-in arrow-down-left. Implemented in CSS by symbol id
  (`:has(use[href="#i-arrow-start"])` etc. under `[dir="rtl"]`) — a single registry,
  not per-instance classes.
- **Never mirror:** home, users, wallet, package, truck, building, receipt, banknote,
  layers, clock, calendar, search, filter, bell, alert, info, check/x circles, refresh,
  wifi-off, cloud-check, trend icons (chart semantics), target, undo, pencil, trash.
- **Charts never mirror** — time axis stays LTR inside the chart in RTL.
- **No paper-plane/send icon exists anywhere in the sprite.**

## 6 · Keyboard & screen reader

- Every interactive element is a real control (button/input/select/label) — Tab order
  follows DOM order; focus-visible ring on all of them.
- Sheets/dialogs: `role="dialog"/"alertdialog"`, `aria-modal`, labelled titles; Tab is
  trapped inside the open overlay; Escape closes; focus returns to the trigger
  (verified with real focus moves).
- Completion announcements through a polite `aria-live` region («تم حفظ المصروف ·
  12.500 د.أ»).
- Charts: `role="img"` + sentence `aria-label` + a **visible** text alternative line.
- Status never depends on color alone: sign + icon + label accompany every semantic.
- Unknown is never rendered as 0 («غير متوفّر»), and the negative sign is the primary
  direction signal.

## 7 · One-hand ergonomics

Primary capture actions (rail) sit in the upper-thumb arc under the first glance
block; sheet CTAs and the bottom nav live in the bottom thumb zone; destructive
actions require a centered dialog (no swipe-to-destroy).

## 8 · Residual limitations (honest)

- Verification ran in headless Chromium (one engine) with VLM visual passes; on-device
  iOS/Android Arabic keyboards and VoiceOver/TalkBack passes are future work.
- `dir="ltr"` text inputs rely on platform keyboard behavior (adapter concern).
- The lab's desktop chrome (tabs/controls) is deliberately outside the product
  surface and not part of the phone a11y contract.
