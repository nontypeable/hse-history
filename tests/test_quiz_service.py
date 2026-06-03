import pytest

from bot.application.services.quiz_service import QuizService


class MockQuizResultRepository:
    def __init__(self) -> None:
        self.saved: list[dict] = []

    async def save(self, user_id: int, score: int, total: int) -> object:
        self.saved.append({"user_id": user_id, "score": score, "total": total})
        return object()

    async def get_best(self, user_id: int) -> None:
        return None


@pytest.fixture
def quiz_service() -> QuizService:
    return QuizService(MockQuizResultRepository())


class TestQuizService:
    def test_get_questions(self, quiz_service: QuizService) -> None:
        questions = quiz_service.get_questions("en")
        assert len(questions) >= 20
        for q in questions:
            assert "question" in q
            assert "options" in q
            assert len(q["options"]) >= 2
            assert "correct_index" in q

    def test_check_correct_answer(self, quiz_service: QuizService) -> None:
        result = quiz_service.check_answer(1, 1, "en")
        assert result["is_correct"] is True
        assert "explanation" in result

    def test_check_wrong_answer(self, quiz_service: QuizService) -> None:
        result = quiz_service.check_answer(1, 0, "en")
        assert result["is_correct"] is False
        assert result["correct_index"] == 1

    def test_check_missing_question(self, quiz_service: QuizService) -> None:
        result = quiz_service.check_answer(999, 0, "en")
        assert "error" in result

    def test_score_calculation(self, quiz_service: QuizService) -> None:
        text_low = quiz_service.get_result_text(5, 25, "en")
        assert "review" in text_low.lower()

        text_mid = quiz_service.get_result_text(10, 25, "en")
        assert "gap" in text_mid.lower() or "not bad" in text_mid.lower()

        text_high = quiz_service.get_result_text(20, 25, "en")
        assert "excellent" in text_high.lower() or "brilliant" in text_high.lower()

    def test_final_result_levels(self, quiz_service: QuizService) -> None:
        assert "review" in quiz_service.get_result_text(5, 25, "en").lower()
        assert "not bad" in quiz_service.get_result_text(10, 25, "en").lower()
        assert "excellent" in quiz_service.get_result_text(17, 25, "en").lower()
        assert "brilliant" in quiz_service.get_result_text(20, 25, "en").lower()

    @pytest.mark.asyncio
    async def test_save_result(self, quiz_service: QuizService) -> None:
        result = await quiz_service.save_result(123, 15, 25, "en")
        assert result.score == 15
        assert result.total == 25
        assert "excellent" in result.level.lower() or "brilliant" in result.level.lower()
