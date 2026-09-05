# Agent 2 — Micro-Specific Adaptation Review

| | |
|---|---|
| Report ID | micro-group-6-parallel-audit-001 / agent-2-zman-transfer-audit |
| Date | 2026-09-05 |
| Baselines | Zman `bdd63ab` (read-only) · Micro `961051f` (on Agent 1 main `1242aa6`) |
| Inputs | SA-4 financial adaptation audit + SA-3 UX audit + principal verification (continuation prompt §6 questions) |

---

## 1. Method

For every financially-relevant transferred capability, the adaptation review answers the continuation prompt's question set: what Zman problem it solved; what the Micro problem is; what was copied literally; what was adapted and why; whether it feels native; minimum-mandatory-inputs discipline; thumb-zone CTAs; plain Arabic and jargon freedom; five-tab placement; first-time discoverability; quick-vs-structured step count; honest empty/unknown/estimated/pending/error/partial states; RTL at 360×800 and 390×844 with keyboard/safe areas; offline behavior; integration with Home/Activity/Finance/Statement/Health/deep links; correction/reversal/backup/restore meaning preservation; harm potential (hidden money, duplicate revenue, misclassified cash, false inventory, unknown-as-zero); added risk; and the final recommendation (ADOPT / ADAPT / REWORK / REJECT_WITH_REASON / MISSING / NEEDS_OWNER_DECISION).

A literal copy that violates Micro's contracts would be rejected. **None was found**: every transferred capability was consciously re-expressed. The three Zman patterns that must never be ported (per SA-4 §2): retroactive read-time depreciation netting; remainder-as-cash-in at delivery; single-idempotency-key retry blocking after reversal (`Z finance/actions.ts:1456-1472` returns `ok` with no data after reversal).

## 2. Per-capability adaptation decisions

| # | Capability | Zman problem → Micro problem | Copied literally | Adapted for Micro (why) | Native feel | Verdict |
|---|---|---|---|---|---|---|
| 1 | Guided financial entry (ZC-01) | "one modal, 4 modes, hints" → "per-kind guided editors + in-sheet quick entry" | nothing structural; the *pattern* of mode-specific minimal fields + pre-save effect copy | 4 server modes split into kind-specific routes with 2 mandatory fields; hints became «ماذا سيحدث؟» decision cards; in-place edit replaced by reverse+replace (correction rule) | **YES** — FAB sheet for 10-second paths, full editor for structured entry; effect copy browser-verified | **ADAPT** |
| 2 | Expense classification (ZC-02) | "named category + 2-dim flags" → "truth-context questions + free label" | label free-text (Zman parity: lazy enrollment) | flags replaced by explicit event kinds (asset, waste, payable); relationship/behavior/purpose/knowledge questions ask *when the answer changes money meaning*, not to fill a taxonomy; 4 natures incl. مختلط | **YES** — collapsed behind «افتح التفاصيل»; never blocks save | **ADAPT** (category management gap → P2-3) |
| 3 | Payments feed → activity (ZC-03) | "unified feed + pagination" → "decision-first recent block + full reader" | nothing | pagination dropped (local scale); corrections+events unified; family guard routes asset/loan events to their owners | **YES** — «آخر ما حدث» on Home; full reader under مالي | **ADAPT** |
| 4 | Manual sales → direct sales (ZC-04) | "cash income outside orders" → same | sale record + revisions shape | INV-4 netting not ported (Micro: order collection path); cancel = mirror wallet reversal (FT-02); post-save consumption bridge | **YES** — FAB «تسجيل بيع» | **ADAPT** |
| 5 | Order lifecycle (ZC-05/06) | "5 statuses + conversion" → "10 statuses + settlement + delivery review" | deposit-as-liability principle | conversion split into delivery (revenue recognition) + explicit settlement (three options) + retained-deposit classification; forfeit-as-revenue not ported | **YES** — DeliveryReview is a Micro-native full-surface commitment step | **ADAPT** |
| 6 | Selective inventory (ZC-07) | "tracked toggle + auto-deduct" → "deliberate tracking + explicit receiving" | tracked/untracked whitelist concept | automation core rejected (4 documented financial-truth violations); purchase→receipt bridge transferred instead (TR-07); non-negative; unknown opening ≠ zero | **YES** — bridge prefills from purchase; zero-stock strip | **ADAPT** |
| 7 | Cost calculator (ZC-08) | "components inside order form" → "standalone thinking tool + snapshots" | component-line cost accumulation concept | calculator is a Micro-only deep tool (no financial event); snapshots immutable; knowledge states; price floor; safety buffer | **YES** — under أدواتي (thinking-tool identity) | **ADAPT** |
| 8 | Single profit function (ZC-09) | "LOCKED-6 + IC-13" → "canonical period reader + MIC-1 cross-check" | the single-source discipline | bounded profit: null-on-unknown is a cross-checked first-class state; no third profit number exists (SA-2 grep-verified independent paths) | **YES** — «غير متاح» honesty instead of a fabricated number | **ADAPT** |
| 9 | Assets & depreciation (ZC-10) | "read-time depreciation" → "explicit recorded depreciation events" | capitalization boundary question («هذا الشيء للاستخدام لفترة طويلة؟») | read-time netting not ported (retroactivity violates truth); disposal/writeoff added; unknown-life honesty («مجهول») | **YES** — browser: unknown-start asset honestly shows "بلا إهلاك حتى تُحدده" | **ADAPT** (F-3 netting gap documented) |
| 10 | Loans/receivables (ZC-11) | "loan = asset" → same principle, event-based | principle + settled-stay-visible | append-only repayments/corrections; FT-03 family guard; MIC-11 | **YES** — plain Arabic «أعطيت مالًا يُعاد» | **ADAPT** |
| 11 | Accounts/owner money (ZC-12/13) | "accounts + opening lock" → "wallets + known/unknown opening" | transfer pairing; owner money never profit | wallet ledger + unallocated allocation/coverage (Micro-only strength); opening honesty (unknown ≠ zero); later completion | **YES** | **ADAPT** (archival P2-6) |
| 12 | Dashboard → Home (ZC-14) | "analytical panels" → "decision-first الأهم الآن" | nothing | panels rejected (identity); the questions analytics answered (period profit, cash, alerts) are answered by Finance period layer + pulse + integrity | **YES** — Home verified at both viewports | **ADAPT** |
| 13 | Reports → statement (ZC-15) | "6 downloads" → "one canonical statement + share" | Markdown+BOM delivery (byte-level parity, browser-verified) | 6 kinds consolidated into statement + activity + integrity; truth lines verbatim; sources expanders; manual share with preview | **YES** | **ADAPT** |
| 14 | Integrity suite (ZC-16) | "IC-1..16" → "MIC-1..16" | check-suite concept + per-check offender ids | derived from Micro's own tested rules; deliberate states = WARN not FAIL; deep links to fixes; this audit adds reverse orphan sweep | **YES** — «اطمن على أرقامك» plain Arabic | **ADAPT** (MIC-3/5/6 reserved → P2 F-4) |
| 15 | Catalog (ZC-17) | "name/unit/cost" → "dimensioned units + conversions" | nothing | unit system re-designed (reverse gap); default cost = prefill snapshot only (parity) | **YES** | **ADAPT** |
| 16 | Waste/write-off (ZC-18) | "immutable shadow expense" → "reasoned reversible waste" | non-cash principle | reversibility added (Zman's own known gap م-5 fixed); netting-into-result differs → F-1 owner decision | **YES** | **ADAPT** (F-1) |
| 17 | Audit log → corrections (ZC-19) | "append-only everything" → "documented corrections + activity" | append-only philosophy | ordinary creates excluded from one stream (single-owner local trade, documented); corrections carry reasons/previews/net effect/restore | **YES** | **ADAPT** |
| 18 | Snippets (ZC-20) | — | — | — | — | **EXCLUDED_BY_OWNER** |
| 19 | WhatsApp templates (ZC-21) | "automation + phone normalization" → "manual share with editable preview" | nothing (automation on never-build list) | fixed per-kind share drafts + SharePreview; no background transmission | **YES** | **ADAPT** (customization P3) |
| 20 | Auth/lock/PWA (ZC-22) | "server passcode + idle lock" → "local lock + dirty-safe PWA" | idle-lock concept; update-prompt concept | no auth (local-first platform refusal); PBKDF2 PIN + backoff + veil (A1-hardened); dirty registry blocks SW reload while a form is dirty | **YES** | **ADAPT** |
| 21 | Backup (ZC-23) | "partial export, no restore" → "verified envelope + restore + tamper rejection" | nothing (Zman's design was the weaker one) | full export with sha256 + counts + migration chain; DP-01/09 + AI-01 (this audit) | **YES** | **ADAPT** (reverse gap) |
| 22 | Mobile RTL UX contracts (ZC-24) | "documented contracts" → "executable guards" | 48px targets; logical RTL properties; teaching empty states; header stability | contracts became CI gates (density caps, token rules, 44px chips); 5s undo replaced by documented delete | **YES** — zero console errors at both viewports | **ADAPT** |

## 3. Micro-specific quality criteria (continuation prompt §6 checklist)

- **Usefulness to a Jordanian micro-business owner** — every ADAPTED row above answers a question the owner actually asks («شو صار على البنزين؟», «مين عليه إلَي؟», «قديش طلعلي هالفترة؟»); nothing transferred exists only as code.
- **Cognitive load / 10-second fast paths** — quick sheet = 1 mandatory field; guided expense = 2 mandatory; classification collapsed; verified in browser.
- **One-handed reachability** — sticky bottom save bars in 14 editors; FAB center action; 44/48px targets (A1 extended chips); SA-3 found no top-positioned primary CTA on transferred surfaces (OrderDetail reader CTA P3-06 documented).
- **Progressive disclosure** — no Zman quick flow became a mandatory-heavy form (SA-3 §8 counts; verified in browser on expense/asset/loan editors).
- **Plain Arabic** — no English leakage; no accounting jargon on transferred surfaces; effect copy before every financial commit (browser-verified texts quoted in test-evidence file).
- **Five tabs + FAB consistency** — all transferred surfaces map to مشروعي الآن/العمل/سجّل/مالي/أدواتي families; no sixth seat; `/review` redirects; no orphan routes (SA-3 §4).
- **Local-first privacy & offline** — zero network in transferred flows; share is manual-only; lock is local; PWA updates are dirty-safe; offline truth lines on every editor.
- **Financial truth, correction, auditability** — 14/14 Micro financial-safety rules pass (SA-4 §3 table); corrections preserve originals with reasons and net effects; source links survive export/import.
- **Discoverability & source navigation** — 0 HIGH orphans; every record kind surfaces in ≥1 core reader with `?event=`/`?from=` links (SA-3 §11; browser-verified).
- **Duplication/competition** — none found: no second write path, no competing navigation system, no duplicate service (SA-5 scenario 13; reverse check via route/service census).
- **Hidden cash/inventory/revenue/deposit/liability effects** — none found: every delta column pair was re-derived in tests (MIC-3 “سلامة الأحداث والتوزيع” PASS on 4 fresh events); deposits stay liabilities until explicit classification; retained-deposit revenue requires a documented decision.
- **Safe to keep / improve / defer / reject** — verdicts: keep everything currently ADAPTED/MATCHED; improve the filed P2s; defer the three NEEDS_OWNER_DECISION items; nothing to reject (the rejections happened in the transfer design and are respected).

## 4. Final recommendation

**ADOPT the current transfer state as the baseline for controlled integration.** The transfer is not a port; it is a disciplined re-expression. The residual work is small, explicit, and owner-gated (see findings file). No REWORK, no REJECT_WITH_REASON, no MISSING capability remains actionable at capability level.
