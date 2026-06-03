import pytest

from bot.application.services.progress_service import ProgressService


class MockUserModel:
    def __init__(self, telegram_id: int, username: str | None, first_name: str | None) -> None:
        self.telegram_id = telegram_id
        self.username = username
        self.first_name = first_name


class MockUserRepository:
    def __init__(self) -> None:
        self.users: dict[int, MockUserModel] = {}

    async def get_or_create(self, telegram_id: int, username: str | None, first_name: str | None) -> MockUserModel:
        if telegram_id not in self.users:
            self.users[telegram_id] = MockUserModel(telegram_id, username, first_name)
        return self.users[telegram_id]

    async def get(self, telegram_id: int) -> MockUserModel | None:
        return self.users.get(telegram_id)


@pytest.fixture
def progress_service() -> ProgressService:
    return ProgressService(MockUserRepository())


class TestProgressService:
    @pytest.mark.asyncio
    async def test_create_user(self, progress_service: ProgressService) -> None:
        user = await progress_service.get_or_create_user(123, "testuser", "Test")
        assert user["telegram_id"] == 123
        assert user["username"] == "testuser"

    @pytest.mark.asyncio
    async def test_get_existing_user(self, progress_service: ProgressService) -> None:
        await progress_service.get_or_create_user(456, "existing", "Existing")
        user = await progress_service.get_or_create_user(456, "existing", "Existing")
        assert user["telegram_id"] == 456

    @pytest.mark.asyncio
    async def test_save_progress(self, progress_service: ProgressService) -> None:
        user = await progress_service.get_or_create_user(789, "progressuser", "Progress")
        assert user["telegram_id"] == 789
