from fastapi import APIRouter, status as HTTPStatus, Depends
from loguru import logger

from backend.managers import InfoManager
from backend import schemas

router = APIRouter()


@router.get(
    "/info",
    status_code=HTTPStatus.HTTP_200_OK,
)
def info(
        info_manager: InfoManager = Depends(InfoManager)
) -> schemas.InfoResponse:
    logger.info("Info requested")
    return schemas.InfoResponse(info=info_manager.get_info())
