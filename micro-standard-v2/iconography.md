# Iconography

Use one outlined 24px family with normalized strokes. Directional icons mirror in RTL; symmetric and object icons do not. Icons support words and state markers and never replace important financial wording.

## Adapter guidance

- **Mirror flags.** Each icon role carries a mirror flag: directional icons (arrows, chevrons, send/return, undo) mirror in RTL; symmetric and object icons never mirror; media controls (play, skip) keep their canonical direction. Mirroring is applied by the consuming adapter (for example a transform on the glyph), not by re-drawing icons.
- **Semantic icon roles.** Icons bind to roles — create, save, confirm, delete, warn, info, check, close, eye, clock — so a product can swap the glyph library without touching contracts. The Standard does not mandate a production icon library; any outlined, normalized-stroke 24px family that honors the mirror flags satisfies the contract.
- Icons support words and state markers and never replace important financial wording.
