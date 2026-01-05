# Точка входа 
import uvicorn
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import Response
from contextlib import asynccontextmanager

from db.engine import db_health_chek

from shared.logger.logger import logger


@asynccontextmanager
async def lifespan(app : FastAPI):
    logger.info(f"Service user startup")
    yield
    logger.info(f"Service user shutdown")

app = FastAPI(lifespan=lifespan, title="User serviice", version="1.0.0")


@app.get("/health")
async def check_haelth(request : Request):
    try:
        logger.debug(f"Health check auth...")
        logger.debug("Service health")
        logger.debug("Check database...")
        await db_health_chek()
        logger.debug("database health")
        return Response(status_code=200, content="ok")
    except Exception as e:
        return Response(status_code=500, content=str(e))

    

if __name__ == "__main__":
    uvicorn.run("user.main:app", port=8002, host="0.0.0.0", reload=True)