from pathlib import Path
import json, re, subprocess, sys

ROOT=Path('/home/ubuntu/Documents_final_copy')
PKG=ROOT/'micro-standard-v2'
checks=[]
def ck(name, ok, detail=''):
    checks.append((ok,name,detail))

# Package inventory.
files=sorted(p.relative_to(PKG).as_posix() for p in PKG.rglob('*') if p.is_file())
ck('package has exactly 31 files',len(files)==31,str(len(files)))
ck('package has 29 core files plus 2 metadata',sum(1 for p in files if p not in {'MANIFEST.json','RELEASE.md'})==29)

# Syntax and JSON.
proc=subprocess.run(['node','--check',str(PKG/'component-gallery.js')],capture_output=True,text=True)
ck('component-gallery.js syntax',proc.returncode==0,proc.stderr.strip())
for name in ['design-tokens.json','MANIFEST.json','coverage-matrix.json']:
    try: json.loads((PKG/name).read_text()); ok=True; detail=''
    except Exception as e: ok=False; detail=str(e)
    ck(f'{name} parses',ok,detail)

# CSS custom-property resolution.
def defs(t): return set(re.findall(r'--([A-Za-z0-9_-]+)\s*:',t))
def uses(t): return set(re.findall(r'var\(--([A-Za-z0-9_-]+)',t))
css=(PKG/'design-tokens.css').read_text()+'\n'+(PKG/'component-gallery.css').read_text()
unresolved=sorted(uses(css)-defs(css))
ck('Standard CSS custom properties resolve',not unresolved,', '.join(unresolved))

# Contract parity.
tok=(PKG/'design-tokens.css').read_text(); tj=json.loads((PKG/'design-tokens.json').read_text())
ck('text-bearing create ink is warm ink', 'vf-action-create-ink: var(--vf-ink)' in tok and tj['action_contracts']['create_add_fab']['text_ink']=='#141413')
ck('icon-only create ink is white', 'vf-action-create-icon-ink: var(--vf-ink-on-dark)' in tok and tj['action_contracts']['create_add_fab']['icon_ink']=='#FFFFFF')
css_gallery=(PKG/'component-gallery.css').read_text()
ck('text create uses create ink token','color: var(--vf-btn-create-ink)' in css_gallery)
ck('icon surfaces use icon ink token','var(--vf-action-create-icon-ink)' in css_gallery)
html=(PKG/'component-gallery.html').read_text()
ck('Gallery evidence states Clay text boundary','White on Clay is non-text-only; text-bearing Clay controls use dark ink.' in html)

# Approved palette guard.
forbidden=['#964E33','#5F3120','#B79C86','#8C7A66','#079FA0','#057B7C']
for c in forbidden:
    hits=[]
    for p in [PKG/'design-tokens.css',PKG/'design-tokens.json',PKG/'component-gallery.css',PKG/'component-gallery.html',PKG/'component-gallery.js']:
        if c.lower() in p.read_text(errors='replace').lower(): hits.append(p.name)
    ck(f'forbidden {c} absent from executable package',not hits,','.join(hits))

# Git hygiene.
proc=subprocess.run(['git','-C',str(ROOT),'diff','--check'],capture_output=True,text=True)
ck('git diff --check',proc.returncode==0,proc.stderr.strip())

# Exact contrast claims used by the correction.
ck('white on Clay is treated as non-text only','3.12' in (PKG/'accessibility.md').read_text())
ck('dark text on Clay is documented','text-bearing Clay controls must use a text-safe dark ink' in (PKG/'accessibility.md').read_text())
ck('Prototype excluded from acceptance','Prototype remains evidence only' in (PKG/'README.md').read_text() and 'Prototype remains evidence only' in (PKG/'RELEASE.md').read_text())

fails=[x for x in checks if not x[0]]
for ok,name,detail in checks: print(('PASS' if ok else 'FAIL')+': '+name+((' — '+detail) if detail else ''))
print(f'SUMMARY: failures={len(fails)} checks={len(checks)}')
sys.exit(1 if fails else 0)
