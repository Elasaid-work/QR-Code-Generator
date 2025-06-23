FROM python:3.10-slim

# Install dependencies and poetry
ENV POETRY_VERSION=1.8.2
ENV PATH="/root/.local/bin:$PATH"

RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get clean

# Set working directory
WORKDIR /app

# Copy only dependency files first
COPY pyproject.toml poetry.lock* ./

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-root

# Copy app code
COPY . .

# Make sure static directory exists
RUN mkdir -p static/qr_codes

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

