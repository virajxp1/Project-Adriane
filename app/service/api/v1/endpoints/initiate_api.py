# endpoints/initiate_api.py
from fastapi import APIRouter

from app.service.api.config import settings

initiate_router = APIRouter(tags=["initiate"])


@initiate_router.get("/initiate")
def initiate():
    """Initiate endpoint - main entry point for initiation process"""
    return {"message": "Initiate", "version": settings.VERSION}
