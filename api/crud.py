from sqlalchemy.orm import Session
from datetime import datetime
from api.models import *
from api.schema import *

def loadTodoList(db : Session):
    todoList = db.query(TodoList).all()
    db.query()
    return todoList

def creatediary(db: Session, diary: CreateDiarySchema):
    diary = UserDiary(content = diary.content,
                      date = datetime.now())
    db.add(diary)
    db.commit()
