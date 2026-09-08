from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path('/home/ubuntu/accounting_visual_foundation_source_pack_v1')
SOURCE = ROOT / 'source-reference' / 'tailwind.config.source.js'
OUT = ROOT / 'source-reference' / 'source-tokens.json'

text = SOURCE.read_text(encoding='utf-8')
hexes = sorted(set(re.findall(r'#[0-9A-Fa-f]{6}', text)))
rgba = sorted(set(re.findall(r'rgba\([^)]*\)', text)))

families: dict[str, dict[str, str]] = {}
current: str | None = None
for line in text.splitlines():
    heading = re.search(r'// ===== ([^=]+?) =====', line)
    if heading:
        current = heading.group(1).strip().lower().replace(' ', '-')
        families.setdefault(current, {})
        continue
    match = re.match(r'\s*([A-Za-z0-9_-]+):\s*[\'\"](#[0-9A-Fa-f]{6})[\'\"],?', line)
    if match and current:
        families[current][match.group(1)] = match.group(2)

result = {
    'source_file': str(SOURCE.relative_to(ROOT)),
    'extraction': 'literal hex and rgba values only; no new values generated',
    'families': families,
    'all_hex_values': hexes,
    'all_rgba_values': rgba,
}
OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'Wrote {OUT}')
print(f'Hex values: {len(hexes)}; rgba values: {len(rgba)}; families: {len(families)}')
