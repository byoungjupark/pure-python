import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager


DB = {
    "user": os.environ.get("DB_USER", "root"),
    "password": os.environ.get("DB_PASSWORD", "password"),
    "host": os.environ.get("DB_HOST", "localhost"),
    "port": os.environ.get("DB_PORT", "3306"),
    "name": os.environ.get("DB_NAME", "test"),
}


class Database:
    def __init__(self):
        self.engine = create_engine(
            f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['name']}"
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
