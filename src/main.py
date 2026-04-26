from fastapi import FastAPI
from routers.base import base_router

app = FastAPI()

app.include_router(base_router)
