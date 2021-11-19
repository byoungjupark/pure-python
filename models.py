from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(30))
    password = Column(String(200))

    def __init__(self, email, password):
        self.email = email
        self.password = password
