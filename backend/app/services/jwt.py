from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt
from app.config import config


def create_access_token(data: dict) -> str:
    to_encode = data.copy()

    expire = (
        datetime.now(timezone.utc)
        + timedelta(
            minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    to_encode.update({
        "exp": expire,
        "type": "access"
    })

    return jwt.encode(
        to_encode,
        config.SECRET_KEY,
        algorithm=config.JWT_ALGORITHM
    )


def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()

    expire = (
        datetime.now(timezone.utc)
        + timedelta(
            days=config.REFRESH_TOKEN_EXPIRE_DAYS
        )
    )

    to_encode.update({
        "exp": expire,
        "type": "refresh"
    })

    return jwt.encode(
        to_encode,
        config.SECRET_KEY,
        algorithm=config.JWT_ALGORITHM
    )


def decode_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(
            token,
            config.SECRET_KEY,
            algorithms=[config.JWT_ALGORITHM]
        )

        if payload.get("type") != "access":
            return {}

        return payload

    except JWTError:
        return {}


def decode_refresh_token(token: str) -> dict:
    try:
        payload = jwt.decode(
            token,
            config.SECRET_KEY,
            algorithms=[config.JWT_ALGORITHM]
        )

        if payload.get("type") != "refresh":
            return {}

        if payload.get("type") != "refresh":
            return {}

        return payload

    except JWTError:
        return {}