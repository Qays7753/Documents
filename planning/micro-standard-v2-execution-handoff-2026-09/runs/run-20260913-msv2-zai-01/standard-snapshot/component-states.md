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

## Interactive states

Every interactive component supports default, pressed, focused, disabled, loading, and completion where relevant.

- **Pressed** is transient feedback (scale 0.97 at 80ms, plus the class-specific edge: `#C96442` for ordinary save and selection). Pressed never converts an action into a success state.
- **Loading** keeps the label visible, swaps the leading icon for a spinner, holds layout stable, and blocks duplicate submission.
- **Quiet completion** returns the control to its quiet surface and shows a check icon plus a past-tense word; the authoritative result is confirmed by wording with a semantic marker, never by color alone.
- **Destructive actions** require confirmation and are never hidden inside a generic success path; they use the high-consequence contract (consequence word, icon, short explanation, independent confirmation path).
- **Unknown result** renders as its own state with word and marker on neutral ink; it is not failure, not success, and not a silent void.
