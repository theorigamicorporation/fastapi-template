# test_health.py


class TestHealthEndpoints:
    """Test cases for health check endpoints."""

    def test_liveness_probe(self, client, api_v1_prefix):
        """Test the liveness probe returns ok status."""
        response = client.get(f"{api_v1_prefix}/health/live")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"

    def test_liveness_probe_response_structure(self, client, api_v1_prefix):
        """Test the liveness probe response has correct structure."""
        response = client.get(f"{api_v1_prefix}/health/live")
        assert response.status_code == 200
        data = response.json()
        assert "status" in data
        assert isinstance(data["status"], str)

    def test_readiness_probe(self, client, api_v1_prefix):
        """Test the readiness probe returns ok status."""
        response = client.get(f"{api_v1_prefix}/health/ready")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"

    def test_readiness_probe_response_structure(self, client, api_v1_prefix):
        """Test the readiness probe response has correct structure."""
        response = client.get(f"{api_v1_prefix}/health/ready")
        assert response.status_code == 200
        data = response.json()
        assert "status" in data
        assert isinstance(data["status"], str)
