from typing import Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    product_id: int
    order_id: int
    count: int


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    store_id: int
    total_price: Optional[int]
    status: str
    items: list[Item]


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True

