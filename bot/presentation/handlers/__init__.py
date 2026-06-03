from telegram.ext import Application

from bot.presentation.handlers import (
    about,
    achievements,
    authors,
    epochs,
    events,
    language,
    map,
    menu,
    quest,
    quiz,
    start,
)


def register_all_handlers(app: Application) -> None:
    for module in (start, menu, language, epochs, authors, events, achievements, quiz, quest, map, about):
        module.register(app)
