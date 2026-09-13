# Motion and Interaction

Motion is restrained and purposeful. Timings (recorded basis):

| Interaction | Timing |
|---|---|
| Press | 80ms · scale 0.97 |
| Fast (menus, borders, snackbar exit) | 120ms |
| Normal (thumbs, bars, scrim, snackbar enter) | 200ms |
| Sheet enter / exit | 240ms / 180ms |
| Dialog enter / exit | 160ms / 120ms |
| Skeleton pulse | 1.5s infinite |
| Snackbar hold | 5000ms |

Easing uses the standard/out/in curves (`--ease-standard`, `--ease-out`, `--ease-in`); entrances decelerate, exits accelerate.

## Rules

Press feedback is brief and transient — it never communicates a result state. Sheets and dialogs enter/exit consistently above one shared scrim that fades at 200ms. List changes affect only the changed row (local insert/remove feedback, never page-wide). Numbers land immediately; there is no count-up on financial values.

## Reduced motion

Reduced motion removes nonessential movement: scale presses, pulses, and slides collapse to near-instant or opacity-only transitions, while state and action meaning is fully preserved through words and markers. A loading spinner remains identifiable in a reduced-motion form (label persistence and `aria-busy` carry the state).
