from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def dashboard():
    return {"Dashboard": "Home Page"}

