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
    ),
}
