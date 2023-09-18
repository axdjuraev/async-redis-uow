from typing import Type, Generic
from axabc.db.async_repository import AbstractAsyncRepository
from async_redis_uow.session_maker.session import LazySession 
from .types import TIModel, TOModel


class BaseRepoCreator(AbstractAsyncRepository, Generic[TIModel, TOModel]):
    Schema: Type[TIModel]
    OSchema: Type[TOModel]

    __abstract__ = False

    def __init__(self, session: LazySession) -> None:
        super().__init__(session)

    def __init_subclass__(cls) -> None:
        if cls.__abstract__ or cls is BaseRepoCreator:
            types = getattr(cls, "__orig_bases__")[0].__args__
            cls.Schema, cls.OSchema = types

