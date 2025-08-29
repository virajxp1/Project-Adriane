import logging

from fastapi import FastAPI

from app.data.db_connection.SupabaseClient import (
    close_connection_pool,
    init_connection_pool,
)
from app.service.api.config import settings
from app.service.api.v1.endpoints import api

logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.VERSION,
)


@app.on_event("startup")
async def startup_event():
    """Initialize database connection pool on startup"""
    try:
        init_connection_pool()
    except Exception as e:
        logger.warning(f"Database connection failed: {e}")


@app.on_event("shutdown")
async def shutdown_event():
    """Close database connection pool on shutdown"""
    close_connection_pool()


# Include API router
app.include_router(api.router, tags=["api"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
