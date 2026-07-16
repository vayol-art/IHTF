import os
import re

css_to_append = """
/* --- NEW PLAY CARD LAYOUT --- */
.new-play-card-section {
  padding: 120px 20px 60px;
  background: #ffffff;
}

.new-play-card {
  max-width: 1040px;
  margin: 0 auto;
  display: flex;
  background: #fff;
  border-radius: 6px;
  overflow: hidden;
  box-shadow: 0 10px 40px rgba(0,0,0,0.15);
  border: 1px solid rgba(0,0,0,0.05);
}

.new-play-left {
  flex: 0 0 52%;
  display: flex;
  flex-direction: column;
}

.npc-country-bar {
  background: var(--theme-color, #761354);
  color: #fff;
  text-align: center;
  padding: 12px;
  font-family: var(--font-body);
  font-size: 22px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-weight: 500;
}

.npc-body {
  padding: 30px 40px;
  color: var(--theme-color, #761354);
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

.npc-body h1 {
  font-family: var(--font-body);
  font-size: clamp(32px, 5vw, 42px);
  margin: 0 0 20px 0;
  text-transform: uppercase;
  line-height: 1.1;
  font-weight: 800;
}

.npc-desc p {
  font-size: 19px;
  line-height: 1.35;
  margin: 0 0 18px 0;
  font-weight: 400;
}

.npc-credits {
  margin-bottom: 30px;
}

.npc-credits .credit-item {
  font-size: 19px;
  margin-bottom: 6px;
}
.npc-credits .credit-item strong {
  font-weight: 800;
}
.npc-credits .credit-item span {
  font-weight: 400;
}

.npc-actions {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-top: auto;
}

.npc-btn {
  background: var(--theme-color, #761354);
  color: #fff !important;
  font-weight: 700;
  padding: 10px 24px;
  border-radius: 999px;
  text-decoration: none;
  font-size: 16px;
  transition: transform 0.2s;
}
.npc-btn:hover {
  transform: scale(1.05);
}

.npc-logos {
  display: flex;
  align-items: center;
  gap: 12px;
}
.npc-logos img {
  height: 40px;
  width: auto;
  object-fit: contain;
  /* some logos might be white originally, so if they are on white bg, we can invert them. But let's leave it as is for now */
}

.npc-extra p {
  font-size: 11px;
  line-height: 1.3;
  margin: 10px 0 0 0;
  opacity: 0.8;
}

.new-play-right {
  flex: 0 0 48%;
  display: flex;
  flex-direction: column;
  position: relative;
  background: #000;
}

.npc-image-container {
  flex-grow: 1;
  position: relative;
  min-height: 400px;
  overflow: hidden;
}

.npc-image-container .carousel-track {
  position: absolute;
  inset: 0;
}

.npc-dates-bar {
  background: var(--theme-color, #761354);
  color: #fff;
  display: flex;
  align-items: stretch;
}

.npc-date-item {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 15px 5px;
  border-left: 1px solid rgba(255,255,255,0.3);
  text-align: center;
}
.npc-date-item:first-child {
  border-left: none;
}

.npc-date-item .m {
  font-size: 11px;
  font-weight: 500;
  text-transform: uppercase;
  margin-bottom: 2px;
}
.npc-date-item .d {
  font-family: var(--font-body);
  font-size: 36px;
  font-weight: 800;
  line-height: 1;
  margin-bottom: 4px;
}
.npc-date-item .t {
  font-size: 13px;
  font-weight: 500;
}
.npc-date-item .note {
  font-size: 9px;
  margin-top: 4px;
  line-height: 1.1;
}

@media (max-width: 900px) {
  .new-play-card {
    flex-direction: column;
  }
  .new-play-left, .new-play-right {
    flex: 0 0 auto;
  }
  .npc-image-container {
    height: 350px;
    min-height: auto;
  }
  .npc-dates-bar {
    flex-wrap: wrap;
  }
  .npc-date-item {
    border-left: none;
    border-top: 1px solid rgba(255,255,255,0.3);
    flex: 0 0 50%;
  }
  .npc-date-item:nth-child(odd) {
    border-right: 1px solid rgba(255,255,255,0.3);
  }
  .npc-date-item:nth-child(1), .npc-date-item:nth-child(2) {
    border-top: none;
  }
}
"""

with open("obra.css", "a") as f:
    f.write("\n" + css_to_append + "\n")

html_template = """    <section class="new-play-card-section">
      <div class="new-play-card" id="play-card-container">
        <div class="new-play-left">
          <div class="npc-country-bar" id="play-country-bar">
            <span id="play-country">País</span>
          </div>
          <div class="npc-body">
            <h1 id="play-title">Título</h1>
            <div id="play-description" class="npc-desc"></div>
            
            <div class="npc-credits">
              <div class="credit-item"><strong>Autor:</strong> <span id="play-author">Autor</span></div>
              <div class="credit-item"><strong>Director:</strong> <span id="play-director">Director</span></div>
              <div class="credit-item"><strong>Elenco:</strong> <span id="play-cast">Elenco</span></div>
            </div>
            
            <div class="npc-actions">
              <a class="npc-btn" id="play-buy-btn" href="agenda.html">Entradas</a>
              <div id="play-bar-logo" class="npc-logos">
                <!-- Logos dynamically inserted -->
              </div>
            </div>
            <div id="play-extra-info" class="npc-extra"></div>
          </div>
        </div>
        
        <div class="new-play-right">
          <div class="npc-image-container">
            <!-- Reuse existing carousel -->
            <div class="hero-carousel-container" id="hero-carousel">
              CAROUSEL_PLACEHOLDER
            </div>
          </div>
          <div class="npc-dates-bar" id="play-schedule">
            <!-- Dates dynamically inserted -->
          </div>
        </div>
      </div>
    </section>"""

js_code = """      // Título de la página
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
        // Some logos are white, to display them on white bg we can invert them, but we will leave them for now
        // Or if it's the arsht-white-logo, invert it
        let extraStyle = logo.includes("white") || logo.includes("blanco") ? 'style="filter: invert(1);"' : '';
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
      buyBtn.href = "obra-" + play.id + ".html";"""


import glob

for filepath in glob.glob("obra-*.html"):
    with open(filepath, "r") as f:
        content = f.read()
        
    # Extract carousel
    carousel_match = re.search(r'(<div class="carousel-track">.*?</div>)', content, re.DOTALL)
    if carousel_match:
        carousel_content = carousel_match.group(1)
    else:
        carousel_content = '<div class="carousel-track"></div>'
        
    # Replace sections
    # Find <section class="hero-wrapper" ... to end of <section id="obra" class="detail-section">... </section>
    
    start_hero = content.find('<section class="hero-wrapper"')
    end_detail = content.find('</section>', content.find('<section id="obra" class="detail-section"')) + 10
    
    if start_hero != -1 and end_detail != -1:
        new_html = html_template.replace("CAROUSEL_PLACEHOLDER", carousel_content)
        content = content[:start_hero] + new_html + content[end_detail:]
        
    # Replace JS
    js_start = content.find('document.title =')
    js_end = content.find('});', js_start)
    
    # We must be careful because of some variable declarations at the top of DOMContentLoaded
    # Like `let playId = ...` and `const play = ...`
    # Let's target everything from `document.title =` down to the end of the script tag before `});`
    
    if js_start != -1 and js_end != -1:
        content = content[:js_start] + js_code + "\n      " + content[js_end:]
        
    with open(filepath, "w") as f:
        f.write(content)
        
print("Updated HTML files.")
