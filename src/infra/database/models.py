from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from src.infra.database.config import Base



class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)



class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date = Column(String)



class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index = True)
    name = Column(String) 
    email = Column(String) 
    password = Column(String)


class Habits(Base):
    __tablename__ = 'table'