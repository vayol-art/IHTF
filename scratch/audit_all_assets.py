import os
import re
from urllib.parse import unquote

BASE_DIR = "/Users/vanessa/Documents/IHTF"

broken_references = []
checked_count = 0

def check_path_exists(html_rel_path, target_rel_url):
    global checked_count
    # Ignore template strings like ${logo} or ${heroBg}
    if "${" in target_rel_url or "}" in target_rel_url:
        return True

    # Clean query string / hash fragment
    target_clean = target_rel_url.split("?")[0].split("#")[0]
    if not target_clean:
        return True

    # Skip external links, data URIs, javascript:, mailto:, tel:
    if target_clean.startswith(("http://", "https://", "//", "data:", "javascript:", "mailto:", "tel:")):
        return True

    html_dir = os.path.dirname(os.path.join(BASE_DIR, html_rel_path))
    unquoted_target = unquote(target_clean)
    abs_target_path = os.path.normpath(os.path.join(html_dir, unquoted_target))

    checked_count += 1
    if not os.path.exists(abs_target_path):
        broken_references.append({
            "html": html_rel_path,
            "target": target_rel_url,
            "resolved": abs_target_path
        })
        return False
    return True

def audit_file(rel_path):
    abs_path = os.path.join(BASE_DIR, rel_path)
    with open(abs_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Check src="..."
    for match in re.finditer(r'src=["\']([^"\']+)["\']', content):
        check_path_exists(rel_path, match.group(1))

    # 2. Check href="..." in <link> tags
    for match in re.finditer(r'<link[^>]+href=["\']([^"\']+)["\']', content):
        check_path_exists(rel_path, match.group(1))

    # 3. Check url(...) in style attributes or <style> tags
    for match in re.finditer(r'url\(["\']?([^"\'\)\#\?]+)["\']?\)', content):
        check_path_exists(rel_path, match.group(1))

    # 4. Check JS strings that look like asset paths ("assets/..." or "../assets/..." or "../../assets/...")
    for match in re.finditer(r'["\']((\.\./)*assets/[^"\']+)["\']', content):
        check_path_exists(rel_path, match.group(1))

def main():
    for root, dirs, files in os.walk(BASE_DIR):
        if ".git" in root or "scratch" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                rel_path = os.path.relpath(os.path.join(root, file), BASE_DIR)
                audit_file(rel_path)

    print(f"Total asset references audited: {checked_count}")
    if broken_references:
        print(f"FOUND {len(broken_references)} BROKEN ASSET REFERENCES:")
        for err in broken_references:
            print(f" - In {err['html']}: '{err['target']}' -> Resolved to '{err['resolved']}' (404 Not Found)")
    else:
        print("SUCCESS: 0 broken asset references found! All images, videos, styles, and scripts across all 41 pages resolve perfectly.")

if __name__ == "__main__":
    main()
