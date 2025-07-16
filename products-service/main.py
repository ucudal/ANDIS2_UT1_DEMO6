from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId


app = FastAPI(title="Products Service")

# MONGO_URL="mongodb://productsusr:Pa55w0rd@localhost:27017/productsdb"
# client = MongoClient(MONGO_URL)

MONGO_HOST = os.environ.get("MONGO_HOST", "localhost")
MONGO_PORT = int(os.environ.get("MONGO_PORT", 27017));
MONGO_DB = os.environ.get("MONGO_DB", "productsdb");
MONGO_USER = os.environ.get("MONGO_USER", "productsusr")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD", "Pa55w0rd")
client = MongoClient(
    host=MONGO_HOST,
    port=MONGO_PORT,
    username=MONGO_USER,
    password=MONGO_PASSWORD,
    authSource=MONGO_DB
)

db = client["productsdb"]
products_collection = db["products"]


class Product(BaseModel):
    name: str
    price: float


@app.post("/products/")
def create_product(product: Product):
    result = products_collection.insert_one(product.dict())
    return {"id": str(result.inserted_id), "msg": "Product created"}


@app.get("/products/")
def list_products():
    products = []
    for prod in products_collection.find():
        prod["_id"] = str(prod["_id"])
        products.append(prod)
    return products


@app.get("/products/{product_id}")
def get_product(product_id: str):
    try:
        obj_id = ObjectId(product_id)
    except InvalidId as e:
        raise HTTPException(status_code=400, detail="Invalid product id format")
    prod = products_collection.find_one({"_id": obj_id})
    if not prod:
        raise HTTPException(status_code=404, detail="Product not found")
    prod["_id"] = str(prod["_id"])
    return prod

