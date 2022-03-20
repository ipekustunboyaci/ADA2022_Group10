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


@app.get('/stores/seed', response_model=list[schemas.Store])
def seed(db: Session = Depends(get_db)):
    stores = [db_seeder.create_store(db) for x in range (20)]
    return stores


@app.post("/stores/", response_model=schemas.Store)
def create(store: schemas.StoreCreate, db: Session = Depends(get_db)):
    return crud.create_store(db=db, store=store)


@app.get("/search", response_model=schemas.Store)
def search(skip: int = 0, limit: int = 100, lat: float = 50.000000, lon: float = 5.000000, db: Session = Depends(get_db)):
    stores = crud.get_stores(db, skip=skip, limit=limit, latitude=lat, longitude=lon)
    if stores is None:
        raise HTTPException(status_code=404, detail="No stores found")

    closest_store = None
    closest_euclidian = 5000.00
    for store in stores:
        if (store.latitude - lat)**2 + (store.longitude -lon)**2 < closest_euclidian:
            closest_store = store
            closest_euclidian = (closest_store.latitude - lat)**2 + (closest_store.longitude - lon)**2

    if closest_store is None:
        raise HTTPException(status_code=404, detail="No nearby store found")
    else:
        return closest_store
