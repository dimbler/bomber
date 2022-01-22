from typing import Optional
from sqlmodel import SQLModel, Field


class PhoneBase(SQLModel):
    name: str
    phone: str


class Phone(PhoneBase, table=True):
    id: int = Field(default=None, primary_key=True)


class PhoneCreate(PhoneBase):
    pass


class SongBase(SQLModel):
    name: str
    artist: str
    year: Optional[int] = None


class Song(SongBase, table=True):
    id: int = Field(default=None, primary_key=True)


class SongCreate(SongBase):
    pass
