import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager


DB = {
    "user": os.environ["DB_USER"],
    "password": os.environ["DB_PASSWORD"],
    "host": os.environ["DB_HOST"],
    "port": os.environ["DB_PORT"],
    "name": os.environ["DB_NAME"],
}


class Database:
    def __init__(self):
        self.engine = create_engine(
            f"mysql+mysqldb://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['name']}?charset=utf8"
        )
        self._session = sessionmaker(self.engine)

    @contextmanager
    def get_db(self):
        session = self._session()
        try:
            yield session
        finally:
            session.close()


db = Database()
Base = declarative_base()
