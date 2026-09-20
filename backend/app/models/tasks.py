from base import Base

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .projects import Projects


class Tasks(Base):

    __tablename__ = "taskflow_tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    project_id: Mapped[int] = mapped_column(ForeignKey('taskflow.projects.id', ondelete="CASCADE"))
    project = relationship(Projects, back_populates="task_ids")

    ''' Columns Need to create stage_id, sub_tasks, assignees, assigner '''



    