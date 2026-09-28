from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Role(Base):
    __tablename__ = "taskflow_roles"

    id : Mapped[int] = mapped_column(
        primary_key=True,
        index=True
        )

    name : Mapped[String] = mapped_column(
        String(50),
        index=True,
        nullable=False,
        unique=True

    )