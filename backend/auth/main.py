# Точка входа 
import uvicorn
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import Response
from contextlib import asynccontextmanager

from shared.logger.logger import logger


@asynccontextmanager
async def lifespan(app : FastAPI):
    logger.info(f"Service auth startup")
    yield
    logger.info(f"Service auth shutdown")


app = FastAPI(lifespan=lifespan, title="Auth service", version="1.0.0")


@app.post("/api/v1/test-auth")
async def test_auth(request : Request):
    logger.info("Authentication ....")
    logger.info("Auth service pricessed request succes")
    return Response(status_code=401, content="-")

@app.post("/health")
async def check_haelth(request : Request):
    logger.info(f"Health check auth")
    return Response(status_code=200, content="ok")
    

    
if __name__ == "__main__":
    uvicorn.run("auth.main:app", port=8001, host="0.0.0.0", reload=True)