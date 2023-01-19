from src.model import *
from pymongo import MongoClient


class TestDocument(fad_factory()):
    a: str
    b: int

class TestModel(BaseModel):
    a: str
    b: int
class TestSchema(FADSchema):
    a: str
    b: int
    c: BaseModel

def test_schemamodel_in_accordance_with_pydantic():
    b = 'qkdnf'
    c = TestSchema(a='wow', b=3, c=TestModel(a='wow', b=3))
    c.load_conf()
    c.save()
    print(c)
    print(c.dict())

    d = c.parse_obj({'a': 'test', 'b': 23, 'c': {'a': 'test', 'b': 23}})
    print(c.schema())
    print(d)
    assert isinstance(c, BaseModel)

def test_mongo_connect():
    client = MongoClient('mongodb+srv://toyaji:qkdnf87!@cluster0.5ahvecd.mongodb.net/test')
    inf = client.server_info()
    print(inf)
    assert True