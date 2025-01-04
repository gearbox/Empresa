from fastapi import APIRouter, status as status_code, Depends
from loguru import logger

from backend import schemas
from backend.managers import InfoManager

router = APIRouter()


@router.get(
    "/info",
    status_code=status_code.HTTP_200_OK,
)
def info(
        info_manager: InfoManager = Depends(InfoManager)
) -> schemas.InfoResponse:
    logger.info("Info requested")
    return schemas.InfoResponse(info=info_manager.get_info())
