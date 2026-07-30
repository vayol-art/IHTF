import os

def process_html_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "favicon.png" in content:
        print(f"Favicon already in {file_path}")
        return

    # Determine relative path to assets based on file depth relative to root
    # root index.html -> assets/favicon.png
    # es/*.html or en/*.html -> ../assets/favicon.png
    norm_path = os.path.normpath(file_path)
    parts = norm_path.split(os.sep)
    
    if "es" in parts or "en" in parts:
        href = "../assets/favicon.png"
    else:
        href = "assets/favicon.png"
        
    tag = f'  <link rel="icon" type="image/png" href="{href}" />\n'
    
    if "<head>" in content:
        new_content = content.replace("<head>", f"<head>\n{tag}", 1)
    elif "<head " in content:
        idx = content.find(">")
        new_content = content[:idx+1] + "\n" + tag + content[idx+1:]
    else:
        print(f"No <head> tag found in {file_path}")
        return

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Added favicon to {file_path}")

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

for dirpath, _, filenames in os.walk(root_dir):
    if "scratch" in dirpath or ".git" in dirpath:
        continue
    for filename in filenames:
        if filename.endswith(".html"):
            process_html_file(os.path.join(dirpath, filename))
