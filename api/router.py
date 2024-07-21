from fastapi import APIRouter, Depends, Request, status, HTTPException, Form
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from api import crud, schema
from config.database import get_db

router = APIRouter(prefix="/api")
templates = Jinja2Templates(directory="templates")
