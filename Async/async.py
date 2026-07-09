import time
import asyncio
from fastapi import FastAPI

app= FastAPI()

@app.get("/")
async def home():
    await asyncio.sleep(4)
    return{
        "message":"after 4 seceond delay "
    }