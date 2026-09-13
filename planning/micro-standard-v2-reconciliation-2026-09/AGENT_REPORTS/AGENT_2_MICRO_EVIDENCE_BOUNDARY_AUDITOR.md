# AGENT-2 Report — Micro Evidence and Transfer Boundary Auditor

**Task ID:** AGENT-2
**Agent:** Agent 2 — Micro Evidence and Transfer Boundary Auditor
**Run:** Micro Standard v2 Reconciliation, 2026-09 (planning run)
**Mode:** READ-ONLY analysis. No repository file in Documents, Micro, wt-context, or wt-comparison was modified, created, or deleted. The only writes produced by this agent are this report and the worklog append.
**Micro evidence SHA:** `c0469e265f24c70427eb7826dee717be117cff87` (main, read-only clone at `/home/z/my-project/recon-work/Micro`) — verified working tree matches the pinned SHA per run preflight.
**Standard baseline SHA:** Documents/main `864263c190f5d3da6041acfafb0720e85ac6e320`, package `micro-standard-v2/` (31 files on disk; MANIFEST `file_count: 29`).

---

## 1. Files read (mandatory reading, completed)

**Context pack** (`/home/z/my-project/recon-work/wt-context/planning/micro-standard-v2-reconciliation-context-2026-09/`):

1. `OWNER_UNIFIED_DECISION_REGISTER.md` — complete (U-01…U-20; governing document).
2. `REPORTS_RECONCILIATION.md` — complete.
3. `REFERENCE_ZAI_FLASH_REPORT.md` — complete (all 19 sections + Annex A; primary baseline). Key sections used: §7 GAP matrix (GAP-01…GAP-47), §12 Micro-specific, §13 missing/where-it-lives, §14 must-be-preserved, §16 D-01…D-12.
4. `REFERENCE_ZAI_5_3_REPORT.md` — complete (cross-check; §12–§14, §16 D1–D13, §17 W0–W6).
5. `EXECUTION_PROMPT_CONTEXT.md` — complete.
6. `README.md` (context pack) — complete.
7. Worklog: `/home/z/my-project/worklog.md` — read first.

**Micro evidence spot-checks (read-only clone, paths under `apps/prototype-web/client/src/` unless noted):**

- `presentation/formatters.ts` (148 L, complete read)
- `components/presentation/DisplayValue.tsx` (86 L, complete)
- `components/forms/UnsavedChangesGuard.tsx` (301 L, complete)
- `components/forms/EnglishNumberInput.tsx` (111 L, complete)
- `components/layout/MicroAppShell.tsx` (122 L, complete)
- `components/layout/AppHeader.tsx` (61 L, complete)
- `components/layout/BottomNav.tsx` (71 L, complete)
- `app/routeClassifier.ts` (76 L, complete; 29 deep-flow regexes counted)
- `app/navigation.ts` (48 L, complete)
- `pages/Home.tsx` L30–99 (fact triad)
- `pages/InventoryMaterials.tsx` L348–392 (knowledge states)
- `components/finance/G5DecisionPanel.tsx` L1–45 (G5 status words)
- `components/layout/QuickActionSheet.tsx` (targeted: modes, alertdialog, idempotency, receipt)
- `pages/ToolsIntegrity.tsx` (targeted: PASS/WARN/FAIL, drift, offenders)
- `pages/Schedule.tsx` (targeted: capacity/recurrence imports and options)
- `index.css` L33–147 (tokens + `.dark`), L284–313 (route-kind clearance + 260ms page transition), L755–789 (keyboard hide + nav/safe areas)
- Counting greps: `role="status"` (110/60 files), `role="alert"`, `د.أ` (279/58 `.tsx`; 319/76 all src), `--space-` in index.css (631), `formatMoneyWithUnit` (17 files), and vocabulary greps (§4 below).
- Correction-lifecycle markers: `EventsLayer.tsx` L730, `CashWallets.tsx` L274, `InventoryMaterials.tsx` L679.

**Standard contract files read (baseline at `/home/z/my-project/recon-work/Documents/micro-standard-v2/`):**

`component-states.md`, `component-contracts.md`, `navigation-shell.md`, `typography.md`, `iconography.md`, `empty-loading-error-states.md`, `overlay-system.md`, `motion-interaction.md`, `README.md`, `MANIFEST.json` (10 files; plus package file listing — 31 files on disk confirmed).

**Additional (run workspace, read-only):** run `micro-standard-v2-UPDATED/component-states.md` checked — currently identical to baseline (knowledge-state addition not yet drafted there; this report's §4–§5 recommendations feed that draft).

---

## 2. Transfer-boundary classification

Classification key: **RC** = Reusable Contract (generalizes into the Standard without product meaning) · **MP** = Micro Feature Pattern (stays in Micro; Standard may at most reference as consumers) · **PD** = Product/Owner Decision (defer; not this run) · **PA** = Preserve-As-IS (Micro strength to protect; no Standard change needed).

| # | Micro capability (evidence) | Class | Standard disposition / register row |
|---|---|---|---|
| 1 | Honest voids: «غير مسجل — سجّله» / «غير متاح» / measured zero (Home.tsx L43–46, L72–84; G5DecisionPanel.tsx L16–19; InventoryMaterials.tsx L383–386 «صفر مؤكد») | **PA** | Standard already codifies the 3-void contract (`component-contracts.md` L28). Void→data-condition wiring stays product-owned (5.3 §12). Additions do not touch void semantics. |
| 2 | Fact-state triad known / not_initialized / incomplete (Home.tsx L43–89) | **MP** | U-20: fact triad is Micro-owned. Standard must not absorb; may name it a valid consumer of value-zone/void contracts. |
| 3 | Knowledge states: unconfirmed quantity, unknown cost, needs-review (InventoryMaterials.tsx L354–379; G5DecisionPanel.tsx L22–31) | **RC** (presentation grammar only) | U-11 + U-05: a general word/marker/tone presentation contract for unconfirmed/unknown/incomplete/needs-review/estimated enters `component-states.md`/`component-contracts.md` with **no Micro words and no state-determination logic** (Micro's `quantityKnowledge`/`costKnowledge` enums stay Micro). |
| 4 | Correction lifecycle (EventsLayer.tsx L730 «الأثر بعد التراجع عن التصحيح»; «سجل لا يحذف بصمت» CashWallets L274, InventoryMaterials L679) | **MP** | U-20; Flash §12.2, GAP-34. No posting/reversal meaning in Standard. |
| 5 | Decision cards (Finance decision cards; DecisionPanel; G5DecisionPanel 346 L) | **MP** | U-20: decision cards stay Micro; Standard may add a generic composition slot note only. |
| 6 | Next-action rows (order rows + priority DecisionPanel, Orders.tsx) | **MP** (row *slots* are already Standard) | U-20: next-action state machine is Micro logic; the operational-row slot/stripe contract (addition 2) is the reusable shell around it. |
| 7 | Integrity-check PASS/WARN/FAIL (ToolsIntegrity.tsx L28–30, L172–178) | **MP** | U-20; GAP-38 (preserve; optional one-line Standard pointer only). |
| 8 | Scheduling capacity/recurrence (Schedule.tsx L25–26, L58–59, L84–91) | **MP** | U-20; GAP-39 "not in Standard by design" — product-owned time semantics. |
| 9 | Party ledger (WalletLedger/Parties) | **MP** | U-20: party ledger is a Micro pattern; `component-contracts.md` L38 already names "party" as a domain composition above primitives — sufficient. |
| 10 | Inline no-toast feedback (110 `role="status"` / 60 files — exact match; 53 `role="alert"`; receipt/outcome cards, QuickActionSheet.tsx L719) | **RC** (variant) + regime stays Micro | U-07: Standard gains the quiet/inline variant as a legitimate Snackbar alternative (addition 5); Snackbar stays optional. Micro's specific regime is the reference consumer, not the contract text. |
| 11 | QuickActionSheet sale/expense forms (QuickActionSheet.tsx: `SheetMode = "menu" \| "sale-form" \| "expense-form" \| "receipt"`, idempotencyKey L283/L353, `role="alertdialog"` discard L435) | **MP** | U-09/W4: AUX chrome vs feature forms split is a Micro-side wave; Standard must not encode sale/expense behavior. |
| 12 | UnsavedChangesGuard / drafts / restore stack (UnsavedChangesGuard.tsx 301 L; useFormDraft; FormDraftRestoreBanner) | **MP** | U-20/GAP-40: forms-protection stack is Micro-owned; Standard may at most gain a pointer that forms protection is a valid consumer of overlay/quiet-feedback contracts. |
| 13 | Keyboard chrome hiding + safe areas + context-label suppression + scroll border (MicroAppShell.tsx L26–33, L62–69, L91; AppHeader.tsx L16–22; index.css L288–298, L774–778) | **RC** | U-10 (+U-09 note): AUX behavior addendum (addition 3) documents these as visual/interaction contracts — no route lists, no labels. |
| 14 | Route-kind chrome gating (routeClassifier.ts: setup/deep/surface; `showsGlobalChrome`; 29 regexes verified) | **RC** (behavior principle) / route list stays Micro | U-10: reader=surface / editor=deep principle generalizes; Micro's route families and the D-10 per-family depth decision stay Micro-side. |
| 15 | 260ms route transition (index.css L304 `animation: micro-enter 260ms var(--motion-out)` on `.micro-page`) | **RC** | U-10: motion table gains a route-transition row (Flash GAP-32/§13; `motion-interaction.md` currently has no route row — verified). |
| 16 | Bidi/digits discipline (formatters.ts L4–22; DisplayValue.tsx `bdi dir="ltr"` L17/29/40; EnglishNumberInput.tsx L58–62, L78 `normalizeAsciiDigits`) | **PA** | §14.7/5.3 §14: already above the Standard's minimum; `typography.md` L23 requires the same. No change; protect. |
| 17 | formatters.ts money/date authority (formatMoneyMinor L50; formatMoneyWithUnit L57 «… د.أ»; DD/MM/YYYY; Asia/Amman) | **PA** | U-19 authority ladder (addition 9) makes this explicit: Standard = contract; Micro runtime (formatters) = carrier. GAP-22 centralization is a later Micro wave, not this run. |
| 18 | Navigation labels «مشروعي الآن/العمل/مالي/أدواتي» + in-grid FAB «سجّل» (navigation.ts L13–18; BottomNav.tsx L29–32) | **PD** (resolved by register; not a Standard content change) | U-09: Micro labels and in-grid labeled FAB stay Micro's. Standard gains only the note that labels/FAB geometry can be product-owned variants (navigation-shell.md wording). No Micro words enter the Standard. |
| 19 | Period controls: native month inputs + quick ranges (FinancePeriodResultSection; Statement L276) | **RC** (variant) / time semantics stay product-owned | U-08: Standard documents chip + native month/date-input as two variants (addition 4); Micro's ranges/defaults remain product-owned. |
| 20 | Token telemetry: 631 `--space-*` uses vs 7 raw margins (index.css — 631 exact match re-verified) | **PA** | GAP-45 preserve; formalized later via the Micro-side `--vf-*` mapping layer (U-01/W2), not in this Standard run. |

**Counts: RC = 6 · MP = 9 · PD = 1 · PA = 4 (20 capabilities classified).**

Boundary verdict: the classification matches the register's supreme rule (register preamble) and U-20: only composition-level grammar (knowledge-state presentation, row marker/stripe, AUX behaviors, period variant, quiet feedback, overlay guidance, type floor, icon mirroring, authority ladder, manifest fixes) crosses into the Standard; every capability that carries Micro data, routes, words, or state logic stays in Micro.

---

## 3. Protect-list verification (with spot-check evidence)

All eight protected strengths verified in the pinned clone; in every case the proposed Standard additions either strengthen or do not touch the strength. **Protect-list verdict: PASS (8/8), no conflicts found**, subject to the vocabulary-firewall conditions in §4.

| Protected strength | One-line evidence (file + line + behavior) | Conflict check vs the 10 additions |
|---|---|---|
| Honest voids | `pages/Home.tsx` L43–46 `factStateLabel`: incomplete → «غير محدد بعد», not_initialized → «غير مسجل» (with road → «غير مسجل — سجّله» L72–80), known → the number itself; `G5DecisionPanel.tsx` L17/19 «غير متاح» for invalid; `InventoryMaterials.tsx` L383–386 «صفر مؤكد» (measured zero). | None. The Standard already encodes the 3 voids (`component-contracts.md` L28: action chip «سجّله» / «غير متاح» / "0"); the knowledge-state addition adds a knowledge tier without redefining voids. Semantics wiring remains product-owned (5.3 §12). |
| Current state words | `G5DecisionPanel.tsx` L22–31: «متاح / يحتاج مراجعة / غير متاح / ناقص»; «بانتظار قرار» ×15/10 files; «مسودة» ×228/59 files — all live Micro copy, tests included. | None, **conditional on the firewall** (§4): U-05 keeps Micro words as-is; the Standard's knowledge-state examples must use neutral words so no ratification-by-example occurs. |
| Bidi/digits | `presentation/formatters.ts` L4–9 Intl `en-US` money formatter; L19–22 policy comment (English digits, numeric DD/MM/YYYY, no month names); `DisplayValue.tsx` L17/29/40 `<bdi dir="ltr">`; `EnglishNumberInput.tsx` L58–62 (`type="text"`, `lang="en"`, `dir="ltr"`) + L78 `normalizeAsciiDigits` (Arabic-Indic → English at entry). | None. `typography.md` L23 requires exactly this; no addition touches digits or bidi. |
| Formatters | `formatters.ts` L50 `formatMoneyMinor`, L57 `formatMoneyWithUnit` (`"<n> د.أ"`), L113–117 `formatLocalDate` (DD/MM/YYYY), L1/L110/L143 domain imports — single presentation authority, presentation never changes stored value (L3 comment). | None. Addition 9 (authority ladder, U-19) *names* formatters.ts-class runtime code as the implementation authority — strengthens it. Note: GAP-22 (275+ inline `د.أ` bypasses) is a Micro-side later wave; my recount: 279 `د.أ` in `.tsx` (incl. tests), 319 across all src — see §6 risks on count definitions. |
| Safe areas | `index.css` L288–289 `--main-bottom-space`/`--main-scroll-space` with `env(safe-area-inset-bottom)`; L291 `safe-area-inset-top` in min-height; L785 `padding-bottom: env(safe-area-inset-bottom)` on the nav; L296–298 surface-route clearance 116px + inset. | None. Addition 3 (AUX addendum, U-10) documents safe-area clearance as contract — codifies what Micro already does. |
| Keyboard clearance | `MicroAppShell.tsx` L62–69 `visualViewport` resize listener (threshold 120px) → L91 `data-keyboard-open`; `index.css` L774–778 hides header+nav when keyboard open (content stays visible). | None. Addition 3 documents keyboard-driven chrome hiding; recommend the addendum state the Micro principle that content is never hidden under the keyboard (chrome hides, content does not). |
| UnsavedChangesGuard | `UnsavedChangesGuard.tsx` (301 L): history sentinel L61–64 + popstate back-interruption L90–114; `beforeunload` L115–123; PWA dirty bridge L60 (`setDirtyForms`); in-dialog save-failure disclosure L47–49/L169–174; dialog L210–300 with focus trap, Esc=stay, least-destructive-first (L207–209 comment). | None. U-20/GAP-40 keep it Micro-owned; additions 5/6 (quiet feedback, overlay guidance) describe patterns this stack already satisfies — the Standard must not claim to specify it beyond a pointer. |
| Domain purity | `formatters.ts` L110/L143 import from `@micro-domain/shared` (presentation re-exports domain logic only, L139–144 comment); reports: zero application→UI imports, 212 `@micro-domain` imports (Flash §8.1). | None. No Standard addition reaches domain/application/storage; addition 9's authority ladder explicitly reserves meaning+persistence to those layers. |

Additional protected items (report-mandated, verified indirectly): navigation labels + in-grid FAB are deliberate/tested (`navigation.ts` L10–18 comment; `BottomNav.tsx` L26–32 audit-cycle comment) — U-09 keeps them; token telemetry 631 verified exact.

---

## 4. Vocabulary firewall

### 4.1 Micro product vocabulary — must NOT enter the Standard (block-list)

Verified by grep in the pinned Micro clone (occurrence counts = total / files):

| Word / phrase | Where it lives in Micro | Count |
|---|---|---|
| «مشروعي الآن» | primary nav label 1 + header contexts (navigation.ts L14, BottomNav, tests) | 17 / 10 |
| «العمل» · «مالي» · «أدواتي» (as the ratified 4-set) | nav labels (navigation.ts L15–17) | set is Micro's per U-09 |
| «سجّل» (FAB label) | BottomNav.tsx L29–31 (aria-label + span) | FAB-specific |
| «غير مسجل — سجّله» (fact-triad phrase) | Home.tsx L72–80 (not_initialized + road) | triad-specific |
| «غير محدد بعد» | Micro's canonical not-initialized / unconfirmed-quantity word (Home.tsx L46; InventoryMaterials.tsx L375; integrityCheckService.ts L674) | 32 / 13 |
| «التكلفة غير معروفة» · «تكلفة معروفة جزئيًا» | knowledge-state copy (InventoryMaterials.tsx L378–381) | knowledge-specific |
| «صفر مؤكد» | confirmed-zero rendering (InventoryMaterials.tsx L385) | Micro rendering |
| «يحتاج مراجعة» | canonical needs-review word (G5DecisionPanel.tsx L26; 47 / 27 files) | 47 / 27 |
| «بانتظار قرار» | G5 pending-decision status (g5Plurals, OrderDepositPanels, services) | 15 / 10 |
| «متاح» / «ناقص» (G5 senses) | G5DecisionPanel.tsx L24/29 | G5-specific |
| «سليم» / «خلل» | integrity PASS/FAIL words (ToolsIntegrity.tsx L28–30) | integrity-specific |
| «الأثر بعد التراجع عن التصحيح» · «سجل لا يحذف بصمت» · «متراجع موثقًا» | correction lifecycle (EventsLayer L730; CashWallets L274; InventoryMaterials L679; activityLabels) | correction-specific |
| «دفتر الناس» · «محافظ الكاش» · «المواد والمخزون» · «ورقة التحصيل» etc. | header context labels (navigation.ts L20–42) | route contexts |
| «مايكرو» | wordmark (AppHeader.tsx L31–33) | brand |

### 4.2 Generic Arabic presentation words already used by the Standard (safe, shared)

From `component-states.md` (matrix examples): «مسودة», «بالانتظار», «تم», «فشل», «ملغي», «عُكس», «رُوجعت», «جزئي», «مستحق», «متأخر», «غير معروف». From `component-contracts.md` L28: «سجّله» (unrecorded-void action chip example), «غير متاح» (unavailable), "0" (measured zero). From `empty-loading-error-states.md`: «سجّل أول قيد» (no-data example), «غير معروف», «بالانتظار».

These are generic: Micro also uses «غير متاح» (101 / 44 files) and «غير معروف» (32+ / 15 files) generically — shared vocabulary, not a firewall violation. Per U-12, all Standard words are examples owned by products; the firewall is about not importing Micro's *canonical* state/feature words (§4.1).

### 4.3 Recommended neutral knowledge-state example words (unconfirmed / unknown / incomplete / needs-review / estimated)

| Knowledge state | Recommended example word | Micro collision check | Verdict |
|---|---|---|---|
| unconfirmed | «غير مؤكد» | 4 hits / 3 files, all inside prose/integrity detail text (e.g., integrityCheckService.ts L674 «رصيد بداية غير مؤكد»), never a canonical chip word (Micro's chip word is «غير محدد بعد») | **Accept with flag** — generic adjective, light prose presence in Micro; example-only |
| unknown | «غير معروف» (reuse the Standard's existing unknown word) | Already the Standard's word (`component-states.md` L18); Micro uses the same generic adjective (32+/15) incl. «التكلفة غير معروفة» | **Accept** — but do NOT import the Micro phrase «التكلفة غير معروفة»; keep the bare adjective |
| incomplete | «غير مكتمل» | 8 hits / 6 files in generic prose/labels (CostEditor L60 «وقت العمل أو سعر الساعة غير مكتمل», OrderDetail L52 «النتيجة غير مكتملة» — feminine variant) | **Accept with flag** — generic adjective, light presence; example-only |
| needs-review | «بحاجة لمراجعة» | **0 hits in Micro** (Micro's canonical phrasing is «يحتاج مراجعة», 47/27 — deliberately a different string) | **Accept — cleanest choice**; the distinct phrasing keeps the Standard example visibly non-Micro |
| estimated | «تقديري» | 37 hits / 24 files across Micro copy (estimated time/cost, estimate tools, EventsLayer, G5) — widespread generic adjective with product contexts | **Accept with flag** — generic Arabic, not Micro-coined, but heavily used in Micro copy; must be presented strictly as an example, never as a ratified product word. (If the owner wants zero collision: omit the Arabic example for this row and state the grammar only.) |

Marker/tone grammar to accompany the words (consistent with the existing matrix, no new colors): every knowledge state = word + non-color marker (question/info icon for unconfirmed and unknown; half-filled/progress shape for incomplete; eye icon for needs-review; `≈` sign prefix for estimated) on neutral ink or the Warm Tint ground with the tint-ink pattern (`component-states.md` L20). A knowledge state never binds Success/Error colors (knowledge ≠ financial outcome: unconfirmed is not a failure, estimated is not a success), never reads as pending, and never silently drops the value. Knowledge states are presentation of information *quality* and must stay distinct from the 10 financial-state matrix rows and from the three honest voids.

**Flagged near-collision to manage:** the Standard already uses «سجّله» as the unrecorded-void action-chip example (`component-contracts.md` L28) while Micro's FAB label is «سجّل» (BottomNav.tsx L29–31). These are distinct strings with distinct roles; keep both, but the Standard must not present «سجّل» as a navigation/FAB example, and the AUX/nav-shell variant note (U-09) must not carry Micro's label set.

---

## 5. Register-row mapping of the ten additions (Micro-side benefit check)

| Addition (this run) | Register row(s) | Register text confirming it | Micro-side benefit |
|---|---|---|---|
| 1. Knowledge-state presentation contract | **U-11** (primary), **U-05** | U-11: «نضيف عقدًا عامًا لحالات unconfirmed/unknown/incomplete/needs-review/estimated، دون فرض كلمات Micro أو معنى مالي جديد» → modifies `component-states.md` + `component-contracts.md`, presentation only; U-05: «عقد Knowledge States عام بلا كلمات منتجية مفروضة» | Micro keeps its words (`غير محدد بعد`, `يحتاج مراجعة`…) and gains a contract its knowledge rows can cite; state adapter + word mapping stay Micro (U-05 ما يبقى في Micro). |
| 2. Operational-row marker + optional ≤3px inline-start stripe | **U-06** | «اعتماد marker وedge stripe اختياري بحد أقصى 3px، ودائمًا مع كلمة الحالة» → Row slot + stripe contract fixed in the 29; Row primitive stays Micro | Micro's rows (next-action, ledger, integrity) gain the non-color redundancy rule; adoption is gradual, Micro-side (W3). |
| 3. AUX behavior addendum (route-kind chrome, keyboard hiding, safe areas, context suppression, scroll border, transition) | **U-10** (route-kind chrome), rides with **U-09**'s variant note | U-10: «عقد route-kind/chrome behavior عام» → enters the 29; routeClassifier + per-family decisions + tests stay Micro | Micro's working-but-contract-less shell behaviors (GAP-32 "preserve") become documented contracts; nothing changes in Micro code this run. |
| 4. Period-control variants (chip + native month/date input; time semantics product-owned) | **U-08** | «يمكن دعم Period Chip كـvariant، وليس استبدالًا إلزاميًا» + «بقاء time semantics خارج Standard» → variant clarification in period contract | Micro's native month inputs + quick ranges are legitimized as the variant; no forced chip migration. |
| 5. Quiet/inline feedback as legitimate Snackbar alternative | **U-07** | «اعتماد inline/quiet feedback في Micro، وعدم إعادة Snackbar كافتراضي. Snackbar يبقى عقدًا اختياريًا غير مفعل» | Micro's no-toast regime (110 `role="status"`, receipt/outcome cards) is ratified as a valid consumer instead of a divergence. |
| 6. Overlay vs in-flow guidance | **U-17** | «confirmation/deletion/high consequence = Dialog/Sheet؛ الشرح والتحرير المستمر = in-flow. لا نحول كل شيء إلى overlay» | Micro's `<details>`/layer disclosure grammar (EventsLayer etc.) is protected from forced overlay conversion. |
| 7. Type floor 13px labels / 12px non-financial metadata / ≥15px financial facts | **U-04** | «13px حد labels، و12px للـmetadata غير المالي فقط، والمبالغ والحقائق المالية لا تقل عن 15px» | Codifies D-04(b); Micro applies tokens gradually (no mass rewrite) — the floor becomes the target for W2/W3. |
| 8. Icon mirror flags + semantic roles, no forced library | **U-13** | «نستخدم Lucide مع mirror flags وقواعد RTL، ويظل Registry مرجعًا تعاقديًا» → icon role/mirror contract clarified; icon adapter + tests stay Micro | Micro's Lucide usage (verified in navigation.ts/AppHeader/BottomNav imports) is not forced onto the 43-glyph registry. |
| 9. Authority ladder (Standard=contracts; Micro mapping=runtime carrier; Micro docs=guidance; domain/application/storage=meaning+persistance) | **U-19** | «Standard = visual contracts؛ Micro mapping = runtime implementation؛ Micro docs = guidance؛ domain/application/storage = meaning and persistence» | Protects formatters.ts as runtime authority and domain purity; sets the docs-sync guard direction. |
| 10. Verification/manifest corrections (29+2 split; no device/screen-reader claims) | **U-19** | «تعديل authority wording والـmanifest/README عند الحاجة» + register's "ما يدخل" item 10 (guard/verification wording preventing unimplemented claims) | Verified defect: `MANIFEST.json` `file_count: 29` vs 31 files on disk (split only in `updated_by` prose). Fix is cosmetic and Documents-side. |

**Mapping confirmation:** 10/10 additions trace to register rows U-04, U-05, U-06, U-07, U-08, U-10, U-11, U-13, U-17, U-19 (with U-09 and U-12 as adjacent constraints: U-09 governs the nav/FAB variant note inside addition 3's file scope; U-12 forbids fixing Micro orthography in this run). Two rows from the task's list are **not** 1:1 additions and must be recorded honestly:

- **U-18 (loading):** its Standard-side deliverable («توضيح أن skeleton optional، وليس قبولًا عامًا لكل شاشة») is not among the ten headline additions. Recommend riding a one-line skeleton-optional clarification into the `empty-loading-error-states.md` revision that the knowledge-state contract touches (it already mandates skeleton at L9 — U-18 requires the optional/honest-text caveat), or explicitly recording its deferral in the reconciliation plan. Unhandled, it is a register-compliance gap.
- **U-20 (Micro feature patterns):** not an addition — it is the governing boundary rule for this audit: the Standard may gain pattern slots/guidance «دون كلمات أو routes أو business policy». All nine MP classifications in §2 derive from it. The ten additions comply (none encodes Micro logic); any drift here is a stop condition (execution prompt §Stop conditions).

---

## 6. Risks and count variances (for the reconciliation log)

1. **Vocabulary leakage via examples (primary risk).** The knowledge-state contract, its gallery demo, and Prototype v1 must use only §4.3 neutral words. The block-list (§4.1) — especially «غير محدد بعد», «يحتاج مراجعة», «بانتظار قرار», «مشروعي الآن», «سجّل» as FAB — must not appear as Standard examples. Suggest an explicit "words are examples; products own their words" clause (consistent with U-12).
2. **Near-collision «سجّله»/«سجّل».** Manage per §4.3 final paragraph; do not let the nav-shell variant note carry Micro's label set.
3. **Knowledge-state tone risk.** Knowledge states must not bind Success/Error colors (unconfirmed ≠ failure; estimated ≠ success) and must not collapse into the honest voids (a knowledge state qualifies a *displayed* value; a void replaces an absent one). Recommend an explicit boundary sentence in the contract.
4. **Count variances (record definitions, per REPORTS_RECONCILIATION; do not silently choose):**
   - `د.أ` inline compositions — Flash: "275 exact literals across 53 files"; my recount: **279 across 58 `.tsx` files (incl. tests)**; **319 across 76 files** across all src (`.ts`+`.tsx`). Direction unchanged (hundreds of inline compositions vs the formatter path); definition-dependent.
   - `formatMoneyWithUnit` consumers — Flash GAP-22: "in 6 files"; my count: **17 files** reference it (incl. application services and tests). Centralization gap stands; definition-dependent.
   - Exact matches re-verified: `role="status"` = **110** (60 files) ✔; `--space-*` uses in index.css = **631** ✔; deep-flow regexes = **29** ✔; UnsavedChangesGuard = 301 L ✔; QuickActionSheet modes = 4 ✔.
5. **U-18 mapping gap** (see §5) — skeleton-optional clarification needs a home or a recorded deferral.
6. **AUX addendum scope discipline.** It must remain behavior-level (chrome visibility by route kind, keyboard hide, safe-area clearance, context-label suppression, scroll border, transition timing/range). Route lists, label sets, FAB geometry, and the D-10 per-family reader-depth decision stay out (Micro-side, post-D-10).
7. **Manifest correction dependency.** The 29+2 fix (addition 10) should also state that `file_count` refers to core contracts only, or adopt a structured split field — cosmetic, Documents-side, reversible.
8. **No Micro changes in this run.** All ten additions are Documents-side; every Micro-side benefit (U-05 marker mapping, U-06 Row primitive, U-13 icon adapter, U-07 Notice primitive, U-08 period-controls pattern module) lands in later Micro waves (W2–W5), per the register's wave plan and the execution prompt's end gate ("This run ends at the updated Standard + Prototype v1 handoff").

---

## 7. Bottom line

The evidence supports the run's premise: Micro's transferable wealth is **composition grammar, not product meaning**. Six capabilities generalize into contracts (knowledge-state presentation, row marker/stripe, AUX behaviors incl. route-kind chrome + 260ms transition, period variants, quiet feedback, plus the type floor/icon/authority/manifest riders); nine are Micro feature patterns to document and protect; one (labels/FAB) is already settled as product-owned by U-09; four are Micro strengths to leave untouched. The protect list passes 8/8 with evidence. The vocabulary firewall has clean neutral words for all five knowledge states — «غير مؤكد», «غير معروف» (reuse), «غير مكتمل», «بحاجة لمراجعة» (zero collision), «تقديري» (flagged) — and a verified block-list of Micro words. The ten additions map to the register without contradiction, with one honest gap (U-18's skeleton-optional note) to resolve in the reconciliation plan.

*Agent 2 — read-only; no repository writes. Report + worklog append only.*
