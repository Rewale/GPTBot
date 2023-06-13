# Этап, на котором выполняются подготовительные действия
FROM python:3.10-slim as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

COPY req.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r req.txt

# Финальный этап
FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/req.txt .

RUN pip install --no-cache /wheels/*
COPY . .
ENTRYPOINT ["python", "main.py"]