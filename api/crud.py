from sqlalchemy.orm import Session
from datetime import datetime
from api.models import *
from api.schema import *

def loadTodoList(db : Session):
    todoList = db.query(TodoList).all()
    db.query()
    return todoList

