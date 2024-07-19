# Base image: https://github.com/runpod/containers/blob/main/official-templates/base/Dockerfile
# DockerHub: https://hub.docker.com/r/runpod/base/tags
FROM runpod/base:0.6.2-cpu AS base

# The base image comes with many system dependencies pre-installed to help you get started quickly.
# Please refer to the base image's Dockerfile for more information before adding additional dependencies.
# IMPORTANT: The base image overrides the default huggingface cache location.

ENV PYTHON_VERSION="3.11"

FROM base AS builder

WORKDIR /tmp

ENV POETRY_CACHE_DIR="/runpod-volume/.cache/pypoetry/" \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_VIRTUALENVS_IN_PROJECT=true

COPY --link pyproject.toml poetry.lock ./

RUN --mount=type=cache,target=/runpod-volume/.cache/pip \
    --mount=type=cache,target=/runpod-volume/.cache/pypoetry \
    pip3 install --upgrade pip && \
    pip3 install poetry && \
    poetry install --no-ansi --no-interaction --no-root

FROM base AS runner

WORKDIR /app

COPY --link --from=builder /tmp/.venv ./.venv
COPY --link ./walletwatch_ml_backend ./walletwatch_ml_backend

ENV PATH="/app/.venv/bin:$PATH"

ENTRYPOINT ["python3", "-m", "walletwatch_ml_backend.main"]
