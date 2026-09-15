# Group 5 — Activity and Reporting (Unified Reader, Statement, Local Markdown)

Group 5 surface contracts for visibility: one canonical read model, one statement truth, one local report format. Files: `application/activity/activityService.ts`, `presentation/activityLabels.ts`, `pages/FinanceActivity.tsx`, `Home.tsx`, `application/finance/statementService.ts` (deep layers), `application/finance/statementMarkdownService.ts`, `Statement.tsx`.

## 1. The canonical activity model

`ActivityRecord` is a read-only projection over the existing stores — never a second truth engine. Each row carries: family (15 total — sales, direct sales, orders, deliveries, expenses, purchases, loan events, asset events, depreciation, deposit classification, collections, transfers, inventory receipts/consumption/waste, corrections), effect class (8, mirroring the domain `DELTA_TABLE`: cash in/out, payable, owner capital, opex, amanah, asset, loan, revenue), `amountMinor | null` (unknown cost stays `null` — never zero), qualifier text, status derived at read time (active / reversed / superseded / cancelled / pending), `reversalOfId` links, `occurredOn` + `recordedAt`, source deep link, and store/id provenance. Transfers group by `transferId` so a wallet move reads as one event, not two. Per-family caps (5 recent / 20 in the full reader) bound render cost; ordering is `recordedAt` descending.

The service joins the existing canonical lock: it never recomputes period results, and the unit tests pin it to the store lists. `activityLabels.ts` is the single Arabic label map (label + effect word + unit) so Home and Finance render identical wording for identical facts.

## 2. Home «آخر ما حدث»

The Home card composes each row as: Arabic label, item/customer qualifier, `DD/MM/YYYY` date, effect word (e.g. «نقدي داخل»), English-digit JOD amount with unit («40.00 د.أ»), and «افتح السجل الكاملة» into the reader. It replaced the older order/draft-only «ما تغير مؤخرًا» list, which missed sales, purchases, loans, assets, deposits, inventory, and corrections, used bare `/finance` links, and sliced UTC timestamps. Amounts and dates follow the product rules: English digits, two decimals, local Amman dates.

Verified live in the production build: the seeded direct sale renders «بيع مباشر · صيانة ماكينة خياطة · 05/09/2026 · نقدي داخل · 40.00 د.أ» with a working deep link; the section hides unknowns honestly rather than printing zero.

## 3. `/finance/activity` reader

The full reader offers: period ranges (this week / last week / this month / since the beginning / custom with the local-date picker), family filter chips (16 families), newest-first rows, per-row deep links to owning surfaces (order detail, sale detail, asset detail, wallet entry, focused event view on Finance), and the offline truth line «يعمل بلا إنترنت — يُقرأ من سجلك المحلي ولا يغيّر شيئًا». Deep links were verified live from both Home and the reader (e.g. the expense row → `/finance?event=<id>` focused view).

## 4. Statement deep-finance layers and unresolved values

`statementService` gained a deep block sourced only from the canonical reader: period depreciation, write-off loss, disposal result, retained-deposit revenue (non-cash result lines), asset book value and standing loans and pending retained deposits (independent layers, «الآن»), and six unresolved-value kinds (unknown direct-sale cost, pending expenses, pending retained deposits, unallocated inventory cost, general waste, shared-unallocated). The page renders the layer with a warning card: unresolved values display as-is and never collapse to zero. The result line itself reads «غير متاح» with the exact reason («هناك تكلفة غير معروفة تمنع رقمًا نهائيًا — لا يُعرض ربح متوهَّم») — verified live with a seeded unknown-cost sale.

Amanah and owner money keep their separation lines («الأمانات — ليست ربحك», «مال المالك لا يدخل النتيجة»), and the corrections block covers all cash-moving families with in-period reversal netting.

## 5. The local Markdown report

«خذ التقرير معك» renders `statementMarkdownService` output: an Arabic RTL Markdown snapshot with a BOM, `# كشف فترة — Micro` heading, generated-on date (`DD/MM/YYYY`), the snapshot disclaimer («نسخة قراءة لحظية من سجلك المحلي — ليست حدثًا ماليًا ولا تغيّر أي رقم»), cash net with the not-profit qualifier, cash-in/cash-out families, documented corrections, the result block with deep non-cash lines, independent layers, unresolved values, categorized expenses, the truth lines, and a generation-local footer («التقرير لا يُرسل شيئًا ولا يفتح شيئًا — مشاركته قرارك اليدوي وحده»).

Delivery follows the established local pattern: `Blob` + `text/markdown;charset=utf-8`, filename `micro-statement-<from>-<to>.md`, deferred `URL.revokeObjectURL` (30 s, WebKit-safe), plus `navigator.share` text and a clipboard fallback through `lib/textDelivery.ts`. Verified live end-to-end: the downloaded file contains the honest unknown-cost wording, the correction netting, the deep layers, the truth lines, and the footer; no secrets or unrelated records appear in the export.

## 6. Privacy and scope boundaries

The report is a read snapshot: generating it writes nothing to any store, creates no financial event, and sends nothing. Its content is limited to the period statement of the local device. The share handoff is manual and explicit (see the sharing report) — Micro never attaches the file anywhere by itself.
