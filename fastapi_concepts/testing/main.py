from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def home():
    return {"message":"Welcome to API"}

@app.get('/addition')
def addition(a:int,b:int):
    return a + b
