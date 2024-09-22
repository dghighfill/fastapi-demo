from fastapi import FastAPI, Path, HTTPException, status
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

coffees = {
    1: { "name": "Hawaii Kona Coffee" },
    2: { "name": "Jamacian Blue Mountain" },
    3: { "name": "Panama Geisha" },
    4: { "name": "Sulawesi Toraja"},
    5: { "name": "TANZANIA PEABERRY" },
    6: { "name": "MOCHA JAVA" },
    7: { "name": "ETHIOPIAN HARRAR" },
}


class Coffee(BaseModel):
    name: str
    roast: str = None  # light, medium, dark
    

@app.get("/coffees")
def get_coffees() -> dict:
    return coffees


@app.get("/coffees/{coffee_id}")
def get_by_id(coffee_id: int = Path(description="The ID of the coffee you'd like to retrieve", gt=0)):
    if coffee_id not in coffees:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Coffee ID does not exists")
    else:
        return coffees[coffee_id]


@app.post("/coffees")
def create_coffee(coffee: Coffee):
    item_id = len(coffees) + 1
    if item_id in coffees:
        raise HTTPException( status_code=status.HTTP_400_BAD_REQUEST, detail="Coffee ID already exists")
    else:
        coffees[item_id] = coffee
    return coffees[item_id]


@app.put("/coffees/{item_id}")
def update_coffee(item_id: int, coffee: Coffee):
    if item_id not in coffees:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Coffee ID does not exists")
    else:
        coffees[item_id] = coffee
    return coffees[item_id]


@app.delete("/coffees/{item_id}")
def delete_coffee(item_id: int):
    if item_id not in coffees:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Coffee ID does not exists")
    else:
        del coffees[item_id]
    return {}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", reload=True)