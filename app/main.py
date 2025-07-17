from fastapi import FastAPI
from app.routes import chatbot
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Chatbot Service for QuizGame")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or "*" to allow all for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(chatbot.router, prefix="/chatbot", tags=["Chatbot"])
