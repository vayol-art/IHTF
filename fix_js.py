import glob
import re

js_template = """  <script>
    document.addEventListener("DOMContentLoaded", function() {
      let playId = "PLAY_ID_PLACEHOLDER";

      const play = playsData[playId];

      // Título de la página
      document.title = `${play.title} | Festival Internacional de Teatro Hispano`;

      // Set Theme color for styling
      document.getElementById("inicio").style.setProperty('--theme-color', 'var(--' + play.colorClass + ')');

      // Populate Texts
      document.getElementById("play-country").textContent = play.country;
      document.getElementById("play-title").innerHTML = play.titleHTML || play.title;

      document.getElementById("play-author").textContent = play.author;
      document.getElementById("play-director").textContent = play.director;
      document.getElementById("play-cast").textContent = play.cast;

      // Populate Logos
      const logosContainer = document.getElementById("play-bar-logo");
      logosContainer.innerHTML = "";
      play.logos.forEach(logo => {
        let extraStyle = logo.includes("white") || logo.includes("blanco") || logo.includes("arsht") ? 'style="filter: invert(1);"' : '';
        logosContainer.innerHTML += `<img src="${logo}" alt="Logo Teatro" ${extraStyle}>`;
      });

      // Funciones
      const scheduleContainer = document.getElementById("play-schedule");
      scheduleContainer.innerHTML = "";
      play.dates.forEach(d => {
        const card = document.createElement("div");
        card.className = "npc-date-item";
        card.innerHTML = `
          <span class="m">${d.month.toUpperCase()}</span>
          <strong class="d">${d.day}</strong>
          <small class="t">${d.time}</small>
          ${d.foro ? `<small class="note">${d.foro}</small>` : ""}
        `;
        scheduleContainer.appendChild(card);
      });

      // Descripción
      const descContainer = document.getElementById("play-description");
      descContainer.innerHTML = "";
      
      const sentences = play.description.split(". ");
      let currentParagraph = "";
      sentences.forEach((sentence, index) => {
        if (sentence.trim()) {
          currentParagraph += sentence.trim() + ". ";
          if ((index + 1) % 2 === 0 || index === sentences.length - 1) {
            const p = document.createElement("p");
            p.textContent = currentParagraph;
            descContainer.appendChild(p);
            currentParagraph = "";
          }
        }
      });

      // Información adicional
      const extraContainer = document.getElementById("play-extra-info");
      extraContainer.innerHTML = "";
      if (play.extraInfo) {
        const extraP = document.createElement("p");
        extraP.textContent = play.extraInfo;
        extraContainer.appendChild(extraP);
      }

      // Botón Comprar Entradas
      const buyBtn = document.getElementById("play-buy-btn");
      buyBtn.textContent = play.buttonText || "Entradas";
      buyBtn.href = "obra-" + play.id + ".html";
    });
  </script>"""

for filepath in glob.glob("obra-*.html"):
    with open(filepath, "r") as f:
        content = f.read()
    
    # Extract playId
    match = re.search(r'let playId = "(.*?)";', content)
    if not match:
        continue
    play_id = match.group(1)
    
    # Find the script tag containing let playId = ...
    # We will replace from <script> that contains let playId = ... to its corresponding </script>
    
    script_start = content.rfind('<script>', 0, match.start())
    script_end = content.find('</script>', match.end()) + 9
    
    if script_start != -1 and script_end != -1:
        new_script = js_template.replace("PLAY_ID_PLACEHOLDER", play_id)
        content = content[:script_start] + new_script + content[script_end:]
        
        with open(filepath, "w") as f:
            f.write(content)
            
print("Fixed JS in HTML files.")
