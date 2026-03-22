from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.orm import relationship
from src.infra.database.config import Base

class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    cellphone = Column(String)
    photo = Column(LargeBinary)

    tasks = relationship('Task', back_populates='user')
    tags = relationship('Tag', back_populates='user')