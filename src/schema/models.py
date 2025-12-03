from pydantic import BaseModel
from typing import Dict, Any, Optional, List
from src.utils.constants import AnswerType

class TechnicalResponse(BaseModel):
    response: Dict[str, Any]

class TextualResponse(BaseModel):
    response: str

class QuitResponse(BaseModel):
    message: str

# class LLMResponse(BaseModel):
#     user_query: str
#     response: Dict[str, Any]

class UserInput(BaseModel):
    session_id: int
    query: str
    answer_type: Optional[AnswerType] = None