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

target_block = """      // Setup the theater logo
      const playBarLogo = document.getElementById("play-bar-logo");
      // The theater logo is usually the last one, or the only one
      const theaterLogoSrc = play.logos[play.logos.length - 1];
      if (theaterLogoSrc) {
        playBarLogo.innerHTML = `<img src="${theaterLogoSrc}" alt="Logo Teatro">`;
      }"""

replacement_block = """      // Setup the theater logo
      const playBarLogo = document.getElementById("play-bar-logo");
      // The theater logo is usually the last one, or the only one
      let theaterLogoSrc = play.logos[play.logos.length - 1];
      if (theaterLogoSrc) {
        if (!theaterLogoSrc.startsWith('../')) {
          theaterLogoSrc = '../' + theaterLogoSrc;
        }
        playBarLogo.innerHTML = `<img src="${theaterLogoSrc}" alt="Logo Teatro">`;
      }"""

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
        print(f"Fixed dynamic logo paths in en/{filename}")
    else:
        print(f"Target block not found in en/{filename}")
