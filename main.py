from fastapi import FastAPI
from pydantic import BaseModel
import ollama
import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("OLLAMA_MODEL", "llama3.2")

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "LLM First API is running!",
        "model": MODEL_NAME
    }


@app.post("/chat")
def chat(request: ChatRequest):

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": request.message
            }
        ]
    )

    return {
        "response": response["message"]["content"]
    }