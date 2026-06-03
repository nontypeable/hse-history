from bot.domain.entities import Event

EVENTS: dict[str, Event] = {
    "war_1812": Event(
        id="war_1812",
        date="1812",
        title="Patriotic War of 1812",
        what_happened=(
            "Napoleon's Grande Armée invaded Russia in June 1812. The Russian strategy of "
            "retreat and scorched earth led to the destruction of Moscow by fire. The French "
            "army, weakened by hunger and cold, retreated and was largely destroyed."
        ),
        why_it_matters=(
            "The victory over Napoleon became a founding myth of modern Russian national identity. "
            "It demonstrated that Russia was a European power and inspired decades of cultural "
            "and political development."
        ),
        connection_to_literature=(
            "The War of 1812 directly inspired Pushkin's 'Borodino,' Lermontov's 'Borodino,' "
            "and Tolstoy's 'War and Peace.' It created the idea of the Russian people as a "
            "historical force."
        ),
        related_author_ids=["pushkin", "lermontov", "tolstoy"],
        related_works=["War and Peace", "Borodino (Pushkin)", "Borodino (Lermontov)"],
        check_question="Which major novel was inspired by the War of 1812?",
        check_answer="Tolstoy's 'War and Peace' — the war is central to the novel's exploration of history and national identity.",
    ),
    "decembrist_revolt": Event(
        id="decembrist_revolt",
        date="1825",
        title="Decembrist revolt",
        what_happened=(
            "On December 14, 1825, a group of noble officers refused to swear allegiance to "
            "Nicholas I and demanded a constitution and the abolition of serfdom. The revolt "
            "was quickly suppressed; five leaders were executed, and over 100 were exiled to Siberia."
        ),
        why_it_matters=(
            "The Decembrist revolt was the first organized political opposition in Russian history. "
            "It began the tradition of revolutionary struggle that would define Russian politics "
            "for the next century."
        ),
        connection_to_literature=(
            "Many Decembrists were Pushkin's friends. The revolt shaped the entire Golden Age — "
            "Pushkin's exile, Lermontov's outrage, and the censorship regime that defined Nicholas I's reign."
        ),
        related_author_ids=["pushkin", "lermontov"],
        related_works=["Death of a Poem (Lermontov)", "Pushkin's exile poetry"],
        check_question="Why were many Decembrists Pushkin's friends?",
        check_answer="Because they were young nobles educated in the same liberal spirit — Pushkin's lyceum classmates were among the rebels.",
    ),
    "westernizers_slavophiles": Event(
        id="westernizers_slavophiles",
        date="1830s–1840s",
        title="Westernizers and Slavophiles",
        what_happened=(
            "Two intellectual movements emerged: Westernizers believed Russia should follow "
            "Europe's path of development, while Slavophiles argued Russia had its own unique "
            "path based on Orthodoxy, community, and tradition."
        ),
        why_it_matters=(
            "This debate — should Russia follow Europe or find its own path? — defined Russian "
            "intellectual life for the rest of the century and echoes in Russian politics today."
        ),
        connection_to_literature=(
            "Chaadayev's 'Philosophical Letters' started the debate. Turgenev represented the "
            "Westernizers; Dostoevsky and the Slavophiles argued for Russian uniqueness. "
            "'Fathers and Sons' dramatized this conflict."
        ),
        related_author_ids=["turgenev", "dostoevsky", "chernyshevsky"],
        related_works=["Fathers and Sons (Turgenev)", "Philosophical Letters (Chaadayev)"],
        check_question="What was the central question of the Westernizer-Slavophile debate?",
        check_answer="Should Russia follow Europe's path of development, or does it have its own unique path?",
    ),
    "reign_alexander_2": Event(
        id="reign_alexander_2",
        date="1855–1881",
        title="Reign of Alexander II",
        what_happened=(
            "Alexander II became Tsar in 1855 and launched the Great Reforms: emancipation of the "
            "serfs, judicial reform, zemstvo reform, and military reform. He was assassinated "
            "by revolutionaries in 1881."
        ),
        why_it_matters=(
            "Alexander II's reforms transformed Russian society. The emancipation of 23 million "
            "serfs in 1861 was the single largest peaceful social transformation in European history."
        ),
        connection_to_literature=(
            "The reforms defined the literature of the 1860s-1880s. Turgenev, Nekrasov, "
            "Tolstoy, and Dostoevsky all wrote in response to them. 'Fathers and Sons' and "
            "'What Is to Be Done?' are direct products of this era."
        ),
        related_author_ids=["tolstoy", "dostoevsky", "nekrasov", "chernyshevsky", "turgenev"],
        related_works=["Fathers and Sons (Turgenev)", "What Is to Be Done? (Chernyshevsky)"],
        check_question="Why was Alexander II called the 'Tsar-Liberator'?",
        check_answer="Because he emancipated 23 million serfs in 1861 — the largest peaceful social transformation in European history.",
    ),
    "emancipation_1861": Event(
        id="emancipation_1861",
        date="1861",
        title="Emancipation of the serfs",
        what_happened=(
            "On March 3, 1861, Alexander II signed the Emancipation Manifesto, freeing 23 million "
            "serfs. However, the land settlement was unfavorable to peasants, who had to pay "
            "redemption payments for decades."
        ),
        why_it_matters=(
            "The emancipation ended centuries of feudal bondage but left the 'land question' "
            "unresolved — a problem that would contribute to the revolutions of 1905 and 1917."
        ),
        connection_to_literature=(
            "The emancipation is the background of Tolstoy's 'Anna Karenina' (Levin's reforms), "
            "Nekrasov's poetry about peasant life, and Turgenev's 'Fathers and Sons.'"
        ),
        related_author_ids=["tolstoy", "nekrasov", "turgenev"],
        related_works=["Anna Karenina (Tolstoy)", "Who Can Be Happy and Free in Russia? (Nekrasov)"],
        check_question="Why did the emancipation fail to fully solve the peasant question?",
        check_answer="Because peasants received too little land and had to pay redemption payments — the 'land question' remained unresolved.",
    ),
    "public_movements": Event(
        id="public_movements",
        date="1860s–1870s",
        title="Growth of public movements",
        what_happened=(
            "After the reforms, a new public sphere emerged: journals, universities, and "
            "societies became centers of debate. Narodnichestvo (populism) sent thousands of "
            "students 'to the people' in 1874."
        ),
        why_it_matters=(
            "These movements showed that educated Russians were no longer willing to let the "
            "state decide everything. They created the tradition of public engagement that "
            "would eventually challenge autocracy."
        ),
        connection_to_literature=(
            "The 'going to the people' movement is directly depicted in Turgenev's 'Virgin Soil' "
            "and influenced Nekrasov's poetry and Chernyshevsky's political writing."
        ),
        related_author_ids=["turgenev", "nekrasov", "chernyshevsky"],
        related_works=["Virgin Soil (Turgenev)", "Who Can Be Happy and Free in Russia? (Nekrasov)"],
        check_question="What was 'going to the people' (narodnichestvo)?",
        check_answer="Thousands of students went to live among the peasants in 1874, hoping to educate them — but the peasants mostly turned them in to the police.",
    ),
    "assassination_alexander_2": Event(
        id="assassination_alexander_2",
        date="1881",
        title="Assassination of Alexander II",
        what_happened=(
            "On March 13, 1881, Alexander II was killed by a bomb thrown by members of "
            "Narodnaya Volya (The People's Will). He was assassinated on the very day he had "
            "approved a plan for constitutional reform."
        ),
        why_it_matters=(
            "The assassination ended the reform era. Alexander III reversed many of his father's "
            "reforms and imposed strict reaction. The cycle of reform and reaction became a "
            "recurring pattern in Russian history."
        ),
        connection_to_literature=(
            "Dostoevsky's 'Demons' was a direct response to revolutionary terrorism. The "
            "assassination cast a shadow over all late 19th-century literature."
        ),
        related_author_ids=["dostoevsky", "tolstoy"],
        related_works=["Demons (Dostoevsky)"],
        check_question="What was tragically ironic about the timing of Alexander II's assassination?",
        check_answer="He was killed on the very day he had approved a plan for constitutional reform — the reform that might have prevented further revolution.",
    ),
    "industrialization": Event(
        id="industrialization",
        date="1890s",
        title="Industrialization and urban growth",
        what_happened=(
            "The 1890s saw rapid industrialization under Witte's economic policy. Railways expanded, "
            "factories grew, and millions of peasants moved to cities. Saint Petersburg "
            "and Moscow doubled in population."
        ),
        why_it_matters=(
            "Industrialization created a new working class, new social tensions, and the conditions "
            "for revolution. It also transformed Russian literature's subject matter."
        ),
        connection_to_literature=(
            "Gorky wrote about the urban poor, Andreev about the anxiety of modern city life, "
            "and Chekhov about the provincial middle class caught between old and new worlds."
        ),
        related_author_ids=["gorky", "andreev", "chekhov"],
        related_works=["The Lower Depths (Gorky)", "Red Laugh (Andreev)"],
        check_question="How did industrialization change Russian literature?",
        check_answer="It brought new subjects — the urban poor, the anxiety of modern city life, and the provincial middle class caught between old and new.",
    ),
    "revolution_1905": Event(
        id="revolution_1905",
        date="1905",
        title="First Russian Revolution",
        what_happened=(
            "Bloody Sunday (January 9, 1905) — troops fired on a peaceful workers' demonstration — "
            "triggered a nationwide revolution. Strikes, mutinies (including the battleship Potemkin), "
            "and peasant uprisings forced the Tsar to create the Duma."
        ),
        why_it_matters=(
            "The Revolution of 1905 was a dress rehearsal for 1917. It showed that autocracy "
            "could be challenged and created the Duma — Russia's first parliament."
        ),
        connection_to_literature=(
            "Blok's 'The Twelve' and Mayakovsky's early poetry were shaped by 1905. "
            "Gorky was arrested during the revolution. Bely's 'Petersburg' reflects the "
            "atmosphere of revolutionary terror."
        ),
        related_author_ids=["blok", "mayakovsky", "gorky", "bely"],
        related_works=["The Twelve (Blok)", "Petersburg (Bely)"],
        check_question="Why was the 1905 Revolution called a 'dress rehearsal'?",
        check_answer="Because it showed that autocracy could be challenged, created the Duma, and previewed the tensions that would explode in 1917.",
    ),
    "wwi": Event(
        id="wwi",
        date="1914",
        title="World War I",
        what_happened=(
            "Russia entered World War I in 1914. Initial patriotism gave way to military disasters, "
            "food shortages, and economic collapse. By 1917, the war had destroyed the Tsarist regime."
        ),
        why_it_matters=(
            "World War I was the catalyst for the fall of the Russian Empire. The strain of war "
            "exposed all the weaknesses of the autocratic system."
        ),
        connection_to_literature=(
            "Mayakovsky and Blok wrote about the war's meaning. Akhmatova's 'In 1914' captured "
            "the initial patriotism. Gumilev fought on the front lines."
        ),
        related_author_ids=["mayakovsky", "blok", "akhmatova", "gumilev"],
        related_works=["A Cloud in Trousers (Mayakovsky)", "Retribution (Blok)"],
        check_question="How did World War I affect the Silver Age poets?",
        check_answer="It shattered their initial idealism — Mayakovsky and Blok wrote about its horror, Gumilev fought on the front, and Akhmatova captured the initial patriotism.",
    ),
    "revolutions_1917": Event(
        id="revolutions_1917",
        date="1917",
        title="Revolutions of 1917",
        what_happened=(
            "The February Revolution overthrew the Tsar. The October Revolution brought the "
            "Bolsheviks to power. These two revolutions ended the Russian Empire and began "
            "the Soviet era."
        ),
        why_it_matters=(
            "The revolutions of 1917 ended the world that Russian literature had been writing about. "
            "Many writers emigrated; others tried to adapt; some were silenced."
        ),
        connection_to_literature=(
            "Blok welcomed the Revolution in 'The Twelve,' then fell silent. Akhmatova, Tsvetaeva, "
            "and many others faced persecution. The Silver Age effectively ended."
        ),
        related_author_ids=["blok", "akhmatova", "tsvetaeva", "mayakovsky", "gorky"],
        related_works=["The Twelve (Blok)", "Requiem (Akhmatova)"],
        check_question="What did the 1917 revolutions mean for the Silver Age?",
        check_answer="They ended it. The world that Blok, Akhmatova, and Tsvetaeva wrote about was destroyed — some emigrated, some were silenced, some tried to adapt.",
    ),
}
