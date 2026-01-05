from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from backend.shared.config import config


engine = create_async_engine(
    url=config.AsyncDataBaseUrl,
    pool_size=20,
    echo=True,
    )


session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False, 
    class_=AsyncSession
    )


async def db_health_chek():
    try:
        session = session_factory()
        await session.execute(text("SELECT 1"))
    except Exception as e:
        raise e
    finally:
        await session.aclose()