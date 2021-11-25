import re
import bcrypt


class Staff:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def email_validate(self) -> bool:
        is_valid_email = re.compile("^[a-zA-Z0-9+-\_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

        if not is_valid_email.match(self.email):
            return False
        return True

    def password_validate(self) -> bool:
        is_valid_password = re.compile(
            "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@!%*#?&])[A-Za-z\d@!%*#?&]{8,}$"
        )

        if not is_valid_password.match(self.password):
            return False
        return True

    def hash_password(self) -> str:
        hash_pw = bcrypt.hashpw(
            self.password.encode("utf-8"), bcrypt.gensalt()
        ).decode()
        return hash_pw
