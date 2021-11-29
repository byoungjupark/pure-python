from typing import Optional, Tuple, Type

from domain import *
from repository import StaffRepo
from grpc_error.exceptions import *
from command import *


class StaffService:
    def __init__(self, staff_repo: StaffRepo):
        self.staff_repo = staff_repo

    def register_staff(
        self, req: SignUpCommand
    ) -> Tuple[None, Optional[Type[Exception]]]:
        staff = Staff(req.email, req.password, req.en_name)

        if not staff.email_validate() or not staff.password_validate():
            return None, InvalidArgument

        if self.staff_repo.get_by_email(staff.email):
            return None, AlreadyExists

        self.staff_repo.register_staff(
            Staff(req.email, staff.hash_password, req.en_name)
        )
        return None, None

    def send_uuid(self, req: SignInCommand) -> Tuple[str, Optional[Type[Exception]]]:
        staff = self.staff_repo.get_by_email(req.email)
        if not staff:
            return "", NotFound

        if not staff.check_password(req.password):
            return "", UnAuthenticated

        return staff.uuid, None

    def update_account(
        self, req: UpdateAccountCommand
    ) -> Tuple[None, Optional[Type[Exception]]]:
        if not (req.update_password == req.check_password):
            return None, IncorrectPassword

        staff = self.staff_repo.get_by_uuid(req.uuid)

        if not staff.check_password(req.origin_password):
            return None, UnAuthenticated

        if staff.check_password(req.update_password):
            return None, SamePassword

        staff.password = req.update_password

        if not staff.password_validate():
            return None, InvalidArgument

        self.staff_repo.update_password(staff.uuid, staff.hash_password)

        return None, None
