# Agent 2 — Test and Evidence Matrix

| | |
|---|---|
| Report ID | micro-group-6-parallel-audit-001 / agent-2-zman-transfer-audit |
| Date | 2026-09-05 |
| Branch | `agent/group-6-zman-transfer-audit` @ `961051f` (parent: Agent 1 main `1242aa6`) |
| Environment | Node v24.19.0 · pnpm 9.15.9 · vitest 4.1.11 · Vite 7.3.6 (PWA v1.3.0) · production build served locally (http.server) with agent-browser (Chromium) at 360×800 and 390×844, RTL |

---

## 1. Clean baseline gates (before any change, at `1242aa6`)

| Gate | Command | Result |
|---|---|---|
| Root typecheck | `pnpm typecheck` | PASS (0 errors) |
| App typecheck | `pnpm prototype:check` | PASS |
| Lint | `pnpm lint` (`--max-warnings 37`) | PASS — 0 errors, 37 warnings (pre-existing baseline, unchanged) |
| Format | `pnpm format:check` | PASS — "All matched files use Prettier code style!" |
| Text density (§10 caps, all 52 routed pages) | `pnpm text-density` | PASS — "All surfaces within §10 caps." |
| Design guards + stylelint (§9) | `pnpm design-guards` | PASS — "no raw hex, all values on scale." |
| Domain tests | `pnpm test` | PASS — 23 files / 277 tests |
| Prototype tests | `pnpm prototype:test` | PASS — 123 files / 784 tests |
| Production build + PWA | `pnpm prototype:build` | PASS — precache 96 entries (2062 KiB), sw.js + workbox emitted |

## 2. Post-fix full regression (at `961051f`, after AI-01/AI-02 fixes + new tests)

| Gate | Result | Delta vs baseline |
|---|---|---|
| Root typecheck | PASS | — |
| App typecheck | PASS | — |
| Lint | PASS — 0 errors / 37 warnings | baseline preserved (no new warnings) |
| Format check | PASS | — |
| Text density | PASS | — |
| Design guards | PASS | — |
| Domain tests | PASS — 23 files / **277** tests | unchanged (fixes are app-layer) |
| Prototype tests | PASS — **124 files / 794 tests** | **+1 file, +10 tests** (see §3) |
| Production build + PWA | PASS — precache 96 entries | unchanged |

## 3. New regression tests added on this branch

| File | Tests | What they lock |
|---|---|---|
| `client/src/application/transfers/localTransferService.familyOrphan.test.ts` | 4 | hand-merged file with asset event but no asset record → rejected (`validation_error`, «ناقص أو لا يطابق»); loan orphan → rejected; intact hand-merged file → accepted with assets/loans counts (proves rejection is the orphan check, not envelope stripping); ghost `assetContext.assetId` injection → rejected |
| `client/src/application/finance/integrityCheckService.test.ts` (extended) | +3 (27 total) | MIC-10 FAIL with `حدث-أصل-بلا-سجل` offender for ghost asset context; MIC-11 FAIL with `حدث-قرض-بلا-سجل` for ghost loan context; paired records → MIC-10/11 PASS |
| `client/src/G4Assets.dom.test.tsx` (extended) | +1 (6 total) | guard-triggered save while a save is in flight → exactly one `create` call (UnsavedChangesGuard «احفظ واستمر» programmatic path — the genuine double-invoke bypass) |
| `client/src/G4Loans.dom.test.tsx` (extended) | +2 (5 total) | loan editor guard-path double-invoke → one `create`; repayment sheet triple-click → one `recordRepayment` (user-visible single-write contract) |

**Negative controls (fix-quality proof):** with the `saveInFlightRef` guard temporarily removed, the AssetEditor and LoanEditor guard-path tests FAIL (verified by running the suites against a guard-disabled build, then restoring). The repayment-sheet contract test passes through the disabled-attr layer and is documented as such in its comment — the ref layer itself is covered by the two guard-path tests that share the mechanism.

**Migration/old-export compatibility:** existing chain suites all green in the full run: `localTransferService.schema29/31/32/33/34.test.ts`, `.envelope27.test.ts` (tamper, malformed-integrity DP-09, wrong-counts DP-01, 26/34 legacy pair), `.test.ts`, `.directSaleRoundTrip.test.ts`, `IndexedDbLocalStore.*.test.ts`, `persistentStorage.test.ts`.

## 4. Browser QA evidence (production build, fresh data, no fixtures)

Both viewports RTL; zero page errors; zero console errors across the whole session (checked after each phase via `agent-browser errors` / `console`).

**360×800 — full fresh-data journey:**

| Step | Evidence (verbatim UI text / artifact) |
|---|---|
| Setup | «ما اسم مشروعك؟» → ورشة الخياطة; «وين تحط فلوسك؟» → الدرج; «شو وضع الدرج هلق؟» → بدأت من الصفر → /foundation; five-tab shell مشروعي الآن/العمل/سجّل/مالي/أدواتي |
| Owner investment 500 JOD | `/finance/new/owner_investment_cash`; effect copy «مال أُدخل للمشروع. ليس مبيعات ولا ربحًا.»; saved → Finance truth strip: «كاش المحافظ المعلن 0.00 · الكاش غير الموزع 500.00 · محافظ مسجلة 1» |
| FAB quick expense 25 JOD | sheet «سجّل مصروفًا الآن» (1 mandatory: amount; category chip بنزين); Home «آخر ما حدث» row «05/09/2026 مصروف مصروف مدفوع في لحظته نقدي خارج 25.00 د.أ»; Finance: unallocated 475.00, opex 25.00 |
| Deep guided expense 40 JOD + classification | collapsed layer «افتح التفاصيل» → category chips (8); nature 4 options incl. «مختلط»; purpose 6; relationship «مصروف مشترك مع البيت أو نشاط آخر»; share modes «مبلغ حصة معروف / نسبة من إجمالي معلوم / أؤجل تحديد الحصة»; effect copy «حصة مؤكدة تدخل نتيجة الفترة مرة واحدة، والباقي خارج المشروع لا يُحمّل عليه»; saved |
| Activity reader + deep link | `/finance/activity` rows with kind chips; row click → `/finance?event=e8dd1243-…&from=%2Ffinance%2Factivity`; focused event card with «عرض الأثر الكامل» → full context echo: «حصة المشروع من مصروف مشترك · معروف · حصة ثابتة معلنة · تصنيفك: كهرباء» + deltas (كاش -40.00، مصروف 40.00) + correction actions (تراجع موثق/عدّل بقيم جديدة/حذف موثق) |
| Asset + double-submit | `/assets/new`; «شراء للاستخدام الطويل»; 300 JOD, life 60, no start → honest «أصل واحد بعمر أو بداية مجهولة — يبقى بلا إهلاك حتى تُحدده بمراجعة موثقة»; **triple click on «احفظ الأصل» → exactly ONE asset** (navigated to its detail; list shows one row, دفتري 300.00) |
| Integrity | `/tools/integrity` → «افحص الآن» → «سليم — الأرقام متسقة»; «إصدار الفحص: قواعد المخطط 35 · التصدير 27»; checks: تطابق نتيجة الفترة، بنية الكاش والمحافظ، سلامة الأحداث والتوزيع (4 حدثًا ماليًا)، رصيد الأمانات، سلامة المخزون والمواد، صدق درجة المعرفة، سلامة الأصول والإهلاك، سلامة القروض والسداد — all سليم |
| Statement export | `/finance/statement` → «ولّد ونزّل التقرير» → `micro-statement-2026-08-30-2026-09-05.md` (3174 bytes): UTF-8 BOM; «الفترة: من 30/08/2026 إلى 05/09/2026»; honest lines («ليس ربحًا ولا نتيجة», «ليس إيرادًا», «أصل طويل الاستخدام — ليس مصروفًا»); «النتيجة المسجّلة: -65.00 د.أ»; cash sections 500.00 in / -65.00 / -300.00; «لا تصحيحات موثقة في هذه الفترة» |
| Backup export | Settings → «تصدير البيانات المحلية» → `micro-local-2026-09-05.json`: version 27 / schemaVersion 35 / sha256 digest (64 hex) / counts {events 4, assets 1, wallets 1…} / asset + family-context event paired |
| **Tamper rejection (AI-01 live)** | hand-merged copy (integrity+counts stripped, `data.assets=[]`) → import → **«الملف ناقص أو لا يطابق بنية Micro المطلوبة. بقيت بيانات هذا الجهاز دون تغيير.»**; live asset still present after rejection |

**390×844 — second-viewport pass:**

- Surfaces render with correct H1s: `/finance/new/operating_expense_cash` «تسجيل مصروف مدفوع» · `/tools/calculator` «حاسبة التكلفة والسعر» · `/tools/integrity` «فحص سلامة مالي» · `/finance/activity` «آخر ما حدث» · `/finance/statement` «كشف الفترة» · `/assets/new` «شراء للاستخدام الطويل» · `/loans/new` «أعطيت مالًا يُعاد».
- Loan 80 JOD «أحمد الجار» with **double click on «احفظ القرض» → exactly ONE loan**; loans list «قرض قائم واحد»، «قائم عند الناس 80.00 د.أ».
- Zero errors / zero console output.

## 5. Test classification of the session

| Check | Classification |
|---|---|
| All gates, both suites, build, PWA | **code/product PASS** |
| Browser journeys, deep links, console | **product PASS** |
| CI for the branch | see §6 |
| No `npm audit` / registry failures encountered this session (all installs and runs completed without `ERR_SOCKET_TIMEOUT`); no retries were needed, no gate was bypassed | **environment clean** |

## 6. CI status of the branch

The repository's CI workflow (`.github/workflows/ci.yml`) triggers on pull requests. Agent 1's §28 note (commit `3e3fa5e`, `c1ae93e`) documents that the write token available to automation lacks `workflow` scope, so the workflow file itself was intentionally left unchanged on branches; the same constraint applies to this branch — CI will run from the existing workflow when the PR is opened. All commands CI runs (typecheck, lint, format, density, guards, both test suites, build) were executed locally on this branch and pass, so the expected CI result is green; any registry-infrastructure failure (`ERR_SOCKET_TIMEOUT` on the npm audit endpoint) would be environmental, not product — the pattern documented in PRs #150–#152 and Agent 1's report §28.
