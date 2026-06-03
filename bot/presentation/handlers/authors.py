import logging

from telegram import Update
from telegram.ext import Application, CallbackContext, CallbackQueryHandler

from bot.infrastructure.i18n import t, tf
from bot.presentation.helpers import get_services
from bot.presentation.keyboards import author_detail_kb, authors_list_kb, back_to_main_kb

logger = logging.getLogger(__name__)


async def on_author(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    author_id = query.data.split(":")[1]
    user_id = query.from_user.id

    async with get_services(context, user_id) as svc:
        if author_id == "list":
            from bot.infrastructure.content import get_authors

            authors_dict = get_authors(svc.lang)
            author_dicts = [{"id": a.id, "name": a.name, "life_years": a.life_years} for a in authors_dict.values()]
            await query.edit_message_text(
                t("authors_title", svc.lang),
                reply_markup=authors_list_kb(author_dicts, svc.lang),
            )
            await query.answer()
            return

        author = svc.content_service.get_author(author_id, svc.lang)
        if author is None:
            await query.edit_message_text(t("author_not_found", svc.lang), reply_markup=back_to_main_kb(svc.lang))
            await query.answer()
            return

        text = (
            f"👤 {author.name}\n"
            f"{t('author_life_years', svc.lang)} {author.life_years}\n\n"
            f"{author.who_they_were}\n\n"
            f"{t('author_why_matter', svc.lang)}\n{author.why_they_matter}\n\n"
            f"{t('author_achievement', svc.lang)}\n{author.main_achievement}\n\n"
            f"{t('author_fact', svc.lang)}\n{author.interesting_fact}"
        )
        await query.edit_message_text(text, reply_markup=author_detail_kb(author.id, svc.lang))

    await query.answer()


async def on_author_works(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    author_id = query.data.split(":")[1]
    user_id = query.from_user.id

    async with get_services(context, user_id) as svc:
        author = svc.content_service.get_author(author_id, svc.lang)
        if author is None:
            await query.edit_message_text(t("author_not_found", svc.lang), reply_markup=back_to_main_kb(svc.lang))
            await query.answer()
            return
        works_text = "\n".join(f"  📖 {w}" for w in author.main_works)
        text = tf("author_works_title", svc.lang, name=author.name) + f"\n\n{works_text}"
        await query.edit_message_text(text, reply_markup=author_detail_kb(author.id, svc.lang))

    await query.answer()


async def on_author_context(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    author_id = query.data.split(":")[1]
    user_id = query.from_user.id

    async with get_services(context, user_id) as svc:
        author = svc.content_service.get_author(author_id, svc.lang)
        if author is None:
            await query.edit_message_text(t("author_not_found", svc.lang), reply_markup=back_to_main_kb(svc.lang))
            await query.answer()
            return
        text = tf("author_context_title", svc.lang, name=author.name) + f"\n\n{author.historical_context}"
        await query.edit_message_text(text, reply_markup=author_detail_kb(author.id, svc.lang))

    await query.answer()


async def on_author_question(update: Update, context: CallbackContext) -> None:
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
            tf("author_question_title", svc.lang, name=author.name)
            + f"\n\n{author.mini_question}\n\n"
            + t("author_answer_label", svc.lang)
            + f"\n{author.mini_answer}"
        )
        await query.edit_message_text(text, reply_markup=author_detail_kb(author.id, svc.lang))

    await query.answer()


def register(app: Application) -> None:
    app.add_handler(CallbackQueryHandler(on_author, pattern=r"^author:"))
    app.add_handler(CallbackQueryHandler(on_author_works, pattern=r"^author_works:"))
    app.add_handler(CallbackQueryHandler(on_author_context, pattern=r"^author_ctx:"))
    app.add_handler(CallbackQueryHandler(on_author_question, pattern=r"^author_q:"))
