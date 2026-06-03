from bot.domain.entities import Achievement, Author, Event, MapPlace, Period, QuestStage, QuizQuestion
from bot.infrastructure.content.en import (
    ACHIEVEMENTS as ACHIEVEMENTS_EN,
)
from bot.infrastructure.content.en import (
    AUTHORS as AUTHORS_EN,
)
from bot.infrastructure.content.en import (
    EVENTS as EVENTS_EN,
)
from bot.infrastructure.content.en import (
    MAP_PLACES as MAP_PLACES_EN,
)
from bot.infrastructure.content.en import (
    PERIODS as PERIODS_EN,
)
from bot.infrastructure.content.en import (
    QUEST_STAGES as QUEST_STAGES_EN,
)
from bot.infrastructure.content.en import (
    QUIZ_QUESTIONS as QUIZ_QUESTIONS_EN,
)

# Backward-compatible aliases (defaults to English)
AUTHORS = AUTHORS_EN
PERIODS = PERIODS_EN
EVENTS = EVENTS_EN
ACHIEVEMENTS = ACHIEVEMENTS_EN
MAP_PLACES = MAP_PLACES_EN
QUIZ_QUESTIONS = QUIZ_QUESTIONS_EN
QUEST_STAGES = QUEST_STAGES_EN


def get_authors(lang: str = "en") -> dict[str, Author]:
    if lang == "ru":
        from bot.infrastructure.content.ru import AUTHORS as AUTHORS_RU

        return AUTHORS_RU
    return AUTHORS_EN


def get_periods(lang: str = "en") -> dict[str, Period]:
    if lang == "ru":
        from bot.infrastructure.content.ru import PERIODS as PERIODS_RU

        return PERIODS_RU
    return PERIODS_EN


def get_events(lang: str = "en") -> dict[str, Event]:
    if lang == "ru":
        from bot.infrastructure.content.ru import EVENTS as EVENTS_RU

        return EVENTS_RU
    return EVENTS_EN


def get_achievements(lang: str = "en") -> dict[str, Achievement]:
    if lang == "ru":
        from bot.infrastructure.content.ru import ACHIEVEMENTS as ACHIEVEMENTS_RU

        return ACHIEVEMENTS_RU
    return ACHIEVEMENTS_EN


def get_map_places(lang: str = "en") -> dict[str, MapPlace]:
    if lang == "ru":
        from bot.infrastructure.content.ru import MAP_PLACES as MAP_PLACES_RU

        return MAP_PLACES_RU
    return MAP_PLACES_EN


def get_quiz_questions(lang: str = "en") -> list[QuizQuestion]:
    if lang == "ru":
        from bot.infrastructure.content.ru import QUIZ_QUESTIONS as QUIZ_QUESTIONS_RU

        return QUIZ_QUESTIONS_RU
    return QUIZ_QUESTIONS_EN


def get_quest_stages(lang: str = "en") -> list[QuestStage]:
    if lang == "ru":
        from bot.infrastructure.content.ru import QUEST_STAGES as QUEST_STAGES_RU

        return QUEST_STAGES_RU
    return QUEST_STAGES_EN


__all__ = [
    "ACHIEVEMENTS",
    "AUTHORS",
    "EVENTS",
    "MAP_PLACES",
    "PERIODS",
    "QUEST_STAGES",
    "QUIZ_QUESTIONS",
    "get_achievements",
    "get_authors",
    "get_events",
    "get_map_places",
    "get_periods",
    "get_quest_stages",
    "get_quiz_questions",
]
