from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import declarative_base,sessionmaker,Session
from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    course: str
    year: str

DATABASE_URL = "sqlite:///./crudtable.db"

engine = create_engine(DATABASE_URL,
                       connect_args={"check_same_thread":False})

Base = declarative_base()

Sessionlocal = sessionmaker(bind=engine)

class Studentschema(Base):
    __tablename__ = "studentable"

    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String,nullable=False)
    course = Column(String,nullable=False)
    year = Column(String,nullable=False)

Base.metadata.create_all(bind=engine)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message":"This API deals with CRUD Operations using Database."}

@app.get('/students')
def display(db:Session = Depends(get_db)):
    student_data = db.query(Studentschema).all()
    return {"message":"List of all students.","data":student_data}

@app.get('/students/{student_id}')
def search(student_id:int,db:Session = Depends(get_db)):
    student_data = db.query(Studentschema).filter(Studentschema.id == student_id).first()

    if not student_data:
        raise HTTPException(status_code=404,
                            detail="Student Details not Found")

    return student_data

@app.post('/students')
def adds(student:Student,db:Session = Depends(get_db)):
    student_data = Studentschema(name=student.name,course=student.course,year=student.year)
    db.add(student_data)
    db.commit()
    db.refresh(student_data)
    return {"message":"Student Details Added Successfully.", "data":student_data}

@app.put('/students/{student_id}')
def update(student_id:int,student:Student,db:Session = Depends(get_db)):
    student_data = db.query(Studentschema).filter(Studentschema.id == student_id).first()

    if not student_data:
        raise HTTPException(status_code=404,detail="Student not Found.")

    student_data.name = student.name
    student_data.course = student.course
    student_data.year = student.year

    db.commit()
    db.refresh(student_data)
    return {"message":"Student Details Updated Successfully.","data":student_data}

@app.delete('/students/{student_id}')
def deletes(student_id:int,db:Session = Depends(get_db)):
    student_data =db.query(Studentschema).filter(Studentschema.id == student_id).first()

    if not student_data:
        raise HTTPException(status_code=404, detail='Student not found.')

    db.delete(student_data)
    db.commit()
    return {"message":"Student Details Removed Successfully.","data":student_data}