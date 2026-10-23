from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.orm import declarative_base,sessionmaker,Session
from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel

app = FastAPI()

class Studentschema(BaseModel):
    name: str
    course: str

DATABASE_URL = 'sqlite:///./test3.db'

engine = create_engine(DATABASE_URL,
                       connect_args={'check_same_thread':False})

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

class Student(Base):
    __tablename__ = 'studentread'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String,nullable=False)
    course = Column(String,nullable=False)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/students')
def inserts(student:Studentschema,db:Session = Depends(get_db)):
    student_data = Student(name=student.name,course=student.course)
    db.add(student_data)
    db.commit()
    db.refresh(student_data)
    return {
        "message":"Student Details Added Successfully.",
        "data":student_data
    }

@app.get('/students')
def display(db:Session = Depends(get_db)):
    student_data = db.query(Student).all()
    return {"message":"List of all the students",
            "data":student_data}

@app.get('/students/{student_id}')
def search(student_id:int,db:Session = Depends(get_db)):
    student_data = db.query(Student).filter(Student.id == student_id).first()
    if not student_data:
        raise HTTPException(status_code=404,detail='Student not Found')

    return student_data