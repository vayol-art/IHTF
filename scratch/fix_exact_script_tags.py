import os
import glob
import re

html_files = glob.glob("es/**/*.html", recursive=True) + glob.glob("en/**/*.html", recursive=True)

for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace any broken script tags leading into toggleLangDropdown with a single clean script tag
    pattern = r'<script>[\s\n]*<script>\s*function toggleLangDropdown'
    if re.search(pattern, content):
        content = re.sub(pattern, '<script>\n  function toggleLangDropdown', content)
        
    # Also clean any empty <script>\s*</script>
    content = re.sub(r'<script>\s*</script>', '', content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Exact script tags cleanup finished.")
