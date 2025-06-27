# test_app.py

from fastapi import FastAPI


class TestAppLifecycle:
    """Test cases for application lifecycle and configuration."""

    def test_app_creation(self, app):
        """Test that the app is created successfully."""
        assert app is not None
        assert isinstance(app, FastAPI)

    def test_app_title(self, app):
        """Test that the app has the correct title."""
        assert app.title == "FastAPI Template"

    def test_app_description(self, app):
        """Test that the app has the correct description."""
        expected = "A simple FastAPI template repository"
        assert app.description == expected

    def test_app_version(self, app):
        """Test that the app has the correct version."""
        assert app.version == "1.0.0"

    def test_app_routes_registered(self, app):
        """Test that all expected routes are registered."""
        routes = [route.path for route in app.routes]
        
        # Check that our custom routes exist
        assert "/" in routes
        assert "/api/v1/hello" in routes
        assert "/api/v1/health/live" in routes
        assert "/api/v1/health/ready" in routes

    def test_app_openapi_url(self, app):
        """Test that OpenAPI documentation is available."""
        assert app.openapi_url == "/openapi.json"