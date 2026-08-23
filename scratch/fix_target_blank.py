import glob

html_files = glob.glob('**/*.html', recursive=True)

old_script = """          if (href && !href.startsWith('#') && !href.startsWith('javascript:') && !href.startsWith('mailto:') && !href.startsWith('tel:')) {
            link.setAttribute('target', '_top');
          }"""

new_script = """          if (href && !href.startsWith('#') && !href.startsWith('javascript:') && !href.startsWith('mailto:') && !href.startsWith('tel:')) {
            var currentTarget = link.getAttribute('target');
            if (currentTarget !== '_blank') {
              link.setAttribute('target', '_top');
            }
          }"""

updated_count = 0

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_script in content:
        new_content = content.replace(old_script, new_script)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_count += 1
        print(f"Updated iframe target script in: {filepath}")

print(f"\nTotal files updated: {updated_count}")
