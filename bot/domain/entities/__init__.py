from dataclasses import dataclass, field


@dataclass(frozen=True)
class Author:
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
    map_places: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class Period:
    id: str
    emoji: str
    title: str
    period: str
    description: str
    historical_context: str
    author_ids: list[str]
    event_ids: list[str]
    achievements: list[str]
    questions: list[dict[str, str]]


@dataclass(frozen=True)
class Event:
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
class Achievement:
    id: str
    emoji: str
    title: str
    explanation: str
    why_it_matters: str
    related_author_ids: list[str]
    related_works: list[str]
    historical_context: str


@dataclass(frozen=True)
class MapPlace:
    id: str
    name: str
    why_it_matters: str
    related_author_ids: list[str]
    historical_value: str


@dataclass(frozen=True)
class QuizQuestion:
    id: int
    question: str
    options: list[str]
    correct_index: int
    explanation: str


@dataclass(frozen=True)
class QuestStage:
    stage_number: int
    period_id: str
    intro: str
    author_ids: list[str]
    event_ids: list[str]
    questions: list[dict[str, str]]
    key_name: str
