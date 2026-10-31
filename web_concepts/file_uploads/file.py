from fastapi import FastAPI,File,UploadFile,HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

app.mount("/files",StaticFiles(directory=UPLOAD_DIR),name="files")

@app.post('/upload')
def uploads(file: UploadFile = File(...)):
    filename = file.filename
    file_path = os.path.join(UPLOAD_DIR,filename)

    if not filename:
        raise HTTPException(status_code=400,detail="File not uploaded.")

    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

        return {
            "message":"File uploaded Successfully.",
            "filename":filename,
            "file_url": f"http://127.0.0.1:8000/files/{filename}"
        }

@app.get("/files/{file_name}")
def display(file_name:str):
    file_path = os.path.join(UPLOAD_DIR,file_name)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404,detail="File not Found.")

    return {
        "file_url":f"http://127.0.0.1:8000/files/{file_name}"
    }