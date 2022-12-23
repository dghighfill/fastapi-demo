from fastapi import FastAPI, Path, HTTPException, status, Depends
import uvicorn
from typing import Optional

import schema
from schema import Coffee as CoffeeSchema
from models import Coffee as CoffeeModel
from schema import Country as CountrySchema
from models import Country as CountryModel


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

beans = {
    1: {"bean": "Columbia"},
    2: {"bean": "Sumatra"}
}
@app.get("/beans")
def get_beans(db: Session = Depends(get_db)) -> Dict:
    return db.query(CoffeeSchema).all()

# @app.get("/beans/bean")
# def get_by_name(name: Optional[str] = None, db: Session = Depends(get_db)):
#     response = None
#
#     for item_id in beans:
#         if beans[item_id]["bean"] == name:
#             response = beans[item_id]
#     if response is not None:
#         return response
#     else:
#         raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Bean ID does not exists")

# @app.get("/beans/{item_id}")
# def get_by_id(item_id: int = Path(None, description="The ID of the bean you'd like to retrieve",gt=0)) -> dict:
#     if item_id not in beans:
#         raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Bean ID does not exists")
#     else:
#         return beans[item_id]
#
@app.post("/beans")
def create_bean(coffee: CoffeeModel, db: Session = Depends(get_db)):
    db.add(coffee)
    db.commit()
    db.refresh(coffee)
    return get_beans(db)
#
# @app.put("/beans/{item_id}")
# def update_bean(item_id: int, bean: Bean):
#     if item_id not in beans:
#         raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Bean ID does not exists")
#     else:
#         beans[item_id] = bean
#     return beans[item_id]
#
# @app.delete("/beans/{item_id}")
# def delete_bean(item_id: int):
#     if item_id not in beans:
#         raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Bean ID does not exists")
#     else:
#         del beans[item_id]
#     return {}

@app.get("/countries")
def countries(db: Session = Depends(get_db)) -> Dict:
    return db.query(CountrySchema).all()

@app.get("/countries/{country_id}")
def get_country_by_id(country_id: int = Path(None, description="The ID of the Country you'd like to retrieve",gt=0)
                      , db: Session = Depends(get_db)) -> dict:
    return db.query(CountrySchema).filter(CountrySchema.id == country_id).first()

@app.post("/country")
def create_bean(country: str, db: Session = Depends(get_db)):
    db_country = schema.Country(name=country)
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return get_country_by_id(db_country.id, db=db)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", reload=True)
