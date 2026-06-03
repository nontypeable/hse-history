from collections import namedtuple
from contextlib import asynccontextmanager

from telegram.ext import CallbackContext

from bot.container import Container
from bot.infrastructure.i18n import DEFAULT_LANG

ServiceBundle = namedtuple(
    "ServiceBundle",
    ["content_service", "progress_service", "quiz_service", "quest_service", "lang"],
)


@asynccontextmanager
async def get_services(context: CallbackContext, user_id: int):
    container: Container = context.bot_data["container"]
    session = container.session()
    try:
        lang = context.user_data.get("lang")
        if lang is None:
            progress = container.progress_service(session)
            lang = await progress.get_language(user_id)
            if not lang:
                lang = DEFAULT_LANG
            context.user_data["lang"] = lang

        svc = ServiceBundle(
            content_service=container.content_service,
            progress_service=container.progress_service(session),
            quiz_service=container.quiz_service(session),
            quest_service=container.quest_service(session),
            lang=lang,
        )
        yield svc
    finally:
        await session.close()


def update_lang_cache(context: CallbackContext, new_lang: str) -> None:
    context.user_data["lang"] = new_lang
