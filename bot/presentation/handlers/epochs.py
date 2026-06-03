import logging

from telegram import Update
from telegram.ext import Application, CallbackContext, CallbackQueryHandler

from bot.infrastructure.i18n import t, tf
from bot.presentation.helpers import get_services
from bot.presentation.keyboards import (
    authors_list_kb,
    back_to_main_kb,
    events_list_kb,
    period_detail_kb,
    period_quiz_answer_kb,
    period_quiz_next_kb,
    period_quiz_result_kb,
    periods_kb,
)

logger = logging.getLogger(__name__)


async def on_period(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    period_id = query.data.split(":")[1]
    user_id = query.from_user.id

    async with get_services(context, user_id) as svc:
        if period_id != "list":
            period_card = svc.content_service.get_period(period_id, svc.lang)
            if period_card is None:
                await query.edit_message_text(t("period_not_found", svc.lang))
                await query.answer()
                return
            achievements_text = "\n".join(f"  • {a}" for a in period_card.achievements)
            text = (
                f"{period_card.emoji} {period_card.title}\n"
                f"{t('period_period_label', svc.lang)} {period_card.period}\n\n"
                f"{period_card.description}\n\n"
                f"{t('period_historical_context', svc.lang)}\n{period_card.historical_context}\n\n"
                f"{t('period_achievements', svc.lang)}\n{achievements_text}"
            )
            await query.edit_message_text(text, reply_markup=period_detail_kb(period_card.id, svc.lang))
        else:
            periods = svc.content_service.get_all_periods(svc.lang)
            period_dicts = [{"id": p.id, "emoji": p.emoji, "title": p.title} for p in periods]
            await query.edit_message_text(
                t("periods_title", svc.lang),
                reply_markup=periods_kb(period_dicts, svc.lang),
            )

    await query.answer()


async def on_period_authors(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    period_id = query.data.split(":")[1]
    user_id = query.from_user.id

    async with get_services(context, user_id) as svc:
        authors = svc.content_service.get_authors_by_period(period_id, svc.lang)
        if not authors:
            await query.edit_message_text(t("no_authors", svc.lang))
            await query.answer()
            return
        author_dicts = [{"id": a.id, "name": a.name, "life_years": a.life_years} for a in authors]
        await query.edit_message_text(
            t("period_authors", svc.lang),
            reply_markup=authors_list_kb(author_dicts, svc.lang),
        )

    await query.answer()


async def on_period_events(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    period_id = query.data.split(":")[1]
    user_id = query.from_user.id

    async with get_services(context, user_id) as svc:
        period_card = svc.content_service.get_period(period_id, svc.lang)
        if period_card is None:
            await query.edit_message_text(t("period_not_found", svc.lang))
            await query.answer()
            return

        from bot.infrastructure.content import get_events

        events = get_events(svc.lang)
        event_dicts = []
        for eid in period_card.event_ids:
            event = events.get(eid)
            if event:
                event_dicts.append({"id": event.id, "date": event.date, "title": event.title})
        await query.edit_message_text(
            t("period_events", svc.lang),
            reply_markup=events_list_kb(event_dicts, svc.lang),
        )

    await query.answer()


async def on_period_quiz(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    period_id = query.data.split(":")[1]
    user_id = query.from_user.id

    async with get_services(context, user_id) as svc:
        period = svc.content_service.get_period(period_id, svc.lang)
        if period is None:
            await query.edit_message_text(t("period_not_found", svc.lang))
            await query.answer()
            return

        if not period.questions:
            await query.edit_message_text(t("quiz_no_questions", svc.lang), reply_markup=back_to_main_kb(svc.lang))
            await query.answer()
            return

        context.user_data["pq_in_quiz"] = True
        context.user_data["pq_period_id"] = period_id
        context.user_data["pq_current"] = 0
        context.user_data["pq_score"] = 0

        first_q = period.questions[0]
        options = [o.strip() for o in first_q["options"].split(";")]
        question_text = (
            tf("period_quiz_title", svc.lang, title=f"{period.emoji} {period.title}")
            + "\n\n"
            + tf("period_quiz_question", svc.lang, num="1", total=str(len(period.questions)))
            + f"\n\n{first_q['question']}"
        )
        await query.edit_message_text(
            question_text,
            reply_markup=period_quiz_answer_kb(period_id, 0, options),
        )

    await query.answer()


async def on_period_quiz_answer(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user_id = query.from_user.id
    ud = context.user_data

    if not ud.get("pq_in_quiz"):
        await query.answer()
        return

    parts = query.data.split(":")
    period_id = parts[1]
    q_idx = int(parts[2])
    option_idx = int(parts[3])

    async with get_services(context, user_id) as svc:
        period = svc.content_service.get_period(period_id, svc.lang)
        if period is None or q_idx >= len(period.questions):
            await query.answer(t("error_generic", svc.lang))
            return

        question = period.questions[q_idx]
        options = [o.strip() for o in question["options"].split(";")]
        user_answer = options[option_idx] if option_idx < len(options) else ""
        correct_answer = question["answer"]
        is_correct = user_answer.strip() == correct_answer.strip()

        score = ud.get("pq_score", 0)
        new_score = score + (1 if is_correct else 0)
        ud["pq_score"] = new_score

        emoji = t("period_quiz_correct", svc.lang) if is_correct else t("period_quiz_wrong", svc.lang)
        correct_info = "" if is_correct else tf("period_quiz_correct_answer", svc.lang, answer=correct_answer)
        text = f"{emoji}{correct_info}"
        await query.edit_message_text(
            text,
            reply_markup=period_quiz_next_kb(period_id, q_idx, svc.lang),
        )

    await query.answer()


async def on_period_quiz_next(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user_id = query.from_user.id
    ud = context.user_data

    if not ud.get("pq_in_quiz"):
        await query.answer()
        return

    parts = query.data.split(":")
    period_id = parts[1]
    current_idx = int(parts[2])

    async with get_services(context, user_id) as svc:
        period = svc.content_service.get_period(period_id, svc.lang)
        if period is None:
            await query.edit_message_text(t("period_not_found", svc.lang), reply_markup=back_to_main_kb(svc.lang))
            await query.answer()
            return

        next_idx = current_idx + 1
        score = ud.get("pq_score", 0)
        total = len(period.questions)

        if next_idx >= total:
            pct = score / total if total else 0
            if pct <= 0.4:
                level = t("period_quiz_result_low", svc.lang)
            elif pct <= 0.7:
                level = t("period_quiz_result_mid", svc.lang)
            else:
                level = t("period_quiz_result_high", svc.lang)

            result_title = tf("period_quiz_title", svc.lang, title=f"{period.emoji} {period.title}")
            result_score = tf("period_quiz_score", svc.lang, score=str(score), total=str(total))
            text = f"{result_title}\n\n{result_score}\n\n{level}"

            ud.pop("pq_in_quiz", None)
            ud.pop("pq_period_id", None)
            ud.pop("pq_current", None)
            ud.pop("pq_score", None)

            await query.edit_message_text(text, reply_markup=period_quiz_result_kb(period_id, svc.lang))
            await query.answer()
            return

        ud["pq_current"] = next_idx
        q = period.questions[next_idx]
        options = [o.strip() for o in q["options"].split(";")]
        question_text = (
            tf("period_quiz_title", svc.lang, title=f"{period.emoji} {period.title}")
            + "\n\n"
            + tf("period_quiz_question", svc.lang, num=str(next_idx + 1), total=str(total))
            + f"\n\n{q['question']}"
        )
        await query.edit_message_text(
            question_text,
            reply_markup=period_quiz_answer_kb(period_id, next_idx, options),
        )

    await query.answer()


def register(app: Application) -> None:
    app.add_handler(CallbackQueryHandler(on_period, pattern=r"^period:"))
    app.add_handler(CallbackQueryHandler(on_period_authors, pattern=r"^period_authors:"))
    app.add_handler(CallbackQueryHandler(on_period_events, pattern=r"^period_events:"))
    app.add_handler(CallbackQueryHandler(on_period_quiz, pattern=r"^period_quiz:"))
    app.add_handler(CallbackQueryHandler(on_period_quiz_answer, pattern=r"^pq_a:"))
    app.add_handler(CallbackQueryHandler(on_period_quiz_next, pattern=r"^pq_next:"))
