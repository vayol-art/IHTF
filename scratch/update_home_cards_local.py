import os

sections = [
    'obra-a-fuego',
    'obra-carrusel',
    'obra-hamlet',
    'obra-historia-de-un-jabali',
    'obra-odd-man-out',
    'obra-pundonor',
    'obra-robinson-crusoe',
    'obra-sueno',
    'obra-zombi-manifiesto',
    'obra'
]

for lang in ['es', 'en']:
    fpath = f'{lang}/index.html'
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    updated = content
    for s in sections:
        updated = updated.replace(f"window.location.href='{s}/'", f"window.location.href='{s}.html'")
        updated = updated.replace(f"window.location.href='{s}'", f"window.location.href='{s}.html'")
        updated = updated.replace(".html.html", ".html")
    
    if updated != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f'Updated local file: {fpath}')
