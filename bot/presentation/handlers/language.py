from telegram import Update
from telegram.ext import Application, CallbackContext, CallbackQueryHandler

from bot.infrastructure.i18n import t
from bot.presentation.helpers import get_services, update_lang_cache
from bot.presentation.keyboards import language_selection_kb, main_menu_kb


async def on_lang_select(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    lang = context.user_data.get("lang", "ru")
    await query.edit_message_text(t("language_select", lang), reply_markup=language_selection_kb())
    await query.answer()


async def on_lang_set(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    new_lang = query.data.split(":")[1]
    user_id = query.from_user.id
    is_first_set = not context.user_data.get("lang_set")

    async with get_services(context, user_id) as svc:
        await svc.progress_service.set_language(user_id, new_lang)
    update_lang_cache(context, new_lang)
    context.user_data["lang_set"] = True

    confirmation = t("language_set_en" if new_lang == "en" else "language_set_ru", new_lang)
    if is_first_set:
        await query.edit_message_text(
            f"{t('welcome', new_lang)}\n\n{confirmation}",
            reply_markup=main_menu_kb(new_lang),
        )
    else:
        await query.edit_message_text(
            f"{confirmation}\n\n{t('menu_text', new_lang)}",
            reply_markup=main_menu_kb(new_lang),
        )
    await query.answer()


def register(app: Application) -> None:
    app.add_handler(CallbackQueryHandler(on_lang_select, pattern=r"^lang:select$"))
    app.add_handler(CallbackQueryHandler(on_lang_set, pattern=r"^lang:(en|ru)$"))
