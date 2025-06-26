# ---------------------
# Stage 1: Build
# ---------------------
FROM python:3.10-slim AS build

ENV POETRY_VERSION=1.8.2
ENV PATH="/root/.local/bin:$PATH"

# Install curl and poetry
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy dependency files first (for better cache)
COPY pyproject.toml poetry.lock* ./

# Install dependencies (without virtualenv)
RUN poetry config virtualenvs.create false && \
    poetry install --no-root

# Copy app source code
COPY . .

# ---------------------
# Stage 2: Run
# ---------------------
FROM python:3.10-slim AS run

ENV PATH="/root/.local/bin:$PATH"

# Copy python packages and binaries from build stage
COPY --from=build /usr/local/lib /usr/local/lib
COPY --from=build /usr/local/bin /usr/local/bin

# Copy your app code
WORKDIR /app
COPY --from=build /app /app

# Create directory for QR output
RUN mkdir -p static/qr_codes

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
