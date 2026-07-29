import os
import re
import shutil

BASE_DIR = "/Users/vanessa/Documents/IHTF"
DOMAIN = "https://vayol-art.github.io/IHTF"
DEFAULT_IMG = f"{DOMAIN}/assets/afiche_1_horizontal.jpg"

PAGES_CONFIG = {
    # Spanish Pages (under es/)
    "es/index.html": {
        "src": "index.html" if os.path.exists(os.path.join(BASE_DIR, "index.html")) and "redirecting" not in open(os.path.join(BASE_DIR, "index.html")).read().lower() else "es/index.html",
        "dest": "es/index.html",
        "url": f"{DOMAIN}/es/",
        "title": "IHTF 40 | Festival Internacional de Teatro Hispano de Miami",
        "description": "Programación oficial del 40° Festival Internacional de Teatro Hispano de Miami. Fechas, obras de teatro, salas y entradas.",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": ""
    },
    "es/nosotros.html": {
        "src": "nosotros/index.html",
        "dest": "es/nosotros/index.html",
        "url": f"{DOMAIN}/es/nosotros/",
        "title": "Sobre Nosotros | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Conozca la historia de Teatro Avante, el equipo de trabajo, los colaboradores y los reconocimientos del Festival Internacional de Teatro Hispano de Miami.",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "nosotros"
    },
    "es/agenda.html": {
        "src": "agenda/index.html",
        "dest": "es/agenda/index.html",
        "url": f"{DOMAIN}/es/agenda/",
        "title": "Programa de Mano | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Consulte el programa de mano completo de las funciones del 40° Festival Internacional de Teatro Hispano de Miami.",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "agenda"
    },
    "es/calendario.html": {
        "src": "calendario/index.html",
        "dest": "es/calendario/index.html",
        "url": f"{DOMAIN}/es/calendario/",
        "title": "Calendario de Funciones | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Calendario con todas las fechas y horarios de las obras del 40° Festival Internacional de Teatro Hispano de Miami.",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "calendario"
    },
    "es/eventos-adicionales.html": {
        "src": "eventos-adicionales/index.html",
        "dest": "es/eventos-adicionales/index.html",
        "url": f"{DOMAIN}/es/eventos-adicionales/",
        "title": "Eventos Adicionales | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Conozca los eventos adicionales, homenajes póstumos y reconocimientos especiales del 40° Festival Internacional de Teatro Hispano de Miami.",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "eventos-adicionales"
    },
    "es/dia-internacional-del-nino.html": {
        "src": "dia-internacional-del-nino/index.html",
        "dest": "es/dia-internacional-del-nino/index.html",
        "url": f"{DOMAIN}/es/dia-internacional-del-nino/",
        "title": "Día Internacional del Niño | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Celebración del Día Internacional del Niño en el Festival Internacional de Teatro Hispano de Miami. Obras de teatro y talleres infantiles.",
        "image": f"{DOMAIN}/assets/card-robinson.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "dia-internacional-del-nino"
    },
    "es/teatros.html": {
        "src": "teatros/index.html",
        "dest": "es/teatros/index.html",
        "url": f"{DOMAIN}/es/teatros/",
        "title": "Teatros y Salas | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Información sobre las salas de teatro y sedes donde se presentarán las obras del 40° Festival Internacional de Teatro Hispano de Miami.",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "teatros"
    },
    "es/sponsors.html": {
        "src": "sponsors/index.html",
        "dest": "es/sponsors/index.html",
        "url": f"{DOMAIN}/es/sponsors/",
        "title": "Patrocinio y Donaciones | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Apoya al Festival Internacional de Teatro Hispano de Miami. Información sobre patrocinadores y cómo realizar donaciones.",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "sponsors"
    },
    "es/contactanos.html": {
        "src": "contactanos/index.html",
        "dest": "es/contactanos/index.html",
        "url": f"{DOMAIN}/es/contactanos/",
        "title": "Contacto | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Póngase en contacto con la organización del Festival Internacional de Teatro Hispano de Miami (Teatro Avante).",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "contactanos"
    },
    "es/inscripciones.html": {
        "src": "inscripciones/index.html",
        "dest": "es/inscripciones/index.html",
        "url": f"{DOMAIN}/es/inscripciones/",
        "title": "Inscripciones 41° Festival | Festival Internacional de Teatro Hispano de Miami",
        "description": "Formulario de inscripción y bases para participar en el 41° Festival Internacional de Teatro Hispano de Miami.",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "inscripciones"
    },
    "es/obra.html": {
        "src": "obra/index.html",
        "dest": "es/obra/index.html",
        "url": f"{DOMAIN}/es/obra/",
        "title": "Obras del Festival | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Catálogo de todas las obras teatrales del 40° Festival Internacional de Teatro Hispano de Miami.",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "obra"
    },
    "es/obra-carrusel.html": {
        "src": "obra-carrusel/index.html",
        "dest": "es/obra-carrusel/index.html",
        "url": f"{DOMAIN}/es/obra-carrusel/",
        "title": "Carrusel por Teatro Avante | IHTF 40",
        "description": "Carrusel, obra de Abel González Melo dirigida por Jackie Briceño. Teatro Avante (EE.UU.).",
        "image": f"{DOMAIN}/assets/card-carrusel.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "obra-carrusel"
    },
    "es/obra-zombi-manifiesto.html": {
        "src": "obra-zombi-manifiesto/index.html",
        "dest": "es/obra-zombi-manifiesto/index.html",
        "url": f"{DOMAIN}/es/obra-zombi-manifiesto/",
        "title": "Zombi Manifiesto por Santiago Sanguinetti | IHTF 40",
        "description": "Zombi Manifiesto, obra de Santiago Sanguinetti (Uruguay). 40° Festival Internacional de Teatro Hispano de Miami.",
        "image": f"{DOMAIN}/assets/card-zombi.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "obra-zombi-manifiesto"
    },
    "es/obra-historia-de-un-jabali.html": {
        "src": "obra-historia-de-un-jabali/index.html",
        "dest": "es/obra-historia-de-un-jabali/index.html",
        "url": f"{DOMAIN}/es/obra-historia-de-un-jabali/",
        "title": "Historia de un jabalí (o algo de Ricardo) | IHTF 40",
        "description": "Historia de un jabalí (o algo de Ricardo), de Gabriel Calderón y dirigida por Cristian Plana (Chile).",
        "image": f"{DOMAIN}/assets/card-jabali.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "obra-historia-de-un-jabali"
    },
    "es/obra-a-fuego.html": {
        "src": "obra-a-fuego/index.html",
        "dest": "es/obra-a-fuego/index.html",
        "url": f"{DOMAIN}/es/obra-a-fuego/",
        "title": "A fuego por Pablo Macho Otero | IHTF 40",
        "description": "A fuego, monólogo de Pablo Macho Otero (España). 40° Festival Internacional de Teatro Hispano de Miami.",
        "image": f"{DOMAIN}/assets/card-a-fuego.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "obra-a-fuego"
    },
    "es/obra-odd-man-out.html": {
        "src": "obra-odd-man-out/index.html",
        "dest": "es/obra-odd-man-out/index.html",
        "url": f"{DOMAIN}/es/obra-odd-man-out/",
        "title": "Odd Man Out (Experiencia Inmersiva a Ciegas) | IHTF 40",
        "description": "Odd Man Out, experiencia sensorial inmersiva en completa oscuridad por PITCHBLACK Airlines (EE.UU.).",
        "image": f"{DOMAIN}/assets/card-odd.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "obra-odd-man-out"
    },
    "es/obra-sueno.html": {
        "src": "obra-sueno/index.html",
        "dest": "es/obra-sueno/index.html",
        "url": f"{DOMAIN}/es/obra-sueno/",
        "title": "Sueño por Compañía Criolla | IHTF 40",
        "description": "Sueño, obra reimaginada por Emiliano Dionisi sobre texto de Shakespeare (Argentina).",
        "image": f"{DOMAIN}/assets/card-sueno.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "obra-sueno"
    },
    "es/obra-robinson-crusoe.html": {
        "src": "obra-robinson-crusoe/index.html",
        "dest": "es/obra-robinson-crusoe/index.html",
        "url": f"{DOMAIN}/es/obra-robinson-crusoe/",
        "title": "Las Asombrosas Aventuras de Robinson Crusoe | IHTF 40",
        "description": "Las Asombrosas Aventuras de Robinson Crusoe (Día Internacional del Niño) en el IHTF 40.",
        "image": f"{DOMAIN}/assets/card-robinson.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "obra-robinson-crusoe"
    },
    "es/obra-pundonor.html": {
        "src": "obra-pundonor/index.html",
        "dest": "es/obra-pundonor/index.html",
        "url": f"{DOMAIN}/es/obra-pundonor/",
        "title": "Pundonor por Andrea Garrote | IHTF 40",
        "description": "Pundonor, unipersonal de Andrea Garrote (Argentina). 40° Festival Internacional de Teatro Hispano de Miami.",
        "image": f"{DOMAIN}/assets/card-pundonor.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "obra-pundonor"
    },
    "es/obra-hamlet.html": {
        "src": "obra-hamlet/index.html",
        "dest": "es/obra-hamlet/index.html",
        "url": f"{DOMAIN}/es/obra-hamlet/",
        "title": "Hamlet por Chela De Ferrari | IHTF 40",
        "description": "Hamlet, versión libre de Chela De Ferrari interpretada por actores con síndrome de Down (Perú).",
        "image": f"{DOMAIN}/assets/card-hamlet.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "obra-hamlet"
    },

    # English Pages (under en/)
    "en/index.html": {
        "src": "en/index.html",
        "dest": "en/index.html",
        "url": f"{DOMAIN}/en/",
        "title": "IHTF 40 | International Hispanic Theatre Festival of Miami",
        "description": "Official program for the 40th International Hispanic Theatre Festival of Miami. Performance dates, plays, venues, and ticket sales.",
        "image": DEFAULT_IMG,
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami",
        "lang": "en",
        "section": ""
    },
    "en/nosotros.html": {
        "src": "en/nosotros/index.html",
        "dest": "en/nosotros/index.html",
        "url": f"{DOMAIN}/en/nosotros/",
        "title": "About Us | International Hispanic Theatre Festival (IHTF 40)",
        "description": "Learn about Teatro Avante, festival history, staff members, collaborators, and awards of the International Hispanic Theatre Festival of Miami.",
        "image": DEFAULT_IMG,
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami",
        "lang": "en",
        "section": "nosotros"
    },
    "en/agenda.html": {
        "src": "en/agenda/index.html",
        "dest": "en/agenda/index.html",
        "url": f"{DOMAIN}/en/agenda/",
        "title": "Playbill | International Hispanic Theatre Festival (IHTF 40)",
        "description": "View the complete playbill and schedule for the 40th International Hispanic Theatre Festival of Miami.",
        "image": DEFAULT_IMG,
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami",
        "lang": "en",
        "section": "agenda"
    },
    "en/calendario.html": {
        "src": "en/calendario/index.html",
        "dest": "en/calendario/index.html",
        "url": f"{DOMAIN}/en/calendario/",
        "title": "Performance Calendar | International Hispanic Theatre Festival (IHTF 40)",
        "description": "Calendar featuring show dates and times for the 40th International Hispanic Theatre Festival of Miami.",
        "image": DEFAULT_IMG,
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami",
        "lang": "en",
        "section": "calendario"
    },
    "en/eventos-adicionales.html": {
        "src": "en/eventos-adicionales/index.html",
        "dest": "en/eventos-adicionales/index.html",
        "url": f"{DOMAIN}/en/eventos-adicionales/",
        "title": "Additional Events | International Hispanic Theatre Festival (IHTF 40)",
        "description": "Explore special events, posthumous tributes, and honors at the 40th International Hispanic Theatre Festival of Miami.",
        "image": DEFAULT_IMG,
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami",
        "lang": "en",
        "section": "eventos-adicionales"
    },
    "en/dia-internacional-del-nino.html": {
        "src": "en/dia-internacional-del-nino/index.html",
        "dest": "en/dia-internacional-del-nino/index.html",
        "url": f"{DOMAIN}/en/dia-internacional-del-nino/",
        "title": "International Children's Day | International Hispanic Theatre Festival (IHTF 40)",
        "description": "International Children's Day celebration at the International Hispanic Theatre Festival of Miami. Plays and children's workshops.",
        "image": f"{DOMAIN}/assets/card-robinson.jpg",
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami",
        "lang": "en",
        "section": "dia-internacional-del-nino"
    },
    "en/teatros.html": {
        "src": "en/teatros/index.html",
        "dest": "en/teatros/index.html",
        "url": f"{DOMAIN}/en/teatros/",
        "title": "Theaters & Venues | International Hispanic Theatre Festival (IHTF 40)",
        "description": "Venues and theaters hosting performances for the 40th International Hispanic Theatre Festival of Miami.",
        "image": DEFAULT_IMG,
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami",
        "lang": "en",
        "section": "teatros"
    },
    "en/sponsors.html": {
        "src": "en/sponsors/index.html",
        "dest": "en/sponsors/index.html",
        "url": f"{DOMAIN}/en/sponsors/",
        "title": "Sponsorship & Donations | International Hispanic Theatre Festival (IHTF 40)",
        "description": "Support the International Hispanic Theatre Festival of Miami. Information about sponsors and donations.",
        "image": DEFAULT_IMG,
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami",
        "lang": "en",
        "section": "sponsors"
    },
    "en/contactanos.html": {
        "src": "en/contactanos/index.html",
        "dest": "en/contactanos/index.html",
        "url": f"{DOMAIN}/en/contactanos/",
        "title": "Contact Us | International Hispanic Theatre Festival (IHTF 40)",
        "description": "Get in touch with the team at the International Hispanic Theatre Festival of Miami (Teatro Avante).",
        "image": DEFAULT_IMG,
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami",
        "lang": "en",
        "section": "contactanos"
    },
    "en/inscripciones.html": {
        "src": "en/inscripciones/index.html",
        "dest": "en/inscripciones/index.html",
        "url": f"{DOMAIN}/en/inscripciones/",
        "title": "41st Festival Inscriptions | International Hispanic Theatre Festival of Miami",
        "description": "Registration form and requirements to participate in the 41st International Hispanic Theatre Festival of Miami.",
        "image": DEFAULT_IMG,
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami",
        "lang": "en",
        "section": "inscripciones"
    },
    "en/obra.html": {
        "src": "en/obra/index.html",
        "dest": "en/obra/index.html",
        "url": f"{DOMAIN}/en/obra/",
        "title": "Festival Plays | International Hispanic Theatre Festival (IHTF 40)",
        "description": "Browse all theatrical performances at the 40th International Hispanic Theatre Festival of Miami.",
        "image": DEFAULT_IMG,
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami",
        "lang": "en",
        "section": "obra"
    },
    "en/obra-carrusel.html": {
        "src": "en/obra-carrusel/index.html",
        "dest": "en/obra-carrusel/index.html",
        "url": f"{DOMAIN}/en/obra-carrusel/",
        "title": "Carrusel by Teatro Avante | IHTF 40",
        "description": "Carrusel, written by Abel González Melo and directed by Jackie Briceño. Teatro Avante (USA).",
        "image": f"{DOMAIN}/assets/card-carrusel.jpg",
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami",
        "lang": "en",
        "section": "obra-carrusel"
    },
    "en/obra-zombi-manifiesto.html": {
        "src": "en/obra-zombi-manifiesto/index.html",
        "dest": "en/obra-zombi-manifiesto/index.html",
        "url": f"{DOMAIN}/en/obra-zombi-manifiesto/",
        "title": "Zombie Manifesto by Santiago Sanguinetti | IHTF 40",
        "description": "Zombie Manifesto by Santiago Sanguinetti (Uruguay). 40th International Hispanic Theatre Festival of Miami.",
        "image": f"{DOMAIN}/assets/card-zombi.jpg",
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami",
        "lang": "en",
        "section": "obra-zombi-manifiesto"
    },
    "en/obra-historia-de-un-jabali.html": {
        "src": "en/obra-historia-de-un-jabali/index.html",
        "dest": "en/obra-historia-de-un-jabali/index.html",
        "url": f"{DOMAIN}/en/obra-historia-de-un-jabali/",
        "title": "Story of a Boar (Or Something of Richard) | IHTF 40",
        "description": "Story of a Boar (Or Something of Richard), by Gabriel Calderón, directed by Cristian Plana (Chile).",
        "image": f"{DOMAIN}/assets/card-jabali.jpg",
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami",
        "lang": "en",
        "section": "obra-historia-de-un-jabali"
    },
    "en/obra-a-fuego.html": {
        "src": "en/obra-a-fuego/index.html",
        "dest": "en/obra-a-fuego/index.html",
        "url": f"{DOMAIN}/en/obra-a-fuego/",
        "title": "A Fuego by Pablo Macho Otero | IHTF 40",
        "description": "A Fuego, written and performed by Pablo Macho Otero (Spain). 40th International Hispanic Theatre Festival of Miami.",
        "image": f"{DOMAIN}/assets/card-a-fuego.jpg",
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami",
        "lang": "en",
        "section": "obra-a-fuego"
    },
    "en/obra-odd-man-out.html": {
        "src": "en/obra-odd-man-out/index.html",
        "dest": "en/obra-odd-man-out/index.html",
        "url": f"{DOMAIN}/en/obra-odd-man-out/",
        "title": "Odd Man Out (Blind Immersive Experience) | IHTF 40",
        "description": "Odd Man Out, an immersive sensory experience in complete darkness by PITCHBLACK Airlines (USA).",
        "image": f"{DOMAIN}/assets/card-odd.jpg",
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami",
        "lang": "en",
        "section": "obra-odd-man-out"
    },
    "en/obra-sueno.html": {
        "src": "en/obra-sueno/index.html",
        "dest": "en/obra-sueno/index.html",
        "url": f"{DOMAIN}/en/obra-sueno/",
        "title": "Sueño by Compañía Criolla | IHTF 40",
        "description": "Sueño, reimagined by Emiliano Dionisi from Shakespeare's text (Argentina).",
        "image": f"{DOMAIN}/assets/card-sueno.jpg",
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami",
        "lang": "en",
        "section": "obra-sueno"
    },
    "en/obra-robinson-crusoe.html": {
        "src": "en/obra-robinson-crusoe/index.html",
        "dest": "en/obra-robinson-crusoe/index.html",
        "url": f"{DOMAIN}/en/obra-robinson-crusoe/",
        "title": "The Amazing Adventures of Robinson Crusoe | IHTF 40",
        "description": "The Amazing Adventures of Robinson Crusoe (International Children's Day) at IHTF 40.",
        "image": f"{DOMAIN}/assets/card-robinson.jpg",
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami",
        "lang": "en",
        "section": "obra-robinson-crusoe"
    },
    "en/obra-pundonor.html": {
        "src": "en/obra-pundonor/index.html",
        "dest": "en/obra-pundonor/index.html",
        "url": f"{DOMAIN}/en/obra-pundonor/",
        "title": "Pundonor by Andrea Garrote | IHTF 40",
        "description": "Pundonor, solo performance by Andrea Garrote (Argentina). 40th International Hispanic Theatre Festival of Miami.",
        "image": f"{DOMAIN}/assets/card-pundonor.jpg",
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami",
        "lang": "en",
        "section": "obra-pundonor"
    },
    "en/obra-hamlet.html": {
        "src": "en/obra-hamlet/index.html",
        "dest": "en/obra-hamlet/index.html",
        "url": f"{DOMAIN}/en/obra-hamlet/",
        "title": "Hamlet by Chela De Ferrari | IHTF 40",
        "description": "Hamlet, free version by Chela De Ferrari performed by actors with Down syndrome (Peru).",
        "image": f"{DOMAIN}/assets/card-hamlet.jpg",
        "locale": "en_US",
        "site_name": "International Hispanic Theatre Festival of Miami",
        "lang": "en",
        "section": "obra-hamlet"
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

def fix_asset_paths(content, dest_depth):
    # For depth 1 (es/index.html or en/index.html):
    # '../style.css', '../fonts.css', '../assets/...', '../data.js'
    # For depth 2 (es/nosotros/index.html or en/nosotros/index.html):
    # '../../style.css', '../../fonts.css', '../../assets/...', '../../data.js'

    if dest_depth == 1:
        # replace any root level asset paths to ../
        content = re.sub(r'href="\.\./\.\./', 'href="../', content)
        content = re.sub(r'src="\.\./\.\./', 'src="../', content)

        content = re.sub(r'href="(?!(?:https?://|\.\./|#|javascript:))', 'href="../', content)
        # But fix stylesheet names that got double ../
        content = content.replace('href="../../', 'href="../')

        # fix css/js/img src/href
        content = re.sub(r'href="style\.css', 'href="../style.css', content)
        content = re.sub(r'href="fonts\.css', 'href="../fonts.css', content)
        content = re.sub(r'src="assets/', 'src="../assets/', content)
        content = re.sub(r'src="data\.js"', 'src="../data.js"', content)

    elif dest_depth == 2:
        # Ensure depth 2 uses ../../
        content = re.sub(r'href="\.\./style\.css', 'href="../../style.css', content)
        content = re.sub(r'href="\.\./fonts\.css', 'href="../../fonts.css', content)
        content = re.sub(r'href="\.\./nosotros\.css', 'href="../../nosotros.css', content)
        content = re.sub(r'href="nosotros\.css', 'href="../../nosotros.css', content)
        content = re.sub(r'href="\.\./agenda\.css', 'href="../../agenda.css', content)
        content = re.sub(r'href="agenda\.css', 'href="../../agenda.css', content)
        content = re.sub(r'href="calendario\.css', 'href="../../calendario.css', content)
        content = re.sub(r'href="contactanos\.css', 'href="../../contactanos.css', content)
        content = re.sub(r'href="dia-internacional-del-nino\.css', 'href="../../dia-internacional-del-nino.css', content)
        content = re.sub(r'href="eventos-adicionales\.css', 'href="../../eventos-adicionales.css', content)
        content = re.sub(r'href="inscripciones\.css', 'href="../../inscripciones.css', content)
        content = re.sub(r'href="obra\.css', 'href="../../obra.css', content)
        content = re.sub(r'href="sponsors\.css', 'href="../../sponsors.css', content)
        content = re.sub(r'href="teatros\.css', 'href="../../teatros.css', content)

        content = re.sub(r'src="\.\./assets/', 'src="../../assets/', content)
        content = re.sub(r'src="assets/', 'src="../../assets/', content)
        content = re.sub(r'src="\.\./data\.js"', 'src="../../data.js"', content)
        content = re.sub(r'src="data\.js"', 'src="../../data.js"', content)

    return content

def fix_navigation_links(content, lang, dest_depth):
    # In es/index.html (depth 1):
    # nav links: agenda/, calendario/, nosotros/, etc.
    # home link: ./#inicio or ./
    # In es/nosotros/index.html (depth 2):
    # nav links: ../agenda/, ../calendario/, ../nosotros/, etc.
    # home link: ../#inicio or ../

    if dest_depth == 1:
        prefix = ""
        home_href = "./#inicio"
    elif dest_depth == 2:
        prefix = "../"
        home_href = "../#inicio"

    replacements = [
        ('href="../#inicio"', f'href="{home_href}"'),
        ('href="./#inicio"', f'href="{home_href}"'),
        ('href="index.html#inicio"', f'href="{home_href}"'),
        ('href="../nosotros/#compania"', f'href="{prefix}nosotros/#compania"'),
        ('href="nosotros/#compania"', f'href="{prefix}nosotros/#compania"'),
        ('href="../nosotros/#personal"', f'href="{prefix}nosotros/#personal"'),
        ('href="nosotros/#personal"', f'href="{prefix}nosotros/#personal"'),
        ('href="../nosotros/"', f'href="{prefix}nosotros/"'),
        ('href="nosotros/"', f'href="{prefix}nosotros/"'),
        ('href="../agenda/"', f'href="{prefix}agenda/"'),
        ('href="agenda/"', f'href="{prefix}agenda/"'),
        ('href="../calendario/"', f'href="{prefix}calendario/"'),
        ('href="calendario/"', f'href="{prefix}calendario/"'),
        ('href="../eventos-adicionales/"', f'href="{prefix}eventos-adicionales/"'),
        ('href="eventos-adicionales/"', f'href="{prefix}eventos-adicionales/"'),
        ('href="../dia-internacional-del-nino/"', f'href="{prefix}dia-internacional-del-nino/"'),
        ('href="dia-internacional-del-nino/"', f'href="{prefix}dia-internacional-del-nino/"'),
        ('href="../teatros/"', f'href="{prefix}teatros/"'),
        ('href="teatros/"', f'href="{prefix}teatros/"'),
        ('href="../sponsors/"', f'href="{prefix}sponsors/"'),
        ('href="sponsors/"', f'href="{prefix}sponsors/"'),
        ('href="../contactanos/"', f'href="{prefix}contactanos/"'),
        ('href="contactanos/"', f'href="{prefix}contactanos/"'),
        ('href="../inscripciones/"', f'href="{prefix}inscripciones/"'),
        ('href="inscripciones/"', f'href="{prefix}inscripciones/"'),
        ('href="../obra/"', f'href="{prefix}obra/"'),
        ('href="obra/"', f'href="{prefix}obra/"'),
        ('href="../obra-a-fuego/"', f'href="{prefix}obra-a-fuego/"'),
        ('href="obra-a-fuego/"', f'href="{prefix}obra-a-fuego/"'),
        ('href="../obra-carrusel/"', f'href="{prefix}obra-carrusel/"'),
        ('href="obra-carrusel/"', f'href="{prefix}obra-carrusel/"'),
        ('href="../obra-hamlet/"', f'href="{prefix}obra-hamlet/"'),
        ('href="obra-hamlet/"', f'href="{prefix}obra-hamlet/"'),
        ('href="../obra-historia-de-un-jabali/"', f'href="{prefix}obra-historia-de-un-jabali/"'),
        ('href="obra-historia-de-un-jabali/"', f'href="{prefix}obra-historia-de-un-jabali/"'),
        ('href="../obra-odd-man-out/"', f'href="{prefix}obra-odd-man-out/"'),
        ('href="obra-odd-man-out/"', f'href="{prefix}obra-odd-man-out/"'),
        ('href="../obra-pundonor/"', f'href="{prefix}obra-pundonor/"'),
        ('href="obra-pundonor/"', f'href="{prefix}obra-pundonor/"'),
        ('href="../obra-robinson-crusoe/"', f'href="{prefix}obra-robinson-crusoe/"'),
        ('href="obra-robinson-crusoe/"', f'href="{prefix}obra-robinson-crusoe/"'),
        ('href="../obra-sueno/"', f'href="{prefix}obra-sueno/"'),
        ('href="obra-sueno/"', f'href="{prefix}obra-sueno/"'),
        ('href="../obra-zombi-manifiesto/"', f'href="{prefix}obra-zombi-manifiesto/"'),
        ('href="obra-zombi-manifiesto/"', f'href="{prefix}obra-zombi-manifiesto/"'),
    ]

    for old_href, new_href in replacements:
        content = content.replace(old_href, new_href)

    return content

def fix_language_switcher(content, cfg):
    lang = cfg["lang"]
    section = cfg["section"]
    dest_depth = len(cfg["dest"].split("/")) - 1

    if lang == "es":
        # From es/index.html (depth 1) -> ../en/
        # From es/nosotros/index.html (depth 2) -> ../../en/nosotros/
        if section == "":
            en_target = "../en/"
        else:
            en_target = f"../../en/{section}/"
            
        old_js_regex = r'langOpts\[1\]\.addEventListener\("click",\s*function\s*\(\)\s*\{[^}]*\}\);'
        new_js = f"""langOpts[1].addEventListener("click", function () {{
            localStorage.setItem("preferred_lang", "en");
            window.location.href = "{en_target}";
          }});"""
        content = re.sub(old_js_regex, new_js, content, flags=re.DOTALL)

    elif lang == "en":
        # From en/index.html (depth 1) -> ../es/
        # From en/nosotros/index.html (depth 2) -> ../../es/nosotros/
        if section == "":
            es_target = "../es/"
        else:
            es_target = f"../../es/{section}/"

        old_js_regex = r'langOpts\[0\]\.addEventListener\("click",\s*function\s*\(\)\s*\{[^}]*\}\);'
        new_js = f"""langOpts[0].addEventListener("click", function () {{
            localStorage.setItem("preferred_lang", "es");
            window.location.href = "{es_target}";
          }});"""
        content = re.sub(old_js_regex, new_js, content, flags=re.DOTALL)

    return content

def add_iframe_and_dynamic_seo_js(content, cfg):
    dest = cfg["dest"]
    lang = cfg["lang"]

    iframe_script = """
  <script>
    document.addEventListener("DOMContentLoaded", function() {
      if (window.top !== window.self) {
        document.querySelectorAll('a[href]').forEach(function(link) {
          var href = link.getAttribute('href');
          if (href && !href.startsWith('#') && !href.startsWith('javascript:') && !href.startsWith('mailto:') && !href.startsWith('tel:')) {
            link.setAttribute('target', '_top');
          }
        });
      }
    });
  </script>
"""
    if "</body>" in content and "window.top !== window.self" not in content:
        content = content.replace("</body>", f"{iframe_script}\n</body>")

    if dest in ["es/obra/index.html", "en/obra/index.html"]:
        dyn_pattern = r'document\.title\s*=\s*`\${play\.title}[^`]*`;'
        
        base_url = f"{DOMAIN}/en/obra/" if lang == "en" else f"{DOMAIN}/es/obra/"
        suffix = "International Hispanic Theatre Festival" if lang == "en" else "Festival Internacional de Teatro Hispano"

        new_dyn_seo = f"""
      const dynamicTitle = `${{play.title}} | {suffix}`;
      const dynamicDesc = play.description ? play.description.substring(0, 160) : "{cfg['description']}";
      const dynamicUrl = `{base_url}?play=${{playId}}`;

      document.title = dynamicTitle;

      function updateMetaTag(selector, attr, val) {{
        let el = document.querySelector(selector);
        if (el) el.setAttribute(attr, val);
      }}

      updateMetaTag('meta[name="description"]', 'content', dynamicDesc);
      updateMetaTag('meta[property="og:title"]', 'content', dynamicTitle);
      updateMetaTag('meta[property="og:description"]', 'content', dynamicDesc);
      updateMetaTag('meta[property="og:url"]', 'content', dynamicUrl);
      updateMetaTag('meta[name="twitter:title"]', 'content', dynamicTitle);
      updateMetaTag('meta[name="twitter:description"]', 'content', dynamicDesc);
      updateMetaTag('meta[name="twitter:url"]', 'content', dynamicUrl);
      updateMetaTag('link[rel="canonical"]', 'href', dynamicUrl);
"""
        content = re.sub(dyn_pattern, new_dyn_seo, content)

    return content

def create_root_redirect():
    redirect_html = f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>IHTF 40 | Festival Internacional de Teatro Hispano de Miami</title>
  <meta name="description" content="Programación oficial del 40° Festival Internacional de Teatro Hispano de Miami." />
  <link rel="canonical" href="{DOMAIN}/es/" />
  <meta http-equiv="refresh" content="0;url=es/" />
  <script>
    var preferredLang = localStorage.getItem("preferred_lang");
    if (preferredLang === "en") {{
      window.location.replace("en/");
    }} else {{
      window.location.replace("es/");
    }}
  </script>
</head>
<body>
  <p>Redirigiendo a <a href="es/">es/</a>...</p>
</body>
</html>"""
    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(redirect_html)
    print("Created root redirect index.html")

def main():
    print("Starting es/ subfolder refactor...")

    source_contents = {}
    for key, cfg in PAGES_CONFIG.items():
        src_path = os.path.join(BASE_DIR, cfg["src"])
        if not os.path.exists(src_path):
            print(f"Warning: Source file {src_path} does not exist.")
            continue
        with open(src_path, "r", encoding="utf-8") as f:
            source_contents[key] = f.read()

    for key, cfg in PAGES_CONFIG.items():
        if key not in source_contents:
            continue

        content = source_contents[key]
        dest_rel = cfg["dest"]
        dest_depth = len(dest_rel.split("/")) - 1

        # 1. Update <head> metadata
        content = re.sub(r'\s*<title>.*?</title>', '', content, flags=re.DOTALL)
        content = re.sub(r'\s*<meta name="description"[^>]*>', '', content)
        content = re.sub(r'\s*<link rel="canonical"[^>]*>', '', content)
        content = re.sub(r'\s*<meta property="og:[^>]*>', '', content)
        content = re.sub(r'\s*<meta name="twitter:[^>]*>', '', content)
        content = re.sub(r'\s*<!-- Open Graph / Facebook / WhatsApp -->', '', content)
        content = re.sub(r'\s*<!-- Twitter -->', '', content)

        new_meta = generate_head_meta(cfg)
        if "<head>" in content:
            content = content.replace("<head>", f"<head>\n{new_meta}", 1)

        # 2. Fix asset paths
        content = fix_asset_paths(content, dest_depth)

        # 3. Fix navigation links
        content = fix_navigation_links(content, cfg["lang"], dest_depth)

        # 4. Fix language switcher JS
        content = fix_language_switcher(content, cfg)

        # 5. Add iframe target="_top" & dynamic SEO JS
        content = add_iframe_and_dynamic_seo_js(content, cfg)

        dest_path = os.path.join(BASE_DIR, dest_rel)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Created: {dest_rel}")

    # Remove root level Spanish folders that were moved to es/
    root_folders_to_remove = [
        "nosotros", "agenda", "calendario", "eventos-adicionales", "dia-internacional-del-nino",
        "teatros", "sponsors", "contactanos", "inscripciones", "obra", "obra-a-fuego",
        "obra-carrusel", "obra-hamlet", "obra-historia-de-un-jabali", "obra-odd-man-out",
        "obra-pundonor", "obra-robinson-crusoe", "obra-sueno", "obra-zombi-manifiesto"
    ]
    for folder in root_folders_to_remove:
        folder_path = os.path.join(BASE_DIR, folder)
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            shutil.rmtree(folder_path)
            print(f"Removed root folder: {folder}")

    # Create root index.html redirect
    create_root_redirect()

    print("Refactor complete!")

if __name__ == "__main__":
    main()
