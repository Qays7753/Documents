# Group 5 — Health Checks and Audit Integrity (MIC-14/15/16, Audit Trail)

Files: `application/finance/integrityCheckService.ts` (+ tests), `application/finance/correctionHistoryService.ts` (+ tests), `components/finance/CorrectionsLayer.tsx`, `components/order/OrderEventLog.tsx`, `pages/ToolsIntegrity.tsx`.

## 1. MIC-14 — unallocated cash truth

Reads the canonical position's unallocated cash and the wallet-decision review state. Negative unallocated cash → **WARN** with the honest explanation («أنفقت أو خصّصت أكثر من مصادر الكاش المسجلة؛ راجع مصدر الفرق قبل الاعتماد على أي رصيد محفظة») and the drift amount; a needs-review deposit state also surfaces. It never repairs, never zeroes, and never hides the sign. Verified live: the seeded data (asset purchase exceeding unallocated sources) produced the WARN with drift 362.50 د.أ and a deep link to the wallet sources.

Note (documented, intentional): the WARN prose rounds the drift to whole dinars (`Math.round`) while the drift line shows the exact value — 363 in prose, 362.50 in the figure.

## 2. MIC-15 — idempotency-key uniqueness

Scans the live store for duplicated `idempotencyKey` values across financial events (the transfer-pair exception is respected). Duplicates would mean double financial effect. Verified live: «كل حدث مفتاحه فريد — لا أثر مالي مكرر في سجلك الحي».

## 3. MIC-16 — owner-money separation

Asserts the domain delta table's separation: owner investment and withdrawal events must carry owner-capital deltas only — never expense, never revenue, never amanah. Verified live: «مال المالك مفصول: الاستثمار والسحب والعربون-المالك لا يدخلون نتيجة الفترة ولا مصاريفها أبدًا».

## 4. Shared health-report contract

The three new checks join the existing 13 with the same shape: `{id, titleAr, status, detailAr, driftMinor?, offenderCount?, offenderSampleIds?, deepLink}`, overall `FAIL > WARN > PASS`, a read-only promise («يقرأ أرقامك ولا يغيّر شيئًا»), injectable clock, and no automatic repair — the deep link routes to the documented correction path. The report carries version stamps «قواعد المخطط 35 · التصدير 27» and a run timestamp, and the healthy verdict adds the honesty line «الاتساق لا يعني الربحية» — consistency is not profitability. The Tools page now advertises sixteen checks.

## 5. MIC-4 and MIC-10 hardening (this session)

The prior session fixed MIC-4's false-positive: re-derivation via domain factories now passes the required asset/loan/deposit contexts, compares expense context JSON, and asset/loan/revenue deltas; healthy Group 4 events pass honestly while malformed context still fails. Re-verified live this session («سلامة الأحداث والتوزيع: سليم — 2 حدثًا ماليًا طابق كلٌّ منها أثره المالي»).

**F-2b (fixed this session):** MIC-10's acquisition check previously read only the asset record's `acquisitionEventId` link, so a legitimate restore (the product's own reverse-then-restore cycle) left the asset flagged «اقتناء-معكوس» forever. The check now resolves the *effective* acquisition: the active original, or an active restore event (deterministic `restore:` idempotency key, matching type and asset context). The full cycle was verified live: reverse → honest FAIL («سلامة الأصول مكسورة») → restore → back to WARN (unknown asset life only). A regression test pins the cycle.

## 6. Audit trail — readable append-only history

`correctionHistoryService.list` aggregates 12+ correction kinds into a readable register: kind, date (`DD/MM/YYYY` — the prior session fixed five raw-ISO label sites), amount effect (`null` when not reducible to a number — never fake zero), reason, original-link relationship, and a deep link per entry. Group 5 added: delivery reversal, deposit classification, inventory reversal, owner reversal, and asset contract revision; and repaired the Group 4 reverse+replace pairing (the `-reversal:`/`-replacement:` key transform) so asset/loan corrections and deposit reclassifications pair correctly with their originals.

The register renders in the Finance «السجل» layer with a restatement note («تصحيح موثق واحد يؤثر في الرقم الظاهر. صافي الأثر −350.00 د.أ. الأصل محفوظ كما هو؛ التصحيح سِجِل جديد...») and per-entry original links («الأصل: شراء أصل نقدًا · 05/09/2026 · 350.00 د.أ»). OrderDetail's event log gained the delivery-consumed / delivery-reversed / deposit-classified labels.

Verified live: a documented reversal with reason «خطأ في الإدخال — تسجيل تجريبي للتدقيق» appears in the register with its reason, net effect, original link, and working «افتح السجل المصدر» deep link; the double-reversal guard and the restore path were exercised end-to-end (see the drafts/backup report).

## 7. Integrity of the integrity layer

All checks remain read-only: the unit test asserts the store snapshot is byte-identical before and after a run. Warnings are honest by design — an unknown asset life, a negative unallocated balance, or a pending deposit are states to review, not corruption to hide. The only FAIL introduced by Group 5 surfaces was the F-2b false-positive, which is now fixed and regression-tested.
