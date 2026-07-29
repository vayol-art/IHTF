import os
import re

DOMAIN = "https://ihtfmiami.org"
DEFAULT_IMG = f"{DOMAIN}/assets/afiche_1_horizontal.jpg"

PAGES_CONFIG = {
    # Spanish Pages
    "index.html": {
        "title": "IHTF 40 | Festival Internacional de Teatro Hispano de Miami",
        "description": "Programación oficial del 40° Festival Internacional de Teatro Hispano de Miami. Fechas, obras de teatro, salas y entradas.",
        "url": f"{DOMAIN}/index.html",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami"
    },
    "nosotros.html": {
        "title": "Sobre Nosotros | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Conozca la historia de Teatro Avante, el equipo de trabajo, los colaboradores y los reconocimientos del Festival Internacional de Teatro Hispano de Miami.",
        "url": f"{DOMAIN}/nosotros.html",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami"
    },
    "agenda.html": {
        "title": "Programa de Mano | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Consulte el programa de mano completo de las funciones del 40° Festival Internacional de Teatro Hispano de Miami.",
        "url": f"{DOMAIN}/agenda.html",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami"
    },
    "calendario.html": {
        "title": "Calendario de Funciones | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Calendario con todas las fechas y horarios de las obras del 40° Festival Internacional de Teatro Hispano de Miami.",
        "url": f"{DOMAIN}/calendario.html",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami"
    },
    "eventos-adicionales.html": {
        "title": "Eventos Adicionales | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Conozca los eventos adicionales, homenajes póstumos y reconocimientos especiales del 40° Festival Internacional de Teatro Hispano de Miami.",
        "url": f"{DOMAIN}/eventos-adicionales.html",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami"
    },
    "dia-internacional-del-nino.html": {
        "title": "Día Internacional del Niño | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Celebración del Día Internacional del Niño en el Festival Internacional de Teatro Hispano de Miami. Obras de teatro y talleres infantiles.",
        "url": f"{DOMAIN}/dia-internacional-del-nino.html",
        "image": f"{DOMAIN}/assets/card-robinson.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami"
    },
    "teatros.html": {
        "title": "Teatros y Salas | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Información sobre las salas de teatro y sedes donde se presentarán las obras del 40° Festival Internacional de Teatro Hispano de Miami.",
        "url": f"{DOMAIN}/teatros.html",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami"
    },
    "sponsors.html": {
        "title": "Patrocinio y Donaciones | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Apoya al Festival Internacional de Teatro Hispano de Miami. Información sobre patrocinadores y cómo realizar donaciones.",
        "url": f"{DOMAIN}/sponsors.html",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami"
    },
    "contactanos.html": {
        "title": "Contacto | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Póngase en contacto con la organización del Festival Internacional de Teatro Hispano de Miami (Teatro Avante).",
        "url": f"{DOMAIN}/contactanos.html",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami"
    },
    "inscripciones.html": {
        "title": "Inscripciones 41° Festival | Festival Internacional de Teatro Hispano de Miami",
        "description": "Formulario de inscripción y bases para participar en el 41° Festival Internacional de Teatro Hispano de Miami.",
        "url": f"{DOMAIN}/inscripciones.html",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami"
    },
    "obra.html": {
        "title": "Obras del Festival | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Catálogo de todas las obras teatrales del 40° Festival Internacional de Teatro Hispano de Miami.",
        "url": f"{DOMAIN}/obra.html",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami"
    },
    "obra-carrusel.html": {
        "title": "Carrusel por Teatro Avante | IHTF 40",
        "description": "Carrusel, obra de Abel González Melo dirigida por Jackie Briceño. Teatro Avante (EE.UU.).",
        "url": f"{DOMAIN}/obra-carrusel.html",
        "image": f"{DOMAIN}/assets/card-carrusel.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami"
    },
    "obra-zombi-manifiesto.html": {
        "title": "Zombi Manifiesto por Santiago Sanguinetti | IHTF 40",
        "description": "Zombi Manifiesto, obra de Santiago Sanguinetti (Uruguay). 40° Festival Internacional de Teatro Hispano de Miami.",
        "url": f"{DOMAIN}/obra-zombi-manifiesto.html",
        "image": f"{DOMAIN}/assets/card-zombi.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami"
    },
    "obra-historia-de-un-jabali.html": {
        "title": "Historia de un jabalí (o algo de Ricardo) | IHTF 40",
        "description": "Historia de un jabalí (o algo de Ricardo), de Gabriel Calderón y dirigida por Cristian Plana (Chile).",
        "url": f"{DOMAIN}/obra-historia-de-un-jabali.html",
        "image": f"{DOMAIN}/assets/card-jabali.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami"
    },
    "obra-a-fuego.html": {
        "title": "A fuego por Pablo Macho Otero | IHTF 40",
        "description": "A fuego, monólogo de Pablo Macho Otero (España). 40° Festival Internacional de Teatro Hispano de Miami.",
        "url": f"{DOMAIN}/obra-a-fuego.html",
        "image": f"{DOMAIN}/assets/card-a-fuego.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami"
    },
    "obra-odd-man-out.html": {
        "title": "Odd Man Out (Experiencia Inmersiva a Ciegas) | IHTF 40",
        "description": "Odd Man Out, experiencia sensorial inmersiva en completa oscuridad por PITCHBLACK Airlines (EE.UU.).",
        "url": f"{DOMAIN}/obra-odd-man-out.html",
        "image": f"{DOMAIN}/assets/card-odd.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami"
    },
    "obra-sueno.html": {
        "title": "Sueño por Compañía Criolla | IHTF 40",
        "description": "Sueño, obra reimaginada por Emiliano Dionisi sobre texto de Shakespeare (Argentina).",
        "url": f"{DOMAIN}/obra-sueno.html",
        "image": f"{DOMAIN}/assets/card-sueno.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami"
    },
    "obra-robinson-crusoe.html": {
        "title": "Las Asombrosas Aventuras de Robinson Crusoe | IHTF 40",
        "description": "Las Asombrosas Aventuras de Robinson Crusoe (Día Internacional del Niño) en el IHTF 40.",
        "url": f"{DOMAIN}/obra-robinson-crusoe.html",
        "image": f"{DOMAIN}/assets/card-robinson.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami"
    },
    "obra-pundonor.html": {
        "title": "Pundonor por Andrea Garrote | IHTF 40",
        "description": "Pundonor, unipersonal de Andrea Garrote (Argentina). 40° Festival Internacional de Teatro Hispano de Miami.",
        "url": f"{DOMAIN}/obra-pundonor.html",
        "image": f"{DOMAIN}/assets/card-pundonor.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami"
    },
    "obra-hamlet.html": {
        "title": "Hamlet por Chela De Ferrari | IHTF 40",
        "description": "Hamlet, versión libre de Chela De Ferrari interpretada por actores con síndrome de Down (Perú).",
        "url": f"{DOMAIN}/obra-hamlet.html",
        "image": f"{DOMAIN}/assets/card-hamlet.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami"
    },

    # English Pages (en/)
    "en/index.html": {
        "title": "IHTF 40 | International Hispanic Theatre Festival of Miami",
        "description": "Official program for the 40th International Hispanic Theatre Festival of Miami. Performance dates, plays, venues, and ticket sales.",
        "url": f"{DOMAIN}/en/index.html",
        "image": DEFAULT_IMG,
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami"
    },
    "en/nosotros.html": {
        "title": "About Us | International Hispanic Theatre Festival (IHTF 40)",
        "description": "Learn about Teatro Avante, festival history, staff members, collaborators, and awards of the International Hispanic Theatre Festival of Miami.",
        "url": f"{DOMAIN}/en/nosotros.html",
        "image": DEFAULT_IMG,
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami"
    },
    "en/agenda.html": {
        "title": "Playbill | International Hispanic Theatre Festival (IHTF 40)",
        "description": "View the complete playbill and schedule for the 40th International Hispanic Theatre Festival of Miami.",
        "url": f"{DOMAIN}/en/agenda.html",
        "image": DEFAULT_IMG,
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami"
    },
    "en/calendario.html": {
        "title": "Performance Calendar | International Hispanic Theatre Festival (IHTF 40)",
        "description": "Calendar featuring show dates and times for the 40th International Hispanic Theatre Festival of Miami.",
        "url": f"{DOMAIN}/en/calendario.html",
        "image": DEFAULT_IMG,
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami"
    },
    "en/eventos-adicionales.html": {
        "title": "Additional Events | International Hispanic Theatre Festival (IHTF 40)",
        "description": "Explore special events, posthumous tributes, and honors at the 40th International Hispanic Theatre Festival of Miami.",
        "url": f"{DOMAIN}/en/eventos-adicionales.html",
        "image": DEFAULT_IMG,
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami"
    },
    "en/dia-internacional-del-nino.html": {
        "title": "International Children's Day | International Hispanic Theatre Festival (IHTF 40)",
        "description": "International Children's Day celebration at the International Hispanic Theatre Festival of Miami. Plays and children's workshops.",
        "url": f"{DOMAIN}/en/dia-internacional-del-nino.html",
        "image": f"{DOMAIN}/assets/card-robinson.jpg",
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami"
    },
    "en/teatros.html": {
        "title": "Theaters & Venues | International Hispanic Theatre Festival (IHTF 40)",
        "description": "Venues and theaters hosting performances for the 40th International Hispanic Theatre Festival of Miami.",
        "url": f"{DOMAIN}/en/teatros.html",
        "image": DEFAULT_IMG,
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami"
    },
    "en/sponsors.html": {
        "title": "Sponsorship & Donations | International Hispanic Theatre Festival (IHTF 40)",
        "description": "Support the International Hispanic Theatre Festival of Miami. Information about sponsors and donations.",
        "url": f"{DOMAIN}/en/sponsors.html",
        "image": DEFAULT_IMG,
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami"
    },
    "en/contactanos.html": {
        "title": "Contact Us | International Hispanic Theatre Festival (IHTF 40)",
        "description": "Get in touch with the team at the International Hispanic Theatre Festival of Miami (Teatro Avante).",
        "url": f"{DOMAIN}/en/contactanos.html",
        "image": DEFAULT_IMG,
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami"
    },
    "en/inscripciones.html": {
        "title": "41st Festival Inscriptions | International Hispanic Theatre Festival of Miami",
        "description": "Registration form and requirements to participate in the 41st International Hispanic Theatre Festival of Miami.",
        "url": f"{DOMAIN}/en/inscripciones.html",
        "image": DEFAULT_IMG,
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami"
    },
    "en/obra.html": {
        "title": "Festival Plays | International Hispanic Theatre Festival (IHTF 40)",
        "description": "Browse all theatrical performances at the 40th International Hispanic Theatre Festival of Miami.",
        "url": f"{DOMAIN}/en/obra.html",
        "image": DEFAULT_IMG,
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami"
    },
    "en/obra-carrusel.html": {
        "title": "Carrusel by Teatro Avante | IHTF 40",
        "description": "Carrusel, written by Abel González Melo and directed by Jackie Briceño. Teatro Avante (USA).",
        "url": f"{DOMAIN}/en/obra-carrusel.html",
        "image": f"{DOMAIN}/assets/card-carrusel.jpg",
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami"
    },
    "en/obra-zombi-manifiesto.html": {
        "title": "Zombie Manifesto by Santiago Sanguinetti | IHTF 40",
        "description": "Zombie Manifesto by Santiago Sanguinetti (Uruguay). 40th International Hispanic Theatre Festival of Miami.",
        "url": f"{DOMAIN}/en/obra-zombi-manifiesto.html",
        "image": f"{DOMAIN}/assets/card-zombi.jpg",
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami"
    },
    "en/obra-historia-de-un-jabali.html": {
        "title": "Story of a Boar (Or Something of Richard) | IHTF 40",
        "description": "Story of a Boar (Or Something of Richard), by Gabriel Calderón, directed by Cristian Plana (Chile).",
        "url": f"{DOMAIN}/en/obra-historia-de-un-jabali.html",
        "image": f"{DOMAIN}/assets/card-jabali.jpg",
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami"
    },
    "en/obra-a-fuego.html": {
        "title": "A Fuego by Pablo Macho Otero | IHTF 40",
        "description": "A Fuego, written and performed by Pablo Macho Otero (Spain). 40th International Hispanic Theatre Festival of Miami.",
        "url": f"{DOMAIN}/en/obra-a-fuego.html",
        "image": f"{DOMAIN}/assets/card-a-fuego.jpg",
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami"
    },
    "en/obra-odd-man-out.html": {
        "title": "Odd Man Out (Blind Immersive Experience) | IHTF 40",
        "description": "Odd Man Out, an immersive sensory experience in complete darkness by PITCHBLACK Airlines (USA).",
        "url": f"{DOMAIN}/en/obra-odd-man-out.html",
        "image": f"{DOMAIN}/assets/card-odd.jpg",
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami"
    },
    "en/obra-sueno.html": {
        "title": "Sueño by Compañía Criolla | IHTF 40",
        "description": "Sueño, reimagined by Emiliano Dionisi from Shakespeare's text (Argentina).",
        "url": f"{DOMAIN}/en/obra-sueno.html",
        "image": f"{DOMAIN}/assets/card-sueno.jpg",
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami"
    },
    "en/obra-robinson-crusoe.html": {
        "title": "The Amazing Adventures of Robinson Crusoe | IHTF 40",
        "description": "The Amazing Adventures of Robinson Crusoe (International Children's Day) at IHTF 40.",
        "url": f"{DOMAIN}/en/obra-robinson-crusoe.html",
        "image": f"{DOMAIN}/assets/card-robinson.jpg",
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami"
    },
    "en/obra-pundonor.html": {
        "title": "Pundonor by Andrea Garrote | IHTF 40",
        "description": "Pundonor, solo performance by Andrea Garrote (Argentina). 40th International Hispanic Theatre Festival of Miami.",
        "url": f"{DOMAIN}/en/obra-pundonor.html",
        "image": f"{DOMAIN}/assets/card-pundonor.jpg",
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami"
    },
    "en/obra-hamlet.html": {
        "title": "Hamlet by Chela De Ferrari | IHTF 40",
        "description": "Hamlet, free version by Chela De Ferrari performed by actors with Down syndrome (Peru).",
        "url": f"{DOMAIN}/en/obra-hamlet.html",
        "image": f"{DOMAIN}/assets/card-hamlet.jpg",
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami"
    }
}

def generate_head_meta(cfg):
    title = cfg["title"]
    desc = cfg["description"]
    url = cfg["url"]
    img = cfg["image"]
    locale = cfg["locale"]
    site_name = cfg["site_name"]

    meta_block = f"""  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="canonical" href="{url}" />

  <!-- Open Graph / Facebook / WhatsApp -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{url}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:image" content="{img}" />
  <meta property="og:image:secure_url" content="{img}" />
  <meta property="og:image:type" content="image/jpeg" />
  <meta property="og:locale" content="{locale}" />
  <meta property="og:site_name" content="{site_name}" />

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:url" content="{url}" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{desc}" />
  <meta name="twitter:image" content="{img}" />"""
    return meta_block

base_dir = "/Users/vanessa/Documents/IHTF"

for rel_path, cfg in PAGES_CONFIG.items():
    file_path = os.path.join(base_dir, rel_path)
    if not os.path.exists(file_path):
        print(f"Skipping missing file: {file_path}")
        continue
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Clean existing meta blocks
    content = re.sub(r'\s*<link rel="canonical"[^>]*>', '', content)
    content = re.sub(r'\s*<meta property="og:[^>]*>', '', content)
    content = re.sub(r'\s*<meta name="twitter:[^>]*>', '', content)

    new_meta = generate_head_meta(cfg)
    pattern = r'<title>.*?</title>(?:\s*<meta name="description" content=".*?"\s*/?>)?'
    
    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, new_meta, content, count=1, flags=re.DOTALL)
    else:
        viewport_pattern = r'(<meta name="viewport" content="[^"]*" />)'
        content = re.sub(viewport_pattern, r'\1\n' + new_meta, content, count=1)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated metadata for: {rel_path}")

print("All 40 files updated successfully with JPG images!")
