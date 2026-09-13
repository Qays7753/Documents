# Component States

Financial states use words plus non-color markers (icon, shape, or sign): draft, pending, posted, failed, cancelled, reversed, reviewed, partial, due, and overdue. Pending never reads as success. Reversed preserves the audit trail. Unknown result is separate from failure.

## State presentation matrix

| State | Word (example) | Marker | Color binding |
|---|---|---|---|
| draft | "مسودة" | pencil/dot outline | neutral ink-secondary |
| pending | "بالانتظار" | clock icon | Info `#2C84DB` |
| posted / success | "تم" | check icon | Success `#629987` |
| failed / error | "فشل" | alert icon | Error `#B53333` |
| cancelled | "ملغي" | close icon | neutral ink-tertiary |
| reversed | "عُكس" | return icon | Info `#2C84DB` + word |
| reviewed | "رُوجعت" | eye/check-circle icon | Status `#1490FF` |
| partial | "جزئي" | half-filled shape | word + Info or ink |
| due / overdue | "مستحق" / "متأخر" | clock/alert icon | word + Error for overdue |
| unknown | "غير معروف" | question/info icon | neutral ink; never success or failure |

Tinted marks reuse the Warm Tint ground with the semantic ink (`--color-negative-50` + `--color-negative-on-tint` pattern). A state mark always pairs color with its word and marker so no state depends on color alone.

## Knowledge-state presentation (information quality)

Knowledge states qualify **how well the information itself is known**. They are orthogonal to the outcome matrix above: an entry can carry any outcome state and any knowledge state at the same time (for example, a posted outcome with an estimated magnitude). Knowledge states never bind Success or Error colors, never render as success or failure, and never collapse into the honest voids (unrecorded → action chip; unavailable → its word; measured zero → "0" — see `component-contracts.md`).

| Knowledge state | Word (example) | Marker (non-color) | Tone binding |
|---|---|---|---|
| confirmed / known | "مؤكد" | check | default ink; no qualifier needed when simply known |
| unconfirmed | "غير مؤكد" | question-mark marker | neutral ink word + marker; never Success/Error |
| incomplete | "غير مكتمل" | half-filled shape | neutral ink word + marker |
| needs-review | "بحاجة لمراجعة" | eye marker | neutral ink word + marker |
| estimated | "تقديري" | tilde (~) approximate marker | neutral ink word + marker; the value renders at its normal size |
| unknown magnitude | "غير معروف" | question/info marker on neutral ink | same word family as result-unknown; never success or failure |

Rules: knowledge words always render in a text-safe ink; the marker carries the non-color signal; the tone stays neutral (ink-secondary/tertiary or the neutral tint ground) because a knowledge state is not an outcome and must not borrow outcome colors. The words shown are examples and remain product-owned. A knowledge qualifier never shrinks a value: an estimated financial amount still renders at its contractual size (never below 15px mono as a financial fact), with the knowledge word as a qualifier beside it. Knowledge-unknown (the magnitude is not known) is distinct from result-unknown (the system cannot confirm what happened, see below) and from the honest voids.

## Interactive states

Every interactive component supports default, pressed, focused, disabled, loading, and completion where relevant.

- **Pressed** is transient feedback (scale 0.97 at 80ms, plus the class-specific edge: `#C96442` for ordinary save and selection). Pressed never converts an action into a success state.
- **Loading** keeps the label visible, swaps the leading icon for a spinner, holds layout stable, and blocks duplicate submission.
- **Quiet completion** returns the control to its quiet surface and shows a check icon plus a past-tense word; the authoritative result is confirmed by wording with a semantic marker, never by color alone. Inline/quiet feedback is a valid completion channel: an inline result region (word + marker, `role="status"` / `aria-live` polite) or a quiet result card may confirm an action in place of a Snackbar. The Snackbar remains an optional transient channel — it is not mandatory, and a product may standardize on inline feedback. On warm-tint quiet surfaces the completion marker renders in ink (the check shape carries the meaning); semantic-hue markers require a surface that meets the 3:1 non-text minimum (see the surface-specific bindings in `accessibility.md`).
- **Destructive actions** require confirmation and are never hidden inside a generic success path; they use the high-consequence contract (consequence word, icon, short explanation, independent confirmation path).
- **Unknown result** renders as its own state with word and marker on neutral ink; it is not failure, not success, and not a silent void.
