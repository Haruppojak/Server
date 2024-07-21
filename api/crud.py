from sqlalchemy.orm import Session
from datetime import datetime
from api.models import UserDiary
from api.schema import CreateDiarySchema, UpdatePostSchema, CreateCommentSchema

def creatediary(db: Session, diary: CreateDiarySchema):
    diary = UserDiary(content = diary.content,
                      date = datetime.now())
    db.add(diary)
    db.commit()