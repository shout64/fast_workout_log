from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()
conn = sqlite3.connect("prod.db")

data = {"1": "Squat"}

@app.get("/")
def get_data():
    return data