import os

en_dir = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF\en"
html_files = [
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

target_block = """      // Botón Comprar Entradas
      const buyBtn = document.getElementById("play-buy-btn");
      buyBtn.textContent = buyText === "Reservar" ? "Reservar ahora" : "Comprar entradas";"""

replacement_block = """      // Botón Comprar Entradas
      const buyBtn = document.getElementById("play-buy-btn");
      const buyText = play.buttonText || "Comprar";
      buyBtn.textContent = buyText === "Reservar" ? "Reserve now" : "Buy tickets";"""

for filename in html_files:
    filepath = os.path.join(en_dir, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target_block in content:
        content = content.replace(target_block, replacement_block)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed button text and defined buyText in en/{filename}")
    else:
        print(f"Target block not found in en/{filename}")
