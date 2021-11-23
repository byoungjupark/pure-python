import re
import bcrypt

from database import *
from models import *


def email_validate(e):
    email = re.compile("^[a-zA-Z0-9+-\_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    if not email.match(e):
        raise Exception("non valid email")

    return True


def password_validate(p):
    password = re.compile(
        "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@!%*#?&])[A-Za-z\d@!%*#?&]{8,}$"
    )

    if not password.match(p):
        raise Exception("non valid password")

    return True


def hash_password(email, password):
    valid_email = email_validate(email)
    valid_password = password_validate(password)

    if valid_email and valid_password:
        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"), bcrypt.gensalt()
        ).decode()
        return hashed_password


def is_exist_email(email):
    with db.get_db() as session:
        if session.query(User).filter(User.email == email).count() > 0:
            raise Exception("Existed email already")
        else:
            return email
