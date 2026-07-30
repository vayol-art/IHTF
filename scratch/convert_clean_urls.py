import os
import glob
import re

ROOT_DIR = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF"

def convert_content(content, is_lang_root=False, lang_code="es"):
    # 1. Update canonical, og:url, twitter:url meta tags removing .html
    # e.g. https://vayol-art.github.io/IHTF/es/nosotros.html -> https://vayol-art.github.io/IHTF/es/nosotros/
    # e.g. https://vayol-art.github.io/IHTF/es/index.html -> https://vayol-art.github.io/IHTF/es/
    content = re.sub(r'href="(https://vayol-art\.github\.io/IHTF/(?:es|en)/[^"]*?)\.html"', r'href="\1/"', content)
    content = re.sub(r'content="(https://vayol-art\.github\.io/IHTF/(?:es|en)/[^"]*?)\.html"', r'content="\1/"', content)
    content = content.replace("https://vayol-art.github.io/IHTF/es/index.html", "https://vayol-art.github.io/IHTF/es/")
    content = content.replace("https://vayol-art.github.io/IHTF/en/index.html", "https://vayol-art.github.io/IHTF/en/")

    # 2. Adjust relative asset paths for subpages (depth 2)
    if not is_lang_root:
        # Increase ../ to ../../ for styles, fonts, assets, js
        content = content.replace('href="../', 'href="../../')
        content = content.replace('src="../', 'src="../../')

    # 3. Update href links to pages
    # List of all page slugs
    pages = [
        "agenda", "calendario", "contactanos", "dia-internacional-del-nino",
        "eventos-adicionales", "inscripciones", "nosotros", "obra",
        "obra-a-fuego", "obra-carrusel", "obra-hamlet", "obra-historia-de-un-jabali",
        "obra-odd-man-out", "obra-pundonor", "obra-robinson-crusoe", "obra-sueno",
        "obra-zombi-manifiesto", "sponsors", "teatros"
    ]

    prefix = "" if is_lang_root else "../"

    # Replace href="page.html" or href="page.html#hash" or href="page.html?query"
    for page in sorted(pages, key=len, reverse=True): # longest first to avoid partial matches
        # e.g. href="nosotros.html#compania" -> href="../nosotros/#compania" or "nosotros/#compania"
        content = re.sub(r'href="' + re.escape(page) + r'\.html(#.*?)?"', r'href="' + prefix + page + r'/\1"', content)
        content = re.sub(r'href="' + re.escape(page) + r'\.html(\?.*?)?"', r'href="' + prefix + page + r'/\1"', content)

    # Replace href="index.html#inicio" or href="index.html"
    if is_lang_root:
        content = content.replace('href="index.html#inicio"', 'href="#inicio"')
        content = content.replace('href="index.html"', 'href="./"')
    else:
        content = content.replace('href="index.html#inicio"', 'href="../#inicio"')
        content = content.replace('href="index.html"', 'href="../"')

    # 4. Update language switcher JS link
    # In subpage (depth 2): window.location.href = "../en/nosotros.html"; -> window.location.href = "../../en/nosotros/";
    # In lang root (depth 1): window.location.href = "../en/index.html"; -> window.location.href = "../en/";
    target_lang = "en" if lang_code == "es" else "es"
    if is_lang_root:
        content = re.sub(r'window\.location\.href\s*=\s*"(\.\./' + target_lang + r'/)(.*?)(\.html)?";', r'window.location.href = "\1";', content)
    else:
        # window.location.href = "../en/page.html"; -> window.location.href = "../../en/page/";
        def lang_repl(m):
            page_file = m.group(2)
            page_name = page_file.replace('.html', '')
            if page_name == 'index' or not page_name:
                return f'window.location.href = "../../{target_lang}/";'
            return f'window.location.href = "../../{target_lang}/{page_name}/";'

        content = re.sub(r'window\.location\.href\s*=\s*"\.\./(' + target_lang + r')/(.*?)";', lang_repl, content)

    return content

def run():
    for lang in ["es", "en"]:
        lang_dir = os.path.join(ROOT_DIR, lang)
        if not os.path.exists(lang_dir):
            continue
        
        # Process index.html in lang_dir
        lang_index_path = os.path.join(lang_dir, "index.html")
        if os.path.exists(lang_index_path):
            with open(lang_index_path, "r", encoding="utf-8") as f:
                c = f.read()
            new_c = convert_content(c, is_lang_root=True, lang_code=lang)
            with open(lang_index_path, "w", encoding="utf-8") as f:
                f.write(new_c)
            print(f"Updated root lang index: {lang_index_path}")

        # Process all other html files in lang_dir
        for item in os.listdir(lang_dir):
            if item.endswith(".html") and item != "index.html":
                page_name = item[:-5] # remove .html
                src_file = os.path.join(lang_dir, item)
                dest_dir = os.path.join(lang_dir, page_name)
                os.makedirs(dest_dir, exist_ok=True)
                dest_file = os.path.join(dest_dir, "index.html")
                
                with open(src_file, "r", encoding="utf-8") as f:
                    c = f.read()
                
                new_c = convert_content(c, is_lang_root=False, lang_code=lang)
                
                with open(dest_file, "w", encoding="utf-8") as f:
                    f.write(new_c)
                
                # Delete original .html file
                os.remove(src_file)
                print(f"Moved {src_file} -> {dest_file}")

if __name__ == "__main__":
    run()
