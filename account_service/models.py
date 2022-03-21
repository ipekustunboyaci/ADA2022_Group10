from pydantic import BaseModel
from typing import List, Optional

class UserIn(BaseModel):
    full_name: str
    email: str
    street_name: str
    street_number: int
    city_name: str
    country_name: str

