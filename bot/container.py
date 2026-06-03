from sqlalchemy.ext.asyncio import AsyncSession

from bot.application.services.content_service import ContentService
from bot.application.services.progress_service import ProgressService
from bot.application.services.quest_service import QuestService
from bot.application.services.quiz_service import QuizService
from bot.infrastructure.database.connection import create_engine, init_db
from bot.infrastructure.repositories import (
    QuestProgressRepository,
    QuizResultRepository,
    UserRepository,
)


class Container:
    def __init__(self, database_url: str) -> None:
        self._database_url = database_url
        self._engine, self._session_factory = create_engine(database_url)
        self._content_service = ContentService()

    async def init(self) -> None:
        await init_db(self._engine)

    async def dispose(self) -> None:
        await self._engine.dispose()

    def session(self) -> AsyncSession:
        return self._session_factory()

    @property
    def content_service(self) -> ContentService:
        return self._content_service

    def progress_service(self, session: AsyncSession) -> ProgressService:
        return ProgressService(UserRepository(session))

    def quiz_service(self, session: AsyncSession) -> QuizService:
        return QuizService(QuizResultRepository(session))

    def quest_service(self, session: AsyncSession) -> QuestService:
        return QuestService(QuestProgressRepository(session))
