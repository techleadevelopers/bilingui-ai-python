# C:\Users\Paulo\Desktop\ai-school-language-app\backend\app\schemas\chat_log.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ChatRequest(BaseModel):
    message: str
    lesson_id: Optional[int] = None # Optional, if chat is sometimes not tied to a lesson
    # Add any other fields your chat endpoint expects, e.g., user_id

class ChatResponse(BaseModel):
    id: int
    user_id: int
    message: str
    response: str # AI's response
    timestamp: datetime
    lesson_id: Optional[int] = None

    # Pydantic V2 config if this schema interacts with SQLAlchemy ORM
    # from pydantic import ConfigDict
    # model_config = ConfigDict(from_attributes=True)