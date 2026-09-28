from app.settings import settings


class Config:
    DATABASE_URL = settings.DATABASE_URL
    SECRET_KEY = settings.SECRET_KEY

    JWT_ALGORITHM = settings.JWT_ALGORITHM
    ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
    REFRESH_TOKEN_EXPIRE_DAYS = settings.REFRESH_TOKEN_EXPIRE_DAYS


config = Config()