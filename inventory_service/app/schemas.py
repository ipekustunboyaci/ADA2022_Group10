from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class ItemBase(BaseModel):
    count: int
    product_name: str
    store_id: int
    price: int


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True


#class StoreBase(BaseModel):
    #name: str
    #description: Optional[str] = None
    #latitude: float
    #longitude: float
    #inventory: list[Item] = []


#class StoreCreate(StoreBase):
   # pass


#class Store(StoreBase):
    #id: int

    #class Config:
        #orm_mode = True