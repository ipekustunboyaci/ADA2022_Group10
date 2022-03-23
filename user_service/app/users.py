from fastapi import FastAPI, HTTPException

from .models import UserIn, UserOut, AddressIn
from . import db_manager
from .db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI()


# Connect to DB
@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# Testing  endpoint
@app.get("/")
async def root():
    return {"message": "Hello World"}


# Create endpoint
@app.post('/create_user', status_code=201)
async def add_user(payload: UserIn):
    something = await db_manager.add_user(payload)
    response = {
        'something': something,
        **payload.dict()
    }

    return response


# Read endpoint
@app.get('/get_user')
async def get_user(user_id: int, response_model=UserOut):
    user_data = await db_manager.get_user(user_id)
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    return user_data


# Update endpoint
@app.post('/change_address')
async def change_address(payload: AddressIn):
    something = await db_manager.change_address(payload)
    response = {
        'something': something,
        **payload.dict()
    }

    return response