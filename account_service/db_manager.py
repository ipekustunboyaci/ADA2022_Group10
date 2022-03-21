from db import users, database
from models import UserIn


async def add_user(payload: UserIn):
    query = users.insert().values(**payload.dict())

    return await database.execute(query=query)