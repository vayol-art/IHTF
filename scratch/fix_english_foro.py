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

target_block = """      play.dates.forEach(d => {
        const card = document.createElement("div");
        card.className = "play-date-item";
        card.innerHTML = `
          <span class="m">${d.month.toUpperCase()}</span>
          <strong class="d">${d.day}</strong>
          <small class="t">${d.time}</small>
          ${d.foro ? `<small class="note">${d.foro}</small>` : ""}
        `;"""

replacement_block = """      play.dates.forEach(d => {
        const card = document.createElement("div");
        card.className = "play-date-item";
        let noteText = d.foro || "";
        if (noteText === "Foro después de la obra") {
          noteText = "Forum after the play";
        }
        card.innerHTML = `
          <span class="m">${d.month.toUpperCase()}</span>
          <strong class="d">${d.day}</strong>
          <small class="t">${d.time}</small>
          ${d.foro ? `<small class="note">${noteText}</small>` : ""}
        `;"""

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
        print(f"Translated date-badge forum notes in en/{filename}")
    else:
        print(f"Target block not found in en/{filename}")
