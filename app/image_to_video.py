from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ImageToVideoRequest(BaseModel):
    image_url: str
    style: str

def image_to_video(image_url: str, style: str):
    print("Converting image to video...")
    return f"https://example.com/{style}.mp4"

@router.post("/image-to-video")
async def image_to_video_api(data: ImageToVideoRequest):
    video_url = image_to_video(data.image_url, data.style)
    return {
        "status": "success",
        "video_url": video_url
    }