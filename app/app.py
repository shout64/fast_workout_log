from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import requests as r

app = FastAPI()
conn = sqlite3.connect("prod.db")

data = r.get("https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/dist/exercises.json")

response = data.json()
print(type(response))

@app.get("/")
def get_data():
    value = []
    for exercise in response[:10]:
        value.append(exercise)
    return value