from abc import ABC, abstractmethod, abstractclassmethod
from typing import Type, Any
from pymongo import MongoClient
class ORMResult:
    status: int
    message: str

class ORMBase(ABC):
    """ORM Base Class"""
    client : Type[MongoClient|None] = None

    @abstractclassmethod
    def connect(self, client: Any):
        pass

    @abstractmethod 
    def save(self, table: str, data: dict,)->ORMResult:
        pass

    @abstractmethod
    def load(self, table: str, data: dict,)->ORMResult:
        pass

    @abstractmethod
    def find(self, table: str, data: dict,):
        pass

    @abstractmethod
    def from_orm(self):
        pass
