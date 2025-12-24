# Точка входа 
import uvicorn
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import Response
from contextlib import asynccontextmanager

from shared.logger.logger import logger


@asynccontextmanager
async def lifespan(app : FastAPI):
    logger.info(f"Service user startup")
    yield
    logger.info(f"Service user shutdown")

app = FastAPI(lifespan=lifespan, title="User serviice", version="1.0.0")


@app.get("/api-test/test")
async def test(request: Request):
    logger.info("Request recive")
    logger.info("Protected path worck")
    return Response(status_code=200, content="ok get")

@app.post("/api-test/test")
async def test_post(request: Request):
    logger.info("Request recive")
    logger.info("Protected path worck")
    return Response(status_code=200, content="ok post")

@app.post("/health")
async def check_haelth(request : Request):
    logger.info(f"Health check user")
    return Response(status_code=200, content="ok")
    
if __name__ == "__main__":
    uvicorn.run("user.main:app", port=8002, host="0.0.0.0", reload=True)