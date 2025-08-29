from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.service.api.config import settings
from app.service.api.v1.endpoints import api

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.VERSION,
)

# Include API router
app.include_router(api.router, tags=["api"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
