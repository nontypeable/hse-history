from bot.application.dto import (
    AchievementCard,
    AuthorCard,
    EventCard,
    MapPlaceCard,
    PeriodCard,
)
from bot.infrastructure.content import (
    get_achievements,
    get_authors,
    get_events,
    get_map_places,
    get_periods,
)
from bot.infrastructure.i18n import DEFAULT_LANG


class ContentService:
    def get_period(self, period_id: str, lang: str = DEFAULT_LANG) -> PeriodCard | None:
        periods = get_periods(lang)
        period = periods.get(period_id)
        if period is None:
            return None
        return PeriodCard(
            id=period.id,
            emoji=period.emoji,
            title=period.title,
            period=period.period,
            description=period.description,
            historical_context=period.historical_context,
            author_ids=period.author_ids,
            event_ids=period.event_ids,
            achievements=period.achievements,
            questions=period.questions,
        )

    def get_all_periods(self, lang: str = DEFAULT_LANG) -> list[PeriodCard]:
        periods = get_periods(lang)
        return [
            PeriodCard(
                id=p.id,
                emoji=p.emoji,
                title=p.title,
                period=p.period,
                description=p.description,
                historical_context=p.historical_context,
                author_ids=p.author_ids,
                event_ids=p.event_ids,
                achievements=p.achievements,
                questions=p.questions,
            )
            for p in periods.values()
        ]

    def get_author(self, author_id: str, lang: str = DEFAULT_LANG) -> AuthorCard | None:
        authors = get_authors(lang)
        author = authors.get(author_id)
        if author is None:
            return None
        return AuthorCard(
            id=author.id,
            name=author.name,
            life_years=author.life_years,
            period_id=author.period_id,
            who_they_were=author.who_they_were,
            why_they_matter=author.why_they_matter,
            historical_context=author.historical_context,
            main_works=author.main_works,
            main_achievement=author.main_achievement,
            interesting_fact=author.interesting_fact,
            mini_question=author.mini_question,
            mini_answer=author.mini_answer,
        )

    def get_authors_by_period(self, period_id: str, lang: str = DEFAULT_LANG) -> list[AuthorCard]:
        authors = get_authors(lang)
        return [
            AuthorCard(
                id=a.id,
                name=a.name,
                life_years=a.life_years,
                period_id=a.period_id,
                who_they_were=a.who_they_were,
                why_they_matter=a.why_they_matter,
                historical_context=a.historical_context,
                main_works=a.main_works,
                main_achievement=a.main_achievement,
                interesting_fact=a.interesting_fact,
                mini_question=a.mini_question,
                mini_answer=a.mini_answer,
            )
            for a in authors.values()
            if a.period_id == period_id
        ]

    def get_event(self, event_id: str, lang: str = DEFAULT_LANG) -> EventCard | None:
        events = get_events(lang)
        event = events.get(event_id)
        if event is None:
            return None
        return EventCard(
            id=event.id,
            date=event.date,
            title=event.title,
            what_happened=event.what_happened,
            why_it_matters=event.why_it_matters,
            connection_to_literature=event.connection_to_literature,
            related_author_ids=event.related_author_ids,
            related_works=event.related_works,
            check_question=event.check_question,
            check_answer=event.check_answer,
        )

    def get_achievement(self, achievement_id: str, lang: str = DEFAULT_LANG) -> AchievementCard | None:
        achievements = get_achievements(lang)
        achievement = achievements.get(achievement_id)
        if achievement is None:
            return None
        return AchievementCard(
            id=achievement.id,
            emoji=achievement.emoji,
            title=achievement.title,
            explanation=achievement.explanation,
            why_it_matters=achievement.why_it_matters,
            related_author_ids=achievement.related_author_ids,
            related_works=achievement.related_works,
            historical_context=achievement.historical_context,
        )

    def get_all_achievements(self, lang: str = DEFAULT_LANG) -> list[AchievementCard]:
        achievements = get_achievements(lang)
        return [
            AchievementCard(
                id=a.id,
                emoji=a.emoji,
                title=a.title,
                explanation=a.explanation,
                why_it_matters=a.why_it_matters,
                related_author_ids=a.related_author_ids,
                related_works=a.related_works,
                historical_context=a.historical_context,
            )
            for a in achievements.values()
        ]

    def get_map_place(self, place_id: str, lang: str = DEFAULT_LANG) -> MapPlaceCard | None:
        places = get_map_places(lang)
        place = places.get(place_id)
        if place is None:
            return None
        return MapPlaceCard(
            id=place.id,
            name=place.name,
            why_it_matters=place.why_it_matters,
            related_author_ids=place.related_author_ids,
            historical_value=place.historical_value,
        )

    def get_all_map_places(self, lang: str = DEFAULT_LANG) -> list[MapPlaceCard]:
        places = get_map_places(lang)
        return [
            MapPlaceCard(
                id=p.id,
                name=p.name,
                why_it_matters=p.why_it_matters,
                related_author_ids=p.related_author_ids,
                historical_value=p.historical_value,
            )
            for p in places.values()
        ]
