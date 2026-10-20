from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import declarative_base,sessionmaker,Session
from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel

app = FastAPI()

DATABASE_URL = 'sqlite:///./test4.db'

class Student(BaseModel):
    name: str
    course: str

engine = create_engine(DATABASE_URL,
                       connect_args={'check_same_thread':False})

Base = declarative_base()

Sessionlocal = sessionmaker(bind=engine)

class Studentschema(Base):
    __tablename__ = 'studentupdate'

    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String,nullable=True)
    course = Column(String,nullable=True)


Base.metadata.create_all(bind=engine)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def home(db:Session = Depends(get_db)):
    return "SQlAlchemy is setup with update."

@app.get('/students')
def display(db:Session = Depends(get_db)):
    student_data = db.query(Studentschema).all()
    return student_data

@app.get('/students/{student_id}')
def search(student_id:int,db:Session = Depends(get_db)):
    student_data = db.query(Studentschema).filter(Studentschema.id == student_id).first()

    if not student_data:
        raise HTTPException(status_code=404,detail="Student not Found")

    return student_data

@app.post('/students')
def inserts(student:Student,db:Session = Depends(get_db)):
    student_data = Studentschema(name=student.name,course=student.course)
    db.add(student_data)
    db.commit()
    db.refresh(student_data)
    return {
        "message":"Student Details Added Successfully."
    }

@app.put('/students/{student_id}')
def update(student:Student,student_id:int,db:Session = Depends(get_db)):
    student_data = db.query(Studentschema).filter(Studentschema.id == student_id).first()

    if not student_data:
        raise HTTPException(status_code=404,detail="Student not Found")

    student_data.name = student.name
    student_data.course = student.course
    db.commit()
    db.refresh(student_data)
    return {"message":"Student Details Updated Successfully.",
            "data":student_data}