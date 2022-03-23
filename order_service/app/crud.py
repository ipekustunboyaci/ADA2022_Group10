from sqlalchemy.orm import Session

from . import models, schemas


def create_order(db: Session, order: schemas.OrderCreate):
    db_items = [models.Item(count=item.count, product_id=item.product_id) for item in order.items]
    db_order = models.Order(store_id=order.store_id, items=db_items, status="pending")
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def get_orders(db: Session, store_id: int):
    db_orders = db.query(models.Order).where(models.Order.store_id == store_id).all()
    return db_orders


def update_order_price(db: Session, order_update: schemas.OrderUpdate):
    db_order = db.query(models.Order).where(models.Order.id == order_update.id).first()
    db_order.total_price = order_update.total_price
    db_order.status = "accepted"
    db.flush()
    db.commit()
    db.refresh(db_order)
    return db_order
