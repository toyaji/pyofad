import yaml

from pydantic import BaseModel, PrivateAttr, BaseSettings, PostgresDsn, AnyUrl
from typing import Type, Any
from pathlib import Path

from .orm import *


def fad_factory(cls: Type[ORMBase]=MongoORM):
    """Factory function to create a FADModel class according to given ORM class."""
    class FADModel(BaseModel, cls):
        _table: str = PrivateAttr()
        _caller_chain: str | None = PrivateAttr()

        def __init__(self, table=None, caller_chain=None, **data: Any) -> None:
            super().__init__(**data)
            self._table = table
            self._caller_chain = caller_chain

    return FADModel

class MongoDsnSrv(AnyUrl):
    """MongoDB DSN with srv support."""
    allowed_schemes = {'mongodb+srv', 'mongodb'}

class FADConfig(BaseSettings):
    """DB dsn config class."""
    mongo_url: MongoDsnSrv
    postgresql_url: PostgresDsn

class FADSchema(BaseModel):
    _mongo: Type[ORMBase] = PrivateAttr(default_factory=MongoORM)
    _postgre: Type[ORMBase] = PrivateAttr(default_factory=PostgresqlORM)
    #_firestore: Type[ORMBase] = PrivateAttr(default_factory=FirestoreORM)
    _table: str = PrivateAttr()
    _default_orm: str = PrivateAttr(default="mongo")
    _default_conf_path: str = PrivateAttr(default="config/conf.yaml")
    _conf: FADConfig = PrivateAttr()

    class Config:
        orm_mode = True

    def __load_conf__(cls, config: FADConfig=None):
        if isinstance(config, (str, Path)) and Path(config).exists():
            with open(config) as f:
                _conf = yaml.load(f, Loader=yaml.FullLoader)
                config = FADConfig(
                    mongo_url=_conf["orm"]["mongo"],
                    postgresql_url=_conf["orm"]["postgres"],
                )
            # set default config path to given str or Path
            cls._default_conf_path = str(config)
        elif config is None and Path(cls._default_conf_path).exists():
            with open(cls._default_conf_path) as f:
                _conf = yaml.load(f, Loader=yaml.FullLoader)
                config = FADConfig(
                    mongo_url=_conf["orm"]["mongo"],
                    postgresql_url=_conf["orm"]["postgres"],
                )
        elif config is not None and isinstance(config, FADConfig):
            pass
        else:
            raise ValueError("config must be a FADConfig instance or default config path must exist.")

        cls._conf = config
        if config.mongo_url is not None:
            cls._mongo.connect(config.mongo_url)
        if config.postgresql_url is not None:
            cls._postgre.connect(config.postgresql_url)
        #if config.firestore_url is not None:
        #   cls._firestore.connect(config.firestore_url

    def __init__(self, **data: Any) -> None:
        self._table = self.__class__.__name__
        super().__init__(**data)

    @property
    def default_orm(self):
        return self._default_orm

    @default_orm.setter
    def default_orm(self, orm: str):
        if not isinstance(orm, str):
            raise TypeError(f"orm name must be a string, not {type(orm)}")
        if not hasattr(self, f"_{orm}"):
            raise AttributeError(f"ORM {orm} is not supported")
        self._default_orm = orm

    def load_conf(self, config: FADConfig|Path=None):
        self.__load_conf__(config)

    def save(self, orm: str = None, **kwargs):
        orm = f"_{self._default_orm}" if orm is None else f"_{orm}"
        if not hasattr(self, orm):
            raise AttributeError(f"ORM {orm} is not supported")
        orm: Type[ORMBase] = getattr(self, orm)
        res = orm.save(self._table, self.dict())
        return res

    def load(self, orm: str = None, **kwargs):
        orm = f"_{self._default_orm}" if orm is None else f"_{orm}"
        if not hasattr(self, orm):
            raise AttributeError(f"ORM {orm} is not supported")
        orm: Type[ORMBase] = getattr(self, orm)
        res = orm.load(self._table, self.dict())
        return res

    def find(self, orm: str = None, **kwargs):
        orm = f"_{self._default_orm}" if orm is None else f"_{orm}"
        if not hasattr(self, orm):
            raise AttributeError(f"ORM {orm} is not supported")
        orm: Type[ORMBase] = getattr(self, orm)
        res = orm.find(self._table, self.dict())
        return res