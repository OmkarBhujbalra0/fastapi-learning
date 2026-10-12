from fastapi import FastAPI
from pydantic import BaseModel

class items(BaseModel):
    item: str

app = FastAPI()

l = []

@app.get('/')
def home():
    return {"message":"Hello World"}

@app.get('/items')
def display():
    return l

@app.post('/items')
def inputs(item: items):
    if item:
        l.append(item)

@app.get('/items/{item_name}')
def search(item_name: str):
    for i in l:
        if item_name == i.item:
            return {"item":i.item}
    return {"message":"Not Found"}