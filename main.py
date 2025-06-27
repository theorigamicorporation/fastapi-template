# main.py

from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel

# Local imports
from routers.health import router as health_router

# API version prefix
V1_PREFIX = "/api/v1"


class HelloWorldResponse(BaseModel):
    message: str
    version: str


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    """
    Manage application lifecycle.
    This is where you would initialize connections, load configurations, etc.
    """
    # Startup
    print("Starting up FastAPI template application...")
    yield
    # Shutdown
    print("Shutting down FastAPI template application...")


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """
    app = FastAPI(
        title="FastAPI Template",
        description="A simple FastAPI template repository",
        version="1.0.0",
        lifespan=app_lifespan
    )

    # Include routers
    app.include_router(
        health_router, 
        prefix=f"{V1_PREFIX}/health", 
        tags=["health"]
    )

    # Root endpoint
    @app.get("/", response_model=HelloWorldResponse)
    def root():
        """Root endpoint returning hello world message."""
        return HelloWorldResponse(
            message="Hello World! Welcome to FastAPI Template",
            version="1.0.0"
        )

    # Hello world endpoint
    @app.get(f"{V1_PREFIX}/hello", response_model=HelloWorldResponse)
    def hello_world():
        """Simple hello world endpoint."""
        return HelloWorldResponse(
            message="Hello from FastAPI Template API v1!",
            version="1.0.0"
        )

    return app


def main():
    """
    Main function to run the application directly.
    """
    import uvicorn
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main() 