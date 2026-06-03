import logging

from telegram import Update
from telegram.ext import Application, CallbackContext, CallbackQueryHandler

from bot.infrastructure.i18n import DEFAULT_LANG, t, tf
from bot.presentation.helpers import get_services
from bot.presentation.keyboards import main_menu_kb, quiz_answer_kb, quiz_next_kb, quiz_result_kb

logger = logging.getLogger(__name__)


async def on_quiz_start(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user_id = query.from_user.id
    ud = context.user_data

    if ud.get("in_quiz"):
        lang = ud.get("lang", DEFAULT_LANG)
        await query.answer(t("quiz_already", lang))
        return

    async with get_services(context, user_id) as svc:
        questions = svc.quiz_service.get_questions(svc.lang)
        if not questions:
            await query.edit_message_text(t("quiz_no_questions", svc.lang), reply_markup=main_menu_kb(svc.lang))
            await query.answer()
            return

        ud["in_quiz"] = True
        ud["quiz_current"] = 0
        ud["quiz_score"] = 0
        ud["quiz_total"] = len(questions)

        first_q = questions[0]
        question_text = tf("quiz_start", svc.lang, num="1", total=str(len(questions)), question=first_q["question"])
        await query.edit_message_text(
            question_text,
            reply_markup=quiz_answer_kb(first_q["id"], first_q["options"]),
        )

    await query.answer()


async def on_quiz_answer(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user_id = query.from_user.id
    ud = context.user_data

    if not ud.get("in_quiz"):
        await query.answer()
        return

    parts = query.data.split(":")
    question_id = int(parts[1])
    answer_index = int(parts[2])
    current_idx = ud.get("quiz_current", 0)
    score = ud.get("quiz_score", 0)

    async with get_services(context, user_id) as svc:
        result = svc.quiz_service.check_answer(question_id, answer_index, svc.lang)
        if "error" in result:
            await query.answer(t("error_generic", svc.lang))
            return

        is_correct = result["is_correct"]
        new_score = score + (1 if is_correct else 0)
        ud["quiz_score"] = new_score

        emoji = t("quiz_correct", svc.lang) if is_correct else t("quiz_wrong", svc.lang)
        correct_text = "" if is_correct else tf("quiz_correct_answer", svc.lang, num=str(result["correct_index"] + 1))

        score_text = tf("quiz_score", svc.lang, score=str(new_score), total=str(current_idx + 1))
        explanation = tf("quiz_explanation", svc.lang, explanation=result["explanation"])
        text = f"{emoji}{correct_text}\n\n{explanation}\n\n{score_text}"
        await query.edit_message_text(text, reply_markup=quiz_next_kb(question_id, svc.lang))

    await query.answer()


async def on_quiz_next(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user_id = query.from_user.id
    ud = context.user_data

    if not ud.get("in_quiz"):
        await query.answer()
        return

    current_idx = ud.get("quiz_current", 0)
    score = ud.get("quiz_score", 0)

    async with get_services(context, user_id) as svc:
        questions = svc.quiz_service.get_questions(svc.lang)
        next_idx = current_idx + 1

        if next_idx >= len(questions):
            result_text = svc.quiz_service.get_result_text(score, len(questions), svc.lang)
            await svc.quiz_service.save_result(user_id, score, len(questions), svc.lang)
            ud.pop("in_quiz", None)
            ud.pop("quiz_current", None)
            ud.pop("quiz_score", None)
            ud.pop("quiz_total", None)
            await query.edit_message_text(result_text, reply_markup=quiz_result_kb(svc.lang))
            await query.answer()
            return

        ud["quiz_current"] = next_idx
        q = questions[next_idx]
        question_text = tf(
            "quiz_start", svc.lang, num=str(next_idx + 1), total=str(len(questions)), question=q["question"]
        )
        await query.edit_message_text(
            question_text,
            reply_markup=quiz_answer_kb(q["id"], q["options"]),
        )

    await query.answer()


def register(app: Application) -> None:
    app.add_handler(CallbackQueryHandler(on_quiz_start, pattern=r"^quiz_start$"))
    app.add_handler(CallbackQueryHandler(on_quiz_answer, pattern=r"^quiz_a:"))
    app.add_handler(CallbackQueryHandler(on_quiz_next, pattern=r"^quiz_next:"))
