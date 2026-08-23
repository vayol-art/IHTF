import glob
import re

gform_url = "https://docs.google.com/forms/d/e/1FAIpQLSczcvvSrHnWwI0TgvGq_Ad9R9uOO-UCv7Eqy5VTrn_HMan4-g/viewform?usp=header"

html_files = glob.glob('**/*.html', recursive=True)

nav_updated = 0
redirect_updated = 0

# 1. Update navigation links in all HTML files
pattern_nav = re.compile(r'href="([^"]*inscripciones/)"')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace navigation hrefs pointing to inscripciones/ with the Google Form URL and target="_blank"
    # Match: <a href="...inscripciones/">
    # Replace: <a href="https://docs.google.com/forms/d/e/1FAIpQLSczcvvSrHnWwI0TgvGq_Ad9R9uOO-UCv7Eqy5VTrn_HMan4-g/viewform?usp=header" target="_blank">
    if pattern_nav.search(content):
        # We need to make sure we add target="_blank" if not present
        def repl(match):
            return f'href="{gform_url}" target="_blank"'
        
        new_content = pattern_nav.sub(repl, content)
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            nav_updated += 1
            print(f"Updated nav link in: {filepath}")

# 2. Update es/inscripciones/index.html and en/inscripciones/index.html to redirect automatically
insc_pages = ['es/inscripciones/index.html', 'en/inscripciones/index.html']

for page in insc_pages:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add meta refresh and JS redirect in <head>
        redirect_code = f'<meta http-equiv="refresh" content="0;url={gform_url}" />\n  <script>window.location.replace("{gform_url}");</script>\n</head>'
        if '</head>' in content and 'window.location.replace' not in content:
            content = content.replace('</head>', redirect_code)
            with open(page, 'w', encoding='utf-8') as f:
                f.write(content)
            redirect_updated += 1
            print(f"Added automatic redirect to: {page}")
    except Exception as e:
        print(f"Error updating {page}: {e}")

print(f"\nTotal files updated with Google Form nav link: {nav_updated}")
print(f"Total inscripciones landing pages with auto-redirect: {redirect_updated}")
