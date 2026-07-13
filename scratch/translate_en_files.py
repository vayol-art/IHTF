import os

en_dir = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF\en"

# A map of exact text replacements for translation in English HTML files
common_replacements = [
    # 1. Navigation Menu
    ('<a href="nosotros.html" class="nav-dropdown-trigger">SOBRE NOSOTROS</a>', '<a href="nosotros.html" class="nav-dropdown-trigger">ABOUT US</a>'),
    ('<a href="nosotros.html#compania" class="submenu-item">La Compañía</a>', '<a href="nosotros.html#compania" class="submenu-item">The Company</a>'),
    ('<a href="nosotros.html#personal" class="submenu-item">Personal</a>', '<a href="nosotros.html#personal" class="submenu-item">Staff</a>'),
    ('<a href="nosotros.html#premios" class="submenu-item">Premios</a>', '<a href="nosotros.html#premios" class="submenu-item">Awards</a>'),
    ('<a href="agenda.html" class="nav-dropdown-trigger">PROGRAMA</a>', '<a href="agenda.html" class="nav-dropdown-trigger">PROGRAM</a>'),
    ('<a href="agenda.html" class="submenu-item">Programa de Mano</a>', '<a href="agenda.html" class="submenu-item">Playbill</a>'),
    ('<a href="calendario.html" class="submenu-item">Calendario</a>', '<a href="calendario.html" class="submenu-item">Calendar</a>'),
    ('<a href="eventos-adicionales.html" class="submenu-item">Eventos Adicionales</a>', '<a href="eventos-adicionales.html" class="submenu-item">Additional Events</a>'),
    ('<a href="dia-internacional-del-nino.html" class="submenu-item">Día Internacional del Niño</a>', '<a href="dia-internacional-del-nino.html" class="submenu-item">International Children\'s Day</a>'),
    ('<a href="teatros.html" class="submenu-item">Teatros</a>', '<a href="teatros.html" class="submenu-item">Theaters</a>'),
    ('<a href="sponsors.html" class="submenu-item">Apoya IHTF</a>', '<a href="sponsors.html" class="submenu-item">Support IHTF</a>'),
    ('<a href="contactanos.html">CONTÁCTANOS</a>', '<a href="contactanos.html">CONTACT US</a>'),
    ('<a href="#">INSCRIPCIONES 40° FESTIVAL</a>', '<a href="#">40th FESTIVAL REGISTRATIONS</a>'),
    
    # 2. Footer Section
    ('<h2>Suscríbete a nuestro Newsletter</h2>', '<h2>Subscribe to our Newsletter</h2>'),
    ('<p>Recibe información actualizada sobre el IHTF</p>', '<p>Receive updated information about IHTF</p>'),
    ('<input type="email" placeholder="Ingresa tu correo" aria-label="Ingresa tu correo" />', '<input type="email" placeholder="Enter your email" aria-label="Enter your email" />'),
    ('<button type="submit">Enviar &rarr;</button>', '<button type="submit">Submit &rarr;</button>'),
    ('<a href="#">Políticas de privacidad</a>', '<a href="#">Privacy Policy</a>'),
    ('<a href="#">Términos y condiciones</a>', '<a href="#">Terms & Conditions</a>'),

    # 3. Country Badges
    ('<span class="country-badge">España</span>', '<span class="country-badge">Spain</span>'),
    ('<span class="country-badge">Perú</span>', '<span class="country-badge">Peru</span>'),
    ('<div class="country">España</div>', '<div class="country">Spain</div>'),
    ('<div class="country">Perú</div>', '<div class="country">Peru</div>'),

    # 4. Standard Badges and Buttons
    ('<small class="foro-label">Foro</small>', '<small class="foro-label">Forum</small>'),
    ('<span class="kids-badge">Día Internacional del Niño</span>', '<span class="kids-badge">International Children\'s Day</span>'),
    ('Entradas</a>', 'Tickets</a>'),
    ('Reservar</a>', 'Reserve</a>'),
    ('Comprar entradas</a>', 'Buy tickets</a>'),
    ('Más información</a>', 'More information</a>')
]

file_specific_replacements = {
    "index.html": [
        # Hero and scroll
        ('<span class="scroll-text">Desliza</span>', '<span class="scroll-text">Scroll</span>'),
        ('<h2>IHTF comienza en</h2>', '<h2>IHTF starts in</h2>'),
        ('<span>Días</span>', '<span>Days</span>'),
        ('<span>Horas</span>', '<span>Hours</span>'),
        ('<span>Minutos</span>', '<span>Minutes</span>'),
        ('<span>Segundos</span>', '<span>Seconds</span>'),
        # Expect section
        ('<h2>Qué esperar</h2>', '<h2>What to Expect</h2>'),
        ('<strong>9</strong><span>Producciones</span>', '<strong>9</strong><span>Productions</span>'),
        ('<strong>+2</strong><span>Idiomas accesibles</span>', '<strong>+2</strong><span>Accessible languages</span>'),
        ('<strong>4</strong><span>Teatros</span>', '<strong>+4</strong><span>Theaters</span>'),
        ('<strong>+28</strong><span>Días en cartelera</span>', '<strong>+28</strong><span>Days on billboard</span>'),
        ('<strong>6</strong><span>Países representados</span>', '<strong>6</strong><span>Represented countries</span>'),
        ('<strong>+5</strong><span>Para todas las edades</span>', '<strong>+5</strong><span>For all ages</span>'),
        ('<a class="primary-cta" href="agenda.html">Programa</a>', '<a class="primary-cta" href="agenda.html">Program</a>'),
        # Program summary header
        ('<h2>RESUMEN DEL PROGRAMA</h2>', '<h2>PROGRAM SUMMARY</h2>')
    ],
    "nosotros.html": [
        # Hero
        ('<h1>Sobre Nosotros</h1>', '<h1>About Us</h1>'),
        # Mission
        ('<p>"Preservar, desarrollar y enriquecer nuestra herencia cultural hispana a través de la creación y presentación del teatro universal y programas educativos, y participar en el crecimiento artístico y la expansión del teatro mundial al presentar algunas de las mejores compañías teatrales del mundo en el galardonado Festival Internacional de Teatro Hispano de Miami, presentado por Avante."</p>',
         '<p>"To preserve, develop, and enrich our Hispanic cultural heritage through the creation and presentation of universal theater and educational programs, and to participate in the artistic growth and expansion of world theater by presenting some of the world\'s finest theater companies in the award-winning International Hispanic Theatre Festival of Miami, presented by Avante."</p>'),
        # Staff list
        ('<h3>Directores</h3>', '<h3>Directors</h3>'),
        ('<li>Verónica Sánchez <em>Presidente</em></li>', '<li>Verónica Sánchez <em>President</em></li>'),
        ('<li>Edna Schwab <em>Tesorera</em></li>', '<li>Edna Schwab <em>Treasurer</em></li>'),
        ('<li>Beatriz J. Rizk <em>Secretaria</em></li>', '<li>Beatriz J. Rizk <em>Secretary</em></li>'),
        ('<span class="note">*Fallecido</span>', '<span class="note">*Deceased</span>'),
        ('<span class="staff-note">* Fallecido</span>', '<span class="staff-note">* Deceased</span>'),
        ('<h2>Personal y Colaboradores</h2>', '<h2>Staff and Collaborators</h2>'),
        ('<p>Director emérito artístico de producción y director de festivales</p>', '<p>Emeritus Producing Artistic Director & Festival Director</p>'),
        ('<p>Directora artística del festival<br><strong>Conecta Miami Arts</strong></p>', '<p>Festival Artistic Director<br><strong>Conecta Miami Arts</strong></p>'),
        ('<p>Directora ejecutiva del festival<br><strong>Conecta Miami Arts</strong></p>', '<p>Festival Executive Director<br><strong>Conecta Miami Arts</strong></p>'),
        ('<p>Directora del Programa Educativo y Consultora Literaria</p>', '<p>Educational Program Director & Literary Consultant</p>'),
        ('<p>Director emérito</p>', '<p>Emeritus Director</p>'),
        ('<p>Gerente de producción</p>', '<p>Production Manager</p>'),
        ('<p>Director Técnico</p>', '<p>Technical Director</p>'),
        ('<p>Gerente de Marketing y Taquilla</p>', '<p>Marketing & Box Office Manager</p>'),
        ('<p>Marketing</p>', '<p>Marketing</p>'),
        ('<p>Editor de sitio web y diseñador de redes sociales</p>', '<p>Website Editor & Social Media Designer</p>'),
        ('<p>Gerente de redes sociales</p>', '<p>Social Media Manager</p>'),
        ('<p>Diseñadores de escenografía, vestuario y utilería</p>', '<p>Scenic, Costume & Prop Designers</p>'),
        ('<p>Coordinadores del Día Internacional del Niño</p>', '<p>International Children\'s Day Coordinators</p>'),
        ('<p>Diseñadora Gráfica</p>', '<p>Graphic Designer</p>'),
        ('<p>Videógrafo</p>', '<p>Videographer</p>'),
        # Avante history
        ('<p>Fundada en 1979, Teatro Avante es una organización cultural sin fines de lucro y exenta de impuestos cuyo objetivo esencial es la preservación de la herencia cultural hispana.</p>',
         '<p>Founded in 1979, Teatro Avante is a non-profit, tax-exempt cultural organization whose primary goal is the preservation of Hispanic cultural heritage.</p>'),
        ('<p>El grupo ha representado a Estados Unidos en México, Costa Rica, España, Japón, Francia, Colombia, República Dominicana, Guatemala, Portugal, Perú, Brasil, Venezuela, Argentina, Puerto Rico y Eslovenia, además de, en Estados Unidos, Nueva York, Albuquerque, Los Ángeles, El Paso y Buffalo.</p>',
         '<p>The group has represented the United States in Mexico, Costa Rica, Spain, Japan, France, Colombia, Dominican Republic, Guatemala, Portugal, Peru, Brazil, Venezuela, Argentina, Puerto Rico, and Slovenia, as well as, within the United States, New York, Albuquerque, Los Angeles, El Paso, and Buffalo.</p>'),
        ('<p>Ha llevado a la escena textos de Albee, Alomá, Ariza, Assad, Cabrujas, Cocteau, Ferrer, García Lorca, Manet, Matas, Pinto, Piñera, Reguera Saumell, Santana, Triana, Valle-Inclán, Williams, Orwell y Shakespeare, entre otros.</p>',
         '<p>It has staged plays by Albee, Alomá, Ariza, Assad, Cabrujas, Cocteau, Ferrer, García Lorca, Manet, Matas, Pinto, Piñera, Reguera Saumell, Santana, Triana, Valle-Inclán, Williams, Orwell, and Shakespeare, among others.</p>'),
        ('<p>En 1994, las Olimpiadas Culturales del Comité Olímpico de Atlanta honraron a Teatro Avante con el Premio Regional de las Artes.</p>',
         '<p>In 1994, the Cultural Olympiad of the Atlanta Olympic Committee honored Teatro Avante with the Regional Arts Award.</p>'),
        ('<p>Ese mismo año recibió el premio Ollantay en Madrid; en 1995, el Federico García Lorca en Fuente Vaqueros, España; en 2004 el Kusillo en La Paz; en 2009 el FIT de Cádiz-Atahualpa del Cioppo en Cádiz; y en 2012 el de la Universidad Científica del Sur (UCSUR) en Lima.</p>',
         '<p>That same year it received the Ollantay Award in Madrid; in 1995, the Federico García Lorca Award in Fuente Vaqueros, Spain; in 2004 the Kusillo Award in La Paz; in 2009 the FIT of Cádiz-Atahualpa del Cioppo in Cádiz; and in 2012 that of the Universidad Científica del Sur (UCSUR) in Lima.</p>'),
        ('<p>Teatro Avante produce y presenta el galardonado Festival Internacional de Teatro Hispano de Miami.</p>',
         '<p>Teatro Avante produces and presents the award-winning International Hispanic Theatre Festival of Miami.</p>'),
        # Tribute Mario
        ('<div class="subtitle">Un gigante de las tablas</div>', '<div class="subtitle">A Giant of the Stage</div>'),
        ('<p>En 2009 cuando el Festival Iberoamericano de Teatro de Cádiz le otorgó el premio Atahualpa del Cioppo al Festival Internacional de Teatro Hispano de Miami, afirmaba que el festival tenía nombre propio, se llamaba Mario Ernesto Sánchez.',
         '<p>In 2009, when the Ibero-American Theater Festival of Cádiz awarded the Atahualpa del Cioppo Prize to the International Hispanic Theatre Festival of Miami, it stated that the festival had its own name, and it was Mario Ernesto Sánchez.'),
        ('Solamente el empeño de este gigante de las tablas (y no me refiero sólo a su tamaño natural), fue capaz de llevar a cabo la ardua labor que se había impuesto desde hacía ya varias décadas, la de preservar la cultura hispana en Estados Unidos, "que tanto contribuye a la calidad de vida de todos," como afirmó una vez. La historia del uno fue y sigue siendo inseparable de la del otro. Desde un principio no se perfilaba como una tarea sencilla de concretar; sin embargo, su manifiesta tenacidad y obstinación estarían de su parte, características que con toda seguridad trajo consigo desde su ciudad natal San Antonio de las Vegas, en Cuba.</p>',
         'Only the dedication of this stage giant (and I do not only refer to his natural size) was capable of carrying out the arduous work he had set for himself for several decades: to preserve Hispanic culture in the United States, "which contributes so much to the quality of life of all," as he once stated. The history of the one was and remains inseparable from that of the other. From the beginning, it did not shape up to be an easy task to realize; however, his manifest tenacity and obstinacy would be on his side, characteristics that he surely brought with him from his hometown of San Antonio de las Vegas, in Cuba.</p>'),
        ('<p>Ya ha pasado mucha agua bajo el puente desde que un grupo de teatristas y activistas de la cultura de Miami se juntara en 1986, bajo el nombre de Acting Together (Actuando en Conjunto) y presentara lo que se llamó el Primer Festival Anual de Teatro Hispano con producciones locales. No es coincidencia, de paso, que este año le estemos otorgando el premio Una Vida de Dedicación a las Artes Escénicas a Olga Garay-English quien fuera parte de ese primer contingente artístico que se preocupó, y sigue preocupándose, por fomentar un arte teatral significativo que pueda generar placer en un público a la vez que reflexión y entendimiento humano sobre temas relevantes.',
         '<p>A lot of water has run under the bridge since a group of theater makers and cultural activists from Miami gathered in 1986 under the name Acting Together and presented what was called the First Annual Hispanic Theatre Festival with local productions. It is no coincidence, by the way, that this year we are presenting the Lifetime Dedication to the Performing Arts Award to Olga Garay-English, who was part of that first artistic contingent that cared, and continues to care, about promoting significant theatrical art that can generate pleasure in an audience while encouraging reflection and human understanding on relevant issues.'),
        ('Ya para el año 1989, el festival se había internacionalizado invitando grupos de fuera, como sucedió al incorporarse España, Colombia, Puerto Rico y Costa Rica a la programación, sino que la gestión pasó enteramente a manos de Mario Ernesto. Y el resto, como dice el refrán, ya es historia. Han pasado por las salas del festival innumerables espectáculos del mundo ibérico e iberoamericano, y de alguno que otro país que se aventuró a montar obras de autores de origen hispano, el único requisito del festival, como pasó con las compañías Lasenkan Theatre de Japón (2003), Insightout de Dinamarca (2005), y el grupo esloveno Ljubijana City Theatre (2008). Aprovechamos esta instancia para darle la bienvenida a las nueve compañías, locales, nacionales e internacionales, que nos honran con su presencia en esta ocasión.</p>',
         'By 1989, the festival had internationalized, inviting groups from abroad, as occurred when Spain, Colombia, Puerto Rico, and Costa Rica joined the program, and management passed entirely into the hands of Mario Ernesto. And the rest, as the saying goes, is history. Countless shows from the Iberian and Ibero-American world have passed through the festival\'s venues, along with a few from other countries that ventured to stage plays by authors of Hispanic origin—the festival\'s only requirement—as occurred with the companies Lasenkan Theatre from Japan (2003), Insightout from Denmark (2005), and the Slovenian group Ljubljana City Theatre (2008). We take this opportunity to welcome the nine local, national, and international companies that honor us with their presence on this occasion.</p>'),
        ('<p>Su otro gran logro fue indiscutiblemente la fundación de su compañía Teatro Avante. Se inició en 1978, co-fundada con Teresa María Rojas y Alina Interián, bajo el nombre de RAS Community Theatre. La obra Electra Garrigó, de Virgilio Piñera (1912-79), se escogió para su estreno trayendo para dirigirla al legendario Francisco Morín (1918- 2017), quien fuera el que la montó en La Habana en 1948, considerado por varios críticos como la introducción a la modernidad del teatro Latino Americanico.',
         '<p>His other great achievement was indisputably the founding of his company Teatro Avante. It began in 1978, co-founded with Teresa María Rojas and Alina Interián, under the name RAS Community Theatre. The play Electra Garrigó, by Virgilio Piñera (1912-79), was chosen for its premiere, bringing the legendary Francisco Morín (1918-2017) to direct it, who was the one who staged it in Havana in 1948, considered by several critics as the introduction of modernity to Latin American theater.'),
        ('Ya bajo el nombre de Avante, que nos acompaña hasta hoy, Mario Ernesto supo rodearse de un equipo estable de talentosos actores que sería difícil de listar sin omitir algunos de los que sin duda han contribuido enormemente al éxito de sus montajes. Por otra parte, entre sus colaboradores más asiduos tras bastidores se hace imposible no mencionar a Ernesto Padilla, Irene Olivera, Leiter Padilla, Gabriel Cutiño, Asela Torres, los diseñadores Pedro Balmaseda y Jorge Noa, y en no pocas ocasiones al compositor Mike Porcel. Trabajó con innumerables autores clásicos y contemporáneos entre los que sobresalen el mismo Piñera, cuyas obras llevó a la escena en ocho ocasiones, y a Abel González Melo, quien devino "dramaturgo en residencia" durante los últimos años. Como asistentes de cabecera en su empeño de llevar adelante el Festival contó con los miembros más allegados de su familia, con Verónica y Gastón en primera línea, así como la autora de estas líneas quien ha estado a cargo del Componente Educativo desde 1994. El festival, en esta nueva etapa que comienza, no puede haber quedado en mejores manos que las de Melissa Messulam y Néher Jacqueline Briceño, allegadas colaboradoras y colegas, a quienes Mario Ernesto designó como sucesoras al frente de las instituciones que fueron parte de su múltiple legado.</p>',
         'Already under the name Avante, which accompanies us to this day, Mario Ernesto knew how to surround himself with a stable team of talented actors who would be difficult to list without omitting some of those who have undoubtedly contributed enormously to the success of his stagings. On the other hand, among his most frequent collaborators behind the scenes, it is impossible not to mention Ernesto Padilla, Irene Olivera, Leiter Padilla, Gabriel Cutiño, Asela Torres, designers Pedro Balmaseda and Jorge Noa, and on not a few occasions the composer Mike Porcel. He worked with countless classical and contemporary authors, among whom Piñera stands out, whose plays he brought to the stage on eight occasions, and Abel González Melo, who became a "playwright in residence" during recent years. As chief assistants in his effort to carry out the Festival, he counted on the closest members of his family, with Verónica and Gastón in the front line, as well as the author of these lines, who has been in charge of the Educational Component since 1994. The festival, in this new stage that begins, could not have been left in better hands than those of Melissa Messulam and Néher Jacqueline Briceño, close collaborators and colleagues, whom Mario Ernesto designated as successors at the head of the institutions that were part of his multiple legacy.</p>'),
        ('<p>No hay duda de que su partida deja un vacío enorme que será casi imposible de superar, abandonándonos antes de llegar a la codiciada fecha de los cuarenta que cumplirá el festival el año entrante. En su memoria, aun en los difíciles momentos en que vivimos, se hará lo imposible por continuar su inmensa labor en nombre también de nuestra tradición, valores y patrimonio cultural que, como él indicaba, nos hace la vida más llevadera.</p>',
         '<p>There is no doubt that his departure leaves a huge void that will be almost impossible to overcome, leaving us before reaching the coveted date of the fortieth anniversary that the festival will celebrate next year. In his memory, even in the difficult times in which we live, the impossible will be done to continue his immense work also in the name of our tradition, values, and cultural heritage which, as he indicated, makes life more bearable.</p>'),
        # Awards section
        ('<h2>Premios</h2>', '<h2>Awards</h2>'),
        ('Premio Regional de las Artes &mdash; Olimpiadas Culturales del Comité Olímpico', 'Regional Arts Award &mdash; Olympic Committee Cultural Olympiad'),
        ('Premio Ollantay', 'Ollantay Award'),
        ('Premio Federico García Lorca', 'Federico García Lorca Award'),
        ('Premio Kusillo', 'Kusillo Award'),
        ('FIT de Cádiz &mdash; Atahualpa del Cioppo', 'FIT of Cádiz &mdash; Atahualpa del Cioppo'),
        ('Premio Baco', 'Baco Award'),
        ('Premio UCSUR', 'UCSUR Award'),
    ],
    "agenda.html": [
        # Hero
        ('<h1>PROGRAMA</h1>', '<h1>PROGRAM</h1>'),
        # Descriptions
        ('Una adolescente agrede a sus compañeros con violencia y abre la puerta de un pasado que revela vínculos secretos que cambiarán sus destinos.',
         'A teenager attacks her classmates with violence and opens the door to a past that reveals secret bonds that will change their destinies.'),
        ('El cadáver de un militar desaparece tras un desentierro clandestino y un secuestro. El muerto se presenta y exige justicia.',
         'The corpse of a military officer disappears after a clandestine exhumation and a kidnapping. The deceased appears and demands justice.'),
        ('Dos actores se enfrentan al reto de interpretar a Ricardo III y entregan un espacio clave para reflexionar sobre los límites de la ambición humana.',
         'Two actors face the challenge of playing Richard III and offer a key space to reflect on the limits of human ambition.'),
        ('En un verso lleno de sátira, juego de palabras y metateatralidad, un personaje obsesionado deja expuesto el narcisismo en la actualidad.',
         'In a verse filled with satire, wordplay, and metatheatre, an obsessed character exposes contemporary narcissism.'),
        ('Una experiencia sensorial inmersiva que despierta los sentidos a través del sonido, el olfato, el gusto y el tacto en completa oscuridad.',
         'An immersive sensory experience that awakens the senses through sound, smell, taste, and touch in complete darkness.'),
        ('Artistas se juntan en el bosque a ensayar una obra y seres mágicos juegan con sus emociones en un torbellino lleno de humor, música y poesía.',
         'Artists gather in the forest to rehearse a play, and magical beings play with their emotions in a whirlwind full of humor, music, and poetry.'),
        ('El joven Robinson decide embarcarse en un viaje en busca de aventuras. Tras naufragar llega a una isla desierta con personajes inolvidables.',
         'Young Robinson decides to embark on a journey in search of adventure. After shipwrecking, he arrives on a deserted island with unforgettable characters.'),
        ('Entre Shakespeare y la vida de actores con síndrome de Down, surge un poderoso Hamlet y el resultado es un espectáculo reflexivo e inquietante.',
         'Between Shakespeare and the lives of actors with Down syndrome, a powerful Hamlet emerges, resulting in a reflective and disturbing show.')
    ],
    "calendario.html": [
        ('Month-title">SEPTIEMBRE', 'Month-title">SEPTEMBER'),
        ('weekday-header">Lunes</div>', 'weekday-header">Monday</div>'),
        ('weekday-header">Martes</div>', 'weekday-header">Tuesday</div>'),
        ('weekday-header">Miércoles</div>', 'weekday-header">Wednesday</div>'),
        ('weekday-header">Jueves</div>', 'weekday-header">Thursday</div>'),
        ('weekday-header">Viernes</div>', 'weekday-header">Friday</div>'),
        ('weekday-header">Sábado</div>', 'weekday-header">Saturday</div>'),
        ('weekday-header">Domingo</div>', 'weekday-header">Sunday</div>'),
        ('<h1>CALENDARIO</h1>', '<h1>CALENDAR</h1>'),
    ],
    "eventos-adicionales.html": [
        ('<h1>Eventos Adicionales</h1>', '<h1>Additional Events</h1>'),
        ('<h2>Componente Educativo <span class="subtitle">Foros</span></h2>', '<h2>Educational Component <span class="subtitle">Forums</span></h2>'),
        ('<span class="dir-by">Dirigido por</span>', '<span class="dir-by">Directed by</span>'),
        ('<p>Directora del Programa Educativo</p>', '<p>Educational Program Director</p>'),
        ('<th>Fecha</th>', '<th>Date</th>'),
        ('<th>Obra</th>', '<th>Play</th>'),
        ('<th>Teatro</th>', '<th>Theater</th>'),
        ('<strong>Jue.</strong>', '<strong>Thu.</strong>'),
        ('<strong>Vier.</strong>', '<strong>Fri.</strong>'),
        ('<strong>Sab.</strong>', '<strong>Sat.</strong>'),
        ('<h2>Premio a una Vida de Dedicación a las Artes Escénicas 2025</h2>', '<h2>Lifetime Dedication to the Performing Arts Award 2025</h2>'),
        ('<p><strong>Olga Garay-English</strong> ha sido consultora internacional de arte desde 2014.',
         '<p><strong>Olga Garay-English</strong> has been an international arts consultant since 2014.'),
        ('Es codirectora de la Iniciativa Nacional de Teatro Latinx (NLTI), una iniciativa de la Compañía de Teatro Latino con sede en Los Ángeles. NLTI ofrece subvenciones plurianuales de Apoyo Operativo General y oportunidades de desarrollo profesional a 52 teatros y conjuntos teatrales latinos en Estados Unidos y Puerto Rico. Con el apoyo de fundaciones nacionales y locales como Mellon, Ford, Duke, Rockefeller Brothers y Joyce, entre otras, en los últimos dos años se han otorgado casi 6,4 millones de dólares. Olga es Asesora Principal de Asuntos Internacionales de la Fundación Teatro a Mil de Chile.</p>',
         'She is co-director of the National Latinx Theater Initiative (NLTI), an initiative of the Los Angeles-based Latino Theater Company. NLTI offers multi-year General Operating Support grants and professional development opportunities to 52 Latinx theaters and theatrical ensembles in the United States and Puerto Rico. Supported by national and local foundations such as Mellon, Ford, Duke, Rockefeller Brothers, and Joyce, among others, nearly $6.4 million has been awarded over the past two years. Olga is Senior Advisor for International Affairs for Chile\'s Fundación Teatro a Mil.</p>'),
        ('<p>Fue Directora Ejecutiva del Departamento de Asuntos Culturales de Los Ángeles (2008-2014), reportando al alcalde Antonio Villaraigosa. Durante su estancia en el DCA, recaudó más de 23 millones de dólares de fuentes de financiación privadas y públicas, lo que equivale a casi 32 millones de dólares en 2025.</p>',
         '<p>She was Executive Director of the Los Angeles Department of Cultural Affairs (2008-2014), reporting to Mayor Antonio Villaraigosa. During her tenure at the DCA, she raised more than $23 million from private and public funding sources, equivalent to nearly $32 million in 2025.</p>'),
        ('<p>Olga fue Directora Fundadora del Programa de Artes de la Fundación Doris Duke (1998-2005), otorgando 145 millones de dólares en subvenciones a organizaciones nacionales e internacionales de artes escénicas, lo que equivale a 236.901.639 dólares en 2025.</p>',
         '<p>Olga was the Founding Director of the Arts Program at the Doris Duke Charitable Foundation (1998-2005), awarding $145 million in grants to national and international performing arts organizations, equivalent to $236,901,639 in 2025.</p>'),
        ('<p>En 1985, Olga colaboró con el difunto Mario Ernesto Sánchez, Director Artístico de Producción de Teatro Avante, para fundar el galardonado Festival Internacional de Teatro Hispano. El Festival presenta obras de dramaturgos y conjuntos hispanos de todo Estados Unidos y el mundo.</p>',
         '<p>In 1985, Olga collaborated with the late Mario Ernesto Sánchez, Producing Artistic Director of Teatro Avante, to found the award-winning International Hispanic Theatre Festival. The Festival presents works by Hispanic playwrights and ensembles from across the United States and the world.</p>'),
        ('<p>Olga financia tres programas de residencias artísticas: los Premios Dr. Kerry English Artists en la Conferencia de Dramaturgos de Ojai, una iniciativa de diez años que comenzó en 2021. Hasta la fecha, cinco dramaturgos han recibido el premio.</p>',
         '<p>Olga funds three artistic residency programs: the Dr. Kerry English Artists Awards at the Ojai Playwrights Conference, a ten-year initiative that began in 2021. To date, five playwrights have received the award.</p>'),
        ('<p>Desde 2021, el Fondo Internacional de Arte Dr. Kerry English del Watermill Center, un reconocido espacio artístico internacional en Long Island, Nueva York, fundado por el aclamado artista Robert Wilson, ha apoyado a artistas chilenos mediante residencias de tres semanas.</p>',
         '<p>Since 2021, the Dr. Kerry English International Art Fund at the Watermill Center—a renowned international art space on Long Island, New York, founded by acclaimed artist Robert Wilson—has supported Chilean artists through three-week residencies.</p>'),
        ('<p>Recientemente, se lanzó el Premio de Residencia Olga Garay-English y Dr. Kerry English. Se trata de una nueva iniciativa trienal que apoya a artistas latinoamericanos y latinxs en el Atelier Samuel Beckett, un programa franco-irlandés de residencias artísticas con sede en Méricourt, Francia.',
         '<p>Recently, the Olga Garay-English and Dr. Kerry English Residency Award was launched. This is a new triennial initiative supporting Latin American and Latinx artists at the Atelier Samuel Beckett, a French-Irish artist residency program based in Méricourt, France.'),
        ('El Atelier fue fundado por Judy Hegarty Lovett y Conor Lovett, directores artísticos de Gare St. Lazare Ireland, reconocidos mundialmente por sus interpretaciones de la obra de Samuel Beckett. Forma parte del Comité Directivo de International Presenting Commons y es Embajadora Creativa del Festival Under the Radar, con sede en Nueva York, cuya creación contribuyó a realizar en 2005. Forma parte de las juntas directivas de la Sociedad Internacional de Artes Escénicas (ISPA), la Organización Regional de Artes South Arts y la Conferencia de Dramaturgos de Ojai, entre otras. Fue nombrada Caballero de la Orden de las Artes y las Letras en 2012. En 2013, recibió el Premio LA Weekly de Teatro al Logro Especial, la Reina de los Ángeles, por su destacado apoyo al sector teatral de Los Ángeles y como cofundadora del Festival Internacional de Teatro RADAR L.A. También recibió el Premio Bessie de los Premios de Danza y Actuación de Nueva York por su sostenida contribución al sector en 2006.</p>',
         'The Atelier was founded by Judy Hegarty Lovett and Conor Lovett, artistic directors of Gare St. Lazare Ireland, globally recognized for their interpretations of Samuel Beckett\'s work. She serves on the Steering Committee of the International Presenting Commons and is a Creative Ambassador for the New York-based Under the Radar Festival, which she helped create in 2005. She serves on the boards of the International Society for the Performing Arts (ISPA), the South Arts Regional Arts Organization, and the Ojai Playwrights Conference, among others. She was named Chevalier of the Order of Arts and Letters in 2012. In 2013, she received the LA Weekly Theater Special Achievement Award, the Queen of the Angels, for her outstanding support of the Los Angeles theater sector and as co-founder of the RADAR L.A. International Theater Festival. She also received a Bessie Award from the New York Dance and Performance Awards for her sustained contribution to the sector in 2006.</p>'),
        ('<p>Nació en Santa Clara, Cuba, y estuvo casada con el difunto Dr. Kerry English, exdirector del Centro Pediátrico Dr. Martin Luther King, Jr. en Watts.</p>',
         '<p>She was born in Santa Clara, Cuba, and was married to the late Dr. Kerry English, former director of the Dr. Martin Luther King, Jr. Pediatric Center in Watts.</p>'),
    ],
    "dia-internacional-del-nino.html": [
        ('<h1>Día Internacional del Niño</h1>', '<h1>International Children\'s Day</h1>'),
        ('<div class="card-header">Septiembre</div>', '<div class="card-header">September</div>'),
        ('<div class="card-weekday">Viernes</div>', '<div class="card-weekday">Friday</div>'),
        ('<div class="card-weekday">Sábado</div>', '<div class="card-weekday">Saturday</div>'),
        ('Creada por <strong>Víctor Hugo Cortés</strong>', 'Created by <strong>Víctor Hugo Cortés</strong>'),
        ('Dirección: <strong>Luciano Cortes</strong>', 'Direction: <strong>Luciano Cortes</strong>'),
        ('Elenco: <strong>Juan Bautista, Cote Composto</strong>', 'Cast: <strong>Juan Bautista, Cote Composto</strong>'),
        ('Elenco: Juan Bautista, Cote Composto', 'Cast: Juan Bautista, Cote Composto'),
        ('<span class="mockup-activity-desc">Pintura facial, personaje en zancos, y distribución de meriendas</span>',
         '<span class="mockup-activity-desc">Face painting, stilt walker, and distribution of snacks</span>'),
        ('<span class="mockup-activity-desc">Juegos de Feria</span>', '<span class="mockup-activity-desc">Fair Games</span>'),
        ('<span class="mockup-activity-desc">Talleres: Pintura, Títeres, Danza y Percusión</span>',
         '<span class="mockup-activity-desc">Workshops: Painting, Puppets, Dance and Percussion</span>'),
        ('<span class="mockup-activity-desc">Espectáculo: <strong>Las asombrosas aventuras de Robinson Crusoe</strong></span>',
         '<span class="mockup-activity-desc">Show: <strong>Las asombrosas aventuras de Robinson Crusoe</strong></span>'),
        ('<div class="free-tag">Entrada y estacionamiento gratis</div>', '<div class="free-tag">Free admission and parking</div>'),
        # Robinson Crusoe detailed desc
        ('<p>Las Asombrosas Aventuras de Robinson Crusoe narra la historia de un joven audaz (Robinson) que decide embarcarse en un viaje sin destino en busca de aventuras. Tras naufragar el barco donde navegaba llega a una isla desierta en donde conoce personajes inolvidables que cambiarán su destino. Con creatividad y optimismo, Robinson se las ingeniará para abastecerse de todo lo necesario para subsistir y aprenderá el valor de la amistad y la compañía, mientras busca la manera de volver a su hogar.</p>',
         '<p>The Amazing Adventures of Robinson Crusoe tells the story of a daring young man (Robinson) who decides to embark on a destination-less journey in search of adventure. After his ship shipwrecks, he arrives on a deserted island where he meets unforgettable characters who will change his destiny. With creativity and optimism, Robinson will manage to supply himself with everything necessary to survive and will learn the value of friendship and companionship, while looking for a way to return home.</p>'),
        ('<p>Durante las aventuras se tocan temas como la creatividad, el ingenio, la amistad y la toma de decisiones que nos llevan a avanzar y aventurarnos en una vida activa. Resalta además con el poder vital de la imaginación, conecta a todo el público con la fantasía y el sentido de aventura, con el juego como metodología y con el poder vital de la imaginación.</p>',
         '<p>During the adventures, themes such as creativity, ingenuity, friendship, and decision-making are touched upon, leading us to move forward and venture into an active life. It also highlights the vital power of imagination, connecting the entire audience with fantasy and a sense of adventure, with play as a methodology and with the vital power of imagination.</p>'),
    ],
    "teatros.html": [
        ('<h1>TEATROS</h1>', '<h1>THEATERS</h1>'),
        ('<p>Entradas: <strong>$30.00</strong></p>', '<p>Tickets: <strong>$30.00</strong></p>'),
        ('<p>Personas mayores de 65 años, estudiantes y<br>personas especiales: <strong>$25.00</strong></p>',
         '<p>Seniors over 65, students, and guests<br>with disabilities: <strong>$25.00</strong></p>'),
        ('<p>Personas mayores de 65 años, estudiantes y<br>personas especiales: <strong>$25.00</strong><br>(No',
         '<p>Seniors over 65, students, and guests<br>with disabilities: <strong>$25.00</strong><br>(Does not'),
        ('incluye 17% handling fee)</p>', 'include 17% handling fee)</p>'),
        ('<p>Personas mayores de 65 años, estudiantes<br>y personas especiales: <strong>$25.00</strong></p>',
         '<p>Seniors over 65, students,<br>and guests with disabilities: <strong>$25.00</strong></p>'),
        ('<p><strong>Estacionamiento gratis</strong></p>', '<p><strong>Free parking</strong></p>'),
        ('<p><strong>Estacionamiento valet gratis</strong></p>', '<p><strong>Free valet parking</strong></p>'),
        ('<p><strong>Estacionamiento: www.arshtcenter.org/parking<br>305.949.6722.</strong></p>',
         '<p><strong>Parking: www.arshtcenter.org/parking<br>305.949.6722.</strong></p>'),
    ],
    "sponsors.html": [
        ('<h1>Apoya IHTF</h1>', '<h1>Support IHTF</h1>'),
        ('<h3>Amigo del Festival</h3>', '<h3>Friend of the Festival</h3>'),
        ('<div class="price">Todos los aportes son bienvenidos</div>', '<div class="price">All contributions are welcome</div>'),
        ('<li>Mención en el programa</li>', '<li>Mention in the playbill</li>'),
        ('<h3>Actor</h3>', '<h3>Actor</h3>'),
        ('<li>Mención en el programa y reconocimiento digital</li>', '<li>Mention in the playbill and digital recognition</li>'),
        ('<li>4 entradas para funciones por festival</li>', '<li>4 tickets for performances per festival</li>'),
        ('<h3>Dramaturgo</h3>', '<h3>Playwright</h3>'),
        ('<li>Reconocimiento con nombre y logo en el sitio web y en el programa</li>', '<li>Recognition with name and logo on the website and in the playbill</li>'),
        ('<li>6 entradas para funciones por festival</li>', '<li>6 tickets for performances per festival</li>'),
        ('<h3>Director</h3>', '<h3>Director</h3>'),
        ('<li>Reconocimiento destacado en el sitio web y en el programa</li>', '<li>Prominent recognition on the website and in the playbill</li>'),
        ('<li>Reconocimiento en redes sociales</li>', '<li>Social media recognition</li>'),
        ('<li>10 entradas para funciones con asientos reservados</li>', '<li>10 tickets for performances with reserved seating</li>'),
        ('<h3>Productor</h3>', '<h3>Producer</h3>'),
        ('<li>Anuncio publicitario en el programa del festival</li>', '<li>Advertisement in the festival playbill</li>'),
        ('<li>20 entradas para funciones con asientos reservados</li>', '<li>20 tickets for performances with reserved seating</li>'),
        ("alert('Gracias por su interés en donar');", "alert('Thank you for your interest in donating');"),
        ('Donar</a>', 'Donate</a>')
    ],
    "contactanos.html": [
        ('<h1>Contáctanos</h1>', '<h1>Contact Us</h1>'),
        ('<h2>Contáctanos</h2>', '<h2>Contact Us</h2>'),
        ('<h3>Consultas de Medios</h3>', '<h3>Media Inquiries</h3>'),
        ('<h3>Consultas Generales</h3>', '<h3>General Inquiries</h3>'),
        ('<input type="text" placeholder="Nombre*" aria-label="Nombre" required />', '<input type="text" placeholder="Name*" aria-label="Name" required />'),
        ('<input type="email" placeholder="Email *" aria-label="Email" required />', '<input type="email" placeholder="Email *" aria-label="Email" required />'),
        ('<input type="text" placeholder="Asunto" aria-label="Asunto" />', '<input type="text" placeholder="Subject" aria-label="Subject" />'),
        ('<textarea placeholder="Mensaje" aria-label="Mensaje"></textarea>', '<textarea placeholder="Message" aria-label="Message"></textarea>'),
        ('alert(\'Mensaje enviado exitosamente\');', 'alert(\'Message sent successfully\');'),
        ('Enviar</button>', 'Submit</button>')
    ],
}

# The play details files update logic
play_detail_replacements = [
    # Label updates
    ('<strong>Autor:</strong>', '<strong>Author:</strong>'),
    ('<strong>Director:</strong>', '<strong>Director:</strong>'),
    ('<strong>Elenco:</strong>', '<strong>Cast:</strong>'),
    ('Comprar entradas</a>', 'Buy tickets</a>'),
    # JavaScript changes for dynamic data rendering
    (
        'document.getElementById("play-country").textContent = play.country;',
        'document.getElementById("play-country").textContent = play.country_en || play.country;'
    ),
    (
        'document.getElementById("play-author").textContent = play.author;',
        'document.getElementById("play-author").textContent = play.author_en || play.author;'
    ),
    (
        'document.getElementById("play-director").textContent = play.director;',
        'document.getElementById("play-director").textContent = play.director_en || play.director;'
    ),
    (
        'document.getElementById("play-cast").textContent = play.cast;',
        'document.getElementById("play-cast").textContent = play.cast_en || play.cast;'
    ),
    (
        'const sentences = play.description.split(". ");',
        'const sentences = (play.description_en || play.description).split(". ");'
    )
]

# We will apply translations to all files in `/en/`
all_files = [
    "index.html",
    "agenda.html",
    "calendario.html",
    "contactanos.html",
    "dia-internacional-del-nino.html",
    "eventos-adicionales.html",
    "nosotros.html",
    "sponsors.html",
    "teatros.html",
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

for filename in all_files:
    filepath = os.path.join(en_dir, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Apply common replacements (header, footer, common badges)
    for orig, trans in common_replacements:
        content = content.replace(orig, trans)
    
    # 2. Apply page-specific replacements
    if filename in file_specific_replacements:
        for orig, trans in file_specific_replacements[filename]:
            content = content.replace(orig, trans)
            
    # 3. Apply play detail modifications if it is a play page
    if filename == "obra.html" or filename.startswith("obra-"):
        for orig, trans in play_detail_replacements:
            content = content.replace(orig, trans)
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Translated en/{filename}")
