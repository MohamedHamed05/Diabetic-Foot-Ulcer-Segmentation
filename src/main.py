from fastapi import FastAPI
from routers.base import base_router
from routers.seg_route import seg_router

app = FastAPI()

app.include_router(base_router)
app.include_router(seg_router)