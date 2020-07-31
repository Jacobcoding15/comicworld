def get_info(character):
    if character == "Batman":
        return["In the name of his murdered parents, Bruce Wayne wages eternal war on the criminals of Gotham City. He is vengeance. He is the night. He is Batman. One of the most iconic fictional characters in the world, Batman has dedicated his life to an endless crusade, a war on all criminals in the name of his murdered parents, who were taken from him when he was just a child. Since that tragic night, he has trained his body and mind to near physical perfection to be a self-made Super Hero. He's developed an arsenal of technology that would put most armies to shame. And he's assembled teams of his fellow DC Super Heroes, like the Justice League, the Outsiders and Batman, Incorporated. A playboy billionaire by day, Bruce Wayne’s double life affords him the comfort of a life without financial worry, a loyal butler-turned-guardian and the perfect base of operations in the ancient network of caves beneath his family’s sprawling estate. By night, however, he sheds all pretense, dons his iconic scalloped cape and pointed cowl and takes to the shadowy streets, skies and rooftops of Gotham City.","https://img.cinemablend.com/quill/8/9/a/5/4/c/89a54c7894a598494ab9426d1767c445e972d2e2.jpg"]
    elif character == "Superman":
        return["The powers of the DC Comics character Superman have changed a great deal since his introduction in the 1930s. As the character developed, his abilities were enhanced in order to maintain the interest of his audience. The extent of his powers peaked during the 1960s and - albeit to a lesser extent - the 1970s and 1980s, to the point where it became difficult to create suitable challenges for the character. As a result, his powers were significantly reduced when his story was rebooted by writer John Byrne after the Crisis on Infinite Earths series. After Byrne's departure, Superman's powers were gradually increased again, although he still remains weaker than his Pre-Crisis incarnation.", "https://i.pinimg.com/originals/5b/ae/0d/5bae0dfc3f41be1f9d23ef1466721101.jpg"]
    elif character == "Spiderman":
        return["In Spider-Man's first story, in Marvel Comics' Amazing Fantasy, no. 15 (1962), American teenager Peter Parker, a poor sickly orphan, is bitten by a radioactive spider. As a result of the bite, he gains superhuman strength, speed, and agility along with the ability to cling to walls.Spider-Man has spider-like abilities including superhuman strength and the ability to cling to most surfaces. He is also extremely agile and has amazing reflexes. Spider-Man also has a “spider sense,” that warns him of impending danger. Spider-Man has supplemented his powers with technology.", "https://bleedingcool.com/wp-content/uploads/2017/12/Amazing-Spider-Man-792-Featured-Image.jpg"]
    elif character == "Thor":
        return ["He's the Norse God of Thunder. He was a religious figure back in the days when the Roman Empire was a thing. ... Blake flees into a cave, finds a walking stick, strikes it against a rock… and is suddenly transformed into Thor, the God of Thunder.", "https://i.pinimg.com/originals/0e/94/b2/0e94b29964e8b8b1cac544851efa9f97.jpg"]
    elif character == "Ironman":
        return ["Young Tony Stark was a prodigy of mechanical engineering genius. ... Tony escaped with James Rhodes (now War Machine) and returned to America to become a part of the Avengers, taking his fathers teachings of giving back to the world to heart and using his new armor to aid mankind.", "https://img1.looper.com/img/gallery/the-real-reason-marvel-decided-not-to-make-iron-man-4/intro-1575053226.jpg"]
    elif character == "Captain America":
        return [ "Captain America is the alter ego of Steve Rogers, a frail young man enhanced to the peak of human perfection by an experimental serum to aid the United States government's efforts in World War II. Near the end of the war, he was trapped in ice and survived in suspended animation until he was revived in modern times.", "https://live.staticflickr.com/7134/7731258764_bb9b6e5b9f_b.jpg"]
    elif character == "Hulk":
        return ["Dr. Bruce Banner lives a life caught between the soft-spoken scientist he's always been and the uncontrollable green monster powered by his rage. Exposed to heavy doses of gamma radiation, scientist Bruce Banner transforms into the mean, green rage machine called the Hulk.", "https://www.insidesimplefinance.com/wp-content/uploads/2020/02/Hulk.jpg"]
    elif character == "Flash":
        return ["Barry Allen's origin is that he was struck by a bolt of lightning that connected him with a mysterious source of power he dubbed the “Speed Force.” Originally created by Harry Lampert and Gardner Fox in Flash Comics #1 in 1940, “The Flash” wasn't Barry Allen when he first appeared.", "https://static1.srcdn.com/wordpress/wp-content/uploads/2020/01/The-Flash-Comic-Year-One-Cover-Art.jpg"]
    elif character == "Wonder Woman":
        return ["Wonder Woman tells the tale of Princess Diana of Themyscira. Her original origin story says she was formed out of clay by her mother, Hippolyta, and had life bestowed upon her by the Greek gods — making her the only Amazon not conceived by a man.", "https://static0.cbrimages.com/wordpress/wp-content/uploads/2020/07/Wonder-Woman-759-Jim-Lee-variant-cover-header.jpg"]
    elif character == "Green Lantern":
        return ["Green Lantern was Hal Jordan, a test pilot who was given a power ring by a dying alien, Abin Sur, and who became a member of the Green Lantern Corps, an interstellar organization of police overseen by the Guardians of the Universe.", "https://cdn1.thr.com/sites/default/files/2018/07/the_green_lantern_-_publicity_-_h_2018.jpg"]
    elif character == "Wolverine":
        return ["Wolverine was born as James Howlett in northern Alberta, Canada, (approximately near Cold Lake) during the late 1880s, purportedly to rich farm owners John and Elizabeth Howlett, though he is actually the illegitimate son of the Howletts' groundskeeper, Thomas Logan.", "https://img.cinemablend.com/filter:scale/quill/a/e/e/4/2/9/aee4298bb4dab330e4043780e66a0801032e1f7a.jpg?mw=600"]
    elif character == "Silver Surfer":
        return ["The Silver Surfer is a humanoid alien with metallic skin who can travel through space with the aid of his surfboard-like craft. Originally a young astronomer named Norrin Radd on the planet Zenn-La, he saved his homeworld from the planet devourer, Galactus, by serving as his herald.", "https://i1.wp.com/twinfinite.net/wp-content/uploads/2019/07/silver-surfer.jpg?fit=1000%2C563&ssl=1"]
    elif character == "Catwoman":
        return ["Catwoman, then called the Cat, first appeared in Batman #1 (Spring 1940) as a mysterious burglar and jewel thief, revealed at the end of the story to be a young, attractive (unnamed) woman, having disguised herself as an old woman during the story and been hired to commit a burglary.", "https://static3.cbrimages.com/wordpress/wp-content/uploads/2020/03/catwoman-80-jim-lee-3-1.jpg"]
    elif character == "Doctor Strange":
        return ["Strange's backstory was first told in Strange Tales #115. At first, he was a talented surgeon with an asshole streak, winning fame and fortune through his work. But a car crash crippled his hands, ruining his career. He spent years looking for a miracle treatment that would fix him, and eventually wound up in Tibet.", "https://geekandsundry.com/wp-content/uploads/2015/06/doctor-strange-2-e1433201423430-970x545.jpg"]
    elif character == "Professor X":
        return ["Charles Xavier, better known as Professor X, is one of the most important figures in the Marvel Universe. First appearing in 1963's X-Men #1, Xavier is a mutant and the world's most powerful telepath. He dreams of a world where mutants and humans can live in peace. However, this puts him in the impossible position of combating not only the bigotry of frightened humans but the anger of mutants fighting to dominate the rest of the world. To help achieve his goals, Xavier founds his School for Gifted Youngsters, leading to the birth of the X-Men, the New Mutants, and by extension, a whole host of spinoff teams like X-Force, X-Factor, Generation X, and more.", "https://static2.cbrimages.com/wordpress/wp-content/uploads/2019/12/Professor-x-Charles-Xavier-Cerebro.jpg"]
    elif character == "Cyclops":
        return ["In Hesiod the Cyclopes were three sons of Uranus and Gaea—Arges, Brontes, and Steropes (Bright, Thunderer, Lightener)—who forged the thunderbolts of Zeus. Later authors made them the workmen of Hephaestus and said that Apollo killed them for making the thunderbolt that slew his son Asclepius.", "https://img1.looper.com/img/gallery/how-cyclops-became-the-most-hated-character-in-marvel/intro.jpg"]
    elif character == "Pheonix":
        return ["The Phoenix is a mythical bird from Ancient Greek legends. The story goes that the bird lives for several hundred years before it dies by setting itself on fire. However, it then starts a new life from the ashes of the fire. ... The Phoenix is often referred to as a fire bird, because it dies and is reborn out of fire.", "https://screenrant.com/wp-content/uploads/2017/08/Dark-Phoenix-defeated-Wolverine.jpg"]
    elif character == "Mr.Fantastic":
        return "He is the inventor of the spacecraft that was bombarded by cosmic radiation on its maiden voyage, granting the Fantastic Four their powers. Richards gained the ability to stretch his body into any shape he desires."
    elif character == "Kid Flash":
        return ["Wally West is the biological son of Rudy and Marry West. He grew up a normal kid in Central City until his aunt Iris married Barry Allen. Not long afterward Wally discovered that his uncle was non other then the hero of central city, The Flash.", "https://www.dccomics.com/sites/default/files/GalleryComics_1920x1080_20180131-v1_0007_flash_ann_1_5a73d50b57a959.37685172.jpg"]
    elif character == "Spawn":
        return ["In his early battles, Spawn faces street thugs and gangs, becoming a dark and brutal antihero, culminating in the brutal murder of a pedophile and child murderer named Billy Kincaid. ... There he meets the bum Cogliostro, who seems to know much more about Spawn than he first lets on, and becomes his mentor.", "https://media.comicbook.com/2020/02/spawn-304-1205331-1280x0.jpeg"]
    elif character == "Doctor Doom":
        return "Victor von Doom was born in a Romani camp outside Haasenstadt, Latveria. His mother, Cynthia, was killed in a bargain with Mephisto that went wrong. Despite his father's attempts to care for her, a noblewoman died and Werner von Doom fled with a young Victor on a cold winter's night."
    elif character == "Martian Manhunter":
        return "One of the last survivors of the civil war that ravaged his home planet of Mars, J'onn J'onnz traveled to Earth and now fights to protect his adoptive home. J'onn J'onzz of the planet Mars was accidentally transported to Earth, where he became one of its greatest champions under the moniker Martian Manhunter."
    elif character == "Galactus":
        return "Galactus was originally the explorer Galan of the planet Taa, which existed in the prime pre-Big Bang universe. When an unknown cosmic cataclysm gradually begins killing off all of the other life in his universe, Galan and other survivors leave Taa on a spacecraft and are engulfed in the Big Crunch."
    elif character == "Magneto":
        return "Magneto was born Max Eisenhardt sometime in the late 1920s to a middle-class German Jewish family. ... Magda and Magnus had a daughter named Anya, and lived uneventfully until an angry mob, spurred on by the first manifestation of Magnus' powers, burned down their home with Anya still inside."
    elif character == "Nightwing":
        return "The original Nightwing in DC Comics was an identity assumed by alien superhero Superman when stranded on the Kryptonian city of Kandor with his friend Jimmy Olsen. ... Meanwhile, Superman stories have seen Superman's adopted son Chris Kent and Power Girl take up the name for brief turns as Nightwing"
    elif character == "Hawkeye":
        return "The man who would become known as Hawkeye was born Clint Barton. Orphaned at an early age, he joined the circus and apprenticed himself to the Swordsman, a performer who specialized in tricks with blades. After he discovered the Swordsman stealing from the circus, the two fought, and Barton was left for dead."
    elif character == "Lex Luthor":
        return "The Modern Age Lex Luthor is a product of child abuse and early poverty. Born in the Suicide Slum district of Metropolis, he is instilled with a desire to become a self-made man. ... Upon graduating from MIT, Luthor founds his own business, LexCorp, which grows to dominate much of Metropolis."
    elif character == "Scarlet Witch":
        return "Scarlet Witch has been through some major changes in her comic book career. Wanda began her career as a mutant on the side of evil, being a member of Magneto's Brotherhood of Evil Mutants. But just over a year later in May 1965, she joined the Avengers and became a hero in Avengers #16."
    elif character == "Joker":
        return "Batman: The Killing Joke (1988) built on the Joker's 1951 origin story, portraying him as a failed comedian pressured into committing crime as the Red Hood to support his pregnant wife. ... This, combined with the trauma of his wife's earlier accidental death, causes him to go insane and become the Joker"
    elif character == "Shazam":
        return ["Shazam informs Billy that he is an ancient Egyptian wizard who has been using his powers for many centuries to fight the forces of evil, but that he is now old and not long for this world. He therefore passes along part of his power to Billy, who shouts his name – SHAZAM! – to transform into Captain Marvel/Shazam.", "https://vignette.wikia.nocookie.net/marvel_dc/images/6/61/Shazam%21_Vol_3_1_Textless_Variant.jpg/revision/latest?cb=20181205234924"]
    elif character == "Deadpool":
        return "Like Wolverine, Deadpool is (or is thought to be) Canadian. The original story had him joining the Weapon X program after being kicked out of the U.S. Army Special Forces and given an artificial healing factor based on Wolverine's thanks to Dr. Emrys Killebrew, one of the head scientists."
    elif character == "Thanos":
        return "Thanos debuted in Iron Man #55, in February of 1973. Born Dione on Saturn's moon of Titan, Thanos grew up in a peace-loving family. ... At one point, Thanos exposed himself to cosmic rays, which distorted his body. He eventually killed many of his fellow Titans, including his own mother."
    elif character == "Darkseid":
        return "Darkseid is among the most powerful beings of the DC Universe from the race known as New Gods. His main power, the Omega Beams, is a form of energy that he fires from his eyes or hands as either a concussive force or a disintegrating energy which is capable of erasing living objects and organisms from existence."
    elif character == "Beast":
        return ""
    elif character == "Punisher":
        return "Punisher- A war veteran and a United States Marine Corps Scout Sniper in Force Recon, Castle is skilled in hand-to-hand combat, guerrilla warfare, and marksmanship. The Punisher's brutal nature and willingness to kill made him an anomaly in mainstream American comic books when he debuted in 1974.The Punisher's iconic skull as a symbol of force in recent years."
    elif character == "Rogue":
        return 
    elif character == "John Constantine":
        return 
    elif character == "Green Goblin":
        return 
    elif character == "Red Hood":
        return 
    elif character == "Doctor Octopus":
        return 
    elif character == "Lois Lane":
        return 
    
      