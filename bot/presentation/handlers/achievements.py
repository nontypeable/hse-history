import logging

from telegram import Update
from telegram.ext import Application, CallbackContext, CallbackQueryHandler

from bot.infrastructure.i18n import t
from bot.presentation.helpers import get_services
from bot.presentation.keyboards import achievements_list_kb, back_to_main_kb

logger = logging.getLogger(__name__)


async def on_achievement(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    ach_id = query.data.split(":")[1]
    user_id = query.from_user.id

    async with get_services(context, user_id) as svc:
        if ach_id == "list":
            achievements = svc.content_service.get_all_achievements(svc.lang)
            ach_dicts = [{"id": a.id, "emoji": a.emoji, "title": a.title} for a in achievements]
            await query.edit_message_text(
                t("achievements_title", svc.lang),
                reply_markup=achievements_list_kb(ach_dicts, svc.lang),
            )
            await query.answer()
            return

        achievement = svc.content_service.get_achievement(ach_id, svc.lang)
        if achievement is None:
            await query.edit_message_text(t("achievement_not_found", svc.lang), reply_markup=back_to_main_kb(svc.lang))
            await query.answer()
            return

        related_authors = []
        for aid in achievement.related_author_ids:
            author = svc.content_service.get_author(aid, svc.lang)
            if author:
                related_authors.append(author.name)

        text = (
            f"{achievement.emoji} {achievement.title}\n\n"
            f"{t('achievement_explanation', svc.lang)}\n{achievement.explanation}\n\n"
            f"{t('achievement_why_matters', svc.lang)}\n{achievement.why_it_matters}\n\n"
            f"{t('achievement_authors', svc.lang)} {', '.join(related_authors)}\n\n"
            f"{t('achievement_works', svc.lang)} {', '.join(achievement.related_works)}\n\n"
            f"{t('achievement_context', svc.lang)}\n{achievement.historical_context}"
        )
        await query.edit_message_text(text, reply_markup=back_to_main_kb(svc.lang))

    await query.answer()


def register(app: Application) -> None:
    app.add_handler(CallbackQueryHandler(on_achievement, pattern=r"^ach:"))
