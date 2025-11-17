from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import requests as r

app    = FastAPI()
def get_db_connection():
    conn   = sqlite3.connect("./prod.db")
    return conn

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
        if name.lower() in (exercise["name"]).lower():
            return exercise
    return HTTPException(status_code=404, detail=f"No exercise found matching {name}")

@app.get("/routines")
def get_routines():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        try:
            results = cursor.execute("SELECT * FROM ROUTINES")
            for row in results:
                print(row)
            return {"result": "Good job learning!"}
        except Exception as e:
            return f"Error: {e}"