from fastapi import FastAPI
from pydantic import BaseModel
import ollama

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "LLM First API is running!"}


@app.post("/chat")
def chat(request: ChatRequest):

    response = ollama.chat(
        model="llama3.2",
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