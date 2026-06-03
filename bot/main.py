import logging

from telegram.ext import ApplicationBuilder

from bot.config import get_settings
from bot.container import Container
from bot.presentation.handlers import register_all_handlers

logger = logging.getLogger(__name__)


def main() -> None:
    settings = get_settings()
    logging.basicConfig(
        level=getattr(logging, settings.LOG_LEVEL, logging.INFO),
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    builder = ApplicationBuilder().token(settings.BOT_TOKEN)
    if settings.PROXY_URL:
        builder = builder.proxy(settings.PROXY_URL).get_updates_proxy(settings.PROXY_URL)
        logger.info("Using proxy: %s", settings.PROXY_URL)

    app = builder.build()

    container = Container(settings.DATABASE_URL)

    async def post_init(application) -> None:
        await container.init()
        application.bot_data["container"] = container
        logger.info("Database initialized")

    async def post_shutdown(application) -> None:
        await container.dispose()

    app.post_init = post_init
    app.post_shutdown = post_shutdown

    register_all_handlers(app)

    logger.info("Handlers registered, starting bot...")
    app.run_polling()


if __name__ == "__main__":
    main()
