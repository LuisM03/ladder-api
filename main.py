from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from schemas.question import questionSchema, questionsSchema
from db import db

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Definir el modelo de los datos que se van a manipular
class Question(BaseModel):
    id: Optional[str]
    question: str
    answer: str
    category: str
    
@app.get('/questions')
async def get_all_questions():
    questions = db.questions.find()
    return questionsSchema(questions)