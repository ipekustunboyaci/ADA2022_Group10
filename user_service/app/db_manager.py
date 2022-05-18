from types import CoroutineType
from .db import users, database
from .models import UserIn, AddressIn


# Crud DB actions of user
# Create
async def add_user(payload: UserIn):
    query = users.insert().values(**payload.dict())

    return await database.execute(query=query)


# Read
async def get_user(user_id):
    query = users.select(users.c.id==user_id)
    return await database.fetch_one(query=query)



# Update
async def change_address(payload: AddressIn):
    query=users.update().\
       values(street_name=payload.street_name, street_number=payload.street_number, city_name=payload.city_name, country_name=payload.country_name, lat=payload.lat, lon=payload.lon).\
       where(users.c.id == payload.user_id)
    return await database.execute(query=query)

