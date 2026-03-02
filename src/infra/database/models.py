from sqlalchemy import Column, Integer, String, ForeignKey, Table
from src.infra.database.config import Base
from sqlalchemy.orm import relationship
from sqlalchemy import LargeBinary


task_tag = Table(
    'task_tag',
    Base.metadata,
    Column('task_id', Integer, ForeignKey('task.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)


class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('user.id', name='fk_user'))

    user = relationship('User', back_populates='tags')
    tasks = relationship('Task', secondary=task_tag, back_populates='tags')


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship('User', back_populates='tasks')
    tags = relationship('Tag', secondary=task_tag, back_populates='tasks')


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    cellphone = Column(String)
    photo = Column(LargeBinary)

    tasks = relationship('Task', back_populates='user')
    tags = relationship('Tag', back_populates='user')