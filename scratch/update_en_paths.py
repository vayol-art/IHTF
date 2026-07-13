import os
import re

en_dir = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF\en"
html_files = [
    "index.html",
    "agenda.html",
    "calendario.html",
    "contactanos.html",
    "dia-internacional-del-nino.html",
    "eventos-adicionales.html",
    "nosotros.html",
    "sponsors.html",
    "teatros.html",
    "obra.html",
    "obra-a-fuego.html",
    "obra-carrusel.html",
    "obra-hamlet.html",
    "obra-historia-de-un-jabali.html",
    "obra-odd-man-out.html",
    "obra-robinson-crusoe.html",
    "obra-sueno.html",
    "obra-zombi-manifiesto.html"
]

target_logic = """        // Language options click behavior
        const langOpts = document.querySelectorAll(".lang-opt");
        if (langOpts.length >= 2) {
          langOpts[0].addEventListener("click", function() { // English
            let filename = window.location.pathname.split("/").pop() || "index.html";
            window.location.href = "en/" + filename;
          });
          langOpts[1].addEventListener("click", function() { // Spanish
            langSelector.classList.remove("open");
            langBtn.setAttribute("aria-expanded", "false");
          });
        }"""

replacement_logic = """        // Language options click behavior
        const langOpts = document.querySelectorAll(".lang-opt");
        if (langOpts.length >= 2) {
          langOpts[0].addEventListener("click", function() { // English
            langSelector.classList.remove("open");
            langBtn.setAttribute("aria-expanded", "false");
          });
          langOpts[1].addEventListener("click", function() { // Spanish
            let filename = window.location.pathname.split("/").pop() || "index.html";
            window.location.href = "../" + filename;
          });
        }"""

for filename in html_files:
    filepath = os.path.join(en_dir, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update css references
    content = re.sub(r'href="([^"]+\.css)', r'href="../\1', content)
    
    # 2. Update data.js script reference
    content = content.replace('src="data.js"', 'src="../data.js"')
    
    # 3. Update asset paths (e.g. images, videos)
    content = content.replace('src="assets/', 'src="../assets/')
    
    # 4. Update the redirection logic
    content = content.replace(target_logic, replacement_logic)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated paths and redirection logic in en/{filename}")
