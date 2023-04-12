from typing import Union
from fastapi import FastAPI
from scraper import google_shop

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/data/{product_name}")
async def product_data(product_name: str):
    return google_shop(product_name)
