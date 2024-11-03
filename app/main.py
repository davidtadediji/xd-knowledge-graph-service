from fastapi import FastAPI
from app.routers import graph_generator
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = FastAPI(title="Knowledge Graph Service")

app.include_router(graph_generator.router)
