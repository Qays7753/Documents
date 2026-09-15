# Button System

Buttons are divided into named action classes. Every class binds to tokens in `design-tokens.css` and follows the shared control baseline: 48px minimum height, 12px control radius, 600 weight, visible focus, duplicate-submit protection, loading without layout shift, and quiet completion. All states are expressed with words and markers; color alone never carries meaning.

## Action classes

### Create / add / FAB — Clay `#D97757`
The identity action. A text-bearing create/add button uses a filled Clay surface with dark `#141413` text and a non-semantic icon; its pressed state moves to `#C96442` with the text remaining readable. Icon-only identity controls such as the FAB and primary icon button use a white icon on the Clay surface. It never displays a financial value, never becomes the general color for commitments, and never fills cards or screens.

### Ordinary save / confirm — Warm Tint `#F5F4ED`
Not a filled black surface. Warm Tint surface with dark `#141413` text and a save icon. Pressing shows a clear `2px` inset `#C96442` edge while the surface stays Warm Tint; pressing never converts the button into a success state. After actual completion, show a success word with a semantic marker (check icon) — quiet completion does not rely on the button color alone.

### High-consequence commit / destructive confirmation — Warm ink `#141413`
Filled warm-ink surface with white text, used when a strong pause is appropriate. The label is a word describing the consequence, paired with an appropriate icon, a short consequence explanation in the dialog body, and an independent confirmation path (explicit confirm/cancel, not a single tap). Pressed moves to the existing `#3D3D3A`. Black never means danger automatically — the wording and context carry it.

### Secondary / outline / ghost
Secondary uses the neutral tint `#E8E6DC`; outline uses a white surface with the interactive boundary; ghost reduces visual weight for quiet actions. These carry no financial semantics.

### Destructive — error `#B53333`
Error ink with words and an icon on a surface or outline treatment; the destructive confirmation step uses the high-consequence contract above.

## State rules
- Pressed is transient feedback; it is never a success, posted, or completed state.
- Loading replaces the leading icon with a spinner while the label persists; width stays stable; duplicate submission is blocked.
- Quiet completion shows a check icon plus a past-tense word (e.g., "Saved" / "تم الحفظ") on the quiet surface, then returns the control to its default; the authoritative confirmation lives in the content/snackbar wording with its semantic marker.
- Disabled uses the disabled surface/ink pair with `cursor: not-allowed`.
- Focus is visible: outline ring on light controls, inset surface ring on filled controls.
