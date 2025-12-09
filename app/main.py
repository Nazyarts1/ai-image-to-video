
from fastapi import FastAPI
from app.image_to_video import image_to_video
app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Video App is running"}

@app.post("/generate")
def create_video(image_url: str):
    result = image_to_video(image_url)
    return {"status": "success", "video_url": result}