from fastapi import FastAPI, status, HTTPException

app = FastAPI()

@app.post("/create_user", status_code= status.HTTP_201_CREATED)
def create():
    return{
        "message":"user created"
    }

#manually status message
@app.get("/user")
def get_user():
    return{
        "status":"Success",
        "message":"user fetch data",
        "data":{
            "name":"obito",
            "relation":"Rin",
            "age":34
        }
    }

#error handling
@app.get("/user/{user_id}")
def get_user(user_id:int):
    if user_id !=1:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
    return{
        "id":1,
        "name":"sakura"
    }

#exception handling