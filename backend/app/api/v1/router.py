from fastapi import APIRouter

api_router = APIRouter()

# Endpoint routers are registered here as each resource is built, e.g.:
#   from app.api.v1.endpoints import auth
#   api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
