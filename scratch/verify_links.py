import os
import glob
import re

errors = []
html_files = glob.glob('es/*.html') + glob.glob('en/*.html')

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    if '../../' in content:
        for line in content.splitlines():
            if '../../' in line and 'http' not in line:
                errors.append(f'{fpath}: found ../.. in line: {line.strip()[:60]}')

    if '.html.html' in content:
        errors.append(f'{fpath}: found .html.html')

    hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
    base_dir = os.path.dirname(fpath)
    for h in hrefs:
        if h.startswith(('http:', 'https:', 'mailto:', 'tel:', '//', 'data:')):
            continue
        clean_h = h.split('?')[0].split('#')[0]
        if not clean_h:
            continue
        target_path = os.path.normpath(os.path.join(base_dir, clean_h))
        if not os.path.exists(target_path):
            errors.append(f'{fpath}: href target missing: {clean_h} -> {target_path}')

if not errors:
    print('ALL VERIFICATIONS PASSED SUCCESSFULLY! No broken links or missing files.')
else:
    print(f'Found {len(errors)} issues:')
    for e in errors:
        print('  -', e)
