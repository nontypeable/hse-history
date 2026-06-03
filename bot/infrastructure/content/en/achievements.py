from bot.domain.entities import Achievement

ACHIEVEMENTS: dict[str, Achievement] = {
    "literary_language": Achievement(
        id="literary_language",
        emoji="🏛",
        title="Creation of the modern Russian literary language",
        explanation=(
            "Before Pushkin, Russian high literature was written in Church Slavonic or French. "
            "Pushkin combined the spoken language with literary tradition, creating a flexible, "
            "expressive literary Russian that we still use today."
        ),
        why_it_matters=(
            "Without a literary language, there is no national literature. Pushkin's synthesis "
            "made it possible for all subsequent Russian writers to express complex ideas in Russian."
        ),
        related_author_ids=["pushkin", "gogol", "lermontov"],
        related_works=["Eugene Onegin (Pushkin)", "The Government Inspector (Gogol)"],
        historical_context=(
            "The debate about whether Russian was suitable for high literature lasted decades. "
            "Pushkin's work settled it permanently."
        ),
    ),
    "russian_novel": Achievement(
        id="russian_novel",
        emoji="📖",
        title="Rise of the Russian novel",
        explanation=(
            "In the 1860s-1880s, Tolstoy and Dostoevsky created novels that rival anything in "
            "world literature. 'War and Peace,' 'Anna Karenina,' 'Crime and Punishment,' and "
            "'The Brothers Karamazov' set the standard for the novel as an art form."
        ),
        why_it_matters=(
            "The Russian novel proved that literature could address the biggest questions — "
            "freedom, faith, justice, the meaning of life — while remaining great art."
        ),
        related_author_ids=["tolstoy", "dostoevsky", "turgenev"],
        related_works=["War and Peace", "Crime and Punishment", "Fathers and Sons"],
        historical_context=(
            "The Great Reforms created a public hungry for answers about Russia's future. "
            "The novel became the vehicle for those answers."
        ),
    ),
    "psychology": Achievement(
        id="psychology",
        emoji="🧠",
        title="Psychological depth",
        explanation=(
            "Russian writers — especially Dostoevsky, Tolstoy, and Chekhov — pioneered the "
            "psychological exploration of characters. They showed that literature could map "
            "the human mind with the precision of science."
        ),
        why_it_matters=(
            "Dostoevsky's interior monologues and Tolstoy's 'diplomatic' narration influenced "
            "Freud, Proust, Faulkner, and the entire tradition of psychological realism."
        ),
        related_author_ids=["dostoevsky", "tolstoy", "chekhov", "lermontov"],
        related_works=["Crime and Punishment", "Anna Karenina", "The Death of Ivan Ilyich"],
        historical_context=(
            "The complexity of Russian society — its contradictions, reforms, and crises — "
            "demanded characters who were psychologically complex, not simply good or evil."
        ),
    ),
    "social_criticism": Achievement(
        id="social_criticism",
        emoji="⚖️",
        title="Social criticism",
        explanation=(
            "From Gogol's satires to Saltykov-Shchedrin's grotesques to Nekrasov's peasant poetry, "
            "Russian literature made social injustice its central subject."
        ),
        why_it_matters=(
            "In a country without free elections or a free press, literature became the main "
            "forum for debating social questions — serfdom, poverty, injustice, and reform."
        ),
        related_author_ids=["gogol", "nekrasov", "saltykov", "turgenev"],
        related_works=[
            "Dead Souls (Gogol)",
            "The Government Inspector (Gogol)",
            "Who Can Be Happy and Free? (Nekrasov)",
        ],
        historical_context=(
            "Censorship made direct political criticism impossible, so writers used literature "
            "as a substitute for public debate."
        ),
    ),
    "new_drama": Achievement(
        id="new_drama",
        emoji="🎭",
        title="New drama",
        explanation=(
            "Ostrovsky created the Russian national theater, and Chekhov revolutionized drama "
            "by replacing direct conflict with subtext. Chekhov's plays changed theater worldwide."
        ),
        why_it_matters=(
            "Chekhov's dramatic method — where what characters don't say matters more than "
            "what they do — became the foundation of modern theater, from Stanislavski to the present."
        ),
        related_author_ids=["chekhov", "ostrovsky", "gorky"],
        related_works=["The Cherry Orchard (Chekhov)", "The Seagull (Chekhov)", "The Storm (Ostrovsky)"],
        historical_context=(
            "Before Ostrovsky, Russian theater was dominated by French and German plays. "
            "Chekhov then took drama in an entirely new direction."
        ),
    ),
    "silver_age_poetry": Achievement(
        id="silver_age_poetry",
        emoji="🌙",
        title="Silver Age poetry",
        explanation=(
            "Between 1890 and 1917, Russian poetry experienced an unprecedented flowering. "
            "Symbolism, Acmeism, and Futurism produced Blok, Akhmatova, Mayakovsky, Tsvetaeva, "
            "and others — a constellation of poetic genius."
        ),
        why_it_matters=(
            "The Silver Age showed that Russian poetry could be as innovative and experimental "
            "as any in Europe — and in some cases, more so."
        ),
        related_author_ids=["blok", "akhmatova", "mayakovsky", "tsvetaeva", "gumilev", "bryusov", "bely", "yesenin"],
        related_works=["The Twelve (Blok)", "Requiem (Akhmatova)", "A Cloud in Trousers (Mayakovsky)"],
        historical_context=(
            "The crisis of the Russian Empire, the 1905 Revolution, and the approaching cataclysm "
            "of 1917 created a pressure that produced extraordinary poetry."
        ),
    ),
    "literary_movements": Achievement(
        id="literary_movements",
        emoji="🧩",
        title="Literary movements",
        explanation=(
            "Russian literature produced distinct literary movements: Romanticism (Pushkin, Lermontov), "
            "Realism (Tolstoy, Dostoevsky), Symbolism (Blok, Bryusov), Acmeism (Gumilev, Akhmatova), "
            "and Futurism (Mayakovsky). Each transformed the language and possibilities of literature."
        ),
        why_it_matters=(
            "These movements were not just aesthetic — each was a response to historical crisis "
            "and a proposal for how literature should engage with reality."
        ),
        related_author_ids=["pushkin", "tolstoy", "blok", "gumilev", "mayakovsky"],
        related_works=["Eugene Onegin (Pushkin)", "The Twelve (Blok)", "A Cloud in Trousers (Mayakovsky)"],
        historical_context=(
            "Each movement emerged from a specific historical moment: Romanticism from the Decembrist era, "
            "Realism from the Great Reforms, and the Silver Age movements from the crisis of autocracy."
        ),
    ),
    "global_importance": Achievement(
        id="global_importance",
        emoji="🌍",
        title="Global importance of Russian literature",
        explanation=(
            "Russian literature of the 19th and early 20th centuries became one of the great "
            "literary traditions of world literature. Tolstoy, Dostoevsky, Chekhov, and others "
            "are read and studied everywhere on Earth."
        ),
        why_it_matters=(
            "Russian literature's global influence extends to philosophy, psychology, political "
            "thought, and every major literary tradition. Writers from Faulkner to Camus to Murakami "
            "acknowledge their debt to the Russian novel."
        ),
        related_author_ids=["tolstoy", "dostoevsky", "chekhov", "pushkin"],
        related_works=["War and Peace", "Crime and Punishment", "The Cherry Orchard"],
        historical_context=(
            "Translations in the late 19th and 20th centuries brought Russian literature to "
            "global audiences. Its combination of philosophical depth and human sympathy "
            "made it universally relevant."
        ),
    ),
}
