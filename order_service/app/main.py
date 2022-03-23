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


@app.put('/stores/orders', response_model=schemas.Order)
def update_order(order_update: schemas.OrderUpdate, db: Session = Depends(get_db)):
    db_order = crud.update_order_price(db, order_update=order_update)
    return db_order


@app.post('/stores/{store_id}/orders', response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    db_order = crud.create_order(db, order=order)
    return db_order


@app.get('/stores/{store_id}/orders', response_model=list[schemas.Order])
def get_orders(store_id: int, db: Session = Depends(get_db)):
    db_orders = crud.get_orders(db, store_id=store_id)
    return db_orders

