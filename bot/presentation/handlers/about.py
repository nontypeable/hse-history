from telegram import Update
from telegram.ext import Application, CallbackContext, CallbackQueryHandler

from bot.infrastructure.i18n import t
from bot.presentation.keyboards import back_to_main_kb


async def on_about(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    lang = context.user_data.get("lang", "ru")
    await query.edit_message_text(t("about_text", lang), reply_markup=back_to_main_kb(lang))
    await query.answer()


def register(app: Application) -> None:
    app.add_handler(CallbackQueryHandler(on_about, pattern=r"^about$"))
