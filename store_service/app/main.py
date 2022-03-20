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


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/stores/seed', response_model=list[schemas.Store])
def seed(db: Session = Depends(get_db)):
    stores = [db_seeder.create_store(db) for x in range (20)]
    return stores


@app.get("/stores/{store_id}", response_model=schemas.Store)
def view(store_id: int, db: Session = Depends(get_db)):
    db_store = crud.get_store(db, store_id=store_id)
    if db_store is None:
        raise HTTPException(status_code=404, detail="Store not found")
    return db_store


@app.post("/stores/", response_model=schemas.Store)
def create(store: schemas.StoreCreate, db: Session = Depends(get_db)):
    return crud.create_store(db=db, store=store)


@app.get("/stores/", response_model=list[schemas.Store])
def index(skip: int = 0, limit: int = 100, lat: float = 50.000000, lon: float = 5.000000, search: bool = False, db: Session = Depends(get_db)):
    stores = crud.get_stores(db, skip=skip, limit=limit, latitude=lat, longitude=lon, search=search)
    if stores is None:
        raise HTTPException(status_code=404, detail="No stores found")
    return stores
