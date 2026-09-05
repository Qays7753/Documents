# Group 5 Recovery and Implementation Report — Visibility, Continuity, and Resilience

Program: Zman→Micro capability transfer (six groups) — Group 5, final resumption session.
Baseline: Micro `main @ 05669a9` (Groups 1–4 merged via PRs #149–#152).
Final: Micro `main @ ad9fc13` (PR #153 merged; local == remote; clean tree; CI green on both the PR run and the post-merge main run).
Date: 2026-09-05. Branch: `agent/group5-visibility-continuity` (ced148f → 5613ec2 → a5f0cd7 → 782127b → 4445da0).

## 1. Recovery gate — the exact stopping point

The assignment opened as a final resumption: the previous Group 5 execution reported "Phase E — push, PR, CI, merge. Setting up credentials per the established pattern" and stopped. The recovery gate verified the actual repository state before any edit:

- Remote Micro `main`: `05669a9` (Group 4 merge). Local HEAD: `782127b` on `agent/group5-visibility-continuity`, tree clean, **already pushed** — `origin/agent/group5-visibility-continuity == 782127b`. No uncommitted work, no untracked files, no stashes, one worktree.
- Four Group 5 commits existed on the branch: `ced148f` (full implementation, 81 files, +5,576/−146), `5613ec2` (draft-persistence gate inversion fix + test-mock repair), `a5f0cd7` (four dead-wire defects found live in browser QA), `782127b` (five-reviewer synthesis — reversal honesty, copy button, lock inertness, DD/MM draft dates, MIC-4 hardening).
- **No pull request existed** for this branch (the newest PR was #152, Group 4). **Zero CI runs** existed for the branch (the single workflow triggers on `pull_request` and `push` to main only).
- The Documents repository (`main @ 508d816`, Group 4 delivery) contained **no Group 5 reports**.
- The previous session's browser-QA evidence (13 screenshots, including production `:4173` with a real service worker) and its five sub-agent reviews were preserved in the worklog.

Conclusion: the push had completed; the PR was never opened. The verified stopping point was inside Phase E, before PR creation. No work was reset, discarded, or reimplemented; nothing required a snapshot because the tree was clean.

## 2. Work preserved (verified in code, not trusted from the log)

All of the prior execution's surfaces were re-verified to exist on `782127b` before this session proceeded: `form-drafts` and `local-security` stores (schema 35, export envelope v27), the canonical `ActivityService`/`ActivityRecord`, the Home «آخر ما حدث» upgrade, the `/finance/activity` reader, statement deep-finance lines plus `statementMarkdownService`, the audit-trail family extensions, MIC-14/15/16 with the honest consistency wording, draft persistence in the four editors (AssetEditor, LoanEditor, SupplierPurchaseEditor, DirectSaleEditor), `localLockService` + `AppLockGate` + `LockSettingsCard`, the dirty-aware PWA update flow (`dirtyRegistry`, `UnsavedChangesGuard` bridge, `PwaRuntimeNotice`), `shareMessageService` + `SharePreview`, the v27 backup envelope with `syncSha256` and tamper rejection, the Group 4 carry-forward fixes, the nine plural fixes and the `--color-line` repair, and the review-synthesis fixes.

## 3. This session's verification and the three defects it found

Rather than trusting the previous session's green gates, the full local gate chain was re-run fresh on `782127b` (EXIT 0: 277/277 domain, 761/761 prototype, PWA 96 precache, `pnpm audit` clean), the production build was re-served through `vite preview` with a real service worker, and a complete fresh browser QA pass was executed in Arabic RTL at 390×844 and 360×800 (33 evidence screenshots in `download/g5-browser-evidence-final/`), covering onboarding, seeded data, the full draft lifecycle, the lock veil, documented reversal and restoration, the statement Markdown download, integrity checks, sharing, backup/restore, offline reload, and the PWA dirty-update block.

The fresh pass found three real defects, all fixed in commit `4445da0` with regression tests:

1. **F-1 (storage feedback invisibility, MAJOR).** Every storage notice — export success, tamper rejection, import preview — rendered inside the collapsed «بيانات البداية والاستعادة» disclosure, while the import trigger lives in the visible «استيراد محلي» row of the first section. A user uploading a tampered file saw nothing at all: rejection was enforced but invisible. Fix: `setStorageNotice` now opens the layer, and `chooseImport` opens it on preview; the existing scroll effect carries the user to the feedback. Verified live: rejection and preview both visible after the fix.
2. **F-2 (correction context passthrough, MAJOR).** `restoreEvent` and `editEvent` built their replacement events through `record()`/`createFinancialEvent` without the asset/loan/deposit contexts. Domain policy requires those contexts for the Group 4 event families, so restoring any reversed asset/loan/deposit event always failed with «أحداث الأصول تتطلب سياق الأصل المرتبط» (nothing was written — honest atomic failure, but the feature was dead for those families). Fix: `FinancialRecordInput` carries the three contexts; `record`, `restoreEvent`, and `editEvent` pass them through. Verified live (restore succeeded and the new event carries its context) plus four service-level regression tests.
3. **F-2b (MIC-10 restore-awareness, MAJOR).** After a legitimate restore, MIC-10 still failed «اقتناء-معكوس» forever, because the asset record's `acquisitionEventId` link still points at the reversed original and the check read only that link — not the product's own restore event (deterministic `restore:` idempotency key). Fix: MIC-10 now reads the *effective* acquisition (active original, or an active restore event with matching type/context). Verified live across the full cycle: reverse → FAIL (honest), restore → back to WARN (unknown asset life only).

An additional observation, documented as intentional and not a defect: MIC-14's WARN prose rounds the drift to whole dinars («سالب (363 د.أ)») via `Math.round` while the exact figure (362.50) is displayed on the adjacent drift line.

## 4. Scope delivered (cumulative, `05669a9` → `4445da0`, 83 files, +5,802/−151)

- **Unified activity reader (4.1).** A canonical read-only `ActivityService` over the existing stores — 15 event families, 8 effect classes mirroring the domain delta table, statuses derived at read time (active/reversed/superseded/cancelled/pending), reversal links, per-family caps, `recordedAt` ordering, period windows, transfers grouped by `transferId`, unknown cost stays `null`. Home shows «آخر ما حدث» (service-composed label + effect + amount + English-digit JOD + DD/MM/YYYY + deep link); `/finance/activity` provides the full reader with family chips, period ranges, and custom range; every row deep-links to its owning surface. Zero new writes, zero recomputed financial truth — the reader joins the canonical-statement lock.
- **Period statement + local Markdown report (4.2).** The statement renders the deep-finance layers (depreciation, write-off loss, disposal result, retained-deposit revenue, asset book value, standing loans, pending retained deposits) and an unresolved-values layer; «خذ التقرير معك» generates an Arabic RTL Markdown snapshot locally (BOM, English digits, DD/MM/YYYY, truth lines, snapshot disclaimer, no secrets, no unrelated records) and downloads it with the deferred-revoke pattern.
- **Health checks MIC-14/15/16 (4.3).** Unallocated-cash truth (negative → WARN with drift), idempotency-key uniqueness, owner-money separation. PASS/WARN/FAIL with plain Arabic explanations, source links, version stamps (schema 35 / export 27), no auto-repair, and the explicit «الاتساق لا يعني الربحية» honesty line.
- **Append-only audit trail (4.4).** Five new correction kinds (delivery reversal, deposit classification, inventory reversal, owner reversal, asset contract revision), the Group 4 reverse+replace pairing repair, and ISO → DD/MM/YYYY labels everywhere; originals remain traceable with reasons and old/new effect deltas.
- **Draft lifecycle (4.5).** `formDraftService` + `useFormDraft` in the four editors with the gate-inversion fix (first keystroke saves), dirty-gated writes, explicit restore offer (clean forms never silently overwritten), full-field restore, final-save clearing, discard removal, refresh/close/offline survival, and zero financial events before explicit save.
- **Local lock + PWA updates (4.6).** PIN hashed with WebCrypto SHA-256 (salted, per-device), failed-attempt backoff, idle auto-lock options, `AppLockGate` veil with an inert/stable tree (forms stay mounted under the veil), public recovery routes exempt, honest no-recovery copy; dirty-aware PWA updates refuse to reload over dirty forms and the update button explains why.
- **Manual sharing (4.7).** `shareMessageService` drafts customer-safe texts (no cost, no margin) for orders, collections, deliveries, reminders, and statements; `SharePreview` offers an editable deep preview with explicit send/copy, manual fallback, Jordanian phone normalization, and privacy copy. No automatic sending, no contact access, no persistent notes/snippets library (the permanent exclusion).
- **Backup/restore v27 (4.8).** The export envelope carries a SHA-256 integrity digest (pure-JS FIPS 180-4 `syncSha256`), embedded counts, and app version; `prepareImport` verifies the digest before any preview (tamper rejection); the v27 round-trip no longer strips the optional fields; restore is validated and atomic with a post-restore health-check verdict card; the Group 4 v26/34 pair remains accepted.
- **Information architecture (4.9).** The five-seat shell is untouched («مشروعي الآن | العمل | سجّل (FAB) | مالي | أدواتي»); no sixth seat, no second bar, no competing FAB; no duplicate dashboard or competing financial formula — all reads join the canonical reader.

Also carried forward from the prior session: the deposit numeric-effect line on OrderDetail, nine plural sites split into `g5Plurals.ts`, three reason inputs split on AssetDetail, the `--color-line` → `--color-border` repair, and the review-synthesis items (reversal status across order events/cash/transfer rows/supplier payments, collection-reversal effect class, real dates on purchase reversals and sale revisions, straight-to-clipboard share copy, AppLockGate stable tree, Amman-converted draft-saved lines, MIC-4 expense-context comparison, Arabic 3–10 plural rules, JOD unit on Home amounts).

## 5. Verification — final gates

All gates ran on the exact push head (`4445da0`) and were re-run on merged main (`ad9fc13`):

| Gate | Result |
| --- | --- |
| Typecheck (root + prototype) | clean, twice |
| Lint | 0 errors / 37 warnings (frozen baseline) |
| Format (`prettier --check`) | clean |
| Text density | all surfaces within caps (documented Group 5 ratchets) |
| Design token guards + stylelint | clean |
| Domain tests | **277/277** (23 files) |
| Prototype tests | **766/766** (120 files — +9 Group 5 tests, +5 this session) |
| Production build + PWA | success, 96 precache entries (2,052.6 KiB) |
| Local dependency audit | no known vulnerabilities |
| Secret scan | clean (no tokens in diff, exports, or reports) |
| Browser QA (production, RTL, 390×844 + 360×800) | 33 screenshots, 0 console/page errors, no overflow |

## 6. CI and merge

| Workflow | Job | First result | Classification | Remediation | Final result | Run |
| --- | --- | --- | --- | --- | --- | --- |
| CI | checks (PR #153, head `4445da04`) | success | — | none needed | success | [33947927146](https://github.com/Qays7753/Micro/actions/runs/33947927146) |
| CI | checks (push, main `ad9fc13`7) | success | — | none needed | success | [33948024196](https://github.com/Qays7753/Micro/actions/runs/33948024196) |
| Cloudflare Pages | external check-run on PR head | success | — | — | success | PR #153 checks |

No failures occurred in this cycle; no retrigger commit, no `--admin`, no protection bypass, no force-push, and no test deletion were needed or used. PR #153 (5 commits, 83 files, +5,802/−151) merged via the API; local `main` was pulled and verified equal to `origin/main` at `ad9fc13` with a clean tree, and the full gate chain re-ran green on the merged head.

## 7. Limitations (genuine, unresolved)

- The `autoConsume` template flag remains a read-only declaration rather than per-line values (documented Group 4 carry-forward; the atomic single-confirmation contract is preserved; assigned to a future group).
- The agreement-time deposit wallet attribution remains deferred (Group 4 carry-forward as-is).
- The quick-entry sale sheet (FAB «تسجيل بيع») is intentionally not draft-enabled — drafts belong to the full-page editors; the FAB sheet is a momentary entry, not a workspace.
- Clipboard write in headless/automation contexts can be permission-blocked; the product's manual fallback path is the designed honest behavior in that case (verified).
- MIC-14's WARN prose rounds the drift to whole dinars while the exact value shows on the drift line (intentional `Math.round`; cosmetic).
