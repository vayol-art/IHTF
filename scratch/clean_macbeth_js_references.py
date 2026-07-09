import os

target_dir = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF"

for filename in os.listdir(target_dir):
    if filename.endswith(".html") and (filename.startswith("obra-") or filename == "obra.html"):
        filepath = os.path.join(target_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        new_content = content
        new_content = new_content.replace('        "habitacion-macbeth": "habitacion-macbeth.jpg",\n', '')
        new_content = new_content.replace('        "habitacion-macbeth": "card-macbeth.jpg",\n', '')
        new_content = new_content.replace('        "habitacion-macbeth": "habitacion-macbeth.jpg",\r\n', '')
        new_content = new_content.replace('        "habitacion-macbeth": "card-macbeth.jpg",\r\n', '')
        
        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Cleaned JS objects in {filename}")
