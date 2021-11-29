# Pure Python API
프레임워크를 사용하지 않고 파이썬 코드로 구현

## 기술스택
Python, MySQL, grpc
<br>

grpc는 아래 링크 참조
<br>
[homi](https://github.com/spaceone-dev/homi)

## 기능
회원가입
- 이메일과 비밀번호 검증
- 중복 이메일 예외처리

로그인
- 이메일, 비밀번호 일치여부
- uuid response

비밀번호 변경
- 비밀번호 유효성 검사

## 디렉토리 구조
```
.
├── ./Dockerfile
├── ./README.md
├── ./app.py
├── ./application.py
├── ./command.py
├── ./db
│   └── ./db/database.py
├── ./docker-compose.yml
├── ./domain.py
├── ./grpc_error
│   ├── ./grpc_error/error.py
│   └── ./grpc_error/exceptions.py
├── ./models.py
├── ./orms.py
├── ./proto
│   ├── ./proto/account.proto
│   ├── ./proto/account_pb2.py
│   └── ./proto/account_pb2_grpc.py
├── ./repository.py
├── ./requirements.txt
├── ./service.py
```
