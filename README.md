# Pure Python API
프레임워크를 사용하지 않고 파이썬 코드로 구현

## 기술스택
Python, MySQL

## 기능
1. 회원가입
- 이메일과 비밀번호 검증
- 중복 이메일 예외처리
2. 로그인
- 이메일 존재 여부와 비밀번호 일치 확인
- 로그인 성공 시 access_token 반환

## 디렉토리 구조

```
.
├── app.py
├── data.json
├── database.py
├── main.py
├── models.py
├── validate.py
```
