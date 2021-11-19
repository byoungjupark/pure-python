import re


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
