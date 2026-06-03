from bot.domain.entities import Author

AUTHORS: dict[str, Author] = {
    "pushkin": Author(
        id="pushkin",
        name="Alexander Pushkin",
        life_years="1799–1837",
        period_id="golden_age",
        who_they_were="Poet, playwright, novelist — the founder of modern Russian literature.",
        why_they_matter=(
            "Pushkin created the modern Russian literary language and established national "
            "literature on a European level. His works defined Russian cultural identity."
        ),
        historical_context=(
            "Born into a noble family, Pushkin lived through the Patriotic War of 1812 and the "
            "Decembrist revolt. He was exiled for his politically charged poetry and died in a duel "
            "at age 37."
        ),
        main_works=[
            "Eugene Onegin",
            "The Captain's Daughter",
            "Boris Godunov",
            "The Bronze Horseman",
            "Ruslan and Lyudmila",
        ],
        main_achievement="Creation of the modern Russian literary language and the Russian novel in verse.",
        interesting_fact=(
            "Pushkin's maternal great-grandfather was Abram Petrovich Gannibal, an African man "
            "who became a general in the Russian army — Pushkin wrote an unfinished novel about him."
        ),
        mini_question="Which Pushkin work is called 'an encyclopedia of Russian life'?",
        mini_answer="Eugene Onegin — Belinsky called it that because it captured all aspects of Russian society.",
        map_places=["moscow", "saint_petersburg"],
    ),
    "lermontov": Author(
        id="lermontov",
        name="Mikhail Lermontov",
        life_years="1814–1841",
        period_id="golden_age",
        who_they_were="Poet, novelist, playwright — Pushkin's successor and a master of psychological lyric.",
        why_they_matter=(
            "Lermontov deepened Russian Romanticism and created the archetype of the rebellious, "
            "disillusioned hero in 'A Hero of Our Time.'"
        ),
        historical_context=(
            "Lermontov's career was defined by political exile to the Caucasus. "
            "His poem 'Death of a Poet,' written after Pushkin's death, was seen as a political act."
        ),
        main_works=[
            "A Hero of Our Time",
            "Mtsyri",
            "The Demon",
            "Death of a Poet",
            "Borodino",
        ],
        main_achievement="Creation of the first Russian psychological novel — 'A Hero of Our Time.'",
        interesting_fact="Like Pushkin, Lermontov died in a duel — at age 26, at the foot of Mashuk mountain.",
        mini_question="What literary type did Lermontov create in 'A Hero of Our Time'?",
        mini_answer="Pechorin — a 'superfluous man' and the first psychologically complex hero in Russian prose.",
        map_places=["tarkhany"],
    ),
    "gogol": Author(
        id="gogol",
        name="Nikolai Gogol",
        life_years="1809–1852",
        period_id="golden_age",
        who_they_were="Prose writer, playwright, satirist — the founder of Russian realistic prose.",
        why_they_matter=(
            "Gogol showed that Russian prose could combine social satire, grotesque, and deep "
            "philosophical meaning. His work directly influenced Dostoevsky and all subsequent realists."
        ),
        historical_context=(
            "Gogol moved from Ukraine to Saint Petersburg, experiencing the contrast between provincial "
            "life and the imperial capital. He burned the second part of 'Dead Souls' shortly before his death."
        ),
        main_works=[
            "Dead Souls",
            "The Overcoat",
            "The Government Inspector",
            "Evenings on a Farm Near Dikanka",
            "The Nose",
        ],
        main_achievement="Creation of Russian social prose and the 'overcoat' tradition in literature.",
        interesting_fact=(
            "Gogol starved himself to death in a religious frenzy, having burned the manuscript "
            "of 'Dead Souls' volume two just days before."
        ),
        mini_question="What phrase became proverbial thanks to Gogol's 'The Overcoat'?",
        mini_answer="'We all came out from under Gogol's overcoat' — Dostoevsky's remark about Gogol's influence.",
        map_places=["saint_petersburg"],
    ),
    "griboyedov": Author(
        id="griboyedov",
        name="Alexander Griboyedov",
        life_years="1795–1829",
        period_id="golden_age",
        who_they_were="Diplomat, playwright, composer — author of the most quoted Russian comedy.",
        why_they_matter=(
            "Griboyedov's 'Woe from Wit' became a cultural phenomenon: dozens of its phrases entered "
            "the Russian language as proverbs."
        ),
        historical_context=(
            "A diplomat in Persia, Griboyedov was killed during an attack on the Russian embassy in Tehran. He was 34."
        ),
        main_works=["Woe from Wit"],
        main_achievement="Creation of 'Woe from Wit' — the most quoted play in the Russian language.",
        interesting_fact=(
            "Dozens of phrases from 'Woe from Wit' became Russian proverbs, e.g. 'Happy hours are not observed.'"
        ),
        mini_question="Why is 'Woe from Wit' so important for Russian culture?",
        mini_answer="Its phrases entered everyday Russian speech as proverbs — practically every educated Russian quotes it.",
        map_places=["moscow"],
    ),
    "zhukovsky": Author(
        id="zhukovsky",
        name="Vasily Zhukovsky",
        life_years="1783–1852",
        period_id="golden_age",
        who_they_were="Poet, translator, tutor to the heir — the 'father of Russian Romanticism.'",
        why_they_matter=(
            "Zhukovsky introduced Romanticism to Russian literature and created a poetic language "
            "of emotional depth that Pushkin built upon."
        ),
        historical_context=(
            "Zhukovsky was the illegitimate son of a nobleman and a Turkish captive. "
            "He became tutor to the future Alexander II and influenced the heir's liberal views."
        ),
        main_works=["The Bard", "Svetlana", "Translations of Homer and Schiller"],
        main_achievement="Introduction of Romanticism to Russian literature and creation of the Russian ballad.",
        interesting_fact="Zhukovsky was Pushkin's literary mentor and later wrote his epitaph.",
        mini_question="What role did Zhukovsky play in Russian literature?",
        mini_answer="He introduced Romanticism and the ballad form, creating the poetic tradition that Pushkin perfected.",
        map_places=[],
    ),
    "turgenev": Author(
        id="turgenev",
        name="Ivan Turgenev",
        life_years="1818–1883",
        period_id="realism",
        who_they_were="Novelist, playwright, translator — the first Russian writer widely recognized in Europe.",
        why_they_matter=(
            "Turgenev captured the social types of his era — the 'superfluous man,' the 'new person,' "
            "the 'fathers and sons' — and was the first to bring Russian literature to Western audiences."
        ),
        historical_context=(
            "Turgenev spent much of his life in Europe and served as a cultural bridge between "
            "Russia and the West. He was friends with Flaubert, Maupassant, and George Sand."
        ),
        main_works=[
            "Fathers and Sons",
            "A Nest of the Gentry",
            "Mumu",
            "Asya",
            "Spring Torrents",
        ],
        main_achievement="Creation of the term 'nihilist' through Bazarov and the first European-scale Russian novel.",
        interesting_fact="Turgenev's 'Fathers and Sons' introduced the word 'nihilism' into the Russian language.",
        mini_question="What social type did Turgenev create in 'Fathers and Sons'?",
        mini_answer="Bazarov — the nihilist, a 'new person' who rejects the old values of the nobility.",
        map_places=["spasskoye"],
    ),
    "goncharov": Author(
        id="goncharov",
        name="Ivan Goncharov",
        life_years="1812–1891",
        period_id="realism",
        who_they_were="Novelist — creator of the most famous lazy person in world literature.",
        why_they_matter=(
            "Goncharov's Oblomov became a symbol of stagnation and the 'Oblomovism' that "
            "characterized a whole stratum of Russian noble society."
        ),
        historical_context=(
            "Goncharov worked as a censor and traveled around the world on a frigate. "
            "His novel 'Oblomov' diagnosed the disease of Russian noble passivity."
        ),
        main_works=["Oblomov", "The Same Old Story", "The Precipice"],
        main_achievement="Creation of 'Oblomovism' — a concept that became a diagnosis of an entire social disease.",
        interesting_fact="The word 'Oblomovism' entered the Russian language as a term for apathy and inaction.",
        mini_question="What social phenomenon did 'Oblomovism' describe?",
        mini_answer="Noble apathy and inability to act — a whole way of life defined by doing nothing.",
        map_places=[],
    ),
    "dostoevsky": Author(
        id="dostoevsky",
        name="Fyodor Dostoevsky",
        life_years="1821–1881",
        period_id="realism",
        who_they_were="Novelist, philosopher, journalist — one of the greatest psychological writers in world literature.",
        why_they_matter=(
            "Dostoevsky explored the darkest corners of the human soul and the deepest philosophical "
            "questions — freedom, suffering, faith, and the nature of evil. His influence extends far beyond literature."
        ),
        historical_context=(
            "Dostoevsky was sentenced to death for political activity, reprieved at the last moment, "
            "and spent four years in Siberian prison. This experience transformed his worldview and art."
        ),
        main_works=[
            "Crime and Punishment",
            "The Brothers Karamazov",
            "The Idiot",
            "Notes from Underground",
            "Demons",
        ],
        main_achievement="Creation of the psychological novel that explored human freedom, suffering, and faith.",
        interesting_fact=(
            "Dostoevsky's mock execution in 1849 was one of the most dramatic moments in literary history — "
            "he was told he would be shot, then pardoned at the last second."
        ),
        mini_question="What philosophical question is central to Dostoevsky's work?",
        mini_answer="Whether suffering or freedom is the essence of human existence — can humanity survive without God?",
        map_places=["saint_petersburg"],
    ),
    "tolstoy": Author(
        id="tolstoy",
        name="Leo Tolstoy",
        life_years="1828–1910",
        period_id="reforms",
        who_they_were="Novelist, philosopher, moral authority — one of the greatest writers in world history.",
        why_they_matter=(
            "Tolstoy's 'War and Peace' and 'Anna Karenina' are among the greatest novels ever written. "
            "In his later years, he became a moral authority whose teachings influenced Gandhi and Martin Luther King."
        ),
        historical_context=(
            "Tolstoy witnessed the Crimean War, the Emancipation of 1861, and the revolutions. "
            "He gave away his property, renounced copyright, and was excommunicated by the Orthodox Church."
        ),
        main_works=[
            "War and Peace",
            "Anna Karenina",
            "The Death of Ivan Ilyich",
            "Resurrection",
            "The Kreutzer Sonata",
        ],
        main_achievement="Creation of the epic novel that combined individual lives with the sweep of history.",
        interesting_fact=(
            "Tolstoy's letter to the Tsar calling the Russian Orthodox Church corrupt got him "
            "excommunicated — and 2,000 people marched in his funeral procession."
        ),
        mini_question="What makes 'War and Peace' unique among novels?",
        mini_answer="It combines the story of individuals with the philosophy of history — showing that historical events are shaped by countless wills, not just 'great men.'",
        map_places=["moscow", "yasnaya_polyana"],
    ),
    "nekrasov": Author(
        id="nekrasov",
        name="Nikolai Nekrasov",
        life_years="1821–1878",
        period_id="reforms",
        who_they_were="Poet, publisher — the voice of the Russian people and the 'peasant poet.'",
        why_they_matter=(
            "Nekrasov brought the suffering and life of ordinary Russians into poetry. "
            "As editor of 'Sovremennik,' he shaped public opinion for two decades."
        ),
        historical_context=(
            "Nekrasov ran Russia's most influential literary journal, 'Sovremennik,' defending it "
            "against censorship while publishing Chernyshevsky, Tolstoy, and Turgenev."
        ),
        main_works=[
            "Who Can Be Happy and Free in Russia?",
            "Red-Nosed Frost",
            "Russian Women",
            "Peddlers",
        ],
        main_achievement="Creation of 'peasant poetry' that gave voice to the suffering of ordinary Russians.",
        interesting_fact=(
            "Nekrasov managed 'Sovremennik' for 20 years, making it Russia's most important literary journal, "
            "all while writing his own poetry."
        ),
        mini_question="What did Nekrasov bring to Russian poetry?",
        mini_answer="The voice of the people — he was the first major poet to write about peasant suffering as the main subject.",
        map_places=[],
    ),
    "ostrovsky": Author(
        id="ostrovsky",
        name="Alexander Ostrovsky",
        life_years="1823–1886",
        period_id="realism",
        who_they_were="Playwright — the creator of the Russian national theater.",
        why_they_matter=(
            "Ostrovsky created the Russian national repertoire. Before him, Russian theaters mostly "
            "performed translated European plays; after him, they had their own living drama."
        ),
        historical_context=(
            "Ostrovsky depicted the merchant class of Moscow — a social stratum that other writers "
            "ignored. He also led the creation of the Society of Russian Dramatic Writers."
        ),
        main_works=["The Storm", "The Forest", "Enough Simplicity for Every Wise Man", "The Snow Maiden"],
        main_achievement="Creation of the Russian national theater and a living dramatic language.",
        interesting_fact="Ostrovsky wrote 47 original plays — almost a play a year for his entire adult life.",
        mini_question="What social class did Ostrovsky bring to the Russian stage?",
        mini_answer="The Moscow merchant class — previously invisible in Russian drama.",
        map_places=["moscow"],
    ),
    "saltykov": Author(
        id="saltykov",
        name="Mikhail Saltykov-Shchedrin",
        life_years="1826–1889",
        period_id="realism",
        who_they_were="Satirist, essayist — Russia's greatest political satirist.",
        why_they_matter=(
            "Saltykov-Shchedrin created a satirical language that could expose the absurdity of "
            "Russian bureaucracy and social inequality under the Tsars."
        ),
        historical_context=(
            "Exiled to Vyatka for his satire, Saltykov later returned to Saint Petersburg and "
            "became one of the most fearless critics of Russian autocracy."
        ),
        main_works=["The Golovlyov Family", "History of a Town", "Fairy Tales for Children"],
        main_achievement="Creation of a satirical language for exposing bureaucratic absurdity and social injustice.",
        interesting_fact="His 'Fairy Tales for Children' are actually sharp political satire disguised as children's stories.",
        mini_question="What literary technique is Saltykov-Shchedrin famous for?",
        mini_answer="Aesopian language — allegorical satire that could criticize the regime while avoiding censorship.",
        map_places=[],
    ),
    "chernyshevsky": Author(
        id="chernyshevsky",
        name="Nikolai Chernyshevsky",
        life_years="1828–1889",
        period_id="reforms",
        who_they_were="Philosopher, critic, revolutionary — the author of 'What Is to Be Done?'",
        why_they_matter=(
            "Chernyshevsky's 'What Is to Be Done?' became the handbook of the Russian revolutionary "
            "movement and influenced Lenin, who called it life-changing."
        ),
        historical_context=(
            "Chernyshevsky was arrested for revolutionary activity and spent 20 years in Siberian exile. "
            "He wrote 'What Is to Be Done?' in prison, and it was published legally."
        ),
        main_works=["What Is to Be Done?", "The Anthropological Principle in Philosophy"],
        main_achievement="Creation of 'What Is to Be Done?' — the program of the Russian revolutionary movement.",
        interesting_fact="Lenin titled his own political pamphlet 'What Is to Be Done?' in direct homage to Chernyshevsky.",
        mini_question="Why was 'What Is to Be Done?' so influential?",
        mini_answer="It provided a model of the 'new person' — rational, self-sacrificing, and committed to social change.",
        map_places=[],
    ),
    "chekhov": Author(
        id="chekhov",
        name="Anton Chekhov",
        life_years="1860–1904",
        period_id="chekhov",
        who_they_were="Short story writer, playwright, doctor — the master of understatement.",
        why_they_matter=(
            "Chekhov revolutionized both the short story and drama by removing moralizing and showing "
            "life as it is. His influence on modern drama is comparable to Shakespeare's."
        ),
        historical_context=(
            "A doctor by training, Chekhov traveled across Siberia to report on prison conditions on "
            "Sakhalin Island. He treated patients for free and built schools for peasants."
        ),
        main_works=[
            "The Cherry Orchard",
            "The Seagull",
            "Uncle Vanya",
            "Three Sisters",
            "The Lady with the Dog",
        ],
        main_achievement="Creation of the modern short story and the new drama — indirect, subtext-driven, without moralizing.",
        interesting_fact="Chekhov was a practicing doctor who said: 'Medicine is my lawful wife, literature is my mistress.'",
        mini_question="What did Chekhov change in drama?",
        mini_answer="He removed direct conflict and moralizing, replacing them with subtext — what characters don't say matters more than what they do.",
        map_places=["moscow", "taganrog"],
    ),
    "korolenko": Author(
        id="korolenko",
        name="Vladimir Korolenko",
        life_years="1853–1921",
        period_id="chekhov",
        who_they_were="Writer, journalist, humanitarian — the conscience of Russian literature.",
        why_they_matter=(
            "Korolenko was a tireless defender of the oppressed. He protested against the Beilis trial, "
            "the famine, and government brutality, setting an example of moral courage."
        ),
        historical_context=(
            "Exiled to Siberia for populist activity, Korolenko later became one of the most respected "
            "public figures in Russia, defending human rights under both Tsarist and Soviet regimes."
        ),
        main_works=["The Blind Musician", "Makar's Dream", "The Paradox"],
        main_achievement="Setting an example of moral courage in Russian literature — defending human rights under both regimes.",
        interesting_fact="Korolenko refused to cooperate with both the Tsarist regime and the Bolsheviks.",
        mini_question="What made Korolenko unique among Russian writers?",
        mini_answer="He defended human rights under both the Tsarist and Soviet regimes, refusing to compromise with either.",
        map_places=[],
    ),
    "gorky": Author(
        id="gorky",
        name="Maxim Gorky",
        life_years="1868–1936",
        period_id="chekhov",
        who_they_were="Novelist, playwright, political figure — the founder of socialist realism.",
        why_they_matter=(
            "Gorky brought the voices of the lower classes into Russian literature and created "
            "the literary model for Soviet culture."
        ),
        historical_context=(
            "Born into poverty, Gorky became a symbol of the self-made intellectual. He was close "
            "to Lenin, opposed the Bolshevik coup, and later returned to the USSR under Stalin."
        ),
        main_works=["The Lower Depths", "Mother", "My Childhood", "The Artamonov Business"],
        main_achievement="Bringing the voice of the lower classes into literature and founding socialist realism.",
        interesting_fact="Gorky's real name was Alexei Peshkov — 'Gorky' means 'bitter,' reflecting his view of life.",
        mini_question="What social class did Gorky bring into Russian literature?",
        mini_answer="The lower classes — tramps, workers, the urban poor — who had been invisible in Russian literature before.",
        map_places=["nizhny_novgorod"],
    ),
    "andreev": Author(
        id="andreev",
        name="Leonid Andreev",
        life_years="1871–1919",
        period_id="chekhov",
        who_they_were="Writer, playwright — master of psychological horror and existential dread.",
        why_they_matter=(
            "Andreev explored the boundary between reality and madness, creating a unique blend "
            "of realism and expressionism that influenced European modernism."
        ),
        historical_context=(
            "Andreev witnessed the 1905 Revolution and the collapse of the old world. "
            "His work expressed the anxiety and existential crisis of pre-revolutionary Russia."
        ),
        main_works=["The Seven Who Were Hanged", "Red Laugh", "The Life of Vasily Fiveysky"],
        main_achievement="Creating a unique blend of realism and expressionism that captured the anxiety of pre-revolutionary Russia.",
        interesting_fact="Andreev died in 1919, the same year as Blok — both symbolizing the end of an era.",
        mini_question="What literary movement did Andreev anticipate?",
        mini_answer="Expressionism — his work blended psychological realism with horror and existential dread.",
        map_places=[],
    ),
    "blok": Author(
        id="blok",
        name="Alexander Blok",
        life_years="1880–1921",
        period_id="silver_age",
        who_they_were="Poet — the greatest lyric poet of the Silver Age.",
        why_they_matter=(
            "Blok's poetry traced the arc from mystical Symbolism to revolutionary disillusionment. "
            "His poem 'The Twelve' captured the contradictory spirit of the Russian Revolution."
        ),
        historical_context=(
            "Blok initially welcomed the 1917 Revolution but became increasingly disillusioned. "
            "He died in 1921, reportedly saying: 'If you really want to know, everything is suffocating.'"
        ),
        main_works=["The Twelve", "Verses about the Beautiful Lady", "The Scythians", "Retribution"],
        main_achievement="Creating Symbolist poetry of extraordinary beauty and capturing the spirit of revolution in verse.",
        interesting_fact="Blok's 'The Twelve' ends with Jesus Christ leading a band of Red Guards through a blizzard — one of the most controversial images in Russian poetry.",
        mini_question="What makes Blok's 'The Twelve' so controversial?",
        mini_answer="It ends with Jesus Christ leading Bolshevik Red Guards through a blizzard — a shocking fusion of revolution and religion.",
        map_places=["saint_petersburg"],
    ),
    "akhmatova": Author(
        id="akhmatova",
        name="Anna Akhmatova",
        life_years="1889–1966",
        period_id="silver_age",
        who_they_were="Poet — the voice of Russian suffering and endurance in the 20th century.",
        why_they_matter=(
            "Akhmatova created a new poetic intimacy and then became the voice of the terror. "
            "Her 'Requiem' is one of the greatest poems about state oppression."
        ),
        historical_context=(
            "Akhmatova's first husband was executed, her son was imprisoned twice, and she was "
            "banned from publishing for decades. She survived all of it and kept writing."
        ),
        main_works=["Requiem", "Poem Without a Hero", "The White Flock", "Evening"],
        main_achievement="Creating a poetry of personal and national memory that survived and documented the terror.",
        interesting_fact=(
            "Akhmatova wrote 'Requiem' in her head and her friends memorized the lines, "
            "then burned the paper — she couldn't write it down for fear of arrest."
        ),
        mini_question="How did Akhmatova write 'Requiem' under the terror?",
        mini_answer="She memorized the lines and had friends memorize them too, then destroyed the written versions — the poem survived only in human memory.",
        map_places=["saint_petersburg"],
    ),
    "gumilev": Author(
        id="gumilev",
        name="Nikolai Gumilev",
        life_years="1886–1921",
        period_id="silver_age",
        who_they_were="Poet, explorer, founder of Acmeism — the romantic adventurer of Russian poetry.",
        why_they_matter=(
            "Gumilev founded Acmeism as a reaction against Symbolism's vagueness, calling for clarity, "
            "precision, and celebration of the material world."
        ),
        historical_context=(
            "Gumilev traveled to Africa, fought in World War I, and was executed by the Cheka in 1921 "
            "for alleged participation in an anti-Bolshevik conspiracy."
        ),
        main_works=["The Pillar of Fire", "The Porcelain Pavilion", "Romantic Blossoms"],
        main_achievement="Founding Acmeism — a poetic movement that replaced Symbolist mystery with clarity and precision.",
        interesting_fact="Gumilev was Akhmatova's first husband — their marriage was one of the most famous literary couples in history.",
        mini_question="What did Acmeism propose instead of Symbolism?",
        mini_answer="Clarity, precision, and celebration of the material world — poetry should be clear, not mysterious.",
        map_places=[],
    ),
    "tsvetaeva": Author(
        id="tsvetaeva",
        name="Marina Tsvetaeva",
        life_years="1892–1941",
        period_id="silver_age",
        who_they_were="Poet — one of the greatest lyric voices in any language.",
        why_they_matter=(
            "Tsvetaeva's poetry is defined by its intensity, rhythm, and emotional extremes. "
            "Her work on love, exile, and rejection has no equal in Russian literature."
        ),
        historical_context=(
            "Tsvetaeva emigrated in 1922, lived in poverty in Paris and Prague, and returned to "
            "the USSR in 1939. She hanged herself in 1941 after her husband was executed and her daughter arrested."
        ),
        main_works=["The Pied Piper", "Poem of the End", "Poem of the Mountain", "After Russia"],
        main_achievement="Creating poetry of extreme emotional intensity that pushed the Russian language to its limits.",
        interesting_fact="Tsvetaeva once said: 'I don't write poems — they write me. I am only the pen.'",
        mini_question="What characterizes Tsvetaeva's poetry?",
        mini_answer="Extreme emotional intensity, radical rhythm, and a language that pushes Russian to its absolute limits.",
        map_places=[],
    ),
    "mayakovsky": Author(
        id="mayakovsky",
        name="Vladimir Mayakovsky",
        life_years="1893–1930",
        period_id="silver_age",
        who_they_were="Poet, artist, propagandist — the explosive voice of Russian Futurism.",
        why_they_matter=(
            "Mayakovsky reinvented Russian poetry with his 'stepladder' verse, street language, "
            "and revolutionary energy. He remains one of the most influential modernist poets."
        ),
        historical_context=(
            "Mayakovsky embraced the Revolution and became its literary voice. Disillusioned by "
            "bureaucracy and personal tragedy, he shot himself in 1930."
        ),
        main_works=["A Cloud in Trousers", "The Backbone Flute", "About That", "Vladimir Ilyich Lenin"],
        main_achievement="Creating a new poetic language — loud, rhythmic, 'stepladder' verse that broke all traditions.",
        interesting_fact="Mayakovsky's suicide note read: 'Don't blame anyone — it's my own fault. Love that boat, and it sails away.'",
        mini_question="What was Mayakovsky's 'stepladder' verse?",
        mini_answer="A visual arrangement of lines in a staircase pattern that forced a new rhythm — breaking traditional Russian verse.",
        map_places=[],
    ),
    "bryusov": Author(
        id="bryusov",
        name="Valery Bryusov",
        life_years="1873–1924",
        period_id="silver_age",
        who_they_were="Poet, critic, translator — the founder of Russian Symbolism.",
        why_they_matter=(
            "Bryusov organized and led the Symbolist movement in Russian poetry, publishing its "
            "manifestos and mentoring younger poets like Blok and Bely."
        ),
        historical_context=(
            "A meticulous craftsman of verse, Bryusov later joined the Bolsheviks and worked in "
            "cultural administration, though his heart was always in the pre-revolutionary world of art."
        ),
        main_works=["The Chevalier of the Bronze", "Stephanos", "Urbi et Orbi"],
        main_achievement="Organizing and leading the Russian Symbolist movement — he was its chief architect and mentor.",
        interesting_fact="Bryusov's early poem 'O, cover thy pale legs' was considered so scandalous it helped launch Symbolism.",
        mini_question="What was Bryusov's role in Russian Symbolism?",
        mini_answer="He was its architect and organizer — publishing manifestos, mentoring younger poets, and giving the movement its structure.",
        map_places=[],
    ),
    "bely": Author(
        id="bely",
        name="Andrei Bely",
        life_years="1880–1934",
        period_id="silver_age",
        who_they_were="Novelist, poet, theorist — the creator of Russian literary modernism.",
        why_they_matter=(
            "Bely's novel 'Petersburg' is considered the Russian 'Ulysses' — a revolutionary "
            "experiment with language, rhythm, and narrative that influenced Nabokov and modernism."
        ),
        historical_context=(
            "Bely was deeply involved in Symbolist theory, anthroposophy, and the cultural upheavals "
            "of the Silver Age. His personal life was as turbulent as his prose."
        ),
        main_works=["Petersburg", "The Silver Dove", "Kotik Letayev"],
        main_achievement="Creating 'Petersburg' — one of the great modernist novels and a radical experiment with Russian prose.",
        interesting_fact="Nabokov ranked 'Petersburg' as one of the four greatest novels of the 20th century.",
        mini_question="Why is Bely's 'Petersburg' compared to Joyce's 'Ulysses'?",
        mini_answer="Both are radical experiments with language, rhythm, and narrative that redefined what a novel could be.",
        map_places=[],
    ),
    "yesenin": Author(
        id="yesenin",
        name="Sergei Yesenin",
        life_years="1895–1925",
        period_id="silver_age",
        who_they_were="Poet — the 'peasant poet' and the most lyrical voice of the Russian countryside.",
        why_they_matter=(
            "Yesenin's poetry captured the beauty and tragedy of rural Russia with unmatched lyricism. "
            "His suicide at 30 became a symbol of the destruction of the old Russian village."
        ),
        historical_context=(
            "Born into a peasant family, Yesenin became famous overnight. He married the American "
            "dancer Isadora Duncan, traveled the world, and returned disillusioned."
        ),
        main_works=["Anna Snegina", "The Black Man", "Letter to My Mother", "I Don't Regret"],
        main_achievement="Creating poetry of rural Russia that captured its beauty and its destruction with unmatched lyricism.",
        interesting_fact="Yesenin's last poem, written in his own blood, ended: 'In this life, dying is nothing new.'",
        mini_question="What did Yesenin's poetry symbolize for Russia?",
        mini_answer="The beauty and destruction of rural Russia — his death became a symbol of the old village dying.",
        map_places=[],
    ),
}
