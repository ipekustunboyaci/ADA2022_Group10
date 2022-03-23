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

class UserOut(BaseModel):
    id: str
    full_name: str
    email: str
    street_name: str
    street_number: int
    city_name: str
    country_name: str

class Coordinates(BaseModel):
    lat: str
    long: str

class AddressIn(BaseModel):
    user_id: int
    street_name: str
    street_number: int
    city_name: str
    country_name: str
