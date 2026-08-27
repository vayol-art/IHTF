import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

es_updated = 0
en_updated = 0

for filepath in html_files:
    if 'programa-de-mano' in filepath:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content

    # Spanish files logic
    if filepath.startswith('es\\') or filepath.startswith('es/'):
        # Match <a href="(...)agenda/" class="submenu-item">PROGRAMA 2026</a>
        pattern = r'(<a\s+href="([^"]*)agenda/"\s+class="submenu-item">PROGRAMA 2026</a>)'
        def es_replacer(match):
            full_match = match.group(1)
            rel_prefix = match.group(2)
            # Check if programa-de-mano is already there
            check_str = f'href="{rel_prefix}programa-de-mano/"'
            if check_str in content:
                return full_match
            return f'{full_match}\n          <a href="{rel_prefix}programa-de-mano/" class="submenu-item">Programa de Mano</a>'

        new_content = re.sub(pattern, es_replacer, new_content)
        if new_content != content:
            es_updated += 1

    # English files logic
    elif filepath.startswith('en\\') or filepath.startswith('en/'):
        # Match <a href="(...)agenda/" class="submenu-item">(Playbill|2026 PROGRAM)</a>
        pattern = r'<a\s+href="([^"]*)agenda/"\s+class="submenu-item">(?:Playbill|2026 PROGRAM)</a>'
        def en_replacer(match):
            rel_prefix = match.group(1)
            check_str = f'href="{rel_prefix}programa-de-mano/"'
            if check_str in content:
                return f'<a href="{rel_prefix}agenda/" class="submenu-item">2026 PROGRAM</a>\n          <a href="{rel_prefix}programa-de-mano/" class="submenu-item">Playbill</a>'
            return f'<a href="{rel_prefix}agenda/" class="submenu-item">2026 PROGRAM</a>\n          <a href="{rel_prefix}programa-de-mano/" class="submenu-item">Playbill</a>'

        new_content = re.sub(pattern, en_replacer, new_content)
        if new_content != content:
            en_updated += 1

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated submenu in: {filepath}")

print(f"\nTotal Spanish files updated: {es_updated}")
print(f"Total English files updated: {en_updated}")
