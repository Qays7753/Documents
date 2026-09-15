# Group 1 Implementation Report — Guided Financial Entry, Expense Classification, Allocation, and Financial Foundation

| | |
|---|---|
| **Report ID** | micro-group-1-guided-financial-entry-001 |
| **Date** | 2026-09-03 |
| **Task** | Group 1 of the six-group Zman→Micro transfer program (standalone execution) |
| **Target repository** | `Qays7753/Micro` — implementation branch `agent/group1-transfer-guided-financial-entry`, merged to `main` via PR #149 |
| **Final Micro `main` commit** | `761638b` (merge); feature commit `bc2e4c5`; baseline before the group: `4db6a5f` |
| **Reference repository (read-only)** | `Qays7753/zman-app` — `main` @ `bdd63ab` (journey/UX reference only; no Zman mechanism was copied where it conflicted with Micro's financial truth rules) |
| **Governing contract** | `docs/contracts/27-guided-financial-entry-contract.md` (new, in Micro) |
| **Scope executed** | prompt §5.1–§5.9: guided expense entry, category classification, cost nature presentation, project relationship + allocation review, paid/payable/purchase/asset path distinction, effect explanation before commit, canonical period-result foundation, financial-integrity foundation, accounts/wallets/owner/opening-state journey review |

## 1. Executive summary

Group 1 delivers the guided financial-entry foundation on top of Micro's existing strong financial core. The owner can now record a real business event through a question sequence that mirrors how they think (what happened → how much → from where → for what → nature → relationship → allocation → knowledge → what will change → confirm), optionally tag expenses with a personal, human classification («تصنيفي للمصاريف») that answers «شو صار على البنزين؟» without touching a single financial delta, review a shared-expense allocation before saving, see an effect preview derived from the exact committed intent, and run a read-only one-tap financial integrity check («فحص سلامة مالي») that proves the numbers agree across every surface.

The group was delivered as one branch (40 files changed, +3,894/−153), guarded by 41 new tests (5 domain + 36 prototype), a full `pnpm check` gate (typecheck, lint at the 37-warning baseline ceiling, formatting, text-density with three newly measured surfaces, design tokens, 231 domain + 607 prototype tests, PWA production build), an independent adversarial QA pass whose findings were all fixed before merge, and a live browser verification of the production build on a 390×844 RTL phone viewport with zero console errors.

Two pre-existing defects were found and fixed with documented decisions: (1) the export/import verifier rejected **any** backup file containing a wallet transfer or transfer reversal (D-025 — the operationKey is one deposit unit that may write a coupled pair); (2) the financial-event editor's unsaved-changes guard was latently inert (dirty-state re-snapshotted every render). Both fixes carry regression tests.

## 2. Completion-state gate (what was found before any work)

- Micro `main` @ `4db6a5f` contained the *previous* program's six groups (PRs #142–#148: experience foundation, financial truth, tools/products/orders, acceptance, audit, closure). The **new** transfer program (this prompt) had **no commits**: the design basis (`zaman-to-micro-gap-analysis-001`, delivered 2026-09-03 in the Documents repository) cites `4db6a5f` as its read-only baseline and no implementation existed after it.
- Working tree clean; no recovery branches for this program; no partial Group 1 work.
- Baseline validation on `4db6a5f`: `pnpm install --frozen-lockfile` OK, typecheck PASS, lint 0 errors / 37 warnings (ceiling), 226 domain tests PASS, 571 prototype tests PASS, PWA build PASS.

## 3. What was implemented (by scope item)

### 3.1 Guided expense entry (§5.1)

- **Field order in `FinancialEventEditor`** now follows the guided question sequence: type/title → amount (with shared total/percentage fields when the mode needs them) → **wallet destination («وجهة الصرف — من وين طلع المبلغ؟»)** → date → counterparty → progressive-disclosure details layer → note → save. The wallet question previously existed only in the quick sheet; the detailed path now has it too, using the sheet's exact vocabulary («من الكاش غير الموزع» / «{wallet} — تغطية من رصيدها»).
- **Fast path** (QuickActionSheet): still exactly one mandatory input (amount); optional note, optional wallet, and now an **optional category chip row** (≤6 suggestions, single tap, deselect allowed) placed after the fields and before the effect line — never above the amount, never requiring a keyboard.
- **Effect line** extended with the honest negatives clause: «…وبلا حركة أمانة ولا سحب مالك.»
- **Draft persistence** (per-type key `micro.finance-draft.<type>.v1`): input-only, written when the form is dirty, offered for restore on reopen with an explicit two-button banner («استرجع المسودة» / «تجاهلها»), cleared by discard and by successful save, never auto-commits a record. Guarded with try/catch (private mode / quota).

### 3.2 Expense category classification (§5.2, §5.3)

- `OperatingExpenseContext += categoryLabel?: string | null` — a human, optional label; normalization (trim, internal-whitespace collapse, blank → null) with an 80-character limit measured **after** normalization; rejection is explicit with an Arabic error (no silent truncation). The field is frozen with the event; `editEvent`/`restoreEvent`/reversal copy it verbatim; a label change is a documented reverse+re-record.
- The category is **provably money-neutral**: `deltas()` reads only type/amount/relationship→allocation, and twin tests at the domain and service levels (all shared modes) assert identical five-delta outputs with and without the label.
- Suggestions are a **derived read model** (`deriveExpenseCategorySuggestions`): recently used labels (≤6, newest first) merged with seed suggestions (بنزين، رواتب، إيجار، كهرباء، مواد، توصيل، تسويق، أدوات عمل) up to 8 total. No managed catalog, no store, no write — the orphan-merge property is inherent to derivation.
- Cost nature (ثابت/متغير/مختلط/غير متأكد) already existed as `behavior`; the guided question («طبيعته: ثابت ولا بتغير؟») is now the field label. Nature and category remain distinct dimensions (salaries can be «رواتب» + ثابت; fuel «بنزين» + متغير; electricity «كهرباء» + مختلط; uncertain stays «غير متأكد» rather than receiving a guessed value).
- **Reporting payoff**: the statement gains a collapsed «مصاريفي حسب تصنيفي» block — per-tag totals with per-event source rows (paid and owed together; unclassified events group honestly under «غير مصنّف»), and the events layer shows «تصنيفك: <label>» in the expanded row detail.

### 3.3 Project relationship and allocation (§5.4)

- The four safe modes (fixed amount / percentage / estimate / deferred) were already in the domain; Group 1 added the **AllocationReviewCard**: label:value rows (no inline bidi-unsafe equations) shown before save inside the details layer — total, project share (+percentage), the outside-the-project remainder, and «المتبقي غير موزّع» (0.00 when fully distributed; the full total when deferred; «إجمالي المصدر غير محفوظ» for fixed/estimate). The share is derived by the **same** domain function the commit uses (`calculateSharedProjectShareMinor`), so the review cannot drift from the record.
- Micro's truth is preserved and explained: `shared` means shared between the project and home/another activity; the remainder is honestly outside the project (never zeroed, never double-assigned; allocation metadata creates cash-continuity attribution entries, not financial events).

### 3.4 Paid vs payable vs purchase vs asset (§5.5)

- The event types keep their exact deltas. The guided journey now distinguishes them explicitly: the payable editor's effect preview states «لا يتغير الكاش الآن — يزيد ما عليك…» and the settlement preview states «لا يُسجل المصروف مرة ثانية».
- **Path guidance** inside the details layer: a real text-action to the suppliers/purchases path for materials («شراء خامات ستبقى في المخزون؟ سجّله من الموردون والمشتريات — لا كمصروف عادي.») and one honest deferral line for the not-yet-built paths («الأصول طويلة الاستخدام والقروض الشخصية لا تُسجَّل من هنا — مساراتها قادمة لاحقًا.») — no invented financial effect, no fake route.

### 3.5 Effect explanation before commit (§5.6)

- The static «الأثر المعروف» line is replaced by **EventEffectPreview**, derived from the actual committed intent: the editor's save payload is expanded by the **same pure module the service uses** (`expenseRecordIntent`, extracted from `record()` in this group — one expansion path for commit and preview), then dry-run through the domain creator `createFinancialEvent` itself; the resulting five deltas are formatted as Arabic lines (primary effect with wallet attribution, combined negative clause «بلا حركة أمانة ولا سحب مالك», category note «لا يغيّر الأثر المالي»). Invalid/partial input falls back to the static text; the preview region has a fixed min-height so nothing above the amount field can jitter.
- Attribution honesty after save: if wallet coverage fails (e.g., insufficient wallet balance), the page stays mounted with «حُفظ الحدث محليًا، لكن نسبته للمحفظة لم تتم… — المال محفوظ ضمن الكاش غير الموزع», plus «افتح السجل المحفوظ» and a safe return button — verified live. The idempotency key is per-mount, so a retry cannot double-record; the attribution uses the `${key}:attribute` operation key exactly like the quick sheet.

### 3.6 Canonical period-result foundation (§5.7)

- `ProjectFinancialService.readRecordedPeriodResult` is designated **the** canonical period-result producer (it already was, in practice: statement and insights consume it; the owner-entitlement evidence injects it). Group 1 adds the missing locks: `periodResultCanonical.test.ts` asserts **full-object deep-equality** across reader / `statement.read().result` / `insights.period`, an **invocation spy** (any competing implementation stops calling the canonical reader and fails the test), null-as-value equality (unknown-cost direct sale produces the same «غير متاح + أسباب» state on every surface), and the derived-total consistency.
- The one page-level period arithmetic (`Statement.tsx` revenue sum) moved into the service as `StatementReading.recognizedRevenueTotalMinor`.
- Fenced non-competing reads are documented in contract 27 (home away-digest, G5 `expenseInputs`, recurring-margin `allocation.resultMinor` naming collision).

### 3.7 Financial-integrity foundation (§5.8)

- `IntegrityCheckService` — strictly read-only (only list/read service methods; an acceptance test deep-compares the full store snapshot before/after a run, including corrupted fixtures). Stable check identifiers with a reserved registry for later groups: **MIC-1** (period-result cross-surface consistency incl. null agreement), **MIC-2** (cash structure: pair-aware operationKey rule, balanced transfer groups, reversal references, sourceRef pairing; negative wallet balance and negative unallocated are WARN — legitimate owner-draw/pre-funding states), **MIC-4** (every event rebuilt through the domain creators and compared on all five deltas + context; share re-derivation; stale settlement references are WARN with honest copy), **MIC-7** (amanah ≥ 0 read-back + position agreement — the import-bypass detector), **MIC-9** (knowledge honesty: null ⟺ declared unknown cost; pending states are «قرار معلق، ليس خطأً» WARN, windowed to the checked month).
- `/tools/integrity` — a **surface** route (bottom nav stays), registered in the router, the canonical-fallback registry (`/tools`), and contract 26. UI: promise card «يقرأ أرقامك ولا يغيّر شيئًا», verdict card with run timestamp (DD/MM/YYYY, English digits), five check cards with status **word + icon + color** (سليم/تحذير/خلل — never color alone), drift lines, collapsed offender ids, and deep links to the focused event row or the wallet ledger. No auto-fix, ever.
- Doorways: a Tools module-states row («فحص سلامة مالي», always enabled) and a Finance truth-section text-action («فحص سلامة مالي — اطمن على أرقامك») preserving `?from`.
- Import hardening in the same scope: aggregate amanah ≥ 0 now also checked at import time.

### 3.7 Accounts/wallets/owner/opening journey (§5.9)

Reviewed against Zman (read-only) with the conclusion that Micro is stronger everywhere this group touches (unknown openings stay «غير محدد بعد» — never 0.00; transfers are atomic paired entries; owner money never enters income/expense). No wallet/owner surface was redesigned; the only changes were the wallet **question** in the expense editor (sheet vocabulary) and honesty wordings already covered above. The loan hint is covered by the expense-editor deferral line; the OwnerWithdrawalEditor hint is deferred (its page is at its text-density cap — documented).

## 4. Data, migration, and compatibility

- **Schema 30 → 31, export 22 → 23** in the single guarded location (`storage/local/types.ts`), with the legacy pair `22/30` added to `prepareImport` acceptance. Old files migrate with the label **absent → null** (no backfill, no invented categories; legacy events surface as «غير مصنّف»).
- Import normalization runs **inside `expenseContext`** (trim/collapse/blank→null); non-string or >80-normalized-chars labels fail cleanly with the device data untouched (tested).
- Round-trip: a labeled expense survives `createVerifiedExport` → `prepareImport` → `confirmImport` verbatim (tested); the transferred-transfer regression (below) now round-trips too.
- Defect fix **D-025**: `cash.transfer` writes its out/in pair with **one operation key**, and a transfer reversal writes a two-entry reversal pair with one key and its own transferId. The import validator previously required per-entry key uniqueness and pushed reversal pairs into transfer groups — so **every backup containing a transfer or transfer reversal was rejected** (and `createVerifiedExport` refused to bless it). The validator now treats the operationKey as one deposit unit: duplicates are allowed only for the two documented coupled pairs, reversal pairs are excluded from transfer groups, reversal-of-reversal is rejected (mirroring the live write path), and the reversal mirror check requires a non-reversal original. Regression tests included; MIC-2 mirrors the same rules at runtime.
- Guard fix: `FinancialEventEditor` passes a stable reset token to `useFormDirty` (the hook re-snapshotted every render without a token, leaving `isDirty` permanently false — the guard never fired). After a successful save the token flips again (SA-5 fix 3), so the guard does not block a saved record.

## 5. Files changed (summary)

40 files, +3,894 / −153: domain types/policies (label), store constants, transfer service (migration + validator fixes), 3 new application modules (`expenseRecordIntent`, `expenseCategorySuggestions`, `integrityCheckService`) + `record()` refactor to the shared expansion, statement service (grouping + derived total), composition root, `FinancialEventEditor` (guided journey + drafts + wallet + honesty), `QuickActionSheet` (chips + effect clause), `AllocationReviewCard` + `EventEffectPreview` components, `EventsLayer` label display, `Statement` grouping block, `ToolsIntegrity` page + router + fallback registry + Tools row + Finance doorway, CSS additions, density registry, 8 new test files (+3 extended), and docs (contract 27, contract 26 row, current-state §23, todo, CHANGELOG, decision log D-025/D-026).

## 6. Verification

- `pnpm check` (full gate) — **green**: typecheck (root + prototype), lint 0 errors / 37 warnings (the baseline ceiling; zero new warnings), format, text-density (all surfaces within caps; ToolsIntegrity 32/32, FinancialEventEditor 138/138, Statement 89/89 measured on first day; Tools 28/34; Finance 181/181), design-token guards + stylelint, **231 domain tests (20 files)** and **607 prototype tests (96 files)**, production PWA build (80 precache entries).
- **CI on GitHub Actions**: `CI: completed success` for commit `bc2e4c5`; PR #149 merged after CI + adversarial review; remote `main` = `761638b`, local tree clean, local == remote.
- **Live browser QA** (production preview, 390×844, agent-browser): full first-use; Scenario A (quick fuel 25.00 JOD with wallet + بنزين chip → effect line with wallet name and negatives → receipt → record shows «تصنيفك: بنزين»); Scenario B (editor 300 JOD, category رواتب, nature fixed, wallet → preview; the attribution-failure honesty path fired for real on a zero-balance wallet and kept the page mounted with the record link); Scenario C (shared 100 JOD / 60% → review card rows + derived 60.00 share); Scenario E (payable preview); integrity page run → «سليم — الأرقام متسقة» with all five checks; Finance doorway; statement grouping (رواتب 300.00 + بنزين 25.00). **Zero console/page errors throughout.**
- **Adversarial QA (SA-5)**: verdict FIX REQUIRED with one major + three minors — all fixed pre-merge (stale settlement reference demoted to WARN + regression test; reversal context comparison; post-save guard disarm; reversal-of-reversal rejection; plus notes adopted: preview min-height, unknown-opening WARN copy, MIC-9 windowing). Backlog notes documented.

## 7. Scenarios A–J (acceptance coverage)

| Scenario | Result | Evidence |
|---|---|---|
| A — quick fuel expense | Pass | Live QA (wallet + optional chip + effect with negatives + receipt) + `QuickActionSheet.category.test.tsx` (label commit, deselect→null, honest negatives) |
| B — fixed salary one project | Pass | Live QA (editor, wallet, رواتب+ثابت, preview) + guided dom tests (wallet select, preview lines, chips commit) |
| C — shared 60/40 allocation | Pass | Live QA (review card, derived 60.00) + guided dom test (reconciled rows incl. «المتبقي غير موزّع 0.00») + domain/service twins |
| D — estimated/deferred | Pass | Service twins (estimate/defer) + integrity WARN «قرار معلق» + defer zero-rule domain test |
| E — payable expense | Pass | Live QA payable preview + effect copy «لا يتغير الكاش الآن» + settlement no-second-expense domain semantics |
| F — purchase vs expense | Pass | Guidance text-action to `/suppliers` + honest future-path line (dom test asserts both) |
| G — classification-only invariance | Pass | Domain + service twins (all modes, edit/restore/reversal copy) |
| H — unknown opening | Pass | Untouched existing «غير محدد بعد» surfaces; integrity page never renders unknown as 0 (empty wallet store → PASS with «لا محافظ معلنة بعد») |
| I — duplicate submit / reload | Pass | Per-mount idempotency keys (unchanged), `${key}:attribute` attribution retry-safety, drafts never auto-commit (dom tests) |
| J — period-result consistency | Pass | `periodResultCanonical.test.ts` (deep-equal + spy + null-as-value) + MIC-1 + live integrity run «سليم» |

## 8. Decisions register (this group)

1. **Category label placement** — inside `OperatingExpenseContext` (rides reversal/edit/restore copies; structurally impossible on non-expense events).
2. **Hybrid suggestions** — derived labels ∪ static seeds (the prompt's examples as presentation constants, not a managed store) — deviation from the gap analysis's derived-only recommendation, per this prompt's authority («initial suggestions may include…»).
3. **D-025** — operationKey is one deposit unit; coupled pairs are legal duplicates in import validation and MIC-2.
4. **D-026** — Finance truth-section doorway lands inside a pre-existing text-density counter blind spot (the whole truth section was never measured); measured set unchanged (181/181) so no cap raise; counter fix deferred as its own decision.
5. **Multi-project A/B allocation mapping** — Micro's shared-share model is preserved and explained (project share vs outside-project remainder), per the prompt's instruction to keep Micro's truth and explain it in the UI.
6. **Quick-sheet knowledge "known"** — truthful: the owner typed the actual paid amount; behavior "unknown" is a different dimension (documented).

## 9. Known limitations / deferred (explicit)

- TR-03 (statement export artifact), TR-05 (activity layer), TR-07 (inventory bridge), TR-09 (undo-delete), EventsLayer tag filter (needs a `?tag` vocabulary entry in contract 26), OwnerWithdrawalEditor loan hint (page at cap), MIC-3/5/6/8/10 (registry reserved), density-counter truth-section blind spot fix — all deferred to later groups with reasons recorded in contract 27 §7 and the decision log.
- Device-level QA (real Android/iOS), production Cloudflare Pages acceptance, and human Pilot remain outside this group, exactly as the repository's acceptance boundaries require.

## 10. Final state

- Micro `main` @ `761638b` (PR #149 merged after green CI); local and remote agree; working tree clean.
- Reports delivered to the Documents repository under `reports/2026/2026-09-03/micro-group-1-guided-financial-entry-001/`.
- No secrets, tokens, or credentials exist anywhere in the Micro diff (verified in the SA-5 scope audit).
