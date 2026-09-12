# Component States

Financial states use words plus non-color markers: draft, pending, posted, failed, cancelled, reversed, reviewed, partial, due, and overdue. Pending never reads as success. Reversed preserves the audit trail. Unknown result is separate from failure.

Every interactive component supports default, pressed, focused, disabled, loading, and completion where relevant. Destructive actions require confirmation and are not hidden inside a generic success path.
