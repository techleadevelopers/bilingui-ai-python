from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.lesson import Lesson
from app.utils.token import get_current_user

router = APIRouter(prefix="/lessons", tags=["Lessons"])


@router.get("/", response_model=List[dict])
def list_lessons(db: Session = Depends(get_db)):
    lessons = db.query(Lesson).all()
    return [
        {
          "id": l.id,
          "language": l.language,
          "level": l.level,
          "title": l.title,
          "type": l.type,
          "content": l.content,
        } for l in lessons
    ]


@router.get("/{lesson_id}", response_model=dict)
def get_lesson(lesson_id: int, db: Session = Depends(get_db)):
    lesson = db.query(Lesson).get(lesson_id)
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return {
        "id": lesson.id,
        "language": lesson.language,
        "level": lesson.level,
        "title": lesson.title,
        "type": lesson.type,
        "content": lesson.content,
    }
