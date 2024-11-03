from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routers import graph_generator
from dotenv import load_dotenv
import os
from app.utils.logger import logger
from contextlib import asynccontextmanager
import asyncio


load_dotenv()  # Load environment variables from .env file


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Document Processor Service...")
    try:
        yield
    except asyncio.CancelledError:
        logger.warning("Lifespan task was cancelled.")
    finally:
        logger.info("Shutting down Document Processor Service...")

app = FastAPI(title="Knowledge Graph Service",  lifespan=lifespan,
)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"},
    )

app.include_router(graph_generator.router)
