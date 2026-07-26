import glob
import re

# 1. Update data.js
with open('data.js', 'r', encoding='utf-8') as f:
    data_content = f.read()

# Update title
data_content = data_content.replace(
    '"title": "Historia de un jabalí (o algo de Ricardo III)"',
    '"title": "Historia de un jabalí (o algo de Ricardo)"'
)
data_content = data_content.replace(
    '"titleHTML": "Historia de un jabalí<br>(o algo de Ricardo III)"',
    '"titleHTML": "Historia de un jabalí<br>(o algo de Ricardo)"'
)

# Update description in data.js
# Remove \\n\\n and replace Ricardo III with Ricardo
old_desc = r'Luego de su estreno en Chile, nos llega una de las piezas más emblemáticas del Festival Internacional Teatro a mil 2026. Dos actores se enfrentan al reto de interpretar a Ricardo III, el monarca despiadado de la tragedia de William Shakespeare. Llevan toda la vida haciendo papeles secundarios y piensan que merecen esta oportunidad. Sin embargo, consideran que el resto del elenco no está a su altura y no les gusta nada de lo que les propone el director. Durante la construcción del personaje, las afinidades entre los actores y el monarca inglés empiezan a aflorar. Los tres son ambiciosos e inteligentes. Como Ricardo III, ellos no quieren conformarse, tienen ansias de poder y no están dispuestos a perder el tiempo con actores blandos, hipersensibles o mediocres. A medida que se entrelazan sus historias de vida, la relación entre los actores, el personaje y el espectador se hace cada vez más estrecha, entregando un espacio para reflexionar sobre los límites de la ambición humana, los mecanismos de poder contemporáneos, el deseo y el resentimiento. \n\n“Una obra que se mueve con inteligencia en un terreno resbaladizo: el de la ambición artística, el ego del actor y el poder como pulsión íntima y política. A partir de la figura de Ricardo III, la pieza no propone una adaptación de Shakespeare, sino una disección contemporánea de su monstruo más célebre” (Galia Bogolasky-Culturizarte)'

new_desc = 'Luego de su estreno en Chile, nos llega una de las piezas más emblemáticas del Festival Internacional Teatro a mil 2026. Dos actores se enfrentan al reto de interpretar a Ricardo, el monarca despiadado de la tragedia de William Shakespeare. Llevan toda la vida haciendo papeles secundarios y piensan que merecen esta oportunidad. Sin embargo, consideran que el resto del elenco no está a su altura y no les gusta nada de lo que les propone el director. Durante la construcción del personaje, las afinidades entre los actores y el monarca inglés empiezan a aflorar. Los tres son ambiciosos e inteligentes. Como Ricardo, ellos no quieren conformarse, tienen ansias de poder y no están dispuestos a perder el tiempo con actores blandos, hipersensibles o mediocres. A medida que se entrelazan sus historias de vida, la relación entre los actores, el personaje y el espectador se hace cada vez más estrecha, entregando un espacio para reflexionar sobre los límites de la ambición humana, los mecanismos de poder contemporáneos, el deseo y el resentimiento. “Una obra que se mueve con inteligencia en un terreno resbaladizo: el de la ambición artística, el ego del actor y el poder como pulsión íntima y política. A partir de la figura de Ricardo, la pieza no propone una adaptación de Shakespeare, sino una disección contemporánea de su monstruo más célebre” (Galia Bogolasky-Culturizarte)'

# Replace description in data_content (handling escaped backslashes in data.js)
data_content = re.sub(
    r'"description": "Luego de su estreno.*?(Galia Bogolasky-Culturizarte)"',
    f'"description": "{new_desc}"',
    data_content,
    flags=re.DOTALL
)

# Update description_en in data.js
new_desc_en = "Following its premiere in Chile, one of the most emblematic pieces of the Teatro a Mil International Festival 2026 comes to us. Two actors face the challenge of playing Richard, the ruthless monarch of William Shakespeare's tragedy. They have been playing supporting roles all their lives and think they deserve this opportunity. However, they consider that the rest of the cast is not up to their level and they do not like anything the director proposes. During the construction of the character, the affinities between the actors and the English monarch begin to surface. All three are ambitious and intelligent. Like Richard, they do not want to settle, they have a lust for power and are not willing to waste time with soft, hypersensitive, or mediocre actors. As their life stories intertwine, the relationship between the actors, the character, and the spectator becomes closer and closer, delivering a key space to reflect on the limits of human ambition, contemporary mechanisms of power, desire, and resentment. 'A play that moves with intelligence on slippery ground: that of artistic ambition, the actor's ego, and power as an intimate and political drive. Based on the figure of Richard, the piece does not propose an adaptation of Shakespeare, but a contemporary dissection of his most famous monster.' (Galia Bogolasky - Culturizarte)"

data_content = re.sub(
    r'"description_en": "Following its premiere.*?(Galia Bogolasky - Culturizarte)"',
    f'"description_en": "{new_desc_en}"',
    data_content,
    flags=re.DOTALL
)

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(data_content)
print("Updated data.js")

# 2. Update all HTML files
html_files = glob.glob("*.html") + glob.glob("en/*.html")
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    orig = content
    content = content.replace("Historia de un jabalí<br>(o algo de Ricardo III)", "Historia de un jabalí<br>(o algo de Ricardo)")
    content = content.replace("Historia de un jabalí<br/>(o algo de Ricardo III)", "Historia de un jabalí<br/>(o algo de Ricardo)")
    content = content.replace("Historia de un Jabalí (O algo de Ricardo III)", "Historia de un Jabalí (O algo de Ricardo)")
    content = content.replace("HISTORIA DE UN JABALÍ (O ALGO DE RICARDO III)", "HISTORIA DE UN JABALÍ (O ALGO DE RICARDO)")
    content = content.replace("interpretar a Ricardo III", "interpretar a Ricardo")
    
    if content != orig:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
