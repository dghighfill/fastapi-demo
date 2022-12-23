from fastapi import FastAPI, Path, HTTPException, status
from typing import Optional
from pydantic import BaseModel



app = FastAPI()

class Bean(BaseModel):
    # bean_id: int
    name: str
    roast: str = None  # light, medium, dark

beans = {
    1: {"bean": "Columbia"},
    2: {"bean": "Sumatra"}
}
@app.get("/beans")
def get_beans() -> dict:
    return beans

@app.get("/beans/bean")
def get_by_name(name: Optional[str] = None):
    response = None

    for item_id in beans:
        if beans[item_id]["bean"] == name:
            response = beans[item_id]
    if response is not None:
        return response
    else:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Bean ID does not exists")

@app.get("/beans/{item_id}")
def get_by_id(item_id: int = Path(None, description="The ID of the bean you'd like to retrieve",gt=0)) -> dict:
    if item_id not in beans:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Bean ID does not exists")
    else:
        return beans[item_id]

@app.post("/beans")
def create_bean(bean: Bean):
    item_id = len(beans) + 1
    if item_id in beans:
        raise HTTPException( status_code=status.HTTP_400_BAD_REQUEST, detail="Bean ID already exists")
    else:
        beans[item_id] = bean
    return beans[item_id]

@app.put("/beans/{item_id}")
def update_bean(item_id: int, bean: Bean):
    if item_id not in beans:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Bean ID does not exists")
    else:
        beans[item_id] = bean
    return beans[item_id]

@app.delete("/beans/{item_id}")
def delete_bean(item_id: int):
    if item_id not in beans:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Bean ID does not exists")
    else:
        del beans[item_id]
    return {}
