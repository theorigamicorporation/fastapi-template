# Dockerfile

FROM python:3.12-slim AS base

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# default target execute whatever is passed in
CMD ["$@"]

FROM base AS api-server
# Start the application
CMD ["uvicorn", "main:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000", "--workers", "4", "--reload"] 