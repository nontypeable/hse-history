TRANSLATIONS: dict[str, dict[str, str]] = {
    "en": {
        # Start / Menu
        "welcome": (
            "Welcome to an interactive guide to Russian literature "
            "of the 19th and early 20th centuries.\n\n"
            "Here you can travel from Pushkin to the Silver Age, "
            "learn how literature reflected Russian history, "
            "and test yourself with quizzes.\n\n"
            "Choose a section:"
        ),
        "menu_text": "Welcome to an interactive guide to Russian literature.\n\nChoose a section:",
        "fallback": "Please use the bot menu.",
        # Main menu buttons
        "menu_periods": "📚 Literary periods",
        "menu_authors": "👤 Writers and poets",
        "menu_events": "⚡ Events and context",
        "menu_achievements": "🏆 Literary achievements",
        "menu_quest": "🎮 Interactive quest",
        "menu_quiz": "🧠 Quiz",
        "menu_map": "🗺 Literary map",
        "menu_about": "ℹ️ About the project",
        "menu_language": "🌐 Language",
        # Navigation
        "back_main": "⬅️ Main Menu",
        "back_periods": "⬅️ Back to periods",
        "back_authors": "⬅️ Back to authors",
        "back_events": "⬅️ Back to events",
        "back_map": "⬅️ Back to map",
        "back_stage": "⬅️ Back to stage",
        # Periods
        "periods_title": "📚 Literary periods\n\nChoose a period to explore:",
        "period_authors": "👤 Authors of this period",
        "period_events": "⚡ Events of this period",
        "period_quiz": "📝 Mini-test",
        "period_not_found": "Period not found.",
        "period_historical_context": "📜 Historical context:",
        "period_achievements": "🏆 Key achievements:",
        "period_period_label": "Period:",
        # Authors
        "authors_title": "👤 Writers and poets\n\nChoose an author:",
        "author_not_found": "Author not found.",
        "author_life_years": "Life years:",
        "author_why_matter": "📌 Why they matter:",
        "author_achievement": "🏆 Main achievement:",
        "author_fact": "💡 Interesting fact:",
        "author_works_btn": "📖 Works",
        "author_context_btn": "🕰 Historical context",
        "author_question_btn": "❓ Question",
        "author_works_title": "📖 Main works by {name}:",
        "author_context_title": "🕰 Historical context for {name}:",
        "author_question_title": "❓ Question about {name}:",
        "author_answer_label": "💡 Answer:",
        # Events
        "events_title": "⚡ Events and context\n\nChoose an event:",
        "event_not_found": "Event not found.",
        "event_what_happened": "📋 What happened:",
        "event_why_matters": "📌 Why it matters:",
        "event_connection": "📚 Connection to literature:",
        "event_authors": "👤 Related authors:",
        "event_works": "📖 Related works:",
        "event_question_btn": "❓ Check question",
        "event_question_title": "❓ Check question:",
        "event_answer_label": "💡 Answer:",
        # Achievements
        "achievements_title": "🏆 Literary achievements\n\nChoose an achievement:",
        "achievement_not_found": "Achievement not found.",
        "achievement_explanation": "📖 Explanation:",
        "achievement_why_matters": "📌 Why it matters:",
        "achievement_authors": "👤 Related authors:",
        "achievement_works": "📖 Related works:",
        "achievement_context": "📜 Historical context:",
        # Map
        "map_title": "🗺 Literary map\n\nChoose a place:",
        "map_not_found": "Place not found.",
        "map_why_matters": "📌 Why it matters:",
        "map_authors": "👤 Related authors:",
        "map_value": "📜 Historical and cultural value:",
        # Quiz
        "quiz_start": "🧠 Quiz — Question {num} of {total}\n\n{question}",
        "quiz_already": "You are already in a quiz! Answer the current question.",
        "quiz_no_questions": "No quiz questions available.",
        "quiz_correct": "✅ Correct!",
        "quiz_wrong": "❌ Wrong!",
        "quiz_correct_answer": "\n\nCorrect answer: {num}",
        "quiz_explanation": "💡 {explanation}",
        "quiz_score": "Score: {score}/{total}",
        "quiz_next": "➡️ Next question",
        "quiz_result_title": "🧠 Quiz results!",
        "quiz_result_score": "You answered {score} out of {total} correctly.",
        "quiz_level_low": "You should review the material. 📚",
        "quiz_level_mid": "Not bad, but there are gaps. 📖",
        "quiz_level_high": "Excellent result! 🎓",
        "quiz_level_max": "Brilliant! You are almost a literary historian! 🏆",
        # Period quiz
        "period_quiz_title": "📝 Mini-quiz: {title}",
        "period_quiz_question": "Question {num} of {total}",
        "period_quiz_correct": "✅ Correct!",
        "period_quiz_wrong": "❌ Wrong!",
        "period_quiz_correct_answer": "\n\nCorrect answer: {answer}",
        "period_quiz_score": "You answered {score} out of {total} correctly.",
        "period_quiz_result_low": "You should review this period. 📚",
        "period_quiz_result_mid": "Not bad, but there are gaps. 📖",
        "period_quiz_result_high": "Excellent result! 🎓",
        "period_quiz_next": "➡️ Next question",
        # Quest
        "quest_intro": (
            "🎮 Interactive Quest: Journey through Literary Russia\n\n"
            "You are a student who enters literary Russia of the 19th and early 20th centuries.\n"
            "You must pass through 5 periods, meet authors, understand historical context, "
            "answer questions, and collect 5 'keys of the era'.\n\n"
            "Are you ready to begin?"
        ),
        "quest_start_btn": "🚀 Start quest",
        "quest_not_found": "Quest error. Please try again.",
        "quest_stage_not_found": "Stage not found.",
        "quest_key_received": '🔑 You received the key: "{era_key}"',
        "quest_keys_collected": "Keys collected:",
        "quest_complete": (
            "🎉 Congratulations!\n\n"
            "You have traveled from Pushkin to the Silver Age.\n\n"
            "Main conclusion:\n"
            "Russian literature of the 19th and early 20th centuries was not only an artistic "
            "phenomenon, but also a way of understanding Russian history: reforms, crises, "
            "public debates, and the search for national identity."
        ),
        "quest_receive_key": "🔑 Receive the era key",
        "quest_question_btn": "📝 Answer questions",
        "quest_next_question": "➡️ Next question",
        "quest_question": "📝 Question {num}:",
        "quest_correct": "✅ Correct!",
        "quest_wrong": "❌ Wrong!",
        "quest_correct_answer": "\n\nCorrect answer: {answer}",
        # About
        "about_text": (
            "ℹ️ About the project\n\n"
            "Our project is an interactive Telegram bot about Russian literature "
            "of the 19th and early 20th centuries.\n\n"
            "🎯 Goal:\n"
            "To show literature as part of Russia's historical development.\n\n"
            "📱 Why Telegram bot format:\n"
            "We chose the Telegram bot format because it makes learning interactive: "
            "the user does not simply read material, but chooses a path, answers questions, "
            "completes a quest, and sees connections between authors, works, and historical events.\n\n"
            "📚 Main features:\n"
            "• Literary periods (5 eras)\n"
            "• Writer and poet cards (25+ authors)\n"
            "• Events and historical context (11 events)\n"
            "• Literary achievements (8 cards)\n"
            "• Interactive quest with 5 stages\n"
            "• Quiz with 25 questions\n"
            "• Literary map (7 places)\n\n"
            "📖 Sources:\n"
            "• University course materials on Russian history\n"
            "• Academic reference materials on Russian literary history\n"
            "• Biographical materials about Russian writers\n"
            "• Works of Russian classical literature\n\n"
            "👥 Project team (25KNT6, HSE University):\n"
            "Andrey Sadkov, Anna Stanovova, Egor Runov, Bogdan Topilin"
        ),
        # Language
        "language_select": "🌐 Choose your language / Выберите язык:",
        "language_set_en": "Language set to English.",
        "language_set_ru": "Язык установлен: Русский.",
        # Error
        "error_generic": "Something went wrong. Please return to the main menu and try again.",
        "no_authors": "No authors found for this period.",
    },
    "ru": {
        # Start / Menu
        "welcome": (
            "Добро пожаловать в интерактивный путеводитель по русской литературе "
            "XIX и начала XX века.\n\n"
            "Здесь вы сможете пройти путь от Пушкина до Серебряного века, "
            "узнать, как литература отражала историю России, "
            "и проверить себя с помощью викторин.\n\n"
            "Выберите раздел:"
        ),
        "menu_text": "Добро пожаловать в интерактивный путеводитель по русской литературе.\n\nВыберите раздел:",
        "fallback": "Пожалуйста, используйте меню бота.",
        # Main menu buttons
        "menu_periods": "📚 Литературные эпохи",
        "menu_authors": "👤 Писатели и поэты",
        "menu_events": "⚡ События и контекст",
        "menu_achievements": "🏆 Литературные достижения",
        "menu_quest": "🎮 Интерактивный квест",
        "menu_quiz": "🧠 Викторина",
        "menu_map": "🗺 Литературная карта",
        "menu_about": "ℹ️ О проекте",
        "menu_language": "🌐 Язык",
        # Navigation
        "back_main": "⬅️ Главное меню",
        "back_periods": "⬅️ Назад к эпохам",
        "back_authors": "⬅️ Назад к авторам",
        "back_events": "⬅️ Назад к событиям",
        "back_map": "⬅️ Назад к карте",
        "back_stage": "⬅️ Назад к этапу",
        # Periods
        "periods_title": "📚 Литературные эпохи\n\nВыберите эпоху:",
        "period_authors": "👤 Авторы этой эпохи",
        "period_events": "⚡ События этой эпохи",
        "period_quiz": "📝 Мини-тест",
        "period_not_found": "Эпоха не найдена.",
        "period_historical_context": "📜 Исторический контекст:",
        "period_achievements": "🏆 Ключевые достижения:",
        "period_period_label": "Период:",
        # Authors
        "authors_title": "👤 Писатели и поэты\n\nВыберите автора:",
        "author_not_found": "Автор не найден.",
        "author_life_years": "Годы жизни:",
        "author_why_matter": "📌 Почему это важно:",
        "author_achievement": "🏆 Главное достижение:",
        "author_fact": "💡 Интересный факт:",
        "author_works_btn": "📖 Произведения",
        "author_context_btn": "🕰 Исторический контекст",
        "author_question_btn": "❓ Вопрос",
        "author_works_title": "📖 Главные произведения {name}:",
        "author_context_title": "🕰 Исторический контекст: {name}",
        "author_question_title": "❓ Вопрос о {name}:",
        "author_answer_label": "💡 Ответ:",
        # Events
        "events_title": "⚡ События и контекст\n\nВыберите событие:",
        "event_not_found": "Событие не найдено.",
        "event_what_happened": "📋 Что произошло:",
        "event_why_matters": "📌 Почему это важно:",
        "event_connection": "📚 Связь с литературой:",
        "event_authors": "👤 Связанные авторы:",
        "event_works": "📖 Связанные произведения:",
        "event_question_btn": "❓ Проверочный вопрос",
        "event_question_title": "❓ Проверочный вопрос:",
        "event_answer_label": "💡 Ответ:",
        # Achievements
        "achievements_title": "🏆 Литературные достижения\n\nВыберите достижение:",
        "achievement_not_found": "Достижение не найдено.",
        "achievement_explanation": "📖 Объяснение:",
        "achievement_why_matters": "📌 Почему это важно:",
        "achievement_authors": "👤 Связанные авторы:",
        "achievement_works": "📖 Связанные произведения:",
        "achievement_context": "📜 Исторический контекст:",
        # Map
        "map_title": "🗺 Литературная карта\n\nВыберите место:",
        "map_not_found": "Место не найдено.",
        "map_why_matters": "📌 Почему это важно:",
        "map_authors": "👤 Связанные авторы:",
        "map_value": "📜 Историческая и культурная ценность:",
        # Quiz
        "quiz_start": "🧠 Викторина — Вопрос {num} из {total}\n\n{question}",
        "quiz_already": "Вы уже в викторине! Ответьте на текущий вопрос.",
        "quiz_no_questions": "Вопросы для викторины недоступны.",
        "quiz_correct": "✅ Правильно!",
        "quiz_wrong": "❌ Неправильно!",
        "quiz_correct_answer": "\n\nПравильный ответ: {num}",
        "quiz_explanation": "💡 {explanation}",
        "quiz_score": "Счёт: {score}/{total}",
        "quiz_next": "➡️ Следующий вопрос",
        "quiz_result_title": "🧠 Результаты викторины!",
        "quiz_result_score": "Вы ответили правильно на {score} из {total} вопросов.",
        "quiz_level_low": "Стоит повторить материал. 📚",
        "quiz_level_mid": "Неплохо, но есть пробелы. 📖",
        "quiz_level_high": "Отличный результат! 🎓",
        "quiz_level_max": "Блестяще! Вы почти литературный историк! 🏆",
        # Period quiz
        "period_quiz_title": "📝 Мини-тест: {title}",
        "period_quiz_question": "Вопрос {num} из {total}",
        "period_quiz_correct": "✅ Правильно!",
        "period_quiz_wrong": "❌ Неправильно!",
        "period_quiz_correct_answer": "\n\nПравильный ответ: {answer}",
        "period_quiz_score": "Вы ответили правильно на {score} из {total} вопросов.",
        "period_quiz_result_low": "Стоит повторить материал этой эпохи. 📚",
        "period_quiz_result_mid": "Неплохо, но есть пробелы. 📖",
        "period_quiz_result_high": "Отличный результат! 🎓",
        "period_quiz_next": "➡️ Следующий вопрос",
        # Quest
        "quest_intro": (
            "🎮 Интерактивный квест: Путешествие по литературной России\n\n"
            "Вы — студент, который попадает в литературную Россию XIX и начала XX века.\n"
            "Вам нужно пройти через 5 эпох, встретить авторов, понять исторический контекст, "
            "ответить на вопросы и собрать 5 «ключей эпохи».\n\n"
            "Готовы начать?"
        ),
        "quest_start_btn": "🚀 Начать квест",
        "quest_not_found": "Ошибка квеста. Попробуйте снова.",
        "quest_stage_not_found": "Этап не найден.",
        "quest_key_received": '🔑 Вы получили ключ: "{era_key}"',
        "quest_keys_collected": "Собранные ключи:",
        "quest_complete": (
            "🎉 Поздравляем!\n\n"
            "Вы прошли путь от Пушкина до Серебряного века.\n\n"
            "Главный вывод:\n"
            "Русская литература XIX и начала XX века была не только художественным "
            "явлением, но и способом осмысления российской истории: реформ, кризисов, "
            "общественных дискуссий и поиска национальной идентичности."
        ),
        "quest_receive_key": "🔑 Получить ключ эпохи",
        "quest_question_btn": "📝 Ответить на вопросы",
        "quest_next_question": "➡️ Следующий вопрос",
        "quest_question": "📝 Вопрос {num}:",
        "quest_correct": "✅ Правильно!",
        "quest_wrong": "❌ Неправильно!",
        "quest_correct_answer": "\n\nПравильный ответ: {answer}",
        # About
        "about_text": (
            "ℹ️ О проекте\n\n"
            "Наш проект — интерактивный Telegram-бот о русской литературе "
            "XIX и начала XX века.\n\n"
            "🎯 Цель:\n"
            "Показать литературу как часть исторического развития России.\n\n"
            "📱 Почему формат Telegram-бота:\n"
            "Формат Telegram-бота делает обучение интерактивным: пользователь не просто "
            "читает материал, а выбирает путь, отвечает на вопросы, проходит квест "
            "и видит связи между авторами, произведениями и историческими событиями.\n\n"
            "📚 Основные возможности:\n"
            "• Литературные эпохи (5 эпох)\n"
            "• Карточки писателей и поэтов (25+ авторов)\n"
            "• События и исторический контекст (11 событий)\n"
            "• Литературные достижения (8 карточек)\n"
            "• Интерактивный квест с 5 этапами\n"
            "• Викторина с 25 вопросами\n"
            "• Литературная карта (7 мест)\n\n"
            "📖 Источники:\n"
            "• Учебные материалы по истории России\n"
            "• Академические справочники по истории русской литературы\n"
            "• Биографические материалы о русских писателях\n"
            "• Произведения русской классической литературы\n\n"
            "👥 Команда проекта (25КНТ6, НИУ ВШЭ):\n"
            "Садков Андрей, Становова Анна, Рунов Егор, Топилин Богдан"
        ),
        # Language
        "language_select": "🌐 Выберите язык / Choose your language:",
        "language_set_en": "Language set to English.",
        "language_set_ru": "Язык установлен: Русский.",
        # Error
        "error_generic": "Что-то пошло не так. Вернитесь в главное меню и попробуйте снова.",
        "no_authors": "Авторы этой эпохи не найдены.",
    },
}

DEFAULT_LANG = "ru"


def t(key: str, lang: str = DEFAULT_LANG) -> str:
    """Translate a UI string key to the given language, falling back to English."""
    translations = TRANSLATIONS.get(lang, TRANSLATIONS["en"])
    value = translations.get(key)
    if value is not None:
        return value
    # Fallback to English
    return TRANSLATIONS["en"].get(key, key)


def tf(key: str, lang: str = DEFAULT_LANG, **kwargs: str) -> str:
    """Translate a UI string with format variables."""
    template = t(key, lang)
    try:
        return template.format(**kwargs)
    except KeyError:
        return template
