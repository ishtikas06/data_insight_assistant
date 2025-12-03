from fastapi import APIRouter
from pathlib import Path
from typing import Union
from src.service.service import generate_insight
from src.utils.prompts import Prompt
from src.utils.constants import AnswerType
from src.schema.models import QuitResponse, TechnicalResponse, TextualResponse, UserInput

router = APIRouter()

@router.post("/analyze/", response_model=Union[TextualResponse, TechnicalResponse, QuitResponse])
async def analyze_data(input: UserInput):

    insights = await generate_insight(input)
    return insights