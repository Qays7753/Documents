from pathlib import Path
import hashlib
import shutil

ROOT = Path('/home/ubuntu/Documents_final_copy')
PACKAGE = ROOT / 'micro-standard-v2'
RUN = ROOT / 'planning/micro-standard-v2-execution-handoff-2026-09/runs/run-20260913-msv2-zai-01'
SNAPSHOT = RUN / 'standard-snapshot'

files = sorted(p for p in PACKAGE.rglob('*') if p.is_file())
if len(files) != 31:
    raise SystemExit(f'Expected 31 package files, found {len(files)}')

for p in SNAPSHOT.rglob('*'):
    if p.is_file() or p.is_symlink():
        p.unlink()
for p in sorted(SNAPSHOT.rglob('*'), reverse=True):
    if p.is_dir():
        p.rmdir()
SNAPSHOT.mkdir(parents=True, exist_ok=True)

lines = []
for source in files:
    relative = source.relative_to(PACKAGE)
    target = SNAPSHOT / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    lines.append(f'{digest}  micro-standard-v2/{relative.as_posix()}')

(RUN / 'final_sha256.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(f'REFRESH_PASS files={len(files)}')
print(f'FINAL_SHA={hashlib.sha256((RUN / "final_sha256.txt").read_bytes()).hexdigest()}')
