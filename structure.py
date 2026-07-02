from fastapi import FastAPI

#basic structure

app = FastAPI()

#home route
@app.get("/")
def home():
    return{"hello fastAPI"}

#about route
@app.get("/about")
def about():
    return('hello about page')

#user route
@app.get("/user")
def user():
    return{
        "user": ['obito','madara','sasuke']
    }