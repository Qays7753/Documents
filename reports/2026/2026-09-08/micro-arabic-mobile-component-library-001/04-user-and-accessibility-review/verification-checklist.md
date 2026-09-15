# Verification Checklist — Binding QA Bar for the Final Lab

Agent 04 · Task 3 · Run `20260908T133450Z-16d11`
This is the **binding checklist** the final lab (`05-synthesis-and-redesign/` → `final/`) must pass before upload. Dimension key: **VP** viewport · **DI** direction · **TS** text scale · **MO** motion · **BU/IN/SA/SD/CH/QA** family coverage (button/input/state/sheet-dialog/chart/rail) · **CU** currency & digits · **AX** accessibility · **LB** lab constraints. Verify methods: **M** = manual (human eye in browser) · **H** = headless-browser (agent-browser screenshot) · **J** = JS-measured (scripted assertion in the Verification view; numbers recorded, not eyeballed).

Contrast reference: `04-user-and-accessibility-review/accessibility-rtl-report.md` §1 (recomputed table) and `contrast_check.py`. Geometry reference: `03-design-system-engineering/variant-state-matrix.md` peek table (recomputed: 320→16px, 360→56, 390→86, 430→30).

---

## 1. Viewport & direction (RTL primary)

| ID | Dimension | Concrete check | Pass condition | Verify |
|---|---|---|---|---|
| VP-01 | viewport 320 | Full test composition at 320px RTL | No horizontal page scroll; no clipped text; order unchanged (top zone → primary value → rail → metrics → follow-ups → pair) | H + M |
| VP-02 | viewport 360 | Same at 360px RTL | Same as VP-01 | H + M |
| VP-03 | viewport 390 | Same at 390px RTL | Same as VP-01 | H + M |
| VP-04 | viewport 430 | Same at 430px RTL | Same as VP-01 | H + M |
| VP-05 | viewport 320 fold | First warning row (`شركة التوصيل السريع — بانتظار التحويل`) visible before the fold at 320px | Row's top edge < viewport height − bottom nav; if not, the 320px-only spacing compression (40→32 / 32→24) is applied and re-measured | J (getBoundingClientRect) |
| VP-06 | viewport all | Screen edge is 16px at all four widths | Content inset = 16±0 | J |
| DI-01 | direction LTR | Geometry-only LTR check: same composition with `dir="ltr"` | Layout mirrors via logical properties; no hand-flipped CSS; nav order flips (`اليوم` leftmost); numbers stay LTR isolates; chart time axis stays LTR | H + M |
| DI-02 | direction | Sheet/dialog titles start-aligned in both directions; value column stays at inline-end | No orphaned physical left/right declarations in component CSS | J (grep CSS for `left:`/`right:` outside `.lab-*`) |
| DI-03 | direction | Icon mirror registry: only chevrons/arrows carry `.icon-mirror` | No semantic icon (check/clock/plus/receipt/package/banknote/trash/calendar) has `.icon-mirror`; no paper-plane/send glyph anywhere | J (DOM scan) |

## 2. Text scaling & motion

| ID | Dimension | Concrete check | Pass condition | Verify |
|---|---|---|---|---|
| TS-01 | scale 100% | Root 16px: all type roles render at spec sizes (32/15/13; 14 floor for Arabic words) | Computed styles match tokens; no Arabic reading text below 14px (exception: rail labels at 13px per §6.8) | J |
| TS-02 | scale 130% | Root 20.8px | Text grows; no clipping; rail tile may grow in height only; nav labels fit | H + J |
| TS-03 | scale 200% | Root 32px | No clipped/overlapping text anywhere; rail tile = min-height (grows, width 88/gap 8/padding 16 unchanged); chips and CTAs grow; value column alignment preserved; page scrolls vertically only | H + J |
| TS-04 | scale 200% labels | Long-label spot checks: `تحصيل دين من مطعم النخيل`، `تسجيل دفعة لمؤسسة الشرق للتجهيزات`، `طحين فاخر 10كغ — تحت الحد` | Wrap, never truncate or overlap | H |
| TS-05 | scale 320 nav | Nav labels at 320px do not clip | `المبيعات` fits 64px seat, else fallback `مبيعات`; all seats ≥44px | J (scrollWidth ≤ clientWidth) |
| MO-01 | motion durations | Press 80ms, fast 120ms, normal 200ms, sheet 240/180, dialog 160/120, scrim 200ms | All transitions consume `--mc-motion-*` tokens; no other durations in component CSS | J (computed transition-duration) |
| MO-02 | motion reduced | `html[data-motion="reduced"]` + `prefers-reduced-motion` | Sheets/dialogs appear in place; scrim instant; skeletons static; switch snaps; state meaning (loading/error/completed) still visible | H + M (toggle in Verification view) |
| MO-03 | motion values | Financial values never animate | `textContent` of the value node is final within one frame after completion (no count-up) | J |
| MO-04 | motion easing | No bounce/spring/overshoot | All easings from `--mc-ease-*` (control points within [0,1]); no `animation` with bounce keyframes | J |
| MO-05 | motion press | Press overlay 8% ink alpha at 80ms on every pressable family | Demonstrated interactively (rail tile, buttons, rows, nav seats) | M + J |

## 3. Family & state coverage vs SPEC §6.9

| ID | Dimension | Concrete check | Pass condition | Verify |
|---|---|---|---|---|
| BU-01 | buttons | Variants visible in matrix: primary, secondary, quiet, destructive, icon-only | Each rendered with correct fills (primary = brand-ink + white 6.11:1) | M |
| BU-02 | buttons | States: loading (label + spinner, footprint stable, `aria-busy`), disabled, focused (2px ring), pressed, quiet completion (check + `تم` ≥1.5s dwell) | All six demonstrated; completion also interactive | M + J |
| IN-01 | inputs | Variants: text, amount (`inputmode="decimal"`, `dir="ltr"`, `د.أ` affix, tabular digits, grouping on blur), search (clear ≥44px), date (DD/MM/YYYY, `اليوم` quick chip ≥44px hit), selection, segmented, tab, checkbox, switch | All nine in the matrix | M |
| IN-02 | inputs | States: focus (ring), error (`أدخل مبلغًا أكبر من صفر`, danger border + `aria-describedby`, 14px), filled, disabled | Error demo is triggerable, not frozen only | M + J |
| SA-01 | states | All ten: empty, loading, error, offline/local-save, decision-critical pending, conflict, failed, completed, cancelled, reversed | Line-based, icon + word + tint; wording from the locked copy bank; no auto-retry after first failure | M |
| SA-02 | states | Empty states carry exactly one useful action (`سجّل بيعًا` / `مسح البحث`) ≥44px | No illustration theatre | M |
| SD-01 | sheets | Open 240ms / close 180ms; scrim 200ms; drag handle hit area ≥44px; focus trap; focus returns to invoker | Interactive demo in Verification view | M + J |
| SD-02 | sheets | Scrim tap, Escape, drag all dismiss clean sheets; all three route dirty sheets through `تجاهل التغييرات؟` | None silently discards entered data | M + J |
| SD-03 | dialogs | Alert/confirm/destructive: 160/120ms; destructive ignores Escape/scrim but `إلغاء` is tabbable; destructive action not initially focused | Keyboard-only walk succeeds (Tab to `إلغاء`, Enter) | M + J |
| SD-04 | sheets | Reduced-motion dismissal still available (tap threshold) and state meaning preserved | MO-02 cross-check | M |
| CH-01 | charts | Four primitives: sparkline, planned-vs-actual, target meter, trend marker | All rendered with direct labels, no legend | M |
| CH-02 | charts | Text alternative for every chart (`role="img"` + sentence + visible `.chart-alt`) | Present on all four | J (DOM scan) |
| CH-03 | charts | Time axis LTR inside RTL page (oldest left, newest right); Arabic labels RTL | Verified in both directions | H |
| CH-04 | charts | Planned vs actual distinguishable without color: dashed vs solid + direct labels `مخطط`/`فعلي` | Grayscale screenshot still distinguishes series | H (grayscale capture) |
| QA-01 | rail | Measured next-tile peek: 16px at 320 (documented exception); 56/86/30 at 360/390/430 (≥28 required) | JS-measured values recorded in Verification view; geometry 88×92/gap 8/padding 16 unchanged at all widths | J |
| QA-02 | rail | RTL horizontal scroll with proximity snap; edge fade at inline-end; exactly one brand-tint tile, first position | Manual swipe/snap check | M |
| QA-03 | rail | Five stable actions, `إضافة بيع` first | Matches locked order | M |

## 4. Currency, digits & financial truth

| ID | Dimension | Concrete check | Pass condition | Verify |
|---|---|---|---|---|
| CU-01 | currency | `د.أ` as separate Arabic node; never inside the LTR isolate; omitted only when unambiguous | DOM scan: no `<bdi dir="ltr">…د.أ…</bdi>` | J |
| CU-02 | currency | No `JOD`, no spelled-out currency in any user-facing surface | String scan of HTML (allowing the rule statement in docs only) | J |
| CU-03 | digits | English digits `0–9` in all values/dates; DD/MM/YYYY; tabular-nums lining-nums on numeric contexts | Visual + computed font-variant-numeric | H + J |
| CU-04 | bidi | Signs lead inside isolates (`-92.50`, `+210.00`); thousands separators correct; `(65%)` isolated with brackets or dropped; `—` in value position isolated | Rendered screenshots show `-92.50` not `92.50-`; meter label brackets not flipped | H + M |
| CU-05 | truth | Unknown ≠ 0: `—` + reason; true zero `0.00` full weight; stock values unsigned; flow values signed; offline pending excluded from cash | Composition + matrix examples show all three distinct | M |

## 5. Accessibility (WCAG 2.2 AA + Micro overrides)

| ID | Dimension | Concrete check | Pass condition | Verify |
|---|---|---|---|---|
| AX-01 | contrast | Every text pair used in the lab passes per the recomputed table (§1 of the a11y report) | ink-subtle never on sunken; positive-on-tint only 32px/icons; warning-on-tint ≥15px with icon+word; ink-disabled only on disabled controls with non-color cue | J (style audit) + reference |
| AX-02 | focus | 2px `ink-strong` ring, 2px offset, on every interactive family via `:focus-visible`; `:focus:not(:focus-visible)` suppresses for pointer | Tab walk shows ring on: buttons, inputs, segments, tabs, checkbox, switch, rows, tiles, nav seats, avatar | M + J |
| AX-03 | focus not obscured | `scroll-padding-bottom ≥ 64px + safe-area` on the scroll owner | Focused element near bottom is fully visible above nav (WCAG 2.2 §2.4.11) | J |
| AX-04 | targets | All interactive elements ≥44px hit area; primary 48px; tappable chips (quick-fill, `اليوم`) ≥44px hit; drag handle ≥44px hit | getBoundingClientRect on all `[data-interactive], button, input, .quick-tile, .nav-item` | J |
| AX-05 | semantics | Buttons are `<button>`; inputs have bound `<label>`; icon-only buttons carry `aria-label`; nav has `aria-current`; switch `aria-checked`; segmented `aria-pressed` | DOM/ARIA scan | J |
| AX-06 | live regions | `role="status"` announces completion (`تم تسجيل البيع`); `role="alert"` announces failure (`فشل الإرسال`); loading regions `aria-busy` announced once | Interactive demo with a screen-reader-ish listener or recorded DOM event | J |
| AX-07 | non-color status | Every semantic use pairs tint with sign/icon/word; the comparison pair has no silent warning dot | Visual grayscale pass over matrices | H (grayscale) |
| AX-08 | keyboard | Full keyboard walk of the lab: tab order = visual RTL order; sheets trap and return focus; no trap anywhere | Keyboard-only session completes a sale entry + a retry | M |
| AX-09 | mirror registry | DI-03 cross-check | No mirrored semantic icons | J |
| AX-10 | scaling | TS-01..05 cross-check | No loss of content or function at 200% | J |

## 6. Lab constraints (hard blockers)

| ID | Dimension | Concrete check | Pass condition | Verify |
|---|---|---|---|---|
| LB-01 | lab | Opens offline (no network) with file:// protocol | No console errors; fonts fall back gracefully; no remote runtime | H (offline load) |
| LB-02 | lab | No `{{...}}` placeholder tokens anywhere in HTML/JS | String scan clean | J |
| LB-03 | lab | Light Mode only: no `.dark`, no `prefers-color-scheme` behavior, no dark tokens | CSS scan | J |
| LB-04 | lab | No fake system UI (status bar, home indicator drawn in HTML) | Visual + DOM scan | M |
| LB-05 | lab | Views: Foundation / Component Library / Test Composition / Verification switchable; matrices visible, not prose-only; audit evidence separated from the showcase | Manual walk | M |
| LB-06 | lab | No raw hex, rejected colors, or implementation notes inside phone compositions; no `#B4613F` anywhere | String scan | J |
| LB-07 | lab | Composition budget holds in the Test Composition (1 PrimaryValueBlock, 1 rail, 1 MetricGroup, ≤3 surfaces, ≤2 semantic families, ≤2 colored numbers, 1 vertical scroll owner) | Manual + J count | M + J |

**Sign-off rule:** every row must be **pass** or carry a documented, spec-justified exception (e.g., VP-05 conditional compression; QA-01 320px peek). Any hard-fail in CU, AX-01..06, or LB blocks upload per SPEC §9.
