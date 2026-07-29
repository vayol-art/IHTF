import os
import re

BASE_DIR = "/Users/vanessa/Documents/IHTF"

EXPECTED_FILES = [
    "index.html",
    "es/index.html",
    "es/nosotros/index.html",
    "es/agenda/index.html",
    "es/calendario/index.html",
    "es/eventos-adicionales/index.html",
    "es/dia-internacional-del-nino/index.html",
    "es/teatros/index.html",
    "es/sponsors/index.html",
    "es/contactanos/index.html",
    "es/inscripciones/index.html",
    "es/obra/index.html",
    "es/obra-carrusel/index.html",
    "es/obra-zombi-manifiesto/index.html",
    "es/obra-historia-de-un-jabali/index.html",
    "es/obra-a-fuego/index.html",
    "es/obra-odd-man-out/index.html",
    "es/obra-sueno/index.html",
    "es/obra-robinson-crusoe/index.html",
    "es/obra-pundonor/index.html",
    "es/obra-hamlet/index.html",
    "en/index.html",
    "en/nosotros/index.html",
    "en/agenda/index.html",
    "en/calendario/index.html",
    "en/eventos-adicionales/index.html",
    "en/dia-internacional-del-nino/index.html",
    "en/teatros/index.html",
    "en/sponsors/index.html",
    "en/contactanos/index.html",
    "en/inscripciones/index.html",
    "en/obra/index.html",
    "en/obra-carrusel/index.html",
    "en/obra-zombi-manifiesto/index.html",
    "en/obra-historia-de-un-jabali/index.html",
    "en/obra-a-fuego/index.html",
    "en/obra-odd-man-out/index.html",
    "en/obra-sueno/index.html",
    "en/obra-robinson-crusoe/index.html",
    "en/obra-pundonor/index.html",
    "en/obra-hamlet/index.html",
]

errors = []

for rel_path in EXPECTED_FILES:
    abs_path = os.path.join(BASE_DIR, rel_path)
    if not os.path.exists(abs_path):
        errors.append(f"Missing file: {rel_path}")
        continue
    
    with open(abs_path, "r", encoding="utf-8") as f:
        content = f.read()

    if rel_path == "index.html":
        if "http-equiv=\"refresh\"" not in content or "es/" not in content:
            errors.append(f"{rel_path}: Root index.html redirect is misconfigured")
        continue

    # Verify head tags
    if "<title>" not in content:
        errors.append(f"{rel_path}: Missing <title>")
    if 'meta name="description"' not in content:
        errors.append(f"{rel_path}: Missing meta description")
    if 'property="og:title"' not in content:
        errors.append(f"{rel_path}: Missing og:title")
    if 'property="og:url"' not in content:
        errors.append(f"{rel_path}: Missing og:url")
    if 'rel="canonical"' not in content:
        errors.append(f"{rel_path}: Missing canonical link")

    # Check for dead .html links in href or onclick
    dead_html_links = re.findall(r'(?:href|location\.href)\s*=\s*["\']([^"\']+\.html[^"\']*)["\']', content)
    for link in dead_html_links:
        if not link.startswith("http") and not link.startswith("//") and link != "index.html":
            errors.append(f"{rel_path}: Found old HTML link format: {link}")

    # Check iframe script
    if "window.top !== window.self" not in content:
        errors.append(f"{rel_path}: Missing iframe target handling script")

if errors:
    print(f"FAILED with {len(errors)} errors:")
    for err in errors:
        print(" -", err)
else:
    print("SUCCESS: All 41 files (es/ and en/ structure + root redirect) verified successfully! No dead .html links in href or onclick!")
