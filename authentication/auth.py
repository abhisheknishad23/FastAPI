from fastapi import FastAPI, HTTPException, Depends, Header
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