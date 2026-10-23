from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    branch: str
    course: str
    adhaar_no: int
    age: int

class Required(BaseModel):
    name: str
    branch: str
    course: str
    age: int

student_list = []

@app.get('/')
def home():
    return {"message":"Welcome to Response Model API","desc":"Here we are using Response Model"}

@app.get('/students',response_model=list[Required])
def display():
    return student_list

@app.get('/students/{student_name}',response_model=Required)
def search(student_name:str):
    for i in student_list:
        if i.name == student_name:
            return i
    raise HTTPException(status_code=404,detail='Student not Found')

@app.post('/students')
def adds(student:Student):
    if student not in student_list:
        student_list.append(student)
        return {"message":"Student details added successfully."}
    return {"error":"Student already exists"}

@app.get('/students/{student_name}',response_model=Required)
def search(student_name: str):
    for i in student_list:
        if i.name == student_name:
            return {"Student":i}    
    return {"error":"Student not Found"}

@app.put('/students/{student_name}')
def update(student_name: str,new:Student):
    for i in student_list:
        if i.name == student_name:
            i.name = new.name
            i.course = new.course
            i.branch = new.branch
            i.age = new.age
            i.adhaar_no = new.adhaar_no
            return {"message":"Student Details Updated Successfully."}
    return {"error":"Student not Found"}

@app.delete('/students/{student_name}')
def deletes(student_name:str):
    for i in student_list:
        if i.name == student_name:
            student_list.remove(i)
            return {"message":"Student Details removed Successfully."}
    return {"error":"Student details not found"}