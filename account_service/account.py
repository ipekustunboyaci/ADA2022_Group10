from fastapi import FastAPI, HTTPException

from models import UserIn, UserOut
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

@app.post('/create_user', status_code=201)
async def add_movie(payload: UserIn):
    something = await db_manager.add_user(payload)
    response = {
        'something': something,
        **payload.dict()
    }

    return response

@app.get('/get_user')
async def add_movie(user_id: int, response_model=UserOut):
    user_data = await db_manager.get_user(user_id)
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    return user_data