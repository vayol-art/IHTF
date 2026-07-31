import os
import re

BASE_DIR = "/Users/inhaus/Documents/IHTF"

PLAY_SLUGS = [
    "obra-a-fuego",
    "obra-carrusel",
    "obra-hamlet",
    "obra-historia-de-un-jabali",
    "obra-odd-man-out",
    "obra-pundonor",
    "obra-robinson-crusoe",
    "obra-sueno",
    "obra-zombi-manifiesto"
]

ALL_SLUGS = PLAY_SLUGS + [
    "agenda",
    "calendario",
    "contactanos",
    "dia-internacional-del-nino",
    "eventos-adicionales",
    "inscripciones",
    "nosotros",
    "sponsors",
    "teatros"
]

total_files_modified = 0

for lang in ["es", "en"]:
    lang_dir = os.path.join(BASE_DIR, lang)
    if not os.path.exists(lang_dir):
        continue
    
    for root, dirs, files in os.walk(lang_dir):
        for file in files:
            if not file.endswith(".html"):
                continue
            
            filepath = os.path.join(root, file)
            rel_from_lang = os.path.relpath(filepath, lang_dir)
            parts = rel_from_lang.split(os.sep)
            
            is_lang_root = (len(parts) == 1 and parts[0] == "index.html")
            prefix = "" if is_lang_root else "../"
            
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                
            orig_content = content
            
            for slug in ALL_SLUGS:
                # Match onclick="window.location.href='obra-pundonor.html'" or with ../ or without .html or with /
                # Pattern handles 'slug.html', 'slug/', '../slug.html', etc. inside single or double quotes
                pattern_onclick = re.compile(
                    r"onclick=(?P<q1>[\"'])window\.location\.href\s*=\s*(?P<q2>['\"])(?:\./|\.\./)*" + re.escape(slug) + r"(?:\.html|/)?(?P=q2)(?P=q1)"
                )
                target_onclick = f"onclick=\"window.location.href='{prefix}{slug}/'\""
                content = pattern_onclick.sub(target_onclick, content)
                
                # Match href="slug.html" or href="../slug.html"
                pattern_href = re.compile(
                    r'href="(?:\./|\.\./)*' + re.escape(slug) + r'\.html(#.*?)?"'
                )
                def href_repl(m, p=prefix, s=slug):
                    fragment = m.group(1) if m.group(1) else ""
                    return f'href="{p}{s}/{fragment}"'
                content = pattern_href.sub(href_repl, content)

            if content != orig_content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                total_files_modified += 1
                print(f"Modified: {os.path.relpath(filepath, BASE_DIR)}")

print(f"\nDone! Modified {total_files_modified} files.")
