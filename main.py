from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

client = OpenAI()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "LLM First API is running!"}


@app.post("/chat")
def chat(request: ChatRequest):
    response = client.responses.create(
        model="gpt-5",
        input=request.message
    )

    return {
        "response": response.output_text
    }