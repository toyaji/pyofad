from src.model import *


def test_fadmodel_in_accordance_with_pydantic():
    b = 'qkdnf'
    c = TestDocument(a='wow', b=3)
    c.save()
    print(c)
    print(c.dict())

    d = c.parse_obj({'a': 'test', 'b': 23})
    print(c.schema())
    print(d)
    assert isinstance(c, BaseModel)

if __name__ == '__main__':
    test_fadmodel_in_accordance_with_pydantic()