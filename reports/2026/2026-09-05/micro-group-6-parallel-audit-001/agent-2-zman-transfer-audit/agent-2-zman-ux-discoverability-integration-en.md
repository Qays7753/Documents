# Agent 2 — Discoverability, UX, Integration, and Harm Assessment

| | |
|---|---|
| Report ID | micro-group-6-parallel-audit-001 / agent-2-zman-transfer-audit |
| Date | 2026-09-05 |
| Baseline | Micro `agent/group-6-zman-transfer-audit` @ `961051f` (on Agent 1 main `1242aa6`) |
| Inputs | SA-3 transfer UX & discoverability audit (static, all 56 routed patterns) + principal fresh-data browser QA at 360×800 and 390×844 RTL |
| Harm vocabulary | financial · data-loss · misleading-state · discoverability · cognitive-load · privacy/security · performance · maintainability · no material harm (continuation prompt §9) |

---

## 1. Tab model and placement audit

The shell is exactly five tabs + FAB: **مشروعي الآن** (`/`) · **العمل** (`/orders`) · **سجّل** (FAB, 56px, `BottomNav.tsx:29-32`) · **مالي** (`/finance`) · **أدواتي** (`/tools`). The FAB sheet carries 5 quick actions (direct sale, expense, order draft, estimate, collection). No transferred surface violates the five-seat model; no sixth seat exists; `/review` redirects to `/finance`; `/foundation` is permanently reachable from Home (`Home.tsx:348`).

Placement of transferred capabilities (browser-verified where noted):

| Transferred capability | Placement | First discoverable | Taps from Home |
|---|---|---|---|
| Guided expense + classification | مالي family + FAB quick sheet | FAB «تسجيل مصروف» (browser) | 1 (sheet) / 2 (deep) |
| Purchase→receipt bridge | العمل family (suppliers → inventory) | purchase card CTA | 3 |
| Waste/shortage | inventory surfaces | inventory FAB actions | 2–3 |
| Calculator + estimates | أدواتي (thinking tools) | Tools module states (browser: H1 renders) | 2 |
| Orders + delivery review | العمل | العمل tab + order cards | 1–2 |
| Direct sale | FAB sheet | «تسجيل بيع» | 1 |
| Deposits/settlement/retained | order detail + collect sheet | order journey | 2–3 |
| Assets | مالي family | Finance «افتح سجل الأصول» (browser) | 2 |
| Loans | مالي family | Finance loans entry (browser: 80 JOD loan created) | 2 |
| Activity reader | مالي | Finance «آخر ما حدث — القارئ الكامل» (browser) | 2 |
| Statement + share | مالي | Finance «كشف الفترة» (browser: report downloaded) | 2 |
| Integrity (health) | أدواتي + مالي doorway | Finance «فحص سلامة مالي» (browser: PASS) | 2 |
| Drafts | editors themselves | restore banner on reopen | 0 (automatic offer) |
| Backup/restore/lock | Settings | Settings data-protection card (browser: export + tamper rejection) | 2 |

## 2. Orphan and reachability findings (SA-3 §4 + browser)

**0 HIGH orphan routes.** All 56 routed patterns were grepped for in-app entries: 53/55 reachable via normal navigation; two intentional URL-only shims (`/orders/new` F-003 compat, `/review` redirect). Two MED single-entry routes:

- **UXD-01 (P2, discoverability):** `/share/preview` has a single deep entry (OrderDetail «شارك رسالة مع الزبون», `OrderDetail.tsx:1158`), 3 taps from Home, invisible from the Finance/Statement family even though its canonical fallback is `/finance` (`navigationContract.ts:164`). Sharing patterns also diverge: orders get an editable preview page (contract 33) while the statement shares directly via the system sheet/clipboard without a preview (`Statement.tsx:236-241`). Harm: **discoverability** (the owner may never find customer-message sharing from financial surfaces). Action: add a «شارك» entry on Statement routing through `/share/preview`, or record the single-context intent in contract 33. Not fixed here (UX placement choice, needs owner nod).
- **UXD-02 (P2, discoverability/cognitive-load):** owner withdrawal (`/finance/withdraw`) is reachable only inside the unified owner ledger (`OwnerEntitlement.tsx:662`) — 3 taps with a concept hop. This is the documented deliberate X-05 single-entry design («يسأل سحب من المشروع لنفسك؟»). Harm: **discoverability**, no material harm (the existing entry writes correctly and previews the effect). Action: optional labeled affordance «اسحب لنفسك» in the Finance hub.

## 3. Label, language, numeric, and date audit

- **Plain Arabic, no jargon, no English leakage:** PASS across all transferred surfaces (SA-3 §5 sample + browser texts: «ماذا سيحدث؟», «أدخل حصة المشروع فقط؛ لا يحفظ النظام إجمالي فاتورة البيت», «السداد يرفع الكاش ويخفض المتبقي — ليس إيرادًا جديدًا ولا ربحًا»). G5 vocabulary never leaks to users («المتوقعات» instead).
- **Effect-explaining copy before every financial commit:** PASS — browser-verified on investment, expense, shared allocation, asset, loan, repayment sheet.
- **English digits (0–9):** PASS — `normalizeAsciiDigits` input boundary (`englishNumeric.ts:8-19`); all 27 numeric pages use it; zero `type="number"` inputs.
- **DD/MM/YYYY:** PASS — centralized `formatters.ts:99-103`; browser-verified on Home rows (05/09/2026), activity reader period line (من 30/08/2026 إلى 05/09/2026), statement export header, integrity timestamp. The only ISO fallbacks are unreachable-with-valid-data render fallbacks (UXD-08, P3, no material harm).
- **Unknown-state honesty:** PASS — «ما بعرف الآن — يُحدَّد لاحقًا» (setup), «مجهول» life/start (assets), «غير مصنّف» (statement), «غير متاح» (bounded profit), status-incomplete reasons (period layer). No unknown rendered as zero was found anywhere.

## 4. One-handed, density, progressive disclosure

- **Primary CTA placement:** sticky bottom save bars in 14 editors; bottom sheets (vaul) for quick entry; full pages for deep entry. No transferred surface places its primary CTA in the top corner. OrderDetail's status-conditional CTA sits in a decision card rather than a dock (UXD-06, P3, no material harm — the page is a reader that keeps bottom nav).
- **Target sizes:** 44/48px discipline including Agent 1's 44px chips (`index.css:6365-6371`, commit `0d45bb4`).
- **Density gates:** all 52 routed pages within §10 caps (design guards + text-density in CI).
- **Progressive disclosure:** quick sheet 1 mandatory field; guided expense 2 mandatory + collapsed classification; asset editor 2 mandatory + conditional life block; loan editor 2 mandatory. No Zman quick flow became mandatory-heavy.
- **RTL at 360×800 and 390×844:** both viewports exercised in the production build; all transferred surfaces render (H1 verified on 7 surfaces at 390×844); zero console errors; keyboard-open hides nav chrome.

## 5. Integration with core read surfaces

Every transferred record kind appears in at least one core read surface with direct source links (SA-3 §11 matrix + browser):

- Home «آخر ما حدث» block shows fresh events with `?event=`-style row links (browser: investment, expense, asset rows visible).
- FinanceActivity reader lists all events with kind chips + per-row source links (browser: 3→4 events).
- Finance period layer + pulse read the canonical period result; MIC-1 cross-checks statement/finance/pulse agreement (browser: PASS).
- Statement groups by category with «غير مصنّف» fallback + per-section «المصادر (n)» expanders (browser).
- Tools integrity deep-links offenders to their fix surfaces; MIC-10/11 link to `/assets`, `/loans`.
- Corrections layer + family guard route asset/loan events to their owner records (FT-03); with AI-01, no imported event can point at a nonexistent owner.
- Drafts surface as restore banners; backup/restore live behind the Settings data-protection card gated by PIN (A1 `DataActionPinGate`).

## 6. Harm assessment summary

| Harm class | Findings | Evidence |
|---|---|---|
| Financial | **none open** after this audit's fixes | SA-4 14/14 rules PASS; AI-01 closed the uncorrectable-orphan import hole (browser-verified rejection); F-1 (waste netting) is a disclosed-state question, not hidden money — filed for owner decision |
| Data-loss | **none** | backup envelope + verified restore + tamper rejection; drafts excluded from export but restorable locally; UnsavedChangesGuard + dirty-safe PWA update |
| Misleading-state | **none material** | bounded profit, unknown-honesty, status-incomplete reasons; UXD-08 ISO fallback is theoretical |
| Discoverability | 2 P2 (UXD-01, UXD-02) + 3 P3 polish | documented above with actions |
| Cognitive-load | 1 P3 (header context fallback duplicates wordmark on 5 paths, `navigation.ts:36-40`) | cosmetic |
| Privacy/security | **none** | local-only data; manual-only sharing (no background transmission, browser-verified); PBKDF2 lock with backoff; tokens never committed |
| Performance | **none found** | production build clean; PWA precache 96 entries; lazy routes all resolve; zero console errors |
| Maintainability | 2 P3 (vestigial `/orders/new` fallback entry; dead SQL noted in Zman only) | trivial |

## 7. Discoverability conclusion

A first-time owner who has never seen Zman can find and safely use every transferred capability: the FAB answers "I need to record something now" in one tap with a one-mandatory-field sheet; the five tabs answer "where do I look"; every financial commit announces its effect before it happens; every reading surface links back to its source; and the two medium discoverability tradeoffs (share preview entry, owner-withdrawal entry) are documented deliberate designs with cheap optional improvements, not defects of the transfer.
