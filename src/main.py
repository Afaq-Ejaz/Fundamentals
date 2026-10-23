from fastapi import FastAPI , HTTPException
from pydantic import BaseModel


class Item(BaseModel):
    text:str = "None"
    is_done :bool = False

app = FastAPI()

items = []

@app.get("/")
def root():
    return "Hola"


@app.post("/items")
def create_item(item:Item):
    items.append(item)
    return items

@app.get("/items/{item_id}")
def item_get(item_id:int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item doesnt exist")

