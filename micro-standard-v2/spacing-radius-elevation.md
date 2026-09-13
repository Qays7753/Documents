# Spacing, Radius, and Elevation

## Spacing grid

A 4px base grid: 4 / 8 / 12 / 16 / 20 / 24 / 32. Screens use 16px inline padding; cards and rows use 16px padding; related controls separate by 8–12px; section groups by 20–24px; screen-level breaks by 32px. Do not add nested card stacks to compensate for missing product structure.

## Radius

| Token | Value | Use |
|---|---|---|
| `--vf-radius-control` | 12px | buttons, inputs, small controls |
| `--vf-radius-card` | 16px | cards, rows, screens-in-frames |
| `--vf-radius-segment` | 18px | segmented containers |
| `--vf-radius-sheet` | 20px | sheets (top corners) |
| `--vf-radius-full` | 999px | pills, chips, counts |

## Elevation

Restrained, warm-toned shadows (recorded values):

- **E1** `0 1px 2px rgba(60,50,40,.06), 0 4px 12px rgba(60,50,40,.06)` — cards, row lists
- **E2** `0 6px 20px rgba(60,50,40,.10)` — menus, sheets, scrolled top bar
- **E3** `0 16px 40px rgba(60,50,40,.16)` — FAB, dialogs, snackbars
- **sm** `0 1px 2px rgba(60,50,40,.06)` — quiet chrome lifts

Surface separation comes primarily from the warm surface ladder (Canvas → Ground/Recessed → white Surface), with shadows as support. Shadows are decoration; they never carry financial or state meaning.
