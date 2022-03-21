from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from db import Base
from daos.store_dao import Store

class CourierDAO(Base):
    __tablename__ = 'courier'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    store_id = Column(String)
    # ForeignKey('stores.id'))
    status = Column(String)
    #status = relationship(Store.__name__, backref=backref("courier", uselist=False))

    def __init__(self, name, store_id, status):
        self.name = name
        self.store_id = store_id
        self.status = status
