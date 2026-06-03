from bot.domain.entities import QuestStage

QUEST_STAGES: list[QuestStage] = [
    QuestStage(
        stage_number=1,
        period_id="golden_age",
        intro=(
            "🌅 Stage 1: The Golden Age of Russian Literature\n\n"
            "You enter literary Russia at the beginning of the 19th century. The Patriotic War of 1812 "
            "has just ended, the Decembrists are plotting, and Pushkin is creating a new language for "
            "Russian literature.\n\n"
            "Walk through this era, meet its authors, and answer questions to earn your first key."
        ),
        author_ids=["pushkin", "lermontov", "gogol"],
        event_ids=["war_1812", "decembrist_revolt"],
        questions=[
            {
                "question": "Why is Pushkin called the 'sun of Russian poetry'?",
                "options": "He wrote about the sun; He created the modern Russian literary language; He was a noble; He lived in the south",
                "answer": "He created the modern Russian literary language",
            },
            {
                "question": "What connects Lermontov's 'Death of a Poem' to Pushkin?",
                "options": "It's about Pushkin's exile; It's a response to Pushkin's death in a duel; It's a translation; They wrote it together",
                "answer": "It's a response to Pushkin's death in a duel",
            },
            {
                "question": "Why did Gogol burn the second volume of 'Dead Souls'?",
                "options": "He lost the manuscript; He was in a religious frenzy; The censor banned it; He gave it to a friend",
                "answer": "He was in a religious frenzy",
            },
        ],
        key_name="Freedom and personality",
    ),
    QuestStage(
        stage_number=2,
        period_id="realism",
        intro=(
            "⚖️ Stage 2: Realism and Social Questions\n\n"
            "You enter the era of the great realist novel. Serfdom still exists, Westernizers and "
            "Slavophiles debate Russia's future, and literature becomes a public arena.\n\n"
            "Turgenev, Dostoevsky, Tolstoy, and others explore the deepest questions of human existence "
            "and social justice."
        ),
        author_ids=["turgenev", "dostoevsky", "tolstoy"],
        event_ids=["westernizers_slavophiles"],
        questions=[
            {
                "question": "What did Turgenev's 'Fathers and Sons' introduce to Russian culture?",
                "options": "The superfluous man; Nihilism; Oblomovism; Populism",
                "answer": "Nihilism",
            },
            {
                "question": "What philosophical question is central to Dostoevsky's work?",
                "options": "How to write better novels; Whether suffering or freedom defines humanity; How to build a utopia; Whether Russia should industrialize",
                "answer": "Whether suffering or freedom defines humanity",
            },
            {
                "question": "What makes Tolstoy's 'War and Peace' unique?",
                "options": "It's the longest Russian novel; It combines individual lives with the philosophy of history; It has no plot; It's written in French",
                "answer": "It combines individual lives with the philosophy of history",
            },
        ],
        key_name="Society and the people",
    ),
    QuestStage(
        stage_number=3,
        period_id="reforms",
        intro=(
            "🏛 Stage 3: Literature and Reforms\n\n"
            "Alexander II is emancipating the serfs and launching the Great Reforms. Literature becomes "
            "directly connected to social change. Tolstoy and Dostoevsky reach their peaks.\n\n"
            "The 'people' question — who are the Russian people and what do they need? — defines the era."
        ),
        author_ids=["nekrasov", "chernyshevsky", "tolstoy"],
        event_ids=["emancipation_1861", "reign_alexander_2"],
        questions=[
            {
                "question": "Why was Alexander II called the 'Tsar-Liberator'?",
                "options": "He freed political prisoners; He emancipated 23 million serfs; He ended censorship; He gave Russia a constitution",
                "answer": "He emancipated 23 million serfs",
            },
            {
                "question": "What was 'going to the people' (narodnichestvo)?",
                "options": "Peasants moving to cities; Students going to live among peasants; A literary movement; A military campaign",
                "answer": "Students going to live among peasants",
            },
        ],
        key_name="Reforms and conflict",
    ),
    QuestStage(
        stage_number=4,
        period_id="chekhov",
        intro=(
            "🍒 Stage 4: Late 19th Century — Chekhov's Era\n\n"
            "The old world is showing cracks. Chekhov transforms prose and drama with understatement. "
            "Gorky brings the lower classes into literature. Cities grow, noble values decline, "
            "and revolution is in the air."
        ),
        author_ids=["chekhov", "gorky", "andreev"],
        event_ids=["assassination_alexander_2", "industrialization"],
        questions=[
            {
                "question": "What did Chekhov change in drama?",
                "options": "He added more monologues; He replaced direct conflict with subtext; He removed all dialogue; He wrote only tragedies",
                "answer": "He replaced direct conflict with subtext",
            },
            {
                "question": "What does 'Gorky' mean and why did he choose this pen name?",
                "options": "It means 'happy' — he was optimistic; It means 'bitter' — reflecting his view of life; It means 'strong' — he was a bodybuilder; It was his mother's maiden name",
                "answer": "It means 'bitter' — reflecting his view of life",
            },
        ],
        key_name="Crisis of the old world",
    ),
    QuestStage(
        stage_number=5,
        period_id="silver_age",
        intro=(
            "🌙 Stage 5: The Silver Age\n\n"
            "You reach the final era — an explosion of poetry, philosophy, and artistic experimentation. "
            "Blok, Akhmatova, Mayakovsky, and others create entirely new literary movements.\n\n"
            "But the Russian Empire is collapsing. Revolution of 1905, World War I, and the "
            "revolutions of 1917 will end this world forever."
        ),
        author_ids=["blok", "akhmatova", "mayakovsky"],
        event_ids=["revolution_1905", "revolutions_1917"],
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
                "question": "What did the 1917 revolutions mean for the Silver Age?",
                "options": "They had no effect; They ended it; They started it; They improved it",
                "answer": "They ended it",
            },
        ],
        key_name="Search for a new language",
    ),
]
