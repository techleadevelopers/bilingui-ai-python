# C:\Users\Paulo\Desktop\ai-school-language-app\backend\app\api\chat.py
from datetime import datetime
from fastapi import APIRouter, Depends
from app.schemas.chat_log import ChatRequest, ChatResponse
from app.services.mistral_service import mistral_service
from app.utils.token import get_current_user

# Prefix is set in main.py include_router("/chat"), so keep path root here
router = APIRouter(tags=["AI Chat"])


@router.post("/", response_model=ChatResponse)
async def chat_with_ai(
    payload: ChatRequest,
    current_user: dict = Depends(get_current_user),
):
    messages_list = [{"role": "user", "content": payload.message}]

    ai_response_text = await mistral_service.chat_with_mistral(
        messages=messages_list,
        context=payload.context,
    )

    return ChatResponse(
        id=1,  # TODO: persist and return real ID
        user_id=current_user["user_id"],
        message=payload.message,
        response=ai_response_text,
        timestamp=datetime.now(),
    )
