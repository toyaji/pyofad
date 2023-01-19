from pymongo import MongoClient
from pydantic import MongoDsn
from .orm_base import ORMBase

class MongoORM(ORMBase):
    clien: MongoClient | None = None

    def __init__(self) -> None:
        """config 받로고"""
        super().__init__()

    @classmethod
    def connect(cls, dsn: MongoDsn):
        cls.client = MongoClient(dsn)
        inf = cls.client.server_info()

        if hasattr(inf, 'version'):
            print(f"MongoDB version: {inf['version']}")

    def save(self, table: str, data: dict,):
        print(f"save {table} {data}")

    def load(self, table: str, data: dict,):
        pass

    def find(self, table: str, data: dict,):
        pass

    def from_orm(self):
        pass