from fastapi import FastAPI

app = FastAPI()

#optinal parameter
@app.get("/users")
def get_users(name: str=None):
    return {'Nmae':name}

#default values
@app.get("/product")
def get_product(limit: int=10):
    return {'limit':limit}

#multiple query params
@app.get("/items")
def get_items(items: str='obito', price: int=200):
    return{
        'items':items,
        'price':price

    }