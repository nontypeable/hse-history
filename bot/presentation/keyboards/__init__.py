from typing import Any

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from bot.infrastructure.content import get_authors, get_events
from bot.infrastructure.i18n import DEFAULT_LANG, t


def language_selection_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text="🇬🇧 English", callback_data="lang:en")],
            [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang:ru")],
        ]
    )


def main_menu_kb(lang: str = DEFAULT_LANG) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text=t("menu_periods", lang), callback_data="period:list")],
            [InlineKeyboardButton(text=t("menu_authors", lang), callback_data="author:list")],
            [InlineKeyboardButton(text=t("menu_events", lang), callback_data="event:list")],
            [InlineKeyboardButton(text=t("menu_achievements", lang), callback_data="ach:list")],
            [InlineKeyboardButton(text=t("menu_quest", lang), callback_data="quest_intro")],
            [InlineKeyboardButton(text=t("menu_quiz", lang), callback_data="quiz_start")],
            [InlineKeyboardButton(text=t("menu_map", lang), callback_data="map:list")],
            [InlineKeyboardButton(text=t("menu_about", lang), callback_data="about")],
            [InlineKeyboardButton(text=t("menu_language", lang), callback_data="lang:select")],
        ]
    )


def back_to_main_kb(lang: str = DEFAULT_LANG) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[InlineKeyboardButton(text=t("back_main", lang), callback_data="main_menu")]])


def periods_kb(periods: list[dict[str, Any]], lang: str = DEFAULT_LANG) -> InlineKeyboardMarkup:
    buttons = []
    for p in periods:
        buttons.append([InlineKeyboardButton(text=f"{p['emoji']} {p['title']}", callback_data=f"period:{p['id']}")])
    buttons.append([InlineKeyboardButton(text=t("back_main", lang), callback_data="main_menu")])
    return InlineKeyboardMarkup(buttons)


def period_detail_kb(period_id: str, lang: str = DEFAULT_LANG) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text=t("period_authors", lang), callback_data=f"period_authors:{period_id}")],
            [InlineKeyboardButton(text=t("period_events", lang), callback_data=f"period_events:{period_id}")],
            [InlineKeyboardButton(text=t("period_quiz", lang), callback_data=f"period_quiz:{period_id}")],
            [InlineKeyboardButton(text=t("back_periods", lang), callback_data="period:list")],
            [InlineKeyboardButton(text=t("back_main", lang), callback_data="main_menu")],
        ]
    )


def authors_list_kb(authors: list[dict[str, Any]], lang: str = DEFAULT_LANG) -> InlineKeyboardMarkup:
    buttons = []
    for a in authors:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=f"👤 {a['name']} ({a['life_years']})",
                    callback_data=f"author:{a['id']}",
                )
            ]
        )
    buttons.append([InlineKeyboardButton(text=t("back_main", lang), callback_data="main_menu")])
    return InlineKeyboardMarkup(buttons)


def author_detail_kb(author_id: str, lang: str = DEFAULT_LANG) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text=t("author_works_btn", lang), callback_data=f"author_works:{author_id}")],
            [InlineKeyboardButton(text=t("author_context_btn", lang), callback_data=f"author_ctx:{author_id}")],
            [InlineKeyboardButton(text=t("author_question_btn", lang), callback_data=f"author_q:{author_id}")],
            [InlineKeyboardButton(text=t("back_authors", lang), callback_data="author:list")],
            [InlineKeyboardButton(text=t("back_main", lang), callback_data="main_menu")],
        ]
    )


def events_list_kb(events: list[dict[str, Any]], lang: str = DEFAULT_LANG) -> InlineKeyboardMarkup:
    buttons = []
    for e in events:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=f"⚡ {e['date']} — {e['title']}",
                    callback_data=f"event:{e['id']}",
                )
            ]
        )
    buttons.append([InlineKeyboardButton(text=t("back_main", lang), callback_data="main_menu")])
    return InlineKeyboardMarkup(buttons)


def event_detail_kb(event_id: str, lang: str = DEFAULT_LANG) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text=t("event_question_btn", lang), callback_data=f"event_q:{event_id}")],
            [InlineKeyboardButton(text=t("back_events", lang), callback_data="event:list")],
            [InlineKeyboardButton(text=t("back_main", lang), callback_data="main_menu")],
        ]
    )


def achievements_list_kb(achievements: list[dict[str, Any]], lang: str = DEFAULT_LANG) -> InlineKeyboardMarkup:
    buttons = []
    for a in achievements:
        buttons.append([InlineKeyboardButton(text=f"{a['emoji']} {a['title']}", callback_data=f"ach:{a['id']}")])
    buttons.append([InlineKeyboardButton(text=t("back_main", lang), callback_data="main_menu")])
    return InlineKeyboardMarkup(buttons)


def map_places_kb(places: list[dict[str, Any]], lang: str = DEFAULT_LANG) -> InlineKeyboardMarkup:
    buttons = []
    for p in places:
        buttons.append([InlineKeyboardButton(text=f"📍 {p['name']}", callback_data=f"map:{p['id']}")])
    buttons.append([InlineKeyboardButton(text=t("back_main", lang), callback_data="main_menu")])
    return InlineKeyboardMarkup(buttons)


def map_place_detail_kb(author_ids: list[str], lang: str = DEFAULT_LANG) -> InlineKeyboardMarkup:
    authors = get_authors(lang)

    buttons = []
    for aid in author_ids:
        author = authors.get(aid)
        if author:
            buttons.append([InlineKeyboardButton(text=f"👤 {author.name}", callback_data=f"map_author:{aid}")])
    buttons.append([InlineKeyboardButton(text=t("back_map", lang), callback_data="map:list")])
    buttons.append([InlineKeyboardButton(text=t("back_main", lang), callback_data="main_menu")])
    return InlineKeyboardMarkup(buttons)


def quiz_answer_kb(question_id: int, options: list[str]) -> InlineKeyboardMarkup:
    buttons = []
    for i, option in enumerate(options):
        buttons.append([InlineKeyboardButton(text=option, callback_data=f"quiz_a:{question_id}:{i}")])
    return InlineKeyboardMarkup(buttons)


def quiz_next_kb(question_id: int, lang: str = DEFAULT_LANG) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(text=t("quiz_next", lang), callback_data=f"quiz_next:{question_id}")]]
    )


def quiz_result_kb(lang: str = DEFAULT_LANG) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[InlineKeyboardButton(text=t("back_main", lang), callback_data="main_menu")]])


def quest_intro_kb(lang: str = DEFAULT_LANG) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text=t("quest_start_btn", lang), callback_data="quest_go")],
            [InlineKeyboardButton(text=t("back_main", lang), callback_data="main_menu")],
        ]
    )


def quest_stage_kb(
    stage_number: int, author_ids: list[str], event_ids: list[str], lang: str = DEFAULT_LANG
) -> InlineKeyboardMarkup:
    authors = get_authors(lang)
    events = get_events(lang)

    buttons = []
    for aid in author_ids:
        author = authors.get(aid)
        if author:
            buttons.append(
                [InlineKeyboardButton(text=f"👤 {author.name}", callback_data=f"quest_author:{aid}:{stage_number}")]
            )
    for eid in event_ids:
        event = events.get(eid)
        if event:
            buttons.append(
                [InlineKeyboardButton(text=f"⚡ {event.title}", callback_data=f"quest_event:{eid}:{stage_number}")]
            )
    buttons.append(
        [InlineKeyboardButton(text=t("quest_question_btn", lang), callback_data=f"quest_q:{stage_number}:0")]
    )
    buttons.append([InlineKeyboardButton(text=t("back_main", lang), callback_data="main_menu")])
    return InlineKeyboardMarkup(buttons)


def quest_question_kb(stage_number: int, question_index: int, options: list[str]) -> InlineKeyboardMarkup:
    buttons = []
    for i, option in enumerate(options):
        buttons.append(
            [InlineKeyboardButton(text=option.strip(), callback_data=f"quest_qa:{stage_number}:{question_index}:{i}")]
        )
    return InlineKeyboardMarkup(buttons)


def quest_complete_stage_kb(stage_number: int, lang: str = DEFAULT_LANG) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(text=t("quest_receive_key", lang), callback_data=f"quest_cs:{stage_number}")]]
    )


def quest_answer_result_kb(
    stage_number: int, question_index: int, total_questions: int, lang: str = DEFAULT_LANG
) -> InlineKeyboardMarkup:
    if question_index + 1 < total_questions:
        return InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=t("quest_next_question", lang),
                        callback_data=f"quest_q:{stage_number}:{question_index + 1}",
                    )
                ]
            ]
        )
    return quest_complete_stage_kb(stage_number, lang)


def quest_back_to_stage_kb(stage_number: int, lang: str = DEFAULT_LANG) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text=t("back_stage", lang), callback_data=f"quest_stage:{stage_number}")],
            [InlineKeyboardButton(text=t("back_main", lang), callback_data="main_menu")],
        ]
    )


def period_quiz_answer_kb(period_id: str, question_idx: int, options: list[str]) -> InlineKeyboardMarkup:
    buttons = []
    for i, option in enumerate(options):
        buttons.append(
            [InlineKeyboardButton(text=option.strip(), callback_data=f"pq_a:{period_id}:{question_idx}:{i}")]
        )
    return InlineKeyboardMarkup(buttons)


def period_quiz_next_kb(period_id: str, question_idx: int, lang: str = DEFAULT_LANG) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(text=t("period_quiz_next", lang), callback_data=f"pq_next:{period_id}:{question_idx}")]]
    )


def period_quiz_result_kb(period_id: str, lang: str = DEFAULT_LANG) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text=t("back_periods", lang), callback_data="period:list")],
            [InlineKeyboardButton(text=t("back_main", lang), callback_data="main_menu")],
        ]
    )
