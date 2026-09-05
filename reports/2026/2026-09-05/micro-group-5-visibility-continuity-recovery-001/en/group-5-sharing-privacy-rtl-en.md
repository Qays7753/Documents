# Group 5 — Sharing, Privacy, and Arabic RTL UX

Files: `application/share/shareMessageService.ts` (+ tests), `pages/SharePreview.tsx`, `pages/OrderDetail.tsx` (entry), `lib/textDelivery.ts`, `presentation/g5Plurals.ts`, `index.css` (RTL/runtime-notice layer), density ratchets in `scripts/text-density-count.py`.

## 1. Manual sharing — explicit, minimal, privacy-safe

`shareMessageService` builds customer-safe drafts for five contexts: an order summary, a collection (payment received) note, a delivery confirmation, a payment reminder, and a statement summary. The content rule is minimal-by-construction: the customer sees their item, the agreed price, what they paid, and what remains — **never cost, never margin, never internal financial detail**. Live verification of the reminder draft for a seeded order: «أتذكر لك 25.00 د.أ من طلب «تنجيد أريكة قماش مقاوم». خبرني متى تناسبك التسوية، وأسعد بتحضيرها.» — receivable and item name only. Jordanian phone numbers normalize (Arabic-Indic digits and forms map to E.164-style handoff numbers) when a contact number is present in the source record.

`SharePreview` is the single deliberate gate before anything leaves the device:

- A deep preview textarea the owner can freely edit — the exact bytes that will leave are the bytes on screen.
- Explicit actions: «أرسل النص» (device handoff via `navigator.share` where available) and «انسخ النص» (clipboard write, falling back to the manual selection path when the clipboard is unavailable — «انسخه يدويًا: ظلّل النص أعلاه وانسخه من لوحة المفاتيح», a review-synthesis behavior verified live).
- The privacy promise is on the surface: «Micro لا يرسل شيئًا تلقائيًا ولا يقرأ جهات اتصالك» and «التسليم النهائي قرارك اليدوي».
- Offline truth: «توليده ونسخه محليان تمامًا».

No automatic sending exists anywhere in the flow; there is no contacts access; and the persistent notes/snippets library remains **not implemented** by permanent exclusion — there is no storage of share texts beyond the transient screen.

## 2. RTL, mobile, and the visual floor

The five-seat shell is untouched: «مشروعي الآن | العمل | سجّل (FAB) | مالي | أدواتي» — no sixth seat, no second bottom bar, no competing FAB. All Group 5 surfaces reuse the design system (tokens, safe-area insets, sheet patterns), and the runtime-notice cards (update/offline) join the same layer.

- **Digits and dates**: every visible number is English digits with two decimals; every visible date is numeric `DD/MM/YYYY`. The prior session's plural fixes moved nine sites to a dedicated `g5Plurals.ts` (split from the shared file to avoid cross-surface inflation) with the Arabic 3–10 singular rule («بعد 30 دقيقة» — thirty enters the plural gate) applied; a review-synthesis pass fixed the 11–99 singular («بعد 30 دقيقة») and Home amounts gained the «د.أ» unit.
- **Density**: the ratchet caps for all touched surfaces are documented in `text-density-count.py` (Home 41, Finance 260, OrderDetail 163, Statement 202, ToolsIntegrity 52, Settings 39, Assets 63, Loans 70, LoanDetail 73, LoanEditor 31, AssetEditor 49, SupplierPurchaseEditor 71, DirectSaleEditor 75; FinanceActivity 55 and SharePreview 24 registered day-one). All surfaces measured within caps in the final gate run.
- **Design tokens**: four undefined `--color-line` references were repaired to `--color-border` (stylelint-guarded).
- **Verification**: the fresh production QA pass covered both required viewports (390×844 and 360×800) across the new surfaces — activity reader, statement + report card, integrity page, settings (lock + backup), share preview, editors — with zero console/page errors, zero horizontal overflow at 360px, no keyboard collision with the FAB or bottom nav, no bidi defects (mixed Arabic/English-digit strings render in the correct order under RTL), no Arabic-Indic digits in visible strings, and correct `DD/MM/YYYY` everywhere dates appear.

## 3. Accessibility notes

Interactive rows and sheets carry Arabic `aria-label`s; the lock veil and runtime notices announce themselves (`role=status` / `aria-live`); the update card's block message uses `role=alert`; form errors use the field-error role; focus follows the sheet open/close pattern of the existing design system. The corrections register's `details/summary` structure keeps keyboard operability native.

## 4. Honest boundaries

- The FAB quick-entry sheet intentionally bypasses drafts (momentary entry, not a workspace).
- Clipboard write can be blocked by browser/OS policy; the manual fallback is the designed honest path (verified live in the restricted automation context).
- `navigator.share` availability depends on the device/browser; where absent, the copy path is the fallback. No silent failure — the surface always states what it did.
