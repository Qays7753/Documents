# Empty, Loading, Error, and Unknown

No data, no results, loading, failure, permission denial, and unknown result are different states. Errors explain the next action and offer retry. Input and staged choices are preserved. A request being sent is not a successful financial result.

## State distinctions

- **No data** — nothing exists yet: guiding copy plus one action (e.g., "سجّل أول قيد").
- **No results** — data exists but the filter excluded it: quiet title plus one clearing action; never shown as failure.
- **Loading** — honest text ("جارٍ التحميل…") or a skeleton that promises the real layout; the skeleton variant is optional and applies where the real layout is stable — it is not a universal requirement for every screen. The section title stays visible; `aria-busy` marks the region. (The chart loading contract in `data-display-system.md` keeps its recorded skeleton basis.)
- **Failure** — explains what failed and the next action, with a retry control; input and staged choices are preserved.
- **Unknown result** — the system cannot confirm what happened: rendered as its own state with the word "غير معروف" and an info marker on neutral ink. Unknown is never success, never failure, and never silently dropped; the user always gets a check path (retry or review).
- **Pending** — a known in-flight financial state that pairs the word "بالانتظار" with a clock marker and the Info role; pending never reads as success.

Quiet completion of an action confirms with a past-tense word plus a semantic marker (check icon) — the button returning to its quiet surface is not itself the proof of success.
