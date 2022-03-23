from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from .db import Base

# SQLalchemy model of item
class Item(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(255))
    store_id = Column(Integer)
    count = Column(Integer)
    price = Column(Integer)
