from typing import Dict

from pydantic import BaseModel, field_serializer  # This trnasforms base python classes into smart data validators

from src.health.constants import HealthStatus


class CompositeHealthResponse(BaseModel):
    status:HealthStatus

    '''
    When FastAPI return the CompositeHealthResponse object and we want to retuen the object in the form of json . While converting this object into json
    below rules are applied 
    This method runs when the model is converted to JSON, such as when FastAPI sends response like "return CompositeHealthResponse(status=HealthStatus.OK)"
    '''
    @field_serializer("status", when_used="json")
    def serialize_status(self, status: HealthStatus):
        return status.name



class HealthResponse(BaseModel):
    status:HealthStatus
    components: Dict[str, CompositeHealthResponse] | None = None  # None = None will make this field optional

    @field_serializer("status", when_used="json")
    def serialize_status(self, status: HealthStatus):
        return status.name