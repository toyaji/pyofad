from .orm_base import ORMBase


class FirestoreORM(ORMBase):
    def __init__(self) -> None:
        """config 받로고"""
        super().__init__()

    def save(self):
        pass

    def load(self):
        pass

    def find(self):
        pass

    def from_orm(self):
        pass