from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "sqlite:///./orders.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def init_db():
    Base.metadata.create_all(bind=engine)
    return engine


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
