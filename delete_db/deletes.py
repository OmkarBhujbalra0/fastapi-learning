from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.orm import declarative_base,sessionmaker,Session
from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    course: str

DATABASE_URL = 'sqlite:///./test5.db'

engine = create_engine(DATABASE_URL,
                       connect_args={'check_same_thread':False})

Base = declarative_base()

Sessionlocal = sessionmaker(bind=engine)

class Studentschema(Base):
    __tablename__ = 'studentdelete'

    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String,nullable=False)
    course = Column(String,nullable=False)

Base.metadata.create_all(bind=engine)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close() 

@app.get('/')
def home(db:Session = Depends(get_db)):
    return {"CRUD API is setup."}

@app.get('/students')
def display(db:Session = Depends(get_db)):
    student_data = db.query(Studentschema).all()
    return student_data

@app.get('/students/{student_id}')
def search(student_id:int,db:Session = Depends(get_db)):
    student_data = db.query(Studentschema).filter(Studentschema.id == student_id).first()

    if not student_data:
        raise HTTPException(status_code=404,
                            detail="Student not Found")

    return student_data

@app.post('/students')
def inserts(student:Student,db:Session = Depends(get_db)):
    student_data = Studentschema(name=student.name,course=student.course)
    db.add(student_data)
    db.commit()
    db.refresh(student_data)
    return {"message":"Student data added successfully.",
            "data":student_data}

@app.put('/students/{student_id}')
def update(student_id:int, student:Student, db:Session = Depends(get_db)):
    student_data = db.query(Studentschema).filter(Studentschema.id == student_id).first()

    if not student_data:
        raise HTTPException(status_code=404,
                            detail="Student not found")

    student_data.name = student.name
    student_data.course = student.course

    db.commit()
    db.refresh(student_data)
    return {"message":"Details updated successfully.","data":student_data}

@app.delete('/students/{student_id}')
def deletes(student_id:int, db:Session = Depends(get_db)):
    student_data = db.query(Studentschema).filter(Studentschema.id == student_id).first()

    if not student_data:
        raise HTTPException(status_code=404,
                            detail='Student not Found.')

    db.delete(student_data)
    db.commit()
    return {"message":"Details removed successfully.",
            "data":student_data}