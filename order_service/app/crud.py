from sqlalchemy.orm import Session

from . import models, schemas


def create_order(db: Session, order: schemas.OrderCreate):
    db_items = [models.Item(count=item.count, product_id=item.product_id) for item in order.items]
    db_order = models.Order(store_id=order.store_id, items=db_items, status=order.status)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
