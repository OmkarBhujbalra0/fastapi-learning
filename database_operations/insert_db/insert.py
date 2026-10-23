from sqlalchemy import create_engine,Column,Integer, String
from sqlalchemy.orm import declarative_base,sessionmaker,Session
from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()

class Studentdata(BaseModel):
    name:str
    course:str

DATABASE_URL = "sqlite:///./insert.db"

engine = create_engine(DATABASE_URL,
                       connect_args={"check_same_thread":False})

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

class Student(Base):
    __tablename__ = "studentable"

    id = Column(Integer, primary_key=True,autoincrement=True)
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
def inserts(student:Studentdata,db:Session = Depends(get_db)):
    studentdata = Student(name=student.name,course=student.course)
    db.add(studentdata)
    db.commit()
    db.refresh(studentdata)
    return {"message":"Student Details Added Successfully.",
            "data":studentdata}