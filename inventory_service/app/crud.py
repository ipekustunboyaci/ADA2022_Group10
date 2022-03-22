from sqlalchemy.orm import Session

from . import models, schemas


def get_inventory(db: Session, store_id: int):
    return db.query(models.Item).filter(models.Item.store_id == store_id).first()


def reserve_store(db:Session, store_id: int, products: list[int]):
    db_store = db.query(models.Store).filter(models.Store.id == store_id).first()

