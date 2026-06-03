from typing import Any

from bot.application.dto import QuestProgressDTO, QuestStageDTO
from bot.infrastructure.content import get_quest_stages
from bot.infrastructure.i18n import DEFAULT_LANG, t
from bot.infrastructure.repositories import QuestProgressRepository


class QuestService:
    def __init__(self, quest_progress_repo: QuestProgressRepository) -> None:
        self._quest_progress_repo = quest_progress_repo

    def get_stages(self, lang: str = DEFAULT_LANG) -> list[QuestStageDTO]:
        stages = get_quest_stages(lang)
        return [
            QuestStageDTO(
                stage_number=s.stage_number,
                period_id=s.period_id,
                intro=s.intro,
                key_name=s.key_name,
            )
            for s in stages
        ]

    def get_stage(self, stage_number: int, lang: str = DEFAULT_LANG) -> dict[str, Any] | None:
        stages = get_quest_stages(lang)
        for stage in stages:
            if stage.stage_number == stage_number:
                return {
                    "stage_number": stage.stage_number,
                    "period_id": stage.period_id,
                    "intro": stage.intro,
                    "author_ids": stage.author_ids,
                    "event_ids": stage.event_ids,
                    "questions": stage.questions,
                    "key_name": stage.key_name,
                }
        return None

    def get_total_stages(self, lang: str = DEFAULT_LANG) -> int:
        return len(get_quest_stages(lang))

    def check_stage_answer(
        self, stage_number: int, question_index: int, answer: str, lang: str = DEFAULT_LANG
    ) -> dict[str, Any]:
        stage = self.get_stage(stage_number, lang)
        if stage is None:
            return {"error": "stage_not_found"}
        questions = stage["questions"]
        if question_index >= len(questions):
            return {"error": "question_not_found"}
        question = questions[question_index]
        options_list = [o.strip() for o in question["options"].split(";")]
        correct = question["answer"]
        is_correct = answer.strip() == correct.strip()
        return {
            "is_correct": is_correct,
            "correct_answer": correct,
            "options": options_list,
        }

    async def get_progress(self, user_id: int) -> QuestProgressDTO:
        progress = await self._quest_progress_repo.get_progress(user_id)
        if progress is None:
            return QuestProgressDTO(
                current_stage=1,
                completed_stages=[],
                collected_keys=[],
                is_completed=False,
            )
        parsed = self._quest_progress_repo.parse_progress(progress)
        return QuestProgressDTO(
            current_stage=parsed["current_stage"],
            completed_stages=parsed["completed_stages"],
            collected_keys=parsed["collected_keys"],
            is_completed=parsed["is_completed"],
        )

    async def complete_stage(self, user_id: int, stage_number: int, key_name: str) -> QuestProgressDTO:
        progress_dto = await self.get_progress(user_id)
        completed = list(progress_dto.completed_stages)
        keys = list(progress_dto.collected_keys)

        if stage_number not in completed:
            completed.append(stage_number)
            keys.append(key_name)

        total_stages = self.get_total_stages()
        is_completed = len(completed) == total_stages
        next_stage = min(stage_number + 1, total_stages) if not is_completed else total_stages

        await self._quest_progress_repo.update_progress(
            user_id=user_id,
            current_stage=next_stage,
            completed_stages=completed,
            collected_keys=keys,
            is_completed=is_completed,
        )

        return QuestProgressDTO(
            current_stage=next_stage,
            completed_stages=completed,
            collected_keys=keys,
            is_completed=is_completed,
        )

    async def start_quest(self, user_id: int) -> QuestProgressDTO:
        progress = await self._quest_progress_repo.get_or_create(user_id)
        parsed = self._quest_progress_repo.parse_progress(progress)
        return QuestProgressDTO(
            current_stage=parsed["current_stage"],
            completed_stages=parsed["completed_stages"],
            collected_keys=parsed["collected_keys"],
            is_completed=parsed["is_completed"],
        )

    def get_completion_message(self, collected_keys: list[str], lang: str = DEFAULT_LANG) -> str:
        keys_text = "\n".join(f"  🔑 {key}" for key in collected_keys)
        completion = t("quest_complete", lang)
        key_received = t("quest_keys_collected", lang)
        return f"{completion}\n\n{key_received}\n{keys_text}"
