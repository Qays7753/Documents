# Group 1 Financial Contracts — Category, Nature, Relationship, Allocation, Effect Preview, Canonical Result, and Integrity

| | |
|---|---|
| **Report ID** | micro-group-1-guided-financial-entry-001 (financial contracts) |
| **Date** | 2026-09-03 |
| **Governing document in-repo** | `docs/contracts/27-guided-financial-entry-contract.md` (Micro @ `761638b`) |
| **Related contracts** | 05 (financial P0 policies), 08 (expense classification), 14 (period result & allocation), 23 (event correction boundary), 26 (navigation & deep links) |

This report is the English statement of the binding contracts Group 1 introduced or extended. The Arabic contract in-repo is authoritative; this document mirrors it for delivery.

## 1. Concept separation contract (the six dimensions)

| Concept | Meaning | Example | Where it lives |
|---|---|---|---|
| Financial event type | What financially happened | Operating expense paid now (`operating_expense_cash`) | `FinancialEventType` (unchanged; exact delta table) |
| Category label | What the money was spent on | Fuel, salaries, rent | `OperatingExpenseContext.categoryLabel` (new) |
| Cost nature | How it behaves over time | Fixed / variable / mixed / unknown | `OperatingExpenseContext.behavior` (existing) |
| Relationship | What it belongs to | The project entirely / shared with home or another activity | `OperatingExpenseContext.relationship` (existing) |
| Allocation | How a shared amount is assigned | Fixed share / percentage / owner estimate / deferred | `sharedProjectShare` (existing; review card new) |
| Knowledge state | How certain the information is | Known / estimated / needs review | `OperatingExpenseContext.knowledge` (existing) |

Binding rule: **a category is a classification and reporting dimension only.** It must never change: the cash delta, the payable delta, the owner-capital delta, the operating-expense delta, the amanah delta, `sharedProjectShare`, or `resultMinor`. Twins tests at domain and service level are the enforcement.

Worked example (now expressible end-to-end):

```
Financial event: operating expense paid
Category: بنزين (fuel)
Nature: variable
Relationship: shared
Allocation: agreed percentage 60% of a 100.00 JOD household bill → project share 60.00 JOD
Amount recorded: 60.00 JOD (the project share)
Wallet: cash drawer (covered via an allocation entry, not a second event)
```

## 2. categoryLabel data contract

| Clause | Rule |
|---|---|
| Type | `categoryLabel?: string \| null` on `OperatingExpenseContext` only (never on the event root, never on non-expense events — structurally enforced) |
| Normalization | Trim both ends; collapse internal whitespace to single spaces; blank → `null` |
| Length limit | ≤ 80 characters measured **after** normalization (domain and import use the same rule) |
| Over-limit behavior | Explicit rejection with the Arabic message «تصنيف المصروف يتجاوز ٨٠ حرفًا؛ اختصره أو اتركه فارغًا.» — no silent truncation |
| Freezing | Frozen with the context object at creation; carried verbatim by reversal, atomic edit replacement, and restore |
| Corrections | A label change is a documented reverse + re-record (the existing correction contract). No rename/merge tools; no silent history rewrite |
| Migration | Schema 30→31 / export 22→23; the legacy pair 22/30 is accepted and migrates absent → null; **no backfill**; legacy events report as «غير مصنّف» (honest absence, never zero) |
| Import | Labels are normalized inside `expenseContext` at import; non-string or over-limit (post-normalization) labels invalidate the snapshot **before** any data is touched |
| Idempotency | Inherits the event's idempotency key — no separate write path exists |

Suggestions contract (read model): `deriveExpenseCategorySuggestions(events)` = recently used distinct labels from non-reversal events (≤6, newest first) ∪ seed list (بنزين، رواتب، إيجار، كهرباء، مواد، توصيل، تسويق، أدوات عمل) to a total of 8 (6 in the quick sheet). Pure derivation — no store, no writes, orphans included by construction.

## 3. Guided-journey contract

Question order (editor): **شو صار؟ → قدّش؟ → من وين طلع المبلغ؟ → (التاريخ) → لشو؟ (التصنيف) → طبيعته؟ → علاقته؟ → حصته؟ → حالته؟ → شو راح يتغير؟ → احفظ**.

- Fast path (quick sheet): amount is the only mandatory input; wallet and category chips are optional single taps; the sheet never requires a keyboard beyond the amount.
- Wallet attribution («وجهة الصرف») exists only for cash-spending types in this group (`operating_expense_cash`); the commit pattern is `record()` followed by `distributeUnallocated(-amount, wallet, sourceRef {expense id}, operationKey \`${idempotencyKey}:attribute\`)` — one event, at most one attribution entry per root key, retry-safe.
- Attribution-failure honesty: the record is saved; the failure message and a deep link to the saved record are shown **before** any navigation; the primary button becomes the safe return.
- Path guidance: purchase → real link to suppliers; assets & personal loans → one honest deferral line («مساراتها قادمة لاحقًا») — no invented event type, no fake route.
- Draft persistence (`micro.finance-draft.<type>.v1`): input-only; restore is an explicit action; discard and successful save clear the key; no code path converts a draft into a record without the save button.

## 4. Effect-preview contract (derived from committed intent)

1. The preview input is the exact payload the save button will send (same amount semantics, same context, same shared-expense mode).
2. Expansion happens through `expenseRecordIntent` — **the same pure module `ProjectFinancialService.record()` calls** (extracted in this group; one expansion for commit and preview).
3. The expanded intent is dry-run through the domain creator `createFinancialEvent` itself; the preview renders the resulting five deltas (never hand-computed copies).
4. Rendering rules: primary effect line with wallet attribution; payable line states cash does not change now; settlement states the expense is not recorded twice; unallocated-shared states it will not enter the period result yet; combined negative clause «بلا حركة أمانة ولا سحب مالك»; category note «التصنيف … لقراءتك لاحقًا — لا يغيّر الأثر المالي».
5. Invalid or partial input falls back to the static known-effect text — no speculative numbers.
6. The preview region has a fixed minimum height (anti-jitter law: no conditional rows above input fields).

## 5. Allocation contract (unchanged rules, new review surface)

- Modes: fixed amount, percentage (bps 1–10000, round-half-up re-derivation), owner estimate, deferred. Validation is the domain's (unchanged): percentage requires total+bps+calculatedShare consistency; allocated amount equals calculatedShare; unallocated amount equals total; knowledge is derived from basis; unallocated-shared keeps `operatingExpenseDelta = 0`.
- The AllocationReviewCard renders label:value rows only (no inline equations — bidi safety) and derives the share with the same domain function; the remainder is labeled honestly («الباقي خارج حصة المشروع — بيت أو نشاط آخر»); deferred shows the full total as «المتبقي غير موزّع» and never as zero.
- Mapping note (authoritative): the prompt's multi-project example («60% Project A / 40% Project B») maps to Micro's model as a 60% project share and a 40% outside-the-project remainder — Micro has one project plus external co-use, and the unallocated portion is deliberately not attributable until the owner decides.

## 6. Canonical period-result contract

- `ProjectFinancialService.readRecordedPeriodResult(from, to)` is the only producer of period-result numbers. Consumers: Finance period view, `StatementService.read` (embeds it), `readFinancialInsights`, owner-entitlement evidence.
- No page performs period arithmetic; the one historical page-level sum moved to `StatementReading.recognizedRevenueTotalMinor`.
- `null` is a value: when the result is unavailable (unknown direct-sale cost), every surface shows the same unavailable state and the same reasons; MIC-1 cross-checks this at runtime.
- Guard: `periodResultCanonical.test.ts` — full-object equality across surfaces, invocation spy on the canonical reader, null-value equality, derived-total consistency. Any second implementation drifts or stops calling the canonical path and fails the suite.
- Fenced non-competing reads (documented, not competing): home away-digest (`homeControlCenterService` — last recorded day, not a period result), G5 `expenseInputs` (its own contract), recurring-margin `allocation.resultMinor` (name collision only).

## 7. Integrity-check contract

- **Promise:** «يقرأ أرقامك ولا يغيّر شيئًا» — enforced architecturally: only read service methods are called; the zero-writes acceptance test deep-compares the store snapshot before/after (including corrupted fixtures); there is no auto-fix, and fix paths are deep links to existing documented correction surfaces.
- Result shape (stable, reserved for later groups): `{ id: "MIC-*", titleAr, status: PASS|WARN|FAIL, detailAr, driftMinor?, offenderCount?, offenderSampleIds?, deepLink? }`; report adds `{ runAt, from, to, overall, checks }`.
- Check registry delivered in Group 1:

| ID | Title (Arabic) | Rule (derived from a tested domain rule) | Deliberate-state behavior |
|---|---|---|---|
| MIC-1 | تطابق نتيجة الفترة | Reader vs statement result vs insights — full-object equality; drift → FAIL with both values | null agreement is checked, not just numbers |
| MIC-2 | بنية الكاش والمحافظ | Pair-aware operationKey rule; balanced transfer groups; reversal references existing non-reversed originals; sourceRef pairing; unknown wallet | Negative wallet balance (owner draw) and negative unallocated → **WARN** |
| MIC-4 | سلامة الأحداث والتوزيع | Every event rebuilt via domain creators; all five deltas + context compared; share re-derivation; settlement must reference an existing payable | Settlement pointing at an edited/deleted payable → **WARN** («المرجع قديم») |
| MIC-7 | رصيد الأمانات | Aggregate amanah ≥ 0 (import-bypass detector) + equals `readPosition` | Zero amanah → PASS with an explicit «صفر معلن» wording |
| MIC-8 | — | reserved | — |
| MIC-9 | صدق درجة المعرفة | `resultMinor === null ⟺ directSaleCostUnknownCount > 0`; incomplete ⇒ reasons non-empty; windowed pending count | Pending (deferred/needs-review) → **WARN** «قرار معلق، ليس خطأً» |

- MIC-3/5/6/8/10 identifiers are reserved for later groups (correction balance, collection consistency, deposit decisions, inventory, retained-deposit visibility) — the shapes are stable so later groups extend the registry without migration.
- Severity law: FAIL is reserved for structural breakage and corruption; deliberate states are WARN with honest copy; the status is always word + icon + color (never color alone).

## 8. Correction contract (unchanged, restated for the label)

- Label corrections go through the existing documented paths: `reverse` (mirror reversal, label copied), `editEvent` (atomic reversal+replacement, context copied verbatim — the replacement keeps the original label), `restoreEvent` (re-record with original values). There is deliberately **no** label-only edit in Group 1; a label change is a full documented replacement.

## 9. Compatibility invariants (all tested)

1. Old records readable (absent label reads as null; surfaces show «غير مصنّف»).
2. Old imports accepted (22/30 and the whole prior chain) with null default; no invented labels.
3. Export/import round-trip preserves labels verbatim; over-limit labels fail cleanly with device data untouched.
4. One write path (page → application → domain → store); atomic commits; per-intent idempotency keys; no page writes to IndexedDB; no second store.
5. The transfer-pair defect fix (D-025) restores round-trip validity for any store containing transfers or transfer reversals.

## 10. Test-to-contract traceability

| Contract clause | Test |
|---|---|
| Label normalization + limit | `tests/domain/expense-category-label.test.ts` (normalization, post-collapse measurement, freeze) |
| Label money-neutrality | same file (twins: paid, payable, allocated, unallocated) + `projectFinancialService.category.test.ts` (service twins across modes; edit/restore/reversal carriage) |
| Migration + import | `localTransferService.schema31.test.ts` (legacy pair, round-trip, blank→null, over-limit rejection + untouched store, transfer-reversal round-trip) |
| Effect preview derivedness | `FinancialEventEditor.guided.test.tsx` (preview lines incl. wallet + negatives; fallback) + the shared-expansion module consumed by both paths |
| Allocation review | guided dom test (reconciled rows, «المتبقي غير موزّع») |
| Canonical result | `periodResultCanonical.test.ts` (deep-equal, spy, null-as-value, derived total) |
| Integrity read-only + severities | `integrityCheckService.test.ts` (clean PASS, corruptions → correct FAIL ids, drift stub, zero-writes, pending WARN, stale-settlement WARN) + `ToolsIntegrity.ui.test.tsx` (surface states + snapshot equality) |
| Quick-sheet chip optionality | `QuickActionSheet.category.test.tsx` (commit, deselect → null, honest negatives) |
