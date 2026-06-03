from dataclasses import dataclass


@dataclass(frozen=True)
class AuthorCard:
    id: str
    name: str
    life_years: str
    period_id: str
    who_they_were: str
    why_they_matter: str
    historical_context: str
    main_works: list[str]
    main_achievement: str
    interesting_fact: str
    mini_question: str
    mini_answer: str


@dataclass(frozen=True)
class PeriodCard:
    id: str
    emoji: str
    title: str
    period: str
    description: str
    historical_context: str
    author_ids: list[str]
    event_ids: list[str]
    achievements: list[str]


@dataclass(frozen=True)
class EventCard:
    id: str
    date: str
    title: str
    what_happened: str
    why_it_matters: str
    connection_to_literature: str
    related_author_ids: list[str]
    related_works: list[str]
    check_question: str
    check_answer: str


@dataclass(frozen=True)
class AchievementCard:
    id: str
    emoji: str
    title: str
    explanation: str
    why_it_matters: str
    related_author_ids: list[str]
    related_works: list[str]
    historical_context: str


@dataclass(frozen=True)
class MapPlaceCard:
    id: str
    name: str
    why_it_matters: str
    related_author_ids: list[str]
    historical_value: str


@dataclass(frozen=True)
class QuizResultDTO:
    score: int
    total: int
    level: str


@dataclass(frozen=True)
class QuestProgressDTO:
    current_stage: int
    completed_stages: list[int]
    collected_keys: list[str]
    is_completed: bool


@dataclass(frozen=True)
class QuestStageDTO:
    stage_number: int
    period_id: str
    intro: str
    key_name: str
