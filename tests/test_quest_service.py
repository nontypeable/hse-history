import json

import pytest

from bot.application.services.quest_service import QuestService


class MockQuestProgressRepository:
    def __init__(self) -> None:
        self.progress: dict[int, dict] = {}

    async def get_or_create(self, user_id: int) -> object:
        if user_id not in self.progress:
            self.progress[user_id] = {
                "current_stage": 1,
                "completed_stages": "[]",
                "collected_keys": "[]",
                "is_completed": False,
            }
        return self

    async def update_progress(
        self,
        user_id: int,
        current_stage: int,
        completed_stages: list[int],
        collected_keys: list[str],
        is_completed: bool,
    ) -> object:
        self.progress[user_id] = {
            "current_stage": current_stage,
            "completed_stages": json.dumps(completed_stages),
            "collected_keys": json.dumps(collected_keys),
            "is_completed": is_completed,
        }
        return self

    async def get_progress(self, user_id: int) -> object | None:
        if user_id not in self.progress:
            return None
        return self

    def parse_progress(self, progress: object) -> dict:
        user_id = 1
        data = self.progress.get(user_id, {})
        if not data:
            return {"current_stage": 1, "completed_stages": [], "collected_keys": [], "is_completed": False}
        return {
            "current_stage": data["current_stage"],
            "completed_stages": (
                json.loads(data["completed_stages"])
                if isinstance(data["completed_stages"], str)
                else data["completed_stages"]
            ),
            "collected_keys": (
                json.loads(data["collected_keys"])
                if isinstance(data["collected_keys"], str)
                else data["collected_keys"]
            ),
            "is_completed": data["is_completed"],
        }


@pytest.fixture
def quest_service() -> QuestService:
    return QuestService(MockQuestProgressRepository())


class TestQuestService:
    def test_get_stages(self, quest_service: QuestService) -> None:
        stages = quest_service.get_stages("en")
        assert len(stages) == 5

    def test_get_stage(self, quest_service: QuestService) -> None:
        stage = quest_service.get_stage(1, "en")
        assert stage is not None
        assert stage["period_id"] == "golden_age"
        assert stage["key_name"] == "Freedom and personality"

    def test_get_missing_stage(self, quest_service: QuestService) -> None:
        stage = quest_service.get_stage(99, "en")
        assert stage is None

    def test_total_stages(self, quest_service: QuestService) -> None:
        assert quest_service.get_total_stages() == 5

    def test_check_stage_answer(self, quest_service: QuestService) -> None:
        result = quest_service.check_stage_answer(1, 0, "He created the modern Russian literary language", "en")
        assert "is_correct" in result

    def test_check_stage_answer_wrong(self, quest_service: QuestService) -> None:
        result = quest_service.check_stage_answer(1, 0, "Wrong answer", "en")
        assert result["is_correct"] is False

    @pytest.mark.asyncio
    async def test_start_quest(self, quest_service: QuestService) -> None:
        progress = await quest_service.start_quest(1)
        assert progress.current_stage == 1
        assert progress.is_completed is False

    @pytest.mark.asyncio
    async def test_complete_stage(self, quest_service: QuestService) -> None:
        progress = await quest_service.complete_stage(1, 1, "Freedom and personality")
        assert 1 in progress.completed_stages
        assert "Freedom and personality" in progress.collected_keys

    @pytest.mark.asyncio
    async def test_completion_message(self, quest_service: QuestService) -> None:
        keys = ["Freedom and personality", "Society and the people"]
        msg = quest_service.get_completion_message(keys, "en")
        assert "Freedom and personality" in msg
        assert "congratulations" in msg.lower()
