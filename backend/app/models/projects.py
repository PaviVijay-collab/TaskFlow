from base import Base

from enum import Enum
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .tasks import Tasks

class Status(str, Enum):
    NEW = "New"
    ONGOING = "Ongoing"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class Projects(Base):
    __tablename__ = 'taskflow_projects'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[Status] = mapped_column(SQLEnum(Status), nullable=False, default="NEW")
    description: Mapped[str] = mapped_column()

    task_ids = relationship(Tasks, back_populates="project")

    ''' Columns Need to create team_members '''

    

