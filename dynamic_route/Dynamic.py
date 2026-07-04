from fastapi import FastAPI

app = FastAPI()

@app.get("/user/{user_id}")
def get_user(user_id):
    return {"user_id": user_id}

#data type
@app.get('/admin/{id}')
def ge_admin(id:int):    #str
    return {"id":id}
