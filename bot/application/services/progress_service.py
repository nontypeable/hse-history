from typing import Any

from bot.infrastructure.repositories import UserRepository


class ProgressService:
    def __init__(self, user_repo: UserRepository) -> None:
        self._user_repo = user_repo

    async def get_or_create_user(
        self, telegram_id: int, username: str | None, first_name: str | None
    ) -> dict[str, Any]:
        user = await self._user_repo.get_or_create(telegram_id, username, first_name)
        return {
            "telegram_id": user.telegram_id,
            "username": user.username,
            "first_name": user.first_name,
        }

    async def get_language(self, telegram_id: int) -> str:
        return await self._user_repo.get_language(telegram_id)

    async def set_language(self, telegram_id: int, language: str) -> None:
        await self._user_repo.set_language(telegram_id, language)
