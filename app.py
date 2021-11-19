import bcrypt
import jwt
import os

from database import db
from models import User
from validate import *


def signup(e, p):
    email = email_validate(e)
    password = password_validate(p)

    if email and password:
        hashed_password = bcrypt.hashpw(p.encode("utf-8"), bcrypt.gensalt()).decode()

        with db.get_db() as session:
            if session.query(User).filter(User.email == e).count() > 0:
                return {"message": "existed email"}
            session.add(User(e, hashed_password))
            session.commit()

    return {"message": "Success", "status_code": 201}


def login(e, p):
    with db.get_db() as session:
        user = session.query(User).filter(User.email == e).first()

        if not user:
            return {"message": "non exist email", "status_code": 400}

        hashed_password = user.password
        check_pw = bcrypt.checkpw(p.encode("utf-8"), hashed_password.encode("utf-8"))

        if check_pw:
            token = jwt.encode(
                {"id": user.id}, os.environ["PRIVATE_KEY"], algorithm="HS256"
            )

            return {"token": token}
