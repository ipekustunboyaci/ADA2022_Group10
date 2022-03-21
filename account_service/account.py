from fastapi import FastAPI

from models import UserIn
import db_manager
from db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/', status_code=201)
async def add_movie(payload: UserIn):
    something = await db_manager.add_user(payload)
    response = {
        'something': something,
        **payload.dict()
    }

    return response
