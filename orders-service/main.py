# orders-service/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import pymysql


app = FastAPI(title="Orders Service")


MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))

def get_conn():
    import logging
    logging.basicConfig(level=logging.INFO, force=True)
    logging.info(f"Connecting to database at {MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE} as {MYSQL_USER}")
    return pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
        port=int(MYSQL_PORT),
        cursorclass=pymysql.cursors.DictCursor
    )


class Order(BaseModel):
    user_id: int
    product_id: str
    quantity: int

@app.post("/orders/")
def create_order(order: Order):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO orders (user_id, product_id, quantity) VALUES (%s, %s, %s)",
        (order.user_id, order.product_id, order.quantity)
    )
    conn.commit()
    order_id = cur.lastrowid
    cur.close()
    conn.close()
    return {"id": order_id, "msg": "Order created"}

@app.get("/orders/")
def list_orders():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, user_id, product_id, quantity FROM orders")
    orders = cur.fetchall()
    cur.close()
    conn.close()
    return orders
