from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Request body
class ImageToVideoRequest(BaseModel):
    image_url: str
    style: str

# Your existing logic (UNCHANGED)
def image_to_video(image_url: str, style: str):
    print("Converting image to video...")
    print("Image:", image_url)
    print("Style:", style)

    output_video = f"https://example.com/image_to_video/{style}_animation.mp4"
    return output_video

# FastAPI endpoint
@router.post("/image-to-video")
async def image_to_video_api(data: ImageToVideoRequest):
    video_url = image_to_video(data.image_url, data.style)
    return {
        "status": "success",
        "video_url": video_url
    }