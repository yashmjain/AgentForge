'''
This is health router class which is a placeholder for all types of health related endpoints
'''

from fastapi import APIRouter
from starlette import status

from health.schemas import HealthResponse
from src.health.constants import HealthStatus

'''
prefix:  /health : All the endpoints in this router will start with /health
include_in_schema: Whether to hide the details of this endpoint in swagger 
tag : All this endpoint will be tagged using this tag 
'''
health_router = APIRouter(prefix="/health", include_in_schema=False, tags=["health"])




@health_router.get("/liveness", status_code=status.HTTP_200_OK, response_model_exclude_none=True)
def liveness() -> HealthResponse:
    return HealthResponse(status=HealthStatus.UP)











