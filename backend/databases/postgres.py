from functools import lru_cache
from typing import Generator, Optional

from loguru import logger
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session

from backend.settings import settings

engine: Optional[Engine] = None
SessionLocal: Optional[sessionmaker] = None


@lru_cache()
def get_postgres_url() -> str:
    return f"postgresql+psycopg2://{settings.postgres_user}:{settings.postgres_password}@" \
                  f"{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_db}"


def init_postgres() -> None:
    db_url = get_postgres_url()
    logger.debug(f"Initializing Postgres database with URL: {db_url}")
    global engine, SessionLocal
    try:
        engine = create_engine(db_url)
        SessionLocal = sessionmaker(bind=engine)
        logger.info("Postgres database initialized successfully")
    except Exception as e:
        logger.error(f"Postgres database initialization failed: {e}")
        engine, SessionLocal = None, None


def get_db_session() -> Generator[Session, None, None]:
    if SessionLocal is None:
        logger.error("Postgres database session not initialized")
        return None
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()