from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class user(BaseModel):
    name:str
    age:int
    password:str

#hide password
class userResponse(BaseModel):
    name:str
    age:int

@app.get("/user", response_model=userResponse)
def get():
    return{
        "name":"Hinata",
        "age":20,
        "password":"123"
    }