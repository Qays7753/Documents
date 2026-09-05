# 03 — Workflow and Arabic Content Verification

## 1. Twenty-one end-to-end workflows — final status

The workflow audit (five specialists, read-only, then fixes) mapped each journey from intent to closure: entry point, required inputs, progressive disclosure, preview, confirmation, success result, source link, correction, cancellation, reload, offline recovery, duplicate submit, error recovery.

| # | Workflow | Status | Notes |
| --- | --- | --- | --- |
| 1 | Quick expense → detailed expense | Complete | Sheet amount-only save; detailed editor adds context/knowledge; unsaved-input guard verified live in browser QA (closing with input raised the honest alertdialog) |
| 2 | Quick sale | Complete | Verified live end-to-end in browser QA: FAB → sheet → 12.50 JOD → receipt dialog → «افتح السجل» → detail with DD/MM/YYYY, unknown-cost preserved |
| 3 | Product/service creation | Complete | Catalog editor, suggestion defaults, deep-link degradation honest |
| 4 | Cost calculation | Complete | Zero financial effect; estimate separate from cash |
| 5 | Order creation → confirmation | Complete | Draft → cost → agreement; unsaved-changes guards on 30 editors |
| 6 | Deposit collection | **Complete (fixed this run)** | WF-01: the pre-delivery عربون had no UI path (collect sheet told the owner to go to Order Detail; Order Detail had no deposit action; FAB promised «عربون أو تحصيل»). Mid-journey panel now on OrderDetail with explicit wallet destination; initial deposit gained wallet choice (FC-04) |
| 7 | Delivery with consumption | Complete | Auto-consume for tracked+approved; untracked no movement; shortage preview + explicit confirm; reversal mirrors |
| 8 | Direct sale | Complete | Cancel mirrors wallet allocations exactly once (prior audit FT-02) |
| 9 | Credit sale → settlement | Complete | Revenue once; settlement revisions labeled (FC-09) |
| 10 | Loans | Complete | AV-02 race fixed; partial repayment/settlement/edit/reversal/history verified |
| 11 | Assets / depreciation views | Complete | Family-guarded corrections; disposal/write-off views |
| 12 | Waste entry | **Complete (fixed)** | FC-01 profit-impact ask; FC-07 shortage warning; AR-07 «هدر» terminology |
| 13 | Direct edit of an old event | Complete (atomic path) + **FC-03 added** | Reverse-and-replace with reason; cross-month period-impact warning (this run); the literal in-place variant is the open owner decision (report 05) |
| 14 | Corrective reversal | Complete | Linked, idempotent, double-reversal prevented; family events via owner surfaces (FT-03/AI-01) |
| 15 | Financial health check | Complete | Tools integrity card, MIC-14..16 |
| 16 | Activity/source navigation | Complete | Activity row → source; receipt → record; statement line → source; deposits → order |
| 17 | Period statement / sharing | Complete | Statement with period picker, honest unknowns («—» not zero), manual share preview |
| 18 | Draft save / recovery / discard / final save | Complete | First-keystroke persistence; version-guarded restore; garbage coercion; cleared only after successful save |
| 19 | Backup validation / restore / post-restore check | **Complete (hardened this run)** | Envelope v27 with digest + embedded counts; DP-01 counts comparison; AI-01 orphan rejection; **AV-04**: stripped-envelope rejection for current versions; PIN-gated import; post-restore integrity check |
| 20 | Local lock / inactivity / PWA update / offline reload | Complete | PIN lock with backoff (prior audit), PWA dirty-safe updates; **offline reload verified live in browser QA** (service worker active, precache served the finance page offline) |
| 21 | Cross-surface money truth | Complete | Single financial truth engine; no duplicate computation surfaces introduced |

**Navigation contract**: exactly 4 nav seats + central FAB «سجّل» — verified live in the browser (`document.querySelectorAll('nav').length === 1`, one `.micro-fab`, labels مشروعي الآن / العمل / سجّل / مالي / أدواتي) and pinned by `navigation.test.ts`. No sixth tab, no duplicate bar, no second FAB anywhere in the diff.

## 2. Arabic financial content — closure status

The stopped run's `c29ad39` committed the AR-01..AR-17 closure; this continuation verified it and finished the two items left uncommitted:

| ID | Item | Status |
| --- | --- | --- |
| AR-01 | Six domain validation messages carried Arabic-Indic digits (٢٠٠/٨٠/١-٦٠٠/٥٠٠) — bypassed the enforced English-digit policy | **Fixed & verified** (English digits; formatters policy test still pins the central policy) |
| AR-02 | Dialect/MSA register split across ~20 status/empty/effect/error texts (incl. collection-reversal refusals, statement trust lines) | **Fixed & verified** — professional MSA sweep, no brand copying |
| AR-03 | ActualTimePanel bare «—» explanations | **Fixed** — real per-status explanations |
| AR-04 | «نقض موثق» vs «تراجع موثق» terminology split | **Fixed** — unified on «تراجع موثق» |
| AR-05/AR-11 | Plural grammar bypasses («N يوم») | **Fixed** — routed through `formatArabicPlural` |
| AR-06/AR-14 | Loans/Orders error states without reassurance/next action | **Fixed** |
| AR-07 | Waste terminology fragmentation (هدر/هالك/الفاقد/تلف) | **Fixed** — unified on «هدر» |
| AR-08 | «بالوحدات الصغرى» engineering jargon | **Fixed** — dinar phrasing |
| AR-09/FC-08 | Unknown-cost movement rows showing confident 0.00 | **Fixed** — «قيمة غير محددة بعد» |
| AR-10/AR-12/AR-13/AR-16/AR-17 | Register/label cleanups (غير معروفة→غير محدد بعد؛ disposal label; price-error wording; % vs bps) | **Fixed** |
| AR-15 | Save-failure messages without data-safety/retry | **Fixed** (10 sites) |
| — | Every warning explains consequence + next action; every error has a recovery action; all states distinct | Verified across surfaces; the new AV-06 warning and FC-03 warning follow the same pattern (consequence + action) |

**Digits and dates**: English digits everywhere (enforced by `formatters.ts` + tests); numeric RTL dates `DD/MM/YYYY` — verified live in browser QA (sale detail showed 05/09/2026 with `lang="en"` input walls and `bdi` isolation).

## 3. Mobile RTL & discoverability — closure status

| ID | Severity | Item | Disposition |
| --- | --- | --- | --- |
| MR-01/WF-01 | P1 | Pre-delivery deposit unreachable | **Fixed** (stopped run, verified: mid-journey panel + tests) |
| MR-02 | P2 | Back-arrow direction split (12 surfaces used ArrowLeft = forward in RTL for back) | **Fixed this run** — all surface back buttons now ArrowRight; forward affordances (open/enter/chevrons) keep ArrowLeft; missed Collect.tsx fixed; imports cleaned |
| MR-03 | P2 | `.micro-button-quiet` at 32px min-height on 31 sites incl. financial correction/reversal | **Fixed this run** — 44px minimum; U09 guard extended |
| MR-04 | P2 | Header context duplicated brand («مايكرو مايكرو») on /collect, /direct-sales/*, /share/preview, /foundation, /catalog | **Fixed this run** — contextual labels (ورقة التحصيل، بيع مباشر، الكتالوج، معاينة المشاركة، صفحة الأساس); verified live: /direct-sales/:id header shows «بيع مباشر» |
| MR-05/WF-03 | P3 | العمل lacks products/materials links per the stated tab contract | **Fixed this run** — two quiet links with the app's canonical labels (منتجاتي وخدماتي / المواد والمخزون) |
| MR-06 | P3 | Backup not under أدواتي | **Fixed this run** — Tools links to النسخ الاحتياطي والبيانات (Settings cards) |

**Layout verification (live)**: 360×800 and 390×844 — zero horizontal overflow at both widths, safe-area insets present, single nav + FAB, vaul/Radix sheets with focus handling, amount inputs use English-number input components (`inputMode=decimal`, `dir=ltr`). No swipe-to-delete anywhere; financial destructive actions remain reason-required, previewed corrections.

## 4. Emotional quality spot-checks (guilt-free, no shaming)

- Draft loss warning: «في رقم مكتوب — تسجّله أو تتجاهله؟» with explicit options — verified live.
- Unknown states: «غير محدد بعد» phrasing, «—» instead of zero on honest rows.
- Correction copy: documents what stays true, offers undo paths, never blames.
- AV-06 warning follows the pattern: state the effect, offer the next action, keep the choice legitimate.
