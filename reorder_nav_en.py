import glob
import re

def reorder_nav(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    nav_match = re.search(r'(<nav class="main-nav"[^>]*>)(.*?)(</nav>)', content, re.DOTALL)
    if not nav_match:
        return

    nav_open = nav_match.group(1)
    nav_inner = nav_match.group(2)
    nav_close = nav_match.group(3)

    # 1. Programa (nav-dropdown-wrapper containing agenda)
    prog_match = re.search(r'(\s*<div class="nav-dropdown-wrapper">\s*<a href="[^"]*agenda\.html"[\s\S]*?</div>\s*</div>)', nav_inner)
    
    # 2. Sobre Nosotros (nav-dropdown-wrapper containing nosotros.html)
    sob_match = re.search(r'(\s*<div class="nav-dropdown-wrapper">\s*<a href="[^"]*nosotros\.html"[\s\S]*?</div>\s*</div>)', nav_inner)
    
    # 3. Contactanos
    cont_match = re.search(r'(\s*<a href="[^"]*contactanos\.html"[^>]*>.*?</a>)', nav_inner)
    
    # 4. Inscripciones (case insensitive, allowing 41st FESTIVAL REGISTRATIONS)
    insc_match = re.search(r'(\s*<a[^>]*>[^<]*41st FESTIVAL REGISTRATIONS[^<]*</a>)', nav_inner, re.IGNORECASE)
    
    # 5. Language selector
    lang_match = re.search(r'(\s*<div class="lang(?:uage)?-selector"[\s\S]*?</div>\s*</div>)', nav_inner)

    if not all([prog_match, sob_match, cont_match, insc_match, lang_match]):
        print(f"Skipping {filepath}, couldn't match all elements.")
        print([bool(x) for x in [prog_match, sob_match, cont_match, insc_match, lang_match]])
        return

    new_inner = prog_match.group(1) + cont_match.group(1) + sob_match.group(1) + insc_match.group(1) + lang_match.group(1) + "\n"
    
    new_nav = nav_open + new_inner + nav_close
    new_content = content[:nav_match.start()] + new_nav + content[nav_match.end():]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filepath}")

html_files = glob.glob('en/**/*.html', recursive=True)
for f in html_files:
    reorder_nav(f)
