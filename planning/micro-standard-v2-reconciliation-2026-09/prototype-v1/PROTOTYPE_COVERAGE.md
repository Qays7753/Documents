# Prototype v1 — Contract Coverage Map

Every changed general-purpose contract maps to at least one scene with selector-level evidence anchors. Baseline contracts exercised throughout are listed last.

## Coverage matrix

| # | Changed contract (source file) | Scene(s) | Evidence anchors in the prototype |
|---|---|---|---|
| 1 | Knowledge-state presentation — confirmed/unconfirmed/incomplete/needs-review/estimated/unknown-magnitude (`component-states.md`) | S1, S2 | `.kgrid`/`.kmark`/`.kword`/`.kval` (six states, word + non-color marker + neutral tone, never Success/Error); `.kmini` in S2 (a knowledge qualifier beside an outcome state — orthogonality); S1 honest voids stay distinct (`.vgrid`) |
| 2 | Operational-row marker + optional ≤3px inline-start stripe (`component-contracts.md`) | S2 | `.rows`/`.row`/`.row-tile`/`.row-main`/`.row-title` (wraps)/`.row-amt` (15px mono ink, end-aligned, `unicode-bidi: isolate`); `.row.stripe::before` (3px, `inset-inline-start: 0`, paired with `.tag` state word); `#stripe-toggle`; inset dividers `.row:not(:first-child)::after` at 72px |
| 3 | AUX behavior addendum (`navigation-shell.md`) + route transition row (`motion-interaction.md`) | S3 | `#ctrl-route` (`data-route-kind="surface|deep"` — deep hides `.bottomnav`/`.fab`); `#ctrl-kb` (`data-keyboard="open"` hides topbar/nav/FAB; `#aux-content` and its field stay visible); `.bottomnav` `max(6px, env(safe-area-inset-bottom))`; `#ctx-toggle` (suppression when duplicating `#aux-h`); scroll listener → `.topbar.scrolled` hairline; `#aux-transition` 200ms `--motion-normal` content fade (`route-in`), no layout animation |
| 4 | Period-control variants (`component-contracts.md`) | S1 | `.vz-period` chips + `.pv .seg` (variant a: chip, 13px labels); `input[type="month"]` in `dir="ltr"` `.field-box` (variant b: native month input, LTR-isolated digits, 44px hit, wrapper focus ring) |
| 5 | Quiet feedback variant — inline completion, Snackbar optional (`component-states.md`) | S4 | `#save-btn` lifecycle: pressed (`.btn-save:active` 2px `#C96442` inset edge) → loading (`.is-loading`, `aria-busy`, spinner, duplicate guard) → `#inline-result` (check + «تم الحفظ» + `role="status"`); `#snackbar` only after `#snack-opt` opt-in (5000ms recorded hold) |
| 6 | Overlay versus in-flow (`component-contracts.md`) | S5 | `#sheet` (deletion confirmation: handle, consequence wording, independent confirm/cancel) and `#dialog-wrap` (high-consequence commit: `#141413` fill, consequence word, independent path) above the shared `#scrim` `rgba(20,20,19,0.45)`, z-ladder 250/300; `details.inflow` (continuous explanation stays in-flow) |
| 7 | Typography floor (`typography.md`) | S1, S6 | `.hgrid` (hero 28 / primary 24 / secondary 15 / tertiary 13 mono; tertiary labeled non-financial numeric); S6 `.type-spec` specimens incl. `.t13` label floor and `.t12` caption (explicitly marked non-financial metadata only); financial facts ≥15px throughout (`.vz-unit` 15, `.row-amt` 15) |
| 8 | Icon and RTL adapter guidance (`iconography.md`) | S6 | `.icon-grid`/`.ic-cell` — directional roles (سهم، شيفرون، إرسال، تراجع) flagged «ينعكس» and mirrored via adapter `transform: scaleX(-1)`; symmetric/object roles (ترس، محفظة، إضافة، تأكيد) flagged «ثابت»; neutral outlined 24px normalized-stroke glyphs (no library forced) |
| 9 | Authority ladder (`README.md`) | Chrome | `#authority-drawer` (سلطة العقود): Standard = contracts; Micro mapping = carrier; Micro docs = guidance; domain/application/storage = meaning/persistence |
| 10 | Verification/manifest corrections (`MANIFEST.json`, `verification-report.md`) | Run records | The updated package itself (29 core + 2 metadata split; testing limitations preserved); the prototype's own validation record is `PROTOTYPE_VALIDATION.md` |

## Baseline contracts exercised (unchanged foundations, demonstrated throughout)

- **Create/add/FAB role** — S3 `.fab` (56px Clay `#D97757`, white icon, own gutter ≥16px above nav, E3 shadow, pressed `#C96442`); S4 `.btn-create` (text-bearing Clay with `#141413` ink) and `.iconbtn-create` (icon-only, white icon).
- **Ordinary save** — S4/S5 `.btn-save` (Warm Tint `#F5F4ED` + ink; pressed = 2px `#C96442` inset edge; press never success).
- **High-consequence confirmation** — S5 `.btn-primary` (`#141413` fill, white text, consequence wording, independent confirmation) and the dialog body explanation.
- **Honest voids** — S1 `.vgrid`: unrecorded → action chip «سجّله»; unavailable → «غير متاح»; measured zero → `0` with its unit; S2 carries a void row.
- **RTL + English digits + bidi isolation** — every number is `<bdi dir="ltr">` inside the RTL document; the month input and amount input are LTR islands in RTL composition.
- **Reduced motion** — control + `prefers-reduced-motion` both collapse transitions/animations to 0.00001s while words/markers/`aria-busy` carry meaning.
- **No-overflow behavior** — validated at 320/360/390/430 × 100/130/200% across all six scenes (72 combinations).
- **Selection grammar** — chips (`aria-pressed` + `.on` = 2px `#C96442` inset edge + weight) and the current-destination nav pill (Clay edge, never black fills).
- **Surface-specific contrast bindings** — tag words in text-safe ink `#4D4C48`; success/status markers only on the white Surface (`.t-review`); info/error markers on the warm ground (`.t-pending`, `.t-failed`); knowledge marks neutral.
