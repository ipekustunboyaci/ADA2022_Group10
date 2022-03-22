from pydantic import BaseModel
from typing import List, Optional

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

class Address(BaseModel):
    street_name: str
    street_number: int
    city_name: str
    country_name: str
