import sqlite3
from fastapi import FastAPI

app = FastAPI()

conn = sqlite3.connect("test.db",check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
            create table if not exists todo(
               id integer primary key,
               title TEXT,
               completed text)
""")

conn.commit()

@app.get("/")
def home():
    return{
        "message": "DB connected"
    }