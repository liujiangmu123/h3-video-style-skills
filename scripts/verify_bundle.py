"""Verify exported source bytes, declared pairs, and every packaged source file."""
from pathlib import Path
import hashlib
import json
import zipfile

root = Path(__file__).resolve().parents[1]
catalog = json.loads((root / 'catalog.json').read_text(encoding='utf-8'))
skills = catalog['skills']
errors = []
names = {s['name']: s for s in skills}
if len(names) != catalog['skill_count'] or len(skills) != 22:
    errors.append('Skill count mismatch')
source_count = 0
for s in skills:
    folder = root / s['path']
    actual = {p.relative_to(folder).as_posix() for p in folder.rglob('*') if p.is_file()}
    if actual != set(s['files']): errors.append(s['name'] + ': file set mismatch')
    pair = s.get('pair')
    if pair and (pair not in names or names[pair].get('pair') != s['name']):
        errors.append(s['name'] + ': invalid pair')
    for rel, expected in s['files'].items():
        p = folder / rel
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != expected['sha256']:
            errors.append(s['name'] + '/' + rel + ': source hash mismatch')
        source_count += 1
    try:
        with zipfile.ZipFile(root / s['package']) as z:
            prefix = s['name'] + '/'
            manifest = json.loads(z.read(prefix + 'skill.manifest.json'))
            if manifest['name'] != s['name'] or manifest['version'] != s['version']:
                errors.append(s['name'] + ': package identity mismatch')
            packaged = {e['path']: e for e in manifest['files']}
            if set(packaged) != set(s['files']): errors.append(s['name'] + ': package manifest mismatch')
            if set(z.namelist()) != {prefix + p for p in s['files']} | {prefix + 'skill.manifest.json'}:
                errors.append(s['name'] + ': package member mismatch')
            for rel, expected in s['files'].items():
                digest = hashlib.sha256(z.read(prefix + rel)).hexdigest()
                if digest != expected['sha256'] or packaged[rel]['sha256'] != digest:
                    errors.append(s['name'] + '/' + rel + ': package hash mismatch')
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as exc:
        errors.append(s['name'] + ': ' + str(exc))
print(json.dumps({'skills': len(skills), 'source_files': source_count, 'packages': len(skills),
                  'errors': errors, 'aesthetics_verified': False}, ensure_ascii=False, indent=2))
raise SystemExit(1 if errors else 0)
