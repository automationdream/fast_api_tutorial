from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {
        "request": request,
    })


@app.post("/stock")
def dashboard():
    return {
        "code": "success",
        "message": "stock created"
    }
