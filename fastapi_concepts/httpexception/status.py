from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    phone_no: int

class Require(BaseModel):
    name: str
    age: int

student_list = []

@app.get('/')
def home():
    return {"message":"Welcome"}

@app.get('/students',response_model=list[Require])
def display():
    return student_list

@app.get('/students/{student_name}',response_model=Require)
def search(student_name:str):
    for i in student_list:
        if i.name == student_name:
            return i
    raise HTTPException(status_code=404,detail="Student not Found")

@app.post('/students',status_code=status.HTTP_201_CREATED)
def adds(student:Student):
    if student not in student_list:
        student_list.append(student)
        return {"message":"Student added successfully."}
    return {"error":"Student already exists."}

@app.put('/students/{student_name}')
def update(student_name:str,new_student:Student):
    for i in student_list:
        if i.name == student_name:
            i.name = new_student.name
            i.age = new_student.age
            i.phone_no = new_student.phone_no
            return {"message":"Student Details updated successfully."}
    raise HTTPException(status_code=404,detail='Student not Found.')

@app.delete('/students/{student_name}')
def deletes(student_name:str):
    for i in student_list:
        if i.name == student_name:
            student_list.remove(i)
            return {"message":"Student details removed successfully."}
    raise HTTPException(status_code=404,detail="Student not Found.")