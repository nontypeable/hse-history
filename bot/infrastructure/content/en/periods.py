from bot.domain.entities import Period

PERIODS: dict[str, Period] = {
    "golden_age": Period(
        id="golden_age",
        emoji="🌅",
        title="Golden Age of Russian literature",
        period="1800s–1840s",
        description=(
            "The Golden Age is the period when modern Russian literature was born. "
            "Pushkin created the literary language, Lermontov deepened psychological lyric, "
            "and Gogol opened new horizons for prose. This era was shaped by the Patriotic War "
            "of 1812, the Decembrist revolt, and the tension between European influence and "
            "Russian national identity."
        ),
        historical_context=(
            "Patriotic War of 1812 · Decembrist revolt of 1825 · "
            "Reigns of Alexander I and Nicholas I · Strict censorship · "
            "Noble culture and estate life · Formation of the modern Russian literary language"
        ),
        author_ids=["pushkin", "lermontov", "gogol", "griboyedov", "zhukovsky"],
        event_ids=["war_1812", "decembrist_revolt"],
        achievements=[
            "Formation of modern Russian literary language",
            "Development of Romanticism and Realism",
            "National literature of European scale",
            "Development of poem, verse novel, comedy, and prose tale",
            '"Superfluous man" archetype',
        ],
        questions=[
            {
                "question": "Why is Pushkin called the 'sun of Russian poetry'?",
                "options": "He wrote about the sun; He created the modern Russian literary language; He was a noble; He lived in the south",
                "answer": "He created the modern Russian literary language",
            },
            {
                "question": "What event of 1825 defined the Golden Age's political context?",
                "options": "The Emancipation Reform; The Decembrist revolt; The Crimean War; The October Revolution",
                "answer": "The Decembrist revolt",
            },
            {
                "question": "Which literary type did Lermontov create in 'A Hero of Our Time'?",
                "options": "The superfluous man; The nihilist; Oblomov; The new person",
                "answer": "The superfluous man",
            },
            {
                "question": "What did Gogol's 'The Overcoat' give rise to in Russian literature?",
                "options": "Romantic poetry; The 'overcoat' tradition of social prose; Symbolist movement; Futurism",
                "answer": "The 'overcoat' tradition of social prose",
            },
            {
                "question": "What makes Griboyedov's 'Woe from Wit' unique in Russian culture?",
                "options": "It was the first novel; Its phrases entered everyday speech as proverbs; It was banned; It was written in French",
                "answer": "Its phrases entered everyday speech as proverbs",
            },
        ],
    ),
    "realism": Period(
        id="realism",
        emoji="⚖️",
        title="Realism and social questions",
        period="1840s–1870s",
        description=(
            "The era of the great realist novel. Turgenev, Dostoevsky, Tolstoy, and others "
            "explored the deepest questions of human existence, social injustice, and the "
            "search for truth. Literature became a public arena for debating Russia's future."
        ),
        historical_context=(
            "Serfdom and its consequences · Westernizers and Slavophiles · "
            "Public thought and journals · People and intelligentsia · "
            "Literary criticism as a social force"
        ),
        author_ids=["turgenev", "goncharov", "dostoevsky", "tolstoy", "nekrasov", "ostrovsky", "saltykov"],
        event_ids=["westernizers_slavophiles"],
        achievements=[
            "Russian realist novel",
            "Psychological depth in prose",
            "Social criticism",
            "Development of drama",
            "Image of the intelligentsia",
            "Literature as public debate",
        ],
        questions=[
            {
                "question": "What concept did Turgenev's 'Fathers and Sons' introduce to Russian culture?",
                "options": "The superfluous man; Nihilism; Oblomovism; Narodnichestvo",
                "answer": "Nihilism",
            },
            {
                "question": "What philosophical question is central to Dostoevsky's work?",
                "options": "How to write better novels; Whether suffering or freedom defines humanity; How to build a utopia; Whether Russia should industrialize",
                "answer": "Whether suffering or freedom defines humanity",
            },
            {
                "question": "What social phenomenon does 'Oblomovism' describe?",
                "options": "Revolutionary activity; Noble apathy and inability to act; Industrial growth; Military reform",
                "answer": "Noble apathy and inability to act",
            },
            {
                "question": "What did Ostrovsky create for Russian culture?",
                "options": "The first Russian novel; The national theater repertoire; The first newspaper; The first university",
                "answer": "The national theater repertoire",
            },
        ],
    ),
    "reforms": Period(
        id="reforms",
        emoji="🏛",
        title="Literature and reforms",
        period="1860s–1880s",
        description=(
            "Literature became directly connected to the Great Reforms. Tolstoy and Dostoevsky "
            "reached their peaks, Nekrasov published the people's poetry, and Chernyshevsky "
            "became the voice of radical thought. The 'people' question defined the era."
        ),
        historical_context=(
            "Great Reforms of Alexander II · Emancipation of the serfs in 1861 · "
            "Judicial, zemstvo, and military reforms · Growth of public movements · "
            "Narodnichestvo · Debates about Russia's future"
        ),
        author_ids=["tolstoy", "dostoevsky", "nekrasov", "chernyshevsky", "saltykov", "turgenev"],
        event_ids=["reign_alexander_2", "emancipation_1861", "public_movements"],
        achievements=[
            "Literature as a space for discussing reforms",
            "Stronger social criticism",
            "The people as a central topic",
            "Moral and political questions",
        ],
        questions=[
            {
                "question": "Why was Alexander II called the 'Tsar-Liberator'?",
                "options": "He freed political prisoners; He emancipated 23 million serfs; He ended censorship; He gave Russia a constitution",
                "answer": "He emancipated 23 million serfs",
            },
            {
                "question": "What is 'narodnichestvo' (going to the people)?",
                "options": "Peasants moving to cities; Students going to live among peasants; A literary movement; A military campaign",
                "answer": "Students going to live among peasants",
            },
            {
                "question": "What did Nekrasov bring to Russian poetry?",
                "options": "Romanticism; The voice of the people and peasant suffering; Futurism; Symbolism",
                "answer": "The voice of the people and peasant suffering",
            },
        ],
    ),
    "chekhov": Period(
        id="chekhov",
        emoji="🍒",
        title="Late 19th century and Chekhov's era",
        period="1880s–1900s",
        description=(
            "Chekhov transformed Russian prose and drama with subtlety and understatement. "
            "Gorky brought the voice of the lower classes into literature. "
            "The old world was showing its cracks, and literature captured that."
        ),
        historical_context=(
            "Late Russian Empire · Urbanization · Growth of cities · "
            "Crisis of noble values · New social environments · "
            "Pre-revolutionary tension"
        ),
        author_ids=["chekhov", "korolenko", "gorky", "andreev"],
        event_ids=["assassination_alexander_2", "industrialization"],
        achievements=[
            "New short story form",
            "New drama",
            "Attention to everyday life",
            "Rejection of direct moralizing",
            "Image of the crisis of the old world",
        ],
        questions=[
            {
                "question": "What did Chekhov change in drama?",
                "options": "He added more monologues; He replaced direct conflict with subtext; He removed all dialogue; He wrote only tragedies",
                "answer": "He replaced direct conflict with subtext",
            },
            {
                "question": "What does 'Gorky' mean and why did he choose this pen name?",
                "options": "It means 'happy'; It means 'bitter' — reflecting his view of life; It means 'strong'; It was his mother's maiden name",
                "answer": "It means 'bitter' — reflecting his view of life",
            },
            {
                "question": "What literary movement did Andreev anticipate?",
                "options": "Romanticism; Realism; Expressionism; Classicism",
                "answer": "Expressionism",
            },
        ],
    ),
    "silver_age": Period(
        id="silver_age",
        emoji="🌙",
        title="Silver Age",
        period="1890s–1910s",
        description=(
            "The Silver Age was an explosion of poetry, philosophy, and artistic experimentation. "
            "Blok, Akhmatova, Mayakovsky, and others created entirely new literary movements. "
            "This era ended with the revolutions of 1917, which changed Russian culture forever."
        ),
        historical_context=(
            "Crisis of the Russian Empire · Revolution of 1905 · World War I · "
            "Revolutions of 1917 · Search for new cultural forms · "
            "Symbolism, Acmeism, Futurism"
        ),
        author_ids=["blok", "akhmatova", "gumilev", "tsvetaeva", "mayakovsky", "bryusov", "bely", "yesenin"],
        event_ids=["revolution_1905", "wwi", "revolutions_1917"],
        achievements=[
            "Flourishing of Russian poetry",
            "New literary movements",
            "Experiments with language and form",
            "Connection between art, philosophy, and politics",
            "Avant-garde literature",
        ],
        questions=[
            {
                "question": "What did Acmeism propose instead of Symbolism?",
                "options": "More mysticism; Clarity and precision; Political revolution; Religious themes",
                "answer": "Clarity and precision",
            },
            {
                "question": "How did Akhmatova preserve 'Requiem' during the terror?",
                "options": "She published it abroad; She and friends memorized it, then burned the paper; She hid it in a wall; She wrote it in invisible ink",
                "answer": "She and friends memorized it, then burned the paper",
            },
            {
                "question": "What was Mayakovsky's 'stepladder' verse?",
                "options": "A visual arrangement of lines in a staircase pattern; A type of sonnet; A military march rhythm; A way to write novels",
                "answer": "A visual arrangement of lines in a staircase pattern",
            },
            {
                "question": "What did the 1917 revolutions mean for the Silver Age?",
                "options": "They had no effect; They ended it; They started it; They improved it",
                "answer": "They ended it",
            },
        ],
    ),
}
