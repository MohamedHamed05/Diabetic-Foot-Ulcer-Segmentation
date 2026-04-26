from fastapi import APIRouter
from fastapi.responses import JSONResponse

base_router = APIRouter(prefix='/api/v1')

@base_router.get('/')
async def health():
    return JSONResponse(
        status_code=200,
        content = {
            'app' : 'DFU_Segmentation',
            'version' : 1.0
        }
    )