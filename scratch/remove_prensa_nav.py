import glob
import re

def remove_prensa_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match main-nav
    nav_match = re.search(r'(<nav class="main-nav"[^>]*>)(.*?)(</nav>)', content, re.DOTALL)
    if not nav_match:
        return

    nav_open = nav_match.group(1)
    nav_inner = nav_match.group(2)
    nav_close = nav_match.group(3)

    if 'prensa/' not in nav_inner:
        return

    # Remove prensa link regex
    nav_inner_clean = re.sub(r'\s*<a href="[^"]*prensa/"[^>]*>[^<]*</a>', '', nav_inner)

    new_nav = nav_open + nav_inner_clean + nav_close
    new_content = content[:nav_match.start()] + new_nav + content[nav_match.end():]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Removed prensa link from {filepath}")

html_files = glob.glob('**/*.html', recursive=True)
for f in html_files:
    remove_prensa_from_file(f)

print("Prensa links removed from navigation.")
