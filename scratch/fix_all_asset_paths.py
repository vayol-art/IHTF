import os
import re

BASE_DIR = "/Users/vanessa/Documents/IHTF"

CSS_FILES = [
    "style.css", "fonts.css", "nosotros.css", "agenda.css", "calendario.css",
    "contactanos.css", "dia-internacional-del-nino.css", "eventos-adicionales.css",
    "inscripciones.css", "obra.css", "sponsors.css", "teatros.css"
]

def fix_file(rel_path):
    abs_path = os.path.join(BASE_DIR, rel_path)
    if not os.path.exists(abs_path):
        return

    depth = len(rel_path.split("/")) - 1
    if depth == 0:
        return # root index.html redirect

    with open(abs_path, "r", encoding="utf-8") as f:
        content = f.read()

    correct_assets = "../assets/" if depth == 1 else "../../assets/"
    correct_root_rel = "../" if depth == 1 else "../../"

    # 1. Normalize all variations of assets/ (../../../assets/, ../assets/, assets/) to exact correct_assets
    content = re.sub(r'(\.\./)+assets/', correct_assets, content)
    content = re.sub(r'(?<![\w/\.\-])assets/', correct_assets, content)

    # 2. Normalize all css files
    for css in CSS_FILES:
        content = re.sub(rf'(\.\./)+{re.escape(css)}', f'{correct_root_rel}{css}', content)
        content = re.sub(rf'(?<![\w/\.\-]){re.escape(css)}', f'{correct_root_rel}{css}', content)

    # 3. Normalize data.js
    content = re.sub(r'(\.\./)+data\.js', f'{correct_root_rel}data.js', content)

    # 4. In obra/index.html JS logic, ensure dynamic logo loading uses correct_root_rel
    if rel_path in ["es/obra/index.html", "en/obra/index.html"]:
        content = content.replace('src="${theaterLogoSrc}"', 'src="${theaterLogoSrc.startsWith(\'..\') ? theaterLogoSrc : \'../../\' + theaterLogoSrc}"')
        content = content.replace('src="${play.image}"', 'src="${play.image.startsWith(\'..\') ? play.image : \'../../\' + play.image}"')

    with open(abs_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Normalized asset paths in {rel_path} (Depth {depth}) -> {correct_assets}")

def main():
    for root, dirs, files in os.walk(BASE_DIR):
        if ".git" in root or "scratch" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                rel_path = os.path.relpath(os.path.join(root, file), BASE_DIR)
                fix_file(rel_path)

if __name__ == "__main__":
    main()
