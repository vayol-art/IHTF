import os
import re

BASE_DIR = "/Users/vanessa/Documents/IHTF"

SECTIONS = [
    "nosotros", "agenda", "calendario", "eventos-adicionales",
    "dia-internacional-del-nino", "teatros", "sponsors", "contactanos",
    "inscripciones", "obra", "obra-carrusel", "obra-zombi-manifiesto",
    "obra-historia-de-un-jabali", "obra-a-fuego", "obra-odd-man-out",
    "obra-sueno", "obra-robinson-crusoe", "obra-pundonor", "obra-hamlet"
]

def fix_page(rel_path):
    abs_path = os.path.join(BASE_DIR, rel_path)
    if not os.path.exists(abs_path):
        return

    depth = len(rel_path.split("/")) - 1
    if depth == 0:
        return # root index.html redirect

    lang = "es" if rel_path.startswith("es/") else "en"

    with open(abs_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Determine sibling prefix based on depth:
    # Depth 1 (es/index.html or en/index.html): sibling sections are in same directory (no ../)
    # Depth 2 (es/agenda/index.html or en/agenda/index.html): sibling sections require ../
    sibling_prefix = "" if depth == 1 else "../"
    home_href = "./#inicio" if depth == 1 else "../#inicio"

    # 1. Replace brand home link
    content = content.replace('href="../#inicio"', f'href="{home_href}"')
    content = content.replace('href="./#inicio"', f'href="{home_href}"')
    content = content.replace('href="index.html#inicio"', f'href="{home_href}"')

    # 2. Fix all href and onclick links to sections
    for sec in SECTIONS:
        # Href replacements
        content = re.sub(rf'href="(?:\.\./|\./)?{sec}\.html#', f'href="{sibling_prefix}{sec}/#', content)
        content = re.sub(rf'href="(?:\.\./|\./)?{sec}\.html"', f'href="{sibling_prefix}{sec}/"', content)
        content = re.sub(rf'href="(?:\.\./|\./)?{sec}/#', f'href="{sibling_prefix}{sec}/#', content)
        content = re.sub(rf'href="(?:\.\./|\./)?{sec}/"', f'href="{sibling_prefix}{sec}/"', content)

        # Onclick replacements
        content = re.sub(rf"onclick=\"window\.location\.href='(?:\.\./|\./)?{sec}\.html'\"", f"onclick=\"window.location.href='{sibling_prefix}{sec}/'\"", content)
        content = re.sub(rf"onclick=\"window\.location\.href='(?:\.\./|\./)?{sec}/'\"", f"onclick=\"window.location.href='{sibling_prefix}{sec}/'\"", content)

        # JS location.href replacements
        content = re.sub(rf"window\.location\.href = '(?:\.\./|\./)?{sec}\.html'", f"window.location.href = '{sibling_prefix}{sec}/'", content)
        content = re.sub(rf"window\.location\.href = '(?:\.\./|\./)?{sec}/'", f"window.location.href = '{sibling_prefix}{sec}/'", content)

    # 3. Fix Language Switcher Target JS
    # From es/index.html (depth 1) -> ../en/
    # From es/nosotros/index.html (depth 2) -> ../../en/nosotros/
    # From en/index.html (depth 1) -> ../es/
    # From en/nosotros/index.html (depth 2) -> ../../es/nosotros/
    section_name = "" if depth == 1 else rel_path.split("/")[1]

    if lang == "es":
        en_target = "../en/" if depth == 1 else f"../../en/{section_name}/"
        old_js = r'langOpts\[1\]\.addEventListener\("click",\s*function\s*\(\)\s*\{[^}]*\}\);'
        new_js = f"""langOpts[1].addEventListener("click", function () {{
            localStorage.setItem("preferred_lang", "en");
            window.location.href = "{en_target}";
          }});"""
        content = re.sub(old_js, new_js, content, flags=re.DOTALL)
    else:
        es_target = "../es/" if depth == 1 else f"../../es/{section_name}/"
        old_js = r'langOpts\[0\]\.addEventListener\("click",\s*function\s*\(\)\s*\{[^}]*\}\);'
        new_js = f"""langOpts[0].addEventListener("click", function () {{
            localStorage.setItem("preferred_lang", "es");
            window.location.href = "{es_target}";
          }});"""
        content = re.sub(old_js, new_js, content, flags=re.DOTALL)

    with open(abs_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Fixed navigation & onclick links in {rel_path} (Depth {depth})")

def main():
    for root, dirs, files in os.walk(BASE_DIR):
        if ".git" in root or "scratch" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                rel_path = os.path.relpath(os.path.join(root, file), BASE_DIR)
                fix_page(rel_path)

    print("All navigation & onclick links fixed successfully!")

if __name__ == "__main__":
    main()
