from fastapi.routing import APIRouter

from api_flowix_template.api import docs, echo, kafka, rabbit, redis
from api_flowix_template.api.foo_admin import monitoring, dummy

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(docs.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(dummy.router, prefix="/dummy", tags=["dummy"])
api_router.include_router(redis.router, prefix="/redis", tags=["redis"])
api_router.include_router(rabbit.router, prefix="/rabbit", tags=["rabbit"])
api_router.include_router(kafka.router, prefix="/kafka", tags=["kafka"])
