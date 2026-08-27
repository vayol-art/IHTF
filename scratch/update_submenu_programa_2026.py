import glob

html_files = glob.glob('**/*.html', recursive=True)
updated_count = 0

old_str = '>Programa de Mano<'
new_str = '>PROGRAMA 2026<'

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_str in content:
        new_content = content.replace(old_str, new_str)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_count += 1
        print(f"Updated: {filepath}")

print(f"\nTotal HTML files updated: {updated_count}")
