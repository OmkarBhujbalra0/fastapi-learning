from fastapi import FastAPI,Depends,HTTPException,Header
from pydantic import BaseModel

app = FastAPI()

class input_data(BaseModel):
    a: int
    b: int

@app.get('/')
def home():
    return "This API deals with using Depends function."

def subtraction(input_data:input_data):
    res = input_data.a - input_data.b
    return res

@app.post('/subs')
def subt(data:int = Depends(subtraction)):
    return data

def verification(token:str = Header()):
    if token == '12345':
        return {"message":"Access Granted"}
    raise HTTPException(
        status_code=401,detail="Wrong Credentials! Access Denied."
    )

@app.post('/verify')
def verification(data=Depends(verification)):
    return data