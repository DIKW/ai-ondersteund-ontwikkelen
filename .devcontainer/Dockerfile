FROM python:3.12.4-slim-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends git bash ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash trainer
USER trainer
WORKDIR /workspace/ai-ondersteund-ontwikkelen
