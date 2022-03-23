from typing import Optional
from pydantic import BaseModel
from datetime import datetime

# Pydantic model of input and output of requests
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


class ItemChange(BaseModel):
    items: list[Item]
    total_price: int
