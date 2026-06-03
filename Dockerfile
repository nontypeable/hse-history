FROM python:3.14-slim

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uv/bin/uv

ENV PATH="/uv/bin/uv:${PATH}"

COPY pyproject.toml uv.lock* ./

RUN uv sync --frozen --no-dev

COPY bot/ ./bot/

RUN mkdir -p data

CMD ["uv", "run", "bot"]