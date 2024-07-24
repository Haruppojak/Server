from fastapi import APIRouter, Depends, Request, status, HTTPException, Form
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from api import crud, schema
from config.database import get_db

router = APIRouter(prefix="/api")

# @router.get("diary/write", response_class=HTMLResponse)
# async def diarywritehtml(request : Request):
#     return HTMLResponse(name="diary.html",request = request)

@router.post("/diary/write", status_code=status.HTTP_204_NO_CONTENT)
async def creatediarys(creatediarys : schema.CreateDiarySchema, db : Session=Depends(get_db)):
    crud.CreateDiary(db=db, diary=creatediarys)

# @router.post("/diary/write", status_code=status.HTTP_201_CREATED)
# async def creatediarys(creatediarys: schema.CreateDiarySchema, db: Session = Depends(get_db)):
#     new_diary = crud.CreateDiary(db=db, diary=creatediarys)
#     return JSONResponse(content=new_diary, status_code=status.HTTP_201_CREATED)

# @router.get("/diary/{diaryid}", response_class=HTMLResponse)
# async def readdiary(diaryid: int, db: Session = Depends(get_db)):
#     readdiaryall = crud.readdiary(db, diaryid=diaryid)
#     if readdiaryall is None:
#         raise HTTPException(status_code=404, detail="diary not found")
#     return readdiaryall

# @router.get("/post/create", response_class=HTMLResponse)
# async def post_create_html(request : Request):
#     return templates.TemplateResponse(name="post_create.html", request=request)
# 요런 느낌