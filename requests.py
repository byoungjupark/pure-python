from pydantic import BaseModel


class StaffRequest(BaseModel):
    email: str = ""
    password: str = ""
    en_name: str = ""
