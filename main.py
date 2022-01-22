from fastapi import FastAPI, Request, Depends, Form
from typing import List
from sqlalchemy import select
from fastapi.responses import HTMLResponse, JSONResponse
from models import Song, SongCreate, Phone, PhoneCreate
from db import get_session
from sqlmodel import Session
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse('base.html', {"request": request})


@app.post("/add_phone")
async def add_phone(name: str = Form(...), phone: str = Form(...), session=Depends(get_session)):
    phone = Phone(name=name, phone=phone)
    session.add(phone)
    session.commit()
    session.refresh(phone)
    return phone


@app.get("/phones", response_model=List[Phone])
async def list_phones(session: Session = Depends(get_session)):
    result = session.execute(select(Phone))
    phones = result.scalars().all()
    return [Phone(name=phone.name, phone=phone.phone) for phone in phones]


@app.get("/ping", response_class=JSONResponse)
async def pong():
    return {"ping": "pong!"}


@app.get("/songs", response_model=List[Song])
def get_songs(session: Session = Depends(get_session)):
    result = session.execute(select(Song))
    songs = result.scalars().all()
    return [Song(name=song.name, artist=song.artist, year=song.year, id=song.id) for song in songs]


@app.post("/songs")
async def add_song(song: SongCreate, session=Depends(get_session)):
    song = Song(name=song.name, artist=song.artist, year=song.year)
    session.add(song)
    session.commit()
    session.refresh(song)
    return song
