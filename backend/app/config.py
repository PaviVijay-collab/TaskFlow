from app.settings import settings


class Config:

    DATABASE_URL = settings.DATABASE_URL
    SECRET_KEY = settings.SECRET_KEY

    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

config = Config()
