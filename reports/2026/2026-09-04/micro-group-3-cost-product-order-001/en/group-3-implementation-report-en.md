# Group 3 Implementation Report — Costing, Products, Orders, Delivery, Direct Sales, and Settlement (English)

## 1. Baseline and completion-state gate
- Micro baseline: `main @ 1207a5a` (Group 1 PR #149 + Group 2 PR #150 merged; domain 239/239, prototype 643/643 green; clean tree; no stashes/worktrees/uncommitted work). No prior new-program Group 3 work existed (remote branch `agent/group3-tools-products-orders` belongs to the previous program, merged pre-#142–#148).
- Zman read-only reference studied via SA-2 (journeys transferred; Zman's looser financial model explicitly NOT copied — see §5).
- State map recorded in worklog (Task ID G3-0): Group 1 COMPLETE_AND_VERIFIED, Group 2 COMPLETE_AND_VERIFIED, Group 3 MISSING → implemented in this delivery.

## 2. What was implemented
1. **Delivery review before commitment** — new full-screen page `/orders/:id/deliver` (`pages/DeliveryReview.tsx`, deep-flow route, hides bottom nav, unsaved-guard): money preview (agreed price, collected incl. deposit, remaining, snapshot cost with knowledge state and gaps), explicit final-price correction (mandatory reason; documented `price_revised` event), inventory consumption proposal per Group 2 contracts, optional collect-at-delivery with wallet destination, one explicit confirm.
2. **Atomic delivery transaction** — new store method `commitOrderDelivery` (IndexedDB single transaction over orders + inventory-movements + inventory-shortages + cash-continuity-entries + cash-wallets; in-transaction identity checks; self-healing reuse by deterministic operation keys). Mirrored in MemoryLocalStore.
3. **Delivery reversal** — domain policy `reverseDelivery` (append-only `delivery_reversed` event linked to the delivery event; recognized revenue/cost neutralized to honest unknown; collected cash untouched) + `commitOrderDeliveryReversal` (order + mirrored reversal movements atomically) + `resumeAfterReview` re-execution path (needs_review → confirmed → in_progress with attempt-aware keys) + OrderDetail "اعكس التسليم" consequential panel.
4. **Inventory↔order integration** — `materialId` identity on cost items (calculator → estimate → draft → frozen snapshot; values never live), expected-consumption preview with available/shortage/cost-knowledge honesty, per-row action (consume / consume-with-shortage / record-shortage / skip), untracked materials stay cost-only, free items never move.
5. **Product definitions** — catalog template components link to inventory materials (service validates material exists; tracked/untracked displayed honestly) + template extras (labor time/rate, packaging, delivery, waste, safety margin) as zero-effect planning references mirroring CostSnapshotInput 1:1.
6. **Direct-sale inventory linkage** — optional, explicit: done-receipt offer → `?sale=` deep link into the InventoryMovementEditor (third consume target; active sales only; `saleId` on the movement; service validates existence and active status).
7. **Collections from orders** — remaining/debt collection buttons route through the Collect sheet (`?source=order:<id>`) — wallet attribution, single documented collection; no unattributed quick-collect paths remain on OrderDetail.
8. **Calculator parity** — inventory suggestion chips via the shared guide `materialSuggestions.ts` (same behavior as CostEditor: last non-reversed receipt → known price; else name/unit only → estimated) + excluded-items honesty (named-but-unpriced items listed as excluded, "غير محدد بعد" not zero).
9. **Migration** — `localSchemaVersion` 32→33, export 24→25; previous pairs 24/32 and 23/31 accepted with null-honest normalization (`materialId ?? null`, `extras ?? null`, `saleId ?? null`); validators extended; old records/exports remain readable.

## 3. Fixes to real bugs found by the new tests
- `markReady`/`deliver` idempotency-key collision made re-execution after reversal a silent no-op → attempt-suffixed keys.
- Store reuse detection matched ANY historical delivery key so re-delivery writes were skipped → last-delivery-key comparison.
- Prettier miss on the complexity refactor caught by CI (fixed in `6016c8b`).
- npm audit endpoint outage (registry.npmjs.org HTTP 500 + socket timeouts) — transient infra, no vulnerability locally (`pnpm audit`: "No known vulnerabilities found"); retriggered per PR #150 precedent until green.

## 4. Verification summary
- Full gate chain green on `main`: typecheck ×2, ESLint 0 errors / exactly 37 baseline warnings, Prettier, text-density (caps ratcheted with documented justifications: Finance 183, OrderDetail 143, DirectSaleEditor 66, Catalog 91, CostCalculator 59, DeliveryReview 48 new), design-token guards + stylelint, domain tests **246/246** (21 files), prototype tests **660/660** (102 files), PWA production build (84 precache entries).
- SA-5 adversarial review: **no blockers** across 10 audit points (duplicate revenue, duplicate movements, hidden deduction, deposit/settlement double-count, history mutation, migration, domain regression, UI wiring, secrets, gates). All REQUIRED/RECOMMEND findings fixed before merge (debt-collection attribution, predicate alignment, duplicate-materialId aggregation/rejection, active-sale validation, store reused-flag honesty, density registration).
- Merged via **PR #151** (CI checks + Cloudflare Pages success) → `main @ 67d4e41`; local == remote; clean tree; tests re-run green on merged main.

## 5. Zman transfer decisions (adopt vs. do-not-copy)
- Adopted: preview-before-confirm with exact money copy; one smart action per status; deposit question gating; snapshot costing with immutable history; catalog picker with stock/cost badges; shortage awareness without blocking (as structured Group 2 rows); cancel decision branches; drafts/idempotency resilience.
- NOT copied (financial truth): auto-posting the full remaining balance as cash at delivery (Micro asks collected amount and books unpaid remainder as debt or open amount); revenue derived from cash movements; deposit-transform reclassification (Micro keeps event identity and neutralizes liability with typed events); person-loans instead of customer debt; default-account hardwiring; description-string accounting; forfeiture booked as a fake sale; zero-cost opening stock; warn-only negative stock.

## 6. Known documented limitations
- Agreement-time deposit collection enters unallocated cash without wallet split (attributable later from Cash Distribution — honest, discoverable state; descope note D6).
- Sale-linked consumption updates inventory positions truthfully but is not wired into period COGS this group (order-linked COGS via `derivePeriodCogs` unchanged).
- Legacy `FulfillmentService.deliver()` retained as an inventory-silent path for API/test compatibility; the primary product path is the delivery review.
- No browser screenshot evidence this run (dom tests + CI build provide behavioral verification; Group 2's browser-evidence process remains the template for a future pass).
