# Agent 2 — Journey and Data-Parity Audit

| | |
|---|---|
| Report ID | micro-group-6-parallel-audit-001 / agent-2-zman-transfer-audit |
| Date | 2026-09-05 |
| Baselines | Zman `main` @ `bdd63ab` (read-only) · Micro `agent/group-6-zman-transfer-audit` @ `961051f` (on Agent 1 main `1242aa6`) |
| Inputs | SA-2 journey/data-parity audit (`agent-2-specialist-02-journey-data-parity-en.md`) + principal verification + fresh-data browser QA |
| Path abbreviations | `Z ` = `repos/zman-app/artifacts/zman-app/`, `M ` = `apps/prototype-web/client/`, `D ` = `src/domain/` in Micro |

---

## 1. Method

Each journey was reconstructed on both sides from code (entry → steps → service → storage → read surfaces → correction path), then compared step-by-step, field-by-field. Seventeen journeys from the continuation prompt §7 were audited; the sixteenth and seventeenth (period statement/manual sharing; categories) are included. Fresh-data browser execution evidence for journeys 1, 8 (asset), 11 (loan), 12 (activity), 13 (draft banner), 14 (backup/restore/tamper), and 16 (statement share) is recorded in `agent-2-zman-test-evidence-en.md` §4. Agent 1's fixes (FT-01/02/03, DP-01/09) were independently re-verified in the current tree because they alter transfer-relevant behavior.

## 2. Journey parity matrix (summary)

| # | Journey | Verdict | One-line reason |
|---|---|---|---|
| 1 | Quick expense → classification → nature → relation → shared allocation → save → period reading | **ADAPTED** | Micro asks truth-context questions (classification, 4 natures, shared amount/percentage/defer) that Zman never asks; value preserved with fewer mandatory fields (2) than Zman's minimal mode |
| 2 | Accrued expense → later settlement without double counting | **MISSING (Zman side) / MICRO-ONLY** | Zman cannot record an unpaid bill without distorting cash; Micro `operating_expense_payable` + `payable_settlement_cash` settle with zero expense delta and mandatory `relatedEventId` (`D/financial-event/policies.ts:276,339-341`) |
| 3 | Tracked material → purchase → explicit receiving → partial → remaining → correction | **ADAPTED** | Zman creates the movement at purchase (no receiving step); Micro requires explicit receipt via the `?purchase=` bridge with over-receipt/shortage guards (`M InventoryMovementEditor.tsx:44-62,157-181`, `inventoryMaterialService.ts:731-785`) |
| 4 | Untracked material without accidental movement | **MATCHED** | both whitelist tracked items; Micro adds explicit untrack/retrack decisions and rejects consume/extract/adjust on untracked (`inventoryMaterialService.ts:813-818,1059-1063,1102-1106`) |
| 5 | Product → cost calculator → snapshot → order creation | **ADAPTED** | Micro adds a standalone calculator, saved estimates with revisions, knowledge states, price floor, safety buffer; agreement requires a saved snapshot (`agreementService.ts:79-150`) |
| 6 | Order → preparation → delivery review → consumption → collection/credit → settlement | **PARTIAL/ADAPTED (model difference, intentional)** | Zman books uncollected remainders as cash-in at delivery (`Z finance/actions.ts:1582-1601`); Micro models receivable + explicit collection/settlement — stronger truth, different period shape; mapping decision filed (P1-2); collections cannot be back-dated (P2-7) |
| 7 | Direct sale ± inventory consumption | **ADAPTED** | FT-02 cancel mirror reversal verified; post-save consumption bridge exists; INV-4 order-linked netting unmapped (P2-4) |
| 8 | Deposit → collection → cancel/refund/retain → explicit classification | **ADAPTED** | Micro replaces Zman's immediate forfeit-as-revenue with explicit reversible retained-deposit classification (owner/revenue options) — strictly safer |
| 9 | Delivery reversal → re-delivery → period attribution + idempotency | **MATCHED** | FT-01 `lastEffectiveDeliveryEvent` (`deliveryAttribution.ts:20-33`) consumed by all four period readers; regression-locked (Jan 0 / Feb 5000 test) |
| 10 | Asset → capitalization → depreciation → disposal/correction | **ADAPTED** | event-based depreciation + disposal + writeoff (Micro-only additions); unrecorded-depreciation proposal visible but not netted (F-3, P2) |
| 11 | Outgoing loan → partial repayments → settlement → correction | **ADAPTED** | append-only repayments/reversals/corrections; settled loans stay visible; FT-03/MIC-11 restore-awareness verified |
| 12 | Activity event → source deep link → correction → updated reading | **MATCHED** | `?event=` focus + family-guard deep links to owner surfaces + append-only corrections; browser-verified |
| 13 | Draft → refresh/close/reopen → discard/final save, no financial event before save | **MATCHED** | `formDraftService` versioned + conflict-guarded + export-excluded; draft truth line «لم تُسجّل أي حركة مالية بعد» browser-verified |
| 14 | Backup → validation → restore → health check → continued use | **ADAPTED** | envelope v27 (sha256 + counts + migrations 12→35) with DP-01/DP-09 + this audit's AI-01 orphan rejection (browser-verified live); Zman has export-only partial JSON with no restore |
| 15 | Local lock and PWA update while a form is dirty | **ADAPTED** | local PIN lock (PBKDF2 + backoff, A1-hardened) replaces server session; dirty-safe PWA update via dirty registry is stronger than Zman's manual SW confirm |
| 16 | Period statement + manual sharing, no background transmission | **MATCHED** | Markdown+BOM parity confirmed; manual-only share with preview; browser download verified |
| 17 | Expense categories: lazy enrollment, seeds, vocabulary | **ADAPTED** | suggestions (6 recent + 8 seeds) + frozen label on event + statement grouping with «غير مصنّف» fallback; no catalog CRUD (P2-3) |

**Verdict counts:** MATCHED 5 · ADAPTED 11 · PARTIAL 1 (J6, intentional model difference with filed decision) · MISSING 1 (Zman side of J2 — Micro-only capability) · REGRESSED 0 · DUPLICATED 0 · CONTRADICTORY 0.

## 3. Agent 1 fix verification (transfer-relevant behavior)

All four financial fixes from PR #154 are present and effective at `1242aa6`/`961051f` and each has a genuine regression test (SA-5 read the test bodies):

- **FT-01** — `deliveryAttribution.ts:20-33`; consumed by `projectFinancialService.ts:549-554`, `g5Service`, `ownerEntitlementService`, `recurringWorkService`; test locks re-delivery period attribution.
- **FT-02** — `directSaleService.ts:168-271` idempotent mirror wallet reversal on cancel; 130-line test block.
- **FT-03 / MIC-11** — `EventsLayer.tsx:80-100` family guard; `integrityCheckService.ts:780-803` loan restore-awareness.
- **DP-01 / DP-09** — `localTransferService.ts:2554-2569` (malformed integrity rejected), `:2840-2852` (counts must match migrated data).

None of these tests mask transfer defects; they lock behavior this audit relies on.

## 4. Data parity — Zman drizzle tables → Micro record kinds

20 Zman tables mapped to Micro's 32 IndexedDB stores (full mapping table in SA-2 §"Data-Kind Mapping"). Meaning preserved for all financially-relevant kinds; dropped kinds are owner-rejected or Zman-side artifacts:

| Zman table | Micro record kind(s) | Meaning preserved |
|---|---|---|
| `expense`, `cash_movement`, `purchase` | `financialEvents` (typed events with delta columns) | **Y** — one movement per cash event kept; classification moved to context fields |
| `expense_category_catalog` | `categoryLabel` on events (no store) | **partial** — vocabulary frozen per event (P2-3) |
| `catalog_component`, `catalog_unit` | `materials` + `catalogItems` + `measurementUnits` + `directConversions` + `catalogTemplates` | **Y+** — dimensioned units and conversions exceed free-text |
| `catalog_movement` | `inventoryMovements` (+ `inventoryShortages`) | **Y** — value-based, non-negative, reasoned |
| `order`, `order_component`, `order_additional_cost` | `orders` (with domain order + cost snapshots + events) | **Y+** — 10 statuses, settlement, event log |
| `sale`, `order_deposit_transform` | `directSales` (+ revisions) and order deposit events | **Y** — conversion replaced by delivery+settlement (model difference J6) |
| `capital_asset`, `depreciation_*` | `assets` (+ `asset_*` events) | **Y+** — event-based, disposal/writeoff added |
| `receivable`, `receivable_payment` | `loans` (+ `loan_*` events) | **Y** — append-only corrections instead of soft deletes |
| `account`, `account_transfer` | `cashWallets` + `cashContinuityEntries` (paired) | **Y** — archival missing (P2-6) |
| `opening_balance` | wallet opening (known/unknown) + `ownerProfile` capital | **Y+** — honest unknown |
| `audit_log` | corrections layer (correction records + reasons) | **partial-Y** — corrections richer; ordinary creates not in one stream (documented trade) |
| `snippet`, `message_template` | — (none) | **N — by owner decision** (snippets) / documented rejection (templates) |
| Zman PWA/auth/ops artifacts | `AppLockGate`, PWA runtime, MIC suite | **Y** — re-expressed locally |

Versions verified: **storage schema 35** (`M/storage/local/types.ts:37`), **export envelope 27** (`types.ts:44`); import accepts the documented legacy chain (12→35) with per-pair migrations and this audit's orphan-family rejection at the end of `validateSnapshot`.

## 5. Field-level parity notes (money, quantities, semantics)

1. **Money scale differs 10×** — Zman fils (÷1000, `Z lib/money.ts:1-2`) vs Micro minor units (÷100, `D/shared/currency.ts:1-4`). Harmless today (no bridge), catastrophic if a future migration copies integers: 1250 fils would become 12.50 JOD. `MoneyMinor` is an unbranded `number`, so the compiler cannot catch it. Filed as **F-2 / P1 NEEDS_OWNER_DECISION** (conversion + rounding policy + branded type before any bridge).
2. **Quantities and cost basis** — Zman: integer quantities + weighted-average unit cost per movement. Micro: milli-quantities + value-only movements. Zman's per-movement cost basis cannot be migrated exactly into Micro's value model — another reason the migration bridge is an owner decision, not a silent import.
3. **Uncollected remainders** — Zman books remainder-as-cash-in at delivery (weakens truth); Micro models receivable. For the same business reality the two apps show different period cash. Any side-by-side reconciliation (e.g. during owner evaluation) needs an explicit mapping — filed as **P1-2 NEEDS_OWNER_DECISION**.
4. **Corrections** — Zman soft-deletes and re-inserts rows (history via audit log); Micro appends reversal/replacement records with reasons and net effects, preserving originals. Micro is stronger; no Zman pattern was ported.
5. **`categoryLabel` end-to-end trace** (verified clean): editor input (`FinancialEventEditor.tsx:819-837`) → domain freeze (`policies.ts:145-151`) → store → statement grouping with «غير مصنّف» fallback (`statementService.ts:503-534`) → suggestions derived from recent use (`expenseCategorySuggestions.ts:24-44`) → finance period layer. The classification travels everywhere it should and creates no financial effect by itself.
6. **Source links survive export/import** — `?event=` deep links reference event ids; the envelope carries events verbatim; DP-01 guards counts; AI-01 (this audit) now guards family contexts, so a restored file cannot contain links to nonexistent asset/loan records.

## 6. Journey-level gaps requiring owner attention (detail in findings file)

- **J6/P2-7 — collection back-dating:** Micro collections and their wallet allocations stamp the recording date (`fulfillmentService`, `projectFinancialService.ts:989` defaults `occurredOn` to today; the Collect sheet has no date field). A late-recorded collection lands in the wrong statement period; repair = same-day reversal + re-collect. Zman allowed date edits. Action: add an optional occurred-on date to the Collect sheet (safe, additive) — not implemented in this audit (touching period attribution without a contract note would be speculative).
- **J17/P2-3 — category vocabulary management:** no rename/merge; typo labels persist as new labels. Action options: (a) accept (labels are free tags), (b) future category correction feature via `commitFinancialEventReplacement` — needs owner nod.
- **J7/P2-4 — INV-4 mapping:** Zman's manual-sale-linked-to-order netting has no Micro counterpart; Micro's answer is the order collection path. Mapping ambiguity documented for any future Zman-user onboarding guide.
