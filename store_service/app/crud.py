from sqlalchemy.orm import Session

from . import models, schemas


def get_stores(db: Session, skip: int = 0, limit: int = 100, longitude: float = 5.000000, latitude: float = 50.000000, search: bool = False):
    if search:
        lat = [latitude - 0.01, latitude + 0.01]
        lon = [longitude - 0.02, longitude + 0.02]
        return db.query(models.Store)\
            .where(lat[0] <= models.Store.latitude) \
            .where(lat[1] >= models.Store.latitude) \
            .where(lon[0] <= models.Store.longitude) \
            .where(lon[1] >= models.Store.longitude) \
            .offset(skip)\
            .limit(limit)\
            .all()
    else:
        return db.query(models.Store).offset(skip).limit(limit).all()


def create_store(db: Session, store: schemas.StoreCreate):
    db_store = models.Store(name=store.name)
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store
