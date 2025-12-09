
from fastapi import FastAPI
from app.video import generate_video

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Video App is running"}

@app.post("/generate")
def create_video(prompt: str):
    result = generate_video(prompt)
    return {"status": "success", "video_url": result}