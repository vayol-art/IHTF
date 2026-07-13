import os

data_path = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF\data.js"

with open(data_path, 'r', encoding='utf-8') as f:
    content = f.read()

translations = {
    "carrusel": {
        "country_en": "USA",
        "description_en": "It seems to be a country in recent democracy that has lived a convulsive and long period of dictatorship. Or perhaps it is the opposite, although the characters are not aware, or should not say it. In the middle of a math class, a teenager begins to attack her classmates in an unexpected and violent way. The teacher meets with the grandfather, her legal guardian, to analyze the strange behavior, which has generated notable physical damage even to the minor herself. The dialogue with a doctor will bring more uncertainties than certitudes, but it will open the door to a past that, slowly, moving between two times, will reveal secret links between these four beings and dictate their destinies."
    },
    "zombi-manifiesto": {
        "country_en": "Uruguay",
        "description_en": "Fifty years after the coup d'état in Uruguay, theater remains an arena for debate. The corpse of a military officer disappears after a clandestine exhumation and a kidnapping. An exemplary bureaucrat demands a decent burial. The deceased appears and demands justice. When memory is reversed, the bodies appear. Marx asserts that history occurs twice: first as tragedy, then as farce. Meanwhile, two young people ask themselves what is the best tool to change the world, political correctness or class consciousness? Marxist philosophy continues to shed light on an economic system that generates the living dead. 'Capital is an abstract parasite, a gigantic vampire, a maker of zombies; but the fresh flesh it converts into dead labor is ours and the zombies it generates are ourselves,' writes Mark Fisher in his book Capitalist Realism. From there are born the eleven scenes of this Zombie Manifesto, like the eleven Theses on Feuerbach that postulated that it is not enough to interpret the world in various ways, what matters is to transform it."
    },
    "historia-de-un-jabali": {
        "country_en": "Chile",
        "description_en": "Following its premiere in Chile, one of the most emblematic pieces of the Teatro a Mil International Festival 2026 comes to us. Two actors face the challenge of playing Richard III, the ruthless monarch of William Shakespeare's tragedy. They have been playing supporting roles all their lives and think they deserve this opportunity. However, they consider that the rest of the cast is not up to their level and they do not like anything the director proposes. During the construction of the character, the affinities between the actors and the English monarch begin to surface. All three are ambitious and intelligent. Like Richard III, they do not want to settle, they have a lust for power and are not willing to waste time with soft, hypersensitive, or mediocre actors. As their life stories intertwine, the relationship between the actors, the character, and the spectator becomes closer and closer, delivering a key space to reflect on the limits of human ambition, contemporary mechanisms of power, desire, and resentment. \\n\\n'A play that moves with intelligence on slippery ground: that of artistic ambition, the actor's ego, and power as an intimate and political drive. Based on the figure of Richard III, the piece does not propose an adaptation of Shakespeare, but a contemporary dissection of his most famous monster.' (Galia Bogolasky - Culturizarte)"
    },
    "a-fuego": {
        "country_en": "Spain",
        "description_en": "Erostratus, a shepherd from Ancient Greece, set fire to the Temple of Artemis at Ephesus, considered one of the seven wonders of the ancient world. After being arrested, interrogated, and tortured, he ended up confessing the true reason that had led him to commit that act: to go down in posterity. In this monologue entirely in verse, full of satire, wordplay, and metatheatre, we will see how the protagonist's fascination with the figure of Erostratus progressively becomes an obsession, to the point of making him commit a crime worthy of his infamous idol. Jumping from one character to another, the author-performer laughs at his own megalomania, inviting us to reflect on the prevailing narcissism of our time and the intrinsic human desire to leave a mark; whether through an artistic expression, a trade, a revolution, or a criminal act."
    },
    "odd-man-out": {
        "country_en": "USA",
        "description_en": "ODD MAN OUT is an immersive sensory experience that awakens your senses and your imagination. You will take a flight like no other – in complete darkness. You arrive at our airport and wait in the lounge and boarding gate of PITCHBLACK Airlines, where we prepare you for the trip. We guide you to your seat in a completely dark cabin. Once on the flight, you will experience a story through sound, smell, taste, and touch. You will even feel the weather happening inside the room. But all in complete darkness. Once you exit, we invite you to stay and enjoy the beauty, life, and hope of your new destination. The show tells the story of a blind musician whose life takes him from Buenos Aires to New York. We will follow Alberto's life as he discovers music, learns to play the guitar, travels the world, and finally leads and triumphs with his own band. He will also experience heartbreak and loss in a country torn by internal conflict. 'ODD MAN OUT' is not just about telling a story, but about creating a unique theatrical experience."
    },
    "sueno": {
        "country_en": "Argentina",
        "description_en": "A company of artists gathers in the forest to rehearse a play, without realizing that the place is plagued with magical beings ready to whimsically play with their emotions. Or is it that true desires manifest themselves freely far from impositions? To the already well-known track record of Compañía Criolla of reimagining classic texts to bring them closer to new audiences, making them vibrate in the present ('Romeo y Julieta de bolsillo', 'Cyrano de más acá', 'La comedia de los Herrores'), is added this new proposal inspired by one of Shakespeare's most magical and funniest comedies; 'A Midsummer Night's Dream'. This time, four performers will be in charge of embodying all the characters of the original play, in a true theatrical whirlwind, full of rhythm, physical deployment, poetry, music, humor, and a lot of love. Since its premiere in 2021, the piece has become a true critical and public success, performing more than three hundred functions, both inside and outside its country. It has participated in festivals around the world and received multiple awards and distinctions, including the 'Certamen Barroco' of the Classical Theater Festival of Almagro, Spain in 2024, the National Theater Festival of the INT Argentina in 2023, ATINA, ACE, and María Guerrero Awards. It is also a candidate for the MAX 2026 Awards in Spain. Thanks to its multiple layers of interpretation, and an agile and youthful gaze, some institutions, such as the 'School of Spectators of Buenos Aires', catalog it as the ideal entry door for those who are interested in universal classics for the first time, as well as for theater lovers and seasoned spectators. An invitation to theatrical play, to cathartic laughter, and to live classic theater as if it were written today, for us. A true celebration of the ritual that continues to summon and move us."
    },
    "robinson-crusoe": {
        "country_en": "USA",
        "description_en": "The Amazing Adventures of Robinson Crusoe tells the story of a daring young man (Robinson) who decides to embark on a destination-less journey in search of adventure. After his ship shipwrecks, he arrives on a deserted island where he meets unforgettable characters who will change his destiny. With creativity and optimism, Robinson will manage to supply himself with everything necessary to survive and will learn the value of friendship and companionship, while looking for a way to return home. \\n\\nDuring the adventures, themes such as creativity, ingenuity, friendship, and decision-making are touched upon, leading us to move forward and venture into an active life. It also highlights the vital power of imagination, connecting the entire audience with fantasy and a sense of adventure, with play as a methodology and with the vital power of imagination."
    },
    "hamlet": {
        "country_en": "Peru",
        "description_en": "The 'Hamlet' of Teatro de La plaza has been touring Europe, Latin America, and the United States, harvesting awards, doubling international tours, and leaving thousands of spectators with a different way of looking at human beings. A group of people with Down syndrome takes the stage to share their desires and frustrations through a free version of Hamlet. The play is a weave between Shakespeare's text and the lives of the actors, and takes as its starting point the question he asks us in front of existence: To be or not to be? What does it mean to be for people who do not find spaces where they are taken into account?\\n\\n'Inclusive theater and disabled actors change society's gaze' (EFE - Madrid)\\n'Another Hamlet is possible: disabled actors tear down prejudices and triumph in the theater listings.' (Raquel Vidales, EL PAÍS.)"
    }
}

for play_id, fields in translations.items():
    # We find the block for the play, e.g. "id": "carrusel", or similar
    # And we insert "country_en" and "description_en" within its definition
    play_marker = f'"id": "{play_id}"'
    if play_marker in content:
        # Find where this play block starts (just before the marker)
        # Find the "country" key of this block
        country_marker = f'"country":'
        # We can find the country marker after the play_marker
        idx = content.find(play_marker)
        c_idx = content.find(country_marker, idx)
        
        # We insert the country_en key
        c_line_end = content.find('\n', c_idx)
        content = content[:c_line_end] + f'\n    "country_en": "{fields["country_en"]}",' + content[c_line_end:]
        
        # Find the "description" key of this block
        desc_marker = f'"description":'
        d_idx = content.find(desc_marker, idx)
        d_line_end = content.find('\n', d_idx)
        # Escape quotes for description_en
        escaped_desc = fields["description_en"].replace('"', '\\"')
        content = content[:d_line_end] + f'\n    "description_en": "{escaped_desc}",' + content[d_line_end:]
        print(f"Added English fields for {play_id}")
    else:
        print(f"Play marker not found: {play_id}")

with open(data_path, 'w', encoding='utf-8') as f:
    f.write(content)
