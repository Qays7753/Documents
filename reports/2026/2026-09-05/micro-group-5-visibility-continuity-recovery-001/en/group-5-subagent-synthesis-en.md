# Group 5 — Sub-Agent Review Synthesis

The Group 5 series ran five read-only specialist reviews in the prior session (before the final synthesis commit `782127b`), plus the five pre-implementation research reviews that produced the contracts. This session's recovery added one more full adversarial pass: a fresh production browser QA that found the three defects fixed in `4445da0`. This report records every reviewer's findings and their disposition.

## Prior session — the five final reviews (against `a5f0cd7`)

**5-RV-A — Activity/reporting and period truth. FIX REQUIRED.** Found: reversal status was not propagated across order events, cash-continuity rows, transfer rows, and supplier payment rows (a reversed collection read as active in the reader); `collection_reversed` carried the wrong effect class; purchase reversals and sale revisions rendered creation dates rather than their real dates. Disposition: all fixed in `782127b` (reversal status propagation + one test, effect class aligned with the truth engine's cash-out semantics, real dates) and re-verified live this session (the reversal pair renders «تم التراجع»/«تراجع موثق» with the original preserved).

**5-RV-B — Health/audit/integrity and financial contracts. APPROVE.** Verified the read-only promise (snapshot identity), the check shapes, the audit kinds and their pairings, and the financial contract boundaries (cash/result/owner/amanah separation; unknowns never zero). No findings.

**5-RV-C — Drafts, lock, PWA, backup/restore, continuity. APPROVE.** Verified the draft lifecycle mechanics, the lock's honest promise, the dirty-registry bridge, and the v27 envelope's tamper rejection. Noted the round-trip stripping bug already fixed in `a5f0cd7`.

**5-RV-D — Arabic RTL, mobile UX, accessibility, density, privacy, sharing. FIX REQUIRED.** Found: share copy went through a leading-space path; the lock veil could remount content (form state loss); the draft-saved line rendered a raw ISO date; Arabic 3–10/11–99 plural rules were inconsistent; Home amounts lacked the JOD unit; a dead conditional remained. Disposition: all fixed in `782127b` (straight-to-clipboard copy path with manual fallback, `inert` + stable wrapper tree, Amman-converted DD/MM/YYYY draft lines, plural rules corrected, «د.أ» on Home, dead code removed) and re-verified live this session.

**5-RV-E — Adversarial QA, regressions, CI, release, report delivery. APPROVE.** Re-ran the gate chain independently (all green at `a5f0cd7`), verified diff hygiene (no secrets, no debug, no network calls, no test deletions — 18 existing test files repaired for the new contracts with count gains only), and confirmed CI-safety (lint at the frozen 37-warning baseline, format coverage, audit step expectations).

Parent synthesis in `782127b` fixed all five MAJOR findings and the cheap minors; the worklog records the full list.

## This session — the recovery QA pass (fresh production build)

Acting as the sixth, adversarial reviewer over the exact code that would be pushed:

**F-1 (MAJOR) — storage feedback invisibility.** Export success, tamper rejection, and import preview all rendered inside the collapsed «بيانات البداية والاستعادة» details while the import trigger sits in the visible «استيراد محلي» row — a user uploading a tampered file saw zero feedback. Root cause: the notice render moved into the guided layer without an open trigger. Fixed in `4445da0` (setStorageNotice + chooseImport open the layer); verified live.

**F-2 (MAJOR) — correction context passthrough.** `restoreEvent`/`editEvent` dropped the asset/loan/deposit contexts required by the domain policy, so restoring any reversed Group 4 event always failed validation («أحداث الأصول تتطلب سياق الأصل المرتبط») — the feature was dead for those families while appearing in their UI. Fixed in `4445da0` (typed passthrough on `FinancialRecordInput` through `record`/`restoreEvent`/`editEvent`); verified live with the full reverse→restore cycle and four regression tests.

**F-2b (MAJOR) — MIC-10 restore false positive.** After a legitimate restore, MIC-10 kept failing «اقتناء-معكوس» forever because it read only the asset record's acquisition link, not the product's own restore event. Fixed in `4445da0` (effective acquisition resolution: active original or matching active restore event); verified live (reverse → FAIL, restore → honest WARN) and pinned by a regression test.

**Verified-not-defects:** the MIC-14 prose rounding (intentional); the clipboard permission block in automation (designed fallback); the SW precache serving a stale bundle after rebuild (automation workflow, not product); the synthetic-event file-input quirk (browser behavior; the CDP-level upload path works); the Bash display pipeline eating `[m` sequences (tooling artifact — hex-verified the source is correct).

## Disposition summary

Every MAJOR or blocking finding across all reviews was fixed and retested before merge; the minors were either fixed in the same commits or documented here with their rationale. No finding was dismissed without evidence, and no test was weakened or deleted to achieve green.
