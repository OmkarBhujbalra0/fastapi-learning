from fastapi import FastAPI,Depends,Header,HTTPException
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from jose import jwt,JWTError
from pydantic import BaseModel
from datetime import datetime, timezone,timedelta
from passlib.context import CryptContext


app = FastAPI()

SECRET_KEY = "secret"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=['bcrypt'],deprecated="auto")

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

fake_user_db = {
    "admin": {
        "username":"admin",
        "password":pwd_context.hash("12345")
    }
}

def hash_pwd(password:str):
    return pwd_context.hash(password)

def verify_pwd(plain_pwd, hashed_pwd):
    return pwd_context.verify(plain_pwd,hashed_pwd)



def create_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.now(timezone.utc) + timedelta(minutes=15)})

    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

@app.post('/login')
def auth(formdata:OAuth2PasswordRequestForm = Depends()):
    user = fake_user_db.get(formdata.username)
    if not user or not verify_pwd(formdata.password,user['password']):
        raise HTTPException(status_code=401,detail="invalid username or password.")
    token = create_token({"sub":formdata.username})
    return {"access_token":token,"token_type":"Bearer"}


def verify_token(token:str = Depends(oauth2_schema)): 
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username:str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401,detail="Invalid token")
        return username
    except JWTError as e:
        print(e)
        raise HTTPException(status_code=401,detail="Invalid token")


@app.get('/')
def home(user:str = Depends(verify_token)):
    return {"message":f"Welcome {user}","user":user}
