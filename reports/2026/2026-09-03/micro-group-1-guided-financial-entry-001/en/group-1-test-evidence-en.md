# Group 1 Test Evidence — Commands, Results, Migration Checks, Browser/Device Checks, Known Limitations

| | |
|---|---|
| **Report ID** | micro-group-1-guided-financial-entry-001 (test evidence) |
| **Date** | 2026-09-03 |
| **Code under test** | Micro `agent/group1-transfer-guided-financial-entry` @ `bc2e4c5`, merged as PR #149 → `main` @ `761638b` (baseline `4db6a5f`) |
| **Environment** | Node v24.19.0, pnpm 9.15.9 (matching CI's Node 22 semantics), Linux sandbox; CI: GitHub Actions (ubuntu-latest, pnpm 9.15.9, Node 22) |

## 1. Baseline (before any change, at `4db6a5f`)

| Command | Result |
|---|---|
| `pnpm install --frozen-lockfile --ignore-scripts` | OK |
| `pnpm typecheck` | PASS |
| `pnpm lint` | 0 errors / 37 warnings (repo ceiling `--max-warnings 37`) |
| `pnpm test` | 226 tests / 19 files PASS |
| `pnpm prototype:test` | 571 tests / 88 files PASS |
| `pnpm prototype:check` + `pnpm prototype:build` | PASS (PWA, 80 precache entries) |
| `python3 scripts/text-density-count.py` | All surfaces within caps |

## 2. Final gates (after implementation, on the branch / merged commit)

| Command | Result |
|---|---|
| `pnpm check` (typecheck + lint + format:check + text-density + design-guards + test + prototype:check + prototype:test + prototype:build) | **PASS end-to-end** |
| `pnpm typecheck` | PASS (root + prototype workspaces) |
| `pnpm lint` | 0 errors / **37 warnings** (identical to baseline; zero new warnings — one warning pair introduced by a first draft of a new test file was eliminated by restructuring before commit) |
| `pnpm test` (domain) | **231 tests / 20 files** PASS (+5 vs baseline: `tests/domain/expense-category-label.test.ts`) |
| `pnpm prototype:test` | **607 tests / 96 files** PASS (+36 vs baseline across 8 new files) |
| `python3 scripts/text-density-count.py` | All surfaces within caps — new registrations: ToolsIntegrity 32/32, FinancialEventEditor 138/138, Statement 89/89; Tools 28/34; Finance 181/181 |
| `pnpm design-guards` (token guard + stylelint) | PASS |
| `pnpm prototype:build` | PASS — PWA generateSW, 80 precache entries (1734 KiB) |
| `pnpm format:check` | PASS |
| GitHub Actions CI (commit `bc2e4c5`) | **`CI: completed success`** (install → audit high → lint → `pnpm check`) |
| PR #149 | Merged (`merge_method=merge`) → `main` @ `761638b`; `git fetch --prune` + local pull verified local == remote; working tree clean |

## 3. New test inventory (41 tests)

| File | Tests | What they lock |
|---|---|---|
| `tests/domain/expense-category-label.test.ts` | 5 | Label normalization (trim/collapse/blank→null; post-collapse 80-char measurement; no silent truncation), twins across paid/payable/allocated/unallocated (all five deltas identical with/without label), freeze + reversal carriage |
| `apps/.../application/finance/projectFinancialService.category.test.ts` | 3 | Service twins: label survives percentage/estimate/defer/fixed expansions with identical deltas and share math; `editEvent`/`restoreEvent`/reversal carry the label verbatim |
| `apps/.../application/transfers/localTransferService.schema31.test.ts` | 5 | Verified round-trip preserves the label (23/31 stamped); legacy 22/30 accepted with null default; import normalization (trim/collapse/blank→null); >80 label rejected with device data untouched; **transfer + documented reversal round-trips through a verified export (D-025 regression)** |
| `apps/.../application/finance/periodResultCanonical.test.ts` | 4 | Canonical lock: full-object deep-equality reader vs statement vs insights; invocation spy (both consumers call the canonical reader); null-as-value cross-surface equality with reasons; derived `recognizedRevenueTotalMinor` consistency |
| `apps/.../application/finance/integrityCheckService.test.ts` | 7 | Clean store → all PASS + **zero writes (snapshot JSON equality before/after)**; tampered deltas → MIC-4 FAIL with offender id; tampered share bps → FAIL; raw negative-amanah write → MIC-7 FAIL; injected statement drift → MIC-1 FAIL carrying both numbers; pending states (deferred share, owner-draw overdraft) → WARN not FAIL; **stale settlement reference after a documented payable edit → WARN** (SA-5 regression) |
| `apps/.../pages/FinancialEventEditor.guided.test.tsx` | 8 | Wallet question renders with sheet-identical vocabulary; derived chip selection commits the label through save; shared percentage review card (reconciled rows incl. «المتبقي غير موزّع 0.00»); effect preview lines (wallet-named primary + combined negatives); attribution-failure honesty before navigation (operation key, wallet id, delta, sourceRef; no false navigate; safe-return button); guidance notes; draft persistence (restore/discard/save-clears; never auto-commits) |
| `apps/.../components/layout/QuickActionSheet.category.test.tsx` | 3 | Chip commit carries `categoryLabel`; deselect saves null (optionality); effect line includes the honest negatives clause |
| `apps/.../ToolsIntegrity.ui.test.tsx` | 2 | Idle promise + run → verdict and five check cards with status words; **store snapshot identical after a UI run**; corrupted fixture → verdict خلل + deep link + offender disclosure |
| `apps/.../group1Surfaces.test.tsx` | 4 | Finance doorway navigates with `?from`; EventsLayer shows «تصنيفك: بنزين» and the legacy honest «مصروف قديم غير مصنف»; statement categories grouping (per-tag totals, payable kind, loss excluded, derived total) |

Extended (not new) files: `QuickActionSheet.guard.test.tsx` and `FinancialEventEditor.ui.test.tsx` mocks extended for the new read-only service calls (`listEvents`, wallet overview); both files' original assertions unchanged and passing.

## 4. Migration & compatibility evidence

- **Schema/export bump:** `localSchemaVersion` 30→31 and `localExportVersion` 22→23 in the single guarded location; exports stamped 23/31 (asserted).
- **Legacy import:** a simulated 22/30 file (label deleted from the current export shape) is accepted, migrated, and re-stamped at current constants with `categoryLabel` reading `null` (asserted).
- **Round-trip:** `createVerifiedExport` on a labeled store → `prepareImport` → `confirmImport` on a fresh store → the event's label is verbatim `بنزين` (asserted).
- **Negative import:** a hand-edited 125-char label fails `prepareImport` (invalid snapshot) with the pre-import device store untouched (investment event still present — asserted).
- **Import normalization:** raw labels `  بنزين     وقود   ` → `بنزين وقود`; whitespace-only → `null` (asserted).
- **IndexedDB upgrade path:** no new object stores; the existing contains-guard upgrade path runs as a no-op (precedent: the amanah field's schema-28 bump); the full IndexedDB test suite (fake-indexeddb) remains green.

## 5. Live browser / device checks (production build, 390×844, headless Chromium)

| Check | Result |
|---|---|
| App boots from production preview; PWA manifest + SW registered | PASS |
| First-use journey (project name → wallet → zero start → foundation) | PASS |
| Five-seat bottom nav + centered FAB unchanged | PASS |
| Scenario A (quick fuel 25.00, wallet, بنزين chip, effect, receipt, record label) | PASS — effect line exact, receipt exact, row shows «تصنيفك: بنزين» |
| Scenario B (editor 300.00, wallet, رواتب+ثابت, preview, save) | PASS — attribution-failure honesty fired for a real zero-balance wallet and the page stayed mounted with the record link |
| Scenario C (shared 100 / 60%) | PASS — review card rows and preview show the derived 60.00 share |
| Scenario E (payable preview) | PASS |
| Integrity run (empty-ish store with one expense) | PASS — «سليم — الأرقام متسقة», date 03/09/2026, five checks |
| Finance doorway + statement grouping expansion | PASS — رواتب 300.00 / بنزين 25.00 with sources |
| Console errors / page errors across the whole session | **0 / 0** |
| Screenshots | `group1-integrity-live.png`, `group1-payable-effect-live.png` (delivery supporting folder) |

## 6. Adversarial review (SA-5) findings and dispositions

| # | Severity | Finding | Disposition |
|---|---|---|---|
| 1 | Major | MIC-4 false-FAIL on the documented «settle → edit/delete payable» flow (stale reference) | **Fixed pre-merge**: demoted to WARN with honest copy + offender links; missing/non-payable reference remains FAIL; regression test added (passes) |
| 2 | Minor | MIC-4 reversal comparison omitted `expenseContext` | **Fixed**: context now compared (JSON of `?? null`) |
| 3 | Minor | Post-save dirty guard could block back navigation after a saved record | **Fixed**: reset token flips after successful save (`savedEpoch`); guard disarms |
| 4 | Minor | Import/MIC-2 accepted hand-crafted reversal-of-reversal pairs | **Fixed**: both validators require a non-reversal original (mirrors the live write path) |
| 5 | Note | Unreachable message-text divergence for an invalid non-operating combo | Documented; no action (same outcome: validation_error, zero writes) |
| 6 | Note | Preview min-height 96px could grow ~16px in the worst case | **Fixed**: raised to 116px |
| 7 | Note | WARN copy didn't distinguish unknown-opening wallets | **Fixed**: per-wallet note distinguishes «رصيد افتتاحي غير معلن بعد» |
| 8 | Note | MIC-9 pending count scanned the whole store | **Fixed**: windowed to the checked month |
| 9 | Note | Draft shape validation is minimal (display-only risk) | Backlog (documented) |
| 10 | Note | One QA test file lives at `src/` root (lint pattern) | Accepted (matches the U001 precedent); documented |

Post-fix full gate re-run: `pnpm check` PASS (231 + 607 tests, lint 0e/37w, all caps) — this is the state that was committed and merged.

## 7. Scenario matrix (A–J) — result

All ten acceptance scenarios pass; the mapping of each scenario to its live-QA and/or test evidence is tabulated in the implementation report §7. Scenario H (unknown openings) is covered by unchanged existing behavior plus the integrity page's explicit empty-state wording; Scenario I by per-mount idempotency keys, the `${key}:attribute` attribution key, and the draft tests; Scenario J by the canonical lock tests and the live MIC-1 «سليم» verdict.

## 8. Known limitations

- Real-device QA (Android/iOS hardware, IME, haptics) and production Cloudflare Pages acceptance remain Pilot-gated (standing repository boundary, unchanged by this group).
- The five live browser journeys cover the happy paths and one real failure path (attribution); deeper destructive-path UI (reversal previews, corrections) is covered by the existing suites, not re-walked live in this group.
- LibreOffice was used only for the Arabic report render check, not for the product.
- Text-density counter blind spot over the Finance truth section is documented (D-026) rather than fixed (its fix materially changes the measured set and warrants an owner decision).
