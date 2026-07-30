import os
import re

ROOT_DIR = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF"
FAVICON_URL = "https://vayol-art.github.io/IHTF/assets/favicon.png"

def update_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content
    # Replace og:image
    new_content = re.sub(
        r'<meta\s+property="og:image"\s+content="[^"]*"\s*/?>',
        f'<meta property="og:image" content="{FAVICON_URL}" />',
        new_content
    )
    # Replace og:image:secure_url
    new_content = re.sub(
        r'<meta\s+property="og:image:secure_url"\s+content="[^"]*"\s*/?>',
        f'<meta property="og:image:secure_url" content="{FAVICON_URL}" />',
        new_content
    )
    # Replace og:image:type
    new_content = re.sub(
        r'<meta\s+property="og:image:type"\s+content="[^"]*"\s*/?>',
        '<meta property="og:image:type" content="image/png" />',
        new_content
    )
    # Replace twitter:image
    new_content = re.sub(
        r'<meta\s+name="twitter:image"\s+content="[^"]*"\s*/?>',
        f'<meta name="twitter:image" content="{FAVICON_URL}" />',
        new_content
    )

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated social preview tags in {file_path}")

for root, _, files in os.walk(ROOT_DIR):
    if "scratch" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith(".html"):
            update_file(os.path.join(root, file))
