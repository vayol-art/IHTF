import glob

sections = [
    'agenda', 'calendario', 'contactanos', 'dia-internacional-del-nino',
    'eventos-adicionales', 'inscripciones', 'nosotros', 'obra',
    'obra-a-fuego', 'obra-carrusel', 'obra-hamlet', 'obra-historia-de-un-jabali',
    'obra-odd-man-out', 'obra-pundonor', 'obra-robinson-crusoe', 'obra-sueno',
    'obra-zombi-manifiesto', 'sponsors', 'teatros'
]

html_files = glob.glob('es/*.html') + glob.glob('en/*.html')

for fpath in html_files:
    if fpath.endswith('index.html'):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    updated = content
    for s in sections:
        updated = updated.replace(f'../{s}/#', f'{s}.html#')
        updated = updated.replace(f'../{s}/', f'{s}.html')
        updated = updated.replace(f'../{s}"', f'{s}.html"')
        updated = updated.replace(f'../{s}\'', f'{s}.html\'')
    
    if updated != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f'Fixed body links in {fpath}')
