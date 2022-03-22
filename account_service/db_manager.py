from db import users, database
from models import UserIn


async def add_user(payload: UserIn):
    query = users.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_user(user_id):
    query = users.select(users.c.id==user_id)
    return await database.fetch_one(query=query)
