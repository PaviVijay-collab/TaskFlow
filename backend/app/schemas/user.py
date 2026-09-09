from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role_id: int


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime
    role_id: int

    model_config = {
        "from_attributes": True
    }