# Visual-Only Boundary

Some source reference files contain real labels, route names, sample values, product-adjacent comments, or imports because they were copied from a running application. These strings are present only as visual evidence of typography, wrapping, alignment, spacing, and state composition.

Do not copy their product wording, route names, calculations, business terms, data model, or workflows into the neutral output. When you need example content, replace it with neutral labels such as `Primary action`, `Secondary action`, `Selected`, `Positive state`, `Warning`, `Information`, `Empty state`, and `Try again`.

The visual reviewer is allowed to preserve the visible geometry of the source while replacing all product-specific content. The final neutral package must not require a database, route table, context provider, or product-specific import to render its gallery.

Files under `rendered-reference/` are visual evidence, not copy sources. Files under `reference-components/` are implementation evidence, not production code to be pasted into another product.
