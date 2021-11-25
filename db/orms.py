from sqlalchemy import Column, Integer, String
from db.database import Base


class Staff(Base):
    __tablename__ = "staffs"
    id = Column(Integer, primary_key=True)
    email = Column(String(30))
    password = Column(String(200))
    en_name = Column(String(30))

    def __init__(self, email, password, en_name):
        self.email = email
        self.password = password
        self.en_name = en_name
