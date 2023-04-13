from typing import Union
from fastapi import FastAPI
from scraper import google_shop,get_by_item

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/data/{Product Name}")
async def product_data(product_name: str):
    return google_shop(product_name)


@app.get("/data/{Product Name}/{id}")
async def product_data(product_name: str,id: int):
    return get_by_item(product_name,id)
