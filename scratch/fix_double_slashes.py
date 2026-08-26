import os
import glob

html_files = glob.glob("es/**/*.html", recursive=True) + glob.glob("en/**/*.html", recursive=True)

fixed_count = 0
for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if '//";' in content:
        new_content = content.replace('//";', '/";')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Fixed double slashes in: {filepath}")
        fixed_count += 1

print(f"Total files fixed: {fixed_count}")
