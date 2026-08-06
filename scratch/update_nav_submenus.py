import os
import glob

es_files = glob.glob('es/**/*.html', recursive=True)
en_files = glob.glob('en/**/*.html', recursive=True)

updated_es = 0
updated_en = 0

for filepath in es_files:
    if 'archivos-del-festival' in filepath:
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    rel_path = 'archivos-del-festival/'
    if os.path.dirname(filepath).replace('\\', '/').strip('/') != 'es':
        rel_path = '../archivos-del-festival/'

    new_item = f'<a href="{rel_path}" class="submenu-item">Archivos del Festival</a>'

    if 'Archivos del Festival' not in content:
        if '<a href="../sponsors/" class="submenu-item">Apoya IHTF</a>' in content:
            content = content.replace(
                '<a href="../sponsors/" class="submenu-item">Apoya IHTF</a>',
                '<a href="../sponsors/" class="submenu-item">Apoya IHTF</a>\n          ' + new_item
            )
            updated_es += 1
        elif '<a href="sponsors/" class="submenu-item">Apoya IHTF</a>' in content:
            content = content.replace(
                '<a href="sponsors/" class="submenu-item">Apoya IHTF</a>',
                '<a href="sponsors/" class="submenu-item">Apoya IHTF</a>\n          ' + new_item
            )
            updated_es += 1

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

for filepath in en_files:
    if 'archivos-del-festival' in filepath:
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    rel_path = 'archivos-del-festival/'
    if os.path.dirname(filepath).replace('\\', '/').strip('/') != 'en':
        rel_path = '../archivos-del-festival/'

    new_item = f'<a href="{rel_path}" class="submenu-item">Festival Archives</a>'

    if 'Festival Archives' not in content:
        if '<a href="../sponsors/" class="submenu-item">Support IHTF</a>' in content:
            content = content.replace(
                '<a href="../sponsors/" class="submenu-item">Support IHTF</a>',
                '<a href="../sponsors/" class="submenu-item">Support IHTF</a>\n          ' + new_item
            )
            updated_en += 1
        elif '<a href="sponsors/" class="submenu-item">Support IHTF</a>' in content:
            content = content.replace(
                '<a href="sponsors/" class="submenu-item">Support IHTF</a>',
                '<a href="sponsors/" class="submenu-item">Support IHTF</a>\n          ' + new_item
            )
            updated_en += 1

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print(f'Successfully updated {updated_es} ES files and {updated_en} EN files.')
