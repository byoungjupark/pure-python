import json

from database import *
from app import *

# mock data 불러오기
BASE_DIR = os.path.dirname(__file__)
MOCK_DATA = os.path.join(BASE_DIR, "data.json")
data = json.loads(open(MOCK_DATA).read())

# 메타데이터를 보관하는 Base를 이용해 스키마 생성하기
Base.metadata.create_all(db.engine)

email = data["email"]
password = data["password"]

signup(email, password)
signin(email, password)
