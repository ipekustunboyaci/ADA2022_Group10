from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from db import Base
# Courier data access object
class CourierDAO(Base):
    __tablename__ = 'couriers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    store_id = Column(Integer)
    status = Column(String(255))


    def __init__(self, name, store_id, status):
        self.name = name
        self.store_id = store_id
        self.status = status
