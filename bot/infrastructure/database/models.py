from datetime import UTC, datetime

from sqlalchemy import Boolean, DateTime, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from bot.infrastructure.i18n import DEFAULT_LANG


def _utcnow() -> datetime:
    return datetime.now(UTC)


class Base(DeclarativeBase):
    pass


class UserModel(Base):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str | None] = mapped_column(String, nullable=True)
    first_name: Mapped[str | None] = mapped_column(String, nullable=True)
    language: Mapped[str] = mapped_column(String, default=DEFAULT_LANG, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)


class QuizResultModel(Base):
    __tablename__ = "quiz_results"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    score: Mapped[int] = mapped_column(Integer, nullable=False)
    total: Mapped[int] = mapped_column(Integer, nullable=False)
    completed_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)


class QuestProgressModel(Base):
    __tablename__ = "quest_progress"

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    current_stage: Mapped[int] = mapped_column(Integer, default=1)
    completed_stages: Mapped[str] = mapped_column(Text, default="")
    collected_keys: Mapped[str] = mapped_column(Text, default="")
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, onupdate=_utcnow)
