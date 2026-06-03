from telegram import Update
from telegram.ext import Application, CallbackContext, CallbackQueryHandler

from bot.infrastructure.i18n import t
from bot.presentation.keyboards import main_menu_kb


async def on_main_menu(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    lang = context.user_data.get("lang", "ru")
    await query.edit_message_text(t("menu_text", lang), reply_markup=main_menu_kb(lang))
    await query.answer()


def register(app: Application) -> None:
    app.add_handler(CallbackQueryHandler(on_main_menu, pattern=r"^main_menu$"))
