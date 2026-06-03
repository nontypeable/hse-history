from dataclasses import dataclass


@dataclass(frozen=True)
class QuizResultData:
    score: int
    total: int
    level: str


@dataclass(frozen=True)
class QuestProgressData:
    current_stage: int
    completed_stages: list[int]
    collected_keys: list[str]
    is_completed: bool
