import json
import logging
from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from bot.infrastructure.database.models import QuestProgressModel, QuizResultModel, UserModel
from bot.infrastructure.i18n import DEFAULT_LANG

logger = logging.getLogger(__name__)


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_or_create(self, telegram_id: int, username: str | None, first_name: str | None) -> UserModel:
        result = await self.session.execute(select(UserModel).where(UserModel.telegram_id == telegram_id))
        user = result.scalar_one_or_none()
        if user is None:
            user = UserModel(
                telegram_id=telegram_id,
                username=username,
                first_name=first_name,
            )
            self.session.add(user)
            await self.session.commit()
            logger.info("Created user: telegram_id=%d, username=%s", telegram_id, username)
        return user

    async def get(self, telegram_id: int) -> UserModel | None:
        result = await self.session.execute(select(UserModel).where(UserModel.telegram_id == telegram_id))
        return result.scalar_one_or_none()

    async def get_language(self, telegram_id: int) -> str:
        user = await self.get(telegram_id)
        return user.language if user else DEFAULT_LANG

    async def set_language(self, telegram_id: int, language: str) -> None:
        user = await self.get(telegram_id)
        if user is not None:
            user.language = language
            await self.session.commit()


class QuizResultRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def save(self, user_id: int, score: int, total: int) -> QuizResultModel:
        result = QuizResultModel(user_id=user_id, score=score, total=total)
        self.session.add(result)
        await self.session.commit()
        logger.info("Quiz result saved: user_id=%d, score=%d/%d", user_id, score, total)
        return result

    async def get_best(self, user_id: int) -> QuizResultModel | None:
        result = await self.session.execute(
            select(QuizResultModel)
            .where(QuizResultModel.user_id == user_id)
            .order_by(QuizResultModel.score.desc())
            .limit(1)
        )
        return result.scalar_one_or_none()


class QuestProgressRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_or_create(self, user_id: int) -> QuestProgressModel:
        result = await self.session.execute(select(QuestProgressModel).where(QuestProgressModel.user_id == user_id))
        progress = result.scalar_one_or_none()
        if progress is None:
            progress = QuestProgressModel(user_id=user_id)
            self.session.add(progress)
            await self.session.commit()
            logger.info("Created quest progress for user_id=%d", user_id)
        return progress

    async def update_progress(
        self,
        user_id: int,
        current_stage: int,
        completed_stages: list[int],
        collected_keys: list[str],
        is_completed: bool,
    ) -> QuestProgressModel:
        progress = await self.get_or_create(user_id)
        progress.current_stage = current_stage
        progress.completed_stages = json.dumps(completed_stages)
        progress.collected_keys = json.dumps(collected_keys)
        progress.is_completed = is_completed
        await self.session.commit()
        return progress

    async def get_progress(self, user_id: int) -> QuestProgressModel | None:
        result = await self.session.execute(select(QuestProgressModel).where(QuestProgressModel.user_id == user_id))
        return result.scalar_one_or_none()

    def parse_progress(self, progress: QuestProgressModel) -> dict[str, Any]:
        return {
            "current_stage": progress.current_stage,
            "completed_stages": json.loads(progress.completed_stages) if progress.completed_stages else [],
            "collected_keys": json.loads(progress.collected_keys) if progress.collected_keys else [],
            "is_completed": progress.is_completed,
        }
