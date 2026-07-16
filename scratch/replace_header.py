import os
import glob

# Paths
base_dir = "/Users/inhaus/Documents/IHTF"
es_files = glob.glob(os.path.join(base_dir, "*.html"))
en_files = glob.glob(os.path.join(base_dir, "en", "*.html"))

# Spanish replacement
es_target = """<a href="nosotros.html#compania" class="submenu-item">La Compañía</a>
          <a href="nosotros.html#personal" class="submenu-item">Personal</a>
          <a href="nosotros.html#premios" class="submenu-item">Premios</a>"""
es_replacement = """<a href="nosotros.html#compania" class="submenu-item">Historia del Festival</a>
          <a href="nosotros.html#personal" class="submenu-item">Personal</a>"""

# English replacement
en_target = """<a href="nosotros.html#compania" class="submenu-item">The Company</a>
          <a href="nosotros.html#personal" class="submenu-item">Staff</a>
          <a href="nosotros.html#premios" class="submenu-item">Awards</a>"""
en_replacement = """<a href="nosotros.html#compania" class="submenu-item">Festival History</a>
          <a href="nosotros.html#personal" class="submenu-item">Staff</a>"""

for file_path in es_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    if es_target in content:
        content = content.replace(es_target, es_replacement)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

for file_path in en_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    if en_target in content:
        content = content.replace(en_target, en_replacement)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Done replacing header navigation.")
