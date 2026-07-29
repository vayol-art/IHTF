import glob

OLD_DOMAIN = "https://vayol-art.github.io/IHTF"
NEW_DOMAIN = "https://ihtfmiami.org"

html_files = glob.glob("*.html") + glob.glob("es/*.html") + glob.glob("en/*.html")

updated_count = 0
for fpath in html_files:
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    if OLD_DOMAIN in content:
        new_content = content.replace(OLD_DOMAIN, NEW_DOMAIN)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        updated_count += 1
        print(f"Updated domain in {fpath}")

print(f"Total files updated: {updated_count}")
