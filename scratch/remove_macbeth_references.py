import os
import re

target_dir = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF"

for filename in os.listdir(target_dir):
    if filename.endswith(".html") and filename != "obra-habitacion-macbeth.html":
        filepath = os.path.join(target_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # We look for <article ...> ... </article> blocks containing "obra-habitacion-macbeth.html"
        pattern = re.compile(r'(<article\b[^>]*>.*?</article>)', re.DOTALL)
        matches = pattern.findall(content)
        modified = False
        for match in matches:
            if "obra-habitacion-macbeth.html" in match:
                content = content.replace(match, "")
                modified = True
                print(f"Removed Macbeth card from {filename}")
        
        if modified:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
