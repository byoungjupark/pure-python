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

"""
AdminUser -> Staff
1. 회원가입 request 이메일, 비밀번호, 영어이름 response -
2. 로그인 : request 이메일 비밀번호 response uuid
이메일일치하는지, 비밀번호일치하는지(checkpw), uuid보내기
3. 비밀변경 : request uuid, 변경할 비밀번호 Response - 
uuid받는다, 업데이트할 비밀번호 암호화하기, 비밀번호 저장하기

해당이메일에 맞는 비밀번호인지
해당uuid에 맞는 비밀번호인지

typing, type hint 사용하기
"""


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
    req = UpdateAccountCommand(uuid=request.uuid, password=request.password)

    stf, err = service.staff.update_account(req)

    if err:
        set_exception(kwargs["context"], err)
        return account_pb2.UpdateAccountResponse()

    return account_pb2.UpdateAccountResponse()


if __name__ == "__main__":
    server = Server(app)
    server.run()
