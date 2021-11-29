from pydantic import BaseModel


class SignUpCommand(BaseModel):
    email: str = ""
    password: str = ""
    en_name: str = ""


class SignInCommand(BaseModel):
    email: str = ""
    password: str = ""


class UpdateAccountCommand(BaseModel):
    uuid: str = ""
    origin_password: str = ""
    update_password: str = ""
    check_password: str = ""
