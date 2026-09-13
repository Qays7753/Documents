# Wave B Report — Gallery and Component Composition

- **Run**: `run-20260913-msv2-zai-01` · **Branch**: `micro-standard-v2-execution-20260913`
- **Commit**: `0d48846` · **Rollback**: `git reset --hard 125115d` (Wave A) or `df4018e` (Wave 0)
- **Status**: **PASS**

## What changed (3 files)

### `component-gallery.html`
1. **Buttons family** — head copy and demos now teach the owner action classes: Create (`#D97757`, plus icon), ordinary Save entry (Warm Tint, check icon), Finalize period (warm-ink fill, high-consequence only), Secondary/Outline/Ghost, Delete record (error), and Accept/Transfer restated with semantic marker icons. New "Ordinary save — six states of one action" frame: default, pressed (Clay edge), focused, disabled, loading (tap-tap duplicate guard), quiet completion (check + past-tense word).
2. **Filtering** — sheet Apply moved from ink fill to the ordinary-save class (`btn-save`, "Apply filters" + ghost Reset); chip anatomy note documents the edge-based selected state.
3. **Charts (new family)** — question-led Arabic bar chart ("أي يوم كان الأقوى هذا الأسبوع؟") with period chip ("آخر 7 أيام"), four honest states cycled by button (data → zero days → no data → loading), one Info highlight on the bar that answers the question, 2px baseline marks for measured zeros, visible Arabic text alternative, and an `aria-label` on the chart region.
4. **Rows** — "Returned" rows moved off the retired gold naming to the neutral pair; new "State slots" frame (Pending/Reviewed/Unknown rows with ≤3px semantic edge stripes, always paired with the word+marker tag); new "State tag grammar" frame (Posted/Failed/Pending/Unknown/Reviewed tags with semantic hue on the marker).
5. **Overlays** — destructive/commit dialog renamed "Finalize period?" with consequence wording documenting the reserved warm-ink surface; action bar trigger aligned.
6. **Evidence panel** — identity note rewritten to the action-class contract; semantic note records gold retirement and marker-based tag grammar; false "155 tokens / 177 custom properties / zero mismatches" claim replaced by the audited counts (18 approved hex values — unchanged; 133 canonical tokens + 5 aliases; 2 disclosed alpha derivatives; 0 unresolved).

### `component-gallery.css`
1. New action classes: `.btn-create` (Clay + pressed `#C96442`), `.btn-save` (Warm Tint + 1px tint border; pressed = inset 2px `#C96442` edge; loading keeps the tint surface; dark spinner variant for light surfaces).
2. `.btn-primary` unchanged as the reserved warm-ink commit fill; `.btn-positive`/`.btn-operational` restated from filled success/info (white text at 3.27:1 / 3.87:1 — AA text failure, color-alone semantics) to Warm Tint surfaces with semantic marker icons and text-safe ink — same values, owner-compliant grammar.
3. Selection grammar: `.chip.on`, `.segctl-thumb`, `.segctl-lines` underline/indicator, and the current-destination `.navpill` now use the chosen/current edge role (`inset 2px #C96442` / underline) with ink labels — no automatic black fills.
4. State grammar: `.tag-neutral/-pending/-review/-unknown` added with semantic hue on markers; gold classes retired (`.tag-gold`/`.t-gold`/`.gold` → neutral equivalents); row edge-stripe classes (`stripe-pending/-failed/-review`, ≤3px, inline-start).
5. Chart styles: question header, period chip, bar series (neutral `#4D4C48` body, one Info highlight, 2px `#87867F` zero-baseline marks), text-alternative caption, no-data and loading states.
6. **Reduced motion defect fixed**: the header control set `html[data-motion="reduced"]` but no CSS consumed it. Added the reduced-motion block (control + `prefers-reduced-motion`), collapsing durations to near-instant while preserving labels, markers, and `aria-busy`.

### `component-gallery.js`
1. Loading-button handler now captures and restores each button's own label ("Save entry") instead of hard-coded "Save".
2. New chart state cycler (`data-chart-cycle`) wiring the four chart states and the question swap for the no-data state.

## Explicitly NOT changed
Inputs, menus, rail cards, snackbars, topbars, empty/skeleton/error panels, icon grid — all baseline demos remain. No product routes, writes, formulas, or business actions were added; all interactions are local demonstrations. No file added/removed (still 31 files). Pre-existing demo conventions outside the owner delta (e.g., the ink `.filter-count` badge, gallery chrome seg) were left as-is.

## Owner-constraint compliance
- Hex set unchanged (18 approved values; audit re-run in Wave A still applies — no raw color added in Wave B; zero marks use the existing interactive-boundary token).
- No Dark Mode, no teal, no `#964E33`/`#5F3120`/`#B79C86`/`#8C7A66`, Terracotta never used as data/success/failure (charts: neutral + Info only).
- FAB stays Clay, icon-only, in its own gutter; amount columns unaffected.

## Tests (executed in headless Chromium; `wave_b_tests.json` + 12 screenshots)
- **Computed contracts**: create `rgb(217,119,87)`; create pressed `rgb(201,100,66)`; save surface `rgb(245,244,237)` with ink `rgb(20,20,19)`; save pressed = inset 2px `rgb(201,100,66)`; commit fill `rgb(20,20,19)`; selected chip = white surface + inset Clay edge (never black); segmented thumb/underline = surface + Clay edge; nav current pill edge; FAB Clay 56px; scrim `rgba(20,20,19,0.45)` (now visible); zero gold classes remain.
- **Interactions**: loading sets `aria-busy=true` while the surface stays Warm Tint; quiet completion shows check + "Saved"; label restores to "Save entry"; chart cycles data→zero(+text alternative)→nodata→loading→data; sheet and dialog open/close (Escape).
- **Viewports**: 320/360/390/430px — no horizontal overflow at any width.
- **Zoom/text scale**: 200% at 320px — no horizontal overflow (screenshot `b12-320px-200pct-full.png`).
- **Reduced motion**: control + system preference collapse transitions/animations to 0.00001s.
- **Errors**: zero console/page errors.
- Not tested / not claimed: physical Samsung device, screen reader.

## Wave boundary
Gate passed → Wave C (verification & documentation) may proceed. Rollback: `git reset --hard 125115d`.

## Amendment (added during Wave P, same branch — commit `3274e6e`)
Validation of the interactive Prototype surfaced a latent defect in `component-gallery.css`: overlay roots carrying author `display` values (`.dialog-anchor { display: grid }`) overrode the UA `[hidden] { display: none }` rule, so a *hidden* dialog anchor remained in layout and could intercept pointer events (the shipped sheets/dialogs had worked only because the overlay manager also toggles classes/transforms). Fix applied: one defensive rule `[hidden] { display: none !important; }` appended to `component-gallery.css`. Full Wave B test battery re-run after the fix: zero errors, dialog/sheet open-close PASS, all computed contracts unchanged. No other Wave B content altered.
