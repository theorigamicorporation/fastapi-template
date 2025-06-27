# FastAPI Template

A simple FastAPI template repository with basic structure and endpoints.

## Features

- FastAPI framework
- Health check endpoints (liveness and readiness probes)
- Hello World endpoint
- Docker support
- GitHub Actions workflows

## Project Structure

```
fastapi-template/
├── Dockerfile          # Docker configuration
├── requirements.txt    # Python dependencies
├── pytest.ini         # Pytest configuration
├── .coveragerc        # Coverage configuration
├── main.py            # Main application file
├── routers/           # API routers
│   ├── __init__.py
│   └── health.py      # Health check endpoints
├── schemas/           # Pydantic models
│   ├── __init__.py
│   └── health.py      # Health response models
├── tests/             # Test files
│   ├── __init__.py
│   ├── conftest.py    # Pytest fixtures
│   ├── test_app.py    # App lifecycle tests
│   ├── test_main.py   # Main endpoint tests
│   ├── test_health.py # Health endpoint tests
│   └── test_errors.py # Error handling tests
└── .github/           # GitHub Actions workflows
    └── workflows/
```

## Endpoints

- `GET /` - Root endpoint with hello world message
- `GET /api/v1/hello` - Hello world API endpoint
- `GET /api/v1/health/live` - Liveness probe
- `GET /api/v1/health/ready` - Readiness probe

## Running Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python main.py
   ```
   
   Or using uvicorn directly:
   ```bash
   uvicorn main:create_app --factory --host 0.0.0.0 --port 8000 --reload
   ```

3. Access the API:
   - API docs: http://localhost:8000/docs
   - Root endpoint: http://localhost:8000/
   - Hello endpoint: http://localhost:8000/api/v1/hello
   - Health endpoints: http://localhost:8000/api/v1/health/live

## Running with Docker

1. Build the Docker image:
   ```bash
   docker build -t fastapi-template .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 fastapi-template
   ```

## Testing

Run tests using pytest:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_health.py

# Run tests with verbose output
pytest -v
```

Test Structure:
- `tests/conftest.py` - Shared pytest fixtures
- `tests/test_app.py` - Tests for app lifecycle and configuration
- `tests/test_main.py` - Tests for root and hello endpoints
- `tests/test_health.py` - Tests for health check endpoints
- `tests/test_errors.py` - Tests for error handling

## Development

This is a template repository. You can use it as a starting point for your FastAPI projects by:

1. Cloning this repository
2. Adding your own routers and business logic
3. Extending the configuration as needed
4. Adding database connections, authentication, etc. 