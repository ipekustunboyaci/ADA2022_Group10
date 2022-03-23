from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas, db_seeder
from .db import SessionLocal, engine, Base

Base.metadata.create_all(engine)
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/order/{store_id}', response_model=schemas.Order)
def create_order(store_id: int, items: list[schemas.ItemCreate], db: Session = Depends(get_db)):
    order = schemas.OrderCreate(items=items, store_id=store_id, status="pending")
    db_order = crud.create_order(db, order=order)
    return db_order
