from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

upload_dir = "uploads"
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

#static file setup
app.mount("/uploads", StaticFiles(directory=upload_dir), name="uploads")

@app.post("/uploadfile")
def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    filepath = os.path.join(upload_dir, filename)

    if not filename:
        raise HTTPException(status_code=400, detail="file not selected")
    
    with open(filepath,"wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

        return{
            "message":"file uploaded successfully",
            "fileName":"filename",
            "file_url":f"http://127.0.0.1:8000/files/{filename}"
        }

#get file url api
@app.get("/files/{filename}")
def get_file(filename:str):
    filepath=os.path.join(upload_dir, filename)

    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="file not found")
    
    return{
        "file_url":f"http://127.0.0.1:8000/files/{filename}"
    }

@app.get("/")
def home():
    return{
        "message":"file uploaded running api"
    }