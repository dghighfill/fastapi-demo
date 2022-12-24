from fastapi import FastAPI
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

@app.get("/coffees")
def get_coffees() -> dict:
    return coffees

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", reload=True)