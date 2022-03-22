#Ref -Bas
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from db import Base


class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    inventory = relationship("Item", back_populates="store")

class Item(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    store_id = Column(Integer, ForeignKey('stores.id'))
    reservation = Column(DateTime)
    store = relationship("Store", back_populates="inventory")