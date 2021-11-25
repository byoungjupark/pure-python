import abc
from data import StaffData


class StaffRepo(abc.ABC):
    @abc.abstractmethod
    def is_exist_email(self, data: StaffData) -> bool:
        pass

    @abc.abstractmethod
    def register_staff(self, data: StaffData) -> None:
        pass
