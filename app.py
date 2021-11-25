from homi import App, Server
from homi.extend.service import reflection_service, health_service

from proto import account_pb2
from db.database import *
from grpc_error.error import *
from service import StaffService
from requests import *

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
회원가입 (이메일, 비밀번호, 영어이름)
로그인
비밀변경

구조분리하기
1. app/main: 엔드포인트, request,response 보내는 곳, 에러있으면 에러response
request key값들을 변수로 넣어서 service함수 파라미터로 넣어줌
2. service(application): db추상화repo 불러오기, domain 함수 불러오기, domain 함수 실행 하는 곳
service 함수 파라미터로 받아서 
3. domain model : 비즈니스 로직 함수 선언하는 곳

4. repository 추상화 : db 껍데기
5. models: repo 클래스 상속받아서 db 실제로 여는 곳

orms : 모델링 하는 곳
to_model : orm 

typing, type hint 사용하기
"""


@app.method(service_name)
def signup(
    request: account_pb2.CreateAccountRequest, **kwargs
) -> account_pb2.CreateAccountResponse:
    req = StaffRequest(
        email=request.email, password=request.password, en_name=request.en_name
    )

    stf, err = StaffService.register_staff(req)

    if err:
        set_exception(kwargs["context"], err)
        return account_pb2.CreateAccountResponse()
    return account_pb2.CreateAccountResponse()


if __name__ == "__main__":
    server = Server(app)
    server.run()
