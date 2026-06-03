from bot.domain.entities import MapPlace

MAP_PLACES: dict[str, MapPlace] = {
    "moscow": MapPlace(
        id="moscow",
        name="Moscow",
        why_it_matters=(
            "The ancient capital and cultural heart of Russia. Moscow was the center of noble life, "
            "the setting for many classic works, and the city where several major writers lived and worked."
        ),
        related_author_ids=["pushkin", "griboyedov", "tolstoy", "chekhov", "ostrovsky"],
        historical_value=(
            "Moscow saw Griboyedov's 'Woe from Wit,' Pushkin's marriage, Tolstoy's childhood, "
            "Ostrovsky's merchant dramas, and Chekhov's medical practice. The city is woven into "
            "the fabric of Russian literature."
        ),
    ),
    "saint_petersburg": MapPlace(
        id="saint_petersburg",
        name="Saint Petersburg",
        why_it_matters=(
            "Peter the Great's 'window to Europe' — the imperial capital and the most literary "
            "city in Russia. Dostoevsky called it 'the most abstract and intentional city in the world.'"
        ),
        related_author_ids=["pushkin", "gogol", "dostoevsky", "blok", "akhmatova"],
        historical_value=(
            "Pushkin's 'Bronze Horseman' is about Petersburg. Gogol's 'Overcoat' and 'Nose' "
            "are set here. Dostoevsky's 'Crime and Punishment' maps the city street by street. "
            "Blok and Akhmatova made it the city of Silver Age poetry."
        ),
    ),
    "yasnaya_polyana": MapPlace(
        id="yasnaya_polyana",
        name="Yasnaya Polyana",
        why_it_matters=(
            "Leo Tolstoy's family estate, where he was born, wrote 'War and Peace' and 'Anna Karenina,' "
            "and is buried. It is one of the most important literary sites in the world."
        ),
        related_author_ids=["tolstoy"],
        historical_value=(
            "Tolstoy ran his estate as a model of the just life he preached — he founded a school "
            "for peasant children and renounced his copyright. He is buried in an unmarked grave "
            "in the forest, as he wished."
        ),
    ),
    "taganrog": MapPlace(
        id="taganrog",
        name="Taganrog",
        why_it_matters=(
            "Anton Chekhov's birthplace — a provincial port city on the Sea of Azov that shaped "
            "his understanding of provincial life."
        ),
        related_author_ids=["chekhov"],
        historical_value=(
            "Chekhov grew up in a merchant family in Taganrog, witnessing the monotony and "
            "petty tyrannies of provincial life that he would later immortalize in his stories."
        ),
    ),
    "tarkhany": MapPlace(
        id="tarkhany",
        name="Tarkhany",
        why_it_matters=(
            "Mikhail Lermontov's childhood estate — the place that inspired his love of nature "
            "and his vision of the Russian countryside."
        ),
        related_author_ids=["lermontov"],
        historical_value=(
            "Lermontov spent his happiest years at Tarkhany. The estate is now a museum where "
            "visitors can see the landscape that inspired 'Mtsyri' and his lyrics."
        ),
    ),
    "spasskoye": MapPlace(
        id="spasskoye",
        name="Spasskoye-Lutovinovo",
        why_it_matters=(
            "Ivan Turgenev's family estate — the setting and inspiration for 'A Nest of the Gentry' "
            "and the world of 'Fathers and Sons.'"
        ),
        related_author_ids=["turgenev"],
        historical_value=(
            "Turgenev's mother was a famously cruel serf owner, and young Ivan grew up witnessing "
            "the brutality of serfdom — an experience that shaped his hatred of serfdom and his "
            "decision to write 'Mumu' and 'A Nest of the Gentry.'"
        ),
    ),
    "nizhny_novgorod": MapPlace(
        id="nizhny_novgorod",
        name="Nizhny Novgorod",
        why_it_matters=(
            "Maxim Gorky's birthplace — the city that gave him his pen name ('Gorky' means 'bitter') "
            "and the setting for his stories about the lower classes."
        ),
        related_author_ids=["gorky"],
        historical_value=(
            "Gorky grew up in poverty in Nizhny, and his autobiographical trilogy 'My Childhood,' "
            "'In the World,' and 'My Universities' describes the harsh life of the lower classes "
            "in this Volga city."
        ),
    ),
}
