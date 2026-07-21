from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#frontend url
origins =[
    "http://localhost:5000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"], #CRUD
    allow_headers=["*"]
)

@app.get("/")
def home():
    return{
        "message":"CORS enable api"
    }