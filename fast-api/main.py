from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from bson.errors import InvalidId

app = FastAPI()

# Connect to MongoDB
client = MongoClient('mongodb://mongodb:27017')
db = client.mydatabase

class Item(BaseModel):
    name: str
    description: str

class ItemResponse(BaseModel):
    id: str
    name: str
    description: str

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/status")
def read_status():
    return {"status": "ok"}

@app.get("/items", response_model=list[ItemResponse])
def read_items():
    items = db.items.find()
    return [{"id": str(item["_id"]), "name": item["name"], "description": item["description"]} for item in items]

@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: str):
    try:
        item = db.items.find_one({"_id": ObjectId(item_id)})
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid item ID format")
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": str(item["_id"]), "name": item["name"], "description": item["description"]}

@app.post("/items")
def create_item(item: Item):
    result = db.items.insert_one(item.dict())
    if result.acknowledged:
        return {"id": str(result.inserted_id)}
    else:
        raise HTTPException(status_code=500, detail="Item could not be added")
