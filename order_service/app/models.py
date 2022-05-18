from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .db import Base


# 2 sqlalchemy models: order and item
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    total_price = Column(Integer)
    status = Column(String(255))
    store_id = Column(Integer)
    items = relationship("Item", back_populates="order")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    stock_id = Column(Integer)
    count = Column(Integer)
    order_id = Column(Integer, ForeignKey('orders.id'))
    order = relationship("Order")
