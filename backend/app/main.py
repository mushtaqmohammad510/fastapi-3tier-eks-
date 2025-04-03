from fastapi import FastAPI
from . import models, crud, database
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware to allow frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=database.engine)

@app.get("/items/")
def read_items():
    db = database.SessionLocal()
    items = crud.get_items(db)
    db.close()
    return items

@app.post("/items/")
def create_item(name: str):
    db = database.SessionLocal()
    item = crud.create_item(db, name)
    db.close()
    return item