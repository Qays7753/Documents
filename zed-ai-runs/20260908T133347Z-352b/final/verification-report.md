# Micro — Verification Report

Run `20260908T133347Z-352b` · built and verified 2026-09-08 · engine: headless
Chromium (agent-browser 0.35.0) + VLM visual passes + runtime audits built into the lab.

## 1 · Environment & method

- Served locally (`http://localhost:8321/`, no network dependencies); fonts loaded from
  the bundled woff2 files. Page errors: **0**. Console errors: **0** (checked after
  every phase).
- Interactions driven by real clicks where focus behavior mattered, programmatic clicks
  otherwise; measurements via in-page `getBoundingClientRect()` audits.
- Visual passes: phone-frame crops reviewed by VLM with defect-specific prompts;
  every VLM flag was re-checked programmatically (three were misreads, one was the
  scroll-under-nav standard pattern — see §5).

## 2 · Viewports, direction, scale, motion

| Configuration | Result |
|---|---|
| 320 / 360 / 390 / 430 @ 100% text, RTL | no horizontal overflow; 0 clipped elements (all 4 frames) |
| 320 / 360 / 390 / 430 @ **200%** text, RTL | no overflow; 0 clipped elements |
| 130% text | exercised via control; spot-checked |
| LTR geometry check | layout mirrors cleanly (screenshot 13); rail fade + logical properties correct |
| RTL default | default state of the document (`dir="rtl"`, `lang="ar"`) |
| Reduced motion (manual toggle) | transitions collapse; sheets/dialogs fade only |
| System `prefers-reduced-motion` | auto-applies at load (matchMedia hook) |

## 3 · Runtime audits (Verification view, re-runnable)

| Audit | Result |
|---|---|
| QuickActionRail next-tile peek | 16 / 56 / 86 / 30 px device-true (14 / 54 / 84 / 28 measured inside the 2px-bordered lab frames). 320 is the documented exception; 360/390/430 ≥ 28 px — measured, not overclaimed |
| Horizontal overflow (all widths, 100% & 200%) | none, 0 clipped elements |
| Touch targets | 56 interactive elements across the four frames; 0 below 44 px |
| "JOD" string | absent (grep of shipped files + runtime scan of product surfaces) |
| Arabic-Indic digits in values | 0 (English digits bidi-isolated everywhere) |
| Dark mode (`.dark` / `prefers-color-scheme`) | absent (the only `.dark` string in the code is the audit's detector) |
| Paper-plane / send icon | absent from the sprite |
| `#B4613F` | absent |
| HTML balance | div/section/button counts balanced; no `{{ }}` placeholders |

## 4 · Interaction tests (all passed)

1. View switching (4 tabs) — foundation/components/composition/verification.
2. Sheet open from rail tile: scrim + sheet 240ms; **focus lands on the amount input**;
   drag-grabber present.
3. Sheet close: Escape (hidden after 180ms), scrim tap, ✕ — focus returns to trigger
   (verified with real focus).
4. Save demo (expense, amount 12.500): button loading 1.1s → quiet completion
   «تم الحفظ» → live region announces «تم حفظ المصروف · 12.500 د.أ» → sheet auto-closes
   → **expenses −182.500 → −195.000, cash 431.100 → 418.600, new row «مصروف نقدي −12.500 · الآن» — all instantly, no count-up**.
5. Collect sheet opens; Escape dismisses; focus return verified.
6. Dialog «إلغاء فاتورة الشراء؟»: opens 160ms, confirm flips the row to cancelled
   («معلَّمة: ملغاة — يمكن عكسها لاحقًا») + live announcement.
7. Error state demo: «إعادة المحاولة» hides the error, shows 3 skeletons, loads 3 rows.
8. Segmented/tabs/checkbox/switch/nav switching all respond.
9. Full-page screenshots captured at every stage (see §6).

## 5 · Bugs found & fixed during verification (honest log)

| Bug | Impact | Fix |
|---|---|---|
| Overlay anchoring to scrolled content (architectural) | sheet/scrim floated mid-content once the phone scrolled | introduced non-scrolling `.phone-screen` + `.phone-scroll` owner + overlay layer; re-verified anchored at scrollTop 400 |
| Selector-building SyntaxError in `findOverlay`/scrim lookup (`[data-sheet]="x"`) | silently killed every sheet/dialog open | correct attribute-selector construction; re-tested all overlays |
| Chrome proximity snap scrolled the rail past its 16px start padding | peek geometry broke (4px @390) | `scroll-padding-inline-start: 16px`; measured peeks restored |
| Focus went to sheet close button instead of first field | keyboard UX | openOverlay prefers the first INPUT/SELECT/TEXTAREA |
| Retry demo self-reference (`querySelector` for the panel inside itself) | error card never stepped aside | hide the panel itself |
| Duplicate CSS rule + inverted rail fade directions + sub-44px clear button | polish/geometry | fixed in CSS |

## 6 · Visual review (VLM) summary

- Test composition (phone-crop): **8.5/10** — "clean design, good RTL support";
  hierarchy, tiles, nav all confirmed. Flagged items re-checked programmatically:
  nav icons/labels pixel-centered (756/756…); tiles uniform 88×92; row "clipping" =
  standard content scrolling under the sticky nav.
- Expense sheet: **8/10** — anchored, rounded, handle, fields, CTAs confirmed;
  "misaligned unit" is the designed RTL position (unit at inline-end);
  "red border" is the brand-ink focus color (perceptual note, recorded, not changed).
- Full-lab screenshot (with review chrome) initially judged "documentation-like" —
  expected: the lab is a review apparatus; the phone surface itself is the product
  deliverable and passes the native-feel review when isolated.

## 7 · Screenshots (evidence)

All under `04-user-and-accessibility-review/screenshots/`:
`01-foundation-390-rtl` · `02-composition-390-rtl` (+ `-crop`) · `03..06-components-*`
· `06b-components-charts-nav` · `07-sheet-crop` (+ full `07-sheet-expense-open`) ·
`08-sheet-completion` · `09-dialog-cancel-open` · `10-verification-frames` ·
`11-verification-audit` · `12-verification-200-scale` · `13-composition-ltr-geometry`
· `14-composition-320-rtl`.

## 8 · Not verified / out of scope (honest)

- Single engine (Chromium); on-device Safari/Android, real Arabic keyboards, and
  VoiceOver/TalkBack remain future work.
- 130% spot-check (not a full matrix run like 100/200%).
- The repo upload is verified by `git ls-remote` + tree diff (§ in run-report).
