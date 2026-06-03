import logging

from telegram import Update
from telegram.ext import Application, CallbackContext, CallbackQueryHandler

from bot.infrastructure.i18n import t
from bot.presentation.helpers import get_services
from bot.presentation.keyboards import back_to_main_kb, event_detail_kb, events_list_kb

logger = logging.getLogger(__name__)


async def on_event(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    event_id = query.data.split(":")[1]
    user_id = query.from_user.id

    async with get_services(context, user_id) as svc:
        if event_id == "list":
            from bot.infrastructure.content import get_events

            events_dict = get_events(svc.lang)
            event_dicts = [{"id": e.id, "date": e.date, "title": e.title} for e in events_dict.values()]
            await query.edit_message_text(
                t("events_title", svc.lang),
                reply_markup=events_list_kb(event_dicts, svc.lang),
            )
            await query.answer()
            return

        event = svc.content_service.get_event(event_id, svc.lang)
        if event is None:
            await query.edit_message_text(t("event_not_found", svc.lang), reply_markup=back_to_main_kb(svc.lang))
            await query.answer()
            return

        related_authors = []
        for aid in event.related_author_ids:
            author = svc.content_service.get_author(aid, svc.lang)
            if author:
                related_authors.append(author.name)

        text = (
            f"⚡ {event.date} — {event.title}\n\n"
            f"{t('event_what_happened', svc.lang)}\n{event.what_happened}\n\n"
            f"{t('event_why_matters', svc.lang)}\n{event.why_it_matters}\n\n"
            f"{t('event_connection', svc.lang)}\n{event.connection_to_literature}\n\n"
            f"{t('event_authors', svc.lang)} {', '.join(related_authors)}\n\n"
            f"{t('event_works', svc.lang)} {', '.join(event.related_works)}"
        )
        await query.edit_message_text(text, reply_markup=event_detail_kb(event.id, svc.lang))

    await query.answer()


async def on_event_question(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    event_id = query.data.split(":")[1]
    user_id = query.from_user.id

    async with get_services(context, user_id) as svc:
        event = svc.content_service.get_event(event_id, svc.lang)
        if event is None:
            await query.edit_message_text(t("event_not_found", svc.lang), reply_markup=back_to_main_kb(svc.lang))
            await query.answer()
            return

        text = (
            t("event_question_title", svc.lang)
            + f"\n\n{event.check_question}\n\n"
            + t("event_answer_label", svc.lang)
            + f"\n{event.check_answer}"
        )
        await query.edit_message_text(text, reply_markup=event_detail_kb(event.id, svc.lang))

    await query.answer()


def register(app: Application) -> None:
    app.add_handler(CallbackQueryHandler(on_event, pattern=r"^event:"))
    app.add_handler(CallbackQueryHandler(on_event_question, pattern=r"^event_q:"))
