from typing import Optional
from pydantic import BaseModel


class StoreBase(BaseModel):
    name: str
    description: Optional[str] = None
    latitude: float
    longitude: float


class StoreCreate(StoreBase):
    pass


class Store(StoreBase):
    id: int

    class Config:
        orm_mode = True