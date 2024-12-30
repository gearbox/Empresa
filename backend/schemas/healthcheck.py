from datetime import datetime

from pydantic import BaseModel


class APIHealthCheck(BaseModel):
    status: bool = True
    start_time: datetime | None = None
    uptime_sec: int = 0
    message: str = "API healthcheck Ok"


class DBHealthCheck(BaseModel):
    status: bool = True
    message: str = "Healthcheck Ok"


class HealthCheckResponse(BaseModel):
    status: bool = True
    status_api: APIHealthCheck
    status_db: DBHealthCheck
    status_redis: DBHealthCheck | None = None
