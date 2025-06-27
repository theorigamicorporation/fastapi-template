# conftest.py

import pytest
from fastapi.testclient import TestClient

from main import create_app


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    yield app


@pytest.fixture
def client(app):
    """Create a test client for the FastAPI app."""
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def api_v1_prefix():
    """Return the API v1 prefix."""
    return "/api/v1" 