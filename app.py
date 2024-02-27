"""
This module defines a FastAPI application for text-to-speech conversion.
"""
from datetime import datetime
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from gtts import gTTS

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def api_running():
    """
    Returns a JSON response indicating that the API is running.
    """
    return {"message": "API is running"}


@app.post("/text_to_speech/")
async def text_to_speech(
    text: str = Form(...), slow: bool = Form(...)
):
    """
    Converts the given text to speech using the specified language and speed.

    Parameters:
    - text (str): The text to be converted to speech.
    - slow (bool): Whether to generate speech at a slower speed.

    Returns:
    - dict: A dictionary containing the message "File created" after creating the speech file.
    """
    speed = "slow" if slow else "fast"
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"text_to_speech_{speed}_{timestamp}.wav"
    tts = gTTS(text=text, lang="no", slow=slow)
    tts.save(filename)
    return {"message": "File created"}
