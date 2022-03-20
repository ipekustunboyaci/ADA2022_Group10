from sqlalchemy.orm import Session

from . import models, schemas


def get_store(db: Session, store_id: int):
    return db.query(models.Store).filter(models.Store.id == store_id).first()


def get_stores(db: Session, skip: int = 0, limit: int = 100, latitude: float = 5.000000, longitude: float = 50.000000):
    lat = [latitude - 0.01, latitude + 0.01]
    lon = [longitude - 0.02, longitude + 0.02]
    return db.query(models.Store)\
        .where(lat[0] <= models.Store.latitude <= lat[1])\
        .where(lon[0] <= models.Store.longitude <= lon[1])\
        .offset(skip)\
        .limit(limit)\
        .all()


def create_store(db: Session, store: schemas.StoreCreate):
    db_store = models.Store(name=store.name)
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store
