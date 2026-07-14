from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel
from jose import jwt 
from datetime import datetime, timedelta, timezone


app = FastAPI()

seceret_key = 'cLaude'
algo = "HS256"

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc)+timedelta(minutes=30)
    to_encode.update({
        "exp":expire
    })
    token = jwt.encode(to_encode, seceret_key,algorithm=algo)

    return token

#login api
@app.post("/login")
def login(username:str, password:str):
    if username!= "admin" or password!="123":
        raise HTTPException(
            status_code=401,
            detail="invalid username and password"
        )
    token = create_token({
        "sub":username
    })
    return{
        "success token": token
    }

#token varify
def varify_token(token: str = Header(None)):
    try:
        payload = jwt.decode(token,seceret_key, algorithms=[algo])
        return payload
    except:
        raise HTTPException(
            status_code=401,
            detail="InvLID OR EXPIRE TOKEN"
        )
    

#protectd route
@app.get("/secure")
def secure_data(user = Depends(varify_token)):
    return{
        "message":"Secure Data Access",
        "user":user
    }