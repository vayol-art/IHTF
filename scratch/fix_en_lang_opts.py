import os
import glob
import re

en_obra_files = glob.glob("en/obra-*/index.html")

for filepath in en_obra_files:
    folder_name = os.path.basename(os.path.dirname(filepath)) # e.g. obra-a-fuego
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Old pattern for langOpts in en/obra-*/index.html
    old_block_pattern = r'const langOpts = document\.querySelectorAll\("\.lang-opt"\);\s*if \(langOpts\.length >= 2\) \{[\s\S]*?\}\s*\}'
    
    new_block = f"""const langOpts = document.querySelectorAll(".lang-opt");
        if (langOpts.length >= 2) {{
          langOpts[0].addEventListener("click", function () {{
            localStorage.setItem("preferred_lang", "en");
            langSelector.classList.remove("open");
            langBtn.setAttribute("aria-expanded", "false");
          }});
          langOpts[1].addEventListener("click", function () {{
            localStorage.setItem("preferred_lang", "es");
            window.location.href = "../../es/{folder_name}/";
          }});
        }}"""
        
    new_content = re.sub(old_block_pattern, new_block, content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Fixed langOpts in {filepath}")

print("Done fixing en langOpts.")
