from .orm_base import ORMBase
from typing import Any

class PostgresqlORM(ORMBase):
    def __init__(self) -> None:
        """config 받로고"""
        super().__init__()

    def connect(self, client: Any):
        pass

    def save(self, table: str, data: dict,):
        pass

    def load(self, table: str, data: dict,):
        pass

    def find(self, table: str, data: dict,):
        pass

    def from_orm(self):
        pass