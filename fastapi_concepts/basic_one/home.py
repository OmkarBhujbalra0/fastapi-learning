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
        l.append(item)

@app.get('/items/{item_name}')
def search(item_name: str):
    for i in l:
        if item_name == i.item:
            return {"item":i.item}
    return {"message":"Not Found"}

@app.put('/items/{item_name}')
def update(item_name:str,change:items):
    for i in l:
        if item_name == i.item:
            i.item = change.item
            return {"item":item_name, "message":"Item Updated."}
    return {"message":"Item not Found"}

@app.delete('/items/{item_name}')
def deletes(item_name:str):
    for i in l:
        if item_name == i.item:
            l.remove(i)
            return {"message":"Removed this item."}
    return {'message':'Item not Found.'}