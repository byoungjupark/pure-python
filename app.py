from homi import App, Server
from homi.extend.service import reflection_service, health_service

from proto import account_pb2

from database import *
from models import User
from validate import hash_password, is_exist_email


Base.metadata.create_all(db.engine)


app = App(
    services=[
        account_pb2._ACCOUNT,
        reflection_service,
        health_service,
    ]
)
service_name = "account.Account"


@app.method(service_name)
def signup(
    request: account_pb2.CreateAccountRequest, **kwargs
) -> account_pb2.CreateAccountResponse:
    email = request.email
    password = request.password
    hashed_password = hash_password(email, password)

    with db.get_db() as session:
        email = is_exist_email(email)
        session.add(User(email, hashed_password))
        session.commit()

    return {"message": "Success", "status_code": 201}


if __name__ == "__main__":
    server = Server(app)
    server.run()
