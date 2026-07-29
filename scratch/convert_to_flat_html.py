import os
import shutil
import re

SECTIONS = [
    "agenda",
    "calendario",
    "contactanos",
    "dia-internacional-del-nino",
    "eventos-adicionales",
    "inscripciones",
    "nosotros",
    "obra",
    "obra-a-fuego",
    "obra-carrusel",
    "obra-hamlet",
    "obra-historia-de-un-jabali",
    "obra-odd-man-out",
    "obra-pundonor",
    "obra-robinson-crusoe",
    "obra-sueno",
    "obra-zombi-manifiesto",
    "sponsors",
    "teatros"
]

LANGS = ["es", "en"]

def update_html_content(content, lang, is_subpage, page_name=None):
    # If it's a subpage (was es/seccion/index.html, now es/seccion.html)
    if is_subpage:
        # Depth changed from es/seccion/ (2 levels) to es/ (1 level)
        # 1. Update root relative paths (CSS, fonts, assets)
        content = content.replace("../../", "../")
        
        # 2. Update brand logo / home link
        content = content.replace('href="../#inicio"', 'href="index.html#inicio"')
        content = content.replace('href="../#programacion"', 'href="index.html#programacion"')
        content = content.replace('href="../"', 'href="index.html"')

        # 3. Update canonical and og meta URLs
        for s in SECTIONS:
            content = content.replace(f"https://vayol-art.github.io/IHTF/{lang}/{s}/", f"https://vayol-art.github.io/IHTF/{lang}/{s}.html")

        # 4. Update language toggle window.location.href
        other_lang = "en" if lang == "es" else "es"
        # In subpages, old was: window.location.href = "../../en/nosotros/"
        # New should be: window.location.href = "../en/nosotros.html"
        for s in SECTIONS:
            content = content.replace(f'window.location.href = "../../{other_lang}/{s}/";', f'window.location.href = "../{other_lang}/{s}.html";')
            content = content.replace(f'window.location.href = "../../{other_lang}/{s}"', f'window.location.href = "../{other_lang}/{s}.html"')
        # Handle fallback for home in lang switcher if any
        content = content.replace(f'window.location.href = "../../{other_lang}/";', f'window.location.href = "../{other_lang}/index.html";')

        # 5. Update navigation links (was href="../agenda/", now href="agenda.html")
        for s in SECTIONS:
            content = content.replace(f'href="../{s}/#', f'href="{s}.html#')
            content = content.replace(f'href="../{s}/"', f'href="{s}.html"')
            content = content.replace(f'href="../{s}"', f'href="{s}.html"')

    else: # es/index.html or en/index.html
        # Update navigation links (was href="agenda/", now href="agenda.html")
        for s in SECTIONS:
            content = content.replace(f'href="{s}/#', f'href="{s}.html#')
            content = content.replace(f'href="{s}/"', f'href="{s}.html"')
            pattern = re.compile(r'href="' + re.escape(s) + r'"')
            content = pattern.sub(f'href="{s}.html"', content)

        # Update language toggle if needed
        other_lang = "en" if lang == "es" else "es"
        for s in SECTIONS:
            content = content.replace(f'window.location.href = "../{other_lang}/{s}/";', f'window.location.href = "../{other_lang}/{s}.html";')

    return content

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"Base Directory: {base_dir}")

    # Process subpages in es/ and en/
    for lang in LANGS:
        lang_dir = os.path.join(base_dir, lang)
        
        # 1. Update lang/index.html
        index_path = os.path.join(lang_dir, "index.html")
        if os.path.exists(index_path):
            with open(index_path, "r", encoding="utf-8") as f:
                content = f.read()
            new_content = update_html_content(content, lang, is_subpage=False)
            with open(index_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {lang}/index.html")

        # 2. Move and update subfolder index.html pages
        for section in SECTIONS:
            sec_dir = os.path.join(lang_dir, section)
            sec_index = os.path.join(sec_dir, "index.html")
            target_html = os.path.join(lang_dir, f"{section}.html")

            if os.path.exists(sec_index):
                with open(sec_index, "r", encoding="utf-8") as f:
                    content = f.read()
                
                new_content = update_html_content(content, lang, is_subpage=True, page_name=section)
                
                with open(target_html, "w", encoding="utf-8") as f:
                    f.write(new_content)
                
                print(f"Created {lang}/{section}.html from {lang}/{section}/index.html")
                
                # Remove old index.html and directory
                os.remove(sec_index)
                try:
                    os.rmdir(sec_dir)
                    print(f"Removed directory {lang}/{section}/")
                except Exception as e:
                    print(f"Could not remove directory {lang}/{section}/: {e}")
            else:
                print(f"Warning: {sec_index} does not exist.")

if __name__ == "__main__":
    main()
