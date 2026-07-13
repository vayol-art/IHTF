import os

target_dir = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF"
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

target_logic = """        // Language Selector Dropdown logic
        const langSelector = document.querySelector(".lang-selector");
        const langBtn = document.querySelector(".lang-btn");
        if (langSelector && langBtn) {
          langBtn.addEventListener("click", function (e) {
            e.stopPropagation();
            const isOpen = langSelector.classList.toggle("open");
            langBtn.setAttribute("aria-expanded", isOpen);
          });
          document.addEventListener("click", function (event) {
            if (!langSelector.contains(event.target)) {
              langSelector.classList.remove("open");
              langBtn.setAttribute("aria-expanded", "false");
            }
          });
        }"""

replacement_logic = """        // Language Selector Dropdown logic
        const langSelector = document.querySelector(".lang-selector");
        const langBtn = document.querySelector(".lang-btn");
        if (langSelector && langBtn) {
          langBtn.addEventListener("click", function (e) {
            e.stopPropagation();
            const isOpen = langSelector.classList.toggle("open");
            langBtn.setAttribute("aria-expanded", isOpen);
          });
          document.addEventListener("click", function (event) {
            if (!langSelector.contains(event.target)) {
              langSelector.classList.remove("open");
              langBtn.setAttribute("aria-expanded", "false");
            }
          });
        }

        // Language options click behavior
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

for filename in html_files:
    filepath = os.path.join(target_dir, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Normalize whitespaces to find a match if layout slightly differs
    if target_logic in content:
        new_content = content.replace(target_logic, replacement_logic)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Added redirection logic to {filename}")
    else:
        # Let's try matching with normalized spaces or report error
        print(f"Warning: Exact target logic block not found in {filename}")
