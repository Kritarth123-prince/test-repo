from fastapi import FastAPI
from pydantic import BaseModel
from rules import get_response

app = FastAPI(title="Rule Based Chatbot API")


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Rule-Based Chatbot API"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    reply = get_response(request.message)

    return {
        "success": True,
        "user_message": request.message,
        "reply": reply
    }
