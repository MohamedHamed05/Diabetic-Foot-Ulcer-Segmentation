from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

base_router = APIRouter(prefix='/api/v1')

@base_router.get('/')
async def health(request: Request):
    model_status = "loaded" if hasattr(request.app.state, "model") else "not loaded"
    return JSONResponse(
        status_code=200,
        content = {
            'model_loaded' : model_status,
            'device' : str(next(iter(request.app.state.model.parameters())).device)
                       if hasattr(request.app.state, "model") else "none",
        }
    )