from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

#depends
# def logic():
#     return{
#         "message":"common logic execute"
#     }

# @app.get("/home")
# def home(data = Depends(logic)):
#     return data

#reusable code
def current_user():
    return{
        "user":"abhishek"
    }

@app.get("/profile")
def profile(user=Depends(current_user)):
    return user

@app.get("/dashboard")
def dashboard(user = Depends(current_user)):
    return user

#token
def varify_token(token: str = Header(None)):
    if token != "secrettoken":
        raise HTTPException(
            status_code=401,
            detail="unauthorized"
        )
    return{
        "user":"Authorized user"
    }

@app.get("/secureData")
def secure(user = Depends(varify_token)):
    return{
        "message":"secure data access",
        "data": user
    }