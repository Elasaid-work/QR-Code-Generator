FROM python:3.10

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Set working dir
WORKDIR /app

# Copy pyproject files
COPY pyproject.toml poetry.lock* ./

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-root

# Copy app code
COPY . .

# Make sure static directory exists
RUN mkdir -p static/qr_codes

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

