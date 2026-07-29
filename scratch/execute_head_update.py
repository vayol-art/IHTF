import os
import re

BASE_DIR = "/Users/vanessa/Documents/IHTF"
DOMAIN = "https://vayol-art.github.io/IHTF"
DEFAULT_IMG = f"{DOMAIN}/assets/afiche_1_horizontal.jpg"

PAGES_CONFIG = {
    # Spanish Pages
    "index.html": {
        "dest": "index.html",
        "url": f"{DOMAIN}/",
        "title": "IHTF 40 | Festival Internacional de Teatro Hispano de Miami",
        "description": "Programación oficial del 40° Festival Internacional de Teatro Hispano de Miami. Fechas, obras de teatro, salas y entradas.",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": ""
    },
    "nosotros.html": {
        "dest": "nosotros/index.html",
        "url": f"{DOMAIN}/nosotros/",
        "title": "Sobre Nosotros | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Conozca la historia de Teatro Avante, el equipo de trabajo, los colaboradores y los reconocimientos del Festival Internacional de Teatro Hispano de Miami.",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "nosotros"
    },
    "agenda.html": {
        "dest": "agenda/index.html",
        "url": f"{DOMAIN}/agenda/",
        "title": "Programa de Mano | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Consulte el programa de mano completo de las funciones del 40° Festival Internacional de Teatro Hispano de Miami.",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "agenda"
    },
    "calendario.html": {
        "dest": "calendario/index.html",
        "url": f"{DOMAIN}/calendario/",
        "title": "Calendario de Funciones | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Calendario con todas las fechas y horarios de las obras del 40° Festival Internacional de Teatro Hispano de Miami.",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "calendario"
    },
    "eventos-adicionales.html": {
        "dest": "eventos-adicionales/index.html",
        "url": f"{DOMAIN}/eventos-adicionales/",
        "title": "Eventos Adicionales | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Conozca los eventos adicionales, homenajes póstumos y reconocimientos especiales del 40° Festival Internacional de Teatro Hispano de Miami.",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "eventos-adicionales"
    },
    "dia-internacional-del-nino.html": {
        "dest": "dia-internacional-del-nino/index.html",
        "url": f"{DOMAIN}/dia-internacional-del-nino/",
        "title": "Día Internacional del Niño | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Celebración del Día Internacional del Niño en el Festival Internacional de Teatro Hispano de Miami. Obras de teatro y talleres infantiles.",
        "image": f"{DOMAIN}/assets/card-robinson.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "dia-internacional-del-nino"
    },
    "teatros.html": {
        "dest": "teatros/index.html",
        "url": f"{DOMAIN}/teatros/",
        "title": "Teatros y Salas | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Información sobre las salas de teatro y sedes donde se presentarán las obras del 40° Festival Internacional de Teatro Hispano de Miami.",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "teatros"
    },
    "sponsors.html": {
        "dest": "sponsors/index.html",
        "url": f"{DOMAIN}/sponsors/",
        "title": "Patrocinio y Donaciones | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Apoya al Festival Internacional de Teatro Hispano de Miami. Información sobre patrocinadores y cómo realizar donaciones.",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "sponsors"
    },
    "contactanos.html": {
        "dest": "contactanos/index.html",
        "url": f"{DOMAIN}/contactanos/",
        "title": "Contacto | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Póngase en contacto con la organización del Festival Internacional de Teatro Hispano de Miami (Teatro Avante).",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "contactanos"
    },
    "inscripciones.html": {
        "dest": "inscripciones/index.html",
        "url": f"{DOMAIN}/inscripciones/",
        "title": "Inscripciones 41° Festival | Festival Internacional de Teatro Hispano de Miami",
        "description": "Formulario de inscripción y bases para participar en el 41° Festival Internacional de Teatro Hispano de Miami.",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "inscripciones"
    },
    "obra.html": {
        "dest": "obra/index.html",
        "url": f"{DOMAIN}/obra/",
        "title": "Obras del Festival | Festival Internacional de Teatro Hispano (IHTF 40)",
        "description": "Catálogo de todas las obras teatrales del 40° Festival Internacional de Teatro Hispano de Miami.",
        "image": DEFAULT_IMG,
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "obra"
    },
    "obra-carrusel.html": {
        "dest": "obra-carrusel/index.html",
        "url": f"{DOMAIN}/obra-carrusel/",
        "title": "Carrusel por Teatro Avante | IHTF 40",
        "description": "Carrusel, obra de Abel González Melo dirigida por Jackie Briceño. Teatro Avante (EE.UU.).",
        "image": f"{DOMAIN}/assets/card-carrusel.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "obra-carrusel"
    },
    "obra-zombi-manifiesto.html": {
        "dest": "obra-zombi-manifiesto/index.html",
        "url": f"{DOMAIN}/obra-zombi-manifiesto/",
        "title": "Zombi Manifiesto por Santiago Sanguinetti | IHTF 40",
        "description": "Zombi Manifiesto, obra de Santiago Sanguinetti (Uruguay). 40° Festival Internacional de Teatro Hispano de Miami.",
        "image": f"{DOMAIN}/assets/card-zombi.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "obra-zombi-manifiesto"
    },
    "obra-historia-de-un-jabali.html": {
        "dest": "obra-historia-de-un-jabali/index.html",
        "url": f"{DOMAIN}/obra-historia-de-un-jabali/",
        "title": "Historia de un jabalí (o algo de Ricardo) | IHTF 40",
        "description": "Historia de un jabalí (o algo de Ricardo), de Gabriel Calderón y dirigida por Cristian Plana (Chile).",
        "image": f"{DOMAIN}/assets/card-jabali.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "obra-historia-de-un-jabali"
    },
    "obra-a-fuego.html": {
        "dest": "obra-a-fuego/index.html",
        "url": f"{DOMAIN}/obra-a-fuego/",
        "title": "A fuego por Pablo Macho Otero | IHTF 40",
        "description": "A fuego, monólogo de Pablo Macho Otero (España). 40° Festival Internacional de Teatro Hispano de Miami.",
        "image": f"{DOMAIN}/assets/card-a-fuego.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "obra-a-fuego"
    },
    "obra-odd-man-out.html": {
        "dest": "obra-odd-man-out/index.html",
        "url": f"{DOMAIN}/obra-odd-man-out/",
        "title": "Odd Man Out (Experiencia Inmersiva a Ciegas) | IHTF 40",
        "description": "Odd Man Out, experiencia sensorial inmersiva en completa oscuridad por PITCHBLACK Airlines (EE.UU.).",
        "image": f"{DOMAIN}/assets/card-odd.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "obra-odd-man-out"
    },
    "obra-sueno.html": {
        "dest": "obra-sueno/index.html",
        "url": f"{DOMAIN}/obra-sueno/",
        "title": "Sueño por Compañía Criolla | IHTF 40",
        "description": "Sueño, obra reimaginada por Emiliano Dionisi sobre texto de Shakespeare (Argentina).",
        "image": f"{DOMAIN}/assets/card-sueno.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "obra-sueno"
    },
    "obra-robinson-crusoe.html": {
        "dest": "obra-robinson-crusoe/index.html",
        "url": f"{DOMAIN}/obra-robinson-crusoe/",
        "title": "Las Asombrosas Aventuras de Robinson Crusoe | IHTF 40",
        "description": "Las Asombrosas Aventuras de Robinson Crusoe (Día Internacional del Niño) en el IHTF 40.",
        "image": f"{DOMAIN}/assets/card-robinson.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "obra-robinson-crusoe"
    },
    "obra-pundonor.html": {
        "dest": "obra-pundonor/index.html",
        "url": f"{DOMAIN}/obra-pundonor/",
        "title": "Pundonor por Andrea Garrote | IHTF 40",
        "description": "Pundonor, unipersonal de Andrea Garrote (Argentina). 40° Festival Internacional de Teatro Hispano de Miami.",
        "image": f"{DOMAIN}/assets/card-pundonor.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "obra-pundonor"
    },
    "obra-hamlet.html": {
        "dest": "obra-hamlet/index.html",
        "url": f"{DOMAIN}/obra-hamlet/",
        "title": "Hamlet por Chela De Ferrari | IHTF 40",
        "description": "Hamlet, versión libre de Chela De Ferrari interpretada por actores con síndrome de Down (Perú).",
        "image": f"{DOMAIN}/assets/card-hamlet.jpg",
        "locale": "es_US",
        "site_name": "Festival Internacional de Teatro Hispano de Miami",
        "lang": "es",
        "section": "obra-hamlet"
    },

    # English Pages
    "en/index.html": {
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

def main():
    print("Injecting head meta tags into all dest index.html files...")

    for src_rel, cfg in PAGES_CONFIG.items():
        dest_rel = cfg["dest"]
        dest_path = os.path.join(BASE_DIR, dest_rel)

        if not os.path.exists(dest_path):
            print(f"Skipping missing dest file: {dest_path}")
            continue

        with open(dest_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Clean any existing meta tags first
        content = re.sub(r'\s*<title>.*?</title>', '', content, flags=re.DOTALL)
        content = re.sub(r'\s*<meta name="description"[^>]*>', '', content)
        content = re.sub(r'\s*<link rel="canonical"[^>]*>', '', content)
        content = re.sub(r'\s*<meta property="og:[^>]*>', '', content)
        content = re.sub(r'\s*<meta name="twitter:[^>]*>', '', content)
        content = re.sub(r'\s*<!-- Open Graph / Facebook / WhatsApp -->', '', content)
        content = re.sub(r'\s*<!-- Twitter -->', '', content)

        new_meta = generate_head_meta(cfg)

        # Insert cleanly right after <head> or <meta charset...>
        if "<head>" in content:
            content = content.replace("<head>", f"<head>\n{new_meta}", 1)

        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Updated metadata in: {dest_rel}")

    print("Head meta injection complete!")

if __name__ == "__main__":
    main()
