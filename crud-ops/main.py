from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todo_list = []

class Todo(BaseModel):
    id:int
    title:str
    completed:bool

@app.post("/todo")
def create_todo(todo:Todo):
    todo_list.append(todo)
    return {
        "message":"tODO ADDED",
        "data":todo
    }

@app.get("/todo")
def get_data():
    return todo_list

#get one data
@app.get("/todo/{todo_id}")
def get_id(todo_id:int):
    for todo in todo_list:
        if todo.id==todo_id:
            return todo
    return {"error":"not found"}

@app.put("/todo/{todo_id}")
def update(todo_id:int, updated:Todo):
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list[index] = updated