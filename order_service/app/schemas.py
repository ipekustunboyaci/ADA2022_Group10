from typing import Optional
from pydantic import BaseModel


# A number of pydantic models to handle incoming and outcoming service data
class ItemBase(BaseModel):
    product_id: int
    count: int


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    order_id: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    store_id: int
    status: Optional[str]


class OrderUpdate(BaseModel):
    id: int
    total_price: int


class OrderCreate(OrderBase):
    items: list[ItemCreate]
    total_price: int


class Order(OrderBase):
    id: int
    items: list[Item]

    class Config:
        orm_mode = True

