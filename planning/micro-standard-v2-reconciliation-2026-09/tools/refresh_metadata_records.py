from pathlib import Path
import hashlib
import json

root = Path('/home/ubuntu/Documents_reconciliation_fix')
run = root / 'planning/micro-standard-v2-reconciliation-2026-09'
pkg = run / 'micro-standard-v2-UPDATED'
manifest_path = run / 'FINAL_MANIFEST.json'
manifest = json.loads(manifest_path.read_text())

files = []
for path in sorted(pkg.rglob('*')):
    if path.is_file():
        rel = path.relative_to(pkg).as_posix()
        raw = path.read_bytes()
        files.append({'file': rel, 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)})
manifest['updated_package']['files'] = files
manifest['updated_package']['file_count'] = len(files)
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')

hash_lines = []
for path in sorted(run.rglob('*')):
    if not path.is_file():
        continue
    rel = path.relative_to(run).as_posix()
    if rel == 'SHA256SUMS.txt':
        continue
    raw = path.read_bytes()
    hash_lines.append(f"{hashlib.sha256(raw).hexdigest()}  {rel}")
(run / 'SHA256SUMS.txt').write_text('\n'.join(hash_lines) + '\n')
print(f'updated_package_files={len(files)}')
print(f'run_hash_lines={len(hash_lines)}')
