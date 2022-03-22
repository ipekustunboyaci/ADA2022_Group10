from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .db import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    items = relationship("Item", back_populates="order")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    count = Column(Integer)
    order_id = Column(Integer, ForeignKey('orders.id'))
    order = relationship("Order")
