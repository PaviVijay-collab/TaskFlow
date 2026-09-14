from app.settings import settings


class Config:

    DATABASE_URL = settings.DATABASE_URL
    SECRET_KEY = settings.SECRET_KEY



config = Config()
