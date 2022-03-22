from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship, backref

from db import Base


class DeliveryDAO(Base):
    __tablename__ = 'delivery'
    id = Column(Integer, primary_key=True, index=True)  # Auto generated primary key
    order_id = Column(Integer)  # Foreign Key will be added, order.id
    delivery_time = Column(DateTime)
    delivery_address = Column(String(255))
    status = Column(String(255))
    status_last_update = Column(TIMESTAMP(timezone=False))
    courier_id = Column(Integer)

    def __init__(self, order_id, delivery_time, delivery_address, status, status_last_update, courier_id):
        self.order_id = order_id
        self.delivery_time = delivery_time
        self.status = status
        self.delivery_address = delivery_address
        self.status_last_update = status_last_update
        self.courier_id = courier_id
