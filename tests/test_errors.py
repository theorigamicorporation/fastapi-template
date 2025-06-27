# test_errors.py


class TestErrorHandling:
    """Test cases for error handling and edge cases."""

    def test_nonexistent_endpoint_returns_404(self, client):
        """Test that accessing a non-existent endpoint returns 404."""
        response = client.get("/nonexistent")
        assert response.status_code == 404

    def test_nonexistent_api_endpoint_returns_404(self, client, api_v1_prefix):
        """Test that accessing a non-existent API endpoint returns 404."""
        response = client.get(f"{api_v1_prefix}/nonexistent")
        assert response.status_code == 404

    def test_method_not_allowed(self, client):
        """Test that using wrong HTTP method returns 405."""
        # Try POST on a GET-only endpoint
        response = client.post("/")
        assert response.status_code == 405

    def test_method_not_allowed_on_health(self, client, api_v1_prefix):
        """Test wrong HTTP method on health endpoints returns 405."""
        # Try POST on health endpoints
        response = client.post(f"{api_v1_prefix}/health/live")
        assert response.status_code == 405
        
        response = client.put(f"{api_v1_prefix}/health/ready")
        assert response.status_code == 405 