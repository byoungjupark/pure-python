from database import *
from orms import Staff
from repository import StaffRepo
from data import StaffData


class StaffModel(StaffRepo):
    def is_exist_email(self, data: StaffData) -> bool:
        print(data.email)
        with db.get_db() as session:
            if session.query(Staff).filter(Staff.email == data.email).count() > 0:
                return True
            return False

    def register_staff(self, data: StaffData) -> None:
        with db.get_db() as session:
            session.add(
                Staff(
                    Staff.email == data.email,
                    Staff.password == data.password,
                    Staff.en_name == data.en_name,
                )
            )
            session.commit()
