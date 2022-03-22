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


@app.get("/inventory/seed", status_code=201)
def seed(db: Session = Depends(get_db)):
    db_inventory = db_seeder.create_inventory(db=db, n=500)
    return {"message": "500 items successfully inserted"}


@app.patch("/inventory/{store_id}", response_model=list[schemas.Item])
def update_inventory(products: dict[int, int], store_id: int, db: Session = Depends(get_db)):
    db_order = crud.update_inventory(db=db, store_id=store_id, products=products)
    return db_order


@app.get("/inventory/{store_id}", response_model=list[schemas.Item])
def index(store_id: int, db: Session = Depends(get_db)):
    db_inventory = crud.get_inventory(db=db, store_id=store_id)
    if db_inventory is None:
        raise HTTPException(status_code=404, detail="Store not found")
    return db_inventory


