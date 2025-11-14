from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import requests as r

app = FastAPI()
conn = sqlite3.connect("prod.db")

data = r.get("https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/dist/exercises.json")
response = data.json()

@app.get("/data")
def get_raw_data():
    value = []
    for exercise in response[:10]:
        value.append(exercise)
    return value

@app.get(f"/exercise/")
def get_exercise(name: str):
    for exercise in response:
        if name in exercise["name"]:
            return exercise
    return HTTPException(status_code=404, detail=f"No exercise found matching {name}")
