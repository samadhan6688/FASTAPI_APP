from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    category: str
    description: str
    product_image: str
    sku: str
    unit_of_measure: str
    lead_time: int

products = []

@app.get("/product/list", response_model=List[Product])
def list_products():
    return products   

@app.get("/product/{pid}/info", response_model=Product)
def get_product(pid: int):
    for product in products:
        if product.id == pid:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/product/add", response_model=Product)
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/product/{pid}/update", response_model=Product)
def update_product(pid: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == pid:
            products[index] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")
