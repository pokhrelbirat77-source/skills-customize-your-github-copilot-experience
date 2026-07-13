from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ItemIn(BaseModel):
    name: str
    description: str
    price: float

class ItemOut(ItemIn):
    id: int

items = {}
next_item_id = 1

@app.get("/items", response_model=list[ItemOut])
def list_items():
    return list(items.values())

@app.get("/items/{item_id}", response_model=ItemOut)
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.post("/items", response_model=ItemOut)
def create_item(item: ItemIn):
    global next_item_id
    item_data = item.dict()
    item_data["id"] = next_item_id
    items[next_item_id] = item_data
    next_item_id += 1
    return item_data
