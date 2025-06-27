# test_main.py


class TestRootEndpoint:
    """Test cases for the root endpoint."""

    def test_root_endpoint(self, client):
        """Test the root endpoint returns hello world message."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "Hello World! Welcome to FastAPI Template"
        assert data["version"] == "1.0.0"

    def test_root_endpoint_response_structure(self, client):
        """Test the root endpoint response has correct structure."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "version" in data
        assert isinstance(data["message"], str)
        assert isinstance(data["version"], str)


class TestHelloEndpoint:
    """Test cases for the hello world API endpoint."""

    def test_hello_endpoint(self, client, api_v1_prefix):
        """Test the hello endpoint returns correct message."""
        response = client.get(f"{api_v1_prefix}/hello")
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "Hello from FastAPI Template API v1!"
        assert data["version"] == "1.0.0"

    def test_hello_endpoint_response_structure(self, client, api_v1_prefix):
        """Test the hello endpoint response has correct structure."""
        response = client.get(f"{api_v1_prefix}/hello")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "version" in data
        assert isinstance(data["message"], str)
        assert isinstance(data["version"], str) 