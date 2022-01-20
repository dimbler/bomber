import os
from sqlmodel import create_engine, SQLModel, Session


DATABASE_URL = os.getenv("DATABASE_URL")  # or other relevant config var
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session