from fastapi import FastAPI
from app.routes import chatbot

app = FastAPI(title="Chatbot Service for QuizGame")

app.include_router(chatbot.router, prefix="/chatbot", tags=["Chatbot"])
