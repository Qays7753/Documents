from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    'AGENTS.md',
    'README.md',
    'SOP_VISUAL_ONLY.md',
    'SOURCE_MANIFEST.md',
    'source-reference/accounting-sop.source.md',
    'source-reference/SOURCE_AUDIT_NOTES.md',
    'source-reference/VISUAL_ONLY_BOUNDARY.md',
    'source-reference/tailwind.config.source.js',
    'source-reference/index.css.source',
    'source-reference/source-tokens.json',
    'reference-components/layout/PageHeader.jsx',
    'reference-components/layout/BottomNav.jsx',
    'reference-components/layout/AppLayout.jsx',
    'reference-components/sheets/Fab.jsx',
    'reference-components/ui/AmountInput.jsx',
    'reference-components/ui/BottomSheet.jsx',
    'reference-components/ui/EmptyState.jsx',
    'reference-components/ui/Icon.jsx',
    'reference-components/ui/SegmentedControl.jsx',
    'reference-components/ui/Snackbar.jsx',
    'rendered-reference/accounting-mockup.html',
    'rendered-reference/accounting-color-identity.html',
    'rendered-reference/accounting-mobile-components.html',
]
missing = [p for p in required if not (ROOT / p).is_file()]
if missing:
    raise SystemExit('Missing required files:\n' + '\n'.join(missing))

json.loads((ROOT / 'source-reference/source-tokens.json').read_text(encoding='utf-8'))

forbidden_names = {'.env', '.env.local', 'package-lock.json', 'node_modules', '__pycache__'}
found_forbidden_names = [p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.name in forbidden_names]
if found_forbidden_names:
    raise SystemExit('Forbidden files found:\n' + '\n'.join(found_forbidden_names))

neutral_docs = [ROOT / 'AGENTS.md', ROOT / 'README.md', ROOT / 'SOP_VISUAL_ONLY.md', ROOT / 'SOURCE_MANIFEST.md']
for path in neutral_docs:
    text = path.read_text(encoding='utf-8').lower()
    for forbidden in ('password', 'api_key', 'access token', 'secret'):
        if forbidden in text and 'do not' not in text and 'not' not in text:
            raise SystemExit(f'Suspicious secret wording in {path}: {forbidden}')

for html in ROOT.glob('rendered-reference/*.html'):
    text = html.read_text(encoding='utf-8').lower()
    if '<html' not in text or '</html>' not in text:
        raise SystemExit(f'HTML shell incomplete: {html}')

print(f'PASS: {len(required)} required files present')
print('PASS: source-tokens.json parses')
print('PASS: no forbidden environment/package files')
print('PASS: rendered reference HTML shells present')
