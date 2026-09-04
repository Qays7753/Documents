# Group 3 — UX and Flow Review (English)

## Surfaces (per prompt §6)
- **Full-screen** (deep flow, bottom nav hidden, unsaved-changes guard, safe return): `/orders/:id/deliver` delivery review — goal, entry point (ready-order button "راجع التسليم وسجّله"), return path (order detail with ?from preserved), primary action ("أكّد التسليم"), first-viewport content (money grid + next-step), progressive details (advanced options behind one disclosure: price correction + collection).
- **Dialog-level consequential decision**: delivery reversal uses the shared CorrectionPreview pattern (original/preview/net effect/unchanged/reason mandatory/danger styling) inside the OrderDetail corrections disclosure.
- **Sheets**: MaterialSheet (cost items) and the Collect sheet (collections) unchanged in role; the sale done-receipt offers the optional consumption deep link.

## Guided Arabic questions answered in-surface
- «شو رح يتغير في المخزون؟» — the consumption preview section header, with per-row available/shortage honesty.
- «شو رح يتغير بعد التسليم؟» — the money grid + confirm summary (revenue once, collection is not revenue, deposit already counted).
- «هل هذا تقدير أم بيع فعلي؟» — calculator/estimates remain explicitly estimate-only ("هذا حساب تقديري…"), delivery confirms the actual sale.
- «استلمت عربون؟ كم بقي على العميل؟» — deposit/collected/remaining in the review grid and OrderDetail summary.

## States defined for changed screens
- DeliveryReview: loading, error (not ready/already delivered with honest guidance), ready (review), validation (price reason, collection over remaining, duplicate material), submitting (busy labels), success receipt (revenue/movements/shortages/collection facts + non-blocking notices), offline-safety (unsaved guard; local-first store).
- OrderDetail: ready→review entry, delivered/settled reversal offer (only while the last delivery is un-reversed), post-reversal resume action, debt/remaining collection routed to the sheet, corrections disclosure unchanged in structure.
- Calculator: suggestions with confidence labels, excluded-items honesty, zero-effect guarantee.
- Catalog: material-linked component picker (tracked/untracked labels), extras disclosure with null-honest time/rate.
- DirectSaleEditor: done-receipt optional consumption offer (explicitly optional — "البيع صحيح بدونه").

## RTL/mobile/formatting compliance
- Arabic RTL layout with English digits only, JOD two decimals, DD/MM/YYYY dates (existing LocalDateValue/MoneyValue/EnglishNumberInput/EnglishQuantityInput components reused throughout). No horizontal overflow (structural CSS on design tokens; stylelint token guards green). Bottom navigation untouched — five seats + FAB intact (route classifier: the review page is a deep flow like its sibling editors). Text-density caps ratcheted with documented justifications (48 for the new page, measured from day one).

## Honest-copy principles kept
- No number without meaning: knowledge labels on cost, "غير معروفة" for unknown position cost, "غير محدد بعد" for unpriced items, shortage quantities stated.
- Consequence previews before every financial commitment (CorrectionPreview pattern).
- Non-blocking failure notices (schedule reconcile, future attribution) — never silent, never destructive.
