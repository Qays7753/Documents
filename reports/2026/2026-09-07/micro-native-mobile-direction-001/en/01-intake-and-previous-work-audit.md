# 01 — Intake and Previous Work Audit

**Delivery:** `micro-native-mobile-direction-001`
**Stage:** 0 — problem definition and audit
**Date:** 2026-09-07
**Author:** central orchestrator (new conversation, independent execution)

---

## 1. Repository status and binding rules observed

The Documents repository (`github.com/Qays7753/Documents`, branch `main`, HEAD `622af98`) was cloned read-only for delivery preparation. The binding rules in `README.md` and `UPLOAD_GUIDE.md` were read first and govern this delivery: deliverables only, dated folder structure `reports/YYYY/YYYY-MM-DD/<delivery-id>/`, no silent replacement, `INDEX.md` updated in the same commit, a plain secret-free commit message, push via a transient environment credential (`GH_DOCS_TOKEN`) consumed by an in-memory credential helper that never writes the token to disk, config, URL, or any file, and a post-push verification checklist. This delivery is **Delivery 14** in the root index and does not overwrite any prior folder.

The production Micro codebase was not touched. Nothing in this delivery edits, proposes edits to, or depends on write access to `github.com/Qays7753/Micro`. The `handoff/` folder pattern from prior deliveries stays deliberately absent until approval.

## 2. What the two prior deliveries attempted — and why both are rejected

**Warm Ledger (`micro-visual-product-concept-001`).** A single continuous ledger-page composition: a concentrically carved hero truth block, full-width bands separated by tonal steps and hairlines, a 3px terracotta spine marking the primary band, a five-seat bottom shell, and review controls placed outside a `.device` phone frame with a 44px-radius bezel and simulated status bar. Its coverage was the strongest of the two: nine working surfaces (Today, Financial Truth, Quick Capture with NumericSurface, Receivables, Orders, Purchases, Cash Closing, Settings, Assistant entry), honest states, effect-preview sheets, and a disciplined token system with computed contrast.

**Calm Ledger (`micro-visual-product-concept-002`).** A typographic statement page: one 34px hero figure answering «وين الكاش؟» in the first 88–96px, subject-right/amount-left row grammar mirroring the paper دفتر, radius 0/4/12, two elevation levels, a fixed 88px tabular amount column, a bidi digit-isolation contract, and the strictest arithmetic calm budget of the cycle. It wrapped this in a **desktop review console** — a grid layout with a 340px control sidebar, contrast legend, and scaled preview thumbnails of the losing directions.

**The shared failure is categorical, not cosmetic.** Both artifacts render a web composition inside a phone-shaped box: a scrollable page read like an article or statement, with a simulated device frame, and (in -002) a laptop-width control panel around it. Navigation is CSS visibility switching between pre-rendered page sections. There is no navigation stack, no push/pop with back affordances, no bottom-sheet system with drag behavior, no keyboard-aware forms, no predictable per-screen scroll ownership, no one-handed reach reasoning, and no platform-aware behavior. The owner's verdict — "this looks like a web page assembled by code, not a serious native mobile product" — is therefore **accepted as final and correct for both directions**. Their useful lessons (Section 4 of `00-previous-work-lessons.md`) are retained as behaviors and principles; their visual language, composition, and internal scores are not.

Both prior deliveries are explicitly **not** approved: their Stage 3 review requests never received an owner approval decision in the repository record, and this brief independently rejects them. No Stage 4 work (files `05`–`16`, `approved-native-concept/`) exists and none will be started from either delivery.

## 3. The three named source packages

`micro-agent-input.zip`, `micro-recovery-docs.zip`, and `MicroPrimitives-anti-reference.html` are **absent** from the repository (verified by full-repo listing and extension search today; consistent with both prior intake reports). Nothing about their contents is invented. Their relevant decisions, as summarized in the repository reports and this brief, are treated as reported evidence, and the absence is documented rather than papered over.

## 4. Fixed identity constraints adopted verbatim

- Existing Micro logo: fixed, used with restraint, never redesigned, never mechanically repeated as tiles/buttons/decoration.
- Terracotta palette: exact hex values for both themes as given in the brief (light primary `#cc785c`, pressed `#b4613f`, text `#964e33`, soft `#f4e4db`, accent `#079fa0`/`#057b7c`/`#e3f5f5`; dark primary `#d59172`, pressed `#cc785c`, text `#8fd5d6`, soft `#332d27`, accent `#5ec0c1`/`#8fd5d6`/`#332d27`). Not called "brown", not re-invented.
- Semantic application per measured evidence: light `#cc785c` is atmosphere/surface only; `#964e33` is the justified high-contrast action/text role; `#b4613f` is press-only; dark roles deliberate, not mechanical inversion.
- State distinctness: focus, loading, disabled, success, danger, warning, estimated, pending, unknown, offline, syncing, synced, conflict, cancelled, reversed, correction — all semantically distinct, never color-only.
- Arabic RTL first; English LTR as verification; JOD currency (two decimals per the verified product corpus); `DD/MM/YYYY`; ASCII digits; portrait widths 320/360/390/430; one-handed use; safe areas; realistic Arabic content.
- Jordanian decorative identity postponed: no shemagh, maps, mosaics, stone textures, flags, stars, or national ornaments.
- Micro is not POS, banking/wallet, crypto, or a desktop ERP in a phone — and it is not a web page pretending to be a mobile app.

## 5. Problem definition for this delivery

The problem is not missing CSS, colors, or component names. The problem is a **category error**: the product was composed as a responsive web page and displayed inside a phone frame. The correction is to design Micro as a phone application first, where HTML is only the review medium. A successful direction must demonstrate an app-level information hierarchy with real top-level destinations; a navigation stack with a visible, reliable back path; bottom sheets for short contextual actions; dialogs only for concise consequential decisions; keyboard-aware capture forms; touch-first targets in one-handed reach zones; predictable scroll ownership per screen; platform-aware iOS/Android behavior where they differ; transitions anchored to source and destination; native-feeling loading, saving, error, offline, and sync states; and screen-level composition that no longer resembles a desktop page or review dashboard.

Execution follows the staged plan: Stage 1 runs five specialists (native architecture, art direction, motion, Arabic-RTL financial mobile, adversarial critique) and synthesizes three genuinely different native directions differing in composition, navigation behavior, screen anatomy, and interaction model — not in color. Stage 2 builds three reviewable prototypes with the required screen set and state coverage, with all review controls kept outside the app viewport (URL parameters plus a separate `review-index.html`). Stage 3 stops at the owner review gate: no final handoff files, no production integration, no Stage 4 until one direction is explicitly approved.

The hard rejection criteria from the brief (dashboard-in-a-phone, bezel reliance, card walls, CSS-switch navigation, color-only differentiation, POS/banking/ERP imitation, ornamental motion, report-without-prototype, translation-only RTL, permanently-successful dashboard) are adopted as self-checks before the gate.

---

*Boundary statement: this audit read repository evidence only; it did not inspect the absent packages, did not edit any production code, and did not treat any prior internal score as approval.*
