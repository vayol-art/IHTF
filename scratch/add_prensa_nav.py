import glob
import re

def update_nav_in_file(filepath):
    normalized_path = filepath.replace('\\', '/')
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match main-nav
    nav_match = re.search(r'(<nav class="main-nav"[^>]*>)(.*?)(</nav>)', content, re.DOTALL)
    if not nav_match:
        return

    nav_open = nav_match.group(1)
    nav_inner = nav_match.group(2)
    nav_close = nav_match.group(3)

    is_english = normalized_path.startswith('en/') or '/en/' in normalized_path
    link_text = "PRESS" if is_english else "PRENSA"

    # Remove existing prensa link if present to re-write cleanly
    nav_inner_clean = re.sub(r'\s*<a href="[^"]*prensa/">[^<]*</a>', '', nav_inner)

    match_insc = re.search(r'href="([^"]*inscripciones/)"', nav_inner_clean)
    if match_insc:
        prefix = match_insc.group(1).rsplit('inscripciones/', 1)[0]
    else:
        match_cont = re.search(r'href="([^"]*contactanos/)"', nav_inner_clean)
        if match_cont:
            prefix = match_cont.group(1).rsplit('contactanos/', 1)[0]
        else:
            prefix = "../" if normalized_path.count('/') > 1 else ""

    prensa_link = f'\n        <a href="{prefix}prensa/">{link_text}</a>'

    new_nav_inner = nav_inner_clean.rstrip() + prensa_link + "\n      "
    new_nav = nav_open + new_nav_inner + nav_close

    new_content = content[:nav_match.start()] + new_nav + content[nav_match.end():]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

html_files = glob.glob('**/*.html', recursive=True)
for f in html_files:
    if f.endswith('prensa/index.html') or f.endswith('prensa\\index.html'):
        continue
    update_nav_in_file(f)
print("Updated navs successfully")
