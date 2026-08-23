import glob

old_code = 'var _ctct_m = "6b84846d-b4c9-4b02-867d-09c8a7ac5d40";'
new_code = 'var _ctct_m = "a79e89c0998befa80793c5464469c842";'

html_files = glob.glob('**/*.html', recursive=True)
updated_count = 0

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_code in content:
        new_content = content.replace(old_code, new_code)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_count += 1
        print(f"Updated: {filepath}")

print(f"\nTotal files updated with correct Constant Contact account ID: {updated_count}")
