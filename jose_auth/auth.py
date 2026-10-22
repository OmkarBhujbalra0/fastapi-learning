from fastapi import FastAPI,Depends,HTTPException,Header
from jose import jwt
from pydantic import BaseModel
from datetime import datetime,timedelta,timezone

app =FastAPI()

class Credentials(BaseModel):
    username: str
    password: str

SECRET_KEY = 'this secret key should not be included in the file.'

ALGORITHM = "HS256"

def create_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.now(timezone.utc) + timedelta(minutes=15)})

    token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    
    return token

@app.post('/login')
def auth(data:Credentials):
    if data.username!="fastapiuser" or data.password!="12345":
        raise HTTPException(status_code=401,detail="Invalid username or password.")

    token = create_token({
        "sub":data.username
    })

    return {"Access Token": token}

def verify_token(token:str = Header(None)):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401,detail="Invalid or Expired Token.")

@app.get("/homepage")
def homepage(user = Depends(verify_token)):
    return {"message":"Secured Data Accessed.","user":user}
