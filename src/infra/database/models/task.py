from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.database.config import Base
from .associations import task_tag

class TaskModel(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship('User', back_populates='tasks')
    tags = relationship('Tag', secondary=task_tag, back_populates='tasks')