from app.routers.image_to_video_router import router as image_to_video_router
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Load OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Home route
@app.get("/")
def home():
    return {"message": "AI Video Generator Backend Running"}

# Include router
app.include_router(image_to_video_router, prefix="/api")

# Video template sample route
@app.post("/video-template")
async def video_template():
    return {"status": "success", "message": "Video template applied"}