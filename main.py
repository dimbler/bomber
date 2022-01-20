from fastapi import FastAPI, Request, Depends
from typing import List
from sqlalchemy import select
from fastapi.responses import HTMLResponse, JSONResponse
from models import Song, SongCreate
from db import get_session
from sqlmodel import Session

app = FastAPI()

@app.get("/")
def read_root():
    return {"200": "Welcome To Heroku"}

@app.get("/ping", response_class=JSONResponse)
async def pong():
    return {"ping": "pong!"}

@app.get("/songs", response_model=List[Song])
def get_songs(session: Session = Depends(get_session)):
    result = session.execute(select(Song))
    songs = result.scalars().all()
    return [Song(name=song.name, artist=song.artist, id=song.id) for song in songs]