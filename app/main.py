import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.data.db_connection.SupabaseClient import (
    close_connection_pool,
    init_connection_pool,
)
from app.service.api.config import settings
from app.service.api.v1.endpoints.api import api_router

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan():
    """Lifespan context manager for startup and shutdown events"""
    # Startup
    init_connection_pool()  # let it raise; container/app exits if DB is unreachable
    yield
    # Shutdown
    close_connection_pool()


app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.VERSION,
    lifespan=lifespan,
)

app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
