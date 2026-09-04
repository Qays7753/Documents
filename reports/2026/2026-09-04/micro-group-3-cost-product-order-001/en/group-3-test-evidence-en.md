# Group 3 — Test Evidence (English)

## Suites and results (merged main @ 67d4e41)
- Domain (root `pnpm test`, vitest): **246/246 passed — 21 files** (239 baseline + 7 new in `tests/domain/craft-order-g3.test.ts`).
- Prototype (`pnpm prototype:test`): **660/660 passed — 102 files** (643 baseline + 17 new).
- Typecheck (root + prototype), ESLint (0 errors / exactly 37 baseline warnings), Prettier, text-density (all surfaces within caps), design-token guards + stylelint: all green.
- PWA production build: generateSW, 84 precache entries (~1.87 MB).
- CI on PR #151: checks = success, Cloudflare Pages = success (after one real prettier fix and two retrigger commits for a registry.npmjs.org audit-endpoint outage — local audit clean: "No known vulnerabilities found").

## New test files and what they prove
1. `application/fulfillment/deliveryReviewService.test.ts` (11 cases):
   - buildReview previews money + proposes consumption only for tracked linked materials; untracked stays cost-only; free items visible without movements; shortage row visible with warning.
   - Review refuses non-ready orders (and guides already-delivered ones).
   - commitDelivery delivers atomically: one revenue recognition, order-linked movement with known cost, delivery_consumed event, untracked/free no movement.
   - Idempotent retry: reused result, one movement, revenue unchanged.
   - consume_with_shortage: partial movement + structured shortage row (no negative stock).
   - Untracked consumption refused.
   - Collect-at-delivery: settled/paid with revenue 6,000 (not 7,000) — deposit never counted as extra revenue.
   - Final-price correction requires a reason; applied as documented revision (from/to preserved).
   - reverseDelivery: revenue neutralized, movement mirrored, cash untouched, order needs_review.
   - Double reversal refused; honest re-delivery after resumeAfterReview + markReady: 2 consumptions, 1 reversal, revenue recognized again (net one live delivery).
2. `pages/DeliveryReview` dom tests (`G3Delivery.dom.test.tsx`, 3 cases): full review render (money + proposed consumption), confirm flow (delivery + 1 movement + zero financial events), OrderDetail ready-order routes to the review (no one-click "تم التسليم" button), calculator suggestion chips fill rows with zero inventory/financial effect.
3. `storage/local/IndexedDbLocalStore.delivery.test.ts` (2 cases): commitOrderDelivery writes order+movements+shortages+cash atomically and refuses duplicates on retry (reused=true, no second writes); commitOrderDeliveryReversal writes the reversed order + mirrored movements and refuses duplicates.
4. `tests/domain/craft-order-g3.test.ts` (7 cases): reverseDelivery semantics (neutralization, history preservation, idempotency, guards), review-lock unlock exactly for reversed deliveries (re-execution and cancellation allowed after reversal; non-reversed delivered orders stay locked), noteDeliveryConsumption link + idempotency + reason validation, frozen snapshot under external mutation + price revision renewing revenue only, catalog template materialId + extras validation (negative rejection).
5. `application/transfers/localTransferService.schema33.test.ts` (1 case): 25/33 export round-trip preserves cost-item materialId verbatim; legacy 24/32 file (Group-3 fields stripped) imports with null normalization; older 23/31 still accepted (no backward break).
6. Updated `localTransferService.schema31/32.test.ts` to the live version pair (25/33) — same verified behaviors.

## Scenario coverage mapping (prompt §10)
1 Calculator free (dom) · 2 product from tracked+untracked components (service + domain) · 3 order snapshot stability (domain) · 4 draft no effect (domain/transitions + calculator dom zero-effect) · 5 confirmation/preparation state actions (service path) · 6 deposit not double profit (collect-at-delivery test) · 7 direct sale one effect (existing suite, regression green) · 8 delivery preview incl. debt/cash/receivable/inventory (service + dom) · 9 confirm→retry→reload no duplicates (service + IDB) · 10 tracked movement only via explicit path (service+dom) · 11 untracked no movement (service) · 12 shortage visible (service) · 13 final price delta + stability (service) · 14 cancellation pre/post deposit (existing suite) + post-delivery via reversal (domain+service) · 15 retained deposit pending (existing suite, regression) · 16 settle remaining no second sale (existing suite, regression) · 17 corrections preserve originals (existing + new reversal tests) · 18 import/export old+new (schema33 test) · 19 repeated taps/offline/draft restore (idempotency keys + unsaved guard; service reused results) · 20 RTL 360–390 (design guards + token-based layout; existing viewport QA applies) · 21 Group 1+2 suites green (239→246, 643→660 — zero regressions).
