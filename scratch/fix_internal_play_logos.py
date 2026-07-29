import os
import re

BASE_DIR = "/Users/vanessa/Documents/IHTF"

def fix_file(rel_path):
    abs_path = os.path.join(BASE_DIR, rel_path)
    if not os.path.exists(abs_path):
        return

    with open(abs_path, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False

    # Fix logosContainer rendering in Spanish play pages (logo)
    # Target: logosContainer.innerHTML += `<img src="${logo}" alt="Logo Teatro" ${extraStyle}>`;
    old_es_logo = r'logosContainer\.innerHTML\s*\+=\s*`<img src="\${logo}" alt="Logo Teatro" \${extraStyle}>`;'
    new_es_logo = r'let cleanLogo = logo.startsWith("../../") ? logo : (logo.startsWith("../") ? "../" + logo : "../../" + logo);\n        logosContainer.innerHTML += `<img src="${cleanLogo}" alt="Logo Teatro" ${extraStyle}>`;'

    if re.search(old_es_logo, content):
        content = re.sub(old_es_logo, new_es_logo, content)
        modified = True

    # Fix logosContainer rendering in English play pages (logoSrc)
    # Target: logosContainer.innerHTML += `<img src="${logoSrc}" alt="Logo Teatro" ${extraStyle}>`;
    old_en_logo = r'logosContainer\.innerHTML\s*\+=\s*`<img src="\${logoSrc}" alt="Logo Teatro" \${extraStyle}>`;'
    new_en_logo = r'let cleanLogo = logoSrc.startsWith("../../") ? logoSrc : (logoSrc.startsWith("../") ? "../" + logoSrc : "../../" + logoSrc);\n        logosContainer.innerHTML += `<img src="${cleanLogo}" alt="Logo Teatro" ${extraStyle}>`;'

    if re.search(old_en_logo, content):
        content = re.sub(old_en_logo, new_en_logo, content)
        modified = True

    # Fix heroBg in obra/index.html
    # Target: assets/hero-a-fuego.jpg or assets/${posterMap[playId]}
    if 'const heroBg =' in content:
        content = content.replace('"assets/hero-a-fuego.jpg"', '"../../assets/hero-a-fuego.jpg"')
        content = content.replace('`assets/${posterMap[playId]}`', '`../../assets/${posterMap[playId]}`')
        modified = True

    if modified:
        with open(abs_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed internal play logos in {rel_path}")

def main():
    for root, dirs, files in os.walk(BASE_DIR):
        if ".git" in root or "scratch" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                rel_path = os.path.relpath(os.path.join(root, file), BASE_DIR)
                fix_file(rel_path)

    print("Internal play logos fix complete!")

if __name__ == "__main__":
    main()
