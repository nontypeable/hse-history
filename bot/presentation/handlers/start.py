import logging

from telegram import Update
from telegram.ext import Application, CallbackContext, CommandHandler, MessageHandler, filters

from bot.infrastructure.i18n import t
from bot.presentation.helpers import get_services
from bot.presentation.keyboards import language_selection_kb, main_menu_kb

logger = logging.getLogger(__name__)


async def cmd_start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    async with get_services(context, user.id) as svc:
        try:
            await svc.progress_service.get_or_create_user(user.id, user.username, user.first_name)
        except Exception:
            logger.exception("Failed to create user")

    if context.user_data.get("lang_set"):
        lang = context.user_data.get("lang", "ru")
        await update.message.reply_text(t("welcome", lang), reply_markup=main_menu_kb(lang))
    else:
        await update.message.reply_text(t("language_select"), reply_markup=language_selection_kb())


async def fallback_message(update: Update, context: CallbackContext) -> None:
    lang = context.user_data.get("lang", "ru")
    await update.message.reply_text(t("fallback", lang))


def register(app: Application) -> None:
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, fallback_message))
