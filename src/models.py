from __future__ import annotations # this is important to have at the top
from pydantic import BaseModel
from typing import List

class CountryCreate(BaseModel):
    name: str

class Country(CountryCreate):
    id: int
    # Only update this through creating a Coffee.  This will be returned from the schema but is never updated through
    # Country
    # coffees: List[Coffee] = []

    class Config:
        orm_mode = True

class CoffeeCreate(BaseModel):
    name: str
    roast: str = None  # light, medium, dark
    country_id: int

class Coffee(CoffeeCreate):
    id: int

    class Config:
        orm_mode = True


from models import Coffee  # NOQA: E402
from models import Country # NOQA: E402
Country.update_forward_refs()
Coffee.update_forward_refs()
