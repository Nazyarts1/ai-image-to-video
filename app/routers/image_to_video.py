from fastapi import APIRouter, UploadFile, File
from services.video_generator import generate_video

router = APIRouter()

@router.post("/image-to-video")
async def image_to_video(image: UploadFile = File(...)):
    video_path = generate_video(image)
    return {"video_url": video_path}
