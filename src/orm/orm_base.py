from abc import ABC, abstractmethod


class ORMBase(ABC):
    _caller_chain: str

    @abstractmethod 
    def save(self):
        print(self._caller_chain)

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def find(self):
        pass