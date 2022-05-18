from pydantic import BaseModel
from typing import List, Optional


# Pydantic definitions of incoming and outgoing data
class UserIn(BaseModel):
    full_name: str
    email: str
    street_name: str
    street_number: int
    city_name: str
    country_name: str
    lat: float
    lon: float

class UserOut(BaseModel):
    id: str
    full_name: str
    email: str
    street_name: str
    street_number: int
    city_name: str
    country_name: str
    lat: float
    lon: float


class AddressIn(BaseModel):
    user_id: int
    street_name: str
    street_number: int
    city_name: str
    country_name: str
    lat: float
    lon: float
