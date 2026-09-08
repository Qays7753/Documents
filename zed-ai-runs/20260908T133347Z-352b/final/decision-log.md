# Micro — Decision Log

Chosen decision · rejected alternatives · reason · evidence. Each recorded once.

| ID | Decision | Rejected alternatives | Reason | Evidence |
|---|---|---|---|---|
| D-01 | Direction: one selected direction «دفء الحانوت / The Warm Counter» | multiple competing concepts; prior prototype lineages (دفتر/طاولة/ميزان) | spec demands one synthesized direction, not a concept gallery | visual-direction.md; prior repo deliveries stayed at approval gates |
| D-02 | Corpus: بقالة النور, 3-decimal fils, English digits, د.أ | new business, JOD label, 2-decimal | continuity with the established Micro money contract + current spec (never JOD) | repo Delivery 15 corpus; runtime digit scans |
| D-03 | Minus sign U+2212 inside ltr bdi | ASCII hyphen | proper math glyph, present in the bundled latin subset, unambiguous under bidi | fonts.css unicode-range includes U+2212; visual check |
| D-04 | Nav = الرئيسية / العمليات / العملاء / المزيد (4+المزيد) | الذمم (Agent 01), 5 full labels | «الذمم» is finance jargon for non-finance users; 5 labels clip at 320 | Agent 01 width math; Agent 04 open question |
| D-05 | Chart time axis LTR inside charts in RTL | Agent 01's RTL-reading charts | spec 6.13 is explicit — spec wins over agent suggestions | spec §6.13; implemented `direction: ltr` on chart svg |
| D-06 | Arabic ≥14px; 13px only for digit/Latin qualifiers + rail labels | all qualifiers 13px | reconciles spec 6.4 (13px qualifiers) with the 14px Arabic floor; rail label 13px is spec-pinned | tokens.css comment; agents 02/03/04 convergence |
| D-07 | Operational rows in ONE grouped surface (T) | canvas rows | press veil over canvas drops pressable text below AA (Agent 04) — surface-backed rows keep contrast under press | a11y report §2; T markup |
| D-08 | Overlay architecture: non-scrolling phone-screen + phone-scroll + overlay layer | overlays inside scrolled content (v1 bug) | absolute overlays anchored to scrolled content misplaced sheets; native pattern = overlay layer above the scroll owner | found in verification; fixed; re-verified anchored at any scroll |
| D-09 | Rail snapport: `scroll-padding-inline-start: 16px` | plain proximity snap | Chrome's initial proximity snap scrolled the rail past its 16px start padding, breaking the locked peek geometry | measured scrollLeft −16 → 0 after fix |
| D-10 | Peek reporting: measured in-lab values (14/54/84/28) with device-true values (16/56/86/30) documented | claiming 16/56/86/30 as measured | lab frames have a 2px border; honesty over overclaiming, per spec §6.8 | audit table + note |
| D-11 | Sheets own entry; dialogs own irreversible confirms | dialog for forms; swipe-to-destroy | Agent 01 matrix + spec phone patterns | interaction demos |
| D-12 | Positive-on-tint and white-on-atmosphere forbidden as text | using them with small labels | computed 4.27:1 / 3.28:1 fail AA; spec pins text-over-atmosphere to dark ink | color-role-map §2 |
| D-13 | Derived sheet shadow (ink 12%) — not a new color token | scrim-only elevation | scrim edge vs surface = 2.96:1 (<3:1); shadow needed for boundary; derived like press-overlay (ink @ %) | tokens: press-overlay precedent |
| D-14 | Icons: CSS-by-symbol-id mirror registry (`:has(use[href])`) | per-instance mirror classes | single source of truth, no per-usage discipline needed | css §icon registry |
| D-15 | Fonts bundled locally (6 woff2 subsets) | Google Fonts CDN link | lab must open offline with no required remote runtime | spec §8 HTML lab requirements |
| D-16 | Focus ring 2px brand-ink + 2px offset | atmosphere ring (3.1:1) | contrast + visibility (Agent 03) | css; keyboard test |
| D-17 | Text scale via `calc(px * var(--text-scale))` on all font tokens | rem-based root scaling | extraction stays lossless at scale 1; single-property verification at 1.3/2 | tokens.css; 200% audit zero overflow |
| D-18 | Live save demos update cash/metrics/list instantly | static demos | "documented ≠ implemented"; quiet completion needs real proof; no count-up | verified: −182.500→−195.000 etc. |
| D-19 | Verification evidence in a separate view + runtime audit panel | inline notes in composition | spec: audit separate from showcase | Verification view |
| D-20 | Upload location: `zed-ai-runs/<RUN_ID>/` + INDEX.md row per binding repo guide | `reports/YYYY/...` dated folder | current task prompt explicitly prescribes the run folder; INDEX.md update is explicitly required by the repo's binding upload guide (satisfies "root index entry if explicitly required") | UPLOAD_GUIDE.md §2/§4; task §2 |
| D-21 | Token via transient `GH_DOCS_TOKEN` env + in-memory git credential helper | token in remote URL / files | binding repo security rules (never in URL, file, log, commit) | UPLOAD_GUIDE §1; push script |
| D-22 | `switch` on-state = brand-ink fill | positive green, atmosphere | switches are settings (identity), not financial semantics | css |
| D-23 | Amount keypad = native `inputmode="decimal"` platform keyboard | custom NumericSurface keypad (Agent 04 prior art) | platform-correct, accessible, less to build; deviation from the prior prototype expectation is logged rather than hidden | inputs markup; a11y report §8 |
| D-24 | Component-level type extensions 16/18/12 (sheet title, compact figure, chart labels) beyond the four core roles | strict 4-role scale | roles stay canonical; extensions are component tokens, 12px is digits-only (chart axis) | library css :root; tokens untouched |
| D-25 | Amount placeholder «0.000» | «أدخل المبلغ» (Agent 01 draft) | the 3-decimal fils format hint teaches the format; label already says «المبلغ» | sheets + inputs |
| D-26 | Agent 05 binding corrections applied pre-upload: د.أ units 14px, warning/info chips icon+ink in pressable rows, freshness line «محدّث الآن 09:40», amount digits hugging the unit (ltr-align toward inline-end), stale tokens comments corrected, entry-ID «قيد NNNN» proof | shipping as-is; dismissing VLM flag as «designed» | adversarial reviewer rulings with real contrast/bidi evidence | 05 decision-log AC series; re-verified after fix |
