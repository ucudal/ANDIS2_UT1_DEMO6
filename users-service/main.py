from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import psycopg2

app = FastAPI(title="Users Service")

POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT", 5432)
POSTGRES_NAME = os.environ.get("POSTGRES_NAME", "usersdb")
POSTGRES_USER = os.environ.get("POSTGRES_USER", "usersusr")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "Pa55w0rd")

def get_conn():
    return psycopg2.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        database=POSTGRES_NAME,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD
    )

class User(BaseModel):
    username: str
    email: str

@app.post("/users/")
def create_user(user: User):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (user.username, user.email))
    conn.commit()
    cur.close()
    conn.close()
    return {"msg": "User created"}

@app.get("/users/")
def list_users():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name, email FROM users")
    users = [{"name": row[0], "email": row[1]} for row in cur.fetchall()]
    cur.close()
    conn.close()
    return users
