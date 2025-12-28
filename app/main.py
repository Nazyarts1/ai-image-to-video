from from fastapi import FastAPI
from app.image_to_video import router as image_to_video_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Video Generator Backend Running"}

# Include router
app.include_router(image_to_video_router, prefix="/api")

# Video template sample route
@app.post("/video-template")
async def video_template():
    return {
        "status": "success",
        "message": "Video template applied"
    }