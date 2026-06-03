from typing import TYPE_CHECKING, Any

from bot.application.dto import QuizResultDTO
from bot.infrastructure.content import get_quiz_questions
from bot.infrastructure.i18n import DEFAULT_LANG, t

if TYPE_CHECKING:
    from bot.infrastructure.repositories import QuizResultRepository


class QuizService:
    def __init__(self, quiz_result_repo: QuizResultRepository) -> None:
        self._quiz_result_repo = quiz_result_repo

    def get_questions(self, lang: str = DEFAULT_LANG) -> list[dict[str, Any]]:
        questions = get_quiz_questions(lang)
        return [
            {
                "id": q.id,
                "question": q.question,
                "options": q.options,
                "correct_index": q.correct_index,
                "explanation": q.explanation,
            }
            for q in questions
        ]

    def check_answer(self, question_id: int, answer_index: int, lang: str = DEFAULT_LANG) -> dict[str, Any]:
        questions = get_quiz_questions(lang)
        question = next((q for q in questions if q.id == question_id), None)
        if question is None:
            return {"error": "question_not_found"}
        is_correct = answer_index == question.correct_index
        return {
            "is_correct": is_correct,
            "correct_index": question.correct_index,
            "explanation": question.explanation,
        }

    def get_result_text(self, score: int, total: int, lang: str = DEFAULT_LANG) -> str:
        level = self._get_level(score, total, lang)
        result_title = t("quiz_result_title", lang)
        result_score = t("quiz_result_score", lang).format(score=score, total=total)
        return f"{result_title}\n\n{result_score}\n\n{level}"

    def _get_level(self, score: int, total: int, lang: str = DEFAULT_LANG) -> str:
        if total == 0:
            return t("quiz_level_low", lang)
        pct = score / total
        if pct <= 0.28:
            return t("quiz_level_low", lang)
        if pct <= 0.52:
            return t("quiz_level_mid", lang)
        if pct <= 0.72:
            return t("quiz_level_high", lang)
        return t("quiz_level_max", lang)

    async def save_result(self, user_id: int, score: int, total: int, lang: str = DEFAULT_LANG) -> QuizResultDTO:
        await self._quiz_result_repo.save(user_id, score, total)
        level = self._get_level(score, total, lang)
        return QuizResultDTO(score=score, total=total, level=level)
