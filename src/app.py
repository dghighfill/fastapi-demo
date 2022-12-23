from fastapi import FastAPI, Path, HTTPException, status, Depends
import uvicorn
from typing import Optional

import schema
from schema import Coffee as CoffeeSchema
from models import Coffee as CoffeeModel
from schema import Country as CountrySchema
from models import Country as CountryModel
from models import CountryCreate as CountryCreateModel
from models import CoffeeCreate as CoffeeCreateModel


from database import engine, SessionLocal, Base
from sqlalchemy.orm import Session
from typing import Dict

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/coffees")
def get_beans(db: Session = Depends(get_db)) -> Dict:
    return db.query(CoffeeSchema).all()

@app.get("/coffees/coffee")
def get_coffee_by_name(name: Optional[str] = None, db: Session = Depends(get_db)):
    # /coffees/coffee?name=sumatra
    coffee = db.query(CoffeeSchema).filter(CoffeeSchema.name == name).first()
    if coffee is not None:
        return coffee
    else:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Coffee does not exists")

@app.get("/coffees/{item_id}")
def get_coffee_by_id(item_id: int = Path(None, description="The ID of the bean you'd like to retrieve",gt=0)
                     , db: Session = Depends(get_db)) -> dict:
    coffee = db.query(CoffeeSchema).filter(CoffeeSchema.id == item_id).first()
    if coffee is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bean ID does not exists")
    return coffee

@app.post("/coffees/coffee")
def create_coffee(coffee: CoffeeCreateModel, db: Session = Depends(get_db)):

    # Check to see if it already exists
    item = db.query(CoffeeSchema).filter(CoffeeSchema.name == coffee.name).first()

    if item is not None:
        raise HTTPException( status_code=status.HTTP_400_BAD_REQUEST, detail="Bean ID already exists")

    db_coffee = CoffeeSchema(name=coffee.name, roast=coffee.roast,
                              country_id=coffee.country_id)
    db.add(db_coffee)
    db.commit()
    db.refresh(db_coffee)
    return get_coffee_by_id(db_coffee.id, db=db)

@app.put("/coffees/coffee")
def update_coffee(coffee: CoffeeModel, db: Session = Depends(get_db)):
    db_coffee = db.query(CoffeeSchema).filter(CoffeeSchema.id == coffee.id).first()
    if db_coffee is None:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Coffee does not exists")
    else:
        db_coffee.name = coffee.name
        db_coffee.roast = coffee.roast
        db_coffee.country_id = coffee.country_id

    db.commit()
    return get_coffee_by_id(db_coffee.id, db=db)

@app.delete("/coffees/{item_id}")
def delete_coffee(item_id: int, db: Session = Depends(get_db)):
    coffee = db.query(CoffeeSchema).filter(CoffeeSchema.id == item_id).first()
    if coffee is not None:
        db.delete(coffee)
        db.commit()
    else:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Coffee does not exists")
    return {}

@app.get("/countries")
def get_countries(db: Session = Depends(get_db)) -> Dict:
    return db.query(CountrySchema).all()

@app.get("/countries/{country_id}/beans")
def get_beans_for_country(country_id: int, db: Session = Depends(get_db)) -> Dict:
    country = db.query(CountrySchema).filter(CountrySchema.id == country_id).first()
    return country.coffees

@app.get("/countries/{country_id}")
def get_country_by_id(country_id: int = Path(None, description="The ID of the Country you'd like to retrieve", gt=0)
                      , db: Session = Depends(get_db)) -> dict:

    country = db.query(CountrySchema).filter(CountrySchema.id == country_id).first()
    if country is None:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Country does not exists")
    return country

@app.post("/countries/country")
def create_country(country: CountryCreateModel, db: Session = Depends(get_db)):
    db_country = schema.Country(name=country.name)
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return get_country_by_id(db_country.id, db=db)

@app.put("/countries/country")
def update_country(country: CountryModel, db: Session = Depends(get_db)):
    db_country = db.query(CountrySchema).filter(CountrySchema.id == country.id).first()
    db_country.name = country.name
    db.commit()
    return get_country_by_id(db_country.id, db=db)
@app.delete("/countries/{country_id}")
def delete_country(country_id: int = Path(None, description="The ID of the Country you'd like to delete", gt=0)
                   , db: Session = Depends(get_db)) -> dict:
    country = db.query(CountrySchema).filter(CountrySchema.id == country_id).first()
    if country is not None:
        db.delete(country)
        db.commit()
    else:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Country does not exists")
    return {}

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", reload=True)
