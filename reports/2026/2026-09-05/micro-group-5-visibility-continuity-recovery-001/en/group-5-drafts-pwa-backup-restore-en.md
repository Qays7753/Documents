# Group 5 — Drafts, Lock, PWA Updates, Backup/Restore (Continuity and Resilience)

Files: `application/drafts/formDraftService.ts`, `components/forms/useFormDraft.ts`, `components/forms/FormDraftRestoreBanner.tsx`, `components/forms/useFormDirty.ts`, `components/forms/UnsavedChangesGuard.tsx`, `application/security/localLockService.ts`, `components/security/AppLockGate.tsx`, `components/security/LockSettingsCard.tsx`, `pwa/dirtyRegistry.ts`, `pwa/register.ts`, `pwa/PwaRuntimeNotice.tsx`, `application/transfers/localTransferService.ts` (v27), `lib/syncSha256.ts`, `lib/textDelivery.ts`, the four editors, `Settings.tsx`, `storage/local/*` (schema 35).

## 1. Form drafts — the full lifecycle, verified

`form-drafts` is a new contains-guarded IndexedDB store (keyPath `id`, indexes on `updatedAt`/`formKind`), excluded from every backup snapshot by design: transient input never leaves the device and never enters the financial record. The service exposes `save` (idempotent per form id), `read`, `clear`, and `list`; the hook `useFormDraft` wires it into the editors with a dirty gate.

The lifecycle, verified live in the production build for DirectSaleEditor (full cycle) and live-write verified for AssetEditor, LoanEditor, and SupplierPurchaseEditor:

1. **First keystroke saves** — the original implementation gated the effect on `phase === "drafting"`, but the phase only became "drafting" inside the write handler the gate prevented, so the first write never happened. The inverted gate (`phase === "restore-offer"` suppresses writes only during the explicit restore offer) fixed it; commit `5613ec2` also repaired the test mocks to the service contract. Live: typing «صيانة ماكينة خياطة» + amounts created `direct_sale:new` with 11 field keys; the AssetEditor draft carried 9 keys, the LoanEditor 5, the SupplierPurchaseEditor 8.
2. **Clean forms write nothing** — dirty-gated; opening an editor and leaving creates no draft.
3. **Reload offers restore explicitly** — the form re-mounts clean and a banner offers «استرجع المسودة / تجاهلها»; clean values are never silently overwritten.
4. **Restore returns all fields** — live: description, quantity, price, collected, and date all returned.
5. **Final save clears the draft** — live: after «حفظ البيع المباشر» the store read zero drafts and the sale record existed (`revenueMinor 4000, status active`).
6. **Discard removes the draft** — live: «تجاهلها» left zero drafts.
7. **Drafts create zero financial events** — the financial store gains records only at explicit save (verified by direct IndexedDB inspection between steps).
8. **The saved line is honest** — «مسودتك محفوظة محليًا — آخر حفظ 05/09/2026؛ لم يُسجّل البيع بعد» (Amman-converted DD/MM/YYYY — a review-synthesis fix).

Scope note: the FAB quick-entry sale sheet is intentionally not draft-enabled — it is a momentary entry, not a workspace; the four full-page editors are the draft surfaces. `InventoryMovementEditor` does not use the hook (the prompt's mention of it was verified against the actual scope: the previous session's fix note said "all four editors").

## 2. Local lock

`localLockService` stores a salted SHA-256 PIN hash via WebCrypto (the PIN itself is never stored and never leaves the device), a failed-attempt counter with human retry delays, idle tracking via `lastActiveAt`, and a disable path requiring the current PIN. `LockSettingsCard` offers auto-lock after 1/5/10/30 minutes or manual-only, with the honest promise always visible: «يحمي من النظرة العابرة على هذا الجهاز فقط، وليس تشفيرًا للبيانات ولا حسابًا سحابيًا. الرمز نفسه لا يُخزَّن ولا يخرج من الجهاز أبدًا».

`AppLockGate` wraps the app: `visibilitychange` marks activity on hide and re-evaluates on show (works for both app-switch and screen-lock — no separate timers), a 30-second heartbeat keeps continuous use unlocked, and public recovery routes are exempt. When locked, the veil renders with `inert` content and a **stable wrapper tree** (a review-synthesis fix: the page does not unmount, so React state survives). Live verification: 1-minute idle → veil engaged with the honest no-recovery copy («لا يوجد استرداد بلا الرمز... ولا يوجد بديل سحابي») and the draft banner visible beneath; wrong PIN → «الرمز غير صحيح — أعد المحاولة»; correct PIN → unlock with the form values intact («أبو خالد» / «150.00» preserved through the whole cycle).

## 3. Dirty-aware PWA updates

`dirtyRegistry` is a module-level count bridging React (`UnsavedChangesGuard` syncs it — the prior session found and fixed a dead wire where the guard never called `setDirtyForms`, leaving the registry at zero) and the service-worker layer (`register.ts`). `onNeedReload` no longer auto-reloads over dirty forms (the S2-11 fix), and `PwaRuntimeNotice`'s «حدّث الآن» explains instead of destroying: «عندك مدخلات غير محفوظة — احفظها أولًا ثم حدّث؛ التحديث لن يبدأ فوق عملك المفتوح».

Live verification with a real service worker: a genuine new SW revision produced a waiting worker, the update card appeared («تحديث Micro جاهز»), and clicking «حدّث الآن» with a dirty sale form showed the block message with the field value intact and no reload. Offline verification: with the SW controlling, network emulation off, a reload served the full app from the 96-entry precache and SPA navigation continued offline («مالي» rendered from cache).

## 4. Backup envelope v27 — integrity, tamper rejection, atomic restore

The export envelope (schema 35 / export version 27) adds `integrity: {algorithm: "sha256", digest}` computed over the canonical JSON of `data`, an embedded `counts` object, and `appVersion`. The digest uses `lib/syncSha256.ts` — a pure-JS FIPS 180-4 SHA-256 so verification works without SubtleCrypto availability constraints.

`prepareImport` verifies the digest **before** any preview: a tampered payload is rejected with «تُغيّر الملف بعد إنشائه فبصمة التكامل لا تطابقه؛ لا تعتمد عليه. بقيت بيانات هذا الجهاز دون تغيير». The prior session found and fixed a real bug where `createVerifiedExport()`'s round-trip through `prepareImport` stripped the v27 optional fields (so the app's own files could never be tamper-checked); the fix carries the fields through and recomputes digest/counts, and a strengthened envelope test pins it.

- Live export: `micro-local-2026-09-05.json` (version 27, format `micro-prototype-local-export`, digest verified in-page and in Node, counts match the store, secret scan clean).
- Live tamper rejection: payload-tampered file (revenue altered, digest not recomputed) rejected before preview — and, after the F-1 fix, **visibly** (see §5).
- Live valid import: preview with true counts («الملف صادر في 05/09/2026 08:18... 1 طلب · 1 بيع مباشر · 3 حدث مالي/تشغيلي...») and the replace warning; confirming ran the atomic restore followed by the post-restore health check verdict card («فحص السلامة بعد الاستعادة...») with a deep link to the integrity page.
- Legacy: the Group 4 v26/34 pair stays accepted; migration paths unchanged.
- Storage parity: `form-drafts` and `local-security` are excluded from snapshots — drafts and lock secrets never leave the device.

## 5. F-1 — storage feedback visibility (fixed this session)

Fresh QA found that every storage notice — export success, tamper rejection, import preview — rendered inside the collapsed «بيانات البداية والاستعادة» details while the import trigger lives in the visible «استيراد محلي» row: a user uploading a tampered file saw nothing change. Fix (commit `4445da0`): `setStorageNotice` opens the layer (the existing scroll effect reveals the notice), and `chooseImport` opens it on preview. Verified live: rejection and preview both appear immediately after upload.
