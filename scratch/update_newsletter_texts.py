import os

target_dir = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF"
old_text = "<p>Recibe novedades del festival, programación, artistas invitados y noticias especiales del IHTF.</p>"
new_text = "<p>Recibe información actualizada sobre el IHTF</p>"

files_to_update = [
    "agenda.html",
    "teatros.html",
    "obra.html",
    "obra-zombi-manifiesto.html",
    "obra-sueno.html",
    "obra-robinson-crusoe.html",
    "obra-odd-man-out.html",
    "obra-historia-de-un-jabali.html",
    "obra-hamlet.html",
    "obra-habitacion-macbeth.html",
    "obra-carrusel.html",
    "obra-a-fuego.html"
]

for filename in files_to_update:
    filepath = os.path.join(target_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        if old_text in content:
            updated_content = content.replace(old_text, new_text)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(updated_content)
            print(f"Updated {filename}")
        else:
            print(f"Old text not found in {filename}")
    else:
        print(f"File not found: {filename}")
