from __future__ import annotations # this is important to have at the top
from pydantic import BaseModel
from typing import List


class Country(BaseModel):
    id: int
    name: str
    coffees: List[Coffee] = []

    class Config:
        orm_mode = True


class Coffee(BaseModel):
    id: int
    name: str
    roast: str = None  # light, medium, dark
    country_id: Country

    class Config:
        orm_mode = True


from models import Coffee  # NOQA: E402
from models import Country # NOQA: E402
Country.update_forward_refs()
Coffee.update_forward_refs()
