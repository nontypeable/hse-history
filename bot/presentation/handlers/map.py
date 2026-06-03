import logging

from telegram import Update
from telegram.ext import Application, CallbackContext, CallbackQueryHandler

from bot.infrastructure.i18n import t
from bot.presentation.helpers import get_services
from bot.presentation.keyboards import back_to_main_kb, map_place_detail_kb, map_places_kb

logger = logging.getLogger(__name__)


async def on_map(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    place_id = query.data.split(":")[1]
    user_id = query.from_user.id

    async with get_services(context, user_id) as svc:
        if place_id == "list":
            places = svc.content_service.get_all_map_places(svc.lang)
            place_dicts = [{"id": p.id, "name": p.name} for p in places]
            await query.edit_message_text(
                t("map_title", svc.lang),
                reply_markup=map_places_kb(place_dicts, svc.lang),
            )
            await query.answer()
            return

        place = svc.content_service.get_map_place(place_id, svc.lang)
        if place is None:
            await query.edit_message_text(t("map_not_found", svc.lang), reply_markup=back_to_main_kb(svc.lang))
            await query.answer()
            return

        related_authors = []
        for aid in place.related_author_ids:
            author = svc.content_service.get_author(aid, svc.lang)
            if author:
                related_authors.append(author.name)

        text = (
            f"📍 {place.name}\n\n"
            f"{t('map_why_matters', svc.lang)}\n{place.why_it_matters}\n\n"
            f"{t('map_authors', svc.lang)} {', '.join(related_authors)}\n\n"
            f"{t('map_value', svc.lang)}\n{place.historical_value}"
        )
        await query.edit_message_text(
            text,
            reply_markup=map_place_detail_kb(place.related_author_ids, svc.lang),
        )

    await query.answer()


async def on_map_author(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    author_id = query.data.split(":")[1]
    user_id = query.from_user.id

    async with get_services(context, user_id) as svc:
        author = svc.content_service.get_author(author_id, svc.lang)
        if author is None:
            await query.edit_message_text(t("author_not_found", svc.lang), reply_markup=back_to_main_kb(svc.lang))
            await query.answer()
            return

        text = (
            f"👤 {author.name}\n"
            f"{t('author_life_years', svc.lang)} {author.life_years}\n\n"
            f"{author.who_they_were}\n\n"
            f"{t('author_achievement', svc.lang)}\n{author.main_achievement}"
        )
        from bot.presentation.keyboards import author_detail_kb

        await query.edit_message_text(text, reply_markup=author_detail_kb(author.id, svc.lang))

    await query.answer()


def register(app: Application) -> None:
    app.add_handler(CallbackQueryHandler(on_map, pattern=r"^map:"))
    app.add_handler(CallbackQueryHandler(on_map_author, pattern=r"^map_author:"))
