import asyncio
from random import randint
from axabc.db import BaseSchema
from axabc.db.repo_collector import BaseRepoCollector
from axabc.db.async_uowf import AsyncUOWFactory

from async_redis_uow.session_maker.session_maker import RedisLazySessionMaker
from async_redis_uow.repository.common import BaseRepository


class Users(BaseSchema):
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


class UsersRepository(BaseRepository[Users, Users]):
    pass


class RepoCollection(BaseRepoCollector):
    users: UsersRepository


async def main():
    url = 'redis://:dKIuag6QkaqFRZYTBRXtg1Np6C7c6EJG@redis-13670.c261.us-east-1-4.ec2.cloud.redislabs.com:13670'
    url = 'redis://localhost:6379'
    uowf = AsyncUOWFactory(RepoCollection, RedisLazySessionMaker.from_url(url))
    users = []
    async with uowf() as uow:
        for i in range(1, 10):
            user = uow.repo.users.Schema(
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
            users.append(user)
            await uow.repo.users.add(user)

        await uow.save()
        await uow.repo.users.delete(5)
        await uow.save()
        users = await uow.repo.users.page(count=5, page=1)
        assert len(users) == 5
        assert users[0].id == 1
        assert users[-1].id == 6

if __name__ == "__main__":
    asyncio.run(main())

