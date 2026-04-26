from pydantic import BaseModel, Field

class SegmentationRequest(BaseModel):
    image: bytes = Field(..., description="The image to be segmented, encoded as bytes.")

class SegmentationResponse(BaseModel):
    pass