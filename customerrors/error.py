from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class Usernotfound(Exception):
    def __init__(self,name):
        self.name = name

@app.exception_handler(Usernotfound)
def usernotfounderror(request:Request,exc:Usernotfound):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message":f"{exc.name} not Found."
        }
    )

class Student(BaseModel):
    name: str
    age:int
    phone_no:int

class Required(BaseModel):
    name: str
    age: int

student_list = []

@app.get('/')
def home():
    return {"message":"Welcome to custom error page."}

@app.get('/students',response_model=list[Required])
def display():
    return student_list

@app.get('/students/{student_name}',response_model=Required)
def search(student_name:str):
    for i in student_list:
        if i.name == student_name:
            return i
    raise Usernotfound(student_name)

@app.post('/students')
def adds(student:Student):
    if student not in student_list:
        student_list.append(student)
        return {"message":"Student Details Added Successfully."}
    return {"error":"Student Details already exists."}

@app.put('/students/{student_name}')
def update(student_name:str,new:Student):
    for i in student_list:
        if i.name == student_name:
            i.name = new.name
            i.age = new.age
            i.phone_no = new.phone_no
            return {"message":"Student Updated Successfully."}
    raise Usernotfound(student_name)

@app.delete('/students/{student_name}')
def deletes(student_name:str):
    for i in student_list:
        if i.name == student_name:
            student_list.remove(i)
            return {"message":"Student Details Removed."}
    raise Usernotfound(student_name)