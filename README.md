# Russian Literature History Bot

Interactive Telegram bot about Russian literature of the 19th and early 20th centuries: people, events, achievements.

## Topic

"Russian Literature of the 19th and early 20th centuries: people, events, achievements"

## Goal

Create an interactive educational Telegram bot that helps users study Russian literature through authors, works, historical events, cultural context, literary achievements, quizzes, and an interactive quest.

## Why Telegram Bot Format

The Telegram bot format makes learning interactive: the user does not simply read material, but chooses a path, answers questions, completes a quest, and sees connections between authors, works, and historical events.

## Bot Features

- **📚 Literary periods** — 5 periods from the Golden Age to the Silver Age
- **👤 Writers and poets** — 25+ author cards with biographical details, works, and interesting facts
- **⚡ Events and context** — 11 historical events with literary connections
- **🏆 Literary achievements** — 8 achievement cards explaining key literary innovations
- **🎮 Interactive quest** — "Journey through Literary Russia" with 5 stages, author encounters, and era keys
- **🧠 Quiz** — 25 questions with scoring and result levels
- **🗺 Literary map** — 7 literary places with connected authors
- **ℹ️ About the project** — project description and sources

## Project Structure

```
literature-history-bot/
├── bot/
│   ├── main.py              # Entry point
│   ├── config.py            # Pydantic settings
│   ├── container.py         # DI container
│   ├── presentation/
│   │   ├── handlers/        # PTB handlers
│   │   └── keyboards/       # Inline keyboards
│   ├── application/
│   │   ├── services/        # Business logic
│   │   └── dto/             # Data transfer objects
│   ├── domain/
│   │   └── entities/        # Domain entities
│   └── infrastructure/
│       ├── database/         # SQLAlchemy models
│       ├── repositories/    # Database repositories
│       └── content/          # Static educational content
├── tests/
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

## Technologies

- Python 3.14
- python-telegram-bot (Telegram Bot API)
- SQLite + SQLAlchemy 2.x async
- pydantic-settings
- uv (package manager)
- Docker / docker-compose
- ruff, mypy, pytest

## Local Setup

1. Install uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Clone the repository and enter the directory
3. Copy `.env.example` to `.env` and set `BOT_TOKEN`
4. Install dependencies: `uv sync`
5. Run the bot: `uv run bot`

## .env Setup

```
BOT_TOKEN=your_telegram_bot_token_here
DATABASE_URL=sqlite+aiosqlite:///./data/bot.db
LOG_LEVEL=INFO
```

## Docker Setup

```bash
docker-compose up -d
```

## Test Commands

```bash
uv run pytest
uv run ruff check .
uv run ruff format .
uv run mypy bot
```

## How to Use the Bot

1. Send `/start` to the bot
2. Use inline buttons to navigate sections
3. Each section has "Back" and "Main Menu" buttons
4. Try the interactive quest for a guided experience
5. Take the quiz to test your knowledge

## Defense Demo Scenario

1. Run `/start` — show the main menu
2. Open "📚 Literary periods"
3. Choose "🌅 Golden Age of Russian literature"
4. Show Pushkin's author card
5. Show the connection with the War of 1812 and Decembrists
6. Start the interactive quest
7. Answer 1-2 questions
8. Show receiving an era key
9. Start the final quiz
10. Show "ℹ️ About project" and sources

## Educational Value

- Literature is presented as part of historical development, not in isolation
- Each author, event, and achievement is connected to its historical context
- The interactive quest forces users to actively engage with the material
- The quiz tests retention and understanding
- The literary map shows physical connections between places and writers

## Sources

- University course materials on Russian history
- Academic reference materials on Russian literary history
- Biographical materials about Russian writers
- Works of Russian classical literature

## Possible Improvements

- Add more authors and events
- Add images and media
- Implement user progress tracking across sessions
- Add difficulty levels for the quiz
- Create a web dashboard for teachers
- Add multilingual support