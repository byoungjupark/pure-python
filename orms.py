import uuid

from sqlalchemy import Column, String
from db.database import Base
from domain import Staff


class StaffTable(Base):
    __tablename__ = "staff"
    uuid = Column(String(200), primary_key=True)
    email = Column(String(30), nullable=False)
    password = Column(String(200), nullable=False)
    en_name = Column(String(30), nullable=False)

    @staticmethod
    def to_model(st: "StaffTable") -> Staff:
        Staff.uuid = st.uuid
        return Staff(email=st.email, password=st.password, en_name=st.en_name)

    @staticmethod
    def from_model(s: Staff) -> "StaffTable":
        staff_table = StaffTable()
        staff_table.uuid = uuid.uuid4()
        staff_table.email = s.email
        staff_table.password = s.password
        staff_table.en_name = s.en_name
        return staff_table
