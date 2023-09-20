from redis.commands.json.path import Path
from axabc.db import AsyncUOWFactory
from async_redis_uow.session_maker.session import LazySession


async def create_models(uowf: AsyncUOWFactory):
    async with uowf() as uow:
        for name in uow.repo.get_repos():
            repo = getattr(uow.repo, name)
            repo_session = repo.session
            if isinstance(repo_session, LazySession):  
                res = await repo_session.json().get(repo.hname).execute()  # type: ignore
                if res is None or res == [None]:
                    await repo_session.json().set(repo.hname, Path('$'), {}).execute()  # type: ignore

