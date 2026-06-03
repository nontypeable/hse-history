from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    DATABASE_URL: str = "sqlite+aiosqlite:///./data/bot.db"
    LOG_LEVEL: str = "INFO"
    PROXY_URL: str | None = None

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


def get_settings() -> Settings:
    import os

    token = os.environ.get("BOT_TOKEN", "")
    kwargs: dict[str, str] = {"BOT_TOKEN": token}
    proxy = os.environ.get("PROXY_URL")
    if proxy:
        kwargs["PROXY_URL"] = proxy
    return Settings(**kwargs)
