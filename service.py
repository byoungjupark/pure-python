from typing import Optional, Tuple, Type

import domain
from repository import StaffRepo
from exceptions import *
from requests import StaffRequest
from data import StaffData


class StaffService:
    def __init__(self, repo: StaffRepo):
        self.repo = repo

    def register_staff(
        self, req: StaffRequest
    ) -> Tuple[None, Optional[Type[Exception]]]:
        staff = domain.Staff(req.email, req.password)

        if not staff.email_validate() or not staff.password_validate():
            return None, InvalidArgument

        hash_password = staff.hash_password()
        staff_data = StaffData(
            email=req.email, password=hash_password, en_name=req.en_name
        )

        if self.repo.is_exist_email(data=staff_data):
            print(staff_data)
            return None, AlreadyExists

        self.repo.register_staff(data=staff_data)

        return None
