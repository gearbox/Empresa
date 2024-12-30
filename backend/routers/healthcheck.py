from fastapi import APIRouter, status as HTTPStatus, Depends, Response

from backend import schemas, managers

router = APIRouter()


@router.get(
    "/healthcheck",
    status_code=HTTPStatus.HTTP_200_OK,
)
def healthcheck(
        response: Response,
        healthcheck_manager: managers.HealthCheckManager = Depends(managers.HealthCheckManager),
) -> schemas.HealthCheckResponse:
    status_api = healthcheck_manager.get_api_status()
    status_db = healthcheck_manager.get_db_status()
    status_redis = healthcheck_manager.get_redis_status()
    status = status_api.status and status_db.status and status_redis.status
    if not status:
        response.status_code = HTTPStatus.HTTP_500_INTERNAL_SERVER_ERROR
    return schemas.HealthCheckResponse(
        status=status,
        status_api=status_api,
        status_db=status_db,
        status_redis=status_redis,
    )
