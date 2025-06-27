# health.py

from fastapi import APIRouter, status

from schemas.health import HealthResponse


router = APIRouter()


@router.get(
    "/live",
    status_code=status.HTTP_200_OK,
    response_model=HealthResponse,
)
def liveness_probe():
    """Check if the service is alive."""
    return HealthResponse(status="ok")


@router.get(
    "/ready",
    status_code=status.HTTP_200_OK,
    response_model=HealthResponse,
)
def readiness_probe():
    """Check if the service is ready to serve requests."""
    # In a real application, you might check database connections, 
    # external services, etc. here
    return HealthResponse(status="ok") 