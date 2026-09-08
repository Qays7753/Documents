# Micro — Variant × State Matrix

**Run:** 20260908T133347Z-352b · **Agent:** 03 (Design-System Engineering) · **Task:** 2-c

## How to read this document

This matrix is the contract between the token layer (`tokens.css`), the architecture (`component-architecture.md`) and the final lab build: every cell names the exact tokens a variant consumes in a given state, so the build can be verified cell-by-cell and extraction can be proven complete. **States are data-attributes, never classes**: `default` is the resting DOM; `pressed` is `:active` plus `[data-pressed]` (held from `pointerdown` to `pointerup` for touch feedback); `focused` means `:focus-visible` only (mouse/touch clicks never draw the ring); `loading` is `[data-state="loading"]` with `aria-busy="true"`; `disabled` is `[aria-disabled="true"]` with the element removed from tab order (never a bare `disabled` attribute on custom controls, so semantics stay reviewable); `error` is `[aria-invalid="true"]`. The focus ring is global and identical everywhere: `outline: 2px solid var(--brand-ink); outline-offset: 2px` — chosen over `--brand-atmosphere` because it measures ≈6:1 on `--canvas` versus ≈3.1:1, giving non-text contrast headroom at 200% zoom. Pressed feedback is always the `--press-overlay` veil at `--dur-press` (80 ms) — no scale transforms, no bounce, ever. The **Demonstrated in** column is **PLANNED** for every row by design; the final lab build fills it with the actual section/anchor where each cell is shown, and any cell left unfilled at review time is a gap, not an omission. Where a cell is genuinely not applicable (e.g. quiet-completion on a destructive button), the row states the routing rule instead of staying silent.

State tokens used throughout, defined once: `--dur-press: 80ms`, `--dur-fast: 120ms`, `--dur-normal: 200ms`, `--ease-standard: cubic-bezier(0.2,0,0,1)`, `--ease-exit: cubic-bezier(0.4,0,1,1)`, `--touch-min: 44px`, `--touch-primary: 48px`.

---

## 1 · Button family — full matrix (5 variants × 6 states)

Shared anatomy: height `var(--touch-primary)` (48px; icon-only 48×48), radius `var(--radius-md)`, padding-inline `var(--space-16)`, label `var(--text-label-size)`/`var(--weight-medium)`/`var(--text-label-line-height)`, transition `var(--dur-fast) var(--ease-standard)`. Loading swaps the label slot for a spinner with the button's width locked (no layout shift). Quiet-completion is a save/confirm feedback state at `var(--dur-normal)`.

| Variant | State | Styling (tokens) | Behaviour / a11y | Demonstrated in |
| --- | --- | --- | --- | --- |
| primary | default | bg `--brand-atmosphere`; color `--on-brand`; label 15/500 | `role="button"`; ≥48px hit | PLANNED |
| primary | pressed | `--press-overlay` veil via `::before`, opacity 1, `--dur-press` | `:active` + `[data-pressed]` | PLANNED |
| primary | focused | ring: outline 2px `--brand-ink`, offset 2px (ring sits on canvas) | `:focus-visible` only | PLANNED |
| primary | loading | bg unchanged; spinner in `--on-brand`; width locked | `[data-state="loading"]`, `aria-busy="true"`, no press | PLANNED |
| primary | disabled | bg `--sunken`; color `--ink-disabled`; no veil | `[aria-disabled="true"]`, out of tab order | PLANNED |
| primary | quiet-completion | bg `--positive`; color `--on-brand`; check 16 + "تم الحفظ" | `[data-state="completed"]`, `aria-live="polite"`, `--dur-normal` crossfade | PLANNED |
| secondary | default | bg `--surface`; border 1px `--line-strong`; color `--ink` | same base anatomy | PLANNED |
| secondary | pressed | `--press-overlay` veil, `--dur-press` | `:active` + `[data-pressed]` | PLANNED |
| secondary | focused | outline 2px `--brand-ink`, offset 2px | `:focus-visible` only | PLANNED |
| secondary | loading | border + bg unchanged; spinner `--ink`; width locked | `aria-busy="true"` | PLANNED |
| secondary | disabled | bg `--sunken`; border `--line-soft`; color `--ink-disabled` | `[aria-disabled="true"]` | PLANNED |
| secondary | quiet-completion | border `--positive`; bg `--positive-tint`; color `--ink` + check 16 `--positive` | `[data-state="completed"]`, `--dur-normal` | PLANNED |
| quiet-text | default | bg transparent; color `--brand-ink` (≈6:1 on canvas) | inline; padding-inline `--space-8`, hit ≥44px | PLANNED |
| quiet-text | pressed | `--press-overlay` veil, `--dur-press` | `:active` + `[data-pressed]` | PLANNED |
| quiet-text | focused | outline 2px `--brand-ink`, offset 2px | `:focus-visible` only | PLANNED |
| quiet-text | loading | text hidden, slot swaps to 16px spinner `--brand-ink` | `aria-busy="true"`; label kept for width | PLANNED |
| quiet-text | disabled | color `--ink-disabled`; no underline | `[aria-disabled="true"]` | PLANNED |
| quiet-text | quiet-completion | color `--positive`; check 16 appears inline-start of label | canonical case; `aria-live="polite"`, `--dur-normal` | PLANNED |
| destructive | default | bg `--danger`; color `--on-brand` (6.6:1) | used for delete/void confirm | PLANNED |
| destructive | pressed | `--press-overlay` veil, `--dur-press` | `:active` + `[data-pressed]` | PLANNED |
| destructive | focused | outline 2px `--brand-ink`, offset 2px | `:focus-visible` only | PLANNED |
| destructive | loading | bg unchanged; spinner `--on-brand`; width locked | `aria-busy="true"` | PLANNED |
| destructive | disabled | bg `--sunken`; color `--ink-disabled` | `[aria-disabled="true"]` | PLANNED |
| destructive | quiet-completion | **N/A** — destructive outcomes route through Dialog confirm + State chip (`--danger-tint`), never inline completion | routing rule documented | PLANNED |
| icon-only | default | 48×48; radius `--radius-md`; 24px glyph `--ink` (or variant colors) | `aria-label` mandatory; no visible text | PLANNED |
| icon-only | pressed | `--press-overlay` veil, `--dur-press` | `:active` + `[data-pressed]` | PLANNED |
| icon-only | focused | outline 2px `--brand-ink`, offset 2px | `:focus-visible` only | PLANNED |
| icon-only | loading | glyph swaps to spinner `--ink`; 48×48 locked | `aria-busy="true"` | PLANNED |
| icon-only | disabled | glyph `--ink-disabled`; bg transparent | `[aria-disabled="true"]` | PLANNED |
| icon-only | quiet-completion | glyph swaps to filled check `--positive`, `--dur-normal` | `[data-state="completed"]` | PLANNED |

---

## 2 · Input family — full matrix (9 controls × 4 states)

Shared field anatomy: label 15/400 `--ink` above; control height `var(--touch-primary)`; bg `--surface`; border 1px `--line-strong`; radius `var(--radius-md)`; helper 13 `--ink-muted` below (≥14px if Arabic script). Error helper: 13 `--danger` + 16px icon, `aria-describedby`. All amount digits render LTR, `<bdi>`-isolated, `font-variant-numeric: var(--numeric-variant)`, currency "د.أ" (never "JOD") placed outside the digit run.

| Control | State | Styling (tokens) | Behaviour / a11y | Demonstrated in |
| --- | --- | --- | --- | --- |
| text | default | bg `--surface`; border 1px `--line-strong`; text 15 `--ink` | label bound via `<label for>` | PLANNED |
| text | focus | border `--brand-atmosphere` + global ring 2px `--brand-ink` offset 2 | `:focus-within` on field group | PLANNED |
| text | error | border `--danger`; helper 13 `--danger` | `aria-invalid="true"`, `aria-describedby` | PLANNED |
| text | disabled | bg `--sunken`; border `--line-soft`; text/placeholder `--ink-disabled` | `[aria-disabled="true"]`, read-only presentation | PLANNED |
| amount | default | as text + suffix "د.أ" qualifier 13/`--ink-muted`; tabular lining digits | `inputmode="decimal"`; digits `<bdi>` LTR | PLANNED |
| amount | focus | as text focus | `:focus-within` + ring | PLANNED |
| amount | error | border `--danger`; helper 13 `--danger` (e.g. "المبلغ مطلوب") | `aria-invalid="true"` | PLANNED |
| amount | disabled | as text disabled | `[aria-disabled="true"]` | PLANNED |
| search | default | leading 20px icon `--ink-muted`; trailing clear button ≥44px hit | `type="search"`; clear `aria-label="مسح"` | PLANNED |
| search | focus | as text focus | `:focus-within` + ring | PLANNED |
| search | error | border `--danger` (rare: search validation) | `aria-invalid="true"` | PLANNED |
| search | disabled | as text disabled; clear hidden | `[aria-disabled="true"]` | PLANNED |
| date | default | as text + trailing calendar glyph 20 `--ink-muted` (not mirrored) | `inputmode` none; value `<bdi>` | PLANNED |
| date | focus | as text focus | `:focus-within` + ring | PLANNED |
| date | error | border `--danger`; helper (e.g. "التاريخ خارج النطاق") | `aria-invalid="true"` | PLANNED |
| date | disabled | as text disabled | `[aria-disabled="true"]` | PLANNED |
| selection | default | trigger styled as field + chevron 16 (mirror registry) `--ink-subtle` | opens Sheet `role="listbox"`; `aria-haspopup="listbox"`, `aria-expanded` | PLANNED |
| selection | focus | as text focus | `:focus-visible` on trigger | PLANNED |
| selection | error | border `--danger`; helper 13 `--danger` | `aria-invalid="true"` | PLANNED |
| selection | disabled | as text disabled | `[aria-disabled="true"]` | PLANNED |
| segmented | default | track bg `--sunken` radius `--radius-md`; active pill bg `--surface` + text `--ink-strong`; inactive text `--ink-muted` | `role="radiogroup"` / `role="radio"` `aria-checked` | PLANNED |
| segmented | focus | ring 2px `--brand-ink` on the focused segment | `:focus-visible` | PLANNED |
| segmented | error | 2px `--danger` outline on the group | `aria-invalid="true"` (required selection) | PLANNED |
| segmented | disabled | track `--line-soft`; text `--ink-disabled` | `[aria-disabled="true"]` | PLANNED |
| tab | default | text 15/400 `--ink-muted`; active: `--ink-strong`/500 + 2px `--brand-atmosphere` underline (3.1:1 non-text) | `role="tablist"`/`tab`/`tabpanel`; scroll-snap row | PLANNED |
| tab | focus | ring 2px `--brand-ink` on tab | `:focus-visible`; roving tabindex | PLANNED |
| tab | error | 6px dot `--danger` at tab corner (content error indicator) | `aria-invalid` surfaced via tabpanel | PLANNED |
| tab | disabled | text `--ink-disabled`; no underline; not focusable | `[aria-disabled="true"]` | PLANNED |
| checkbox | default | box 20×20 (44px hit via label); radius `--radius-sm`; border 1px `--line-strong`; unchecked bg `--surface` | `role="checkbox"`/native + `aria-checked` | PLANNED |
| checkbox | focus | ring 2px `--brand-ink` around box | `:focus-visible` | PLANNED |
| checkbox | error | border `--danger` + helper 13 `--danger` | `aria-invalid="true"` | PLANNED |
| checkbox | disabled | box bg `--sunken`; border `--line-soft`; check `--ink-disabled` | `[aria-disabled="true"]` | PLANNED |
| checkbox | checked (ref) | fill `--brand-atmosphere` (≥3:1 non-text); check glyph `--on-brand` | `aria-checked="true"`; swap at `--dur-fast` | PLANNED |
| switch | default | track 44×24 radius `--radius-full`; off `--ink-disabled` fill; thumb `--surface` w/ soft shadow `--press-overlay` | `role="switch"` `aria-checked` | PLANNED |
| switch | focus | ring 2px `--brand-ink` | `:focus-visible` | PLANNED |
| switch | error | 2px `--danger` outline + helper | `aria-invalid="true"` | PLANNED |
| switch | disabled | track `--line-soft`; thumb `--ink-disabled` | `[aria-disabled="true"]` | PLANNED |
| switch | on (ref) | track fill `--brand-atmosphere`; thumb `--on-brand` | thumb slides `--dur-fast` `--ease-standard` | PLANNED |

---

## 3 · State family (10 statuses)

One component, `.mc-state--{status}`: tinted container (radius `--radius-md`, padding 12/16) + 16px status icon + message 13 (14px floor for Arabic script), `aria-live="polite"`. Positive chips pair a `--positive` icon with `--ink` text (measured 4.28:1 for positive-on-tint — below AA); danger/warning/info pairs carry colored text (5.5:1 / 4.5:1 / 5.9:1). Enter: fade+slide `--dur-normal` `--ease-standard`. No looping animations except the loading spinner.

| Status | Container | Icon | Text | Semantics (Arabic label) | Demonstrated in |
| --- | --- | --- | --- | --- | --- |
| empty | transparent | 24 `--ink-subtle` | 15 `--ink-muted` + 13 hint | "لا توجد بيانات بعد" | PLANNED |
| loading | `--sunken` | spinner `--ink-muted` | 13 `--ink-muted` | "جارٍ التحميل…" + `aria-busy` | PLANNED |
| error | `--danger-tint` | 16 `--danger` | 13 `--danger` | "تعذّر إتمام العملية" | PLANNED |
| offline-local-save | `--warning-tint` | 16 `--warning` | 13 `--ink` | "محفوظ محلياً — سيُزامن عند الاتصال" | PLANNED |
| pending | `--info-tint` | 16 `--info` | 13 `--ink` | "قيد المعالجة" | PLANNED |
| conflict | `--warning-tint` | 16 `--warning` | 13 `--ink` + quiet resolve action | "تعارض في البيانات" → resolve sheet | PLANNED |
| failed | `--danger-tint` | 16 `--danger` | 13 `--danger` | transaction-level failure ("فشل التحويل") vs form `error` | PLANNED |
| completed | `--positive-tint` | 16 `--positive` | 13 `--ink` | "تمّت العملية" | PLANNED |
| cancelled | `--sunken` | 16 `--ink-muted` | 13 `--ink-muted` | "ملغي" | PLANNED |
| reversed | `--sunken` | 16 `--ink-subtle` | 13 `--ink-subtle`, amount `line-through` + `<bdi>` | "معكوس" | PLANNED |

---

## 4 · Sheet / Dialog — motion states

Sheet: bottom-anchored `--surface`, top corners `--radius-lg`, grabber 32×4 radius `--radius-full` `--line-strong`, content padding `--space-24`. Dialog: centered, `--radius-lg`, max-inline-size `min(360px, 100% − 2×--space-edge)`. Focus is trapped while open; on close focus returns to the trigger (stored `document.activeElement` at open). Escape and scrim-tap both dismiss. All motion is translateY/scale/opacity — direction-safe under RTL.

| Component | Motion state | Tokens | Behaviour / a11y | Demonstrated in |
| --- | --- | --- | --- | --- |
| sheet | opening | translateY(100%→0), `--dur-sheet-in` (240ms) `--ease-standard` | `[data-state="opening"]`; focus moves in after settle | PLANNED |
| sheet | open | static; grabber visible | `[data-state="open"]`, `role="dialog"`, `aria-modal="true"`, focus trap | PLANNED |
| sheet | closing | translateY(0→100%), `--dur-sheet-out` (180ms) `--ease-exit` | `[data-state="closing"]` | PLANNED |
| sheet | closed | removed from flow / `display:none` after exit | focus returns to trigger | PLANNED |
| dialog | opening | scale(0.96→1) + opacity, `--dur-dialog-in` (160ms) `--ease-standard` | `[data-state="opening"]` | PLANNED |
| dialog | open | static | `role="dialog"`, `aria-modal`, `aria-labelledby`, trap | PLANNED |
| dialog | closing | scale(1→0.96) + opacity, `--dur-dialog-out` (120ms) `--ease-exit` | `[data-state="closing"]` | PLANNED |
| dialog | closed | removed | focus returns to trigger | PLANNED |
| scrim | fade-in | opacity 0→1, `--dur-scrim` (200ms) | `--scrim` at `--z-scrim-sheet` (250) / `--z-scrim-dialog` (350) | PLANNED |
| scrim | fade-out | opacity 1→0, `--dur-scrim`, `--ease-exit` | tap dismisses (non-modal regions only) | PLANNED |
| both | escape-dismiss | exit sequence as closing | keyboard `Esc`; announced via live region | PLANNED |

---

## 5 · Content families (compact matrices)

| Family | Variant/state | Key tokens | Demonstrated in |
| --- | --- | --- | --- |
| QuickActionRail | tile default | tile 88×92, icon 24, label 13, gap `--space-8`, edge `--space-edge`, `--surface`, radius `--radius-md` | PLANNED |
| QuickActionRail | tile pressed | `--press-overlay` veil `--dur-press` | PLANNED |
| QuickActionRail | tile focused | ring 2px `--brand-ink` | PLANNED |
| QuickActionRail | rail scrolling | `scroll-snap-type: x mandatory`, snap-align start; edge fade mask both edges | PLANNED |
| PrimaryValueBlock | default | 32/600/1.15 `--ink-strong` on `--canvas`, "د.أ" qualifier 13 `--ink-muted`, `<bdi>` tabular | PLANNED |
| PrimaryValueBlock | delta up / down | text-only chip `--positive` / `--danger` (on canvas, AA ✓) | PLANNED |
| PrimaryValueBlock | loading | `--sunken` placeholder block, no count-up, `aria-busy` | PLANNED |
| PrimaryValueBlock | stale / error | qualifier "آخر تحديث…" 13 `--ink-subtle`; "—" placeholder `--ink-subtle` | PLANNED |
| MetricGroup | rows default | `--surface` card radius `--radius-lg` pad `--space-16`; grid label 15/qualifier 13/value 15·500 tabular `--ink-strong`; dividers 1px `--line-soft` | PLANNED |
| MetricGroup | loading | row value slot → `--sunken` bars | PLANNED |
| MetricGroup | delta rows | value `--positive` / `--danger` where signed | PLANNED |
| OperationalRow | default | 40×40 tinted status chip + 24 icon; title 15; qualifier 13; amount 15·500 `<bdi>`; chevron 16 mirrored | PLANNED |
| OperationalRow | pressed / focused | `--press-overlay` veil / ring 2px `--brand-ink` | PLANNED |
| OperationalRow | status chips | `--info-tint`/`--positive-tint`/`--danger-tint`/`--warning-tint`/`--sunken` per status | PLANNED |
| BottomNavigation | tab default / active / pressed / focused / disabled | radius **0** edge-to-edge; `--surface` + 1px `--line-soft`; active `--brand-ink`, inactive `--ink-muted`; icon 24 + label 13→14; `--z-nav`; safe-area padding | PLANNED |
| Chart primitive | default / focused | grid `--line-soft`; series `--brand-atmosphere`; semantics `--positive`/`--danger`; `role="img"` + `aria-label` + `aria-describedby` data table; static values (no count-up) | PLANNED |
| Chart primitive | empty / error | "لا توجد بيانات" / State chip instead of axes | PLANNED |

---

## 6 · Coverage checklist for the final lab

- [ ] All 30 Button cells demonstrated (destructive quiet-completion row documents the routing rule).
- [ ] All 36 Input cells demonstrated (checkbox/switch include their checked/on reference rows).
- [ ] All 10 State statuses demonstrated, including reversed amount `line-through` + `<bdi>`.
- [ ] Sheet + Dialog full open/close cycles with focus return and scrim at correct z-order.
- [ ] Every "PLANNED" above replaced with a real lab location before extraction sign-off.
