import os
import glob
import re

html_files = glob.glob("es/**/*.html", recursive=True) + glob.glob("en/**/*.html", recursive=True)

# Pattern matching the redundant langBtn click listener that causes double-toggle
pattern = r'langBtn\.addEventListener\s*\(\s*"click"\s*,\s*function\s*\([^\)]*\)\s*\{[\s\S]*?langSelector\.classList\.toggle\s*\(\s*"open"\s*\)[\s\S]*?\}\s*\)\s*;'

count = 0
for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if re.search(pattern, content):
        new_content = re.sub(pattern, '', content)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1
        print(f"Removed redundant langBtn listener in: {filepath}")

print(f"Total files cleaned of double-toggle: {count}")
