# Group 4 Contracts — Assets and Depreciation

Micro deep-finance extension, contract 29 (عقد ٢٩). Baseline `main @ 67d4e41` → final `main @ 05669a9`.

## 1. Event model

Three of the nine new `FinancialEventType` values carry the asset lifecycle; all require a mandatory `AssetEventContext { assetId, name, bookValueMinor? }` (absent context on asset events, or present context on non-asset events, is rejected at the domain boundary):

| Type | cash | payable | ownerCapital | operatingExpense | amanah | asset | loan | retainedRevenue |
|---|---|---|---|---|---|---|---|---|
| `asset_purchase_cash` | −A | 0 | 0 | 0 | 0 | +A | 0 | 0 |
| `asset_purchase_payable` | 0 | +A | 0 | 0 | 0 | +A | 0 | 0 |
| `asset_depreciation` | 0 | 0 | 0 | 0 | 0 | −A | 0 | 0 |
| `asset_disposal_cash` | +proceeds | 0 | 0 | 0 | 0 | −bookValue (frozen in context) | 0 | 0 |
| `asset_writeoff` | 0 | 0 | 0 | 0 | 0 | −A | 0 | 0 |

Invariants: acquisition creates the cash/payable and asset effect exactly once (deterministic idempotency keys `${assetId}:create` / attempt-suffixed on correction); depreciation creates no cash movement and never enters operating expense (its result effect is the independent period term `assetDepreciation`); disposal carries two announced amounts (cash proceeds and the frozen book value); write-off is a non-cash book loss. No asset event ever sets `operatingExpenseDeltaMinor` — an asset is never duplicated as an operating expense.

## 2. Asset record and storage

`AssetRecord` (new store, schema 34): identity, category label, acquisition amount/kind, purchase date, `lifeMonths: number | null`, `depreciationStartOn: string | null`, status (`active`/`disposed`/`written_off`), `acquisitionEventId`, disposal/write-off references, contract revisions, operation key. Book value is a derived read (never stored). Six atomic commit transactions exist in both IndexedDB and Memory with exact parity: acquisition correction, depreciation, depreciation reversal, disposal, write-off, contract revision. Legacy 25/33 files import with `assets: []` — no history invented.

## 3. Depreciation contract (straight-line, last-month sweep)

- Monthly charge = floor(acquisition / lifeMonths); the final month absorbs the remainder so the total exactly equals the acquisition over the life.
- Full months elapsed from `depreciationStartOn`; day-aware. A start date later than purchase delays the first charge honestly.
- Proposal = scheduled accumulated − already recorded; re-recording the same `asOf` is a no-op (idempotent); recording cannot jump to a future date.
- Unknown life (`lifeMonths: null`) or unknown start (`depreciationStartOn: null`) keeps readiness `unknown_life` / `unknown_start` — no depreciation until a documented contract revision fixes it. The unknown is displayed as unknown, never as zero.
- Contract revision (life/start) is a documented correction: previously recorded depreciation is untouched; future proposals follow the new contract.

## 4. Corrections

- **Acquisition correction** (`correctAcquisition`): reverse + replace atomically (reversal of the original event, replacement on the original purchase date, record re-pointed to the replacement); requires a reason; rejects a no-change request ("لا تغيير عن المسجّل"). Surfaced from AssetDetail (active assets) with a preview.
- **Depreciation reversal**: documented reversal event; the original stays in history and is visually marked ("عُكِس لاحقًا"); reason required inline.
- **Disposal / write-off**: retirement with announced proceeds (cash in, difference to frozen book value shown as result gain/loss) or pure write-off (non-cash loss of book value); both set terminal status and stop depreciation.

## 5. Canonical reading

`readRecordedPeriodResult` adds `assetDepreciation` and `assetWriteOffLoss` and `assetDisposalResult` as independent period-result terms with reversal-aware active filtering (reversed originals excluded, reversals included). `readPosition` adds the `assetMinor` layer (sum of active asset deltas). The cash statement (after fix 1) shows the two cash-moving families with explicit qualifiers; the FinancialEventEditor excludes the linked-context types from the generic editor (they are only created through their services).

## 6. UX journey (Arabic, 360–390px, RTL)

Editor question flow per contract: «هذا الشيء للاستخدام لفترة طويلة؟» → «نعم، عمره طويل» / «لا، يُستهلك فورًا» (the latter blocks saving and guides to the expense path); «متى بدأ استخدامه؟» optional start date; «كم عمره المتوقع؟» life months (empty = honest unknown). Effect preview before save: «يخرج X د.أ من الكاش» / «يُفتح التزام…» and «لا يُسجَّل مصروفًا هذا الشهر». Detail page: book value today, accumulated depreciation, proposed charge with owner-chosen as-of date («سجّل حتى تاريخ»), contract revision, disposal/write-off with announced economics, full event history with reversal actions and marks. English digits, JOD two decimals, DD/MM/YYYY throughout; offline truth line on every surface.

## 7. Test evidence

Domain: asset policy tests (234-line suite) — acquisition deltas, floor + sweep, delayed start, unknown life, disposal two-amount, write-off, revision immutability of recorded history. App: assetService tests (10) including acquisition correction atomicity + no-change guard. Dom: G4Assets (5) — editor journey with preview, unknown-life rejection, list honesty, depreciation confirm + no-double-record, acquisition correction surface. IDB: `IndexedDbLocalStore.group4.test` (5) — transaction atomicity/parity. Integrity: MIC-10 fixtures.
