import grpc
from grpc._server import _Context
from homi import App, Server
from homi.extend.service import reflection_service, health_service

from proto import account_pb2

from database import *
from models import User
from validate import AccountValidate
from error import *

Base.metadata.create_all(db.engine)
# acc = AccountValidate()

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
    acc = AccountValidate(email, password)

    pw, pw_error = acc.hash_password()
    em, em_error = acc.is_exist_email()

    if pw_error:
        set_exception(kwargs["context"], pw_error)
        return account_pb2.CreateAccountResponse()
    elif em_error:
        set_exception(kwargs["context"], em_error)
        return account_pb2.CreateAccountResponse()
    else:
        with db.get_db() as session:
            session.add(User(em, pw))
            session.commit()
            return account_pb2.CreateAccountResponse()


if __name__ == "__main__":
    server = Server(app)
    server.run()
