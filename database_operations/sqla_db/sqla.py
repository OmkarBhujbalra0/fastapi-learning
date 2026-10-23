from sqlalchemy import Column,Integer,String,create_engine
from sqlalchemy.orm import declarative_base,sessionmaker,Session
from fastapi import FastAPI,Depends

app = FastAPI()

DATABASE_URL = 'sqlite:///./test.db'

engine = create_engine(DATABASE_URL,
                       connect_args={"check_same_thread":False})

Sessionlocal = sessionmaker(bind=engine)

Base = declarative_base()

class Intro(Base):
    __tablename__ = "introtable"

    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String,nullable=False)
    age = Column(Integer,nullable=False)

Base.metadata.create_all(bind=engine)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def home(db: Session = Depends(get_db)):
    return {"message":"SQLAlchemy DB is setup."}