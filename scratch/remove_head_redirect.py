import os
import glob
import re

en_files = glob.glob("en/**/*.html", recursive=True)

removed_count = 0
for filepath in en_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Pattern matching head redirect script in en/ files
    pattern = r'<script>\s*if\s*\(\s*localStorage\.getItem\("preferred_lang"\)\s*!==\s*"en"\s*\)\s*\{[\s\S]*?\}\s*</script>'
    
    if re.search(pattern, content):
        new_content = re.sub(pattern, '', content)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        removed_count += 1
        print(f"Removed head auto-redirect in: {filepath}")

print(f"Total head auto-redirects removed: {removed_count}")
