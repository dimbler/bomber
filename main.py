from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from models import Song, SongCreate

app = FastAPI()

@app.get("/")
def read_root():
    return {"200": "Welcome To Heroku"}

@app.get("/ping", response_class=JSONResponse)
async def pong():
    return {"ping": "pong!"}
