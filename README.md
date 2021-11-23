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

## 디렉토리 구조

```
.
├── README.md
├── app.py
├── database.py
├── models.py
├── proto
│   ├── account.proto
│   ├── account_pb2.py
│   └── account_pb2_grpc.py
├── requirements.txt
├── validate.py
```
