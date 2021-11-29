from homi import App, Server
from homi.extend.service import reflection_service, health_service

from proto import account_pb2
from db.database import *
from grpc_error.error import *
from command import *
from application import service


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
    req = SignUpCommand(
        email=request.email, password=request.password, en_name=request.en_name
    )

    stf, err = service.staff.register_staff(req)

    if err:
        set_exception(kwargs["context"], err)
        return account_pb2.CreateAccountResponse()

    return account_pb2.CreateAccountResponse()


@app.method(service_name)
def signin(request: account_pb2.LoginRequest, **kwargs) -> account_pb2.LoginResponse:
    req = SignInCommand(email=request.email, password=request.password)

    stf, err = service.staff.send_uuid(req)

    if err:
        set_exception(kwargs["context"], err)
        return account_pb2.LoginResponse()

    return account_pb2.LoginResponse(uuid=stf)


@app.method(service_name)
def update_account(
    request: account_pb2.UpdateAccountRequest, **kwargs
) -> account_pb2.UpdateAccountResponse:
    req = UpdateAccountCommand(
        uuid=request.uuid,
        origin_password=request.origin_password,
        update_password=request.update_password,
        check_password=request.check_password,
    )

    stf, err = service.staff.update_account(req)

    if err:
        set_exception(kwargs["context"], err)
        return account_pb2.UpdateAccountResponse()

    return account_pb2.UpdateAccountResponse()


if __name__ == "__main__":
    server = Server(app)
    server.run()
