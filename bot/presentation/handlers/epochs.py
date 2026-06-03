import logging

from telegram import Update
from telegram.ext import Application, CallbackContext, CallbackQueryHandler

from bot.infrastructure.i18n import t
from bot.presentation.helpers import get_services
from bot.presentation.keyboards import authors_list_kb, back_to_main_kb, events_list_kb, period_detail_kb, periods_kb

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

        await query.edit_message_text(
            f"📝 {t('period_quiz', svc.lang)}: {period.emoji} {period.title}\n\n" + t("quiz_redirect", svc.lang),
            reply_markup=back_to_main_kb(svc.lang),
        )

    await query.answer()


def register(app: Application) -> None:
    app.add_handler(CallbackQueryHandler(on_period, pattern=r"^period:"))
    app.add_handler(CallbackQueryHandler(on_period_authors, pattern=r"^period_authors:"))
    app.add_handler(CallbackQueryHandler(on_period_events, pattern=r"^period_events:"))
    app.add_handler(CallbackQueryHandler(on_period_quiz, pattern=r"^period_quiz:"))
