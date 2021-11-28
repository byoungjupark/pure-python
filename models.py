from sqlalchemy import select, update

from db.database import db
from orms import StaffTable
from repository import StaffRepo
from domain import Staff


class StaffModel(StaffRepo):
    def get_by_email(self, email: str):
        with db.get_db() as session:
            staff = session.execute(
                select(StaffTable).where(StaffTable.email == email)
            ).scalar()

            if not staff:
                return False

            return StaffTable.to_model(staff)

    def register_staff(self, data: Staff) -> None:
        with db.get_db() as session:
            session.add(StaffTable.from_model(data))
            session.commit()

    def find_uuid(self, email: str, password: str):
        with db.get_db() as session:
            staff = session.execute(
                select(StaffTable).where(
                    StaffTable.email == email, StaffTable.password == password
                )
            ).scalar()
            return StaffTable.to_model(staff)

    def get_by_uuid(self, uuid: str):
        with db.get_db() as session:
            staff = session.execute(
                select(StaffTable).where(StaffTable.uuid == uuid)
            ).scalar()

            if not staff:
                return False

            return StaffTable.to_model(staff)

    def update_password(self, uuid: str, password: str):
        with db.get_db() as session:
            session.execute(
                update(StaffTable)
                .where(StaffTable.uuid == uuid)
                .values(password=password)
            )

            session.commit()
