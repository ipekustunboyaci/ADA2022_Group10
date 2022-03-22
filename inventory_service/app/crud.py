from sqlalchemy.orm import Session
from fastapi import HTTPException

from . import models, schemas


def get_inventory(db: Session, store_id: int):
    return db.query(models.Item).filter(models.Item.store_id == store_id).all()


def update_inventory(db:Session, store_id: int, products: dict[int, int]):
    db_order = db.query(models.Item).filter(models.Item.id.in_(products)).all()
    for item in db_order:
        item.count = item.count + products[item.id]
        if(item.count < 0):
            raise HTTPException(status_code=400, detail="Product(s) are not available anymore")
    db.flush()
    db.commit()
    return db_order

