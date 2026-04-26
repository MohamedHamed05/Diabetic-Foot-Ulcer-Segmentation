from fastapi import APIRouter
from fastapi.responses import JSONResponse
from model.schemes import SegmentationRequest
from base64 import b64encode

seg_router = APIRouter(prefix='/api/v1/segmentation')

@seg_router.post('/')
async def segment_image(request: SegmentationRequest):
    # Placeholder for actual segmentation logic
    return JSONResponse(content={"message": "Image segmented successfully"})