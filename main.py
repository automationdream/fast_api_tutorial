from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from pydantic import BaseModel

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")


class StockRequest(BaseModel):
    symbol: str

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {
        "request": request,
    })


@app.post("/stock")
def create_stock(stock_request: StockRequest):
    '''
    create a stock and store it in the database
    '''

    return {
        "code": "success",
        "message": "stock created"
    }
