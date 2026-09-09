# Component Contracts

Every family shown in the gallery has a contract here. Each contract states anatomy, dimensions, tokens, allowed content, states, interaction feedback, and accessibility — the SOP §9 requirement. Sizes are rem-based (px shown at the default 16px root); all interactive elements honor the 44px touch minimum and the dual-ring focus contract (light surfaces: accent.600 ring + 2px offset; dark fills: inset surface ring at −4px, R-05).

---

## 1. Button

- **Anatomy:** optional leading icon slot (fixed 20px, houses icon or spinner) + label; or icon-only (44px round).
- **Dimensions:** min-height 48px (compact 40px), radius 12, padding 12/24, gap 8.
- **Tokens:** fills per `button-system.md` ladder; destructive = negative.600 (R-19); label 15px/600.
- **Content:** verb-first label ≤ 24 chars, never truncating; icon 20px; `aria-label` when icon-only.
- **States:** default, pressed (0.97 + one deeper fill step, 80ms), focused (dual ring), disabled, loading (spinner in the icon slot, label persists, aria-busy, activation blocked), quiet-completion (check + positive tint 800ms).
- **Feedback:** 80ms press; loading guards duplicate submits; completion resets and confirms via snackbar.
- **A11y:** dual-ring focus; disabled exempt from contrast but visually inert; loading announced via `aria-busy`.
- **Example:** the six-state strip + live loading cycle in the gallery.

## 2. Input (text / search / select / amount / multiline)

- **Anatomy:** label 13px/500 (8px above) + field + helper/error 12px (4px below); optional leading/trailing icons.
- **Dimensions:** 48px min-height, radius 12, padding 12, 1px border.
- **Tokens:** border `border-soft` → focus `accent.500` + ring; error `negative.500` + message `negative.600`.
- **Content:** placeholder as example; amount = mono 24/700 centered LTR `inputMode=decimal` live grouping; multiline grows.
- **States:** default, focused (ring visible — R-04), error, disabled, read-only, long-content.
- **Feedback:** 120ms border-color transition; menus (select/sort) open E2 panels that close on Escape/outside/option and restore focus (R-23).
- **A11y:** label associated; errors via `aria-describedby` + `aria-invalid`; never color-only (icon + text).
- **Recovery:** validation errors render at the control, preserve the typed value, and refocus the input (R-15).
- **Example:** labeled field with helper; live recovery loop in the gallery.

## 3. Filter control + filter sheet (Repair C)

- **Anatomy:** compact trigger (icon 20 + label + count badge) in the list header; sheet with drag handle, title, close, grouped choice chips, Reset + Apply footer.
- **Dimensions:** trigger 36px visual/44px hit, full-radius; sheet per overlay contract; chips 36/44.
- **Tokens:** trigger surface + divider border; count badge primary.700/white; groups label 13/600 + hint 12.
- **Content:** Status (7 values, multi), Date range (4 values, single), Type (4 values, multi); sort lives in the sibling single-choice dropdown — one dropdown per context.
- **States:** trigger default/pressed/focused/expanded; chips aria-pressed (multi) or radiogroup (single); sheet open/expanded/dragging/closed.
- **Feedback:** sheet 240/180 + scrim 200; staging semantics — Apply commits, Reset clears the draft, Cancel/scrim/Escape/drag discards; reopen stages from applied (R-29); after apply only the summary line + count remain.
- **A11y:** `role=dialog` + `aria-modal` + labelled; trigger `aria-expanded` + `aria-haspopup`; chips expose pressed/checked; summary is a live region.
- **Example:** the live filterable list with count, summary, filtering, sorting, and the no-results swap.

## 4. Chip / Tag

- **Anatomy:** label-only pill (optional 20px leading icon); tags are read-only status pills with a mandatory icon/dot.
- **Dimensions:** 36px visual, 44px hit (`::after` inset −4px, R-26), full radius, 12px horizontal padding.
- **Tokens:** unselected white + 1px `divider` + `ink-secondary`/500; selected `primary.700` + white/600, no border; tags use the badge pairings.
- **Content:** filter names ≤ 18 chars; one selected per single-choice group; multi groups toggle.
- **States:** default, selected, focused, disabled.
- **Feedback:** 120ms tint transition; press scale.
- **A11y:** `aria-pressed`/`aria-checked` state semantics (R-21); selection visible without color.
- **Example:** chips inside the filter sheet + the anatomy reference row; tags inside rows.

## 5. Segmented control

- **Anatomy:** pill variant — ivory 18px-radius track (4px inset) + sliding 12px thumb; underline variant — labels over a 2px divider with a sliding 2px primary indicator.
- **Dimensions:** buttons 44px min-height; labels 13px/600.
- **Tokens:** track `recessed`; thumb `primary.700` + `shadow-sm`; active label white (pill) or ink (underline).
- **Content:** 2–5 segments; optional count badges.
- **States:** per-segment active/inactive/focused; whole control disabled.
- **Feedback:** thumb and indicator slide 200ms, RTL-aware logical offsets (R-25); arrow-key activation.
- **A11y:** radiogroup/radio (pill) or tablist/tab (underline) + aria-checked/selected (R-21).
- **Example:** both variants, live.

## 6. Metric surface (Repair D)

- **Anatomy:** direct primary value = label + number + optional change; summary composition = label + period + 28px mono total + 8px two-segment relationship bar + two supporting values (34px icon chip + name + mono value); grouped surface = label rows with dividers.
- **Dimensions:** content-driven height; bar track 8px (`progress.track-height`); cards radius 16, padding 16.
- **Tokens:** bar track `recessed`; segments `operational.600` + `positive.500`; chips 100-step tints + 600 icons; totals `kpi-hero`.
- **Content:** numbers first, labels short; supporting values must **sum to the total**; two-column parts only when the comparison is genuine (stack below 360px).
- **States:** static + updating (bar moves 200ms, numbers immediate, aria-label carries values — R-14); skeleton during load.
- **A11y:** bar labeled with the live relationship; semantic structure; no white-card-in-white-card.
- **Example:** direct value card, summary composition with simulate-update, grouped surface.

## 7. Row (Repair E)

- **Anatomy:** leading 44×44 semantic tile + flexible text column (title + sub row with optional status tag + mono date) + trailing area (signed mono amount + optional 44px chevron or remove action).
- **Dimensions:** min 56px, padding 16, content-driven; title wraps + 2-line clamps.
- **Tokens:** dividers 1px `border-soft` inset to the text column (72px — one rule); alt rows canvas; amounts semantic 600-step mono, bidi-isolated.
- **Content:** short + long Arabic titles, wrapped qualifiers, dates, trailing actions; chevron mirrors in RTL and nudges toward the reading end on activation (120ms).
- **States:** default, alternate, pressed, focused, long-content (wraps), is-new (600ms tint flash), is-removing (200ms collapse).
- **Feedback:** local insert/remove only; removal + real undo restores the node (R-13).
- **A11y:** sign + icon + color for state; 44px targets by construction; remove buttons carry aria-labels.
- **Example:** grid demo, the filterable list, the manage list.

## 8. Quick action rail (Repair G)

- **Anatomy:** horizontally scrollable row of action cards — tinted card (radius 16, padding 12) + white 48px icon chip (radius 16) + 15px/600 label + 12px caption.
- **Dimensions:** cards 136px wide, snap-align start; gap 12.
- **Tokens:** card tints = semantic 50-steps + primary.100; chip icons semantic 600-step / primary.700.
- **Content:** 4–8 creation/quick actions (source Fab sheet vocabulary: sale, collect, expense, purchase, withdrawal, invoice).
- **States:** default, pressed (0.97), focused (dual ring — tinted card gets the accent ring).
- **Feedback:** scroll-snap x proximity; native touch scroll; pointer drag on desktop; `touch-action: pan-x pan-y` so vertical page scroll is never hijacked; the peeking next card is the cue.
- **A11y:** cards are real buttons with accessible names; directional glyphs mirror in RTL.
- **Example:** the six-action rail.

## 9. Navigation (top bar / bottom nav / FAB / action bar)

- Contract per `navigation-shell.md`. One active destination with a filled 24px icon; 3–5 destinations; `aria-current`; FAB 56px **identity.500** E3 end-anchored 80px above nav (R-18); action bar 72px + safe area with one primary.
- **A11y:** `nav` landmark; 44px+ items; dual-ring focus.

## 10. Overlay (sheet / dialog / menu / snackbar)

- Contract per `overlay-system.md`. Shared: scrim (200ms), one close path, focus trap + restore (R-07), Escape stack (top layer first), body scroll lock (R-28), `[hidden]` guard (R-03). Sheet: 84/94 snaps, drag (−50 expand/+130 dismiss/−44 clamp), 240/180. Dialog: centered grid anchor (R-30), 160/120. Menu: 12r E2, 44px options, 120ms, accent.600 check. Snackbar: ink surface, 5s, real undo action, 200/120.
- **A11y:** `role=dialog` + `aria-modal`; snackbar `role=status`.

## 11. Empty / loading / error states

- Contract per `empty-loading-error-states.md`. Empty: 64px tile + title + body + action. Loading: skeletons (never spinners for content). Error: panel + retry with guard; field errors at the control. No-results distinct from no-data — and wired live to the filter state.
- **A11y:** `role=status`; errors announced.

## 12. Icon

- 24 (default) / 20 (rows, slots) viewBox-24 outline SVGs, stroke 1.5–2.5, round caps/joins, `currentColor`; 43-glyph sprite with a name + mirror-flag registry (R-11); selective RTL mirroring per `iconography.md`; icon-only controls carry `aria-label`.
- **Example:** the labeled 43-glyph grid + the chevron mirror demo.
