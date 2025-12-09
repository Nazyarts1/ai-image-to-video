
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/")
def home():
    return {"message": "AI Video Generator Backend Running"}

@app.post("/image-to-video")
async def image_to_video(image: UploadFile = File(...)):
    try:
        return {"status": "success", "message": "Video generated from image"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/video-template")
async def video_template():
    return {"status": "success", "message": "Video template applied"}