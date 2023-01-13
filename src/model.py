from pydantic import BaseModel, PrivateAttr
from typing import Any
from .orm.orm_base import ORMBase
from typing import TypeVar, ClassVar, Generic, Self

class FADModel(BaseModel, ORMBase):
    _table: str = PrivateAttr()
    _caller_chain: str | None = PrivateAttr()

    def __init__(__pydantic_self__, table=None, caller_chain=None, **data: Any) -> None:
        super().__init__(**data)
        __pydantic_self__._table = table
        __pydantic_self__._caller_chain = caller_chain


class TestDocument(FADModel):
    a: str
    b: int
