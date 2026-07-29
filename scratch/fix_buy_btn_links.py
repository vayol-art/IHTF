import os
import re

BASE_DIR = "/Users/vanessa/Documents/IHTF"

def main():
    for root, dirs, files in os.walk(BASE_DIR):
        if ".git" in root or "scratch" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, BASE_DIR)

                with open(abs_path, "r", encoding="utf-8") as f:
                    content = f.read()

                modified = False

                if 'buyBtn.href = "agenda.html";' in content:
                    content = content.replace('buyBtn.href = "agenda.html";', 'buyBtn.href = "../agenda/";')
                    modified = True

                if 'buyBtn.href = "obra-" + play.id + ".html";' in content:
                    content = content.replace('buyBtn.href = "obra-" + play.id + ".html";', 'buyBtn.href = "../obra-" + play.id + "/";')
                    modified = True

                if modified:
                    with open(abs_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"Fixed buyBtn links in {rel_path}")

if __name__ == "__main__":
    main()
