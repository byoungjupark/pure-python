from models import StaffModel
from service import StaffService


class Application:
    def __init__(self, staff_repo: StaffModel = StaffModel()):
        self.staff = StaffService(staff_repo)


service = Application()
