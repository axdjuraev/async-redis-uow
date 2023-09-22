from redis.commands.json.path import Path
from axabc.db import AsyncUOWFactory
from async_redis_uow.repository.common import BaseRepository
from async_redis_uow.session_maker.session import LazySession
from async_redis_uow.session_maker.session import LazySession


async def create_models(uowf: AsyncUOWFactory):
    async with uowf() as uow:
        for name in uow.repo.get_repos():
            repo = getattr(uow.repo, name)
            if not isinstance(repo, BaseRepository):
                continue

            repo_session: LazySession = repo.session

            if not isinstance(repo_session, LazySession):  
                continue

            res = await repo_session.json().get(repo.hname).execute()  # type: ignore
            if res is None or res == [None]:
                await repo_session.json().set(repo.hname, Path('$'), {}).execute()  # type: ignore

