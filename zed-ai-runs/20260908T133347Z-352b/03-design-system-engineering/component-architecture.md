# Micro — Component Architecture & Token Hierarchy

**Run:** 20260908T133347Z-352b · **Agent:** 03 (Design-System Engineering) · **Task:** 2-c
**Scope:** Arabic-first RTL, phone-only (320 / 360 / 390 / 430 px), light-mode-only financial/operational component library for Jordanian small businesses. Currency is always **"د.أ"** — never "JOD". Digits are English (Latin), bidi-isolated, and tabular.

---

## 1 · Scope & Engineering Constraints

The target repository is documents-only with no code stack, so the lab itself must remain framework-neutral vanilla CSS/HTML/JS; nevertheless the architecture is authored so that every artifact survives extraction into a real product stack without translation. Three constraints drive every decision below. First, **light mode only**: no `.dark` class, no `prefers-color-scheme` query, no theme switch will ever be authored — the token set is closed and single-mode. Second, **exact token values**: every color, spacing step, radius, type role, duration and easing comes verbatim from the Micro token spec; nothing is rounded, re-derived or invented, and any raw value that appears outside `tokens.css` is a bug by definition. Third, **RTL-first**: the layout assumes `dir="rtl" lang="ar"` from the root down; LTR is never the reference implementation, only a mirrored degenerate case. The typography stack is IBM Plex Sans Arabic 400/500/600 with Noto Sans Arabic fallback, and all numerals render with `font-variant-numeric: tabular-nums lining-nums` so columns of Latin digits inside Arabic sentences stay aligned. Motion is deliberately austere — no bounce, no springs, no count-up animations; values always render at their final state immediately.

## 2 · Token Hierarchy: Primitive → Semantic → Component

The system has exactly three layers, and value authority flows strictly downward. **Primitives** are the raw values — hex colors, the `2/4/8/12/16/24/32/40` px spacing scale, radii, type roles, millisecond durations and the two easing curves — documented as the spec source inside `tokens.css`. **Semantic tokens** are the `:root` custom properties themselves (`--canvas`, `--surface`, `--sunken`, `--ink-*`, `--line-*`, `--brand-*`, `--positive*`, `--danger*`, `--warning*`, `--info*`, `--scrim`, `--press-overlay`); they answer *what a value means*, never *where it is used*. **Component-level tokens** are private locals declared inside a component block using the `--_` prefix (`.mc-btn { --_bg: var(--brand-atmosphere); }`), which may only reference semantic tokens or other locals of the same component. This is what makes extraction lossless: deleting or copying a component stylesheet can never orphan a raw value.

One structural decision deserves emphasis: the palette enforces a **role split between fill and text usage of the brand colors**. `--brand-atmosphere` (#CC785C) measures ≈3.1:1 against `--canvas` — sufficient for non-text surfaces (fills, indicators, chart series ≥3:1) but never for body-size text. `--brand-ink` (#964E33) measures ≈6:1 on canvas and is therefore the brand *text* color (quiet-text buttons, links, active navigation labels). The same measurement discipline produced two more rules: `--positive` text on `--positive-tint` measures 4.28:1 (below the 4.5:1 AA threshold), so positive chips pair a positive *icon* with `--ink` text, while danger (5.5:1), warning (4.5:1) and info (5.9:1) pairs may carry colored text. And `--on-brand` white on `--brand-atmosphere` measures ≈3.3:1 — the spec mandates this pairing for primary buttons, so it is kept but flagged to Agent 04; a compliant alternative exists (`--ink-strong` on atmosphere ≈5.0:1) if the accessibility review requires it.

Type carries a verification hook: every font-size token is written `calc(px * var(--text-scale))` with `--text-scale: 1` as default, and line-heights are unitless. At scale 1 extraction yields the exact spec pixels (32px stays 32px); the lab sets `--text-scale: 1.3` / `2` on `<html data-text-scale>` to verify 130% and 200% behavior — no clipping, preserved hit areas, and no Arabic-script text below the 14px floor at the active scale. The 13px qualifier role is reserved for digit runs, Latin and unit marks; the currency mark "د.أ" is Arabic script and is never rendered below 14px.

## 3 · Naming Conventions & State Grammar

Component classes are BEM-ish with an `.mc-` (Micro component) prefix: block (`.mc-btn`), element (`.mc-btn__label`, `.mc-oprow__amount`), modifier (`.mc-btn--primary`, `.mc-input--search`). Variants — the *kind* of thing — use modifier classes. **States — the *condition* of a thing — never use classes**; they are expressed orthogonally through data-attributes and ARIA: `[data-state="loading"]`, `[data-state="completed"]`, `[data-pressed]` (touch feedback), `[aria-disabled="true"]`, `[aria-invalid="true"]`, `[aria-expanded="true"]`, `[data-state="open"|"closed"|"opening"|"closing"]` for overlays. This grammar keeps CSS selectors composable (a loading *destructive* button is simply both selectors), keeps React prop→DOM mapping trivial, and keeps the final HTML self-documenting for review. Directional icons use the `.icon-mirror` registry (see §6). Numbers embedded in Arabic sentences are wrapped in `<bdi>` (or rely on `unicode-bidi: isolate`), which the lab applies to every amount, percentage and date. Classes never encode direction (`-rtl` suffixes are forbidden); `[dir="rtl"]` appears only in the icon registry and, if ever needed, in the one documented exception list.

## 4 · Component Families & Structural API

**QuickActionRail** — horizontal, natively-scrollable action strip pinned to the screen edges. Tiles are exactly **88×92 px** with a **24 px** icon and a **13 px** label (digit-safe only; Arabic labels at 14px minimum), arranged with **8 px** gap and **16 px** edge padding (`--space-edge`). `scroll-snap-type: x mandatory` with `scroll-snap-align: start` (logical — snaps to the right edge in RTL), plus a both-edges fade via `mask-image: linear-gradient(...)` so direction never matters. Tiles use `--surface` on `--canvas`, radius `--radius-md`, pressed veil `--press-overlay` at `--dur-press`.

**PrimaryValueBlock** — the hero number, set **on canvas** (never on a card): 32px/600/1.15 (`--text-value-*`) in `--ink-strong`, tabular + `<bdi>`, currency "د.أ" as a `--ink-muted` qualifier inline-end, a text-only delta chip in `--positive` / `--danger` (text-on-canvas passes AA; no tinted background), and a 13→14px eyebrow label. No count-up: the final value renders immediately.

**MetricGroup** — one `--surface` card, radius `--radius-lg`, 16px padding, containing aligned **MetricRows** laid out on a shared grid (`grid-template-columns: auto 1fr auto`, which mirrors automatically in RTL): label 15/`--ink`, qualifier 13/`--ink-subtle`, value 15/500 tabular `--ink-strong`, rows separated by 1px `--line-soft`. Alignment across rows is a property of the group, not of each row — that is the point of the family.

**OperationalRow** — anatomy: leading 24px status icon in a 40×40 tinted chip (`--info-tint`, `--positive-tint`, …) → title 15/`--ink` + qualifier 13/`--ink-muted` → trailing amount 15/500 tabular with signed `<bdi>` → 16px chevron from the mirror registry in `--ink-subtle`. Height ≥ `--touch-primary`, pressed veil, dividers `--line-soft`.

**Button** — variants primary (`--brand-atmosphere`/`--on-brand`), secondary (`--surface`, 1px `--line-strong`, `--ink`), quiet-text (transparent, `--brand-ink` text), destructive (`--danger`/`--on-brand`), icon-only (48×48, 24px glyph, `aria-label` mandatory). Height `--touch-primary`, radius `--radius-md`, label 15/500. Pressed = `--press-overlay` veil at `--dur-press` (no scale, no bounce). Loading swaps the label slot for a spinner with width locked and `aria-busy="true"`. Disabled = `--sunken`/`--ink-disabled`, out of tab order. Quiet-completion flips to `--positive` semantics at `--dur-normal`.

**Input** — field group: label 15/`--ink` above a 48px control (`--surface`, 1px `--line-strong`, radius `--radius-md`), helper 13/`--ink-muted` below. Variants: text, amount (`inputmode="decimal"`, tabular, "د.أ" suffix outside the LTR digit run), search (icon + 44px clear button), date, selection (trigger + sheet-hosted `role="listbox"`), segmented (sunken track, surface active pill, `--dur-fast`), tab (2px `--brand-atmosphere` underline), checkbox and switch (44px hit areas; "on" fill `--brand-atmosphere` ≥3:1 non-text). Error = `--danger` border + helper + `aria-invalid`; focus = `--brand-atmosphere` border plus the standard ring (§7).

**State** — one component, ten statuses: empty, loading, error, offline-local-save, pending, conflict, failed, completed, cancelled, reversed. Tinted container + 16px status icon + 13/14px message, `aria-live="polite"`. Reversed renders amounts with `line-through` in `--ink-subtle`.

**Sheet / Dialog** — sheet: bottom-anchored, `--surface`, top corners `--radius-lg`, slides `--dur-sheet-in` / `--dur-sheet-out`; dialog: centered, `--radius-lg` all corners, scale+fade `--dur-dialog-in` / `--dur-dialog-out`; both over a `--scrim` fading at `--dur-scrim`, with `--z-scrim-sheet: 250` / `--z-sheet: 300` / `--z-scrim-dialog: 350` / `--z-dialog: 400`, focus trap while open, **focus returned to the trigger on close** (JS stores `document.activeElement` at open).

**BottomNavigation** — fixed, full-width, **radius 0 (edge-to-edge)**, `--surface` with 1px `--line-soft` top border, `--z-nav`, `env(safe-area-inset-bottom)` padding; items ≥48px with 24px icon + 13→14px label; active in `--brand-ink`, inactive `--ink-muted`.

**Chart primitives** — bar/line/donut built from token colors (`--line-soft` grid, `--brand-atmosphere` series, `--positive`/`--danger` semantics), static values (never count-up), each chart is `role="img"` with an `aria-label` summary and `aria-describedby` pointing at a real data table that carries the same numbers as text.

## 5 · Vanilla Lab → React/TypeScript Adapter Mapping

The vanilla lab *is* the reference implementation; React adapters are mechanical projections of the same CSS, because state already lives in data-attributes. A component library would copy `tokens.css` + `components/*.css` verbatim and map props to classes/attributes:

| React prop | Type | CSS hook emitted |
| --- | --- | --- |
| `variant` | `"primary" \| "secondary" \| "quiet" \| "destructive" \| "icon"` | `mc-btn--{variant}` |
| `loading` | `boolean` | `data-state="loading"` + `aria-busy="true"` |
| `disabled` | `boolean` | `aria-disabled="true"` (out of tab order) |
| `invalid` | `boolean` | `aria-invalid="true"` + `mc-input--error` helper |
| `completion` | `boolean` (quiet) | `data-state="completed"` |
| `status` | State family union | `mc-state--{status}` |
| `open` / `onOpenChange` | overlay | `data-state="open"…"closing"` + focus return |
| `icon` / `mirror` | registry name | `<svg class="mc-icon icon-mirror">` |
| press handlers | touch | `data-pressed` during `pointerdown→up` |

`onClick` → press semantics, `onPressStart`/`onPressEnd` → `data-pressed`, and every amount child is already `<bdi>`-wrapped. The Tailwind v4 theme file (`tailwind-v4-theme.css`) is the optional bridge for a Next.js future; the lab itself never imports it, which keeps the two stacks provably token-identical rather than accidentally identical.

## 6 · RTL Strategy

The page declares `<html dir="rtl" lang="ar">`, and layout is written exclusively with **logical properties**: `margin-inline-start`, `padding-inline`, `inset-inline-end`, `border-inline-start`, `text-align: start`, `inline-size`. Flexbox and CSS grid mirror themselves under `direction`, so no row or column ever needs a direction-specific rule; scroll containers and `scroll-snap-align: start` likewise resolve to the leading (right) edge in RTL. Physical properties (`left`, `right`, `text-align: right`) are forbidden outside the documented exception list — currently empty. Directional *glyphs* are the only things that flip, governed by an **icon-mirror registry**: `.icon-mirror { }` is inert by default and becomes `transform: scaleX(-1)` **only under `[dir="rtl"]`**. Registered: back/next chevrons, progress arrows, "external/open" arrows, list disclosure chevrons, breadcrumb separators. Explicitly *not* mirrored: numerals, checkmarks, plus/minus, media transport controls, brand marks, clocks, charts. Mixed-direction text (Latin digits, ISO dates, amounts) is isolated with `<bdi>` or `unicode-bidi: isolate` so Arabic sentence flow is never broken by an LTR run; amounts keep `dir="ltr"` internally with alignment to the inline end.

## 7 · Accessibility Hooks

Focus is keyboard-visible everywhere: a single global rule draws `outline: 2px solid var(--brand-ink); outline-offset: 2px` on `:focus-visible` (≈6:1 on canvas — chosen over `--brand-atmosphere` at ≈3.1:1 for headroom at 200% zoom); it is never removed, only never triggered by touch. Roles: `role="dialog"` + `aria-modal="true"` + `aria-labelledby` for sheet/dialog, `role="listbox"`/`option` for selection, `role="radiogroup"` for segmented, `role="tablist"`/`tab`/`tabpanel` for tabs, `role="switch"` + `aria-checked` for switches, `role="img"` + `aria-label` + `aria-describedby` (data table) for charts. Live semantics: `aria-live="polite"` on the State family and quiet-completion feedback; `aria-busy="true"` on loading controls. Every numeric value is `<bdi>`-isolated; hit areas are ≥ `--touch-min` 44px with `--touch-gap` 8px separation. One recommendation is deliberately left open for Agent 04: adding `@media (prefers-reduced-motion: reduce)` to collapse durations — it does not violate the no-dark-mode/no-theme constraints (it concerns motion, not color), but the policy call belongs to the accessibility review.

## 8 · Extraction Folder Structure

```
micro-design-system/
├── tokens.css                  # canonical semantic layer (this run)
├── base.css                    # reset, font-face hookup, focus ring, icon-mirror
├── tailwind-v4-theme.css       # OPTIONAL Next.js/Tailwind v4 adapter
├── fonts/ + fonts.css          # IBM Plex Sans Arabic 400/500/600 (woff2 subsets)
└── components/
    ├── quick-action-rail.css   # .mc-rail, .mc-rail__tile (88×92, snap, edge fade)
    ├── primary-value-block.css # .mc-value (32px hero number on canvas)
    ├── metric-group.css        # .mc-metrics, .mc-metric-row (aligned grid)
    ├── operational-row.css     # .mc-oprow anatomy
    ├── button.css              # .mc-btn + 5 variants × states
    ├── input.css               # .mc-input family (9 controls × states)
    ├── state.css               # .mc-state × 10 statuses
    ├── sheet.css / dialog.css  # overlays, scrim, focus return
    ├── bottom-navigation.css   # edge-to-edge, radius 0
    └── chart.css               # primitives + text alternatives
```

Extraction contract: `tokens.css` + `base.css` + any subset of `components/*.css` is a working system; no component file may declare a raw color, size, duration or easing that does not resolve to a `tokens.css` var, and the `variant-state-matrix.md` documents every combination the lab must demonstrate before extraction is considered proven.
