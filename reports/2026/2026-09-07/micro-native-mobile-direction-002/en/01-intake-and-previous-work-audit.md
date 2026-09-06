# 01 — Intake and Previous-Work Audit

**Delivery:** `micro-native-mobile-direction-002` · Stage 0 · 2026-09-07
**Author:** central orchestrator
**Status:** Stage 0 complete → proceeding to Stage 1 (specialist research). **Stage 4 will not start until the owner explicitly approves one direction at the Stage 3 gate.**

---

## 1. Repository status

- Repository `Qays7753/Documents` cloned on branch `main` at commit `622af98` (HEAD: "docs: add Micro end-to-end user flow atlas"). Working tree clean at intake.
- Repository rules read and adopted (`README.md`, `UPLOAD_GUIDE.md`, `INDEX.md`): deliverables only; dated-folder packages with `metadata.yml` and a folder-level `INDEX.md`; root `INDEX.md` updated **in the same commit** as every upload; next root row numbers start at **38** (rows 1–37 used); no secrets in any file, commit, log, or URL; post-push verification required (ls-remote, file presence, token-leak grep of the diff).
- Access credential handling: supplied token used **transiently** for git operations only; never written to any file, script, log, remote URL, or commit. (No `scripts/push-documents-repo.sh` exists in this workspace; the equivalent transient-credential discipline was applied directly.)

## 2. What was read

| Evidence | Depth |
|---|---|
| `micro-visual-product-concept-001/en/02-research-and-direction-synthesis.md` | full |
| `micro-visual-product-concept-001/en/01-current-work-lessons.md` | full |
| `micro-visual-product-concept-001/supporting/review-evidence/*.png` (incl. `01-today-390-light-ar.png`) | visual inspection |
| `micro-visual-product-concept-002/en/02-research-and-direction-synthesis.md` (token sheet §5.1, decisions DSY-01…DSY-25, open-question register) | full |
| `micro-visual-product-concept-002/en/04-REVIEW-REQUEST.md` | full |
| `micro-visual-product-concept-002/supporting/qa-screenshots/shot-01-home-light-ar.png` (and neighbors) | visual inspection |
| `micro-visual-product-concept-002/metadata.yml` (format template for this delivery) | full |
| Root `README.md`, `UPLOAD_GUIDE.md`, `INDEX.md` | full |

## 3. The verdict on the previous work

**Both previous directions are rejected as final visual directions. The reason is a category error, not a styling error.**

- **Warm Ledger (‑001)** put a *phone-bezel mockup with a fake status bar* on a dark desktop stage and filled the screen with **stacked rounded cards** (offline banner card, tinted hero card, white band cards) plus a caption banner underneath. Whatever the label said, the object was "a poster of an app on a presentation page."
- **Calm Ledger (‑002)** produced the opposite failure with the same root: a **desktop review console** (control strip, demo buttons, annotated comparison columns with spec prose) dominating the viewport, with a framed phone inside it showing a **document-flow composition** — headings, rules, and rows scrolling like a styled article. Typographically disciplined, still not an application.
- **Common root cause, stated precisely:** both deliveries composed **web content** (page sections, cards, document rhythm, review chrome) instead of **application chrome** (top-level destinations, navigation stacks, back behavior, sheets vs dialogs, transitions tied to navigation events, keyboard-aware forms, scroll ownership). The HTML medium leaked into the product. The owner's phrase — "a web page assembled by code" — is the correct diagnosis, and both internal scoreboards (7.90/10, 28/30) failed to predict it because they measured decoration compliance, not *nativeness*.

**What this delivery does with them:** keep their measured decisions and honest-state behaviors (bucket K in `en/00`), adapt their sound principles into native anatomy (bucket A), and hard-reject their visual language — bezels, desktop consoles, card walls, document screens, decorative terracotta (bucket R). Items neither delivery could verify remain open (bucket V).

## 4. Fixed constraint register (authority level 1)

| ID | Constraint |
|---|---|
| C-01 | Micro logo is fixed; used with restraint; never redesigned, never repeated as decoration/cards/tiles |
| C-02 | Terracotta identity fixed. Light: `#cc785c` primary · `#b4613f` pressed · `#964e33` text · `#f4e4db` soft; accent `#079fa0` / `#057b7c` / `#e3f5f5`. Dark: `#d59172` primary · `#cc785c` pressed · `#8fd5d6` text · `#332d27` soft; accent `#5ec0c1` / `#8fd5d6` / `#332d27`. Never renamed "brown", never re-valued |
| C-03 | Measured semantic rules: `#cc785c` = atmosphere/surface role, **white text on it is not permitted** where contrast fails (measured 3.28:1); `#964e33` = high-contrast action role; `#b4613f` = press-only (≈4.45:1 with white — never reported as a pass); dark roles deliberate, never mechanical inversion |
| C-04 | States kept semantically distinct: focus, loading, disabled, success, danger, warning, estimated, pending, unknown, offline, syncing, synced, conflict, cancelled, reversed, correction — never color-alone |
| C-05 | Arabic RTL first; English LTR verification; realistic Arabic content; ASCII digits unless the owner decides otherwise; JOD; `DD/MM/YYYY` |
| C-06 | Portrait widths 320/360/390/430; one-handed use; safe areas; touch-first targets |
| C-07 | Jordanian decorative identity postponed — no shemagh, maps, mosaics, stone, flags, stars, ornaments |
| C-08 | Micro is not POS, banking/wallet, crypto, desktop-ERP-in-a-phone, or a generic SaaS dashboard |

## 5. Problem statement for this delivery

Design Micro's **native mobile visual product concept**: three genuinely different, genuinely native directions — different in navigation model, screen anatomy, composition grammar, and interaction model, not three recolorings — evaluated as application screens first, with all review apparatus separated from the product surface. The success condition is the owner opening a prototype and feeling: **"this finally feels like a serious native mobile product, not a web page assembled by code."**

## 6. Method and staged plan

- **Stage 0 (this file + `en/00`):** intake, audit, problem definition. Production codebase untouched.
- **Stage 1:** five specialist reports (`subagents/01…05`) run in parallel; the central orchestrator alone decides and writes `en/02-native-direction-synthesis.md` recommending one direction — **not finalized**.
- **Stage 2:** three separate app-like prototypes (`prototype/direction-a|b|c/`, each a self-contained HTML application screen experience) plus `prototype/review-index.html`. Product UI contains no review controls; the review index and a small out-of-frame review toolbar carry the apparatus. Screens cover the owner's full surface set; states are honest; motion follows the register; 320-first verification.
- **Stage 3 (hard stop):** `en/03-native-prototype-review-guide.md` + `en/04-REVIEW-REQUEST.md`. No Stage 4 files, no production integration, no finalization until the owner explicitly approves one direction or returns focused rejection feedback.

## 7. Scope boundaries

- No production Micro codebase is read as a build baseline or modified; the delivery is design evidence for a later integration agent.
- Prototypes are front-of-the-screen only: in-memory demo data, simulated sync/save, no backend.
- All previous deliveries' scores, rankings, and "ready" claims are inert here; this delivery re-argues everything from evidence.

## 8. Missing sources

`micro-agent-input.zip`, `micro-recovery-docs.zip`, and `MicroPrimitives-anti-reference.html` are **absent** from the repository (repo-wide search, 2026-09-07). Documented, not invented; identical to the absence recorded by both previous deliveries. Grounding comes from the fixed constraint block (authority level 1) and the repository's own reports.
