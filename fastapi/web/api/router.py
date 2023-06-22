from fastapi.routing import APIRouter
from fastapi.web.api import echo
from fastapi.web.api import dummy
from fastapi.web.api import docs
from fastapi.web.api import monitoring

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(docs.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(dummy.router, prefix="/dummy", tags=["dummy"])
