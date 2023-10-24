from fastapi import FastAPI,Response
from pydantic import BaseModel

app = FastAPI()


products = [
    {"id": 1, "name": "iPad", "price": 599},
    {"id": 2, "name": "iPhone", "price": 999},
    {"id": 3, "name": "iWatch", "price": 699},
]

class Product(BaseModel):
    name: str
    price: float

@app.get("/products")
def index():
    return products

@app.get("/products/search")
def index(name, response: Response):
    founded_products = [product for product in products if name.lower() in product["name"].lower()]

    if not founded_products: 
        response.status_code = 404
        return "No Products Found"

    return founded_products if len(founded_products) > 1 else founded_products[0]

@app.get("/products/{id}")
def index(id:int,response:Response):
    for product in products:
        if(product["id"]==id):
            return product
    response.status_code = 404
    return "Not found"

@app.post("/product")
def create_product(product: Product, response:Response):
    product = product.dict()
    product["id"] = len(products)+1
    products.append(product)
    response.status_code = 201
    return product

@app.put("/product")
def edit_product(id: int, edited_product : Product, response: Response):
    for product in products:
        if (product["id"] == id):
            product["name"] = edited_product.name
            product["price"] = edited_product.price
            response.status_code = 200
            return product
        response.status_code = 404
        return "Product not found"