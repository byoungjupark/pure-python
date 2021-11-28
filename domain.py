import re
import bcrypt


class Staff:
    def __init__(self, email: str, password: str, en_name: str):
        self.email = email
        self.password = password
        self.en_name = en_name

    def email_validate(self) -> bool:
        is_valid_email = re.compile("^[a-zA-Z0-9+-\_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
        return bool(is_valid_email.match(self.email))

    def password_validate(self) -> bool:
        is_valid_password = re.compile(
            "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@!%*#?&])[A-Za-z\d@!%*#?&]{8,}$"
        )
        return bool(is_valid_password.match(self.password))

    @property
    def hash_password(self) -> str:
        return bcrypt.hashpw(self.password.encode("utf-8"), bcrypt.gensalt()).decode()

    def check_password(self, req_password) -> bool:
        return bcrypt.checkpw(
            req_password.encode("utf-8"), self.password.encode("utf-8")
        )
