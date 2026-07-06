from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    email:str

@app.post('/create_user')
def schemas(user:User):
    return{
        "message":"user created",
        "data":user
    }