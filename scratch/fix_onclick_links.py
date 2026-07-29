import os
import re

BASE_DIR = "/Users/vanessa/Documents/IHTF"

PLAY_PAGES = [
    "obra-carrusel",
    "obra-zombi-manifiesto",
    "obra-historia-de-un-jabali",
    "obra-a-fuego",
    "obra-odd-man-out",
    "obra-sueno",
    "obra-robinson-crusoe",
    "obra-pundonor",
    "obra-hamlet",
    "obra",
    "nosotros",
    "agenda",
    "calendario",
    "eventos-adicionales",
    "dia-internacional-del-nino",
    "teatros",
    "sponsors",
    "contactanos",
    "inscripciones"
]

def fix_file(rel_path):
    abs_path = os.path.join(BASE_DIR, rel_path)
    if not os.path.exists(abs_path):
        return

    depth = len(rel_path.split("/")) - 1
    if depth == 0:
        return # root index.html

    with open(abs_path, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False

    # For depth 1 pages (es/index.html, en/index.html): relative prefix to sibling subfolders is '../'
    # For depth 2 pages (es/agenda/index.html, etc.): relative prefix to sibling subfolders is '../'
    prefix = "../"

    for page in PLAY_PAGES:
        # Match onclick="window.location.href='obra-carrusel.html'" or similar
        old_pattern_1 = f"onclick=\"window.location.href='{page}.html'\""
        new_pattern_1 = f"onclick=\"window.location.href='{prefix}{page}/'\""
        if old_pattern_1 in content:
            content = content.replace(old_pattern_1, new_pattern_1)
            modified = True

        old_pattern_2 = f"onclick=\"window.location.href='../{page}.html'\""
        new_pattern_2 = f"onclick=\"window.location.href='{prefix}{page}/'\""
        if old_pattern_2 in content:
            content = content.replace(old_pattern_2, new_pattern_2)
            modified = True

        old_pattern_3 = f"window.location.href = '{page}.html'"
        new_pattern_3 = f"window.location.href = '{prefix}{page}/'"
        if old_pattern_3 in content:
            content = content.replace(old_pattern_3, new_pattern_3)
            modified = True

    if modified:
        with open(abs_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed onclick links in {rel_path}")

def main():
    for root, dirs, files in os.walk(BASE_DIR):
        if ".git" in root or "scratch" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                rel_path = os.path.relpath(os.path.join(root, file), BASE_DIR)
                fix_file(rel_path)

    print("Onclick links fix complete!")

if __name__ == "__main__":
    main()
