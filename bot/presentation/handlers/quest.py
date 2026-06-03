import logging

from telegram import Update
from telegram.ext import Application, CallbackContext, CallbackQueryHandler

from bot.infrastructure.i18n import t, tf
from bot.presentation.helpers import get_services
from bot.presentation.keyboards import (
    back_to_main_kb,
    main_menu_kb,
    quest_answer_result_kb,
    quest_back_to_stage_kb,
    quest_intro_kb,
    quest_question_kb,
    quest_stage_kb,
)

logger = logging.getLogger(__name__)


async def on_quest_intro(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    lang = context.user_data.get("lang", "ru")
    await query.edit_message_text(t("quest_intro", lang), reply_markup=quest_intro_kb(lang))
    await query.answer()


async def on_quest_go(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user_id = query.from_user.id

    async with get_services(context, user_id) as svc:
        progress = await svc.quest_service.start_quest(user_id)

        if progress.is_completed:
            completion_msg = svc.quest_service.get_completion_message(progress.collected_keys, svc.lang)
            await query.edit_message_text(completion_msg, reply_markup=main_menu_kb(svc.lang))
            await query.answer()
            return

        stage = svc.quest_service.get_stage(progress.current_stage, svc.lang)
        if stage is None:
            await query.edit_message_text(t("quest_not_found", svc.lang), reply_markup=main_menu_kb(svc.lang))
            await query.answer()
            return

        context.user_data["quest_stage"] = progress.current_stage

        text = stage["intro"]
        await query.edit_message_text(
            text,
            reply_markup=quest_stage_kb(stage["stage_number"], stage["author_ids"], stage["event_ids"], svc.lang),
        )

    await query.answer()


async def on_quest_stage(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    stage_number = int(query.data.split(":")[1])
    user_id = query.from_user.id

    async with get_services(context, user_id) as svc:
        stage = svc.quest_service.get_stage(stage_number, svc.lang)
        if stage is None:
            await query.edit_message_text(t("quest_stage_not_found", svc.lang), reply_markup=back_to_main_kb(svc.lang))
            await query.answer()
            return

        text = stage["intro"]
        await query.edit_message_text(
            text,
            reply_markup=quest_stage_kb(stage["stage_number"], stage["author_ids"], stage["event_ids"], svc.lang),
        )

    await query.answer()


async def on_quest_author(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    parts = query.data.split(":")
    author_id = parts[1]
    stage_number = int(parts[2])
    user_id = query.from_user.id

    async with get_services(context, user_id) as svc:
        author = svc.content_service.get_author(author_id, svc.lang)
        if author is None:
            await query.answer(t("author_not_found", svc.lang))
            return
        text = (
            f"👤 {author.name}\n"
            f"{t('author_life_years', svc.lang)} {author.life_years}\n\n"
            f"{author.who_they_were}\n\n"
            f"{t('author_achievement', svc.lang)}\n{author.main_achievement}"
        )
        await query.edit_message_text(text, reply_markup=quest_back_to_stage_kb(stage_number, svc.lang))

    await query.answer()


async def on_quest_event(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    parts = query.data.split(":")
    event_id = parts[1]
    stage_number = int(parts[2])
    user_id = query.from_user.id

    async with get_services(context, user_id) as svc:
        event = svc.content_service.get_event(event_id, svc.lang)
        if event is None:
            await query.answer(t("event_not_found", svc.lang))
            return
        text = (
            f"⚡ {event.date} — {event.title}\n\n"
            f"{t('event_what_happened', svc.lang)}\n{event.what_happened}\n\n"
            f"{t('event_connection', svc.lang)}\n{event.connection_to_literature}"
        )
        await query.edit_message_text(text, reply_markup=quest_back_to_stage_kb(stage_number, svc.lang))

    await query.answer()


async def on_quest_question(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    parts = query.data.split(":")
    stage_number = int(parts[1])
    q_idx = int(parts[2])
    user_id = query.from_user.id

    async with get_services(context, user_id) as svc:
        stage = svc.quest_service.get_stage(stage_number, svc.lang)
        if stage is None:
            await query.answer(t("quest_stage_not_found", svc.lang))
            return
        questions = stage["questions"]
        if q_idx >= len(questions):
            await query.answer(t("quest_not_found", svc.lang))
            return
        question = questions[q_idx]
        options = [o.strip() for o in question["options"].split(";")]
        text = tf("quest_question", svc.lang, num=str(q_idx + 1)) + f"\n\n{question['question']}"
        await query.edit_message_text(
            text,
            reply_markup=quest_question_kb(stage_number, q_idx, options),
        )

    await query.answer()


async def on_quest_question_answer(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    parts = query.data.split(":")
    stage_number = int(parts[1])
    q_idx = int(parts[2])
    option_idx = int(parts[3])
    user_id = query.from_user.id

    async with get_services(context, user_id) as svc:
        stage = svc.quest_service.get_stage(stage_number, svc.lang)
        if stage is None:
            await query.answer(t("quest_stage_not_found", svc.lang))
            return
        questions = stage["questions"]
        if q_idx >= len(questions):
            await query.answer(t("quest_not_found", svc.lang))
            return
        question = questions[q_idx]
        options = [o.strip() for o in question["options"].split(";")]
        user_answer = options[option_idx] if option_idx < len(options) else ""

        result = svc.quest_service.check_stage_answer(stage_number, q_idx, user_answer, svc.lang)
        if "error" in result:
            await query.answer(t("error_generic", svc.lang))
            return

        is_correct = result["is_correct"]
        emoji = t("quest_correct", svc.lang) if is_correct else t("quest_wrong", svc.lang)
        correct_info = "" if is_correct else tf("quest_correct_answer", svc.lang, answer=result["correct_answer"])

        text = f"{emoji}{correct_info}"
        await query.edit_message_text(
            text,
            reply_markup=quest_answer_result_kb(stage_number, q_idx, len(questions), svc.lang),
        )

    await query.answer()


async def on_quest_complete_stage(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    stage_number = int(query.data.split(":")[1])
    user_id = query.from_user.id

    async with get_services(context, user_id) as svc:
        stage = svc.quest_service.get_stage(stage_number, svc.lang)
        if stage is None:
            await query.edit_message_text(t("quest_stage_not_found", svc.lang), reply_markup=back_to_main_kb(svc.lang))
            await query.answer()
            return

        key_name = stage["key_name"]
        progress = await svc.quest_service.complete_stage(user_id, stage_number, key_name)

        key_text = tf("quest_key_received", svc.lang, era_key=key_name)
        keys_so_far = "\n".join(f"  🔑 {k}" for k in progress.collected_keys)

        if progress.is_completed:
            completion_msg = svc.quest_service.get_completion_message(progress.collected_keys, svc.lang)
            await query.edit_message_text(completion_msg, reply_markup=main_menu_kb(svc.lang))
        else:
            next_stage = svc.quest_service.get_stage(progress.current_stage, svc.lang)
            if next_stage is None:
                await query.edit_message_text(t("quest_not_found", svc.lang), reply_markup=main_menu_kb(svc.lang))
                await query.answer()
                return
            context.user_data["quest_stage"] = progress.current_stage
            text = f"{key_text}\n\n{t('quest_keys_collected', svc.lang)}\n{keys_so_far}\n\n{'—' * 30}\n\n{next_stage['intro']}"
            await query.edit_message_text(
                text,
                reply_markup=quest_stage_kb(
                    next_stage["stage_number"], next_stage["author_ids"], next_stage["event_ids"], svc.lang
                ),
            )

    await query.answer()


def register(app: Application) -> None:
    app.add_handler(CallbackQueryHandler(on_quest_intro, pattern=r"^quest_intro$"))
    app.add_handler(CallbackQueryHandler(on_quest_go, pattern=r"^quest_go$"))
    app.add_handler(CallbackQueryHandler(on_quest_stage, pattern=r"^quest_stage:"))
    app.add_handler(CallbackQueryHandler(on_quest_author, pattern=r"^quest_author:"))
    app.add_handler(CallbackQueryHandler(on_quest_event, pattern=r"^quest_event:"))
    app.add_handler(CallbackQueryHandler(on_quest_question, pattern=r"^quest_q:"))
    app.add_handler(CallbackQueryHandler(on_quest_question_answer, pattern=r"^quest_qa:"))
    app.add_handler(CallbackQueryHandler(on_quest_complete_stage, pattern=r"^quest_cs:"))
