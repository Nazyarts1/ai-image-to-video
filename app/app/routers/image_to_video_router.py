from fastapi import APIRouter, UploadFile, File
from app.image_to_video import generate_video_from_image

router = APIRouter()

@router.post("/image-to-video")
async def image_to_video_route(image: UploadFile = File(...)):
    video_path = generate_video_from_image(image)
    return {"message": "Video generated successfully", "video_path": video_path}
``