from sqlalchemy import *
from sqlalchemy.orm import relationship
from config.database import Base


class Test(Base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True)


class UserInfo(Base):
    __tablename__ = "userinfo"

    id = Column(Integer, primary_key=True)

    userID = Column(String, nullable=False)
    userPassword = Column(String, nullable=False)

    userName = Column(String, nullable=False)
    userBirth = Column(Date, nullable=False)  # 수정 필요
    userEmail = Column(String, nullable=False)
    userGender = Column(Integer, nullable=False)

    userPpojakCoin = Column(Integer, nullable=False)
    userProfileName = Column(String, nullable=False)
    userProfileComment = Column(String, nullable=True)

    # Follower, Following column 추가
<<<<<<< HEAD
    
    # Diary =  relationship("UserDiary", back_populates="Diaryuser")



class UserDiary(Base):

    __tablename__= "userdiary"

    id = Column(Integer,primary_key=True)

    Date = Column(DateTime, nullable=False)
    Diarycontent = Column(Text,nullable=False)
    Response = Column(Text,nullable=False)
    Diarytodo = Column(String, nullable=True)
    
    # Diaryuserid = Column(Integer, ForeignKey('userinfo.id'))

    # Diaryuser =  relationship("UserInfo", back_populates="Diary")
=======


class TodoList(Base):
    __tablename__ = "todolist"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    todo = Column(String, nullable=False)
    check = Column(Boolean, nullable=False, default=False)
>>>>>>> d08863027d3a27e4f761c8727af28976237e0c80
