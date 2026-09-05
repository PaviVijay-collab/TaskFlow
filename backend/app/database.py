from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from config import config

engine = create_engine(config.DATABASE_URL)
sessionLocal = sessionmaker(bind=engine, autoflush=False)


def get_db():

    db = sessionLocal()

    try:
        yield db

    finally:
        db.close()