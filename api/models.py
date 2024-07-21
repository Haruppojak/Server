from sqlalchemy import *
from sqlalchemy.orm import relationship
from config.database import Base


class Test(Base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True)


class UserInfo(Base):
    __tablename__ = "userinfo"

    id = Column(Integer, primary_key=True)

    ID = Column(String, nullable=False)
    Password = Column(String, nullable=False)

    Name = Column(String, nullable=False)
    Birth = Column(Date, nullable=False)  # 수정 필요
    Email = Column(String, nullable=False)
    Gender = Column(Integer, nullable=False)

    PpojakCoin = Column(Integer, nullable=False)
    ProfileName = Column(String, nullable=False)
    ProfileComment = Column(String, nullable=True)

    # Follower, Following column 추가


class TodoList(Base):
    __tablename__ = "todolist"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    todo = Column(String, nullable=False)
    check = Column(Boolean, nullable=False, default=False)
