from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#simple formate
@app.post('/create_user')
def create_user(name:str, age:int):
    return{
        "name":name,
        "age":age
    }
#validation using pydantic
class User(BaseModel):
    name:str
    age:int
#json formate
@app.post("/create-user")
def create(user:User):
    return{
        "message":"new user created",
        "data":user
    }