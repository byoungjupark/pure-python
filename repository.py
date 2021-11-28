import abc
from domain import Staff


class StaffRepo(abc.ABC):
    @abc.abstractmethod
    def get_by_email(self, email: str):
        pass

    @abc.abstractmethod
    def register_staff(self, data: Staff) -> None:
        pass

    @abc.abstractmethod
    def find_uuid(self, email: str, password: str):
        pass

    @abc.abstractmethod
    def get_by_uuid(self, uuid: str):
        pass

    @abc.abstractmethod
    def update_password(self, uuid: str, password: str):
        pass
