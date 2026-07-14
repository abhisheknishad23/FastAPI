#Oauth2 + JWT
#adavnce

from fastapi import FastAPI, HTTPException, Depends, Header
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

app =FastAPI()

#jwt configuration
SECRET_KEY = "mysecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

#password hasing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#OauthSetup
oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

#user DB
user_db = {
   "admin":{
        "username":"admin",
        "hashed_password":pwd_context.hash("123")
   }
}

#hash password
def hash_password(password:str):
    return pwd_context.hash(password)

#verify password
def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

#create token
def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc)+timedelta(minutes=30)
    to_encode.update({
        "exp":expire
    })
    token = jwt.encode(to_encode, SECRET_KEY,algorithm=ALGORITHM)

    return token
#login api(OAUTH2)
@app.post("/login")
def login(form: OAuth2PasswordRequestForm=Depends()):
    user = user_db.get(form.username)
    if not user or not verify_password(form.password,user["hashed_password"]):
        raise HTTPException(
            status_code=400,
            detail="invalid username and password"
        )
    access_token = create_token({"sub":form.username})

    return{
        "access_token":access_token,
        "token_type":"bearer"
    }

#token verify
def verify_token(token:str=Depends(oauth2_schema)):
    try:
        payload = jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=401,
                detail="invalid token"
            )
        return username
    except jwt.JWTError:
        raise HTTPException(
            status_code=401,
            detail="invalid token"
        )
    

#protectd route
@app.get("/protectd")
def protectd_data(username: str = Depends(verify_token)):
    return{
        "message":f"hello {username} Data Access",
        "user":username
    }
    