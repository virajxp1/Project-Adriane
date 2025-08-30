from fastapi import APIRouter

from app.service.api.config import settings
from app.service.api.v1.endpoints.initiate_api import initiate_router

# Create the main API router
api_router = APIRouter(prefix=settings.API_V1_STR)
api_router.include_router(initiate_router)


@api_router.get("/", tags=["api"])
def root():
    return {"message": "Welcome to Project-Adriane API", "version": settings.VERSION}


@api_router.get("/health", tags=["api"])
def health_check():
    return {"status": "healthy", "service": settings.PROJECT_NAME}
