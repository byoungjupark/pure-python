from pydantic import BaseModel


class StaffData(BaseModel):
    email: str = ""
    password: str = ""
    en_name: str = ""
