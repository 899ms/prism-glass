#!/usr/bin/env python3
import json, hashlib, sys, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
required=['SKILL.md','README.md','README.zh-CN.md','MASTER_PROMPT.md','QUICK_START_PROMPT.md','DESIGN_SYSTEM.md','COMPONENT_API.md','ACCEPTANCE_CHECKLIST.md','INTEGRATION_GUIDE.md','CONFIG_SCHEMA.json','REFERENCE_CONFIG.json','manifest.json','CANONICAL_CORE_HASHES.json','LICENSE','NOTICE','references/canonical-reference.png','references/canonical-demo-single-file.html','references/dark-glass-tokens.css','references/component-recipes.css','references/palette-presets.json','references/palette-engine.js','references/visual-regression-spec.md','screenshots/ACCEPTANCE_REPORT.md','screenshots/ACCEPTANCE_RESULT.json']
errors=[]
for rel in required:
    if not (ROOT/rel).exists(): errors.append('missing: '+rel)
manifest=json.loads((ROOT/'manifest.json').read_text(encoding='utf-8')) if (ROOT/'manifest.json').exists() else {}
for rel in (manifest.get('canonicalCore') or {}).values():
    if isinstance(rel,str) and not (ROOT/rel).exists(): errors.append('manifest target missing: '+rel)
hashes=json.loads((ROOT/'CANONICAL_CORE_HASHES.json').read_text(encoding='utf-8')) if (ROOT/'CANONICAL_CORE_HASHES.json').exists() else {}
for rel,digest in hashes.items():
    p=ROOT/rel
    if not p.exists(): errors.append('hash target missing: '+rel);continue
    if hashlib.sha256(p.read_bytes()).hexdigest()!=digest: errors.append('hash mismatch: '+rel)
# Palette system guards
preset=ROOT/'references/palette-presets.json'
if preset.exists():
    data=json.loads(preset.read_text(encoding='utf-8'))
    ids=[p.get('id') for p in data.get('palettes',[])]
    if ids!=[f'US-{i:02d}' for i in range(16)]: errors.append('palette IDs must be US-00..US-15')
    for p in data.get('palettes',[]):
        if len(p.get('colors',[]))!=5: errors.append('palette does not contain exactly 5 colors: '+str(p.get('id')))
if (ROOT/'references/theme-presets.json').exists(): errors.append('legacy theme-presets.json should not exist')
# Ensure docs do not advertise old 4-theme system / source-style literary names.
for rel in ['SKILL.md','README.md','README.zh-CN.md','DESIGN_SYSTEM.md','MASTER_PROMPT.md','COMPONENT_API.md']:
    p=ROOT/rel
    if not p.exists(): continue
    t=p.read_text(encoding='utf-8',errors='ignore')
    for token in ['Glacier Cyan','Deep Sea Blue','Amethyst Night','Graphite Silver']:
        if token in t: errors.append(f'legacy theme name found: {token} @ {rel}')
acc=ROOT/'screenshots/ACCEPTANCE_RESULT.json'
if acc.exists():
    result=json.loads(acc.read_text(encoding='utf-8'))
    if not result.get('passed'): errors.append('browser acceptance did not pass')
print(json.dumps({'passed':not errors,'errors':errors,'hashCount':len(hashes),'scope':'ui-design-only','paletteEngine':True,'paletteCount':16,'optionalIntegration':'fluidglass-ui'},ensure_ascii=False,indent=2))
sys.exit(0 if not errors else 1)
