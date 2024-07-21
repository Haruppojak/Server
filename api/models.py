from sqlalchemy import *
from sqlalchemy.orm import relationship
from config.database import Base


class Test(Base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True)