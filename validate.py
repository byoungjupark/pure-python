import re
import bcrypt

from database import *
from models import *
from exceptions import *


class AccountValidate:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def email_validate(self):
        is_valid_email = re.compile("^[a-zA-Z0-9+-\_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

        if not is_valid_email.match(self.email):
            return None
        return True

    def password_validate(self):
        is_valid_password = re.compile(
            "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@!%*#?&])[A-Za-z\d@!%*#?&]{8,}$"
        )

        if not is_valid_password.match(self.password):
            return None
        return True

    def hash_password(self):
        valid_email = self.email_validate()
        valid_password = self.password_validate()

        if valid_email and valid_password:
            hashed_password = bcrypt.hashpw(
                self.password.encode("utf-8"), bcrypt.gensalt()
            ).decode()
            return hashed_password, None
        else:
            return None, InvalidArgument

    def is_exist_email(self):
        with db.get_db() as session:
            if session.query(User).filter(User.email == self.email).count() > 0:
                return None, AlreadyExists
            return self.email, None
