import os
import glob

en_obra_files = glob.glob("en/obra-*/index.html")

for filepath in en_obra_files:
    folder_name = os.path.basename(os.path.dirname(filepath)) # e.g. obra-a-fuego
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We fix the block precisely
    old_broken = "        });\n          }, observerOptions);"
    if old_broken in content:
        content = content.replace(old_broken, "        }\n\n        // Secciones animadas (scroll reveal)\n        const sections = document.querySelectorAll(\"main > section, .venues-stack > section, .program-grid > article, .program-card, .play-card, .subpage-hero, .footer-wrapper\");\n        if (window.IntersectionObserver) {\n          const observerOptions = {\n            root: null,\n            rootMargin: \"0px 0px -60px 0px\",\n            threshold: 0.08\n          };\n          \n          const observer = new IntersectionObserver((entries, obs) => {")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed syntax in {filepath}")

print("Syntax check done.")
