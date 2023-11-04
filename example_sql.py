import asyncio
from datetime import datetime
from random import randint
from pydantic import BaseModel
from axabc.db.repo_collector import BaseRepoCollector
from axabc.db.async_uowf import AsyncUOWFactory


from axsqlalchemy.settings import Settings as DBSettings
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from axsqlalchemy.model import BaseTable, Base as TablesBase
from axsqlalchemy.repository import BaseRepository as SQLBaseRepository
from axsqlalchemy.utils.creation import create_models
import sqlalchemy as sa




class UsersModel(BaseTable):
    id = sa.Column(sa.Integer, primary_key=True)
    name1 = sa.Column(sa.String(256))
    name2 = sa.Column(sa.String(256))
    name3 = sa.Column(sa.String(256))
    name4 = sa.Column(sa.String(256))
    name5 = sa.Column(sa.String(256))
    name6 = sa.Column(sa.String(256))
    name7 = sa.Column(sa.String(256))
    name8 = sa.Column(sa.String(256))
    name9 = sa.Column(sa.String(256))
    name10 = sa.Column(sa.String(256))
    name11 = sa.Column(sa.String(256))
    name12 = sa.Column(sa.String(256))
    name13 = sa.Column(sa.String(256))
    name14 = sa.Column(sa.String(256))


class Users(BaseModel):
    id: int
    name1: str
    name2: str
    name3: str
    name4: str
    name5: str
    name6: str
    name7: str
    name8: str
    name9: str
    name10: str
    name11: str
    name12: str
    name13: str
    name14: str
    
    class Config:
        orm_mode = True


class UsersRepository(SQLBaseRepository[UsersModel, Users, Users]):
    pass


class RepoCollection(BaseRepoCollector):
    users: UsersRepository


async def main():
    settings = DBSettings(DB_DRIVERNAME='sqlite+aiosqlite', DB_DATABASE='db.sqlite3')
    engine = create_async_engine(settings.db_connection_string)
    session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)  # type: ignore
    uowf = AsyncUOWFactory(RepoCollection, session_maker)  # type: ignore
    start_time = datetime.now()
    await create_models(engine, TablesBase)
    async with uowf() as uow:
        for i in range(1, 10):
            await uow.repo.users.add(
                uow.repo.users.Schema(
                    id=i,
                    name1=str(randint(123456789, 999999999)),
                    name2=str(randint(123456789, 999999999)),
                    name3=str(randint(123456789, 999999999)),
                    name4=str(randint(123456789, 999999999)),
                    name5=str(randint(123456789, 999999999)),
                    name6=str(randint(123456789, 999999999)),
                    name7=str(randint(123456789, 999999999)),
                    name8=str(randint(123456789, 999999999)),
                    name9=str(randint(123456789, 999999999)),
                    name10=str(randint(123456789, 999999999)),
                    name11=str(randint(123456789, 999999999)),
                    name12=str(randint(123456789, 999999999)),
                    name13=str(randint(123456789, 999999999)),
                    name14=str(randint(123456789, 999999999)),
                )
            )
        await uow.save()
        for i in range(1, 10):
            user = await uow.repo.users.get(i)
            print(user)

    spend_time = (datetime.now() - start_time).total_seconds()
    print(f"{spend_time=}")
        

if __name__ == "__main__":
    asyncio.run(main())

