from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel
import jwt
from datetime import datetime, timedelta,timezone
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials

app = FastAPI()
security = HTTPBearer()

SECRET_KEY = 'hide the secret key before using it in projects.'

ALGORITHM = "HS256"

class Credentials(BaseModel):
    username: str
    password: str

@app.get('/')
def home():
    return {"message":"Fastapi for authentication."}

@app.post('/login')
def login(data:Credentials):
    payload = {
        "sub": data.username,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=15)
    }

    if data.username!="studentname" or data.password!="12345":
        raise HTTPException(status_code=401,detail="Invalid Credentials.")

    token = jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
    return {"Access Token": token, "Token Type": "Bearer"}

def verify_token(credentials:HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return payload["sub"]

@app.get('/me')
def logged_page(user = Depends(verify_token)):
    return {"message":f"Welcome,{user}"}