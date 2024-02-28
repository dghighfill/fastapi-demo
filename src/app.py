from fastapi import FastAPI
import uvicorn
from coffee_router import router

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", reload=True)