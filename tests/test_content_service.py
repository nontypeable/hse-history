import pytest

from bot.application.services.content_service import ContentService


@pytest.fixture
def content_service() -> ContentService:
    return ContentService()


class TestContentServicePeriods:
    def test_get_period_by_id(self, content_service: ContentService) -> None:
        period = content_service.get_period("golden_age", "en")
        assert period is not None
        assert period.id == "golden_age"
        assert period.emoji == "🌅"
        assert "Pushkin" in period.description or "Golden" in period.title

    def test_get_all_periods(self, content_service: ContentService) -> None:
        periods = content_service.get_all_periods("en")
        assert len(periods) == 5
        ids = {p.id for p in periods}
        assert ids == {"golden_age", "realism", "reforms", "chekhov", "silver_age"}

    def test_get_period_missing_id(self, content_service: ContentService) -> None:
        result = content_service.get_period("nonexistent", "en")
        assert result is None


class TestContentServiceAuthors:
    def test_get_author_by_id(self, content_service: ContentService) -> None:
        author = content_service.get_author("pushkin", "en")
        assert author is not None
        assert author.name == "Alexander Pushkin"
        assert author.period_id == "golden_age"

    def test_get_authors_by_period(self, content_service: ContentService) -> None:
        authors = content_service.get_authors_by_period("golden_age", "en")
        assert len(authors) >= 5
        assert any(a.name == "Alexander Pushkin" for a in authors)

    def test_get_author_missing_id(self, content_service: ContentService) -> None:
        result = content_service.get_author("nonexistent", "en")
        assert result is None

    def test_all_authors_have_required_fields(self, content_service: ContentService) -> None:
        all_authors = content_service.get_authors_by_period("", "en")
        for author in all_authors:
            assert author.id
            assert author.name
            assert author.life_years
            assert author.main_works
            assert author.why_they_matter


class TestContentServiceEvents:
    def test_get_event_by_id(self, content_service: ContentService) -> None:
        event = content_service.get_event("war_1812", "en")
        assert event is not None
        assert event.title == "Patriotic War of 1812"

    def test_get_event_missing_id(self, content_service: ContentService) -> None:
        result = content_service.get_event("nonexistent", "en")
        assert result is None

    def test_all_events_have_fields(self, content_service: ContentService) -> None:
        from bot.infrastructure.content import EVENTS

        for event_id in EVENTS:
            event = content_service.get_event(event_id, "en")
            assert event is not None
            assert event.what_happened
            assert event.connection_to_literature


class TestContentServiceAchievements:
    def test_get_achievement_by_id(self, content_service: ContentService) -> None:
        achievement = content_service.get_achievement("literary_language", "en")
        assert achievement is not None
        assert "literary language" in achievement.title.lower()

    def test_get_all_achievements(self, content_service: ContentService) -> None:
        achievements = content_service.get_all_achievements("en")
        assert len(achievements) == 8

    def test_get_achievement_missing_id(self, content_service: ContentService) -> None:
        result = content_service.get_achievement("nonexistent", "en")
        assert result is None


class TestContentServiceMapPlaces:
    def test_get_map_place_by_id(self, content_service: ContentService) -> None:
        place = content_service.get_map_place("moscow", "en")
        assert place is not None
        assert place.name == "Moscow"

    def test_get_all_map_places(self, content_service: ContentService) -> None:
        places = content_service.get_all_map_places("en")
        assert len(places) == 7

    def test_get_map_place_missing_id(self, content_service: ContentService) -> None:
        result = content_service.get_map_place("nonexistent", "en")
        assert result is None
