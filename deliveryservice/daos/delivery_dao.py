from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship, backref

from db import Base


class DeliveryDAO(Base):
    __tablename__ = 'delivery'
    id = Column(Integer, primary_key=True)  # Auto generated primary key
    order_id = Column(String) # Foreign Key will be added, order.id
    delivery_time = Column(DateTime)
    delivery_address = Column(String)
    status = Column(String)
    status_last_update = Column(TIMESTAMP(timezone=False))

    def __init__(self, order_id, delivery_time, delivery_address, status, status_last_update):
        self.order_id = order_id
        self.delivery_time = delivery_time
        self.status = status
        self.delivery_address = delivery_address
        self.status_last_update = status_last_update
