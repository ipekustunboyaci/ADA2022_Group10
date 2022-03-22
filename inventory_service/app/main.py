from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas, db_seeder
from .db import SessionLocal, engine

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/inventory/seed", response_model=list[schemas.Item])
def seed(db: Session = Depends(get_db)):
    db_inventory = db_seeder.create_inventory(db, 500)
    return db_inventory


@app.get("/inventory/{store_id}", response_model=list[schemas.Item])
def index(store_id: int, db: Session = Depends(get_db)):
    db_inventory = crud.get_inventory(db, store_id=store_id)
    if db_inventory is None:
        raise HTTPException(status_code=404, detail="Store not found")
    return db_inventory
