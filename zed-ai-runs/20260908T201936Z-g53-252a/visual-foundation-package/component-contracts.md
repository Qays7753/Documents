# Component Contracts

Every family shown in the gallery has a contract here. Each contract states anatomy, dimensions, tokens, allowed content, states, interaction feedback, and accessibility — the SOP §9 requirement. Sizes are rem-based (px shown at the default 16px root); all interactive elements honor the 44px touch minimum and the unified focus ring.

---

## 1. Button

- **Anatomy:** optional leading icon (20px) + label; or icon-only (44px round).
- **Dimensions:** min-height 48px (compact 40px with 20px padding), radius 12, padding 12/24, gap 8.
- **Tokens:** fills per `button-system.md` ladder; label 15px/600; pressed fill one step deeper.
- **Content:** verb-first label ≤ 24 chars, never truncating; icon 20px; `aria-label` when icon-only.
- **States:** default, pressed, focused, disabled, loading, quiet-completion.
- **Feedback:** 120ms scale 0.97 + fill step; loading disables activation (double-submit guard).
- **A11y:** focus ring 2px accent.600; disabled exempt from contrast but must look inert; loading announced via `aria-busy`.
- **Example:** one filled primary `Save` with the full state row in the gallery.

## 2. Input (text / search / select / amount / multiline)

- **Anatomy:** label 13px/500 (8px above) + field + helper/error 12px (4px below); optional leading/trailing icons.
- **Dimensions:** 48px min-height, radius 12, padding 12, 1px border.
- **Tokens:** border `border-soft` → focus `accent.500`; error `negative.500` + message `negative.600`; disabled recessed.
- **Content:** placeholder as example; amount = mono 24/700 centered LTR `inputMode=decimal` live grouping; multiline grows.
- **States:** default, focused, error, disabled, read-only, long-content.
- **Feedback:** 150ms border-color transition + focus ring; select opens E2 panel (44px options, selected = accent.50 + accent.600 + check).
- **A11y:** label programmatically associated; errors via `aria-describedby`; never color-only (icon + text).
- **Example:** labeled text field with helper; error field with message.

## 3. Chip / Tag

- **Anatomy:** label-only pill (optional 20px leading icon).
- **Dimensions:** 36px height, full radius, 12px horizontal padding, 44px hit area, 8px gaps in a scrollable row.
- **Tokens:** unselected white + 1px `divider` + `ink-secondary`/500; selected `primary.700` + white/600, no border.
- **Content:** filter names ≤ 18 chars; **one selected maximum** per group.
- **States:** default, selected, focused, disabled; tags are non-interactive status pills.
- **Feedback:** 200ms tint transition; press scale.
- **A11y:** `aria-pressed` for selection; selection visible without color (fill + weight).
- **Example:** filter row with one active chip.

## 4. Segmented control

- **Anatomy:** pill variant — ivory track (18px radius, 4px inset) + sliding 12px-radius thumb + labels; underline variant — labels over 2px divider with a 4px primary indicator.
- **Dimensions:** track 4px inset; buttons 40px min-height; labels 13–15px/600.
- **Tokens:** track `recessed`; thumb `primary.700` + `shadow.sm`; active label white; inactive `ink-secondary`.
- **Content:** 2–5 segments; optional count badges (12px/600 pill).
- **States:** per-segment active/inactive/focused; whole control disabled.
- **Feedback:** thumb slides 300ms ease-out (RTL-aware logical offset); underline slides same.
- **A11y:** `radiogroup` semantics, arrow-key movement (contract; gallery demonstrates selection), one active segment.
- **Example:** 3-segment pill switcher, live.

## 5. Badge

- **Anatomy:** text pill, optional leading 12px icon or 6px dot.
- **Dimensions:** 4px/12px padding, full radius, 12px/600.
- **Tokens:** pairs per `data-display-system.md` (progress gold.50/gold.700, ready accent.50/accent.600, closed recessed/ink-secondary, semantic 50-tint + 600-step).
- **Content:** status words ≤ 16 chars, number + unit.
- **States:** static (no interaction).
- **A11y:** color never sole cue — icon/dot or adjacent sign; contrast per table (all ≥ 4.5).
- **Example:** full status + semantic set.

## 6. Card / KPI surface

- **Anatomy:** optional header (15px/600) + content; KPI: label 13px/500 + number 24–28px mono + change line 12px; featured: recessed fill with inner white tiles (12px radius, 16px padding, 34px icon chips).
- **Dimensions:** radius 16, padding 16 (compact 12), gaps 12/24.
- **Tokens:** surface + E1 no border; recessed variant + E1; change line in semantic 600.
- **Content:** content-driven height; long text wraps or line-clamps; numbers mono tabular.
- **States:** static; skeleton replaces card content during load; ghost-out removal animation for dismissed items.
- **A11y:** semantic structure (headings/labels); contrast pairs measured.
- **Example:** white KPI card + ivory featured card.

## 7. Row

- **Anatomy:** leading 44×44 icon tile (semantic 50 bg) + title + secondary line + type badge + trailing signed amount.
- **Dimensions:** min 56px, padding 16, content-driven growth.
- **Tokens:** separators `border-soft` 1px; alternate rows canvas; amounts semantic 600-step mono.
- **Content:** title truncates with ellipsis (line-clamp preferred); date/time mono 12px; amount with explicit sign.
- **States:** default, alternate, pressed, focused (whole row tappable), long-content (grows).
- **Feedback:** press tint on the row surface; no swipe actions in the neutral system (documented product behavior).
- **A11y:** sign + icon + color for state; 44px+ target by construction.
- **Example:** four semantic rows with alternating background.

## 8. Navigation (top bar / bottom nav / FAB / action bar)

- Contract per `navigation-shell.md`. One active destination; filled active icon; 3–5 destinations; focus ring on items; FAB 56px E3 end-anchored 80px above nav; action bar 72px + safe area with one primary.
- **A11y:** `nav` landmark + `aria-current` on the active item; 44px+ items.

## 9. Overlay (sheet / dialog / menu / snackbar)

- Contract per `overlay-system.md`. Shared: scrim, single close path, focus containment + restore, Escape, body scroll lock. Sheet: 84/94vh snaps, drag handle, 340ms slide. Dialog: centered 16px-radius E3, scaleIn 200ms. Menu: 12px-radius E2, 44px options, selected accent pair. Snackbar: ink surface, 5s, undo action, polite live region.
- **A11y:** `role=dialog` + `aria-modal`; snackbar `role=status`.

## 10. Empty / loading / error states

- Contract per `empty-loading-error-states.md`. Empty: 64px icon tile + title + body + action. Loading: skeletons (never spinners for content). Error: negative-tinted panel + retry. No-results distinct from no-data.
- **A11y:** `role=status` for empty/loading; errors announced.

## 11. Icon

- 24 (default) / 20 (small) viewBox-24 outline SVGs, stroke 1.5–2.5, round caps/joins, `currentColor`; selective RTL mirroring per `iconography.md`; icon-only controls carry `aria-label`.
- **Example:** 26-glyph sheet with mirrored chevrons in RTL.
