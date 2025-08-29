from fastapi import APIRouter

from app.service.api.config import settings

# Create the main API router
router = APIRouter(prefix=settings.API_V1_STR)

@router.get("/")
def root():
    return {"message": "Welcome to Project-Adriane API", "version": settings.VERSION}

@router.get("/health")
def health_check():
    return {"status": "healthy", "service": settings.PROJECT_NAME}