# Group 2 Test Evidence — Gates, Scenarios, CI, Browser QA, and Adversarial Review Resolutions

**Delivery:** micro-group-2-catalog-inventory-recovery-001 · **Date:** 2026-09-04
**Verified state:** Micro `main` @ `1207a5adc460829322c9e33013e492d3cdb816bd` (PR #150 merged; tree `622716ae`)

Every result below was **re-executed during this recovery session** on the merged state; nothing is quoted from the interrupted session's logs. Commands run from the repository root unless noted.

---

## 1. Gate matrix

| Gate | Command | Result |
|---|---|---|
| Typecheck (domain/root) | `pnpm typecheck` | clean (exit 0) |
| Typecheck (client) | `pnpm prototype:check` (`tsc --noEmit`) | clean (exit 0) |
| Lint | `pnpm lint` (`--max-warnings 37`) | 0 errors / 37 warnings — baseline ceiling, zero new |
| Format | `pnpm format:check` | all files pass Prettier |
| Text density | `pnpm text-density` | all surfaces within §10 caps |
| Design guards | `pnpm design-guards` | no raw hex; all values on scale; stylelint clean |
| Domain tests | `pnpm test` | **239/239 passed (20 files)** |
| Prototype tests | `pnpm prototype:test` | **643/643 passed (98 files)** |
| Production build | `pnpm prototype:build` | Vite build + PWA `generateSW`: 82 precache entries (1828.25 KiB) |
| Full chain | `pnpm check` | **exit 0** (typecheck → lint → format → density → guards → tests → client check → client tests → build) |

Density rows for Group 2 surfaces (exact caps, honest counts): Finance 182/182, CostEditor 58/58, InventoryMaterials 56/56, MaterialEditor 39/39, InventoryMovementEditor 54/54, SupplierPurchaseEditor 62/62, ToolsIntegrity 34/34.

Test-count growth versus the Group 1 baseline (231 domain / 607 prototype): +8 domain tests across 7 new Group 2 suites; +36 prototype tests across the service scenarios, schema-32 round trips, dom surfaces, and MIC-8 checks. During recovery, the prototype suite went from 639 tests with 3 failures (the interrupted session's defective SA-5 dom tests) to 643/643.

## 2. Key test files and what they prove

| File | Proves |
|---|---|
| `tests/domain/inventory-material.test.ts` (+7 suites) | tracking/opening validators; value-zero ⟺ unknown; consumption order-or-reason; position cost knowledge; shortage constructor/resolution; untracked guards |
| `apps/.../application/inventory/inventoryMaterialService.test.ts` (22 tests) | purchase cash separation; over-consumption rejection; partial-receipt caps and quota release after reversal; activation idempotency; unknown-cost openings and marked-zero consumption; Scenarios A–K incl. atomic consume-with-shortage, repeat-safety (reused), extractRemainder incl. the SA-5 F2 untracked rejection; tracked-only references |
| `apps/.../application/suppliers/supplierPurchaseService.test.ts` | material link + expected quantity recorded; edit revision before-fields; R7 total-below-received rejection; SA-5 F3 link-change/clear rejection while receipts stand |
| `apps/.../application/transfers/localTransferService.schema32.test.ts` | schema 24/32 round trips for tracked/untracked, activation, receipts (full/partial), waste, corrections, unknown states, shortages; legacy 23/31 import |
| `apps/.../group2InventorySurfaces.test.tsx` (16 tests) | MaterialEditor guided journey (all branches); InventoryMaterials sections/states/untrack dialog/shortage disclosure; movement-editor bridge prefill (F1: quantity `6`, money `60.00`) and shortage panel; purchase-detail bridge card + CTA + safe return (F6); fully-received state (F6b); Scenario G through the real CostEditor (chips fill the estimate row, zero movements/events); Finance period waste row (known 2.50 non-cash; unknown «قيمة الهدر غير معروفة بعد», never 0.00) |
| `apps/.../application/finance/integrityCheckService.test.ts` (MIC-8) | structural FAILs (fold negative, value-zero without unknown, double reversal, duplicate keys); WARN for open shortage and explicit unconfirmed; absent-opening legacy = known (no false positives) |
| `group1Surfaces.test.tsx` + guided-entry suites | Group 1 regression — green throughout |

## 3. Scenario matrix (program prompt §9)

| # | Scenario | Automated evidence | Browser evidence |
|---|---|---|---|
| A | Untracked material, cost input, no inventory | Scenario A service test; Scenario G dom (no movement/event) | — |
| B | Tracked activation, known opening | «Scenarios B & C» service; MaterialEditor dom (saves 20 → 20000 milli, knowledge states) | screenshots 02–04 |
| C | Unknown opening ≠ zero | service «unconfirmed, never zero»; dom «غير محدد بعد» + preview honesty | — |
| D | Purchase without receipt: inventory unchanged | «Scenario D & E & F» service (purchase writes no movement); bridge dom (form open ⇒ 0 movements) | screenshot 05 |
| E | Full receipt via source action: one linked movement | service receipt tests; F6b dom (fully received state) | screenshots 06–07 |
| F | Partial receipt: remaining + safe second | caps tests (reversed excluded); F1 dom (remaining 6 / 60.00 prefill); repeat idempotency | screenshot 07 (12.00/20.00 · 30/50) |
| G | Untracked/estimate item without movement | Scenario G dom through real CostEditor | — |
| H | Deliberate tracked consumption | Scenario H service (reason + idempotency; orderId-null path) | — |
| I | Consumption above known quantity | Scenario I service (reject → atomic partial+shortage → resolve; repeat reused); dom shortage panel («استهلك المتاح» → position 0 + openShortageCount 1) | — |
| J | Waste non-cash, no duplicate expense | Scenario J service (0 events; period summary; unknown-cost flag); Finance dom ×2 | screenshots 09–10 (`2.00 — غير نقدي`) |
| K | Untrack with consequences | Scenario K service (history preserved; retrack unconfirmed); dom (4 consequences, safe cancel, row moves) | — |
| L | Correction preserves original | reversal tests (mirror + cost-knowledge inheritance + quota release) | — |
| M | Repeat submission / reload | reused-idempotency assertions across consume/receive/waste/extract/shortage-pair | — |
| N | Old exports + new round trips | schema-31 legacy import; schema-32 round-trip suite | — |

Additional prompt-level requirements verified by tests: old records readable (legacy pair), unknown defaults null (migration tests), atomicity (three-store commit tests), estimates never commit (Scenario G), MIC-8 policy-defined WARN (never unexplained PASS), and Group 1 green in every run.

## 4. CI runs on PR #150

| Run | Trigger | Outcome | Notes |
|---|---|---|---|
| 1 | push `e40da57` | `checks` **failure** at **Audit dependencies** | npm registry security-audit endpoint returned HTTP 500 then ERR_SOCKET_TIMEOUT (all retries) — infrastructure failure, **no vulnerability** (local `pnpm audit`: "No known vulnerabilities found"); Lint and Verify steps were skipped, never executed |
| 2 | push `2e8dcab` (empty retrigger) | `checks` **success**; `Cloudflare Pages` **success** | full chain green on the runner: install → audit → lint → `pnpm check` |

The re-run could not be requested via the API (token lacks `actions:write`), so the retrigger was a transparent empty commit whose message states the reason (`2e8dcab`). The audit failure involved zero code defects; this is recorded as a CI flake, not a code finding.

## 5. Adversarial review (SA-5) — findings and resolutions

SA-5 reviewed the complete 45-file working-tree diff (+4296/−411 at that time) file-by-file, ran the gates read-only, and returned **FIX REQUIRED**: 1 MAJOR + 6 MINOR + notes. Resolutions, all verified by tests in the merged state:

| Finding | Severity | Resolution |
|---|---|---|
| Bridge deep-link quantity/value prefill never fires (early ref assignment blocks the status-card prefill; inverse: no-deep-link numerically prefills the first purchase) | MAJOR | Pre-fill logic restructured to the receipt-status effect (once per purchase, never over owner edits); verified by the F1 dom test (quantity 6, money 60.00) **and** live browser (quantity 50, value 20.00 prefilled from the CTA deep link) |
| `extractRemainder` missing untracked guard | MINOR | Guard added («المادة غير متتبَّعة…»); SA-5 F2 service test added in recovery |
| `editPurchase` allows material-link change with active receipts (unit-mixing risk) | MINOR | Link change/clear rejected while receipts stand (SA-5 F3); tested |
| R7 edit guard + revision before-fields untested | MINOR | Service tests exist and pass (before-fields; total-below-received rejection) |
| Raw ISO `resolvedOn` rendered | MINOR | `LocalDateValue` on all shortage dates (verified in InventoryMaterials) |
| Promised S13 dom tests missing (bridge card / MaterialSheet Scenario G / Finance waste row) | MINOR | All three delivered in recovery (16-test dom file), incl. the fully-received state and both waste-row branches |
| «صفر مؤكد» keyed to live fold instead of declared opening | MINOR | Keyed to `material.opening.quantityState === "confirmed" && quantityMilli === 0` |
| Notes (repeat-safety of consume-with-shortage; import-rejection gaps; unknown-id deep-link fallback; MIC-8 shortage.orderId; template-literal money in previews; confirmMaterialOpening asymmetry) | notes | Repeat-safety now tested; the rest documented in the contracts report §9 / limitations — none blocks shipping |

## 6. Browser QA (live, 390×844 RTL, dev build)

Session log: setup (project name, default wallet, known opening 500.00) → inventory activation → empty states → guided material creation («خيط حرير», meter, 30 m, 12.00 JOD, source «جرد الرف العلوي») → purchase («مورد الخيط», linked material, expected 50, total 20.00, paid 0) → purchase detail bridge card → CTA → deep-linked receipt editor prefilled (50 / 20.00 / material / note) → partial receipt saved (30 / 12.00) → safe return to purchase detail → inventory position (60 m) → waste (5 m, reason «خيط تلف من الرطوبة») → Finance period view waste row («هدر مخزون هذه الفترة | 2.00 — غير نقدي: لا يخرج كاش ولا يدخل نتيجة الفترة.» — weighted average 24.00/60 m × 5 m = 2.00) → integrity run (MIC-8 «سلامة المخزون والمواد» سليم: «المراجع موصولة، والطيّ غير سالب، ولا نقص مفتوح»).

**Zero console errors, zero page errors** (`agent-browser errors` / console scan clean). Twelve screenshots delivered in `supporting/`. The five-seat bottom nav and centered FAB are intact in every frame; no horizontal overflow or RTL defects observed; all visible numbers English digits, dates `DD/MM/YYYY`, JOD two decimals.

## 7. Security checks

- Token scan of the merged diff and the delivery package: **no credentials, no `.env`, no secrets** (scan performed on the full `761638b..1207a5a` diff and on every file in this folder).
- Tokens were held in a path-scoped credential store outside the repositories; remote URLs stayed clean; no token appears in any command output, log, commit message, or report.
- Zman was read-only throughout (`bdd63ab`, never modified or pushed).

## 8. Known limitations

1. Template-literal money inside effect-preview sentences (bidi-correct digits, but not `MoneyValue` bdi nodes) — cards/status surfaces all use `MoneyValue`; documented, non-blocking.
2. Unknown-id deep links fall back to first purchase with the prefill-once guard — documented behavior.
3. CI flake record (npm audit endpoint outage on run 1) — resolved by retrigger; no code change.
4. Order-to-sale deduction (Group 3), richer estimate surfaces, and any delivery automation remain future groups by scope; contracts are in place so they extend rather than rewrite.
