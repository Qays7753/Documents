# 01 — System Overview and Method

## What Micro is (current `main`, evidence-based)

Micro is an Arabic-first, RTL, mobile-first financial operations prototype for micro and small
businesses and owner-operated projects in Jordan. It is a local-first offline PWA: every
financial fact lives in the device's IndexedDB; there is **no backend, no cloud sync, no
accounts, and no network calls at all** in the client source (verified by searching for
`fetch`, `WebSocket`, `XMLHttpRequest`, `axios`, `supabase`, `firebase` — zero matches in
`apps/prototype-web/client/src`). The app is used by one local actor: the project owner.

**Analysis baseline (read-only):**

| Item | Value |
| --- | --- |
| Repository | https://github.com/Qays7753/Micro (branch `main`) |
| Commit | `4af025d38f04dfb36ee645a4f9ca3345e362bf5b` |
| Commit subject | Merge pull request #158 from Qays7753/agent/final-continuation-contract-reconciliation |
| Commit date | 2026-09-06T13:21:03+03:00 |
| Analysis date | 2026-09-06 (Asia/Amman) |
| Working tree | clean (read-only analysis; no Micro source file was modified) |

Repository state at the analysed commit: local schema version **35**,
export envelope **27** (format `micro-prototype-local-export`),
IndexedDB database `micro-prototype-local` with **32** object stores,
**52** page components over **44** route patterns,
**4** bottom tabs + a central FAB with **5** quick actions,
**14** pure domain modules, **53** application
service files, **125** prototype/DOM test files and **23**
domain test files, **17** financial event types, **10**
order statuses, and a CI lint warning ceiling of **37**
(`package.json` → `eslint src tests apps/prototype-web/client/src --max-warnings 37`).

## Architecture layers (traced)

1. **UI layer** — React 19 + wouter router, Tailwind 4 design tokens, RTL Arabic surfaces
   (`apps/prototype-web/client/src/pages`, `components`, `app/MicroRouter.tsx`).
   UI never touches storage: ESLint forbids `@/storage/local/*` imports from `pages/**` and
   `components/**` (`eslint.config.js`).
2. **Application services** — `apps/prototype-web/client/src/application/**` (53 files): one
   boundary per domain capability; every write idempotent and committed atomically through the
   store port. Application/storage layers are banned from importing React.
3. **Domain core** — `src/domain/**` (14 modules, pure TypeScript): state machines, policies,
   money math in JOD minor units (integer piastres), quantities in milli (1.000 = 1000),
   local dates in Asia/Amman. Raw `Math.round`/`Math.floor` are banned in domain code except
   shared helpers (ESLint rule).
4. **Persistence** — `apps/prototype-web/client/src/storage/local/IndexedDbLocalStore.ts`
   (3,495 lines) implementing the `PrototypeLocalStore` port; `MemoryLocalStore` exists for
   tests only. One open per fan-out; cross-tab freshness via `BroadcastChannel("micro-data-changed")`.
5. **PWA shell** — vite-plugin-pwa with `registerType: "prompt"`, precache + SPA fallback,
   no runtime caching; updates require owner approval and never reload over dirty forms.

## The five financial boundaries (verified invariants)

The atlas is organised around the five boundaries that cut across every contract, test, and
screen in this repository:

1. **Collection is not profit** — cash in never re-recognizes revenue.
2. **Debt is not cash** — receivables are tracked separately from collected money.
3. **Purchase is not COGS/expense** — supplier purchases affect cash/payables until consumption.
4. **Owner money is separate** — withdrawals/investments are never expenses/revenue.
5. **Unknown is never zero** — missing cost/knowledge yields `null`/«غير متاح», displayed honestly.

## Method

- Repository-first evidence: every claim in this atlas carries a file path with line reference
  or a test name. External UX references were never used as evidence of a Micro feature.
- The analysis cloned `main` at the commit above and did not modify any Micro source file,
  test, fixture, workflow, contract, or documentation (task constraint honored).
- Status vocabulary (fixed): `IMPLEMENTED`, `PARTIALLY_IMPLEMENTED`, `PLANNED_OR_CONCEPTUAL`,
  `NOT_FOUND`, `CONFLICTING`, `UNVERIFIABLE_FROM_REPOSITORY`. A recommendation never becomes a
  current-state fact: future content is quarantined in the future-state sections of the atlas.
- Cross-checking: automated exploration of routes/screens/services/domain/storage/CI/docs/tests,
  followed by direct verification of the load-bearing facts (state machine, event types, delta
  table, schema versions, key labels) by reading the cited files.

## Scope boundaries of this document

This package documents **the current product surface as-is**. The network expansion (market,
delivery companies, moderation, identity), POS, sync, and any AI decisioning are future state
and are documented as `PLANNED_OR_CONCEPTUAL` with their contract references only
(see `09-gaps-conflicts-and-recommendations-en.md` and the future-state diagram DGM-26).

## Deliverable inventory

| File | Content |
| --- | --- |
| `README.md` | Package overview and usage |
| `INDEX.md` | Full index of stable IDs |
| `metadata.yml` | Machine-readable metadata |
| `01..10-*-en.md` | Analytical reports (this file is 01) |
| `micro-user-flow-atlas.html` | Arabic RTL interactive atlas (offline, self-contained) |
| `micro-user-flow-atlas-data.json` | Structured data (all arrays, stable IDs) |
