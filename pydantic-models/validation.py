from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class address(BaseModel):
    city:str
    pin:int

class User(BaseModel):
    name:str
    age:int
    email:str
    Address:address

@app.post("/nested_user")
def validate(user:User):
    return user